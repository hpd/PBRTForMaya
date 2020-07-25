import datetime
import os
import math
import platform

import maya.cmds as cmds
import maya.OpenMaya as om

import pymel.core

from process import Process

__author__ = 'Haarm-Pieter Duiker'
__copyright__ = 'Copyright (C) 2016 - Duiker Research Corp'
__license__ = ''
__maintainer__ = 'Haarm-Pieter Duiker'
__email__ = 'support@duikerresearch.org'
__status__ = 'Production'

__major_version__ = '1'
__minor_version__ = '0'
__change_version__ = '0'
__version__ = '.'.join((__major_version__,
                        __minor_version__,
                        __change_version__))

# Will be populated as materials are registered with Maya
materialNodeTypes = []

# Maya-native types that have basic rendering support
mayaMaterialNodeTypes = ["lambert", "phong", "phongE", "blinn"]

#
# IO functions
#
global renderDir
renderDir = None

global exportVerbosity
exportVerbosity = 0

#
# PBRT Scene elements
#
from PBRTScene import *

#
# General functionality
#
def getOperatingEnvironment():
    try:
        user = os.getlogin()
    except:
        try:
            user = os.getenv('USERNAME')
            if user is None:
                user = os.getenv('USER')
        except:
            user = 'unknown_user'
    try:
        (sysname, nodename, release, version, machine,
         processor) = platform.uname()
    except:
        (sysname, nodename, release, version, machine, processor) = (
            'unknown_sysname', 'unknown_nodename', 'unknown_release',
            'unknown_version', 'unknown_machine', 'unknown_processor')

    return (user, sysname, nodename, release, version, 
        machine, processor)

# Returns the surfaceShader node for a piece of geometry (geom)
def getSurfaceShader(geom):
    shapeNode = cmds.listRelatives(geom, children=True, shapes=True, fullPath=True)[0]
    sgs = cmds.listConnections(shapeNode, type="shadingEngine")
    # handles instances
    for sg in sgs:
        objects = cmds.sets(sg, query=True)
        # objects list doesn't contain the full dag path - it's just transform and shape
        # shapeNode is a full path
        # hence, search for object in shapeNode
        matches = [x for x in objects if x in shapeNode]
        if matches:
            break

    shader = cmds.listConnections(sg+".surfaceShader")
    if shader:
        shader = shader[0]
    return shader

def getVolumeShader(geom):
    shapeNode = cmds.listRelatives(geom, children=True, shapes=True, fullPath=True)[0]
    sg = cmds.listConnections(shapeNode, type="shadingEngine")[0]
    shader = cmds.listConnections(sg+".volumeShader")
    if shader:
        shader = shader[0]
    return shader

def getGeometryShader(geom):
    shapeNode = cmds.listRelatives(geom, children=True, shapes=True, fullPath=True)[0]
    sg = cmds.listConnections(shapeNode, type="shadingEngine")[0]
    shader = cmds.listConnections(sg+".displacementShader")
    if shader:
        shader = shader[0]
    return shader

#
# Functions to retrieve parameters, if they are connected to textures or set explicitly
#
def getTextureConnection(material, connectionAttr):
    connections = cmds.listConnections(material, connections=True)
    nodeName = None
    for i in range(len(connections)):
        if i%2==1:
            connection = connections[i]
            connectionType = cmds.nodeType(connection)
            #if( connections[i-1].lower() == (material+"."+connectionAttr).lower() ):
            if( connections[i-1].split('.')[-1].lower() == connectionAttr.lower() ):
                nodeName = connection
                break

    return nodeName

def getTexturePath(nodeName):
    fileTexture = None

    connectionType = cmds.nodeType(nodeName)
    if( connectionType == "file" ):
        connection = nodeName
        fileTexture = cmds.getAttr(connection+".fileTextureName")
        hasFile=True
        #print( "Found texture : %s" % fileTexture )

        animatedTexture = cmds.getAttr("%s.%s" % (connection, "useFrameExtension"))
        if animatedTexture:
            textureFrameNumber = cmds.getAttr("%s.%s" % (connection, "frameExtension"))
            # Should make this an option at some point
            tokens = fileTexture.split('.')
            tokens[-2] = str(textureFrameNumber).zfill(4)
            fileTexture = '.'.join(tokens)
            #print( "Animated texture path : %s" % fileTexture )

    if fileTexture:
        fileTexture = os.path.relpath( fileTexture, renderDir ).replace("\\", "/")

    return fileTexture

def addMappingAttributes(textureElement, texturePlacementNodeName,
    repeatUScale = 1.0, repeatVScale = 1.0):
    # Should support other mappings at some point

    repeatUV = cmds.getAttr("%s.repeatUV" % texturePlacementNodeName )[0]
    offsetUV = cmds.getAttr("%s.offset" % texturePlacementNodeName )[0]

    textureElement.addAttributeString('mapping', 'uv')
    textureElement.addAttributeFloat('uscale', repeatUV[0]*repeatUScale )
    textureElement.addAttributeFloat('vscale', repeatUV[1]*repeatVScale )
    textureElement.addAttributeFloat('udelta', offsetUV[0])
    textureElement.addAttributeFloat('vdelta', offsetUV[1])

def createTextureFile(textureNodeName, dataType='spectrum'):
    texturePath = getTexturePath(textureNodeName)
    textureExtension = os.path.splitext( texturePath )[-1]

    colorSpace = cmds.getAttr("%s.colorSpace" % textureNodeName )
    colorSpace = colorSpace.split(' ')[0]

    if textureExtension in ['.ptx', '.ptex']:
        textureElement = PtexTextureElement(textureNodeName, dataType, texturePath)
    else:
        textureElement = ImageMapTextureElement(textureNodeName, dataType, texturePath)

        addMappingAttributes(textureElement, textureNodeName)

        # PBRT's only colorspace support is 'gamma' on or off

        # Add a rule to cover EXR files
        #  and textureExtension != ".exr":
        if colorSpace == 'sRGB':
            textureElement.addAttributeBoolean('gamma', True)
        else:
            textureElement.addAttributeBoolean('gamma', False)

    return [textureElement]

def createTextureChecker(textureNodeName, dataType='spectrum'):
    texturePlacement = getTextureConnection( textureNodeName, "uvCoord" )

    textureElement = TextureElement(textureNodeName, dataType, 'checkerboard')

    textureElements = []
    addTexturedAttribute(textureNodeName, 'color1', textureElement, 
        textureElements, rendererParameter="tex1", dataType=dataType)
    addTexturedAttribute(textureNodeName, 'color2', textureElement, 
        textureElements, rendererParameter="tex2", dataType=dataType)

    addMappingAttributes(textureElement, texturePlacement,
        repeatUScale=2.0, repeatVScale=2.0)

    # Main texture element
    textureElements.append(textureElement)

    return textureElements

def createTextureFBM(textureNodeName, dataType='spectrum'):
    octaves = cmds.getAttr("%s.octaves" % textureNodeName )
    roughness = cmds.getAttr("%s.roughness" % textureNodeName )
    matrix = cmds.getAttr("%s.placementMatrix" % textureNodeName )

    textureElement = MatrixTextureElement(textureNodeName, dataType, 
        'fbm', matrix)

    textureElement.addAttributeInteger('octaves', octaves)
    textureElement.addAttributeFloat('roughness', roughness)

    return [textureElement]

def createTextureMarble(textureNodeName, dataType='spectrum'):
    octaves = cmds.getAttr("%s.octaves" % textureNodeName )
    roughness = cmds.getAttr("%s.roughness" % textureNodeName )
    noiseScale = cmds.getAttr("%s.noiseScale" % textureNodeName )
    variation = cmds.getAttr("%s.variation" % textureNodeName )
    matrix = cmds.getAttr("%s.placementMatrix" % textureNodeName )

    textureElement = MatrixTextureElement(textureNodeName, dataType, 
        'marble', matrix)

    textureElement.addAttributeInteger('octaves', octaves)
    textureElement.addAttributeFloat('roughness', roughness)
    textureElement.addAttributeFloat('scale', noiseScale)
    textureElement.addAttributeFloat('variation', variation)

    return [textureElement]

def createTextureWindy(textureNodeName, dataType='spectrum'):
    matrix = cmds.getAttr("%s.placementMatrix" % textureNodeName )

    textureElement = MatrixTextureElement(textureNodeName, dataType, 
        'windy', matrix)

    return [textureElement]

def createTextureWrinkled(textureNodeName, dataType='spectrum'):
    octaves = cmds.getAttr("%s.octaves" % textureNodeName )
    roughness = cmds.getAttr("%s.roughness" % textureNodeName )
    matrix = cmds.getAttr("%s.placementMatrix" % textureNodeName )

    textureElement = MatrixTextureElement(textureNodeName, dataType, 
        'wrinkled', matrix)

    textureElement.addAttributeInteger('octaves', octaves)
    textureElement.addAttributeFloat('roughness', roughness)

    return [textureElement]

def createTextureConstant(textureNodeName, dataType='spectrum'):
    textureElements = []

    textureElement = TextureElement(textureNodeName, dataType, 'constant')

    addTexturedAttribute(textureNodeName, 'value', textureElement, textureElements,
        dataType=dataType)

    # Main texture element
    textureElements.append(textureElement)

    return textureElements

def createTextureDotsCloth(textureNodeName, dataType='spectrum'):
    texturePlacement = getTextureConnection( textureNodeName, "uvCoord" )

    textureElement = TextureElement(textureNodeName, dataType, 'dots')

    textureElements = []
    addTexturedAttribute(textureNodeName, 'uColor', textureElement, 
        textureElements, rendererParameter="inside", dataType=dataType)
    addTexturedAttribute(textureNodeName, 'vColor', textureElement, 
        textureElements, rendererParameter="outside", dataType=dataType)

    addMappingAttributes(textureElement, texturePlacement,
        repeatUScale=2.0, repeatVScale=2.0)

    # Main texture element
    textureElements.append(textureElement)

    return textureElements

def createTextureBlackbody(textureNodeName, dataType='blackbody'):
    textureElements = []

    temperature = cmds.getAttr("%s.temperature" % textureNodeName )
    intensity = cmds.getAttr("%s.intensity" % textureNodeName )

    textureElement = TextureElement(textureNodeName, dataType, 'blackbody')
    textureElement.addAttributeFloat('value', [temperature, intensity])

    # Main texture element
    textureElements.append(textureElement)

    return textureElements

def createTextureXYZ(textureNodeName, dataType='xyz'):
    textureElements = []

    preset = cmds.getAttr(textureNodeName+".preset", asString=True)

    # Values from www.poynton.com/notes/color/GretagMacbeth-ColorChecker.html
    presetValues = {
        "D50" : [0.96421, 1.0, 0.82519],
        "D60 - ACES" : [0.95265, 1.0, 1.00883],
        "D65" : [0.9504, 1.0, 1.08887],
        "Illuminant A" : [1.0985, 1.0, 0.3558],
        "Macbeth Patch 1  - Dark Skin" : [0.115428571, 0.101, 0.072142857],
        "Macbeth Patch 2  - Light Skin" : [0.391205797, 0.358, 0.288475362], 
        "Macbeth Patch 3  - Blue Sky" : [0.189924303, 0.193, 0.386], 
        "Macbeth Patch 4  - Foliage" : [00.1062109, 0.133, 0.075954976],
        "Macbeth Patch 5  - Blue Flower" : [0.2683125, 0.243, 0.5011875],
        "Macbeth Patch 6  - Bluish Green" : [0.327962099, 0.431, 0.497597668],
        "Macbeth Patch 7  - Orange" : [0.374216216, 0.301, 0.064341523],
        "Macbeth Patch 8  - Purplish Blue" : [0.144685714, 0.12, 0.421028571],
        "Macbeth Patch 9  - Moderate Red" : [0.293117647, 0.198, 0.155941176],
        "Macbeth Patch 10 - Purple" : [0.093118812, 0.066, 0.167613861],
        "Macbeth Patch 11 - Yellow Green" : [0.344253579, 0.443, 0.118676892],
        "Macbeth Patch 12 - Orange Yellow" : [0.465440639, 0.431, 0.087577626],
        "Macbeth Patch 13 - Blue" : [0.088426357, 0.061, 0.32344186],
        "Macbeth Patch 14 - Green" : [0.149309623, 0.234, 0.106230126],
        "Macbeth Patch 15 - Red" : [0.206645367, 0.12, 0.056741214],
        "Macbeth Patch 16 - Yellow" : [0.56333617, 0.591, 0.103110638],
        "Macbeth Patch 17 - Magenta" : [0.309321888, 0.198, 0.342463519],
        "Macbeth Patch 18 - Cyan" : [0.154, 0.198, 0.433714286],
        "Macbeth Patch 19 - White" : [0.882911392, 0.9, 1.065189873],
        "Macbeth Patch 20 - Neutral 8" : [0.579778481, 0.591, 0.699474684],
        "Macbeth Patch 21 - Neutral 6.5" : [0.355126582, 0.362, 0.428443038],
        "Macbeth Patch 22 - Neutral 5" : [0.194240506, 0.198, 0.234341772],
        "Macbeth Patch 23 - Neutral 3.5" : [0.088291139, 0.09, 0.106518987],
        "Macbeth Patch 24 - Black" : [0.030411392, 0.031, 0.036689873]
    }

    if preset != "None" and preset in presetValues:
        value = presetValues[preset]
    else:
        value = cmds.getAttr("%s.value" % textureNodeName )[0]

    textureElement = TextureElement(textureNodeName, dataType, 'xyz')
    textureElement.addAttributeFloat('value', value)

    # Main texture element
    textureElements.append(textureElement)

    return textureElements

