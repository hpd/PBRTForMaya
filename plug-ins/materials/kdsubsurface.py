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

kPluginNodeName = "PBRTKDSubSurfaceMaterial"
kPluginNodeClassify = "shader/surface"
kPluginNodeId = OpenMaya.MTypeId(0x8704A)

class kdsubsurface(OpenMayaMPx.MPxNode):
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        mKd = OpenMaya.MObject()
        mMfp = OpenMaya.MObject()
        mKr = OpenMaya.MObject()
        mKt = OpenMaya.MObject()

        mEta = OpenMaya.MObject()
        mScale = OpenMaya.MObject()
        mG = OpenMaya.MObject()

        mRemapRoughness = OpenMaya.MObject()
        mURoughness = OpenMaya.MObject()
        mVRoughness = OpenMaya.MObject()
        mBump = OpenMaya.MObject()

        mOutColor = OpenMaya.MObject()

    def compute(self, plug, block):
        if plug == kdsubsurface.mOutColor:
            resultColor = OpenMaya.MFloatVector(0.0,0.0,0.0)
            
            outColorHandle = block.outputValue( kdsubsurface.mOutColor )
            outColorHandle.setMFloatVector(resultColor)
            outColorHandle.setClean()
        else:
            return OpenMaya.kUnknownParameter


def nodeCreator():
    return kdsubsurface()

def nodeInitializer():
    nAttr = OpenMaya.MFnNumericAttribute()
    eAttr = OpenMaya.MFnEnumAttribute()

    try:
        kdsubsurface.mKd = nAttr.createColor("Kd", "kd")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.5,0.5,0.5)

        kdsubsurface.mMfp = nAttr.createColor("mfp", "mfp")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.5,0.5,0.5)

        kdsubsurface.mKr = nAttr.createColor("Kr", "kr")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(1.0,1.0,1.0)

        kdsubsurface.mKt = nAttr.createColor("Kt", "kt")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(1.0,1.0,1.0)

        kdsubsurface.mEta = nAttr.create("eta","eta", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(1.33)
        nAttr.setConnectable(0)

        kdsubsurface.mScale = nAttr.create("scale","sc", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(1.0)
        nAttr.setConnectable(0)

        kdsubsurface.mG = nAttr.create("g","g", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.0)
        nAttr.setConnectable(0)

        kdsubsurface.mRemapRoughness = nAttr.create("remapRoughness", "rr", OpenMaya.MFnNumericData.kBoolean, True)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)

        kdsubsurface.mURoughness = nAttr.create("uRoughness","ur", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(-1.0)

        kdsubsurface.mVRoughness = nAttr.create("vRoughness","vr", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(-1.0)

        kdsubsurface.mBump = nAttr.create("bumpmap", "b", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(-1.0)

        kdsubsurface.mOutColor = nAttr.createColor("outColor", "oc")
        nAttr.setStorable(0)
        nAttr.setHidden(0)
        nAttr.setReadable(1)
        nAttr.setWritable(0)
    except:
        sys.stderr.write("Failed to create attributes\n")
        raise

    try:
        kdsubsurface.addAttribute(kdsubsurface.mKd)
        kdsubsurface.addAttribute(kdsubsurface.mMfp)
        kdsubsurface.addAttribute(kdsubsurface.mKr)
        kdsubsurface.addAttribute(kdsubsurface.mKt)
        kdsubsurface.addAttribute(kdsubsurface.mEta)
        kdsubsurface.addAttribute(kdsubsurface.mScale)
        kdsubsurface.addAttribute(kdsubsurface.mG)
        kdsubsurface.addAttribute(kdsubsurface.mRemapRoughness)
        kdsubsurface.addAttribute(kdsubsurface.mURoughness)
        kdsubsurface.addAttribute(kdsubsurface.mVRoughness)
        kdsubsurface.addAttribute(kdsubsurface.mBump)
        kdsubsurface.addAttribute(kdsubsurface.mOutColor)
    except:
        sys.stderr.write("Failed to add attributes\n")
        raise

    try:
        kdsubsurface.attributeAffects (kdsubsurface.mKd, kdsubsurface.mOutColor)
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
