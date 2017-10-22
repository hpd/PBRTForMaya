#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

#
# PBRT Scene Elements
#
def listToText(list):
    return " ".join( map(str, list) )

def booleanToText(b):
    if b:
        return "true"
    else:
        return "false"

class SceneElement(dict):
    def __init__(self, identifier=None, pluginType=None, attributes=None, *args):
        dict.__init__(self, args)
        self.children = []
        self.attributes = {}
        dict.__setitem__(self, 'children', self.children )
        dict.__setitem__(self, 'attributes', self.attributes )
        dict.__setitem__(self, 'identifier', identifier )
        dict.__setitem__(self, 'plugin', pluginType )
        if attributes:
            for key, value in attributes.iteritems():
                self.attributes[key] = value
        self.bracketed = False
        self.separator = False
      
    def addChild(self, child, separator=False):
        if separator:
            child.separator = True

        self.children.append( child )
         
    def addChildren(self, children, separator=False, separateEvery=True):
        if separator:
            if separateEvery:
                for child in children:
                    child.separator = True
            else:
                children[-1].separator = True

        self.children.extend( children )

    def getChild(self, index):
        return self.children[index]
        
    def addAttribute(self, key, value):
        self.attributes[key] = value

    def addAttributeRGB(self, key, value):
        self.addAttribute(key, {'type':'rgb', 'value':listToText(value)})

    def addAttributeSpectrum(self, key, value):
        self.addAttribute(key, {'type':'spectrum', 'value':value})

    def addAttributeBlackBody(self, key, value):
        self.addAttribute(key, {'type':'blackbody', 'value':value})

    def addAttributeXYZ(self, key, value):
        self.addAttribute(key, {'type':'xyz', 'value':value})

    def addAttributePoint(self, key, value):
        self.addAttribute(key, {'type':'point', 'value':listToText(value)})

    def addAttributeFloat(self, key, value):
        if type(value) is list or type(value) is tuple:
            self.addAttribute(key, {'type':'float', 'value':listToText(value)})
        else:
            self.addAttribute(key, {'type':'float', 'value':float(value)})

    def addAttributeInteger(self, key, value):
        if type(value) is list or type(value) is tuple:
            self.addAttribute(key, {'type':'integer', 'value':listToText(value)})
        else:
            self.addAttribute(key, {'type':'integer', 'value':value})

    def addAttributeBoolean(self, key, value):
        self.addAttribute(key, {'type':'bool', 'value':"\"%s\"" % booleanToText(value)})

    def addAttributeString(self, key, value):
        self.addAttribute(key, {'type':'string', 'value':"\"%s\"" % value})

    def addAttributeTexture(self, key, value):
        self.addAttribute(key, {'type':'texture', 'value':"\"%s\"" % value})

    def removeAttribute(self, key):
        if key in self.attributes:
            del( self.attributes[key] )         

    def getAttribute(self, key):
        if key in self.attributes:
            return self.attributes[key]
        else:
            return None

    def formatPlugin(self, plugin, spacing=None):
        return "\"%s\"" % plugin

    def writeElementText(self, depth=0):
        #print( "element : %s" % str(element) )
        element = self

        if 'attributes' in element:
            attributes = element['attributes']
        else:
            attributes = {}
        if 'children' in element:
            children = element['children']
        else:
            children = []

        identifierName = element['identifier']

        spacing = '\t'*max(0, depth)

        elementText = ""
        if identifierName:
            #print( "id : %s" % identifierName )
            elementText += spacing + "%s" % identifierName
            if self.bracketed:
                elementText += "Begin"
                #elementText += "\n"

            if element['plugin'] is not None:
                elementText += " %s" % self.formatPlugin(element['plugin'], spacing=spacing)

            elementText += "\n"

            if attributes:
                for paramName, paramValues in attributes.iteritems():
                    paramType = paramValues['type']
                    paramValue = paramValues['value']

                    elementText += "%s\"%s %s\" [%s]" % ('\t'*(depth+1), paramType, paramName, paramValue)
                    elementText += "\n"

        if children:
            for child in children:
                #print( "child : %s" % str(child) )
                elementText += child.writeElementText(depth+1)
        
        if identifierName:
            if self.bracketed:
                elementText += "%sEnd\n" % (spacing + identifierName)

        # Simple formatting cheat to make the files a little more readable
        if element.separator:
            elementText += "\n"

        return elementText

    # Other options to be provided later
    def write(self, outFile, depth=0):
        elementText = self.writeElementText(depth=depth-1)
        outFile.write(elementText)

def WorldElement():
    element = SceneElement('World')
    element.bracketed = True
    return element

def AttributeElement():
    element = SceneElement('Attribute')
    element.bracketed = True
    return element

def ObjectElement(objectName):
    element = SceneElement('Object', objectName)
    element.bracketed = True
    return element

def ObjectInstanceElement(objectName):
    element = SceneElement('ObjectInstance', objectName)
    return element

