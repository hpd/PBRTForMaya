import os
import sys

import maya.cmds as cmds

from PBRTRenderer import createRenderSettingsNode, getRenderSettingsNode

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

global renderSettings

global renderSettingsWindow
global samplerFrames
global acceleratorFrames
global integratorFrames
global filmFrames
global filterFrames
global cameraOverrideFrames

def changeMenu(menu, attribute, renderSettings, value):
    #selected = cmds.optionMenu(menu, query=True, value=True)
    cmds.setAttr("%s.%s" % (renderSettings, attribute), value, type="string")

#
# Sampler Frames
#
def createSamplerFramesMaxMin(renderSettings):
    samplerMaxMinDimensions = cmds.getAttr("%s.%s" % (renderSettings, "samplerMaxMinDimensions"))

    imageSettings = cmds.frameLayout(label="Max Min", cll=True)

    cmds.intFieldGrp(numberOfFields=1, label="Dimensions", value1=samplerMaxMinDimensions,
        changeCommand=lambda (x): getIntFieldGroup(None, "samplerMaxMinDimensions", x))

    cmds.setParent('..')

    return imageSettings

def createSamplerFramesStratified(renderSettings):
    samplerStratifedJitter = cmds.getAttr("%s.%s" % (renderSettings, "samplerStratifedJitter"))
    samplerStratifedXSamples = cmds.getAttr("%s.%s" % (renderSettings, "samplerStratifedXSamples"))
    samplerStratifedYSamples = cmds.getAttr("%s.%s" % (renderSettings, "samplerStratifedYSamples"))
    samplerStratifedDimensions = cmds.getAttr("%s.%s" % (renderSettings, "samplerStratifedDimensions"))

    imageSettings = cmds.frameLayout(label="Stratified", cll=True)

    cmds.checkBox("Jitter", value=samplerStratifedJitter, 
        changeCommand=lambda (x): getCheckBox(None, "samplerStratifedJitter", x))
    cmds.intFieldGrp(numberOfFields=1, label="X Samples", value1=samplerStratifedXSamples,
        changeCommand=lambda (x): getIntFieldGroup(None, "samplerStratifedXSamples", x))
    cmds.intFieldGrp(numberOfFields=1, label="Y Samples", value1=samplerStratifedYSamples,
        changeCommand=lambda (x): getIntFieldGroup(None, "samplerStratifedYSamples", x))
    cmds.intFieldGrp(numberOfFields=1, label="Dimensions", value1=samplerStratifedDimensions,
        changeCommand=lambda (x): getIntFieldGroup(None, "samplerStratifedDimensions", x))

    cmds.setParent('..')

    return imageSettings

def createSamplerFramesLowDiscrepancy(renderSettings):
    samplerLowDiscrepancyDimensions = cmds.getAttr("%s.%s" % (renderSettings, "samplerLowDiscrepancyDimensions"))

    imageSettings = cmds.frameLayout(label="Low Discrepancy", cll=True)

    cmds.intFieldGrp(numberOfFields=1, label="Dimensions", value1=samplerLowDiscrepancyDimensions,
        changeCommand=lambda (x): getIntFieldGroup(None, "samplerLowDiscrepancyDimensions", x))

    cmds.setParent('..')

    return imageSettings

def createSamplerFrames(renderSettings):
    global samplerFrames
    samplerFrames = []

    # Sampler Frames
    maxMinSettings = createSamplerFramesMaxMin(renderSettings)
    stratifiedSettings = createSamplerFramesStratified(renderSettings)
    lowDiscrepancySettings = createSamplerFramesLowDiscrepancy(renderSettings)

    samplerFrames.append(maxMinSettings)
    samplerFrames.append(stratifiedSettings)
    samplerFrames.append(lowDiscrepancySettings)

#
# Accelerator Frames
#
def createAcceleratorFrameKDTree(renderSettings):
    acceleratorKDTreeIntersectCost = cmds.getAttr("%s.%s" % (renderSettings, "acceleratorKDTreeIntersectCost"))
    acceleratorKDTreeTraversalCost = cmds.getAttr("%s.%s" % (renderSettings, "acceleratorKDTreeTraversalCost"))
    acceleratorKDTreeEmptyBonus = cmds.getAttr("%s.%s" % (renderSettings, "acceleratorKDTreeEmptyBonus"))
    acceleratorKDTreeMaxPrims = cmds.getAttr("%s.%s" % (renderSettings, "acceleratorKDTreeMaxPrims"))
    acceleratorKDTreeMaxDepth = cmds.getAttr("%s.%s" % (renderSettings, "acceleratorKDTreeMaxDepth"))

    acceleratorSettings = cmds.frameLayout(label="KD Tree", cll=True)

    cmds.intFieldGrp(numberOfFields=1, label="Intersect Cost", value1=acceleratorKDTreeIntersectCost,
        changeCommand=lambda (x): getIntFieldGroup(None, "acceleratorKDTreeIntersectCost", x))
    cmds.intFieldGrp(numberOfFields=1, label="Traversal Cost", value1=acceleratorKDTreeTraversalCost,
        changeCommand=lambda (x): getIntFieldGroup(None, "acceleratorKDTreeTraversalCost", x))
    cmds.floatFieldGrp(numberOfFields=1, label="Empty Bonus", value1=acceleratorKDTreeEmptyBonus,
        changeCommand=lambda (x): getFloatFieldGroup(None, "acceleratorKDTreeEmptyBonus", x))
    cmds.intFieldGrp(numberOfFields=1, label="Max Prims", value1=acceleratorKDTreeMaxPrims,
        changeCommand=lambda (x): getIntFieldGroup(None, "acceleratorKDTreeMaxPrims", x))
    cmds.intFieldGrp(numberOfFields=1, label="Max Depth", value1=acceleratorKDTreeMaxDepth,
        changeCommand=lambda (x): getIntFieldGroup(None, "acceleratorKDTreeMaxDepth", x))

    cmds.setParent('..')

    return acceleratorSettings

