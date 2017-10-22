import os
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

kPluginNodeName = "PBRTRenderSettings"
kPluginNodeId = OpenMaya.MTypeId(0x87040)

# Command
class PBRTRenderSetting(OpenMayaMPx.MPxNode):
    # Class variables
    mPBRTPath = OpenMaya.MObject()
    mOIIOToolPath = OpenMaya.MObject()

    # PBRT Version control
    mPBRTVersion = OpenMaya.MObject()

    # Sampler variables
    mSampler = OpenMaya.MObject()
    mSamplerPixelSamples = OpenMaya.MObject()

    mSamplerMaxMinDimensions = OpenMaya.MObject()

    mSamplerStratifedJitter = OpenMaya.MObject()
    mSamplerStratifedXSamples = OpenMaya.MObject()
    mSamplerStratifedYSamples = OpenMaya.MObject()
    mSamplerStratifedDimensions = OpenMaya.MObject()

    mSamplerLowDiscrepancyDimensions = OpenMaya.MObject()

    # Accelerator variables
    mAccelerator = OpenMaya.MObject()

    mAcceleratorKDTreeIntersectCost = OpenMaya.MObject()
    mAcceleratorKDTreeTraversalCost = OpenMaya.MObject()
    mAcceleratorKDTreeEmptyBonus = OpenMaya.MObject()
    mAcceleratorKDTreeMaxPrims = OpenMaya.MObject()
    mAcceleratorKDTreeMaxDepth = OpenMaya.MObject()

    mAcceleratorBVHSplitMethod = OpenMaya.MObject()
    mAcceleratorBVHMaxNodePrims = OpenMaya.MObject()

    # Integrator variables
    mIntegrator = OpenMaya.MObject()

    mIntegratorPathMaxDepth = OpenMaya.MObject()
    mIntegratorPathRRThreshold = OpenMaya.MObject()
    mIntegratorPathLightSampleStrategy = OpenMaya.MObject()

    mIntegratorBidirectionalPathMaxDepth = OpenMaya.MObject()
    mIntegratorBidirectionalPathVisualizeStrategies = OpenMaya.MObject()
    mIntegratorBidirectionalPathVisualizeWeights = OpenMaya.MObject()
    mIntegratorBidirectionalPathLightSampleStrategy = OpenMaya.MObject()

    mIntegratorDirectLightingMaxDepth = OpenMaya.MObject()
    mIntegratorDirectLightingStrategy = OpenMaya.MObject()

    mIntegratorMetropolisLightTransportMaxDepth = OpenMaya.MObject()
    mIntegratorMetropolisLightTransportBootstrapSamples = OpenMaya.MObject()
    mIntegratorMetropolisLightTransportChains = OpenMaya.MObject()
    mIntegratorMetropolisLightTransportMutationsPerPixel = OpenMaya.MObject()
    mIntegratorMetropolisLightTransportLargeStepProbability = OpenMaya.MObject()
    mIntegratorMetropolisLightTransportSigma = OpenMaya.MObject()

    mIntegratorStochasticProgressivePhotonMapNumIterations = OpenMaya.MObject()
    mIntegratorStochasticProgressivePhotonMapMaxDepth = OpenMaya.MObject()
    mIntegratorStochasticProgressivePhotonMapPhotonsPerIteration = OpenMaya.MObject()
    mIntegratorStochasticProgressivePhotonMapImageWriteFrequency = OpenMaya.MObject()
    mIntegratorStochasticProgressivePhotonMapRadius = OpenMaya.MObject()

    mIntegratorVolumetricPathMaxDepth = OpenMaya.MObject()
    mIntegratorVolumetricPathRRThreshold = OpenMaya.MObject()
    mIntegratorVolumetricPathLightSampleStrategy = OpenMaya.MObject()

    mIntegratorWhittedMaxDepth = OpenMaya.MObject()

    # Film variables
    mFilm = OpenMaya.MObject()
    mFilmMaxSampleLuminance = OpenMaya.MObject()
    mFilmScale = OpenMaya.MObject()

    # Film - Image variables
    mImageFilmFileFormat = OpenMaya.MObject()

    # Reconstruction Filter variables
    mFilter = OpenMaya.MObject()
    mFilterXWidth = OpenMaya.MObject()
    mFilterYWidth = OpenMaya.MObject()
    mFilterAlpha = OpenMaya.MObject()
    mFilterB = OpenMaya.MObject()
    mFilterC = OpenMaya.MObject()
    mFilterTau = OpenMaya.MObject()

    # Camera variables
    mCameraOverride = OpenMaya.MObject()

    mCameraRealisticLensFile = OpenMaya.MObject()
    mCameraRealisticSimpleWeighting = OpenMaya.MObject()
    mCameraRealisticApertureDiameter = OpenMaya.MObject()
    mCameraRealisticFocusDistance = OpenMaya.MObject()

    # Overall controls
    mMotionBlur = OpenMaya.MObject()
    mExportOnly = OpenMaya.MObject()
    mKeepTempFiles = OpenMaya.MObject()
    mSkipGeometryExport = OpenMaya.MObject()
    mUsePLYExport = OpenMaya.MObject()
    mVerboseRender = OpenMaya.MObject()
    mVerboseExport = OpenMaya.MObject()
    mThreads = OpenMaya.MObject()
    mCommandLineParameters = OpenMaya.MObject()

    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)

    # Invoked when the command is evaluated.
    def compute(self, plug, block):
        print "Render Settings evaluate!"
        return OpenMaya.kUnknownParameter

    @staticmethod
    def addBooleanAttribute(nAttr, attribute, longName, shortName, defaultBoolean=True):
        setattr(PBRTRenderSetting, attribute, nAttr.create(longName, shortName, OpenMaya.MFnNumericData.kBoolean, defaultBoolean) )
        nAttr.setStorable(1)
        nAttr.setWritable(1)
 
    @staticmethod
    def addIntegerAttribute(nAttr, attribute, longName, shortName, defaultInt=0):
        setattr(PBRTRenderSetting, attribute, nAttr.create(longName, shortName, OpenMaya.MFnNumericData.kInt, defaultInt) )
        nAttr.setStorable(1)
        nAttr.setWritable(1)

    @staticmethod
    def addFloatAttribute(nAttr, attribute, longName, shortName, defaultFloat=0.0):
        setattr(PBRTRenderSetting, attribute, nAttr.create(longName, shortName, OpenMaya.MFnNumericData.kFloat, defaultFloat) )
        nAttr.setStorable(1)
        nAttr.setWritable(1)

    @staticmethod
    def addColorAttribute(nAttr, attribute, longName, shortName, defaultRGB):
        setattr(PBRTRenderSetting, attribute, nAttr.createColor(longName, shortName) )
        nAttr.setDefault(defaultRGB[0], defaultRGB[1], defaultRGB[2])
        nAttr.setStorable(1)
        nAttr.setWritable(1)

    @staticmethod
    def addStringAttribute(sAttr, attribute, longName, shortName, defaultString=""):
        stringFn = OpenMaya.MFnStringData()
        defaultText = stringFn.create(defaultString)
        setattr(PBRTRenderSetting, attribute, sAttr.create(longName, shortName, OpenMaya.MFnData.kString, defaultText) )
        sAttr.setStorable(1)
        sAttr.setWritable(1)

