import inspect
import os
import pkgutil
import sys

import maya.cmds as cmds
import maya.OpenMayaMPx as OpenMayaMPx

kPluginName = "PBRTForMaya"
kPluginCompany = "Duiker Research"

from util.mayautil import createMelPythonCallback

# Make sure translator modules can be found
pluginDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.join(pluginDir, "translators"))

# Import modules for renderer, settings, material, lights and volumes
from renderer import (
    PBRTRenderSettings,
    PBRTRenderer)

from translators import (
    ply)

import lights
import materials
import shapes
import textures
import volumes

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

global rendererModules
global generalNodeModules
global shadingNodeGroups

rendererModules = [
    PBRTRenderer]

generalNodeModules = [
    PBRTRenderSettings]

translatorModules = [
    ply]

# Get the modules in materials, lights, textures, volumes
materialsPath = os.path.dirname(materials.__file__)
materialsNodeNames = [name for _, name, _ in pkgutil.iter_modules([materialsPath])]

lightsPath = os.path.dirname(lights.__file__)
lightsNodeNames = [name for _, name, _ in pkgutil.iter_modules([lightsPath])]

texturesPath = os.path.dirname(textures.__file__)
texturesNodeNames = [name for _, name, _ in pkgutil.iter_modules([texturesPath])]

volumesPath = os.path.dirname(volumes.__file__)
volumesNodeNames = [name for _, name, _ in pkgutil.iter_modules([volumesPath])]

shapesPath = os.path.dirname(shapes.__file__)
shapesNodeNames = [name for _, name, _ in pkgutil.iter_modules([shapesPath])]

shadingNodeGroups = { 
    'materials' : materialsNodeNames,
    'lights' : lightsNodeNames,
    'textures' : texturesNodeNames,
    'volumes' : volumesNodeNames,
    'shapes' : shapesNodeNames,
}

#
# AE Templates
#
from templates import (
    AEPBRTFourierMaterialTemplate,
    AEPBRTPlyMeshGeometryTemplate,
    AEPBRTIncludeGeometryTemplate,
    AEPBRTHeterogeneousMediumTemplate)

# Initialize the script plug-in
def initializePlugin(mobject):
    global rendererModules
    global generalNodeModules
    global shadingNodeGroups
    global translatorModules

    mplugin = OpenMayaMPx.MFnPlugin(mobject, kPluginCompany, "1.0", "Any")

    # Load needed plugins
    neededPlugins = ["objExport", "OpenEXRLoader"]

    for neededPlugin in neededPlugins:
        try:
            if not cmds.pluginInfo( neededPlugin, query=True, loaded=True ):
                cmds.loadPlugin( neededPlugin )
            print( "%s - Loaded plugin       : %s" % (kPluginName, neededPlugin))
        except:
                sys.stderr.write( "Failed to load %s plugin\n" % neededPlugin)
                raise

    # Register translator nodes
    try:
        for translatorModule in translatorModules:
            moduleName = os.path.split( inspect.getfile(translatorModule) )[-1].split('.')[0]

            translatorOptions = None
            if translatorModule.kPluginTranslatorOptionsUIFunction:
                translatorOptions = createMelPythonCallback(
                    moduleName, 
                    translatorModule.kPluginTranslatorOptionsUIFunction,
                    parametersList=[('string', 'parent'), 
                        ('string', 'action'), 
                        ('string', 'initialSettings'), 
                        ('string', 'resultCallback')],
                    returnType="int")

            mplugin.registerFileTranslator( translatorModule.kPluginTranslatorTypeName, 
                None, 
                translatorModule.translatorCreator,
                translatorOptions,
                translatorModule.kPluginTranslatorDefaultOptions)
            print( "%s - Registered translator : %s" % (kPluginName, 
                translatorModule.kPluginTranslatorTypeName))
    except:
            sys.stderr.write( "%s - Failed to register node: %s\n" % (
                kPluginName, translatorModule.kPluginTranslatorTypeName) )
            raise

    # Register general nodes
    try:
        for generalNodeModule in generalNodeModules:
            mplugin.registerNode( generalNodeModule.kPluginNodeName, 
                generalNodeModule.kPluginNodeId, 
                generalNodeModule.nodeCreator, 
                generalNodeModule.nodeInitializer, 
                OpenMayaMPx.MPxNode.kDependNode )
            print( "%s - Registered node     : %s" % (kPluginName, generalNodeModule.kPluginNodeName))
    except:
            sys.stderr.write( "%s - Failed to register node: %s\n" % (kPluginName, generalNodeModule.kPluginNodeName) )
            raise

    # Register materials, textures, volumes, lights
    for shadingModule, shadingNodeNames in shadingNodeGroups.iteritems():
        #print( "%s - Registering %s nodes" % (kPluginName, shadingModule) )

        for shadingNodeName in shadingNodeNames:
            try:
                #print( "Registering %s" % shadingNodeName )

                node = None
                try:
                    __import__(shadingModule, fromlist=[shadingNodeName])
                    module = sys.modules[shadingModule+'.'+shadingNodeName]
                    reload(module)
                    node = module
                except ImportError:
                    OpenMaya.MGlobal.displayError( "Failed to load %s" % (shadingModule+'.'+shadingNodeName) )
               
                # abstract node classes should return None in nodeName() method
                if node:
                    isNode = node.kPluginNodeName  
                    if isNode is None:
                        #print( "isNode == None" )
                        continue

                mplugin.registerNode( node.kPluginNodeName, 
                    node.kPluginNodeId, 
                    node.nodeCreator, 
                    node.nodeInitializer, 
                    OpenMayaMPx.MPxNode.kDependNode, 
                    node.kPluginNodeClassify )

                PBRTRenderer.registMaterialNodeType(node.kPluginNodeName)

                print( "%s - Registered %s : %s" % (kPluginName, shadingModule, node.kPluginNodeName) )
            except:
                    sys.stderr.write( "%s - Failed to register node: %s\n" % (kPluginName, shadingNodeName) )
                    raise

    # Register Renderer commands
    for rendererModule in rendererModules:
        try:
            mplugin.registerCommand( rendererModule.kPluginCmdName, rendererModule.cmdCreator )
            print( "%s - Registered command  : %s" % (kPluginName, rendererModule.kPluginCmdName) )
        except:
            sys.stderr.write( "%s - Failed to register command: %s\n" % (kPluginName, rendererModule.kPluginCmdName) )
            raise

    # Register Renderers
    for rendererModule in rendererModules:
        try:
            rendererModule.registerRenderer()
            print( "%s - Registered renderer : %s" % (kPluginName, rendererModule.kPluginCmdName) )
        except:
            sys.stderr.write( "%s - Failed to register renderer: %s\n" % (kPluginName, rendererModule.kPluginCmdName) )
            raise