def createAcceleratorFrameBVH(renderSettings):
    acceleratorBVHSplitMethod = cmds.getAttr("%s.%s" % (renderSettings, "acceleratorBVHSplitMethod"))
    acceleratorBVHMaxNodePrims = cmds.getAttr("%s.%s" % (renderSettings, "acceleratorBVHMaxNodePrims"))

    acceleratorSettings = cmds.frameLayout(label="BVH", cll=True)

    splitMethodMenu = cmds.optionMenu(label="Split Method")
    cmds.optionMenu(splitMethodMenu, edit=True,
        changeCommand=lambda (x): changeMenu(splitMethodMenu, "acceleratorBVHSplitMethod", renderSettings, x))
    cmds.menuItem('SAH')
    cmds.menuItem('HLBVH')
    cmds.menuItem('Middle')
    cmds.menuItem('Equal')

    if acceleratorBVHSplitMethod not in ["", None]:
        cmds.optionMenu(splitMethodMenu, edit=True, value=acceleratorBVHSplitMethod)

    cmds.intFieldGrp(numberOfFields=1, label="Max Node Prims", value1=acceleratorBVHMaxNodePrims,
        changeCommand=lambda (x): getIntFieldGroup(None, "acceleratorBVHMaxNodePrims", x))

    cmds.setParent('..')

    return acceleratorSettings

def createAcceleratorFrames(renderSettings):
    global acceleratorFrames
    acceleratorFrames = []

    # Accelerator Frames
    kdtreeSettings = createAcceleratorFrameKDTree(renderSettings)
    bvhSettings = createAcceleratorFrameBVH(renderSettings)

    acceleratorFrames.append(kdtreeSettings)
    acceleratorFrames.append(bvhSettings)

#
# Integrator Frames
#
def createIntegratorFramePath(renderSettings):
    integratorPathMaxDepth = cmds.getAttr("%s.%s" % (renderSettings, "integratorPathMaxDepth"))
    integratorPathRRThreshold = cmds.getAttr("%s.%s" % (renderSettings, "integratorPathRRThreshold"))
    integratorPathLightSampleStrategy = cmds.getAttr("%s.%s" % (renderSettings, "integratorPathLightSampleStrategy"))

    integratorSettings = cmds.frameLayout(label="Path Tracer", cll=True)

    cmds.intFieldGrp(numberOfFields=1, label="Max Depth", value1=integratorPathMaxDepth,
        changeCommand=lambda (x): getIntFieldGroup(None, "integratorPathMaxDepth", x))
    cmds.intFieldGrp(numberOfFields=1, label="Russian Roulette Thresh.", value1=integratorPathRRThreshold,
        changeCommand=lambda (x): getIntFieldGroup(None, "integratorPathRRThreshold", x))

    lightSampleStrategyMenu = cmds.optionMenu(label="Light Sample Strategy")
    cmds.optionMenu(lightSampleStrategyMenu, edit=True,
        changeCommand=lambda (x): changeMenu(lightSampleStrategyMenu, "integratorPathLightSampleStrategy", renderSettings, x))
    cmds.menuItem('Uniform')
    cmds.menuItem('Power')
    cmds.menuItem('Spatial')

    if integratorPathLightSampleStrategy not in ["", None]:
        cmds.optionMenu(lightSampleStrategyMenu, edit=True, value=integratorPathLightSampleStrategy)

    cmds.setParent('..')

    return integratorSettings

def createIntegratorFrameBidirectionalPath(renderSettings):
    integratorBidirectionalPathMaxDepth = cmds.getAttr("%s.%s" % (renderSettings, "integratorBidirectionalPathMaxDepth"))
    integratorBidirectionalPathVisualizeStrategies = cmds.getAttr("%s.%s" % (renderSettings, "integratorBidirectionalPathVisualizeStrategies"))
    integratorBidirectionalPathVisualizeWeights = cmds.getAttr("%s.%s" % (renderSettings, "integratorBidirectionalPathVisualizeWeights"))
    integratorBidirectionalPathLightSampleStrategy = cmds.getAttr("%s.%s" % (renderSettings, "integratorBidirectionalPathLightSampleStrategy"))

    integratorSettings = cmds.frameLayout(label="Bidirectional Path Tracer", cll=True)

    cmds.intFieldGrp(numberOfFields=1, label="Max Depth", value1=integratorBidirectionalPathMaxDepth,
        changeCommand=lambda (x): getIntFieldGroup(None, "integratorBidirectionalPathMaxDepth", x))
    cmds.checkBox("Visualize Strategies", value=integratorBidirectionalPathVisualizeStrategies, 
        changeCommand=lambda (x): getCheckBox(None, "integratorBidirectionalPathVisualizeStrategies", x))
    cmds.checkBox("Visualize Weights", value=integratorBidirectionalPathVisualizeWeights, 
        changeCommand=lambda (x): getCheckBox(None, "integratorBidirectionalPathVisualizeWeights", x))

    lightSampleStrategyMenu = cmds.optionMenu(label="Light Sample Strategy")
    cmds.optionMenu(lightSampleStrategyMenu, edit=True,
        changeCommand=lambda (x): changeMenu(lightSampleStrategyMenu, "integratorBidirectionalPathLightSampleStrategy", renderSettings, x))
    cmds.menuItem('Uniform')
    cmds.menuItem('Power')
    cmds.menuItem('Spatial')

    if integratorBidirectionalPathLightSampleStrategy not in ["", None]:
        cmds.optionMenu(lightSampleStrategyMenu, edit=True, value=integratorBidirectionalPathLightSampleStrategy)

    cmds.setParent('..')

    return integratorSettings