def FilmElement(filmName):
    elementDict = SceneElement('Film', filmName )
    return elementDict

def CameraElement(cameraType):
    elementDict = SceneElement('Camera', cameraType )
    return elementDict

def LightElement(lightPluginType):
    return SceneElement('LightSource', lightPluginType)

def MaterialElement(materialPluginType):
    elementDict = SceneElement('Material', materialPluginType )
    return elementDict

def MakeNamedMaterialElement(materialName, materialPluginType):
    elementDict = SceneElement('MakeNamedMaterial', materialName )
    elementDict.addAttributeString('type', materialPluginType)
    return elementDict

def NamedMaterialElement(materialName):
    return SceneElement('NamedMaterial', materialName )

def MakeNamedMediumElement(mediumName, materialPluginType):
    elementDict = SceneElement('MakeNamedMedium', mediumName )
    elementDict.addAttributeString('type', materialPluginType)
    return elementDict

class MediumElement(SceneElement):
    def __init__(self, outside, inside, attributes=None):
        SceneElement.__init__(self, identifier='MediumInterface', pluginType=outside, 
            attributes=attributes)
        self.inside = inside
 
    def formatPlugin(self, plugin, spacing=None):
        inside = "" if self.inside is None else self.inside
        outside = "" if plugin is None else plugin
        return "\"%s\" \"%s\"" % (outside, inside)

def NamedMediumElement(mediumNameInside, mediumNameOutside=None):
    return MediumElement(mediumNameInside, mediumNameOutside)

class ActiveTransformElement(SceneElement):
    def __init__(self, activeTime, attributes=None):
        SceneElement.__init__(self, 'ActiveTransform', activeTime, attributes=attributes)

    def formatPlugin(self, plugin, spacing=None):
        return plugin

class TransformElement(SceneElement):
    def __init__(self, identifier, transformParameters=None, attributes=None):
        SceneElement.__init__(self, identifier, transformParameters, attributes)

    def formatPlugin(self, plugin, spacing=None):
        return " ".join(plugin)

class LookAtElement(SceneElement):
    def __init__(self, position, aim, up, attributes=None):
        values = []
        values.extend(position)
        values.extend(aim)
        values.extend(up)
        values = map(float, values)
        SceneElement.__init__(self, "LookAt", values, attributes)

    def formatPlugin(self, plugin, spacing=None):
        pluginf = map(lambda x: "%3.6f" % x, plugin)
        return " ".join(pluginf)

def TranslateElement(values):
    return TransformElement("Translate", map(str, values) )

def RotateElement(values):
    return TransformElement("Rotate", map(str, values) )

def ScaleElement(values):
    return TransformElement("Scale", map(str, values) )

def TransformTimesElement(values):
    return TransformElement("TransformTimes", map(str, values) )

class TransformMatrixElement(SceneElement):
    def __init__(self, transformParameters=None, attributes=None):
        SceneElement.__init__(self, "Transform", transformParameters, attributes)

    def formatPlugin(self, plugin, spacing=""):
        return "\n%s[%s\n%s %s\n%s %s\n%s %s]" % ( 
            spacing+"\t", " ".join(map(str, plugin[0:4])),
            spacing+"\t", " ".join(map(str, plugin[4:8])),
            spacing+"\t", " ".join(map(str, plugin[8:12])),
            spacing+"\t", " ".join(map(str, plugin[12:16])))

def CommentElement(comment):
    elementDict = TransformElement('#', [comment] )
    return elementDict

class TextureElement(SceneElement):
    def __init__(self, name, pixelType, plugin, attributes=None):
        SceneElement.__init__(self, identifier='Texture', pluginType=name, 
            attributes=attributes)
        self.pixelType = pixelType
        self.texturePlugin = plugin

    def formatPlugin(self, plugin, spacing=None):
        return "\"%s\" \"%s\" \"%s\"" % (plugin, self.pixelType, self.texturePlugin)

def ImageMapTextureElement(name, pixelType, path):
    elementDict = TextureElement(name, pixelType, 'imagemap')
    elementDict.addAttributeString('filename', path)
    return elementDict

def PtexTextureElement(name, pixelType, path):
    elementDict = TextureElement(name, pixelType, 'ptex')
    elementDict.addAttributeString('filename', path)
    return elementDict

class MatrixTextureElement(TextureElement):
    def __init__(self, name, pixelType, plugin, matrix, attributes=None):
        SceneElement.__init__(self, identifier='Transform', pluginType=name)
        self.pixelType = pixelType
        self.texturePlugin = plugin
        self.bracketed = True

        # Placement matrix
        matrixElement = TransformMatrixElement(matrix)
        self.addChild( matrixElement )

        # Add child texture element
        textureElement = TextureElement(name, pixelType, plugin, 
            attributes=attributes)
        self.addChild( textureElement )
        self.textureElement = textureElement
        self.texturePlugin = plugin

    def addAttribute(self, key, value):
        self.textureElement.attributes[key] = value

    def formatPlugin(self, plugin, spacing=None):
        return " "
