import inspect
import os
import sys

import maya.cmds as cmds
import maya.OpenMayaMPx as OpenMayaMPx

kPluginCmdName = "PBRT"

pluginDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(pluginDir)

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'util')))

from process import Process
from mayautil import createMelPythonCallback

# Import modules for settings, material, lights and volumes
import PBRTRenderSettings

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
renderSettings = None

#
# IO
#
import PBRTRendererIO

#
# Utility functions
#
def registMaterialNodeType(materialNodeType):
    PBRTRendererIO.materialNodeTypes.append(materialNodeType)

def createRenderSettingsNode():
    global renderSettings
    #print( "\n\n\n%s Render Settings - Create Node - Python\n\n\n" % (kPluginCmdName) )

    existingSettings = cmds.ls(type='PBRTRenderSettings')
    if existingSettings != []:
        # Just use the first one?
        renderSettings = existingSettings[0]
        print( "%s - Using existing PBRT settings node : %s" % (kPluginCmdName, renderSettings) )
    else:
        renderSettings = cmds.createNode('PBRTRenderSettings', name='defaultPBRTRenderGlobals', shared=True)
        print( "%s - Creating new PBRT settings node : %s" % (kPluginCmdName, renderSettings) )

def getRenderSettingsNode():
    global renderSettings
    return renderSettings

def updateRenderSettings():
    global renderSettings
    #print( "\n\n\%s Render Settings - Update - Python\n\n\n" % kPluginCmdName)

def getImageExtension(renderSettings):
    filmType = cmds.getAttr( "%s.film" % renderSettings )

    if filmType == 'Image Film':
        filmImageFileFormat = cmds.getAttr("%s.%s" % (renderSettings, "filmImageFileFormat"))

        mayaFileFormatUINameToExtension = {
            "OpenEXR (.exr)"  : "exr",
            "TGA (.tga)" : "tga",
            "Portable Float Map (.pfm)"  : "pfm"
        }

        if filmImageFileFormat in mayaFileFormatUINameToExtension:
            filmImageFileFormatExtension = mayaFileFormatUINameToExtension[filmImageFileFormat]
        else:
            filmImageFileFormatExtension = "exr"

        extension = filmImageFileFormatExtension
    else:
        extension = "exr"

    return extension

#
# UI
#
import PBRTRendererUI

#
# Renderer functions
#