def createTextureXYY(textureNodeName, dataType='xyz'):
    textureElements = []

    preset = cmds.getAttr(textureNodeName+".preset", asString=True)

    # Values from www.poynton.com/notes/color/GretagMacbeth-ColorChecker.html
    presetValues = {
        "D50" : [0.34567, 0.35850, 1.0],
        "D60 - ACES" : [0.32168, 0.33767, 1.0],
        "D65" : [0.31272, 0.32902, 1.0],
        "Illuminant A" : [0.44757, 0.40745, 1.0],
        "Macbeth Patch 1  - Dark Skin" : [0.400, 0.350, 0.101],
        "Macbeth Patch 2  - Light Skin" : [0.377, 0.345, 0.358], 
        "Macbeth Patch 3  - Blue Sky" : [0.247, 0.251, 0.193], 
        "Macbeth Patch 4  - Foliage" : [0.337, 0.422, 0.133],
        "Macbeth Patch 5  - Blue Flower" : [0.265, 0.24, 0.243],
        "Macbeth Patch 6  - Bluish Green" : [0.261, 0.343, 0.431],
        "Macbeth Patch 7  - Orange" : [0.506, 0.407, 0.301],
        "Macbeth Patch 8  - Purplish Blue" : [0.211, 0.175, 0.12],
        "Macbeth Patch 9  - Moderate Red" : [0.453, 0.306, 0.198],
        "Macbeth Patch 10 - Purple" : [0.285, 0.202, 0.066],
        "Macbeth Patch 11 - Yellow Green" : [0.38, 0.489, 0.443],
        "Macbeth Patch 12 - Orange Yellow" : [0.473, 0.438, 0.431],
        "Macbeth Patch 13 - Blue" : [0.187, 0.129, 0.061],
        "Macbeth Patch 14 - Green" : [0.305, 0.478, 0.234],
        "Macbeth Patch 15 - Red" : [0.539, 0.313, 0.12],
        "Macbeth Patch 16 - Yellow" : [0.448, 0.47, 0.591],
        "Macbeth Patch 17 - Magenta" : [0.364, 0.233, 0.198],
        "Macbeth Patch 18 - Cyan" : [0.196, 0.252, 0.198],
        "Macbeth Patch 19 - White" : [0.31, 0.316, 0.90],
        "Macbeth Patch 20 - Neutral 8" : [0.31, 0.316, 0.591],
        "Macbeth Patch 21 - Neutral 6.5" : [0.31, 0.316, 0.362],
        "Macbeth Patch 22 - Neutral 5" : [0.31, 0.316, 0.198],
        "Macbeth Patch 23 - Neutral 3.5" : [0.31, 0.316, 0.09],
        "Macbeth Patch 24 - Black" : [0.31, 0.316, 0.031]
    }

    if preset != "None" and preset in presetValues:
        value = presetValues[preset]
    else:
        value = cmds.getAttr("%s.value" % textureNodeName )[0]

    # xyY to XYZ
    Y = value[2]
    X = value[0]*Y/value[1]
    Z = (1 - value[0] - value[1])*Y/value[1]

    textureElement = TextureElement(textureNodeName, dataType, 'xyz')
    textureElement.addAttributeFloat('value', (X, Y, Z))

    # Main texture element
    textureElements.append(textureElement)

    return textureElements

def createTextureUV(textureNodeName, dataType='spectrum'):
    texturePlacement = cmds.listConnections( "%s.uv" % textureNodeName )[0]

    textureElement = TextureElement(textureNodeName, dataType, 'uv')

    addMappingAttributes(textureElement, texturePlacement)

    return [textureElement]

def createTextureBilerp(textureNodeName, dataType='spectrum'):
    textureElements = []

    textureElement = TextureElement(textureNodeName, dataType, 'bilerp')

    addTexturedAttribute(textureNodeName, 'value00', textureElement, textureElements,
        dataType=dataType, rendererParameter='v00')
    addTexturedAttribute(textureNodeName, 'value01', textureElement, textureElements,
        dataType=dataType, rendererParameter='v01')
    addTexturedAttribute(textureNodeName, 'value10', textureElement, textureElements,
        dataType=dataType, rendererParameter='v10')
    addTexturedAttribute(textureNodeName, 'value11', textureElement, textureElements,
        dataType=dataType, rendererParameter='v11')

    # Main texture element
    textureElements.append(textureElement)

    return textureElements

def createTextureMix(textureNodeName, dataType='spectrum'):
    textureElements = []

    textureElement = TextureElement(textureNodeName, dataType, 'mix')

    addTexturedFloatAttribute(textureNodeName, 'Amount', textureElement, textureElements,
        rendererParameter='amount')
    addTexturedAttribute(textureNodeName, 'Texture1', textureElement, textureElements,
        rendererParameter='tex1', dataType=dataType)
    addTexturedAttribute(textureNodeName, 'Texture2', textureElement, textureElements,
        rendererParameter='tex2', dataType=dataType)

    # Main texture element
    textureElements.append(textureElement)

    return textureElements

def createTextureScale(textureNodeName, dataType='spectrum'):
    textureElements = []

    textureElement = TextureElement(textureNodeName, dataType, 'scale')

    addTexturedAttribute(textureNodeName, 'Texture1', textureElement, textureElements,
        rendererParameter='tex1', dataType=dataType)
    addTexturedAttribute(textureNodeName, 'Texture2', textureElement, textureElements,
        rendererParameter='tex2', dataType=dataType)

    # Main texture element
    textureElements.append(textureElement)

    return textureElements

def createTexture(material, attribute, dataType='spectrum'):
    textureElements = []

    textureName = getTextureConnection(material, attribute)
    if textureName:
        textureType = cmds.nodeType(textureName)
    
        mayaTypeToCreateFunction = {
            "checker" : createTextureChecker,
            "PBRTConstantTexture" : createTextureConstant,
            "cloth" : createTextureDotsCloth,
            "PBRTFBMTexture" : createTextureFBM,
            "file" : createTextureFile,
            "PBRTMixTexture" : createTextureMix,
            "PBRTScaleTexture" : createTextureScale,
            "PBRTMarbleTexture" : createTextureMarble,
            "PBRTWindyTexture" : createTextureWindy,
            "PBRTWrinkledTexture" : createTextureWrinkled,
            "PBRTBlackBody" : createTextureBlackbody,
            "PBRTxyz" : createTextureXYZ,
            "PBRTxyY" : createTextureXYY,
            "PBRTuv" : createTextureUV,
            "PBRTBilerpTexture" : createTextureBilerp,
        }

        if textureType in mayaTypeToCreateFunction:
            if exportVerbosity:
                print( "Creating texture : %s, type  : %s." % (textureName, textureType) )
            createFunction = mayaTypeToCreateFunction[textureType]
        else:
            if exportVerbosity:
                print( "Skipping unsupported texture : %s." % textureType)
            createFunction = None

        if createFunction:
            textureElements = createFunction(textureName, dataType=dataType)

    return textureElements

#
# Textured attribute handling
#
def TexturedColorAttributeElement(material, attribute, rendererParameter=None):
    if not rendererParameter:
        rendererParameter = attribute

    textureElements = createTexture(material, attribute, dataType='spectrum')
    if textureElements:
        # Check if texture is a .spd file, xyz or blackbody node
        textureType = 'image'
        textureElement = textureElements[-1]
        if textureElement.texturePlugin == 'imagemap':
            fileName = textureElement.attributes['filename']['value']
            extension = os.path.splitext(fileName)[-1][1:-1]
            if extension == 'spd':
                textureType = 'spd'
        elif textureElement.texturePlugin == 'blackbody':
            textureType = 'blackbody'
        elif textureElement.texturePlugin == 'xyz':
            textureType = 'xyz'

        if textureType == 'spd':
            paramType = 'spectrum'
            paramValue = fileName
            textureElements = []
        elif textureType == 'blackbody':
            powerIntensity = textureElement.attributes['value']['value']
            paramType = 'blackbody'
            paramValue = powerIntensity
            textureElements = []
        elif textureType == 'xyz':
            value = textureElement.attributes['value']['value']
            paramType = 'xyz'
            paramValue = value
            textureElements = []
        else:
            paramType = 'texture'
            paramValue = textureElements[-1]['plugin']
    else:
        value = cmds.getAttr(material + "." + attribute)
        paramType = 'rgb'
        paramValue = value[0]
        textureElements = []

    return (paramType, paramValue, textureElements)

def TexturedFloatAttributeElement(material, attribute, rendererParameter=None):
    if not rendererParameter:
        rendererParameter = attribute

    textureElements = createTexture(material, attribute, dataType='float')
    if textureElements:
        paramType = 'texture'
        paramValue = textureElements[-1]['plugin']
        textureElements[-1].pixelType = 'float'
    else:
        value = cmds.getAttr(material + "." + attribute)
        paramType = 'float'
        paramValue = value
        textureElements = []

    return (paramType, paramValue, textureElements)

def TexturedAttributeElement(material, attribute, dataType='spectrum', 
    rendererParameter=None):

    if dataType == 'float':
        (paramType, paramValue, textureElements) = TexturedFloatAttributeElement(
            material, attribute, rendererParameter=rendererParameter)
    else:
        (paramType, paramValue, textureElements) = TexturedColorAttributeElement(
            material, attribute, rendererParameter=rendererParameter)

    return (paramType, paramValue, textureElements)

def addTexturedColorAttribute(material, attribute, 
    materialElement, textureElements,
    rendererParameter=None):
    (paramType,
     paramValue,
     paramTextureElements) = TexturedColorAttributeElement(material, attribute)

    if not rendererParameter:
        rendererParameter = attribute

    if paramType == 'texture':
        textureElements.extend(paramTextureElements)
        materialElement.addAttributeTexture(rendererParameter, paramValue)
    elif paramType == 'spectrum':
        materialElement.addAttributeSpectrum(rendererParameter, paramValue)        
    elif paramType == 'blackbody':
        materialElement.addAttributeBlackBody(rendererParameter, paramValue)        
    elif paramType == 'xyz':
        materialElement.addAttributeXYZ(rendererParameter, paramValue)        
    else:
        materialElement.addAttributeRGB(rendererParameter, paramValue)

def addTexturedFloatAttribute(material, attribute, 
    materialElement, textureElements, noDefault=False,
    rendererParameter=None):
    (paramType,
     paramValue,
     paramTextureElements) = TexturedFloatAttributeElement(material, attribute)

    if not rendererParameter:
        rendererParameter = attribute

    if paramType == 'texture':
        textureElements.extend(paramTextureElements)
        materialElement.addAttributeTexture(rendererParameter, paramValue)
    else:
        if not noDefault or int(paramValue) != -1:
            materialElement.addAttributeFloat(rendererParameter, paramValue)

def addTexturedAttribute(material, attribute, 
    materialElement, textureElements,
    rendererParameter=None, dataType='spectrum'):
    (paramType,
     paramValue,
     paramTextureElements) = TexturedAttributeElement(material, attribute,
        dataType=dataType)

    if not rendererParameter:
        rendererParameter = attribute

    if paramType == 'texture':
        textureElements.extend(paramTextureElements)
        materialElement.addAttributeTexture(rendererParameter, paramValue)
    elif paramType == 'spectrum':
        materialElement.addAttributeSpectrum(rendererParameter, paramValue)        
    elif paramType == 'blackbody':
        materialElement.addAttributeBlackBody(rendererParameter, paramValue)        
    elif paramType == 'xyz':
        materialElement.addAttributeXYZ(rendererParameter, paramValue)        
    elif paramType == 'float':
        value = paramValue[0]
        # Handle case where the Maya parameter is a color but we only
        # need a float value
        if type(value) is list or type(value) is tuple:
            materialElement.addAttributeFloat(rendererParameter, value[0])        
        else:
            materialElement.addAttributeFloat(rendererParameter, value)        
    else:
        materialElement.addAttributeRGB(rendererParameter, paramValue)

#
# Create the integrator
#
def createIntegratorPathTracer(renderSettings):
    PBRTVersion = cmds.getAttr("%s.%s" % (renderSettings, "PBRTVersion"))

    integratorPathMaxDepth = cmds.getAttr("%s.%s" % (renderSettings, "integratorPathMaxDepth"))
    integratorPathRRThreshold = cmds.getAttr("%s.%s" % (renderSettings, "integratorPathRRThreshold"))
    integratorPathLightSampleStrategy = cmds.getAttr("%s.%s" % (renderSettings, "integratorPathLightSampleStrategy"))
 
    mayaUINameToRendererName = {
        "Uniform" : "uniform",
        "Power" : "power",
        "Spatial" : "spatial",
    }

    if integratorPathLightSampleStrategy in mayaUINameToRendererName:
        integratorPathLightSampleStrategyRenderer = mayaUINameToRendererName[integratorPathLightSampleStrategy]
    else:
        integratorPathLightSampleStrategyRenderer = "spatial"

    integratorElement = SceneElement("Integrator", "path")
    integratorElement.addAttributeInteger("maxdepth", integratorPathMaxDepth)

    if PBRTVersion != "v3 Book":
        integratorElement.addAttributeFloat("rrthreshold", integratorPathRRThreshold)
        integratorElement.addAttributeString("lightsamplestrategy", integratorPathLightSampleStrategyRenderer)

    return integratorElement

def createIntegratorBidirectionalPathTracer(renderSettings):
    PBRTVersion = cmds.getAttr("%s.%s" % (renderSettings, "PBRTVersion"))

    integratorBidirectionalPathMaxDepth = cmds.getAttr("%s.%s" % (renderSettings, "integratorBidirectionalPathMaxDepth"))
    integratorBidirectionalPathVisualizeStrategies = cmds.getAttr("%s.%s" % (renderSettings, "integratorBidirectionalPathVisualizeStrategies"))
    integratorBidirectionalPathVisualizeWeights = cmds.getAttr("%s.%s" % (renderSettings, "integratorBidirectionalPathVisualizeWeights"))
    integratorBidirectionalPathLightSampleStrategy = cmds.getAttr("%s.%s" % (renderSettings, "integratorBidirectionalPathLightSampleStrategy"))
 
    mayaUINameToRendererName = {
        "Uniform" : "uniform",
        "Power" : "power",
        "Spatial" : "spatial",
    }

    if integratorBidirectionalPathLightSampleStrategy in mayaUINameToRendererName:
        integratorBidirectionalPathLightSampleStrategyRenderer = mayaUINameToRendererName[integratorBidirectionalPathLightSampleStrategy]
    else:
        integratorBidirectionalPathLightSampleStrategyRenderer = "spatial"

    integratorElement = SceneElement("Integrator", "bdpt")
    integratorElement.addAttributeInteger("maxdepth", integratorBidirectionalPathMaxDepth)

    if PBRTVersion != "v3 Book":
        integratorElement.addAttributeBoolean("visualizestrategies", integratorBidirectionalPathVisualizeStrategies)
        integratorElement.addAttributeBoolean("visualizeweights", integratorBidirectionalPathVisualizeWeights)
        integratorElement.addAttributeString("lightsamplestrategy", integratorBidirectionalPathLightSampleStrategyRenderer)

    return integratorElement

