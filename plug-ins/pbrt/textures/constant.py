import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.cmds as cmds

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

kPluginNodeName = "PBRTConstantTexture"
kPluginNodeClassify = "texture/2d"
kPluginNodeId = OpenMaya.MTypeId(0x87063)

class constant(OpenMayaMPx.MPxNode):
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        mValue = OpenMaya.MObject()

        # Attributes needed to support UV placement
        mUVCoord = OpenMaya.MObject()
        mUVFilterSize = OpenMaya.MObject()

        mOutColor = OpenMaya.MObject()

    def compute(self, plug, block):
        if plug == constant.mOutColor:
            resultColor = OpenMaya.MFloatVector(0.0,0.0,0.0)
            
            outColorHandle = block.outputValue( constant.mOutColor )
            outColorHandle.setMFloatVector(resultColor)
            outColorHandle.setClean()
        else:
            return OpenMaya.kUnknownParameter


def nodeCreator():
    return constant()

def nodeInitializer():
    nAttr = OpenMaya.MFnNumericAttribute()

    try:
        constant.mValue = nAttr.createColor("value", "val")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)
        nAttr.setDefault(1.0, 1.0, 1.0)

        # Attribute needed to support UV placement
        child1 = nAttr.create("uCoord","u", OpenMaya.MFnNumericData.kFloat)
        child2 = nAttr.create("vCoord","v", OpenMaya.MFnNumericData.kFloat)
        constant.mUVCoord = nAttr.create("uvCoord","uv", child1, child2)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)

        # Attribute needed to support UV placement
        child1 = nAttr.create("uvFilterSizeX","fsx", OpenMaya.MFnNumericData.kFloat)
        child2 = nAttr.create("uvFilterSizeY","fsy", OpenMaya.MFnNumericData.kFloat)
        constant.mUVFilterSize = nAttr.create("uvFilterSize","fx", child1, child2)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)

        constant.mOutColor = nAttr.createColor("outColor", "oc")
        nAttr.setStorable(0)
        nAttr.setHidden(0)
        nAttr.setReadable(1)
        nAttr.setWritable(0)
    except:
        sys.stderr.write("Failed to create attributes\n")
        raise

    try:
        constant.addAttribute(constant.mValue)

        constant.addAttribute(constant.mUVCoord)
        constant.addAttribute(constant.mUVFilterSize)

        constant.addAttribute(constant.mOutColor)
    except:
        sys.stderr.write("Failed to add attributes\n")
        raise

    try:
        constant.attributeAffects (constant.mValue, constant.mOutColor)
    except:
        sys.stderr.write("Failed in setting attributeAffects\n")
        raise


# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerNode( kPluginNodeName, kPluginNodeId, nodeCreator, 
                    nodeInitializer, OpenMayaMPx.MPxNode.kDependNode, kPluginNodeClassify )
    except:
        sys.stderr.write( "Failed to register node: %s" % kPluginNodeName )
        raise

# uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( kPluginNodeId )
    except:
        sys.stderr.write( "Failed to deregister node: %s" % kPluginNodeName )
        raise
