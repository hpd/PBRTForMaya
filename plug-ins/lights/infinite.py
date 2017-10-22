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

kPluginNodeName = "PBRTInfiniteLight"
kPluginNodeClassify = "light/general"
kPluginNodeId = OpenMaya.MTypeId(0x87051)

class infinite(OpenMayaMPx.MPxNode):
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        mLuminance = OpenMaya.MObject()
        mNSamples = OpenMaya.MObject()
        mEnvMap = OpenMaya.MObject()
        mRotate = OpenMaya.MObject()
        mOutColor = OpenMaya.MObject()

    def compute(self, plug, block):
        status = None
        
        if plug == infinite.mOutColor:
            resultColor = OpenMaya.MFloatVector(0.0,0.0,0.0)
            
            outColorHandle = block.outputValue( infinite.mOutColor )
            outColorHandle.setMFloatVector(resultColor)
            block.setClean( plug )
        else:
            status = OpenMaya.kUnknownParameter

        return status

def nodeCreator():
    return infinite()

def nodeInitializer():
    nAttr = OpenMaya.MFnNumericAttribute()

    try:
        infinite.mLuminance = nAttr.createColor("luminance", "l")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(0)
        nAttr.setWritable(1)
        nAttr.setDefault(1.0,1.0,1.0)
        nAttr.setConnectable(0)

        infinite.mEnvMap = nAttr.createColor("envmap", "e")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(0)
        nAttr.setWritable(1)
        nAttr.setDefault(0.0,0.0,0.0)

        infinite.mNSamples = nAttr.create("nsamples","n", OpenMaya.MFnNumericData.kInt, 1)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)

        infinite.mRotate = nAttr.create("rotate", "ro", OpenMaya.MFnNumericData.k3Float)
        nAttr.usedAsColor = False
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.0,0.0,0.0)

        infinite.mOutColor = nAttr.createColor("outColor", "oc")
        nAttr.setStorable(0)
        nAttr.setHidden(0)
        nAttr.setReadable(1)
        nAttr.setWritable(0)

    except:
        sys.stderr.write("Failed to create attributes\n")
        raise

    try:
        infinite.addAttribute(infinite.mEnvMap)
        infinite.addAttribute(infinite.mLuminance)
        infinite.addAttribute(infinite.mNSamples)
        infinite.addAttribute(infinite.mRotate)
        infinite.addAttribute(infinite.mOutColor)
    except:
        sys.stderr.write("Failed to add attributes\n")
        raise

    try:
        infinite.attributeAffects (infinite.mLuminance, infinite.mOutColor)
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