def createIntegratorDirectLighting(renderSettings):
    integratorDirectLightingMaxDepth = cmds.getAttr("%s.%s" % (renderSettings, "integratorDirectLightingMaxDepth"))
    integratorDirectLightingStrategy = cmds.getAttr("%s.%s" % (renderSettings, "integratorDirectLightingStrategy"))
 
    mayaUINameToRendererName = {
        "One" : "one",
        "All" : "all",
    }

    if integratorDirectLightingStrategy in mayaUINameToRendererName:
        integratorDirectLightingStrategyRenderer = mayaUINameToRendererName[integratorDirectLightingStrategy]
    else:
        integratorDirectLightingStrategyRenderer = "spatial"

    integratorElement = SceneElement("Integrator", "directlighting")
    integratorElement.addAttributeInteger("maxdepth", integratorDirectLightingMaxDepth)
    integratorElement.addAttributeString("strategy", integratorDirectLightingStrategyRenderer)

    return integratorElement

def createIntegratorMetropolisLightTransport(renderSettings):
    integratorMetropolisLightTransportMaxDepth = cmds.getAttr("%s.%s" % (renderSettings, "integratorMetropolisLightTransportMaxDepth"))
    integratorMetropolisLightTransportBootstrapSamples = cmds.getAttr("%s.%s" % (renderSettings, "integratorMetropolisLightTransportBootstrapSamples"))
    integratorMetropolisLightTransportChains = cmds.getAttr("%s.%s" % (renderSettings, "integratorMetropolisLightTransportChains"))
    integratorMetropolisLightTransportMutationsPerPixel = cmds.getAttr("%s.%s" % (renderSettings, "integratorMetropolisLightTransportMutationsPerPixel"))
    integratorMetropolisLightTransportLargeStepProbability = cmds.getAttr("%s.%s" % (renderSettings, "integratorMetropolisLightTransportLargeStepProbability"))
    integratorMetropolisLightTransportSigma = cmds.getAttr("%s.%s" % (renderSettings, "integratorMetropolisLightTransportSigma"))

    integratorElement = SceneElement("Integrator", "mlt")
    integratorElement.addAttributeInteger("maxdepth", integratorMetropolisLightTransportMaxDepth)
    integratorElement.addAttributeInteger("bootstrapsamples", integratorMetropolisLightTransportBootstrapSamples)
    integratorElement.addAttributeInteger("chains", integratorMetropolisLightTransportChains)
    integratorElement.addAttributeInteger("mutationsperpixel", integratorMetropolisLightTransportMutationsPerPixel)
    integratorElement.addAttributeFloat("largestepprobability", integratorMetropolisLightTransportLargeStepProbability)
    integratorElement.addAttributeFloat("sigma", integratorMetropolisLightTransportSigma)

    return integratorElement

def createIntegratorStochasticProgressivePhotonMap(renderSettings):
    integratorStochasticProgressivePhotonMapNumIterations = cmds.getAttr("%s.%s" % (renderSettings, "integratorStochasticProgressivePhotonMapNumIterations"))
    integratorStochasticProgressivePhotonMapMaxDepth = cmds.getAttr("%s.%s" % (renderSettings, "integratorStochasticProgressivePhotonMapMaxDepth"))
    integratorStochasticProgressivePhotonMapPhotonsPerIteration = cmds.getAttr("%s.%s" % (renderSettings, "integratorStochasticProgressivePhotonMapPhotonsPerIteration"))
    integratorStochasticProgressivePhotonMapImageWriteFrequency = cmds.getAttr("%s.%s" % (renderSettings, "integratorStochasticProgressivePhotonMapImageWriteFrequency"))
    integratorStochasticProgressivePhotonMapRadius = cmds.getAttr("%s.%s" % (renderSettings, "integratorStochasticProgressivePhotonMapRadius"))

    integratorElement = SceneElement("Integrator", "sppm")
    integratorElement.addAttributeInteger("numiterations", integratorStochasticProgressivePhotonMapNumIterations)
    integratorElement.addAttributeInteger("maxdepth", integratorStochasticProgressivePhotonMapMaxDepth)
    integratorElement.addAttributeInteger("photonsperiteration", integratorStochasticProgressivePhotonMapPhotonsPerIteration)
    integratorElement.addAttributeInteger("imagewritefrequency", integratorStochasticProgressivePhotonMapImageWriteFrequency)
    integratorElement.addAttributeFloat("radius", integratorStochasticProgressivePhotonMapRadius)

    return integratorElement

def createIntegratorVolumetricPathTracer(renderSettings):
    PBRTVersion = cmds.getAttr("%s.%s" % (renderSettings, "PBRTVersion"))

    integratorVolumetricPathMaxDepth = cmds.getAttr("%s.%s" % (renderSettings, "integratorVolumetricPathMaxDepth"))
    integratorVolumetricPathRRThreshold = cmds.getAttr("%s.%s" % (renderSettings, "integratorVolumetricPathRRThreshold"))
    integratorVolumetricPathLightSampleStrategy = cmds.getAttr("%s.%s" % (renderSettings, "integratorVolumetricPathLightSampleStrategy"))
 
    mayaUINameToRendererName = {
        "Uniform" : "uniform",
        "Power" : "power",
        "Spatial" : "spatial",
    }

    if integratorVolumetricPathLightSampleStrategy in mayaUINameToRendererName:
        integratorVolumetricPathLightSampleStrategyRenderer = mayaUINameToRendererName[integratorVolumetricPathLightSampleStrategy]
    else:
        integratorVolumetricPathLightSampleStrategyRenderer = "spatial"

    integratorElement = SceneElement("Integrator", "volpath")
    integratorElement.addAttributeInteger("maxdepth", integratorVolumetricPathMaxDepth)

    if PBRTVersion != "v3 Book":
        integratorElement.addAttributeFloat("rrthreshold", integratorVolumetricPathRRThreshold)
        integratorElement.addAttributeString("lightsamplestrategy", integratorVolumetricPathLightSampleStrategyRenderer)

    return integratorElement

def createIntegratorWhitted(renderSettings):
    integratorWhittedMaxDepth = cmds.getAttr("%s.%s" % (renderSettings, "integratorWhittedMaxDepth"))

    integratorElement = SceneElement("Integrator", "whitted")
    integratorElement.addAttributeInteger("maxdepth", integratorWhittedMaxDepth)

    return integratorElement

def createIntegrator(renderSettings):
    # Filter
    integratorMaya = cmds.getAttr("%s.%s" % (renderSettings, "integrator")).replace('_' ,' ')
    mayaUINameToRendererName = {
        "Path Tracer" : "path",
        "Bidirectional Path Tracer" : "bdpt",
        "Direct Lighting" : "directlighting",
        "Metropolis Light Transport" : "mlt",
        "Stochastic Progressive Photon Map" : "sppm",
        "Volumetric Path Tracer" : "volpath",
        "Whitted Path Tracer" : "whitted",
    }

    if integratorMaya in mayaUINameToRendererName:
        integratorRenderer = mayaUINameToRendererName[integratorMaya]
    else:
        integratorRenderer = "path"

    mayaUINameToCreateFunction = {
        "Path Tracer" : createIntegratorPathTracer,
        "Bidirectional Path Tracer" : createIntegratorBidirectionalPathTracer,
        "Direct Lighting" : createIntegratorDirectLighting,
        "Metropolis Light Transport" : createIntegratorMetropolisLightTransport,
        "Stochastic Progressive Photon Map" : createIntegratorStochasticProgressivePhotonMap,
        "Volumetric Path Tracer" : createIntegratorVolumetricPathTracer,
        "Whitted Path Tracer" : createIntegratorWhitted,
    }

    if integratorMaya in mayaUINameToCreateFunction:
        createFunction = mayaUINameToCreateFunction[integratorMaya]
    else:
        if exportVerbosity:
            print( "Unsupported Accelerator : %s. Using Path Tracer" % integratorMaya)
        createFunction = createIntegratorPathTracer

    integratorElement = createFunction(renderSettings)

    return integratorElement

#
# Create the accelerator
#
def createAcceleratorKDTree(renderSettings):
    acceleratorKDTreeIntersectCost = cmds.getAttr("%s.%s" % (renderSettings, "acceleratorKDTreeIntersectCost"))
    acceleratorKDTreeTraversalCost = cmds.getAttr("%s.%s" % (renderSettings, "acceleratorKDTreeTraversalCost"))
    acceleratorKDTreeEmptyBonus = cmds.getAttr("%s.%s" % (renderSettings, "acceleratorKDTreeEmptyBonus"))
    acceleratorKDTreeMaxPrims = cmds.getAttr("%s.%s" % (renderSettings, "acceleratorKDTreeMaxPrims"))
    acceleratorKDTreeMaxDepth = cmds.getAttr("%s.%s" % (renderSettings, "acceleratorKDTreeMaxDepth"))

    acceleratorElement = SceneElement("Accelerator", 'kdtree')

    acceleratorElement.addAttributeInteger("intersectcost", acceleratorKDTreeIntersectCost)
    acceleratorElement.addAttributeInteger("traversalcost", acceleratorKDTreeTraversalCost)
    acceleratorElement.addAttributeFloat("emptybonus", acceleratorKDTreeEmptyBonus)
    acceleratorElement.addAttributeInteger("maxprims", acceleratorKDTreeMaxPrims)
    acceleratorElement.addAttributeInteger("maxdepth", acceleratorKDTreeMaxDepth)

    return acceleratorElement

def createAcceleratorBVH(renderSettings):
    acceleratorBVHSplitMethodMaya = cmds.getAttr("%s.%s" % (renderSettings, "acceleratorBVHSplitMethod"))
    acceleratorBVHMaxNodePrims = cmds.getAttr("%s.%s" % (renderSettings, "acceleratorBVHMaxNodePrims"))
 
    mayaUINameToRendererName = {
        "SAH" : "sah",
        "HLBVH" : "hlbvh",
        "Middle" : "middle",
        "Equal" : "equal",
    }

    if acceleratorBVHSplitMethodMaya in mayaUINameToRendererName:
        acceleratorBVHSplitMethodRenderer = mayaUINameToRendererName[acceleratorBVHSplitMethodMaya]
    else:
        acceleratorBVHSplitMethodRenderer = "sah"

    acceleratorElement = SceneElement("Accelerator", "bvh")
    acceleratorElement.addAttributeString("splitmethod", acceleratorBVHSplitMethodRenderer)
    acceleratorElement.addAttributeInteger("maxnodeprims", acceleratorBVHMaxNodePrims)

    return acceleratorElement

def createAccelerator(renderSettings):
    # Filter
    acceleratorMaya = cmds.getAttr("%s.%s" % (renderSettings, "accelerator")).replace('_' ,' ')
    mayaUINameToRendererName = {
        "KD Tree" : "kdtree",
        "BVH" : "bvh",
    }

    if acceleratorMaya in mayaUINameToRendererName:
        acceleratorRenderer = mayaUINameToRendererName[acceleratorMaya]
    else:
        acceleratorRenderer = "bvh"

    mayaUINameToCreateFunction = {
        "KD Tree" : createAcceleratorKDTree,
        "BVH" : createAcceleratorBVH,
    }

    if acceleratorMaya in mayaUINameToCreateFunction:
        createFunction = mayaUINameToCreateFunction[acceleratorMaya]
    else:
        if exportVerbosity:
            print( "Unsupported Accelerator : %s. Using BVH" % acceleratorMaya)
        createFunction = createAcceleratorBVH

    acceleratorElement = createFunction(renderSettings)

    return acceleratorElement

#
# Create image sample generator
#
def createSamplerGeneric(renderSettings, samplerRenderer):
    pixelSamples = cmds.getAttr("%s.%s" % (renderSettings, "samplerPixelSamples"))

    samplerElement = SceneElement("Sampler", samplerRenderer)
    samplerElement.addAttributeInteger("pixelsamples", pixelSamples)

    return samplerElement

def createSamplerHalton(renderSettings):
    samplerElement = createSamplerGeneric(renderSettings, 'halton')
    return samplerElement

def createSamplerMaxMin(renderSettings):
    samplerElement = createSamplerGeneric(renderSettings, 'maxmindist')

    samplerMaxMinDimensions = cmds.getAttr("%s.%s" % (renderSettings, "samplerMaxMinDimensions"))
    samplerElement.addAttributeInteger("dimensions", samplerMaxMinDimensions)

    return samplerElement

def createSampleRandom(renderSettings):
    samplerElement = createSamplerGeneric(renderSettings, 'random')
    return samplerElement

def createSamplerSobol(renderSettings):
    samplerElement = createSamplerGeneric(renderSettings, 'sobol')
    return samplerElement

def createSamplerStratified(renderSettings):
    samplerStratifedJitter = cmds.getAttr("%s.%s" % (renderSettings, "samplerStratifedJitter"))
    samplerStratifedXSamples = cmds.getAttr("%s.%s" % (renderSettings, "samplerStratifedXSamples"))
    samplerStratifedYSamples = cmds.getAttr("%s.%s" % (renderSettings, "samplerStratifedYSamples"))
    samplerStratifedDimensions = cmds.getAttr("%s.%s" % (renderSettings, "samplerStratifedDimensions"))

    samplerElement = SceneElement("Sampler", 'stratified')

    samplerElement.addAttributeBoolean("jitter", samplerStratifedJitter)
    samplerElement.addAttributeInteger("xsamples", samplerStratifedXSamples)
    samplerElement.addAttributeInteger("ysamples", samplerStratifedYSamples)
    samplerElement.addAttributeInteger("dimensions", samplerStratifedDimensions)

    return samplerElement