def createIntegratorFrameDirectLighting(renderSettings):
    integratorDirectLightingMaxDepth = cmds.getAttr("%s.%s" % (renderSettings, "integratorDirectLightingMaxDepth"))
    integratorDirectLightingStrategy = cmds.getAttr("%s.%s" % (renderSettings, "integratorDirectLightingStrategy"))

    integratorSettings = cmds.frameLayout(label="Direct Lighting", cll=True)

    cmds.intFieldGrp(numberOfFields=1, label="Max Depth", value1=integratorDirectLightingMaxDepth,
        changeCommand=lambda (x): getIntFieldGroup(None, "integratorDirectLightingMaxDepth", x))

    lightSampleStrategyMenu = cmds.optionMenu(label="Light Sample Strategy")
    cmds.optionMenu(lightSampleStrategyMenu, edit=True,
        changeCommand=lambda (x): changeMenu(lightSampleStrategyMenu, "integratorDirectLightingStrategy", renderSettings, x))
    cmds.menuItem('One')
    cmds.menuItem('All')

    if integratorDirectLightingStrategy not in ["", None]:
        cmds.optionMenu(lightSampleStrategyMenu, edit=True, value=integratorDirectLightingStrategy)

    cmds.setParent('..')

    return integratorSettings

def createIntegratorFrameMetropolisLightTransport(renderSettings):
    integratorMetropolisLightTransportMaxDepth = cmds.getAttr("%s.%s" % (renderSettings, "integratorMetropolisLightTransportMaxDepth"))
    integratorMetropolisLightTransportBootstrapSamples = cmds.getAttr("%s.%s" % (renderSettings, "integratorMetropolisLightTransportBootstrapSamples"))
    integratorMetropolisLightTransportChains = cmds.getAttr("%s.%s" % (renderSettings, "integratorMetropolisLightTransportChains"))
    integratorMetropolisLightTransportMutationsPerPixel = cmds.getAttr("%s.%s" % (renderSettings, "integratorMetropolisLightTransportMutationsPerPixel"))
    integratorMetropolisLightTransportLargeStepProbability = cmds.getAttr("%s.%s" % (renderSettings, "integratorMetropolisLightTransportLargeStepProbability"))
    integratorMetropolisLightTransportSigma = cmds.getAttr("%s.%s" % (renderSettings, "integratorMetropolisLightTransportSigma"))

    integratorSettings = cmds.frameLayout(label="Metropolis Light Transport", cll=True)

    cmds.intFieldGrp(numberOfFields=1, label="Max Depth", value1=integratorMetropolisLightTransportMaxDepth,
        changeCommand=lambda (x): getIntFieldGroup(None, "integratorMetropolisLightTransportMaxDepth", x))
    cmds.intFieldGrp(numberOfFields=1, label="Bootstrap Samples", value1=integratorMetropolisLightTransportBootstrapSamples,
        changeCommand=lambda (x): getIntFieldGroup(None, "integratorMetropolisLightTransportBootstrapSamples", x))
    cmds.intFieldGrp(numberOfFields=1, label="Chains", value1=integratorMetropolisLightTransportChains,
        changeCommand=lambda (x): getIntFieldGroup(None, "integratorMetropolisLightTransportChains", x))
    cmds.intFieldGrp(numberOfFields=1, label="Mutations Per Pixel", value1=integratorMetropolisLightTransportMutationsPerPixel,
        changeCommand=lambda (x): getIntFieldGroup(None, "integratorMetropolisLightTransportMutationsPerPixel", x))

    cmds.floatFieldGrp(numberOfFields=1, label="Large Step Probability", value1=integratorMetropolisLightTransportLargeStepProbability,
        changeCommand=lambda (x): getFloatFieldGroup(None, "integratorMetropolisLightTransportLargeStepProbability", x))
    cmds.floatFieldGrp(numberOfFields=1, label="Sigma", value1=integratorMetropolisLightTransportSigma,
        changeCommand=lambda (x): getFloatFieldGroup(None, "integratorMetropolisLightTransportSigma", x))

    cmds.setParent('..')

    return integratorSettings

def createIntegratorFrameStochasticProgressivePhotonMap(renderSettings):
    integratorStochasticProgressivePhotonMapNumIterations = cmds.getAttr("%s.%s" % (renderSettings, "integratorStochasticProgressivePhotonMapNumIterations"))
    integratorStochasticProgressivePhotonMapMaxDepth = cmds.getAttr("%s.%s" % (renderSettings, "integratorStochasticProgressivePhotonMapMaxDepth"))
    integratorStochasticProgressivePhotonMapPhotonsPerIteration = cmds.getAttr("%s.%s" % (renderSettings, "integratorStochasticProgressivePhotonMapPhotonsPerIteration"))
    integratorStochasticProgressivePhotonMapImageWriteFrequency = cmds.getAttr("%s.%s" % (renderSettings, "integratorStochasticProgressivePhotonMapImageWriteFrequency"))
    integratorStochasticProgressivePhotonMapRadius = cmds.getAttr("%s.%s" % (renderSettings, "integratorStochasticProgressivePhotonMapRadius"))

    integratorSettings = cmds.frameLayout(label="Stochastic Progressive Photon Map", cll=True)

    cmds.intFieldGrp(numberOfFields=1, label="Num Iterations", value1=integratorStochasticProgressivePhotonMapNumIterations,
        changeCommand=lambda (x): getIntFieldGroup(None, "integratorStochasticProgressivePhotonMapNumIterations", x))
    cmds.intFieldGrp(numberOfFields=1, label="Max Depth", value1=integratorStochasticProgressivePhotonMapMaxDepth,
        changeCommand=lambda (x): getIntFieldGroup(None, "integratorStochasticProgressivePhotonMapMaxDepth", x))
    cmds.intFieldGrp(numberOfFields=1, label="Photons Per Iteration", value1=integratorStochasticProgressivePhotonMapPhotonsPerIteration,
        changeCommand=lambda (x): getIntFieldGroup(None, "integratorStochasticProgressivePhotonMapPhotonsPerIteration", x))
    cmds.intFieldGrp(numberOfFields=1, label="Image Write Frequency", value1=integratorStochasticProgressivePhotonMapImageWriteFrequency,
        changeCommand=lambda (x): getIntFieldGroup(None, "integratorStochasticProgressivePhotonMapImageWriteFrequency", x))

    cmds.floatFieldGrp(numberOfFields=1, label="Radius", value1=integratorStochasticProgressivePhotonMapRadius,
        changeCommand=lambda (x): getFloatFieldGroup(None, "integratorStochasticProgressivePhotonMapRadius", x))

    cmds.setParent('..')

    return integratorSettings


