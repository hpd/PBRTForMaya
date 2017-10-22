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

kPluginNodeName = "PBRTSubSurfaceMaterial"
kPluginNodeClassify = "shader/surface"
kPluginNodeId = OpenMaya.MTypeId(0x8704D)

class subsurface(OpenMayaMPx.MPxNode):
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        mName = OpenMaya.MObject()
        mG = OpenMaya.MObject()
        mScale = OpenMaya.MObject()
        mEta = OpenMaya.MObject()

        mSigmaA = OpenMaya.MObject()
        mSigmaS = OpenMaya.MObject()

        mKr = OpenMaya.MObject()
        mKt = OpenMaya.MObject()

        mRemapRoughness = OpenMaya.MObject()
        mURoughness = OpenMaya.MObject()
        mVRoughness = OpenMaya.MObject()
        mBump = OpenMaya.MObject()

        mOutColor = OpenMaya.MObject()

    def compute(self, plug, block):
        if plug == subsurface.mOutColor:
            resultColor = OpenMaya.MFloatVector(0.0,0.0,0.0)
            
            outColorHandle = block.outputValue( subsurface.mOutColor )
            outColorHandle.setMFloatVector(resultColor)
            outColorHandle.setClean()
        else:
            return OpenMaya.kUnknownParameter


def nodeCreator():
    return subsurface()

def nodeInitializer():
    nAttr = OpenMaya.MFnNumericAttribute()
    eAttr = OpenMaya.MFnEnumAttribute()
    sAttr = OpenMaya.MFnTypedAttribute()

    try:
        subsurface.mName = eAttr.create("Preset", "pre" )
        eAttr.setKeyable(1) 
        eAttr.setStorable(1)
        eAttr.setReadable(1)
        eAttr.setWritable(1)

        Materials = ["None",
            "Apple",
            "Chicken1", 
            "Chicken2",
            "Cream",
            "Ketchup",
            "Marble",
            "Potato",
            "Skimmilk",
            "Skin1",
            "Skin2",
            "Spectralon",
            "Wholemilk",
            "Lowfat Milk",
            "Reduced Milk",
            "Regular Milk",
            "Espresso",
            "Mint Mocha Coffee",
            "Lowfat Soy Milk",
            "Regular Soy Milk",
            "Lowfat Chocolate Milk",
            "Regular Chocolate Milk",
            "Coke",
            "Pepsi",
            "Sprite",
            "Gatorade",
            "Chardonnay",
            "White Zinfandel",
            "Merlot",
            "Budweiser Beer",
            "Coors Light Beer",
            "Clorox",
            "Apple Juice",
            "Cranberry Juice",
            "Grape Juice",
            "Ruby Grapefruit Juice",
            "White Grapefruit Juice",
            "Shampoo",
            "Strawberry Shampoo",
            "Head & Shoulders Shampoo",
            "Lemon Tea Powder",
            "Orange Powder",
            "Pink Lemonade Powder",
            "Cappuccino Powder",
            "Salt Powder",
            "Sugar Powder",
            "Suisse Mocha Powder",
            "Pacific Ocean Surface Water"]

        for i in range(len(Materials)):
            eAttr.addField(Materials[i], i)

        # Default to Skin1
        eAttr.setDefault(9)

        subsurface.mG = nAttr.create("g","g", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)
        nAttr.setDefault(0.0)

        subsurface.mScale = nAttr.create("scale","sc", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)
        nAttr.setDefault(1.0)

        subsurface.mEta = nAttr.create("eta","eta", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)
        nAttr.setDefault(1.33)

        subsurface.mSigmaA = nAttr.createColor("sigma_a", "sa")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(0.0011, 0.0024, 0.014)

        subsurface.mSigmaS = nAttr.createColor("sigma_s", "ss")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(2.55, 3.21, 3.77)

        subsurface.mKr = nAttr.createColor("Kr", "kr")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(1.0, 1.0, 1.0)

        subsurface.mKt = nAttr.createColor("Kt", "kt")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(1.0, 1.0, 1.0)

        subsurface.mRemapRoughness = nAttr.create("remapRoughness", "rr", OpenMaya.MFnNumericData.kBoolean, True)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)

        subsurface.mURoughness = nAttr.create("uRoughness","ur", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(-1.0)

        subsurface.mVRoughness = nAttr.create("vRoughness","vr", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(-1.0)

        subsurface.mBump = nAttr.create("bumpmap", "b", OpenMaya.MFnNumericData.kFloat)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setDefault(-1.0)

        subsurface.mOutColor = nAttr.createColor("outColor", "oc")
        nAttr.setStorable(0)
        nAttr.setHidden(0)
        nAttr.setReadable(1)
        nAttr.setWritable(0)
    except:
        sys.stderr.write("Failed to create attributes\n")
        raise

    try:
        subsurface.addAttribute(subsurface.mName)
        subsurface.addAttribute(subsurface.mG)
        subsurface.addAttribute(subsurface.mScale)
        subsurface.addAttribute(subsurface.mEta)
        subsurface.addAttribute(subsurface.mSigmaA)
        subsurface.addAttribute(subsurface.mSigmaS)

        subsurface.addAttribute(subsurface.mKr)
        subsurface.addAttribute(subsurface.mKt)
        subsurface.addAttribute(subsurface.mRemapRoughness)
        subsurface.addAttribute(subsurface.mURoughness)
        subsurface.addAttribute(subsurface.mVRoughness)
        subsurface.addAttribute(subsurface.mBump)
        subsurface.addAttribute(subsurface.mOutColor)
    except:
        sys.stderr.write("Failed to add attributes\n")
        raise

    try:
        subsurface.attributeAffects (subsurface.mKr, subsurface.mOutColor)
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
