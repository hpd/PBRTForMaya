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

kPluginNodeName = "PBRTMarbleTexture"
kPluginNodeClassify = "texture/3d"
kPluginNodeId = OpenMaya.MTypeId(0x87066)

class marble(OpenMayaMPx.MPxNode):
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        mOctaves = OpenMaya.MObject()
        mRoughness = OpenMaya.MObject()

        mNScale = OpenMaya.MObject()
        mVariation = OpenMaya.MObject()

        mPlacementMatrix = OpenMaya.MObject()

        mOutColor = OpenMaya.MObject()

    def compute(self, plug, block):
        if plug == marble.mOutColor:
            resultColor = OpenMaya.MFloatVector(0.0,0.0,0.0)
            
            outColorHandle = block.outputValue( marble.mOutColor )
            outColorHandle.setMFloatVector(resultColor)
            outColorHandle.setClean()
        else:
            return OpenMaya.kUnknownParameter


def nodeCreator():
    return marble()

def nodeInitializer():
    nAttr = OpenMaya.MFnNumericAttribute()
    mAttr = OpenMaya.MFnMatrixAttribute()

    try:
        marble.mOctaves = nAttr.create("octaves","oct", OpenMaya.MFnNumericData.kInt, 8)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)

        marble.mRoughness = nAttr.create("roughness","rg", OpenMaya.MFnNumericData.kFloat, 0.5)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)

        marble.mNScale = nAttr.create("noiseScale","nsc", OpenMaya.MFnNumericData.kFloat, 1.0)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)

        marble.mVariation = nAttr.create("variation","vr", OpenMaya.MFnNumericData.kFloat, 0.2)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)

        marble.mPlacementMatrix = mAttr.create("placementMatrix", "pm", OpenMaya.MFnMatrixAttribute.kFloat);
        mAttr.setKeyable(1) 
        mAttr.setStorable(1)
        mAttr.setReadable(1)
        mAttr.setWritable(1)

        marble.mOutColor = nAttr.createColor("outColor", "oc")
        nAttr.setStorable(0)
        nAttr.setHidden(0)
        nAttr.setReadable(1)
        nAttr.setWritable(0)
    except:
        sys.stderr.write("Failed to create attributes\n")
        raise

    try:
        marble.addAttribute(marble.mOctaves)
        marble.addAttribute(marble.mRoughness)
        marble.addAttribute(marble.mNScale)
        marble.addAttribute(marble.mVariation)

        marble.addAttribute(marble.mPlacementMatrix)

        marble.addAttribute(marble.mOutColor)
    except:
        sys.stderr.write("Failed to add attributes\n")
        raise

    try:
        marble.attributeAffects (marble.mOctaves, marble.mOutColor)
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