def createIntegratorFrameVolumetricPath(renderSettings):
    integratorVolumetricPathMaxDepth = cmds.getAttr("%s.%s" % (renderSettings, "integratorVolumetricPathMaxDepth"))
    integratorVolumetricPathRRThreshold = cmds.getAttr("%s.%s" % (renderSettings, "integratorVolumetricPathRRThreshold"))
    integratorVolumetricPathLightSampleStrategy = cmds.getAttr("%s.%s" % (renderSettings, "integratorVolumetricPathLightSampleStrategy"))

    integratorSettings = cmds.frameLayout(label="Volumetric Path Tracer", cll=True)

    cmds.intFieldGrp(numberOfFields=1, label="Max Depth", value1=integratorVolumetricPathMaxDepth,
        changeCommand=lambda (x): getIntFieldGroup(None, "integratorVolumetricPathMaxDepth", x))
    cmds.intFieldGrp(numberOfFields=1, label="Russian Roulette Thresh.", value1=integratorVolumetricPathRRThreshold,
        changeCommand=lambda (x): getIntFieldGroup(None, "integratorVolumetricPathRRThreshold", x))

    lightSampleStrategyMenu = cmds.optionMenu(label="Light Sample Strategy")
    cmds.optionMenu(lightSampleStrategyMenu, edit=True,
        changeCommand=lambda (x): changeMenu(lightSampleStrategyMenu, "integratorVolumetricPathLightSampleStrategy", renderSettings, x))
    cmds.menuItem('Uniform')
    cmds.menuItem('Power')
    cmds.menuItem('Spatial')

    if integratorVolumetricPathLightSampleStrategy not in ["", None]:
        cmds.optionMenu(lightSampleStrategyMenu, edit=True, value=integratorVolumetricPathLightSampleStrategy)

    cmds.setParent('..')

    return integratorSettings

def createIntegratorFrameWhitted(renderSettings):
    integratorWhittedMaxDepth = cmds.getAttr("%s.%s" % (renderSettings, "integratorWhittedMaxDepth"))

    integratorSettings = cmds.frameLayout(label="Whitted Path Tracer", cll=True)

    cmds.intFieldGrp(numberOfFields=1, label="Max Depth", value1=integratorWhittedMaxDepth,
        changeCommand=lambda (x): getIntFieldGroup(None, "integratorWhittedMaxDepth", x))

    cmds.setParent('..')

    return integratorSettings

def createIntegratorFrames(renderSettings):
    global integratorFrames
    integratorFrames = []

    # Integrator Frames
    pathSettings = createIntegratorFramePath(renderSettings)
    bdptSettings = createIntegratorFrameBidirectionalPath(renderSettings)
    directLightingSettings = createIntegratorFrameDirectLighting(renderSettings)
    mltSettings = createIntegratorFrameMetropolisLightTransport(renderSettings)
    sppmSettings = createIntegratorFrameStochasticProgressivePhotonMap(renderSettings)
    volpathSettings = createIntegratorFrameVolumetricPath(renderSettings)
    whittedSettings = createIntegratorFrameWhitted(renderSettings)

    integratorFrames.append(pathSettings)
    integratorFrames.append(bdptSettings)
    integratorFrames.append(directLightingSettings)
    integratorFrames.append(mltSettings)
    integratorFrames.append(sppmSettings)
    integratorFrames.append(volpathSettings)
    integratorFrames.append(whittedSettings)

#
# Film Frames
#
def createFilmFrameImage(renderSettings):
    existingFilmMaxSampleLuminance = cmds.getAttr("%s.%s" % (renderSettings, "filmMaxSampleLuminance"))
    existingFilmScale = cmds.getAttr("%s.%s" % (renderSettings, "filmScale"))
    filmImageFileFormat = cmds.getAttr("%s.%s" % (renderSettings, "filmImageFileFormat"))

    imageSettings = cmds.frameLayout(label="Image Film", cll=True)

    fileFormatMenu = cmds.optionMenu(label="File Format")
    cmds.optionMenu(fileFormatMenu, edit=True,
        changeCommand=lambda (x): changeMenu(fileFormatMenu, "filmImageFileFormat", renderSettings, x))
    cmds.menuItem('OpenEXR (.exr)')
    cmds.menuItem('TGA (.tga)')
    cmds.menuItem('Portable Float Map (.pfm)')

    if filmImageFileFormat not in ["", None]:
        cmds.optionMenu(fileFormatMenu, edit=True, value=filmImageFileFormat)

    cmds.floatFieldGrp(numberOfFields=1, label="Max Sample Luminance", 
        value1=existingFilmMaxSampleLuminance, precision=3,
        changeCommand=lambda (x): getFloatFieldGroup(None, "filmMaxSampleLuminance", x))

    cmds.floatFieldGrp(numberOfFields=1, label="Scale", 
        value1=existingFilmScale, precision=3,
        changeCommand=lambda (x): getFloatFieldGroup(None, "filmScale", x))

    cmds.setParent('..')

    return imageSettings

def createFilmFrames(renderSettings):
    global filmFrames
    filmFrames = []

    # Film Settings
    imageSettings = createFilmFrameImage(renderSettings)

    filmFrames.append(imageSettings)

#
# Filter Frames
#
def createFilterFrameGaussian(renderSettings):
    existingFilterAlpha = cmds.getAttr("%s.%s" % (renderSettings, "filterAlpha"))

    imageSettings = cmds.frameLayout(label="Gaussian", cll=True)

    cmds.floatFieldGrp(numberOfFields=1, label="Alpha", value1=existingFilterAlpha,
        changeCommand=lambda (x): getFloatFieldGroup(None, "filterAlpha", x))

    cmds.setParent('..')

    return imageSettings