# A command to render with Maya
class PBRTForMaya(OpenMayaMPx.MPxCommand):
    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)

    # Invoked when the command is run.
    def doIt(self,argList):
        global renderSettings
        print( "Rendering with %s..." % kPluginCmdName )

        # Create a render settings node
        createRenderSettingsNode()

        #Save the user's selection
        userSelection = cmds.ls(sl=True)
        
        print( "Render Settings - Node            : %s" % renderSettings )

        #Get the directories and other variables
        projectDir = cmds.workspace(q=True, fn=True)
        renderDir = os.path.join(projectDir, "renderData")
        pluginDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        version = cmds.about(v=True).replace(" ", "-")

        # Get render settings
        pbrtPath = cmds.getAttr("%s.%s" % (renderSettings, "PBRTPath"))
        oiiotoolPath = cmds.getAttr("%s.%s" % (renderSettings, "oiiotoolPath"))
        pbrtDir = os.path.split(pbrtPath)[0]
        integrator = cmds.getAttr("%s.%s" % (renderSettings, "integrator"))
        sampler = cmds.getAttr("%s.%s" % (renderSettings, "sampler"))
        pixelSamples = cmds.getAttr("%s.%s" % (renderSettings, "samplerPixelSamples"))
        reconstructionFilter = cmds.getAttr("%s.%s" % (renderSettings, "filter"))
        keepTempFiles = cmds.getAttr("%s.%s" % (renderSettings, "keepTempFiles"))
        verboseRender = cmds.getAttr("%s.%s" % (renderSettings, "verboseRender"))
        verboseExport = cmds.getAttr("%s.%s" % (renderSettings, "verboseExport"))
        exportOnly = cmds.getAttr("%s.%s" % (renderSettings, "exportOnly"))
        commandLineParameters = cmds.getAttr("%s.%s" % (renderSettings, "commandLineParameters"))

        print( "Render Settings - PBRT Path        : %s" % pbrtPath )
        print( "Render Settings - Integrator       : %s" % integrator )
        print( "Render Settings - Sampler          : %s" % sampler )
        print( "Render Settings - Pixel Samples    : %s" % pixelSamples )
        print( "Render Settings - Filter           : %s" % reconstructionFilter )
        print( "Render Settings - Render Dir       : %s" % renderDir )
        print( "Render Settings - oiiotool Path    : %s" % oiiotoolPath )
        print( "Render Settings - Verbose Render   : %s" % verboseRender )
        print( "Render Settings - Verbose Export   : %s" % verboseExport )
        print( "Render Settings - Export Only      : %s" % exportOnly )
        print( "Render Settings - Keep Temp Files  : %s" % keepTempFiles )
        print( "Render Settings - Cmd Line Params  : %s" % commandLineParameters )

        animation = self.isAnimation(exportOnly)
        print( "Render Settings - Animation        : %s" % animation )

        # Animation
        if animation:
            startFrame = int(cmds.getAttr("defaultRenderGlobals.startFrame"))
            endFrame = int(cmds.getAttr("defaultRenderGlobals.endFrame"))
            byFrame = int(cmds.getAttr("defaultRenderGlobals.byFrameStep"))
            print( "Animation frame range : %d to %d, step %d" % (
                startFrame, endFrame, byFrame) )

            for frame in range(startFrame, endFrame+1, byFrame):
                print( "Rendering frame " + str(frame) + " - begin" )

                self.exportAndRender(renderDir, renderSettings, pbrtPath, 
                    oiiotoolPath, pbrtDir, keepTempFiles, animation, 
                    frame, verboseRender, verboseExport, exportOnly,
                    commandLineParameters)

                print( "Rendering frame " + str(frame) + " - end" )

            print( "Animation finished" )

        # Single frame
        else:
            imageName = self.exportAndRender(renderDir, renderSettings, 
                pbrtPath, oiiotoolPath, pbrtDir, keepTempFiles, animation, 
                None, verboseRender, verboseExport, exportOnly,
                commandLineParameters)

            # Display the render
            if imageName and not cmds.about(batch=True):
                PBRTRendererUI.showRender(imageName)

        # Select the objects that the user had selected before they rendered, or clear the selection
        if len(userSelection) > 0:
            cmds.select(userSelection)
        else:
            cmds.select(cl=True)

    def isAnimation(self, exportOnly=False):
        animation = cmds.getAttr("defaultRenderGlobals.animation")
        if not cmds.about(batch=True) and animation and not exportOnly:
            print( "Animation isn't currently supported outside of Batch mode. Rendering current frame." )
            animation = False

        mayaReleasePythonGIL = os.environ.get('MAYA_RELEASE_PYTHON_GIL')
        mayaVersion = float(cmds.about(version=True))
        if mayaVersion >= 2016 and not mayaReleasePythonGIL:
            print( "\n\n\n\n")
            print( "For versions of Maya 2016 and greater, you must set the environment variable MAYA_RELEASE_PYTHON_GIL"
                " to 1 to render animations. Rendering current frame only." )
            print( "\n\n\n\n")
            animation = False

        return animation

    def resetImageDataWindow(self, imageName, oiiotoolPath):
        editor = cmds.renderWindowEditor(q=True, editorName=True )
        if editor:
            renderRegion = cmds.renderWindowEditor(editor, q=True, mq=True)
            if renderRegion:
                left = cmds.getAttr( "defaultRenderGlobals.left" )
                right = cmds.getAttr( "defaultRenderGlobals.rght" )
                top = cmds.getAttr( "defaultRenderGlobals.top" )
                bottom = cmds.getAttr( "defaultRenderGlobals.bot" )
            
                imageWidth = cmds.getAttr("defaultResolution.width")
                imageHeight = cmds.getAttr("defaultResolution.height")

                pathTokens = os.path.splitext(imageName)
                imageNameCropped = "%s_crop%s" % (pathTokens[0], pathTokens[1])

                oiiotoolResult = None
                try:
                    #print( "Generating cropped image : %s" % imageNameCropped )

                    #oiiotool picks up on the PBRT EXR's pixel data origin, so
                    #we don't have to do anything fancy here
                    cropArgs = '%dx%d-%d-%d' % (imageWidth, imageHeight, 0, 0)

                    args = ['-v', imageName, '--crop', cropArgs, '--noautocrop', '-o', imageNameCropped]
                    oiiotool = Process(description='reset image data window',
                        cmd=oiiotoolPath,
                        args=args)
                    oiiotool.execute()
                    oiiotoolResult = oiiotool.status
                    #print( "oiiotool result : %s" % oiiotoolResult )
                except:
                    print( "Unable to run oiiotool" )
                    oiiotoolResult = None

                # Move the image with the new data window over the original rendered image
                if oiiotoolResult in [0, None]:
                    # Useful for debugging
                    #imageNameOriginal = "%s_uncropped%s" % (pathTokens[0], pathTokens[1])
                    #os.rename(imageName, imageNameOriginal)

                    os.rename(imageNameCropped, imageName)

    def getScenePrefix(self):
        return str('.'.join(os.path.split(cmds.file(q=True, sn=True))[-1].split('.')[:-1]))

    def renderScene(self,
                    sceneFileName, 
                    renderDir, 
                    PBRTPath,
                    oiiotoolPath, 
                    pbrtDir, 
                    keepTempFiles, 
                    geometryFiles, 
                    animation=False, 
                    frame=1, 
                    verboseRender=0,
                    verboseExport=False,
                    renderSettings=None,
                    commandLineParameters=None):
        projectDir = cmds.workspace(q=True, fn=True)
        imageDir = os.path.join(projectDir, "images")
        os.chdir(imageDir)

        sceneName = self.getScenePrefix()

        imagePrefix = cmds.getAttr("defaultRenderGlobals.imageFilePrefix")
        if imagePrefix is None:
            imagePrefix = sceneName

        writePartialResults = False
        writePartialResultsInterval = -1
        blockSize = 32
        threads = 0
        extension = 'exr'
        if renderSettings:
            extension = getImageExtension(renderSettings)

            threads = cmds.getAttr("%s.%s" % (renderSettings, "threads"))
            if threads:
                print( "Render Settings - Threads          : %s" % threads )

            # pbrt version
            PBRTVersion = cmds.getAttr("%s.%s" % (renderSettings, "PBRTVersion"))
            print( "Render Settings - Version          : %s" % PBRTVersion )

        if animation:
            extensionPadding = cmds.getAttr("defaultRenderGlobals.extensionPadding")
            logName = os.path.join(imageDir, imagePrefix + "." + str(frame).zfill(extensionPadding) +".log")
            imageName = os.path.join(imageDir, imagePrefix + "." + str(frame).zfill(extensionPadding) + "." + extension)
        else:
            logName = os.path.join(imageDir, imagePrefix + ".log")
            imageName = os.path.join(imageDir, imagePrefix + "." + extension)

        imageNameLocal = os.path.relpath( imageName, imageDir )
        sceneFileNameLocal = os.path.relpath( sceneFileName, imageDir )

        args = []
        if verboseRender >= 0:
            if PBRTVersion == "v3 Book":
                if verboseRender == 0:
                    args.append('--quiet')
                else:
                    args.append('--verbose')
            else:
                if verboseRender == 0:
                    args.append('--quiet')
                elif verboseRender > 1:
                    args.extend(['--v', str(verboseRender-2), '--logtostderr'])

        if threads:
            args.extend(['--nthreads', str(threads)])

        if commandLineParameters:
            args.extend(commandLineParameters.split())

        args.extend([
            '--outfile',
            imageNameLocal,
            sceneFileNameLocal])

        if ' ' in pbrtDir:
            env = {"LD_LIBRARY_PATH":str("\"%s\"" % pbrtDir)}
        else:
            env = {"LD_LIBRARY_PATH":str(pbrtDir)}

        PBRTRender = Process(description='render an image',
            cmd=PBRTPath,
            args=args,
            env=env)

        #PBRTRender.echo = False
        PBRTRender.execute()
        PBRTRender.write_log_to_disk(logName, format='txt')

        print( "Render execution returned : %s" % PBRTRender.status )

        if oiiotoolPath != "":
            self.resetImageDataWindow(imageName, oiiotoolPath)

        if not keepTempFiles:
            #Delete all of the temp file we just made
            os.chdir(renderDir)
            for geometryFile in list(set(geometryFiles)):
                try:
                    print( "Removing geometry : %s" % geometryFile )
                    os.remove(geometryFile)
                except:
                    print( "Error removing temporary file : %s" % geometryFile )
            print( "Removing PBRT scene description : %s" % sceneFileName )
            os.remove(sceneFileName)
            print( "Removing PBRT render log        : %s" % logName )
            os.remove(logName)
        else:
            print( "Keeping temporary files" )

        return imageName

    def exportAndRender(self,
                        renderDir,
                        renderSettings,
                        PBRTPath,
                        oiiotoolPath,
                        pbrtDir, 
                        keepTempFiles,  
                        animation, 
                        frame=None, 
                        verboseRender=0,
                        verboseExport=False,
                        exportOnly=False,
                        commandLineParameters=None):

        if frame != None:
            # Calling this can lead to Maya 2016 locking up if you don't have 
            # the environment variable MAYA_RELEASE_PYTHON_GIL set
            # See Readme
            cmds.currentTime(float(frame))
        else:
            frame = 1

        sceneName = self.getScenePrefix()

        scenePrefix = cmds.getAttr("defaultRenderGlobals.imageFilePrefix")
        if scenePrefix is None:
            scenePrefix = sceneName

        if animation:
            extensionPadding = cmds.getAttr("defaultRenderGlobals.extensionPadding")
            sceneFileName = os.path.join(renderDir, "%s.%s.pbrt" % (scenePrefix, str(frame).zfill(extensionPadding)))
        else:
            sceneFileName = os.path.join(renderDir, "%s.pbrt" % scenePrefix)

        # Export scene and geometry
        geometryFiles = PBRTRendererIO.exportScene(sceneFileName, renderDir, 
            renderSettings, verboseExport)

        # Render scene, delete scene and geometry
        imageName = None
        if not exportOnly:
            imageName = self.renderScene(sceneFileName, renderDir, PBRTPath, oiiotoolPath,
                pbrtDir, keepTempFiles, geometryFiles, animation, frame, verboseRender,
                verboseExport, renderSettings, commandLineParameters)

        return imageName

