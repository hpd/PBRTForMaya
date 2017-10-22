from pymel.core import *
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

class BaseTemplate(ui.AETemplate):
    def __init__(self, nodeName):
        ui.AETemplate.__init__(self,nodeName)
        self.beginLayout("params", collapse=0)
        self.buildBody(nodeName)
        self.endLayout()

    def addControl(self, control, label=None, **kwargs):
        ui.AETemplate.addControl(self, control, label=label, **kwargs)
    
    def beginLayout(self, name, collapse=True):
        ui.AETemplate.beginLayout(self, name, collapse=collapse)

class AEPBRTHeterogeneousMediumTemplate(BaseTemplate):
    def getFilePath(self, textFieldName, nodeName, attrName):
        startingDirectory = None
        existingPath = cmds.getAttr("%s.%s" % (nodeName, attrName) )
        if existingPath:
            (pathFolder, pathFile) = os.path.split( existingPath )
            startingDirectory = pathFolder

        path = cmds.fileDialog2(fileMode=1, fileFilter="*.pbrt", 
            startingDirectory=startingDirectory)
        if path not in [None, []]:
            strPath = str(path[0])
            cmds.textFieldButtonGrp(textFieldName, e=1, text=strPath)
            cmds.setAttr("%s.%s" % (nodeName, attrName), strPath, type="string")

    def changeTextFieldGroup(self, nodeName, attrName, value=None):
        attr = "%s.%s" % (nodeName, attrName)
        cmds.setAttr(attr, value, type="string")

    def newFileDialog(self, attr, label):
        #print( "ae template new file dialog : %s" % attr )
        (nodeName, attrName) = attr.split('.')
        value = cmds.getAttr( attr )
        #print( "\tvalue : %s" % value )
        self.densityFileCtrl = cmds.textFieldButtonGrp(label=label, text=value,
            buttonLabel="Open", buttonCommand="browseFiles")
        cmds.textFieldButtonGrp(self.densityFileCtrl, e=1, 
            buttonCommand=lambda: self.getFilePath(self.densityFileCtrl, nodeName, attrName),
            changeCommand=lambda (x): self.changeTextFieldGroup(nodeName, attrName, x) )

    def replaceFileDialog(self, attr, label):
        (nodeName, attrName) = attr.split('.')
        #print( "ae template replace : %s" % attr )
        existingValue = cmds.getAttr("%s.%s" % (nodeName, attrName) )
        #print( "\tvalue : %s" % existingValue )
        if attrName == 'densityfile':
            if existingValue is None:
                existingValue = ""
            #print( "\tsetting text field group : %s" % existingValue )

            cmds.textFieldButtonGrp( self.densityFileCtrl, e=1, label=label,
                text=existingValue,
                buttonLabel="Open", buttonCommand="browseFiles" )
            cmds.textFieldButtonGrp(self.densityFileCtrl, e=1, 
                buttonCommand=lambda: self.getFilePath(self.densityFileCtrl, nodeName, attrName),
                changeCommand=lambda (x): self.changeTextFieldGroup(nodeName, attrName, x) )

    def newDensityFileDialog(self, attr):
        self.newFileDialog(attr, "Density File")

    def replaceDensityFileDialog(self, attr):
        self.replaceFileDialog(attr, "Density File")

    def buildBody(self, nodeName):
        #print( "ae template build body : %s" % nodeName )
        #self.beginLayout("params", collapse=0)
        self.callCustom(self.newDensityFileDialog, self.replaceDensityFileDialog, "densityfile")
        self.addControl("preset", label="Preset")
        self.addControl("scale", label="Scale")
        self.addControl("g", label="g")
        self.addControl("sigma_a", label="Sigma_A")
        self.addControl("sigma_s", label="Sigma_S")
        self.addControl("boundingBoxLowerOverride", label="BB Lower Override")
        self.addControl("boundingBoxUpperOverride", label="BB Upper Override")
        #self.endLayout()