def createFilterFrameMitchell(renderSettings):
    existingFilterB = cmds.getAttr("%s.%s" % (renderSettings, "filterB"))
    existingFilterC = cmds.getAttr("%s.%s" % (renderSettings, "filterC"))

    imageSettings = cmds.frameLayout(label="Mitchell", cll=True)

    cmds.floatFieldGrp(numberOfFields=1, label="B", value1=existingFilterB,
        changeCommand=lambda (x): getFloatFieldGroup(None, "filterB", x))
    cmds.floatFieldGrp(numberOfFields=1, label="C", value1=existingFilterC,
        changeCommand=lambda (x): getFloatFieldGroup(None, "filterC", x))

    cmds.setParent('..')

    return imageSettings

def createFilterFrameSinc(renderSettings):
    existingFilterTau = cmds.getAttr("%s.%s" % (renderSettings, "filterTau"))

    imageSettings = cmds.frameLayout(label="Sinc", cll=True)

    cmds.floatFieldGrp(numberOfFields=1, label="Tau", value1=existingFilterTau,
        changeCommand=lambda (x): getFloatFieldGroup(None, "filterTau", x))

    cmds.setParent('..')

    return imageSettings

def createFilterFrames(renderSettings):
    global filterFrames
    filterFrames = []

    # Filter Settings
    gaussianSettings = createFilterFrameGaussian(renderSettings)
    mitchellSettings = createFilterFrameMitchell(renderSettings)
    sincSettings = createFilterFrameSinc(renderSettings)

    filterFrames.append(gaussianSettings)
    filterFrames.append(mitchellSettings)
    filterFrames.append(sincSettings)

#
# Filter Frames
#
def createCameraOverrideRealistic(renderSettings):
    existingCameraRealisticLensFile = cmds.getAttr("%s.%s" % (renderSettings, "cameraRealisticLensFile"), asString=True)
    existingCameraRealisticSimpleWeighting = cmds.getAttr("%s.%s" % (renderSettings, "cameraRealisticSimpleWeighting"))
    existingCameraRealisticApertureDiameter = cmds.getAttr("%s.%s" % (renderSettings, "cameraRealisticApertureDiameter"))
    existingCameraRealisticFocusDistance = cmds.getAttr("%s.%s" % (renderSettings, "cameraRealisticFocusDistance"))

    settings = cmds.frameLayout(label="Realistic Perspective", cll=True)

    cameraRealisticLensFileGroup = cmds.textFieldButtonGrp(label="Lens File", 
        buttonLabel="Open", buttonCommand="browseFiles")
    # Get default
    if existingCameraRealisticLensFile not in ["", None]:
        cmds.textFieldButtonGrp(cameraRealisticLensFileGroup, e=1, text=existingCameraRealisticLensFile)
    cmds.textFieldButtonGrp(cameraRealisticLensFileGroup, e=1, 
        buttonCommand=lambda: getRenderSettingsPath(cameraRealisticLensFileGroup, "cameraRealisticLensFile"),
        changeCommand=lambda (x): getTextFieldGroup(None, "cameraRealisticLensFile", x))

    cmds.checkBox("Simple Weighting", value=existingCameraRealisticSimpleWeighting, 
        changeCommand=lambda (x): getCheckBox(None, "cameraRealisticSimpleWeighting", x))
    cmds.floatFieldGrp(numberOfFields=1, label="Aperture Diameter", value1=existingCameraRealisticApertureDiameter,
        changeCommand=lambda (x): getFloatFieldGroup(None, "cameraRealisticApertureDiameter", x))
    cmds.floatFieldGrp(numberOfFields=1, label="Focus Distance", value1=existingCameraRealisticFocusDistance,
        changeCommand=lambda (x): getFloatFieldGroup(None, "cameraRealisticFocusDistance", x))

    cmds.setParent('..')

    return settings

def createCameraOverrideFrames(renderSettings):
    global cameraOverrideFrames
    cameraOverrideFrames = []

    # Camera Settings
    realisticSettings = createCameraOverrideRealistic(renderSettings)

    cameraOverrideFrames.append(realisticSettings)

#
# Utilities
#
def getRenderSettingsPath(name, renderSettingsAttribute=None):
    global renderSettings

    path = cmds.fileDialog2(fileMode=1, fileFilter="*")
    if path not in [None, []]:
        strPath = str(path[0])
        cmds.textFieldButtonGrp(name, e=1, text=strPath)
        if renderSettingsAttribute:
            cmds.setAttr("%s.%s" % (renderSettings, renderSettingsAttribute), strPath, type="string")

def getCheckBox(name, renderSettingsAttribute=None, value=None):
    global renderSettings

    if renderSettingsAttribute:
        attr = "%s.%s" % (renderSettings, renderSettingsAttribute)
        cmds.setAttr(attr, value)

def getIntFieldGroup(name, renderSettingsAttribute=None, value=None):
    global renderSettings

    if renderSettingsAttribute:
        attr = "%s.%s" % (renderSettings, renderSettingsAttribute)
        cmds.setAttr(attr, value)

def getFloatFieldGroup(name, renderSettingsAttribute=None, value=None):
    global renderSettings

    if renderSettingsAttribute:
        attr = "%s.%s" % (renderSettings, renderSettingsAttribute)
        cmds.setAttr(attr, value)

def getTextFieldGroup(name, renderSettingsAttribute=None, value=None):
    global renderSettings

    if renderSettingsAttribute:
        attr = "%s.%s" % (renderSettings, renderSettingsAttribute)
        cmds.setAttr(attr, value, type="string")

def getOptionMenu(name, renderSettingsAttribute=None, value=None,
    attrType="string"):
    global renderSettings

    if renderSettingsAttribute:
        attr = "%s.%s" % (renderSettings, renderSettingsAttribute)
        if attrType == "string":
            cmds.setAttr(attr, value, type=attrType)
        else:
            cmds.setAttr(attr, value)

