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

kPluginNodeName = "PBRTDisneyMaterial"
kPluginNodeClassify = "shader/surface"
kPluginNodeId = OpenMaya.MTypeId(0x8704E)

class disney(OpenMayaMPx.MPxNode):
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        mColor = OpenMaya.MObject()
        mMetallic = OpenMaya.MObject()
        mETA = OpenMaya.MObject()
        mRoughness = OpenMaya.MObject()
        mSpecularTint = OpenMaya.MObject()
        mAnisotropic = OpenMaya.MObject()
        mSheen = OpenMaya.MObject()
        mSheenTint = OpenMaya.MObject()
        mClearCoat = OpenMaya.MObject()
        mClearCoatGloss = OpenMaya.MObject()
        mSpecTrans = OpenMaya.MObject()
        mScatterDistance = OpenMaya.MObject()
        mThin = OpenMaya.MObject()
        mFlatness = OpenMaya.MObject()
        mDiffTrans = OpenMaya.MObject()
        mBump = OpenMaya.MObject()

        mOutColor = OpenMaya.MObject()

    def compute(self, plug, block):
        if plug == disney.mOutColor:
            resultColor = OpenMaya.MFloatVector(0.0,0.0,0.0)
            
            outColorHandle = block.outputValue( disney.mOutColor )
            outColorHandle.setMFloatVector(resultColor)
            outColorHandle.setClean()
        else:
            return OpenMaya.kUnknownParameter


def nodeCreator():
    return disney()

def nodeInitializer():
    nAttr = OpenMaya.MFnNumericAttribute()
    eAttr = OpenMaya.MFnEnumAttribute()

    try:
        mBump = OpenMaya.MObject()


        disney.mColor = nAttr.createColor("color", "c")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.5,0.5,0.5)

        disney.mMetallic = nAttr.create("metallic","mt", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.0)

        disney.mETA = nAttr.create("eta","e", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(1.5)

        disney.mRoughness = nAttr.create("roughness","r", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.5)

        disney.mSpecularTint = nAttr.create("specularTint","st", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.0)

        disney.mAnisotropic = nAttr.create("anisotropic","a", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.0)

        disney.mSheen = nAttr.create("sheen","sh", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.0)

        disney.mSheenTint = nAttr.create("sheenTint","shtn", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.5)

        disney.mClearCoat = nAttr.create("clearCoat","cc", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.0)

        disney.mClearCoatGloss = nAttr.create("clearCoatGloss","ccg", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(1.0)

        disney.mSpecTrans = nAttr.create("specTrans","sptr", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.0)

        disney.mScatterDistance = nAttr.createColor("scatterDistance", "sd")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.0,0.0,0.0)

        disney.mThin = nAttr.create("thin", "tn", OpenMaya.MFnNumericData.kBoolean, False)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)

        disney.mFlatness = nAttr.create("flatness","fl", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.0)

        disney.mDiffTrans = nAttr.create("diffTrans","dt", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(1.0)

        disney.mBump = nAttr.create("bumpmap", "b", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(-1.0)

        disney.mOutColor = nAttr.createColor("outColor", "oc")
        nAttr.setStorable(0)
        nAttr.setHidden(0)
        nAttr.setReadable(1)
        nAttr.setWritable(0)
    except:
        sys.stderr.write("Failed to create attributes\n")
        raise

    try:
        disney.addAttribute(disney.mColor)
        disney.addAttribute(disney.mMetallic)
        disney.addAttribute(disney.mETA)
        disney.addAttribute(disney.mRoughness)
        disney.addAttribute(disney.mSpecularTint)
        disney.addAttribute(disney.mAnisotropic)
        disney.addAttribute(disney.mSheen)
        disney.addAttribute(disney.mSheenTint)
        disney.addAttribute(disney.mClearCoat)
        disney.addAttribute(disney.mClearCoatGloss)
        disney.addAttribute(disney.mSpecTrans)
        disney.addAttribute(disney.mScatterDistance)
        disney.addAttribute(disney.mThin)
        disney.addAttribute(disney.mFlatness)
        disney.addAttribute(disney.mDiffTrans)
        disney.addAttribute(disney.mBump)
        disney.addAttribute(disney.mOutColor)
    except:
        sys.stderr.write("Failed to add attributes\n")
        raise

    try:
        disney.attributeAffects (disney.mColor, disney.mOutColor)
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
