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

kPluginNodeName = "PBRTuv"
kPluginNodeClassify = "texture/2d"
kPluginNodeId = OpenMaya.MTypeId(0x8706A)

class uv(OpenMayaMPx.MPxNode):
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)

        # Attributes needed to support UV placement
        mUVCoord = OpenMaya.MObject()
        mUVFilterSize = OpenMaya.MObject()

        mOutColor = OpenMaya.MObject()

    def compute(self, plug, block):
        if plug == uv.mOutColor:
            resultColor = OpenMaya.MFloatVector(0.0,0.0,0.0)
            
            outColorHandle = block.outputValue( uv.mOutColor )
            outColorHandle.setMFloatVector(resultColor)
            outColorHandle.setClean()
        else:
            return OpenMaya.kUnknownParameter


def nodeCreator():
    return uv()

def nodeInitializer():
    nAttr = OpenMaya.MFnNumericAttribute()

    try:
        # Attribute needed to support UV placement
        child1 = nAttr.create("uCoord","u", OpenMaya.MFnNumericData.kFloat)
        child2 = nAttr.create("vCoord","v", OpenMaya.MFnNumericData.kFloat)
        uv.mUVCoord = nAttr.create("uvCoord","uv", child1, child2)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)

        # Attribute needed to support UV placement
        child1 = nAttr.create("uvFilterSizeX","fsx", OpenMaya.MFnNumericData.kFloat)
        child2 = nAttr.create("uvFilterSizeY","fsy", OpenMaya.MFnNumericData.kFloat)
        uv.mUVFilterSize = nAttr.create("uvFilterSize","fx", child1, child2)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)

        uv.mOutColor = nAttr.createColor("outColor", "oc")
        nAttr.setStorable(0)
        nAttr.setHidden(0)
        nAttr.setReadable(1)
        nAttr.setWritable(0)
    except:
        sys.stderr.write("Failed to create attributes\n")
        raise

    try:
        uv.addAttribute(uv.mUVCoord)
        uv.addAttribute(uv.mUVFilterSize)
        uv.addAttribute(uv.mOutColor)
    except:
        sys.stderr.write("Failed to add attributes\n")
        raise

    try:
        uv.attributeAffects (uv.mUVCoord, uv.mOutColor)
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