'''
This function creates the render settings window.
This includes the integrator, sample generator, image filter,
and film type.
'''
def createRenderSettingsUI():
    global renderSettings
    renderSettings = getRenderSettingsNode()

    global renderSettingsWindow

    #print( "\n\n\nPBRT Render Settings - Create UI - Python - %s\n\n\n" % renderSettings )

    parentForm = cmds.setParent(query=True)

    PBRTGlobalsScrollLayout = cmds.scrollLayout(horizontalScrollBarThickness=0)
    cmds.columnLayout(adjustableColumn=True)

    #
    # Paths
    #

    # Path to executable
    PBRTPathGroup = cmds.textFieldButtonGrp(label="PBRT Path", 
        buttonLabel="Open", buttonCommand="browseFiles")
    # Get default
    existingPBRTPath = cmds.getAttr( "%s.%s" % (renderSettings, "PBRTPath"))
    if existingPBRTPath not in ["", None]:
        cmds.textFieldButtonGrp(PBRTPathGroup, e=1, text=existingPBRTPath)
    cmds.textFieldButtonGrp(PBRTPathGroup, e=1, 
        buttonCommand=lambda: getRenderSettingsPath(PBRTPathGroup, "PBRTPath"),
        changeCommand=lambda (x): getTextFieldGroup(None, "PBRTPath", x))

    # Path to executable
    oiiotoolPathGroup = cmds.textFieldButtonGrp(label="oiiotool Path", 
        buttonLabel="Open", buttonCommand="browseFiles")
    # Get default
    existingOIIOToolPath = cmds.getAttr( "%s.%s" % (renderSettings, "oiiotoolPath"))
    if existingOIIOToolPath not in ["", None]:
        cmds.textFieldButtonGrp(oiiotoolPathGroup, e=1, text=existingOIIOToolPath)
    cmds.textFieldButtonGrp(oiiotoolPathGroup, e=1, 
        buttonCommand=lambda: getRenderSettingsPath(oiiotoolPathGroup, "oiiotoolPath"),
        changeCommand=lambda (x): getTextFieldGroup(None, "oiiotoolPath", x))

    #
    # Version
    #
    cmds.frameLayout(label='PBRT Version', collapsable=True, collapse=False)
    cmds.columnLayout(adjustableColumn=True)

    existingPBRTVersion = cmds.getAttr( "%s.%s" % (renderSettings, "PBRTVersion"))
    pbrtVersionMenu = cmds.optionMenu(label="PBRT Version", changeCommand=changePBRTVersion)

    cmds.menuItem('v3 Master Branch')
    cmds.menuItem('v3 Book')

    if existingPBRTVersion not in ["", None]:
        cmds.optionMenu(pbrtVersionMenu, edit=True, value=existingPBRTVersion)
    else:
        cmds.optionMenu(pbrtVersionMenu, edit=True, select=0)
        existingPBRTVersion = "v3 Book"

    changePBRTVersion(existingPBRTVersion)

    cmds.setParent('..')
    cmds.setParent('..')

    #
    # Sampler controls
    #
    cmds.frameLayout(label='Sampler', collapsable=True, collapse=False)
    cmds.columnLayout(adjustableColumn=True)

    existingSampler = cmds.getAttr( "%s.%s" % (renderSettings, "sampler"))
    samplerMenu = cmds.optionMenu(label="Sampler", changeCommand=changeSampler)

    createSamplerFrames(renderSettings)

    cmds.menuItem('Halton')
    cmds.menuItem('Max Min')
    cmds.menuItem('Random')
    cmds.menuItem('Sobol')
    cmds.menuItem('Stratified')
    cmds.menuItem('Low Discrepancy')

    if existingSampler not in ["", None]:
        cmds.optionMenu(samplerMenu, edit=True, value=existingSampler)
    else:
        cmds.optionMenu(samplerMenu, edit=True, select=0)
        existingSampler = "Halton"

    changeSampler(existingSampler)

    existingPixelSamples = cmds.getAttr("%s.%s" % (renderSettings, "samplerPixelSamples"))
    cmds.intFieldGrp(numberOfFields=1, label="Pixel Samples", value1=existingPixelSamples,
        changeCommand=lambda (x): getIntFieldGroup(None, "samplerPixelSamples", x))

    cmds.setParent('..')
    cmds.setParent('..')

    #
    # Accelerator controls
    #
    cmds.frameLayout(label='Accelerator', collapsable=True, collapse=True)
    cmds.columnLayout(adjustableColumn=True)

    existingAccelerator = cmds.getAttr( "%s.%s" % (renderSettings, "accelerator"))

    acceleratorMenu = cmds.optionMenu(label="Accelerator", changeCommand=changeAccelerator)
    cmds.menuItem('KD Tree')
    cmds.menuItem('BVH')

    createAcceleratorFrames(renderSettings)

    if existingAccelerator not in ["", None]:
        cmds.optionMenu(acceleratorMenu, edit=True, value=existingAccelerator)
    else:
        cmds.optionMenu(acceleratorMenu, edit=True, select=0)
        existingAccelerator = "BVH"

    changeAccelerator(existingAccelerator)

    cmds.setParent('..')
    cmds.setParent('..')

    #
    # Integrator controls
    #
    cmds.frameLayout(label='Integrator', collapsable=True, collapse=False)
    cmds.columnLayout(adjustableColumn=True)

    existingIntegrator = cmds.getAttr( "%s.%s" % (renderSettings, "integrator"))

    integratorMenu = cmds.optionMenu(label="Integrator", changeCommand=changeIntegrator)
    cmds.menuItem('Path Tracer')
    cmds.menuItem('Bidirectional Path Tracer')
    cmds.menuItem('Direct Lighting')
    cmds.menuItem('Metropolis Light Transport')
    cmds.menuItem('Stochastic Progressive Photon Map')
    cmds.menuItem('Volumetric Path Tracer')
    cmds.menuItem('Whitted Path Tracer')

    createIntegratorFrames(renderSettings)

    if existingIntegrator not in ["", None]:
        cmds.optionMenu(integratorMenu, edit=True, value=existingIntegrator)
    else:
        cmds.optionMenu(integratorMenu, edit=True, select=0)
        existingIntegrator = "Path Tracer"

    changeIntegrator(existingIntegrator)

    cmds.setParent('..')
    cmds.setParent('..')

    #
    # Film controls
    #
    cmds.frameLayout(label='Film', collapsable=True, collapse=True)
    cmds.columnLayout(adjustableColumn=True)

    existingFilm = cmds.getAttr( "%s.%s" % (renderSettings, "film"))

    filmMenu = cmds.optionMenu(label="Film", changeCommand=changeFilm)
    cmds.menuItem('Image Film')

    createFilmFrames(renderSettings)

    if existingFilm not in ["", None]:
        cmds.optionMenu(filmMenu, edit=True, value=existingFilm)
    else:
        cmds.optionMenu(filmMenu, edit=True, select=0)
        existingFilm = "Image Film"

    changeFilm(existingFilm)

    cmds.setParent('..')
    cmds.setParent('..')

    #
    # Filter controls
    #
    cmds.frameLayout(label='Reconstruction Filter', collapsable=True, collapse=True)
    cmds.columnLayout(adjustableColumn=True)

    existingReconstructionFilter = cmds.getAttr( "%s.%s" % (renderSettings, "filter"))

    rfilterMenu = cmds.optionMenu(label="Filter", 
        changeCommand=changeFilter)
    cmds.menuItem("Box")
    cmds.menuItem("Gaussian")
    cmds.menuItem("Mitchell")
    cmds.menuItem("Sinc")
    cmds.menuItem("Triangle")

    createFilterFrames(renderSettings)

    if existingReconstructionFilter not in ["", None]:
        cmds.optionMenu(rfilterMenu, edit=True, value=existingReconstructionFilter)
        rfilter = existingReconstructionFilter
    else:
        cmds.optionMenu(rfilterMenu, edit=True, select=1)
        rfilter = "Gaussian"

    changeFilter(rfilter)

    existingFilterXWidth = cmds.getAttr("%s.%s" % (renderSettings, "filterXWidth"))
    cmds.floatFieldGrp(numberOfFields=1, label="X Width", value1=existingFilterXWidth,
        changeCommand=lambda (x): getFloatFieldGroup(None, "filterXWidth", x))

    existingFilterYWidth = cmds.getAttr("%s.%s" % (renderSettings, "filterYWidth"))
    cmds.floatFieldGrp(numberOfFields=1, label="Y Width", value1=existingFilterYWidth,
        changeCommand=lambda (x): getFloatFieldGroup(None, "filterYWidth", x))

    cmds.setParent('..')
    cmds.setParent('..')

    #
    # Camera controls
    #
    cmds.frameLayout(label='Camera', collapsable=True, collapse=True)
    cmds.columnLayout(adjustableColumn=True)

    existingCameraOverride = cmds.getAttr( "%s.%s" % (renderSettings, "cameraOverride"))

    cameraOverrideMenu = cmds.optionMenu(label="Camera Override", changeCommand=changeCameraOverride)
    cmds.menuItem('None')
    cmds.menuItem('Environment')
    cmds.menuItem('Realistic Perspective')

    createCameraOverrideFrames(renderSettings)

    if existingCameraOverride not in ["None", "", None]:
        cmds.optionMenu(cameraOverrideMenu, edit=True, value=existingCameraOverride)
        cameraOverride = existingCameraOverride
    else:
        cmds.optionMenu(cameraOverrideMenu, edit=True, select=1)
        cameraOverride = "None"

    changeCameraOverride(cameraOverride)

    cmds.setParent('..')
    cmds.setParent('..')

    #
    # Motion Blur controls
    #
    cmds.frameLayout(label='Motion Blur', collapsable=True, collapse=True)
    cmds.columnLayout(adjustableColumn=True)

    existingMotionBlur = cmds.getAttr( "%s.%s" % (renderSettings, "motionBlur"))
    motionBlur = cmds.checkBox(label="Motion Blur", value=existingMotionBlur)
    cmds.checkBox(motionBlur, edit=1,
        changeCommand=lambda (x): getCheckBox(motionBlur, "motionBlur", x))

    cmds.setParent('..')
    cmds.setParent('..')

    #
    # Overall controls
    #
    cmds.frameLayout(label='Overall', collapsable=True, collapse=False)
    cmds.columnLayout(adjustableColumn=True)

    existingVerboseRender = cmds.getAttr( "%s.%s" % (renderSettings, "verboseRender"))

    verboseRenderMenu = cmds.optionMenu(label="Render Verbosity", changeCommand=changeVerboseRender)
    cmds.menuItem('0 - Quiet')
    cmds.menuItem('1 - Progress')
    cmds.menuItem('2 - Info')
    cmds.menuItem('3 - Warning')
    cmds.menuItem('4 - Error')
    cmds.menuItem('5 - Fatal')

    if existingVerboseRender not in ["None", "", None]:
        cmds.optionMenu(verboseRenderMenu, edit=True, select=(existingVerboseRender+1))
    else:
        cmds.optionMenu(verboseRenderMenu, edit=True, select=2)

    existingThreads = cmds.getAttr( "%s.%s" % (renderSettings, "threads"))
    changeThreads = lambda (x): getIntFieldGroup(None, "threads", x)
    threadsGroup = cmds.intFieldGrp(numberOfFields=1, label="Threads", value1=existingThreads)
    cmds.intFieldGrp(threadsGroup, edit=1, changeCommand=changeThreads)    

    existingVerboseExport = cmds.getAttr( "%s.%s" % (renderSettings, "verboseExport"))
    verboseExport = cmds.checkBox(label="Export Verbosity", value=existingVerboseExport)
    cmds.checkBox(verboseExport, edit=1,
        changeCommand=lambda (x): getCheckBox(verboseExport, "verboseExport", x))

    existingExportOnly = cmds.getAttr( "%s.%s" % (renderSettings, "exportOnly"))
    exportOnly = cmds.checkBox(label="Export Only (No Render)", value=existingExportOnly)
    cmds.checkBox(exportOnly, edit=1,
        changeCommand=lambda (x): getCheckBox(exportOnly, "exportOnly", x))

    existingSkipGeometryExport = cmds.getAttr( "%s.%s" % (renderSettings, "skipGeometryExport"))
    skipGeometryExport = cmds.checkBox(label="Skip Geometry Export", value=existingSkipGeometryExport)
    cmds.checkBox(skipGeometryExport, edit=1,
        changeCommand=lambda (x): getCheckBox(skipGeometryExport, "skipGeometryExport", x))

    existingUsePLYExport = cmds.getAttr( "%s.%s" % (renderSettings, "usePLYExport"))
    usePLYExport = cmds.checkBox(label="Use PLY Export", value=existingUsePLYExport)
    cmds.checkBox(usePLYExport, edit=1,
        changeCommand=lambda (x): getCheckBox(usePLYExport, "usePLYExport", x))

    existingKeepTempFiles = cmds.getAttr( "%s.%s" % (renderSettings, "keepTempFiles"))
    keepTempFiles = cmds.checkBox(label="Keep Temp Files", value=existingKeepTempFiles)
    cmds.checkBox(keepTempFiles, edit=1,
        changeCommand=lambda (x): getCheckBox(keepTempFiles, "keepTempFiles", x))

    # Extra command line parameters
    commandLineParametersGroup = cmds.textFieldGrp(label="Extra Cmd Line Params")
    # Get default
    existingCommandLineParameters = cmds.getAttr( "%s.%s" % (renderSettings, "commandLineParameters"))
    if existingCommandLineParameters not in ["", None]:
        cmds.textFieldGrp(commandLineParametersGroup, e=1, text=existingCommandLineParameters)
    cmds.textFieldGrp(commandLineParametersGroup, e=1, 
        changeCommand=lambda (x): getTextFieldGroup(None, "commandLineParameters", x))

    cmds.setParent('..')
    cmds.setParent('..')


    af = []
    af.append((PBRTGlobalsScrollLayout, 'top', 0))
    af.append((PBRTGlobalsScrollLayout, 'bottom', 0))
    af.append((PBRTGlobalsScrollLayout, 'left', 0))
    af.append((PBRTGlobalsScrollLayout, 'right', 0))
    cmds.formLayout(parentForm, edit=True, attachForm=af)

