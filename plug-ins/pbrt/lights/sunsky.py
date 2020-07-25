import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

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

kPluginNodeName = "PBRTSunSkyLight"
kPluginNodeClassify = "light/general"
kPluginNodeId = OpenMaya.MTypeId(0x8706C)

class sunsky(OpenMayaMPx.MPxNode):
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        mLuminance = OpenMaya.MObject()
        mAlbedo = OpenMaya.MObject()
        mElevation = OpenMaya.MObject()
        mTurbidity = OpenMaya.MObject()
        mNSamples = OpenMaya.MObject()
        mResolution = OpenMaya.MObject()
        mRotate = OpenMaya.MObject()
        mOutColor = OpenMaya.MObject()

    def compute(self, plug, block):
        status = None
        
        if plug == sunsky.mOutColor:
            resultColor = OpenMaya.MFloatVector(0.0,0.0,0.0)
            
            outColorHandle = block.outputValue( sunsky.mOutColor )
            outColorHandle.setMFloatVector(resultColor)
            block.setClean( plug )
        else:
            status = OpenMaya.kUnknownParameter

        return status

def nodeCreator():
    return sunsky()

def nodeInitializer():
    nAttr = OpenMaya.MFnNumericAttribute()

    try:
        sunsky.mLuminance = nAttr.createColor("luminance", "l")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(0)
        nAttr.setWritable(1)
        nAttr.setDefault(1.0,1.0,1.0)
        nAttr.setConnectable(0)

        sunsky.mAlbedo = nAttr.create("albedo", "ab", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.5)

        sunsky.mElevation = nAttr.create("elevation", "ev", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(10.0)

        sunsky.mTurbidity = nAttr.create("turbidity", "tb", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(3.0)

        sunsky.mNSamples = nAttr.create("nsamples","n", OpenMaya.MFnNumericData.kInt, 1)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)

        sunsky.mResolution = nAttr.create("resolution","r", OpenMaya.MFnNumericData.kInt, 1024)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)

        sunsky.mRotate = nAttr.create("rotate", "ro", OpenMaya.MFnNumericData.k3Float)
        nAttr.usedAsColor = False
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.0,0.0,0.0)

        sunsky.mOutColor = nAttr.createColor("outColor", "oc")
        nAttr.setStorable(0)
        nAttr.setHidden(0)
        nAttr.setReadable(1)
        nAttr.setWritable(0)

    except:
        sys.stderr.write("Failed to create attributes\n")
        raise

    try:
        sunsky.addAttribute(sunsky.mLuminance)
        sunsky.addAttribute(sunsky.mAlbedo)
        sunsky.addAttribute(sunsky.mElevation)
        sunsky.addAttribute(sunsky.mTurbidity)
        sunsky.addAttribute(sunsky.mNSamples)
        sunsky.addAttribute(sunsky.mResolution)
        sunsky.addAttribute(sunsky.mRotate)
        sunsky.addAttribute(sunsky.mOutColor)
    except:
        sys.stderr.write("Failed to add attributes\n")
        raise

    try:
        sunsky.attributeAffects (sunsky.mLuminance, sunsky.mOutColor)
    except:
        sys.stderr.write("Failed in setting attributeAffects\n")
        raise

# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerNode( kPluginNodeName, 
                      kPluginNodeId, 
                      nodeCreator, 
                      nodeInitializer, 
                      OpenMayaMPx.MPxNode.kDependNode, 
                      kPluginNodeClassify )
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