def createSamplerLowDiscrepancy(renderSettings):
    samplerElement = createSamplerGeneric(renderSettings, 'lowdiscrepancy')

    samplerLowDiscrepancyDimensions = cmds.getAttr("%s.%s" % (renderSettings, "samplerLowDiscrepancyDimensions"))
    samplerElement.addAttributeInteger("dimensions", samplerLowDiscrepancyDimensions)

    return samplerElement

def createSampler(renderSettings):
    # Filter
    samplerMaya = cmds.getAttr("%s.%s" % (renderSettings, "sampler")).replace('_' ,' ')
    mayaUINameToRendererName = {
        "Halton" : "halton",
        "Max Min" : "maxmindist",
        "Random" : "random",
        "Sobol" : "sobol",
        "Stratified" : "stratified",
        "Low Discrepancy" : "lowdiscrepancy",
    }

    if samplerMaya in mayaUINameToRendererName:
        samplerRenderer = mayaUINameToRendererName[samplerMaya]
    else:
        samplerRenderer = "lowdiscrepancy"

    mayaUINameToCreateFunction = {
        "Halton" : createSamplerHalton,
        "Max Min" : createSamplerMaxMin,
        "Random" : createSampleRandom,
        "Sobol" : createSamplerSobol,
        "Stratified" : createSamplerStratified,
        "Low Discrepancy" : createSamplerLowDiscrepancy,
    }

    if samplerMaya in mayaUINameToCreateFunction:
        createFunction = mayaUINameToCreateFunction[samplerMaya]
    else:
        if exportVerbosity:
            print( "Unsupported Sampler : %s. Using Low Discrepancy" % samplerMaya)
        createFunction = createSamplerLowDiscrepancy

    samplerElement = createFunction(renderSettings)

    return samplerElement

#
# Create pixel filter
#
def createFilterGeneric(renderSettings, reconstructionFilterRenderer):
    filterXWidth = cmds.getAttr("%s.%s" % (renderSettings, "filterXWidth"))
    filterYWidth = cmds.getAttr("%s.%s" % (renderSettings, "filterYWidth"))

    filterElement = SceneElement("PixelFilter", reconstructionFilterRenderer)
    filterElement.addAttributeFloat("xwidth", filterXWidth)
    filterElement.addAttributeFloat("ywidth", filterYWidth)

    return filterElement

def createFilterBox(renderSettings):
    return createFilterGeneric(renderSettings, 'box')

def createFilterGaussian(renderSettings):
    filterAlpha = cmds.getAttr("%s.%s" % (renderSettings, "filterAlpha"))

    filterElement = createFilterGeneric(renderSettings, 'gaussian')
    filterElement.addAttributeFloat("alpha", filterAlpha)

    return filterElement

def createFilterMitchell(renderSettings):
    filterB = cmds.getAttr("%s.%s" % (renderSettings, "filterB"))
    filterC = cmds.getAttr("%s.%s" % (renderSettings, "filterC"))

    filterElement = createFilterGeneric(renderSettings, 'mitchell')
    filterElement.addAttributeFloat("B", filterB)
    filterElement.addAttributeFloat("C", filterC)

    return filterElement

def createFilterSinc(renderSettings):
    filterTau = cmds.getAttr("%s.%s" % (renderSettings, "filterTau"))

    filterElement = createFilterGeneric(renderSettings, 'sinc')
    filterElement.addAttributeFloat("tau", filterTau)

    return filterElement

def createFilterTriangle(renderSettings):
    return createFilterGeneric(renderSettings, 'triangle')

def createFilter(renderSettings):
    # Filter
    filterMaya = cmds.getAttr("%s.%s" % (renderSettings, "filter")).replace('_' ,' ')
    mayaUINameToRendererName = {
        "Box"  : "box",
        "Gaussian" : "gaussian",
        "Mitchell" : "mitchell",
        "Sinc" : "sinc",
        "Triangle" : "triangle",
    }

    if filterMaya in mayaUINameToRendererName:
        filterRenderer = mayaUINameToRendererName[filterMaya]
    else:
        filterRenderer = "box"

    mayaUINameToFilterFunction = {
        "Box"  : createFilterBox,
        "Gaussian" : createFilterGaussian,
        "Mitchell" : createFilterMitchell,
        "Sinc" : createFilterSinc,
        "Triangle" : createFilterTriangle,
    }

    if filterMaya in mayaUINameToFilterFunction:
        createFilterFunction = mayaUINameToFilterFunction[filterMaya]
    else:
        if exportVerbosity:
            print( "Unsupported Filter : %s. Using Box" % filterMaya)
        createFilterFunction = createBoxFilter

    filterElement = createFilterFunction(renderSettings)

    return filterElement

#
# Create film
#
def createFilmImage(renderSettings):
    filmElement = FilmElement('image')

    PBRTVersion = cmds.getAttr("%s.%s" % (renderSettings, "PBRTVersion"))
    existingFilmMaxSampleLuminance = cmds.getAttr("%s.%s" % (renderSettings, "filmMaxSampleLuminance"))
    existingFilmScale = cmds.getAttr("%s.%s" % (renderSettings, "filmScale"))

    filmElement.addAttributeFloat('scale', existingFilmScale)

    if PBRTVersion != "v3 Book":
        if existingFilmMaxSampleLuminance > 0.0:
            filmElement.addAttributeFloat('maxsampleluminance', existingFilmMaxSampleLuminance)

    # Find renderable camera
    rCamShape = getRenderableCamera()

    # Sensor size, width, height, diagonal
    sensorSizeX = cmds.getAttr(rCamShape+".horizontalFilmAperture")
    sensorSizeY = cmds.getAttr(rCamShape+".verticalFilmAperture")

    sensorSizeXMM = sensorSizeX*2.54*10
    sensorSizeYMM = sensorSizeY*2.54*10

    sensorDiagonalMM = math.sqrt(sensorSizeXMM*sensorSizeXMM + sensorSizeYMM*sensorSizeYMM)

    filmElement.addAttributeFloat('diagonal', sensorDiagonalMM)

    return filmElement

def addRenderRegionCropCoordinates(filmElement):
    editor = cmds.renderWindowEditor(q=True, editorName=True )
    #print( "addRenderRegionCropCoordinates - editor : %s" % editor )
    if editor:
        renderRegion = cmds.renderWindowEditor(editor, q=True, mq=True)
        #print( "addRenderRegionCropCoordinates - render region : %s" % renderRegion )
        if renderRegion:
            left = cmds.getAttr( "defaultRenderGlobals.left" )
            right = cmds.getAttr( "defaultRenderGlobals.rght" )
            top = cmds.getAttr( "defaultRenderGlobals.top" )
            bottom = cmds.getAttr( "defaultRenderGlobals.bot" )

            imageWidth = cmds.getAttr("defaultResolution.width")
            imageHeight = cmds.getAttr("defaultResolution.height")

            cropWindow = [float(left)/(imageWidth-1), 
                          float(right)/(imageWidth-1),
                          float(imageHeight-1-top)/(imageHeight-1),
                          float(imageHeight-1-bottom)/(imageHeight-1)
            ]

            filmElement.addAttributeFloat('cropwindow', cropWindow)


    return filmElement

def createFilm(renderSettings):
    #Resolution
    imageWidth = cmds.getAttr("defaultResolution.width")
    imageHeight = cmds.getAttr("defaultResolution.height")

    # Film
    filmMaya = cmds.getAttr("%s.%s" % (renderSettings, "film"))

    mayaUINameToCreateFunction = {
        "Image Film" : createFilmImage,
    }

    if filmMaya in mayaUINameToCreateFunction:
        createFilmFunction = mayaUINameToCreateFunction[filmMaya]
    else:
        if exportVerbosity:
            print( "Unsupported Film : %s. Using Image" % filmMaya)
        createFilmFunction = createFilmImage

    filmElement = createFilmFunction(renderSettings)

    # Set resolution
    imageWidth = cmds.getAttr("defaultResolution.width")
    imageHeight = cmds.getAttr("defaultResolution.height")
    filmElement.addAttributeInteger('xresolution', imageWidth)
    filmElement.addAttributeInteger('yresolution', imageHeight)

    # Set crop window
    filmElement = addRenderRegionCropCoordinates(filmElement)

    return filmElement

#
# Create camera transforms and camera
#
def getRenderableCamera():
    cams = cmds.ls(type="camera", long=True)
    rCamShape = ""
    for cam in cams:
        isRenderable = cmds.getAttr(cam+".renderable")
        if isRenderable:
            print( "Render Settings - Camera           : %s" % cam )
            rCamShape = cam
            break

    if rCamShape == "":
        if exportVerbosity:
            print( "No renderable camera found. Rendering with first camera : %s" % cams[0] )
        rCamShape = cams[0]

    return rCamShape

def createCameraScreenWindow(renderSettings, camera):
    shiftX = cmds.getAttr(camera+".filmTranslateH")
    shiftY = cmds.getAttr(camera+".filmTranslateV")
    
    imageWidth = cmds.getAttr("defaultResolution.width")
    imageHeight = cmds.getAttr("defaultResolution.height")

    ratio = float(imageWidth) / float(imageHeight)
    invRatio = 1.0/ratio

    scale = 1

    # orthoWidth / 2 when rendering an ortho camea
    if cmds.getAttr(camera+".orthographic"):
        orthographicWidth = cmds.getAttr( camera + ".orthographicWidth")
        scale = orthographicWidth / 2

    screenwindow = [ ( (2 * shiftX) - 1 ) * scale,
                     ( (2 * shiftX) + 1 ) * scale,
                     ( (2 * shiftY) - invRatio ) * scale,
                     ( (2 * shiftY) + invRatio ) * scale
                   ]
    
    return (screenwindow[0], screenwindow[1], screenwindow[2], screenwindow[3])

def createCameraTransforms(rCamShape, renderSettings):
    motionBlur = cmds.getAttr(renderSettings+".motionBlur")

    transformElements = []

    def getCameraTransforms(camShape):
        transformElements = []

        scale = ScaleElement((-1, 1, 1))
        transformElements.append( scale )

        camera = pymel.core.PyNode(camShape)
        camAim = camera.getWorldCenterOfInterest()
        camPos = camera.getEyePoint('world')
        camUp = camera.getWorldUp()

        lookAt = LookAtElement(camPos, camAim, camUp)
        transformElements.append( lookAt )

        return transformElements

    '''
    def getCameraTransforms1(camShape):
        transformElements = []

        scale = ScaleElement((-1, 1, 1))
        transformElements.append( scale )

        xform = cmds.listRelatives(camShape, parent=True, fullPath=True)[0]
        matrix = cmds.getAttr(xform+".worldMatrix")
        transform = TransformMatrixElement(matrix)

        transformElements.append( transform )

        return transformElements
    '''

    if motionBlur:
        if exportVerbosity:
            print( "Creating animated camera transforms for motion blur" )

        currentFrame = cmds.currentTime(query=True)

        activeTransformElement1 = ActiveTransformElement("StartTime")
        transformElements.append( activeTransformElement1 )

        transforms1 = getCameraTransforms(rCamShape)
        transformElements.extend( transforms1 )

        cmds.currentTime(float(currentFrame+1))

        activeTransformElement1 = ActiveTransformElement("EndTime")
        transformElements.append( activeTransformElement1 )

        transforms2 = getCameraTransforms(rCamShape)
        transformElements.extend( transforms2 )

        activeTransformElement1 = ActiveTransformElement("All")
        transformElements.append( activeTransformElement1 )

        cmds.currentTime(float(currentFrame))
    else:
        if exportVerbosity:
            print( "Creating static camera transforms" )
        transformElements = getCameraTransforms(rCamShape)

    return transformElements

def createCamera(renderSettings):
    # Find renderable camera
    rCamShape = getRenderableCamera()

    # Type
    camType = "perspective"
    if cmds.getAttr(rCamShape+".orthographic"):
        camType = "orthographic"

    depthOfField = False
    if cmds.getAttr(rCamShape+".depthOfField"):
        depthOfField = True

    # Camera type override
    cameraOverride = cmds.getAttr("%s.cameraOverride" % renderSettings)
    mayaUINameToPBRTCamera = { 
        "Environment" : "environment",
        "Realistic Perspective" : "realistic",
    }

    if cameraOverride not in [None, "", "None"]:
        camType = mayaUINameToPBRTCamera[cameraOverride]
        print( "Sensor Override : %s - %s" % (cameraOverride, camType) )

    # DoF
    apertureRadius = 1
    focusDistance = 1
    if depthOfField:
        apertureRadius = cmds.getAttr(rCamShape+".focusRegionScale")
        focusDistance = cmds.getAttr(rCamShape+".focusDistance")

    # FoV
    fov = cmds.camera(rCamShape, query=True, horizontalFieldOfView=True)

    # Orthographic
    orthographicWidth = cmds.getAttr( rCamShape + ".orthographicWidth")
    orthographicWidth /= 2.0

    # Near Clip Plane
    nearClip = cmds.getAttr(rCamShape+".nearClipPlane")

    # Create Camera
    cameraElements = []
    cameraElement = CameraElement( camType ) 

    if camType in ["perspective"]:
        cameraElement.addAttributeFloat('fov', fov)

    if depthOfField:
        cameraElement.addAttributeFloat('lensradius', apertureRadius)
        cameraElement.addAttributeFloat('focaldistance', focusDistance)

    screenwindow = createCameraScreenWindow(renderSettings, rCamShape)

    if camType is "realistic":
        apertureDiameter = cmds.getAttr(renderSettings+".cameraRealisticApertureDiameter")
        focusDistance = cmds.getAttr(renderSettings+".cameraRealisticFocusDistance")
        simpleWeighting = cmds.getAttr(renderSettings+".cameraRealisticSimpleWeighting")
        lensFile = cmds.getAttr(renderSettings+".cameraRealisticLensFile", asString=True)

        cameraElement.addAttributeFloat('aperturediameter', apertureDiameter)
        cameraElement.addAttributeFloat('focusdistance', focusDistance)
        cameraElement.addAttributeBoolean('simpleweighting', simpleWeighting)

        if lensFile:
            lensFileRelative = os.path.relpath( lensFile, renderDir )
            cameraElement.addAttributeString('lensfile', lensFileRelative)

        PBRTVersion = cmds.getAttr("%s.%s" % (renderSettings, "PBRTVersion"))
        if PBRTVersion == "v3 Book":
            cameraElement.addAttributeFloat('screenwindow', screenwindow)
    else:
        cameraElement.addAttributeFloat('screenwindow', screenwindow)

    # Transforms
    transformElements = createCameraTransforms(rCamShape, renderSettings)

    comment1 = CommentElement("Camera begin")
    cameraElements.append( comment1 )

    cameraElements.extend( transformElements )
    cameraElements.append( cameraElement )

    comment2 = CommentElement("Camera end")
    cameraElements.append( comment2 )

    return cameraElements