def nodeCreator():
    return PBRTRenderSetting()

def nodeInitializer():
    print "Render Settings initialize!"
    sAttr = OpenMaya.MFnTypedAttribute()
    nAttr = OpenMaya.MFnNumericAttribute()

    try:
        # Path to PBRT executable
        defaultPBRTPath = os.getenv( "PBRT_PATH" )
        if not defaultPBRTPath:
            defaultPBRTPath = ""
        PBRTRenderSetting.addStringAttribute(sAttr, "mPBRTPath", "PBRTPath", "pbrtp", defaultPBRTPath)

        # Path to oiiotool executable
        defaultOIIOToolPath = os.getenv( "OIIOTOOL_PATH" )
        if not defaultOIIOToolPath:
            defaultOIIOToolPath = ""
        PBRTRenderSetting.addStringAttribute(sAttr, "mOIIOToolPath", "oiiotoolPath", "oiiotp", defaultOIIOToolPath)

        # Version variables
        PBRTRenderSetting.addStringAttribute(sAttr,  "mPBRTVersion", "PBRTVersion", "pbrtv", "v3 Book")

        # Sampler variables
        PBRTRenderSetting.addStringAttribute(sAttr,  "mSampler", "sampler", "smpl", "Halton")
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mSamplerPixelSamples", "samplerPixelSamples", "smps", 4)

        PBRTRenderSetting.addIntegerAttribute(nAttr, "mSamplerMaxMinDimensions", "samplerMaxMinDimensions", "smpmmd", 4)

        PBRTRenderSetting.addBooleanAttribute(nAttr, "mSamplerStratifedJitter", "samplerStratifedJitter", "smpsj", True)
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mSamplerStratifedXSamples", "samplerStratifedXSamples", "smpsxs", 4)
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mSamplerStratifedYSamples", "samplerStratifedYSamples", "smpsys", 4)
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mSamplerStratifedDimensions", "samplerStratifedDimensions", "smpsd", 4)

        PBRTRenderSetting.addIntegerAttribute(nAttr, "mSamplerLowDiscrepancyDimensions", "samplerLowDiscrepancyDimensions", "smpldd", 4)

        # Accelerator variables
        PBRTRenderSetting.addStringAttribute(sAttr,  "mAccelerator", "accelerator", "accl", "BVH")
        
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mAcceleratorKDTreeIntersectCost", "acceleratorKDTreeIntersectCost", "acclkdic", 80)
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mAcceleratorKDTreeTraversalCost", "acceleratorKDTreeTraversalCost", "acclkdtc", 1)
        PBRTRenderSetting.addFloatAttribute(nAttr, "mAcceleratorKDTreeEmptyBonus", "acceleratorKDTreeEmptyBonus", "acclkdeb", 0.5)
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mAcceleratorKDTreeMaxPrims", "acceleratorKDTreeMaxPrims", "acclkdmp", 1)
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mAcceleratorKDTreeMaxDepth", "acceleratorKDTreeMaxDepth", "acclkdmd", -1)

        PBRTRenderSetting.addStringAttribute(sAttr, "mAcceleratorBVHSplitMethod", "acceleratorBVHSplitMethod", "acclbsm", "SAH")
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mAcceleratorBVHMaxNodePrims", "acceleratorBVHMaxNodePrims", "acclbnp", 4)

        # Integrator variables
        PBRTRenderSetting.addStringAttribute(sAttr,  "mIntegrator", "integrator", "intg", "Path Tracer")
        
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mIntegratorPathMaxDepth", "integratorPathMaxDepth", "intgpmd", 5)
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mIntegratorPathRRThreshold", "integratorPathRRThreshold", "intgprrt", 1)
        PBRTRenderSetting.addStringAttribute(sAttr,  "mIntegratorPathLightSampleStrategy", "integratorPathLightSampleStrategy", "intgplss", "Spatial")

        PBRTRenderSetting.addIntegerAttribute(nAttr, "mIntegratorBidirectionalPathMaxDepth", "integratorBidirectionalPathMaxDepth", "intgbpmd", 5)
        PBRTRenderSetting.addBooleanAttribute(nAttr, "mIntegratorBidirectionalPathVisualizeStrategies", "integratorBidirectionalPathVisualizeStrategies", "intgbpvs", False)
        PBRTRenderSetting.addBooleanAttribute(nAttr, "mIntegratorBidirectionalPathVisualizeWeights", "integratorBidirectionalPathVisualizeWeights", "intgbpvw", False)
        PBRTRenderSetting.addStringAttribute(sAttr,  "mIntegratorBidirectionalPathLightSampleStrategy", "integratorBidirectionalPathLightSampleStrategy", "intgbplss", "Spatial")

        PBRTRenderSetting.addIntegerAttribute(nAttr, "mIntegratorDirectLightingMaxDepth", "integratorDirectLightingMaxDepth", "intgdlmd", 5)
        PBRTRenderSetting.addStringAttribute(sAttr,  "mIntegratorDirectLightingStrategy", "integratorDirectLightingStrategy", "intgdls", "All")

        PBRTRenderSetting.addIntegerAttribute(nAttr, "mIntegratorMetropolisLightTransportMaxDepth", "integratorMetropolisLightTransportMaxDepth", "intgmltmd", 5)
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mIntegratorMetropolisLightTransportBootstrapSamples", "integratorMetropolisLightTransportBootstrapSamples", "intgmltbs", 100000)
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mIntegratorMetropolisLightTransportChains", "integratorMetropolisLightTransportChains", "intgmltc", 1000)
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mIntegratorMetropolisLightTransportMutationsPerPixel", "integratorMetropolisLightTransportMutationsPerPixel", "intgmltmpp", 100)
        PBRTRenderSetting.addFloatAttribute(nAttr,  "mIntegratorMetropolisLightTransportLargeStepProbability", "integratorMetropolisLightTransportLargeStepProbability", "intgmltlp", 0.3)
        PBRTRenderSetting.addFloatAttribute(nAttr, "mIntegratorMetropolisLightTransportSigma", "integratorMetropolisLightTransportSigma", "intgmlts", 0.01)

        PBRTRenderSetting.addIntegerAttribute(nAttr, "mIntegratorStochasticProgressivePhotonMapNumIterations", "integratorStochasticProgressivePhotonMapNumIterations", "intgsppmni", 64)
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mIntegratorStochasticProgressivePhotonMapMaxDepth", "integratorStochasticProgressivePhotonMapMaxDepth", "intgsppmmd", 5)
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mIntegratorStochasticProgressivePhotonMapPhotonsPerIteration", "integratorStochasticProgressivePhotonMapPhotonsPerIteration", "intgsppmppi", -1)
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mIntegratorStochasticProgressivePhotonMapImageWriteFrequency", "integratorStochasticProgressivePhotonMapImageWriteFrequency", "intgsppmiwf", 2147483648)
        PBRTRenderSetting.addFloatAttribute(nAttr,  "mIntegratorStochasticProgressivePhotonMapRadius", "integratorStochasticProgressivePhotonMapRadius", "intgsppmr", 1.0)

        PBRTRenderSetting.addIntegerAttribute(nAttr, "mIntegratorVolumetricPathMaxDepth", "integratorVolumetricPathMaxDepth", "intgvpmd", 5)
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mIntegratorVolumetricPathRRThreshold", "integratorVolumetricPathRRThreshold", "intgvprrt", 1)
        PBRTRenderSetting.addStringAttribute(sAttr,  "mIntegratorVolumetricPathLightSampleStrategy", "integratorVolumetricPathLightSampleStrategy", "intgvplss", "Spatial")

        PBRTRenderSetting.addIntegerAttribute(nAttr, "mIntegratorWhittedMaxDepth", "integratorWhittedMaxDepth", "intgwmd", 5)

        # Film variables
        PBRTRenderSetting.addStringAttribute(sAttr,  "mFilm", "film", "fm", "Image Film")
        PBRTRenderSetting.addFloatAttribute(nAttr,   "mFilmMaxSampleLuminance", "filmMaxSampleLuminance", "fmmsl", -1.0)
        PBRTRenderSetting.addFloatAttribute(nAttr,   "mFilmScale", "filmScale", "fmsc", 1.0)

        # Film - Image variables
        PBRTRenderSetting.addStringAttribute(sAttr,  "mImageFilmFileFormat", "filmImageFileFormat", "fiff", "OpenEXR (.exr)")
 
        # Reconstruction Filter variables
        PBRTRenderSetting.addStringAttribute(sAttr,  "mFilter", "filter", "flt", "Gaussian")

        PBRTRenderSetting.addFloatAttribute(nAttr,   "mFilterXWidth", "filterXWidth", "fltxw", 2.0)
        PBRTRenderSetting.addFloatAttribute(nAttr,   "mFilterYWidth", "filterYWidth", "fltyw", 2.0)
        PBRTRenderSetting.addFloatAttribute(nAttr,   "mFilterAlpha", "filterAlpha", "fltal", 2.0)
        PBRTRenderSetting.addFloatAttribute(nAttr,   "mFilterB", "filterB", "fltb", 0.333)
        PBRTRenderSetting.addFloatAttribute(nAttr,   "mFilterC", "filterC", "fltc", 0.333)
        PBRTRenderSetting.addFloatAttribute(nAttr,   "mFilterTau", "filterTau", "fltt", 3.0)

        # Camera variables
        PBRTRenderSetting.addStringAttribute(sAttr,  "mCameraOverride", "cameraOverride", "co", "None")

        PBRTRenderSetting.addStringAttribute(sAttr,  "mCameraRealisticLensFile", "cameraRealisticLensFile", "crlf", "")
        PBRTRenderSetting.addBooleanAttribute(nAttr,  "mCameraRealisticSimpleWeighting", "cameraRealisticSimpleWeighting", "crsw", True)
        PBRTRenderSetting.addFloatAttribute(nAttr,  "mCameraRealisticApertureDiameter", "cameraRealisticApertureDiameter", "crad", 1.0)
        PBRTRenderSetting.addFloatAttribute(nAttr,  "mCameraRealisticFocusDistance", "cameraRealisticFocusDistance", "crfd", 10.0)

         # Overall controls
        PBRTRenderSetting.addBooleanAttribute(nAttr, "mMotionBlur", "motionBlur", "mb", False)
        PBRTRenderSetting.addBooleanAttribute(nAttr, "mExportOnly", "exportOnly", "eo", False)
        PBRTRenderSetting.addBooleanAttribute(nAttr, "mKeepTempFiles", "keepTempFiles", "kt", False)
        PBRTRenderSetting.addBooleanAttribute(nAttr, "mSkipGeometryExport", "skipGeometryExport", "sge", False)
        PBRTRenderSetting.addBooleanAttribute(nAttr, "mUsePLYExport", "usePLYExport", "uplye", True)
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mVerboseRender", "verboseRender", "vbr", 2)
        PBRTRenderSetting.addBooleanAttribute(nAttr, "mVerboseExport", "verboseExport", "vbe", False)
        PBRTRenderSetting.addIntegerAttribute(nAttr, "mThreads", "threads", "th", 0)

        PBRTRenderSetting.addStringAttribute(sAttr, "mCommandLineParameters", "commandLineParameters", "clp", "")


    except:
        sys.stderr.write("Failed to create and add attributes\n")
        raise

    try:
        # Path to executables
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mPBRTPath)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mOIIOToolPath)

        # Version variables
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mPBRTVersion)

        # Sampler variables
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mSampler)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mSamplerPixelSamples)

        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mSamplerMaxMinDimensions)

        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mSamplerStratifedJitter)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mSamplerStratifedXSamples)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mSamplerStratifedYSamples)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mSamplerStratifedDimensions)

        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mSamplerLowDiscrepancyDimensions)

        # Accelerator variables
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mAccelerator)

        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mAcceleratorKDTreeIntersectCost)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mAcceleratorKDTreeTraversalCost)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mAcceleratorKDTreeEmptyBonus)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mAcceleratorKDTreeMaxPrims)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mAcceleratorKDTreeMaxDepth)

        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mAcceleratorBVHSplitMethod)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mAcceleratorBVHMaxNodePrims)

        # Integrator variables
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegrator)

        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorPathMaxDepth)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorPathRRThreshold)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorPathLightSampleStrategy)

        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorBidirectionalPathMaxDepth)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorBidirectionalPathVisualizeStrategies)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorBidirectionalPathVisualizeWeights)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorBidirectionalPathLightSampleStrategy)

        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorDirectLightingMaxDepth)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorDirectLightingStrategy)

        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorMetropolisLightTransportMaxDepth)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorMetropolisLightTransportBootstrapSamples)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorMetropolisLightTransportChains)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorMetropolisLightTransportMutationsPerPixel)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorMetropolisLightTransportLargeStepProbability)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorMetropolisLightTransportSigma)

        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorStochasticProgressivePhotonMapNumIterations)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorStochasticProgressivePhotonMapMaxDepth)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorStochasticProgressivePhotonMapPhotonsPerIteration)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorStochasticProgressivePhotonMapImageWriteFrequency)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorStochasticProgressivePhotonMapRadius)

        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorVolumetricPathMaxDepth)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorVolumetricPathRRThreshold)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorVolumetricPathLightSampleStrategy)

        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mIntegratorWhittedMaxDepth)

        # Film variables
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mFilm)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mFilmMaxSampleLuminance)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mFilmScale)

        # Film - Image variables
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mImageFilmFileFormat)
 
        # Reconstruction Filter variables
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mFilter)

        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mFilterXWidth)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mFilterYWidth)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mFilterAlpha)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mFilterB)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mFilterC)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mFilterTau)

        # Camera variables
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mCameraOverride)

        # Camera - Realistic variables
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mCameraRealisticLensFile)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mCameraRealisticSimpleWeighting)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mCameraRealisticApertureDiameter)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mCameraRealisticFocusDistance)

        # Overall controls
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mMotionBlur)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mExportOnly)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mKeepTempFiles)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mSkipGeometryExport)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mUsePLYExport)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mVerboseRender)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mVerboseExport)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mThreads)
        PBRTRenderSetting.addAttribute(PBRTRenderSetting.mCommandLineParameters)

    except:
        sys.stderr.write("Failed to add attributes\n")
        raise
        
# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerNode( kPluginNodeName, 
                              kPluginNodeId, 
                              nodeCreator, 
                              nodeInitializer, 
                              OpenMayaMPx.MPxNode.kDependNode )
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
                