# Uninitialize the script plug-in
def uninitializePlugin(mobject):
    global rendererModules
    global generalNodeModules
    global shadingNodeGroups
    global translatorModules

    mplugin = OpenMayaMPx.MFnPlugin(mobject, kPluginCompany, "1.0", "Any")

    for rendererModule in rendererModules:
        try:
            cmds.renderer(rendererModule.kPluginCmdName, edit=True, unregisterRenderer=True)
        except:
            sys.stderr.write( "Failed to unregister renderer: %s\n" % rendererModule.kPluginCmdName )

        try:
            mplugin.deregisterCommand( rendererModule.kPluginCmdName )
        except:
            sys.stderr.write( "Failed to unregister command: %s\n" % rendererModule.kPluginCmdName )

    # Unregister materials, textures, volumes, lights
    for shadingModule, shadingNodeNames in shadingNodeGroups.iteritems():
        print( "%s - Unegistering %s nodes" % (kPluginName, shadingModule) )

        for shadingNodeName in shadingNodeNames:
            try:
                node = None
                try:
                    __import__(shadingModule, fromlist=[shadingNodeName])
                    module = sys.modules[shadingModule+'.'+shadingNodeName]
                    reload(module)
                    node = module
                except ImportError:
                    OpenMaya.MGlobal.displayError( "Failed to load %s" % (shadingModule+'.'+shadingNodeName) )

                if node:
                    mplugin.deregisterNode( node.kPluginNodeId )
            except:
                sys.stderr.write( "Failed to unregister node: %s\n" % (shadingModule+'.'+shadingNodeName) )
                raise

    # Unregister general nodes
    try:
        for generalNodeModule in generalNodeModules:
            mplugin.deregisterNode( generalNodeModule.kPluginNodeId )
    except:
            sys.stderr.write( "Failed to unregister node: %s\n" % generalNodeModule.kPluginNodeName )
            raise

    # Unregister translator nodes
    try:
        for translatorModule in translatorModules:
            mplugin.deregisterFileTranslator( translatorModule.kPluginTranslatorTypeName )
    except:
            sys.stderr.write( "Failed to unregister node: %s\n" % translatorModule.kPluginTranslatorTypeName )
            raise