#
# Create Lights
#
def getConnectedTexturePath(destination, connectionAttr, acceptedExtensions=None):
    fileName = None
    source = getTextureConnection(destination, connectionAttr)

    if not acceptedExtensions:
        acceptedExtensions = []

    if source:
        fileName = getTexturePath(source)

        if fileName:
            extension = os.path.splitext(fileName)[-1]
            if( acceptedExtensions != [] and 
                extension.lower() not in acceptedExtensions ):
                if exportVerbosity:
                    print( "%s - File format must be in %s" % (destination, acceptedExtensions) )
                fileName = None
        else:
            if exportVerbosity:
                print( "%s - Please connect a file to attribute %s" % (destination, connectionAttr) )

    return fileName

def createLightInfinite(light):
    envMapFileName = getConnectedTexturePath(light, "envmap", [".exr"])

    lightElement = None
    if envMapFileName:
        nsamples = cmds.getAttr(light+".nsamples")

        lightElement = AttributeElement()

        translateElements = []

        rotate = cmds.getAttr("%s.rotate" % light )[0]
        if rotate[1] != 0.0:
            rotateY = RotateElement(( rotate[1], 0.0, 1.0, 0.0))
            translateElements.append( rotateY )

        rotate1 = RotateElement(( 90.0, 0.0, 1.0, 0.0))
        rotate2 = RotateElement((-90.0, 1.0, 0.0, 0.0))
        scale = ScaleElement((-1, 1, 1))

        translateElements.append( rotate1 )
        translateElements.append( rotate2 )
        translateElements.append( scale )

        # Create a structure to be written
        infiniteLightElement = LightElement('infinite')

        textureElements = []
        addTexturedColorAttribute(light, 'luminance', infiniteLightElement, 
            textureElements, rendererParameter="L")

        infiniteLightElement.addAttributeInteger('nsamples', nsamples)
        infiniteLightElement.addAttributeString('mapname', envMapFileName)

        lightElement.addChildren( translateElements )
        lightElement.addChild( infiniteLightElement )

    return lightElement

def createLightDirectional(light):
    intensity = cmds.getAttr(light+".intensity")

    matrix = cmds.getAttr(light+".worldMatrix")
    lightDir = [-matrix[8],-matrix[9],-matrix[10]]

    # Create a structure to be written
    lightElement = AttributeElement()

    comment1 = CommentElement("Maya Directional Light : %s" % light)

    directionalLightElement = LightElement('distant')

    textureElements = []
    addTexturedColorAttribute(light, 'color', directionalLightElement, 
        textureElements, rendererParameter="L")
    directionalLightElement.addAttributeRGB('scale', 
        [intensity, intensity, intensity])

    directionalLightElement.addAttributePoint('to', lightDir)

    lightElement.addChild( comment1 )
    lightElement.addChild( directionalLightElement )

    return lightElement

def createLightPoint(light):
    intensity = cmds.getAttr(light+".intensity")

    matrix = cmds.getAttr(light+".worldMatrix")
    position = [matrix[12],matrix[13],matrix[14]]

    lightElement = AttributeElement()

    comment1 = CommentElement("Maya Point Light : %s" % light)
    translate1 = TranslateElement(position)

    # Create a structure to be written
    pointLightElement = LightElement('point')

    textureElements = []
    addTexturedColorAttribute(light, 'color', pointLightElement, 
        textureElements, rendererParameter="I")
    pointLightElement.addAttributeRGB('scale', 
        [intensity, intensity, intensity])

    lightElement.addChild( comment1 )
    lightElement.addChild( translate1 )
    lightElement.addChild( pointLightElement )

    return lightElement

def createLightTransformsFromMayaObject(shape):
    parent = cmds.listRelatives(shape, parent=True, shapes=False, fullPath=True)
    if parent:
        xform = parent[0]
    else:
        xform = shape

    transforms = []

    matrix = cmds.getAttr(xform+".worldInverseMatrix")
    position = [-matrix[12],-matrix[13],-matrix[14]]

    mMatrix = om.MMatrix()
    om.MScriptUtil.createMatrixFromList(matrix, mMatrix)

    vec = om.MVector.yAxis*10.0
    uvec = vec * mMatrix
    vec = om.MVector.zAxis*10.0
    avec = vec * mMatrix

    scale1 = ScaleElement((-1, -1, -1))

    lookAt = LookAtElement(position, 
        [avec.x + position[0], avec.y + position[1], avec.z + position[2]], 
        [uvec.x + position[0], uvec.y + position[1], uvec.z + position[2]])

    # Sets the horizontal prjection properly
    scale2 = ScaleElement((-1,  1,  1))

    transforms.append( scale1 )
    transforms.append( lookAt )
    transforms.append( scale2 )

    return transforms

def createLightSpotProjector(light):
    colorFileName = getConnectedTexturePath(light, "color", [".exr"])

    lightElement = None
    if colorFileName:
        intensity = cmds.getAttr(light+".intensity")
        irradiance = [intensity,intensity,intensity]

        coneAngle = float(cmds.getAttr(light+".coneAngle"))

        transforms = createLightTransformsFromMayaObject(light)

        # Create a structure to be written
        lightElement = AttributeElement()

        comment1 = CommentElement("Maya Spot Light as Projection : %s" % light)

        spotLightElement = LightElement('projection')
        spotLightElement.addAttributeRGB('scale', irradiance)
        spotLightElement.addAttributeFloat('fov', coneAngle)
        spotLightElement.addAttributeString('mapname', colorFileName)
 
        lightElement.addChild( comment1 )
        lightElement.addChildren( transforms )
        lightElement.addChild( spotLightElement )

    return lightElement

def createLightSpotGoniometric(light):
    dropoffFileName = getConnectedTexturePath(light, "dropoff", [".exr"])

    lightElement = None
    if dropoffFileName:
        intensity = cmds.getAttr(light+".intensity")
        color = cmds.getAttr(light+".color")[0]
        irradiance = [0,0,0]
        for i in range(3):
            irradiance[i] = intensity*color[i]

        transforms = createLightTransformsFromMayaObject(light)

        # Create a structure to be written
        lightElement = AttributeElement()

        comment1 = CommentElement("Maya Spot Light as Goniometric : %s" % light)

        spotLightElement = LightElement('goniometric')
        spotLightElement.addAttributeRGB('scale', irradiance)
        spotLightElement.addAttributeString('mapname', dropoffFileName)

        # Additional rotate, to align gonio space with light space
        rotateG = RotateElement((-90.0, 1.0, 0.0, 0.0))
 
        lightElement.addChild( comment1 )
        lightElement.addChildren( transforms )
        lightElement.addChild( rotateG )
        lightElement.addChild( spotLightElement )

    return lightElement

def createLightSpot(light):
    intensity = cmds.getAttr(light+".intensity")

    coneAngle = float(cmds.getAttr(light+".coneAngle"))/2.0
    penumbraAngle = float(cmds.getAttr(light+".penumbraAngle"))

    matrix = cmds.getAttr(light+".worldMatrix")
    position = [matrix[12],matrix[13],matrix[14]]
    lightDir = [-matrix[8],-matrix[9],-matrix[10]]
    positionTo = [(position[0] + lightDir[0]),
        (position[1] + lightDir[1]),
        (position[2] + lightDir[2])]

    lightElement = AttributeElement()

    comment1 = CommentElement("Maya Spot Light : %s" % light)
    translate1 = TranslateElement(position)

    # Create a structure to be written
    spotLightElement = LightElement('spot')

    textureElements = []
    addTexturedColorAttribute(light, 'color', spotLightElement, 
        textureElements, rendererParameter="I")
    spotLightElement.addAttributeRGB('scale', 
        [intensity, intensity, intensity])

    spotLightElement.addAttributeFloat('coneangle', coneAngle+penumbraAngle)
    spotLightElement.addAttributeFloat('conedeltaangle', penumbraAngle)

    spotLightElement.addAttributePoint('from', position)
    spotLightElement.addAttributePoint('to', positionTo)

    lightElement.addChild( comment1 )
    lightElement.addChild( spotLightElement )

    return lightElement

def createLightMayaSpot(light):
    colorFileName = getConnectedTexturePath(light, "color", [".exr"])
    colorIsSPD = False
    if colorFileName:
        extension = os.path.splitext(colorFileName)[-1][1:]
        colorIsSPD = (extension == "spd")

    dropoffFileName = getConnectedTexturePath(light, "dropoff", [".exr"])

    if colorFileName and not colorIsSPD:
        lightElement = createLightSpotProjector(light)
    elif dropoffFileName:
        lightElement = createLightSpotGoniometric(light)
    else:
        lightElement = createLightSpot(light)

    return lightElement

def isVisible(object):
    #print( "Checking visibility : %s" % object )
    visible = True

    if cmds.attributeQuery("visibility", node=object, exists=True):
        visible = visible and cmds.getAttr(object+".visibility")

    if cmds.attributeQuery("intermediateObject", node=object, exists=True):
        visible = visible and not cmds.getAttr(object+".intermediateObject")

    if cmds.attributeQuery("overrideEnabled", node=object, exists=True):
        visible = visible and cmds.getAttr(object+".overrideVisibility")

    if visible:
        parents = cmds.listRelatives(object, fullPath=True, parent=True)
        if parents:
            for parent in parents:
                parentVisible = isVisible(parent)
                if not parentVisible:
                    #print( "\tParent not visible. Breaking : %s" % parent )
                    visible = False
                    break
                
    #print( "\tVisibility : %s" % visible )
    
    return visible

def createLightElements():
    # Gather visible lights
    lights = cmds.ls(type="light", long=True)
    lights = [x for x in lights if isVisible(x)]

    infiniteLights = cmds.ls(type="PBRTInfiniteLight", long=True)
    infiniteLights = [x for x in infiniteLights if isVisible(x)]

    # Warn if multiple environment lights are active
    if infiniteLights and len(infiniteLights)>1:
        if exportVerbosity:
            print( "\n" )
            print( "Cannot specify more than one environment light (PBRTInfiniteLight)" )
            print( "Using first infinite light : %s" % infiniteLights[0] )
            print( "\n" )

    # Create light elements
    lightElements = []

    # Gather element definitions for standard lights
    for light in lights:
        lightType = cmds.nodeType(light)
        if lightType == "directionalLight":
            lightElements.append( createLightDirectional(light) )
        elif lightType == "pointLight":
            lightElements.append( createLightPoint(light) )
        elif lightType == "spotLight":
            lightElements.append( createLightMayaSpot(light) )

    # Gather element definitions for 'infinite' Environment lights
    if infiniteLights:
        infinite = infiniteLights[0]
        lightElements.append( createLightInfinite(infinite) )

    return lightElements

#
# Create Volume Scattering Models
#
def createMediumHomogeneous(medium, mediumName):
    textureElements = []

    preset = cmds.getAttr(medium+".preset", asString=True)

    mediumElement = MakeNamedMediumElement(mediumName, 'homogeneous')

    if preset != "None":
        mediumElement.addAttributeString('preset', preset)
    else:
        addTexturedColorAttribute(medium, 'sigma_a', mediumElement, textureElements)
        addTexturedColorAttribute(medium, 'sigma_s', mediumElement, textureElements)

    addTexturedFloatAttribute(medium, 'g', mediumElement, textureElements)
    addTexturedFloatAttribute(medium, 'scale', mediumElement, textureElements)

    return ([mediumElement], textureElements)

def createMediumHeterogeneous(medium, mediumName):
    textureElements = []

    densityFilename = cmds.getAttr(medium+".densityfile", asString=True)
    densityFilenameRelative = os.path.relpath( densityFilename, renderDir )
    preset = cmds.getAttr(medium+".preset", asString=True)

    mediumElement = SceneElement('Include', densityFilenameRelative)

    if preset != "None":
        mediumElement.addAttributeString('preset', preset)
    else:
        addTexturedColorAttribute(medium, 'sigma_a', mediumElement, textureElements)
        addTexturedColorAttribute(medium, 'sigma_s', mediumElement, textureElements)

    addTexturedFloatAttribute(medium, 'g', mediumElement, textureElements)
    addTexturedFloatAttribute(medium, 'scale', mediumElement, textureElements)

    boundingBoxLowerOverride = cmds.getAttr(medium+".boundingBoxLowerOverride")[0]
    boundingBoxUpperOverride = cmds.getAttr(medium+".boundingBoxUpperOverride")[0]
    if boundingBoxLowerOverride != boundingBoxUpperOverride:
        mediumElement.addAttributePoint('p0', boundingBoxLowerOverride)
        mediumElement.addAttributePoint('p1', boundingBoxUpperOverride)

    return ([mediumElement], textureElements)

#
# Create Surface Scattering Models
#
def createMaterialUber(material, materialName):
    remapRoughness = cmds.getAttr(material+".remapRoughness")

    textureElements = []

    materialElement = MakeNamedMaterialElement(materialName, 'uber')

    addTexturedColorAttribute(material, 'Kd', materialElement, textureElements)
    addTexturedColorAttribute(material, 'Ks', materialElement, textureElements)
    addTexturedColorAttribute(material, 'Kr', materialElement, textureElements)
    addTexturedColorAttribute(material, 'opacity', materialElement, textureElements)

    addTexturedFloatAttribute(material, 'roughness', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'index', materialElement, textureElements)

    materialElement.addAttributeBoolean("remaproughness", remapRoughness)

    addTexturedFloatAttribute(material, 'uRoughness', materialElement, 
        textureElements, noDefault=True, rendererParameter='uroughness')
    addTexturedFloatAttribute(material, 'vRoughness', materialElement, 
        textureElements, noDefault=True, rendererParameter='vroughness')
    addTexturedFloatAttribute(material, 'bumpmap', materialElement, 
        textureElements, noDefault=True)
    addTexturedFloatAttribute(material, 'bumpmap', materialElement, 
        textureElements, noDefault=True)

    return ([materialElement], textureElements)