def batchRenderProcedure(options):
    print("\n\n\n%s - batchRenderProcedure - options : %s\n\n\n" % (kPluginCmdName, str(options)))

def batchRenderOptionsProcedure():
    print("\n\n\n%s - batchRenderOptionsProcedure\n\n\n" % kPluginCmdName)

def batchRenderOptionsStringProcedure():
    print("\n\n\n%s - batchRenderOptionsStringProcedure\n\n\n" % kPluginCmdName)
    return ' -r %s' % kPluginCmdName

def cancelBatchRenderProcedure():
    print("\n\n\n%s cancelBatchRenderProcedure\n\n\n" % kPluginCmdName)
    cmds.batchRender()

def commandRenderProcedure(options):
    print("\n\n\n%s - commandRenderProcedure - options : %s\n\n\n" % (kPluginCmdName, str(options)))

    kwargs = {}
    try:
        cmds.PBRT(batch=True, **kwargs)
    except RuntimeError, err:
        print err

# Creator
def cmdCreator():
    return OpenMayaMPx.asMPxPtr( PBRTForMaya() )

# Register Renderer
def registerRenderer():
    cmds.renderer(kPluginCmdName, rendererUIName=kPluginCmdName)
    cmds.renderer(kPluginCmdName, edit=True, renderProcedure=kPluginCmdName)

    batchRenderProcedureMel = createMelPythonCallback("PBRTRenderer", "batchRenderProcedure", True)
    cmds.renderer(kPluginCmdName, edit=True, batchRenderProcedure=batchRenderProcedureMel)

    commandRenderProcedureMel = createMelPythonCallback("PBRTRenderer", "commandRenderProcedure", True)
    cmds.renderer(kPluginCmdName, edit=True, commandRenderProcedure=commandRenderProcedureMel)

    batchRenderOptionsProcedureMel = createMelPythonCallback("PBRTRenderer", "batchRenderOptionsProcedure")
    cmds.renderer(kPluginCmdName, edit=True, batchRenderOptionsProcedure=batchRenderOptionsProcedureMel)

    batchRenderOptionsStringProcedureMel = createMelPythonCallback("PBRTRenderer", "batchRenderOptionsStringProcedure")
    cmds.renderer(kPluginCmdName, edit=True, batchRenderOptionsStringProcedure=batchRenderOptionsStringProcedureMel)

    cancelBatchRenderProcedureMel = createMelPythonCallback("PBRTRenderer", "cancelBatchRenderProcedure")
    cmds.renderer(kPluginCmdName, edit=True, cancelBatchRenderProcedure=cancelBatchRenderProcedureMel)

    cmds.renderer(kPluginCmdName, edit=True, renderRegionProcedure="mayaRenderRegion" )

    cmds.renderer(kPluginCmdName, edit=True, addGlobalsTab=("Common", 
        "createMayaSoftwareCommonGlobalsTab", 
        "updateMayaSoftwareCommonGlobalsTab"))

    cmds.renderer(kPluginCmdName, edit=True, addGlobalsTab=("PBRT Common", 
        createMelPythonCallback("PBRTRendererUI", "createRenderSettings"),
        createMelPythonCallback("PBRTRenderer", "updateRenderSettings")))

    cmds.renderer(kPluginCmdName, edit=True, addGlobalsNode="defaultPBRTRenderGlobals" )

# Initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)

    # Load needed plugins
    neededPlugins = ["objExport", "OpenEXRLoader"]

    for neededPlugin in neededPlugins:
        try:
            if not cmds.pluginInfo( neededPlugin, query=True, loaded=True ):
                cmds.loadPlugin( neededPlugin )
            print( "%s - Loaded plugin       : %s" % (kPluginName, neededPlugin))
        except:
                sys.stderr.write( "Failed to load %s plugin\n" % neededPlugin)
                raise

    try:
        # Register PBRT Renderer
        mplugin.registerCommand( kPluginCmdName, cmdCreator )
    except:
        sys.stderr.write( "Failed to register command: %s\n" % kPluginCmdName )
        raise

    try:
        registerRenderer()
    except:
        sys.stderr.write( "Failed to register renderer: %s\n" % kPluginCmdName )
        raise

# Uninitialize the script plug-in
def uninitializePlugin(mobject):
    global materialNodeModules
    global generalNodeModules

    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        cmds.renderer("PBRT", edit=True, unregisterRenderer=True)
    except:
        sys.stderr.write( "Failed to deregister renderer: %s\n" % kPluginCmdName )

    try:
        mplugin.deregisterCommand( kPluginCmdName )
    except:
        sys.stderr.write( "Failed to deregister command: %s\n" % kPluginCmdName )