def createRenderSettings():
    createRenderSettingsNode()
    createRenderSettingsUI()

def showRenderSettings(self):
    global renderSettingsWindow
    cmds.showWindow(renderSettingsWindow)

def getRenderWindowPanel():
    renderPanels = cmds.getPanel(scriptType="renderWindowPanel")

    if renderPanels == []: 
        renderPanel = cmds.scriptedPanel(type="renderWindowPanel", unParent=True) 
        #cmds.scriptedPanel(e=True, label=`interToUI $renderPanel` $renderPanel; 
    else: 
        renderPanel = renderPanels[0] 

    return renderPanel

def showRender(fileName):
    renderWindowName = getRenderWindowPanel()
    cmds.renderWindowEditor(renderWindowName, edit=True, loadImage=fileName)

#
# Turn UI frames on and off for various optins
#
def changePBRTVersion(selectedPBRTVersion):
    getOptionMenu(None, "PBRTVersion", selectedPBRTVersion)

def changeVerboseRender(selectedVerboseRender):
    tokens = selectedVerboseRender.split('-')
    verbosity = int(tokens[0].strip())
    getOptionMenu(None, "verboseRender", verbosity, attrType="int")

def changeSampler(selectedSampler):
    global samplerFrames

    #Set all other frameLayouts to be invisible
    for frame in samplerFrames:
        currentFrameLabel = cmds.frameLayout(frame, query=True, label=True)
        if currentFrameLabel == selectedSampler:
            cmds.frameLayout(frame, edit=True, visible=True)
        else:
            cmds.frameLayout(frame, edit=True, visible=False)

    getOptionMenu(None, "sampler", selectedSampler)