def createMaterialFourier(material, materialName):
    textureElements = []

    filename = cmds.getAttr(material+".bsdffile", asString=True)
    filenameRelative = os.path.relpath( filename, renderDir )

    materialElement = MakeNamedMaterialElement(materialName, 'fourier')
    materialElement.addAttributeString('bsdffile', filenameRelative)

    addTexturedFloatAttribute(material, 'bumpmap', materialElement, 
        textureElements, noDefault=True)

    return ([materialElement], textureElements)

def createMaterialGlass(material, materialName):
    remapRoughness = cmds.getAttr(material+".remapRoughness")

    textureElements = []

    materialElement = MakeNamedMaterialElement(materialName, 'glass')

    addTexturedColorAttribute(material, 'Kr', materialElement, textureElements)
    addTexturedColorAttribute(material, 'Kt', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'index', materialElement, textureElements)

    materialElement.addAttributeBoolean("remaproughness", remapRoughness)

    addTexturedFloatAttribute(material, 'uRoughness', materialElement, 
        textureElements, noDefault=True, rendererParameter='uroughness')
    addTexturedFloatAttribute(material, 'vRoughness', materialElement, 
        textureElements, noDefault=True, rendererParameter='vroughness')

    addTexturedFloatAttribute(material, 'bumpmap', materialElement, 
        textureElements, noDefault=True)

    return ([materialElement], textureElements)

def createMaterialHair(material, materialName):
    textureElements = []

    materialElement = MakeNamedMaterialElement(materialName, 'hair')

    addTexturedColorAttribute(material, 'sigma_a', materialElement, textureElements)
    addTexturedColorAttribute(material, 'color', materialElement, textureElements)

    addTexturedFloatAttribute(material, 'eumelanin', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'pheomelanin', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'beta_m', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'beta_n', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'alpha', materialElement, textureElements)

    return ([materialElement], textureElements)

def createMaterialKDSubSurface(material, materialName):
    remapRoughness = cmds.getAttr(material+".remapRoughness")

    textureElements = []

    materialElement = MakeNamedMaterialElement(materialName, 'kdsubsurface')

    addTexturedColorAttribute(material, 'Kd', materialElement, textureElements)
    addTexturedColorAttribute(material, 'mfp', materialElement, textureElements)
    addTexturedColorAttribute(material, 'Kr', materialElement, textureElements)
    addTexturedColorAttribute(material, 'Kt', materialElement, textureElements)

    addTexturedFloatAttribute(material, 'eta', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'scale', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'g', materialElement, textureElements)

    materialElement.addAttributeBoolean("remaproughness", remapRoughness)

    addTexturedFloatAttribute(material, 'uRoughness', materialElement, 
        textureElements, noDefault=True, rendererParameter='uroughness')
    addTexturedFloatAttribute(material, 'vRoughness', materialElement, 
        textureElements, noDefault=True, rendererParameter='vroughness')

    addTexturedFloatAttribute(material, 'bumpmap', materialElement, 
        textureElements, noDefault=True)

    return ([materialElement], textureElements)

def createMaterialMatte(material, materialName):
    textureElements = []

    materialElement = MakeNamedMaterialElement(materialName, 'matte')

    addTexturedColorAttribute(material, 'Kd', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'sigma', materialElement, textureElements)

    addTexturedFloatAttribute(material, 'bumpmap', materialElement, 
        textureElements, noDefault=True)

    return ([materialElement], textureElements)

def createMaterialMetal(material, materialName):
    remapRoughness = cmds.getAttr(material+".remapRoughness")

    textureElements = []

    materialElement = MakeNamedMaterialElement(materialName, 'metal')

    addTexturedColorAttribute(material, 'eta', materialElement, textureElements)
    addTexturedColorAttribute(material, 'k', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'roughness', materialElement, textureElements)

    materialElement.addAttributeBoolean("remaproughness", remapRoughness)

    addTexturedFloatAttribute(material, 'uRoughness', materialElement, 
        textureElements, noDefault=True, rendererParameter='uroughness')
    addTexturedFloatAttribute(material, 'vRoughness', materialElement, 
        textureElements, noDefault=True, rendererParameter='vroughness')

    addTexturedFloatAttribute(material, 'bumpmap', materialElement, 
        textureElements, noDefault=True)

    return ([materialElement], textureElements)

def createMaterialMirror(material, materialName):
    textureElements = []

    materialElement = MakeNamedMaterialElement(materialName, 'mirror')

    addTexturedColorAttribute(material, 'Kr', materialElement, textureElements)

    addTexturedFloatAttribute(material, 'bumpmap', materialElement, 
        textureElements, noDefault=True)

    return ([materialElement], textureElements)

def createMaterialPlastic(material, materialName):
    remapRoughness = cmds.getAttr(material+".remapRoughness")

    textureElements = []

    materialElement = MakeNamedMaterialElement(materialName, 'plastic')

    addTexturedColorAttribute(material, 'Kd', materialElement, textureElements)
    addTexturedColorAttribute(material, 'Ks', materialElement, textureElements)

    materialElement.addAttributeBoolean("remaproughness", remapRoughness)

    addTexturedFloatAttribute(material, 'roughness', materialElement, textureElements)

    addTexturedFloatAttribute(material, 'bumpmap', materialElement, 
        textureElements, noDefault=True)

    return ([materialElement], textureElements)

def createMaterialSubstrate(material, materialName):
    remapRoughness = cmds.getAttr(material+".remapRoughness")

    textureElements = []

    materialElement = MakeNamedMaterialElement(materialName, 'substrate')

    addTexturedColorAttribute(material, 'Kd', materialElement, textureElements)
    addTexturedColorAttribute(material, 'Ks', materialElement, textureElements)

    materialElement.addAttributeBoolean("remaproughness", remapRoughness)

    addTexturedFloatAttribute(material, 'uRoughness', materialElement, 
        textureElements, noDefault=True, rendererParameter='uroughness')
    addTexturedFloatAttribute(material, 'vRoughness', materialElement, 
        textureElements, noDefault=True, rendererParameter='vroughness')

    addTexturedFloatAttribute(material, 'bumpmap', materialElement, 
        textureElements, noDefault=True)

    return ([materialElement], textureElements)

def createMaterialSubSurface(material, materialName):
    remapRoughness = cmds.getAttr(material+".remapRoughness")

    textureElements = []

    name = cmds.getAttr(material+".Preset", asString=True)

    materialElement = MakeNamedMaterialElement(materialName, 'subsurface')

    if name != "None":
        materialElement.addAttributeString('name', name)
    else:
        addTexturedColorAttribute(material, 'sigma_a', materialElement, textureElements)
        addTexturedColorAttribute(material, 'sigma_s', materialElement, textureElements)
        addTexturedFloatAttribute(material, 'g', materialElement, textureElements)

    addTexturedFloatAttribute(material, 'scale', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'eta', materialElement, textureElements)

    addTexturedColorAttribute(material, 'Kr', materialElement, textureElements)
    addTexturedColorAttribute(material, 'Kt', materialElement, textureElements)

    materialElement.addAttributeBoolean("remaproughness", remapRoughness)

    addTexturedFloatAttribute(material, 'uRoughness', materialElement, 
        textureElements, noDefault=True, rendererParameter='uroughness')
    addTexturedFloatAttribute(material, 'vRoughness', materialElement, 
        textureElements, noDefault=True, rendererParameter='vroughness')

    addTexturedFloatAttribute(material, 'bumpmap', materialElement, 
        textureElements, noDefault=True)

    return ([materialElement], textureElements)

def createMaterialTranslucent(material, materialName):
    remapRoughness = cmds.getAttr(material+".remapRoughness")

    textureElements = []

    materialElement = MakeNamedMaterialElement(materialName, 'translucent')

    addTexturedColorAttribute(material, 'Kd', materialElement, textureElements)
    addTexturedColorAttribute(material, 'Ks', materialElement, textureElements)

    addTexturedColorAttribute(material, 'reflect', materialElement, textureElements)
    addTexturedColorAttribute(material, 'transmit', materialElement, textureElements)

    addTexturedFloatAttribute(material, 'roughness', materialElement, textureElements)

    materialElement.addAttributeBoolean("remaproughness", remapRoughness)

    addTexturedFloatAttribute(material, 'bumpmap', materialElement, 
        textureElements, noDefault=True)

    return ([materialElement], textureElements)

def createMaterialMaya(material, materialName):
    textureElements = []

    materialElement = MakeNamedMaterialElement(materialName, 'matte')

    addTexturedColorAttribute(material, 'color', materialElement, textureElements,
        rendererParameter='Kd')

    return ([materialElement], textureElements)

def createMaterialDisney(material, materialName):
    thin = cmds.getAttr(material+".thin")

    textureElements = []

    materialElement = MakeNamedMaterialElement(materialName, 'disney')

    addTexturedColorAttribute(material, 'color', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'metallic', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'eta', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'roughness', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'specularTint', materialElement, textureElements,
        rendererParameter='speculartint')
    addTexturedFloatAttribute(material, 'anisotropic', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'sheen', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'sheenTint', materialElement, textureElements,
        rendererParameter='sheentint')
    addTexturedFloatAttribute(material, 'clearCoat', materialElement, textureElements,
        rendererParameter='clearcoat')
    addTexturedFloatAttribute(material, 'clearCoatGloss', materialElement, textureElements,
        rendererParameter='clearcoatgloss')
    addTexturedFloatAttribute(material, 'specTrans', materialElement, textureElements,
        rendererParameter='spectrans')
    addTexturedColorAttribute(material, 'scatterDistance', materialElement, textureElements,
        rendererParameter='scatterdistance')
    materialElement.addAttributeBoolean("thin", thin)
    addTexturedFloatAttribute(material, 'flatness', materialElement, textureElements)
    addTexturedFloatAttribute(material, 'diffTrans', materialElement, textureElements,
        rendererParameter='difftrans')
    addTexturedFloatAttribute(material, 'bumpmap', materialElement, 
        textureElements, noDefault=True)

    return ([materialElement], textureElements)

def createMaterialMix(material, materialName):
    materialElements = []
    textureElements = []

    materialElement = MakeNamedMaterialElement(materialName, 'mix')

    # Amount
    addTexturedColorAttribute(material, 'Amount', materialElement, textureElements,
        rendererParameter='amount')

    # Material 1
    (m1MaterialElements, 
     m1TextureElements) = ConnectedMaterialAttributeElement(material, 'Material1')

    if m1MaterialElements:
        materialElements.extend(m1MaterialElements)
        textureElements.extend(m1TextureElements)

        m1MaterialElement = materialElements[-1]
        m1MaterialName = m1MaterialElement['plugin']
        materialElement.addAttributeString("namedmaterial1", m1MaterialName)

    # Material 2
    (m2MaterialElements, 
     m2TextureElements) = ConnectedMaterialAttributeElement(material, 'Material2')

    if m2MaterialElements:
        materialElements.extend(m2MaterialElements)
        textureElements.extend(m2TextureElements)

        m2MaterialElement = materialElements[-1]
        m2MaterialName = m2MaterialElement['plugin']
        materialElement.addAttributeString("namedmaterial2", m2MaterialName)

    # Main material element
    materialElements.append(materialElement)

    return (materialElements, textureElements)

def createMaterialDiffuseArea(material, materialName):
    textureElements = []

    luminance = cmds.getAttr(material+".luminance")
    scale = cmds.getAttr(material+".scale")
    nsamples = cmds.getAttr(material+".nsamples")

    areaLightElement = SceneElement('AreaLightSource', 'diffuse')

    areaLightElement.addAttributeRGB('L', luminance[0])
    areaLightElement.addAttributeRGB('scale', scale[0])
    areaLightElement.addAttributeInteger('nsamples', nsamples)

    return ([areaLightElement], textureElements)

#
# Create a material
#
def createMaterial(material, materialName):
    matType = cmds.nodeType(material)
    
    mayaMaterialTypeToShaderFunction = {
        "PBRTFourierMaterial" : createMaterialFourier,
        "PBRTGlassMaterial" : createMaterialGlass,
        "PBRTHairMaterial" : createMaterialHair,
        "PBRTKDSubSurfaceMaterial" : createMaterialKDSubSurface,
        "PBRTMetalMaterial" : createMaterialMetal,
        "PBRTMatteMaterial" : createMaterialMatte,
        "PBRTMirrorMaterial" : createMaterialMirror,
        "PBRTMixMaterial" : createMaterialMix,
        "PBRTPlasticMaterial" : createMaterialPlastic,
        "PBRTSubstrateMaterial" : createMaterialSubstrate,
        "PBRTSubSurfaceMaterial" : createMaterialSubSurface,
        "PBRTTranslucentMaterial" : createMaterialTranslucent,
        "PBRTUberMaterial" : createMaterialUber,
        "PBRTDisneyMaterial" : createMaterialDisney,
        "PBRTDiffuseAreaLight" : createMaterialDiffuseArea,
        "PBRTHomogeneousMedium" : createMediumHomogeneous,
        "PBRTHeterogeneousMedium" : createMediumHeterogeneous,
        "lambert" : createMaterialMaya,
        "blinn" : createMaterialMaya,
        "phong" : createMaterialMaya,
        "phongE" : createMaterialMaya,
    }

    if matType in mayaMaterialTypeToShaderFunction:
        if exportVerbosity:
            print( "Creating material : %s, type : %s." % (material, matType) )
        createMaterialFunction = mayaMaterialTypeToShaderFunction[matType]
    else:
        if exportVerbosity:
            print( "Skipping unsupported material : %s." % matType)
        createMaterialFunction = None

    materialElements = []
    textureElements = []
    if createMaterialFunction:
        (materialElements, 
         textureElements) = createMaterialFunction(material, materialName)

    return (materialElements, textureElements)

