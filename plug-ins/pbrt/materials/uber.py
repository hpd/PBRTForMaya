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

kPluginNodeName = "PBRTUberMaterial"
kPluginNodeClassify = "shader/surface"
kPluginNodeId = OpenMaya.MTypeId(0x87043)

class uber(OpenMayaMPx.MPxNode):
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        mKd = OpenMaya.MObject()
        mKs = OpenMaya.MObject()
        mKr = OpenMaya.MObject()

        mRoughness = OpenMaya.MObject()
        mIndex = OpenMaya.MObject()

        mOpacity = OpenMaya.MObject()

        mRemapRoughness = OpenMaya.MObject()
        mURoughness = OpenMaya.MObject()
        mVRoughness = OpenMaya.MObject()
        mBump = OpenMaya.MObject()

        mOutColor = OpenMaya.MObject()

    def compute(self, plug, block):
        if plug == uber.mOutColor:
            resultColor = OpenMaya.MFloatVector(0.0,0.0,0.0)
            
            outColorHandle = block.outputValue( uber.mOutColor )
            outColorHandle.setMFloatVector(resultColor)
            outColorHandle.setClean()
        else:
            return OpenMaya.kUnknownParameter


def nodeCreator():
    return uber()

def nodeInitializer():
    nAttr = OpenMaya.MFnNumericAttribute()
    eAttr = OpenMaya.MFnEnumAttribute()

    try:
        uber.mKd = nAttr.createColor("Kd", "kd")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.25,0.25,0.25)

        uber.mKs = nAttr.createColor("Ks", "ks")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.25,0.25,0.25)

        uber.mKr = nAttr.createColor("Kr", "kr")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.0,0.0,0.0)

        uber.mRoughness = nAttr.create("roughness","r", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.1)

        uber.mIndex = nAttr.create("index","i", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(1.5)

        uber.mOpacity = nAttr.createColor("opacity", "o")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(1.0,1.0,1.0)

        uber.mRemapRoughness = nAttr.create("remapRoughness", "rr", OpenMaya.MFnNumericData.kBoolean, True)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)

        uber.mURoughness = nAttr.create("uRoughness","ur", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(-1.0)

        uber.mVRoughness = nAttr.create("vRoughness","vr", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(-1.0)

        uber.mBump = nAttr.create("bumpmap", "b", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(-1.0)

        uber.mOutColor = nAttr.createColor("outColor", "oc")
        nAttr.setStorable(0)
        nAttr.setHidden(0)
        nAttr.setReadable(1)
        nAttr.setWritable(0)
    except:
        sys.stderr.write("Failed to create attributes\n")
        raise

    try:
        uber.addAttribute(uber.mKd)
        uber.addAttribute(uber.mKs)
        uber.addAttribute(uber.mKr)
        uber.addAttribute(uber.mRoughness)
        uber.addAttribute(uber.mIndex)
        uber.addAttribute(uber.mOpacity)
        uber.addAttribute(uber.mRemapRoughness)
        uber.addAttribute(uber.mURoughness)
        uber.addAttribute(uber.mVRoughness)
        uber.addAttribute(uber.mBump)
        uber.addAttribute(uber.mOutColor)
    except:
        sys.stderr.write("Failed to add attributes\n")
        raise

    try:
        uber.attributeAffects (uber.mKd, uber.mOutColor)
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