def changeAccelerator(selectedAccelerator):
    global acceleratorFrames

    #Set all other frameLayouts to be invisible
    for frame in acceleratorFrames:
        currentFrameLabel = cmds.frameLayout(frame, query=True, label=True)
        if currentFrameLabel == selectedAccelerator:
            cmds.frameLayout(frame, edit=True, visible=True)
        else:
            cmds.frameLayout(frame, edit=True, visible=False)

    getOptionMenu(None, "accelerator", selectedAccelerator)

def changeIntegrator(selectedIntegrator):
    global integratorFrames

    #Set all other frameLayouts to be invisible
    for frame in integratorFrames:
        currentFrameLabel = cmds.frameLayout(frame, query=True, label=True)
        if currentFrameLabel == selectedIntegrator:
            cmds.frameLayout(frame, edit=True, visible=True)
        else:
            cmds.frameLayout(frame, edit=True, visible=False)

    getOptionMenu(None, "integrator", selectedIntegrator)

def changeFilm(selectedFilm):
    global filmFrames

    #Set all other frameLayouts to be invisible
    for frame in filmFrames:
        currentFrameLabel = cmds.frameLayout(frame, query=True, label=True)
        if currentFrameLabel == selectedFilm:
            cmds.frameLayout(frame, edit=True, visible=True)
        else:
            cmds.frameLayout(frame, edit=True, visible=False)

    getOptionMenu(None, "film", selectedFilm)

def changeFilter(selectedFilter):
    global filterFrames

    #Set all other frameLayouts to be invisible
    for filterFrame in filterFrames:
        currentFrameLabel = cmds.frameLayout(filterFrame, query=True, label=True)
        if currentFrameLabel == selectedFilter:
            cmds.frameLayout(filterFrame, edit=True, visible=True)
        else:
            cmds.frameLayout(filterFrame, edit=True, visible=False)

    getOptionMenu(None, "filter", selectedFilter)

def changeCameraOverride(selectedCameraOverride):
    global cameraOverrideFrames

    #Set all other frameLayouts to be invisible
    for frame in cameraOverrideFrames:
        currentFrameLabel = cmds.frameLayout(frame, query=True, label=True)
        if currentFrameLabel == selectedCameraOverride:
            cmds.frameLayout(frame, edit=True, visible=True)
        else:
            cmds.frameLayout(frame, edit=True, visible=False)

    getOptionMenu(None, "cameraOverride", selectedCameraOverride)








