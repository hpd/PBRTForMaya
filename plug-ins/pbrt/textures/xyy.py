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

kPluginNodeName = "PBRTxyY"
kPluginNodeClassify = "utility/color"
kPluginNodeId = OpenMaya.MTypeId(0x87069)

class xyy(OpenMayaMPx.MPxNode):
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)

        mPreset = OpenMaya.MObject()
        mValue = OpenMaya.MObject()

        mOutColor = OpenMaya.MObject()

    def compute(self, plug, block):
        if plug == xyy.mOutColor:
            resultColor = OpenMaya.MFloatVector(0.0,0.0,0.0)
            
            outColorHandle = block.outputValue( xyy.mOutColor )
            outColorHandle.setMFloatVector(resultColor)
            outColorHandle.setClean()
        else:
            return OpenMaya.kUnknownParameter

def nodeCreator():
    return xyy()

def nodeInitializer():
    nAttr = OpenMaya.MFnNumericAttribute()
    eAttr = OpenMaya.MFnEnumAttribute()

    try:
        xyy.mPreset = eAttr.create("preset", "pre" )
        eAttr.setKeyable(1) 
        eAttr.setStorable(1)
        eAttr.setReadable(1)
        eAttr.setWritable(1)

        Presets = ["None",
            "D50",
            "D60 - ACES",
            "D65",
            "Illuminant A",
            "Macbeth Patch 1  - Dark Skin",
            "Macbeth Patch 2  - Light Skin", 
            "Macbeth Patch 3  - Blue Sky", 
            "Macbeth Patch 4  - Foliage",
            "Macbeth Patch 5  - Blue Flower",
            "Macbeth Patch 6  - Bluish Green",
            "Macbeth Patch 7  - Orange",
            "Macbeth Patch 8  - Purplish Blue",
            "Macbeth Patch 9  - Moderate Red",
            "Macbeth Patch 10 - Purple",
            "Macbeth Patch 11 - Yellow Green",
            "Macbeth Patch 12 - Orange Yellow",
            "Macbeth Patch 13 - Blue",
            "Macbeth Patch 14 - Green",
            "Macbeth Patch 15 - Red",
            "Macbeth Patch 16 - Yellow",
            "Macbeth Patch 17 - Magenta",
            "Macbeth Patch 18 - Cyan",
            "Macbeth Patch 19 - White",
            "Macbeth Patch 20 - Neutral 8",
            "Macbeth Patch 21 - Neutral 6.5",
            "Macbeth Patch 22 - Neutral 5",
            "Macbeth Patch 23 - Neutral 3.5",
            "Macbeth Patch 24 - Black"
        ] 

        for i in range(len(Presets)):
            eAttr.addField(Presets[i], i)

        # Default to None
        eAttr.setDefault(0)

        xyy.mValue = nAttr.create("value", "val", OpenMaya.MFnNumericData.k3Float)
        nAttr.usedAsColor = False
        nAttr.setKeyable(1) 
        nAttr.setStorable(1)
        nAttr.setReadable(1)
        nAttr.setWritable(1)
        nAttr.setConnectable(0)

        # Normalized CIE 1931 2 degree observer D65
        nAttr.setDefault(0.31272, 0.32902, 1.0)

        xyy.mOutColor = nAttr.createColor("outColor", "oc")
        nAttr.setStorable(0)
        nAttr.setHidden(0)
        nAttr.setReadable(1)
        nAttr.setWritable(0)
    except:
        sys.stderr.write("Failed to create attributes\n")
        raise

    try:
        xyy.addAttribute(xyy.mPreset)
        xyy.addAttribute(xyy.mValue)

        xyy.addAttribute(xyy.mOutColor)
    except:
        sys.stderr.write("Failed to add attributes\n")
        raise

    try:
        xyy.attributeAffects (xyy.mValue, xyy.mOutColor)
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