def ConnectedMaterialAttributeElement(baseMaterial, attribute, rendererParameter=None):
    if not rendererParameter:
        rendererParameter = attribute

    connections = cmds.listConnections(baseMaterial, connections=True)
    nodeName = None
    for i in range(len(connections)):
        if i%2==1:
            connection = connections[i]
            if( connections[i-1].lower() == (baseMaterial+"."+attribute).lower() ):
                nodeName = connection

    materialElements = []
    textureElements = []

    if nodeName:
        (materialElements, 
         textureElements) = createMaterial(nodeName, nodeName)

    return (materialElements, textureElements)

def createMaterialElements(geoms):
    createdMaterialElements = []
    createdTextureElements = []

    createdMaterialNames = []
    createdTextureNames = []

    def createMaterialsAndTextures(material):
        if material and material not in createdMaterialNames:
            #print( "createMaterialsAndTextures : %s" % material )
            materialType = cmds.nodeType(material)

            if( (materialType in materialNodeTypes or
                 materialType in mayaMaterialNodeTypes) and 
                materialType != "PBRTDiffuseAreaLight" ):

                (materialElements, 
                 textureElements) = createMaterial(material, material)

                createdMaterialElements.extend(materialElements)
                materialNames = [x['plugin'] for x in materialElements]
                createdMaterialNames.extend(materialNames)

                for texture in textureElements:
                    textureName = texture['plugin']
                    if textureName not in createdTextureNames:
                        createdTextureElements.append(texture)
                        createdTextureNames.append(textureName)

    #Create the material and textures for each piece of geometry in the scene
    for geom in geoms:
        # Surface shader
        material = getSurfaceShader(geom)
        createMaterialsAndTextures(material)

        # Medium / Volume shaders
        medium = getVolumeShader(geom)
        createMaterialsAndTextures(medium)
        
    return (createdMaterialElements, createdTextureElements)

#
# Export and create geometry
#
def getRenderableGeometry(transforms=None):
    # Build list of visible geometry
    availableTransforms = transforms
    if not availableTransforms:
        availableTransforms = cmds.ls(type="transform", long=True)
    geoms = []

    for transform in availableTransforms:
        #print( "Transform : %s" % transform )
        rels = cmds.listRelatives(transform, fullPath=True)
        if rels:
            ##print( "\tRelatives : %d" % len(rels) )
            for rel in rels:
                #print( "\tRelative : %s" % rel )
                #print( "\tNode type : %s" % cmds.nodeType(rel) )

                if cmds.nodeType(rel) == "mesh":
                    visible = isVisible(transform)
                    if visible:
                        #print( "\tVisible mesh : %s" % transform )
                        if transform not in geoms:
                            geoms.append(transform)
                            #print( "\tAdding transform" )
                        #else:
                            #print( "\tTransform already cached" )

                elif cmds.nodeType(rel) == "transform":
                    #print( "\tRecurse\n" )
                    childGeoms = getRenderableGeometry([rel])
                    if childGeoms:
                        geoms.extend(childGeoms)

                #print( "" )

    return list(set(geoms))

def exportGeometryObj(geom, renderDir, renderSettings):
    geomFilename = geom.replace(':', '__').replace('|', '__')

    skipGeometryExport = cmds.getAttr( "%s.%s" % (renderSettings, "skipGeometryExport"))

    alpha = cmds.getAttr(geom+".primaryVisibility")
    shadowalpha = cmds.getAttr(geom+".castsShadows")

    cmds.select(geom)

    # Export OBJ
    objFilenamePath = geomFilename + ".obj"
    objFilenameFullPath = os.path.join(renderDir, objFilenamePath)

    if skipGeometryExport and os.path.isfile(objFilenameFullPath):
        if exportVerbosity:
            print( "Skipping export of %s" % objFilenamePath)
    else:
        objFile = cmds.file(objFilenameFullPath, 
            op=True, 
            typ="OBJexport", 
            options="groups=1;ptgroups=1;materials=0;smoothing=1;normals=1", 
            exportSelected=True, 
            force=True)

    # Convert OBJ to PBRT
    pbrtPath = cmds.getAttr( "%s.%s" % (renderSettings, "PBRTPath"))
    obj2pbrtPath = os.path.join(os.path.split(pbrtPath)[0], 'obj2pbrt')

    pbrtTempFilenamePath = geomFilename + "_temp.pbrt"
    pbrtTempFilenameFullPath = os.path.join(renderDir, pbrtTempFilenamePath)

    if skipGeometryExport and os.path.isfile(pbrtTempFilenameFullPath):
        if exportVerbosity:
            print( "Skipping gen. of   %s" % pbrtTempFilenamePath)
    else:
        args = [objFilenameFullPath, pbrtTempFilenameFullPath]
        obj2pbrt = Process(description='convert from obj to pbrt',
            cmd=obj2pbrtPath,
            args=args)
        obj2pbrt.execute()

    # Strip out the 'Material' definition
    # Add in alpha and shadowalpha values
    pbrtFilenamePath = geomFilename + ".pbrt"
    pbrtFilenameFullPath = os.path.join(renderDir, pbrtFilenamePath)
    PBRTVersion = cmds.getAttr("%s.%s" % (renderSettings, "PBRTVersion"))

    if skipGeometryExport and os.path.isfile(pbrtFilenameFullPath):
        if exportVerbosity:
            print( "Skipping conv. of  %s" % pbrtFilenamePath)
    else:
        pbrtTempFile = open(pbrtTempFilenameFullPath, 'r') 
        with open(pbrtFilenameFullPath, 'w+') as pbrtFile:
            for line in pbrtTempFile:
                if "Material" in line:
                    continue
                if "AttributeEnd" in line:
                    pbrtFile.write("\"  float alpha\" [%f]\n" % alpha )
                    if PBRTVersion != "v3 Book":
                        pbrtFile.write("\"  float shadowalpha\" [%f]\n" % shadowalpha )

                pbrtFile.write(line)

    return (objFilenameFullPath, pbrtTempFilenameFullPath, pbrtFilenameFullPath)

def exportGeometryPly(geom, renderDir, renderSettings, space='object'):
    geomFilename = geom.replace(':', '__').replace('|', '__')

    skipGeometryExport = cmds.getAttr( "%s.%s" % (renderSettings, "skipGeometryExport"))

    cmds.select(geom)

    # Export PLY
    plyFilenamePath = geomFilename + ".ply"
    plyFilenameFullPath = os.path.join(renderDir, plyFilenamePath)

    if skipGeometryExport and os.path.isfile(plyFilenameFullPath):
        if exportVerbosity:
            print( "Skipping export of %s" % plyFilenameFullPath)
    else:
        '''
        PLY import in PBRT currently doesn't support per-face normals, so don't use that option
        '''
        plyFile = cmds.file(plyFilenameFullPath, 
            op=True, 
            typ="ply", 
            exportSelected=True, 
            options="space=%s;format=binary;triangulate=true;verbose=false;" % space,
            force=True)

    return [plyFilenameFullPath]

def exportGeometry(geom, renderDir, objectToExportedFiles, renderSettings):
    translators = cmds.pluginInfo( "PBRTForMaya", query=True, translator=True )
    usePLYExport = cmds.getAttr( "%s.%s" % (renderSettings, "usePLYExport"))

    if geom in objectToExportedFiles:
        geometryFiles = objectToExportedFiles[geom]
    else:
        shape = cmds.listRelatives(geom, shapes=True, fullPath=True)[0]

        if usePLYExport and translators and 'ply' in translators:
            #motionBlur = cmds.getAttr( "%s.%s" % (renderSettings, "motionBlur"))
            #space = 'object' if motionBlur else 'world'
            space = 'object'
            geometryFiles = exportGeometryPly(shape, renderDir, renderSettings, space)
        else:
            geometryFiles = exportGeometryObj(shape, renderDir, renderSettings)

        objectToExportedFiles[geom] = geometryFiles

        # Handle instancing
        shapeParents = cmds.listRelatives(shape, allParents=True, fullPath=True)
        if len(shapeParents) > 1:
            for transform in shapeParents:
                objectToExportedFiles[transform] = geometryFiles

    return geometryFiles

#
# Procedural Geometry
#
def createProceduralGeometryPlyMesh(mayaObject, geometryShader, renderSettings):
    elements = []
    textureElements = []

    #print( "createProceduralGeometryPlyMesh : %s, %s" % (mayaObject, geometryShader) )

    geomFilename = cmds.getAttr(geometryShader+".plyfile", asString=True)    
    geomFilenameRelative = os.path.relpath( geomFilename, renderDir )

    shapeElement = SceneElement('Shape', "plymesh")
    shapeElement.addAttributeString("filename", geomFilenameRelative)

    addTexturedFloatAttribute(geometryShader, 'alpha', shapeElement, textureElements)

    PBRTVersion = cmds.getAttr("%s.%s" % (renderSettings, "PBRTVersion"))
    if PBRTVersion != "v3 Book":
        addTexturedFloatAttribute(geometryShader, 'shadowAlpha', shapeElement, textureElements,
            rendererParameter='shadowalpha')

    elements.append( shapeElement )

    return elements

def createProceduralGeometryInclude(mayaObject, geometryShader, renderSettings):
    elements = []

    #print( "createProceduralGeometryInclude : %s, %s" % (mayaObject, geometryShader) )

    geomFilename = cmds.getAttr(geometryShader+".pbrtfile", asString=True)    
    geomFilenameRelative = os.path.relpath( geomFilename, renderDir )

    shapeElement = SceneElement('Include', geomFilenameRelative)

    elements.append( shapeElement )

    return elements

def createProceduralGeometryCone(mayaObject, geometryShader, renderSettings):
    elements = []

    #print( "createProceduralGeometryCone : %s, %s" % (mayaObject, geometryShader) )

    radius = cmds.getAttr( "%s.%s" % (geometryShader, "radius"))
    height = cmds.getAttr( "%s.%s" % (geometryShader, "height"))
    phimax = cmds.getAttr( "%s.%s" % (geometryShader, "phimax"))

    shapeElement = SceneElement('Shape', "cone")
    shapeElement.addAttributeFloat("radius", radius)
    shapeElement.addAttributeFloat("height", height)
    shapeElement.addAttributeFloat("phimax", phimax)

    elements.append( shapeElement )

    return elements

def createProceduralGeometryCylinder(mayaObject, geometryShader, renderSettings):
    elements = []

    radius = cmds.getAttr( "%s.%s" % (geometryShader, "radius"))
    zmin = cmds.getAttr( "%s.%s" % (geometryShader, "zmin"))
    zmax = cmds.getAttr( "%s.%s" % (geometryShader, "zmax"))
    phimax = cmds.getAttr( "%s.%s" % (geometryShader, "phimax"))

    shapeElement = SceneElement('Shape', "cylinder")
    shapeElement.addAttributeFloat("radius", radius)
    shapeElement.addAttributeFloat("zmin", zmin)
    shapeElement.addAttributeFloat("zmax", zmax)
    shapeElement.addAttributeFloat("phimax", phimax)

    elements.append( shapeElement )

    return elements

def createProceduralGeometryDisk(mayaObject, geometryShader, renderSettings):
    elements = []

    height = cmds.getAttr( "%s.%s" % (geometryShader, "height"))
    radius = cmds.getAttr( "%s.%s" % (geometryShader, "radius"))
    innerRadius = cmds.getAttr( "%s.%s" % (geometryShader, "innerRadius"))
    phimax = cmds.getAttr( "%s.%s" % (geometryShader, "phimax"))

    shapeElement = SceneElement('Shape', "disk")
    shapeElement.addAttributeFloat("height", height)
    shapeElement.addAttributeFloat("radius", radius)
    shapeElement.addAttributeFloat("innerradius", innerRadius)
    shapeElement.addAttributeFloat("phimax", phimax)

    elements.append( shapeElement )

    return elements

def createProceduralGeometryHyperboloid(mayaObject, geometryShader, renderSettings):
    elements = []

    p1 = cmds.getAttr( "%s.%s" % (geometryShader, "p1"))[0]
    p2 = cmds.getAttr( "%s.%s" % (geometryShader, "p2"))[0]
    phimax = cmds.getAttr( "%s.%s" % (geometryShader, "phimax"))

    shapeElement = SceneElement('Shape', "hyperboloid")
    shapeElement.addAttributePoint("p1", p1)
    shapeElement.addAttributePoint("p2", p2)
    shapeElement.addAttributeFloat("phimax", phimax)

    elements.append( shapeElement )

    return elements

def createProceduralGeometryParaboloid(mayaObject, geometryShader, renderSettings):
    elements = []

    radius = cmds.getAttr( "%s.%s" % (geometryShader, "radius"))
    zmin = cmds.getAttr( "%s.%s" % (geometryShader, "zmin"))
    zmax = cmds.getAttr( "%s.%s" % (geometryShader, "zmax"))
    phimax = cmds.getAttr( "%s.%s" % (geometryShader, "phimax"))

    shapeElement = SceneElement('Shape', "paraboloid")
    shapeElement.addAttributeFloat("radius", radius)
    shapeElement.addAttributeFloat("zmin", zmin)
    shapeElement.addAttributeFloat("zmax", zmax)
    shapeElement.addAttributeFloat("phimax", phimax)

    elements.append( shapeElement )

    return elements

def createProceduralGeometrySphere(mayaObject, geometryShader, renderSettings):
    elements = []

    radius = cmds.getAttr( "%s.%s" % (geometryShader, "radius"))
    zmin = cmds.getAttr( "%s.%s" % (geometryShader, "zmin"))
    zmax = cmds.getAttr( "%s.%s" % (geometryShader, "zmax"))
    phimax = cmds.getAttr( "%s.%s" % (geometryShader, "phimax"))

    shapeElement = SceneElement('Shape', "sphere")
    shapeElement.addAttributeFloat("radius", radius)
    shapeElement.addAttributeFloat("zmin", zmin)
    shapeElement.addAttributeFloat("zmax", zmax)
    shapeElement.addAttributeFloat("phimax", phimax)

    elements.append( shapeElement )

    return elements

