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

kPluginNodeName = "PBRTHomogeneousMedium"
kPluginNodeClassify = "shader/volume"
kPluginNodeId = OpenMaya.MTypeId(0x87058)

class homogeneous(OpenMayaMPx.MPxNode):
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)

        mName = OpenMaya.MObject()

        mScale = OpenMaya.MObject()
        mG = OpenMaya.MObject()
        mSigmaA = OpenMaya.MObject()
        mSigmaS = OpenMaya.MObject()

        mOutColor = OpenMaya.MObject()

    def compute(self, plug, block):
        if plug == homogeneous.mOutColor:
            resultColor = OpenMaya.MFloatVector(0.0,0.0,0.0)
            
            outColorHandle = block.outputValue( homogeneous.mOutColor )
            outColorHandle.setMFloatVector(resultColor)
            outColorHandle.setClean()
        else:
            return OpenMaya.kUnknownParameter

def nodeCreator():
    return homogeneous()

def nodeInitializer():
    nAttr = OpenMaya.MFnNumericAttribute()
    eAttr = OpenMaya.MFnEnumAttribute()

    try:
        homogeneous.mName = eAttr.create("preset", "pre" )
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

        homogeneous.mScale = nAttr.create("scale","s", OpenMaya.MFnNumericData.kFloat, 1.0)
        nAttr.setKeyable(0) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)

        homogeneous.mG = nAttr.create("g","g", OpenMaya.MFnNumericData.kFloat, 0.0)
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)

        homogeneous.mSigmaA = nAttr.createColor("sigma_a", "sa")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)
        nAttr.setDefault(0.0011, 0.0024, 0.014)

        homogeneous.mSigmaS = nAttr.createColor("sigma_s", "ss")
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)
        nAttr.setDefault(2.55, 3.21, 3.77)

        homogeneous.mOutColor = nAttr.createColor("outColor", "oc")
        nAttr.setStorable(0)
        nAttr.setHidden(0)
        nAttr.setReadable(1)
        nAttr.setWritable(0)

    except:
        sys.stderr.write("Failed to create attributes\n")
        raise

    try:
        homogeneous.addAttribute(homogeneous.mName)

        homogeneous.addAttribute(homogeneous.mScale)
        homogeneous.addAttribute(homogeneous.mG)

        homogeneous.addAttribute(homogeneous.mSigmaA)
        homogeneous.addAttribute(homogeneous.mSigmaS)

        homogeneous.addAttribute(homogeneous.mOutColor)
    except:
        sys.stderr.write("Failed to add attributes\n")
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