def createProceduralGeometry(mayaObject, geometryShader, renderSettings):
    matType = cmds.nodeType(geometryShader)
    
    mayaMaterialTypeToShaderFunction = {
        "PBRTPlyMeshGeometry" : createProceduralGeometryPlyMesh,
        "PBRTConeGeometry" : createProceduralGeometryCone,
        "PBRTCylinderGeometry" : createProceduralGeometryCylinder,
        "PBRTDiskGeometry" : createProceduralGeometryDisk,
        "PBRTHyperboloidGeometry" : createProceduralGeometryHyperboloid,
        "PBRTParaboloidGeometry" : createProceduralGeometryParaboloid,
        "PBRTSphereGeometry" : createProceduralGeometrySphere,
        "PBRTIncludeGeometry" : createProceduralGeometryInclude,
    }

    if matType in mayaMaterialTypeToShaderFunction:
        if exportVerbosity:
            print( "Creating procedural procedural geometry : %s, type : %s." % (geometryShader, matType) )
        createProceduralFunction = mayaMaterialTypeToShaderFunction[matType]
    else:
        if exportVerbosity:
            print( "Skipping unsupported procedural geometry : %s." % matType)
        createProceduralFunction = None

    proceduralElements = []
    if createProceduralFunction:
        proceduralElements = createProceduralFunction(mayaObject, geometryShader, renderSettings)

    return proceduralElements

def createExportedGeometryReference(geomName, geomFilename, renderDir, renderSettings):
    extension = os.path.splitext(geomFilename)[-1][1:]
    geometryIsPly = (extension == "ply")

    if exportVerbosity:
        print( "geom filename : %s" % geomFilename)

    element = None
    if geometryIsPly:
        geomFilenameRelative = os.path.relpath( geomFilename, renderDir )
        shapeElement = SceneElement('Shape', "plymesh")
        shapeElement.addAttributeString("filename", geomFilenameRelative)

        alpha = cmds.getAttr(geomName+".primaryVisibility")
        shadowalpha = cmds.getAttr(geomName+".castsShadows")

        shapeElement.addAttributeFloat("alpha", alpha)

        PBRTVersion = cmds.getAttr("%s.%s" % (renderSettings, "PBRTVersion"))
        if PBRTVersion != "v3 Book":
            shapeElement.addAttributeFloat("shadowalpha", shadowalpha)
        element = shapeElement

    else:
        geomFilenameRelative = os.path.relpath( geomFilename, renderDir )
        objectIncludeElement = SceneElement('Include', geomFilenameRelative)
        element = objectIncludeElement

    return element

def createMaterialReference(surfaceShader, materialElements):
    materialType = cmds.nodeType(surfaceShader)
    if materialType == "PBRTDiffuseAreaLight":
        (materialElements, textureElements) = createMaterial(surfaceShader, surfaceShader)
        element = materialElements[-1]
    else:
        element = NamedMaterialElement(surfaceShader)
    return element

def createMediumReference(insideMediumShader=None, outsideMediumShader=None):
    element = NamedMediumElement(insideMediumShader, outsideMediumShader)
    return element

def createObject(geomFilename, 
    surfaceShader, 
    volumeShader,
    geometryShader,
    renderDir,
    materialElements, 
    geomName,
    renderSettings):

    materialElement = None
    if surfaceShader:
        materialElement = createMaterialReference(surfaceShader, materialElements)

    mediumElement = None
    if volumeShader:
        mediumElement = createMediumReference(volumeShader)

    objectElement = None

    # Instance-able object or regular Attribute block
    if materialElement:
        # Area lights aren't instanced
        if materialElement['identifier'] == "AreaLightSource":
            if exportVerbosity:
                print( "Creating an Attribute element for %s" % geomName )
            objectElement = AttributeElement()

            # Add in transform to place light
            transforms = createTransformsFromMayaObject(geomName, renderSettings)
            objectElement.addChildren( transforms )

        # Geometry can be instanced
        else:
            if exportVerbosity:
                print( "Creating an Object element for %s" % geomName )
            objectElement = ObjectElement(geomName)

    elif mediumElement:
        if exportVerbosity:
            print( "Creating an Object element for %s" % geomName )

        objectElement = ObjectElement(geomName)
    else:
        if exportVerbosity:
            print( "Can't create object or attribute element for object %s without a material or medium assinged" % geomName )

    # Object declaration
    if objectElement:
        shape = cmds.listRelatives(geomName, shapes=True, fullPath=True)[0]
        comment = CommentElement("Maya Geometry : %s" % (shape) )
        objectElement.addChild( comment )

        if materialElement:
            objectElement.addChild( materialElement )

        if mediumElement:
            if not materialElement:
                materialElement = MaterialElement("")
                objectElement.addChild( materialElement )
            objectElement.addChild( mediumElement )

        if geometryShader:
            shapeElements = createProceduralGeometry(geomName, geometryShader, renderSettings)
            objectElement.addChildren( shapeElements )
        else:
            shapeElement = createExportedGeometryReference(geomName, geomFilename, renderDir, renderSettings)
            objectElement.addChild( shapeElement )

    return objectElement

def createTransformsFromMayaObject(xform, renderSettings):
    motionBlur = cmds.getAttr(renderSettings+".motionBlur")

    transformElements = []

    if motionBlur:
        if exportVerbosity:
            print( "Creating animated object transforms for motion blur" )

        currentFrame = cmds.currentTime(query=True)

        activeTransformElement1 = ActiveTransformElement("StartTime")
        transformElements.append( activeTransformElement1 )
 
        matrix = cmds.getAttr(xform+".worldMatrix")
        transform1 = TransformMatrixElement(matrix)
        transformElements.append( transform1 )

        cmds.currentTime(float(currentFrame+1))

        activeTransformElement1 = ActiveTransformElement("EndTime")
        transformElements.append( activeTransformElement1 )

        matrix = cmds.getAttr(xform+".worldMatrix")
        transform2 = TransformMatrixElement(matrix)
        transformElements.append( transform2 )

        activeTransformElement1 = ActiveTransformElement("All")
        transformElements.append( activeTransformElement1 )

        cmds.currentTime(float(currentFrame))
    else:
        if exportVerbosity:
            print( "Creating static object transforms" )

        matrix = cmds.getAttr(xform+".worldMatrix")
        transform = TransformMatrixElement(matrix)
        transformElements.append( transform )

    return transformElements

def createInstance(geomName, 
    addTransform, 
    renderSettings):
    objectInstanceElement = AttributeElement()

    comment = CommentElement("Maya Transform : %s" % (geomName) )
    objectInstanceElement.addChild( comment )

    if addTransform:
        transforms = createTransformsFromMayaObject(geomName, renderSettings)
        objectInstanceElement.addChildren( transforms )

    instance = ObjectInstanceElement(geomName)
    objectInstanceElement.addChild( instance )

    return objectInstanceElement

#
# Create a material
#
def createGeometryAndMaterials(renderDir, renderSettings):
    renderableObjectNames = getRenderableGeometry()

    (materialElements, 
     textureElements) = createMaterialElements(renderableObjectNames)

    exportedGeometryFiles = []
    shapeElements = []
    instanceElements = []

    # Used to keep a mapping between exported objects and files
    # In the case of instancing, a set of different objects will
    # point to one set of exported files so that set doesn't have
    # to be exported multiple times
    objectToExportedFiles = {}

    #Write each piece of geometry with references to materials
    for renderableObjectName in renderableObjectNames:
        if exportVerbosity:
            print( "Create Geometry And Materials" )
            print( "\tObject : %s" % renderableObjectName )
        surfaceShader = getSurfaceShader(renderableObjectName)
        volumeShader  = getVolumeShader(renderableObjectName)
        geometryShader  = getGeometryShader(renderableObjectName)

        if exportVerbosity:
            print( "\tSurface   : %s" % surfaceShader )
            print( "\tVolume    : %s" % volumeShader )
            print( "\tGeometry  : %s" % geometryShader )

        geomFilename = None
        if not geometryShader:
            geomFilenames = exportGeometry(renderableObjectName, 
                renderDir, 
                objectToExportedFiles,
                renderSettings)
            geomFilename = geomFilenames[-1]
            exportedGeometryFiles.extend(geomFilenames)

        shapeElement = createObject(geomFilename, 
            surfaceShader, 
            volumeShader, 
            geometryShader,
            renderDir, 
            materialElements, 
            renderableObjectName,
            renderSettings)
        shapeElements.append(shapeElement)

        # Instanced geometry
        # - Area lights aren't instanced
        # - Geometry can be instanced
        if shapeElement['identifier'] == "Object":
            # Only support transforms on procedural geometry or ply-exports 
            translators = cmds.pluginInfo( "PBRTForMaya", query=True, translator=True )
            usePLYExport = cmds.getAttr( "%s.%s" % (renderSettings, "usePLYExport"))
            usePLYExport = usePLYExport and translators and 'ply' in translators

            # when motion blur is on
            #motionBlur = cmds.getAttr( "%s.%s" % (renderSettings, "motionBlur"))
            #addTransform = (geometryShader is not None) or (usePLYExport and motionBlur)
            addTransform = (geometryShader is not None) or usePLYExport

            instanceElement = createInstance(renderableObjectName, 
                addTransform, 
                renderSettings)
            shapeElements.append(instanceElement)

    return (exportedGeometryFiles, shapeElements, instanceElements, materialElements, textureElements)

def createHeaderComments(renderSettings):
    #date = datetime.datetime.now()
    #(user, sysname, nodename, release, version, 
    #    machine, processor) = getOperatingEnvironment()
    #comment1 = CommentElement( "Exported by PBRTForMaya at %s on machine %s" % (date, nodename) )

    PBRTVersion = cmds.getAttr("%s.%s" % (renderSettings, "PBRTVersion"))
    comment2 = CommentElement( "Exported for PBRT Version : %s" % PBRTVersion )

    return [comment2]

def createMotionBlur(renderSettings):
    motionBlur = cmds.getAttr(renderSettings+".motionBlur")

    motionBlurElements = None
    if motionBlur:
        motionBlurElements = []

        comment = CommentElement( "Motion Blur shutter open and close" )
        motionBlurElements.append( comment )

        transformTimesElement = TransformTimesElement([0.0, 1.0])
        motionBlurElements.append( transformTimesElement )

    return motionBlurElements

def createGlobalVolume(renderSettings):
    def getGlobalVolume():
        # Build list of visible geometry
        availableLocators = cmds.ls(type="nurbsSurface", long=True)
        globalVolume = None
        for locator in availableLocators:
            if 'globalVolume' in locator:
                globalVolume = cmds.listRelatives(locator, allParents=True, fullPath=True)[0]
                break
        return globalVolume

    globalVolumeElements = []

    globalVolumeNode = getGlobalVolume()
    if globalVolumeNode and isVisible(globalVolumeNode):
        if exportVerbosity:
            print( "Global Volume Node : %s" % globalVolumeNode )
        medium = getVolumeShader(globalVolumeNode)
        materialType = cmds.nodeType(medium)

        if( materialType in materialNodeTypes ):
            if exportVerbosity:
                print( "Global Volume Shader : %s, %s" % (medium, materialType) )
            globalMediumName = "%s_global" % medium

            (mediumElements, 
             textureElements) = createMaterial(medium, globalMediumName)

            globalVolumeElements.extend(textureElements)
            globalVolumeElements.extend(mediumElements)

            mediumReferenceElement = createMediumReference(insideMediumShader="", outsideMediumShader=globalMediumName)

            globalVolumeElements.append( mediumReferenceElement )

    return globalVolumeElements

def addSettings(sceneElement, renderSettings):
    comments = createHeaderComments(renderSettings)
    sceneElement.addChildren( comments, separator=True, separateEvery=False )

    # Create film, sampler, filter, integrator, accelerator
    filmElement = createFilm(renderSettings)
    sceneElement.addChild( filmElement, separator=True )

    samplerElement = createSampler(renderSettings)
    sceneElement.addChild( samplerElement, separator=True )

    filterElement = createFilter(renderSettings)
    sceneElement.addChild( filterElement, separator=True )

    integratorElement = createIntegrator(renderSettings)
    sceneElement.addChild( integratorElement, separator=True )

    acceleratorElement = createAccelerator(renderSettings)
    sceneElement.addChild( acceleratorElement, separator=True )

    motionBlurElement = createMotionBlur(renderSettings)
    if motionBlurElement:
        sceneElement.addChildren( motionBlurElement, separator=True, separateEvery=False )

    # Create global volume element
    globalVolumeElements = createGlobalVolume(renderSettings)
    if globalVolumeElements:
        sceneElement.addChildren( globalVolumeElements, separator=True )

#
# Create and write whole scene
#
def exportScene(outFileName, exportDir, renderSettings, verboseExport=False):
    global renderDir
    renderDir = exportDir

    global exportVerbosity
    exportVerbosity = 1 if cmds.getAttr("%s.%s" % (renderSettings, "verboseExport")) else 0

    #
    # Generate scene element hierarchy
    #
    sceneElement = SceneElement()

    #
    # Add general settings
    #
    pbrtSettings = addSettings(sceneElement, renderSettings)

    # Create Camera
    cameraElements = createCamera(renderSettings)
    sceneElement.addChildren( cameraElements, separator=True, separateEvery=False )

    #
    # Create the World - includes Lights, Textures, Materials, Objects
    #
    worldElement = WorldElement()

    # Create lights
    lightElements = createLightElements()
    if lightElements:
        worldElement.addChildren( lightElements, separator=True )

    # Create geometry, texture and material assignments
    (exportedGeometryFiles, 
     shapeElements, 
     instanceElements,
     materialElements,
     textureElements) = createGeometryAndMaterials(renderDir, renderSettings)

    if textureElements:
        worldElement.addChildren( textureElements, separator=True )

    if materialElements:
        worldElement.addChildren( materialElements, separator=True )

    if shapeElements:
        worldElement.addChildren( shapeElements, separator=True )

    if instanceElements:
        worldElement.addChildren( instanceElements, separator=True )

    sceneElement.addChild( worldElement )

    #
    # Write the structure to disk
    #
    with open(outFileName, 'w+') as outFile:
        sceneElement.write(outFile)

    return exportedGeometryFiles

