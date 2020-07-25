import inspect
import os
import math
import sys
import timeit

import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaAnim as OpenMayaAnim

import numpy as np
import plyfile as ply

from mayautil import createMelPythonCallback

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

kPluginTranslatorTypeName = "ply"
kPluginTranslatorOptionsUIFunction = "exportOptions"
kPluginTranslatorDefaultOptions = "space=world;format=binary;verbose=false;triangulate=false;"

# Node definition
class plyTranslator(OpenMayaMPx.MPxFileTranslator):
    def __init__(self):
        OpenMayaMPx.MPxFileTranslator.__init__(self)
    def haveWriteMethod(self):
        return True
    def haveReadMethod(self):
        return True
    def filter(self):
        return "*.ply"
    def defaultExtension(self):
        return "ply"

    def writer( self, fileObject, optionString, accessMode ):
        #print( "options string : %s" % optionString )
        optionsList = map(lambda x: map(str, x.split('=')), optionString.split(';'))
        optionsList = [x for x in optionsList if len(x) == 2]
        options = {}
        for option in optionsList:
            options[option[0]] = option[1]

        #print( "options : %s" % options )

        if OpenMayaMPx.MPxFileTranslator.kExportAccessMode == accessMode:
            result = self.exportAll(fileObject, options)
        elif OpenMayaMPx.MPxFileTranslator.kExportActiveAccessMode == accessMode:
            result = self.exportSelection(fileObject, options)

    def reader( self, fileObject, optionString, accessMode ):
        #
        try:
            optionsList = map(lambda x: map(str, x.split('=')), optionString.split(';'))
            optionsList = [x for x in optionsList if len(x) == 2]
            options = {}
            for option in optionsList:
                options[option[0]] = option[1]

            fullName = fileObject.fullName()
            #print( "ply::reader - Reading %s" % fullName )
            #print( "ply::reader - Options %s" % optionString )
            #print( "ply::reader - Mode    %s" % accessMode )

            self.importPly(fullName, options)

            # Create Maya mesh data
        except:
            sys.stderr.write( "Failed to read file information\n")
            raise

    def importPly(self, plyPath, importOptions):
        verbose = False
        if importOptions:
            if 'verbose' in importOptions and importOptions['verbose'] == 'true':
                verbose=True

        plydata = ply.PlyData.read(str(plyPath))
        #if verbose:
        #    print( plydata )

        #
        # Process vertices
        #
        vertexElement = plydata['vertex']
        numVertices = vertexElement.count
        vertexAttributes = map(lambda x: x[0], vertexElement.dtype())

        if verbose:
            print( "Vertices : %d" % numVertices )
            print( "Vertex Attributes : %s" % vertexAttributes )

        vertexProperties = vertexElement.properties
        (x, y, z) = (vertexElement[t] for t in ('x', 'y', 'z'))

        vertices = OpenMaya.MFloatPointArray(numVertices)
        for i in range(numVertices):
            vertices.set(i, float(x[i]), float(y[i]), float(z[i]))

        vertexNormalsPresent = ('nx' in vertexAttributes and
            'ny' in vertexAttributes and
            'nz' in vertexAttributes )

        if vertexNormalsPresent:
            if verbose:
                print( "Vertex Normals present" )
            (nx, ny, nz) = (vertexElement[t] for t in ('nx', 'ny', 'nz'))
            vertexNormals = OpenMaya.MVectorArray()
            vertexNormalsIndices = OpenMaya.MIntArray()
            vertexNormalsIndices.setLength( numVertices )
            for i in range(numVertices):
                vertexNormals.append( OpenMaya.MVector( float(nx[i]), float(ny[i]), float(nz[i]) ) )
                vertexNormalsIndices.set(i, i)

        vertexUVsPresent = ('u' in vertexAttributes and
            'v' in vertexAttributes )
        if vertexUVsPresent:
            if verbose:
                print( "Vertex UVs present" )
            (u, v) = (vertexElement[t] for t in ('u', 'v'))
            uArray = OpenMaya.MFloatArray()
            uArray.setLength( numVertices )

            vArray = OpenMaya.MFloatArray()
            vArray.setLength( numVertices )

            for i in range(numVertices):
                uArray.set(float(u[i]), i)
                vArray.set(float(v[i]), i)

        vertexColorsPresent = ('r' in vertexAttributes and
            'g' in vertexAttributes and
            'b' in vertexAttributes )
        if vertexColorsPresent:
            if verbose:
                print( "Vertex Colors present" )
            (r, g, b) = (vertexElement[t] for t in ('r', 'g', 'b'))
            vertexColors = OpenMaya.MColorArray()
            vertexColorsIndices = OpenMaya.MIntArray()
            vertexColorsIndices.setLength( numVertices )
            for i in range(numVertices):
                vertexColors.append( OpenMaya.MColor( float(r[i]), float(g[i]), float(b[i]) ) )
                vertexColorsIndices.set(i, i)

        #
        # Process faces
        #
        faceElement = plydata['face']
        numFaces = faceElement.count
        faceAttributes = map(lambda x: x[0], faceElement.dtype())

        if verbose:
            print( "Faces : %d" % numFaces )
            print( "Face Attributes : %s" % faceAttributes )

        vertex_indices = faceElement['vertex_indices']

        faceCounts = OpenMaya.MIntArray()
        faceCounts.setLength( numFaces )
        faceIndicesCount = 0
        for i in range( numFaces ):
            indices = vertex_indices[i]
            faceCounts.set(int(len(indices)), i)
            faceIndicesCount += int(len(indices))

        faceIndicesArray  = OpenMaya.MIntArray()
        faceIndicesArray.setLength( faceIndicesCount )
        n = 0
        for i in range( numFaces ):
            indices = vertex_indices[i]
            for j in range(len(indices)):
                faceIndicesArray.set(int(indices[j]), int(n))
                n = n + 1

        faceNormalsPresent = ('nx' in faceAttributes and
            'ny' in faceAttributes and
            'nz' in faceAttributes )

        if faceNormalsPresent:
            if verbose:
                print( "Per Face Normals present" )
            (nx, ny, nz) = (faceElement[t] for t in ('nx', 'ny', 'nz'))
            faceNormals = OpenMaya.MVectorArray()
            faceNormalsIndices = OpenMaya.MIntArray()
            faceNormalsVertexIndices = OpenMaya.MIntArray()
            
            faceNormalsIndices.setLength( faceIndicesCount )
            faceNormalsVertexIndices.setLength( faceIndicesCount )
            n = 0
            for i in range(numFaces):
                indices = vertex_indices[i]
                for j in range(len(indices)):
                    faceNormals.append( OpenMaya.MVector( float(nx[i]), float(ny[i]), float(nz[i]) ) )
                    faceNormalsIndices.set(i, n)
                    faceNormalsVertexIndices.set(int(indices[j]), int(n))
                    n = n + 1

        normalsElement = None
        if 'normals' in plydata:
            normalsElement = plydata['normals']
        facePerVertexNormalsPresent = ('normals_indices' in faceAttributes) and normalsElement

        if facePerVertexNormalsPresent:
            if verbose:
                print( "Per Face Per Vertex Normals present" )

            (nx, ny, nz) = (normalsElement[t] for t in ('nx', 'ny', 'nz'))
            normals_indices = faceElement['normals_indices']

            faceNormals = OpenMaya.MVectorArray()
            faceNormalsIndices = OpenMaya.MIntArray()
            faceNormalsVertexIndices = OpenMaya.MIntArray()
            
            faceNormalsIndices.setLength( faceIndicesCount )
            faceNormalsVertexIndices.setLength( faceIndicesCount )
            n = 0
            for i in range(numFaces):
                indices = normals_indices[i]
                for j in range(len(indices)):
                    normalIndex = indices[j]
                    faceNormals.append( OpenMaya.MVector( float(nx[normalIndex]), float(ny[normalIndex]), float(nz[normalIndex]) ) )
                    faceNormalsIndices.set(i, n)
                    faceNormalsVertexIndices.set(int(normalIndex), int(n))
                    n = n + 1

                    #if verbose:
                    #    print( "Face %d : Vertex %d : Normal %3.3f, %3.3f, %3.3f" % (
                    #        i, j, float(nx[normalIndex]), float(ny[normalIndex]), float(nz[normalIndex])))

        uvElement = None
        if 'uvs' in plydata:
            uvElement = plydata['uvs']
        faceUVsPresent = ('uv_indices' in faceAttributes) and uvElement

        if faceUVsPresent:
            if verbose:
                print( "Per Face Per Vertex UVs present" )
            (u, v) = (uvElement[t] for t in ('u', 'v'))
            uv_indices = faceElement['uv_indices']
            
            uArray = OpenMaya.MFloatArray()
            uArray.setLength( len(u) )

            vArray = OpenMaya.MFloatArray()
            vArray.setLength( len(v) )

            for i in range(len(u)):
                uArray.set(float(u[i]), i)
                vArray.set(float(v[i]), i)

        colorsElement = None
        if 'colors' in plydata:
            colorsElement = plydata['colors']
        facePerVertexColorsPresent = ('colors_indices' in faceAttributes) and colorsElement

        if facePerVertexColorsPresent:
            if verbose:
                print( "Per Face Per Vertex Colors present" )

            (r, g, b) = (colorsElement[t] for t in ('r', 'g', 'b'))
            colors_indices = faceElement['colors_indices']

            faceColors = OpenMaya.MColorArray()
            faceColorsIndices = OpenMaya.MIntArray()
            faceColorsVertexIndices = OpenMaya.MIntArray()
            
            faceColorsIndices.setLength( faceIndicesCount )
            faceColorsVertexIndices.setLength( faceIndicesCount )
            n = 0
            for i in range(numFaces):
                indices = colors_indices[i]
                for j in range(len(indices)):
                    colorIndex = indices[j]
                    faceColors.append( OpenMaya.MColor( 
                        float(r[colorIndex]), 
                        float(g[colorIndex]), 
                        float(b[colorIndex]) ) )
                    faceColorsIndices.set(i, n)
                    faceColorsVertexIndices.set(int(colorIndex), int(n))
                    n = n + 1

        #
        # Build Maya mesh
        #
        outputMesh = OpenMaya.MObject()
        meshFS = OpenMaya.MFnMesh()
        newMesh = meshFS.create(numVertices, numFaces, vertices, faceCounts, 
            faceIndicesArray, outputMesh)

        if vertexNormalsPresent:    
            meshFS.setVertexNormals(vertexNormals, vertexNormalsIndices )

        if vertexColorsPresent:    
            meshFS.setVertexColors(vertexColors, vertexColorsIndices )

        if facePerVertexNormalsPresent:
            status = meshFS.setFaceVertexNormals(faceNormals, faceNormalsIndices, faceIndicesArray)

        if faceNormalsPresent:    
            status = meshFS.setFaceVertexNormals(faceNormals, faceNormalsIndices, faceIndicesArray)

        if facePerVertexColorsPresent:    
            meshFS.setFaceVertexColors(faceColors, faceColorsIndices, faceIndicesArray)

        if vertexUVsPresent:
            if verbose:
                print( "Vertex UVs present" )
            meshFS.setUVs(uArray, vArray)

            uvCounts = OpenMaya.MIntArray()
            uvCounts.setLength( numFaces )    
            uvIds = OpenMaya.MIntArray()
            uvIds.setLength( faceIndicesCount )
            
            uvCountsIndex = 0
            uvIndex = 0
            for i in range(numFaces):
                numPolygonVertices = meshFS.polygonVertexCount(i)
                uvCounts.set(numPolygonVertices, int(uvCountsIndex))
                uvCountsIndex = uvCountsIndex + 1
                
                if numPolygonVertices == 0:
                    continue
                
                indices = vertex_indices[i]
                for vertexIndex in range(numPolygonVertices):
                    uvIds.set(int(indices[vertexIndex]), int(uvIndex))
                    uvIndex = uvIndex + 1
            
            meshFS.assignUVs(uvCounts, uvIds)

        if faceUVsPresent:
            if verbose:
                print( "Face UVs present" )
            meshFS.setUVs(uArray, vArray)
            
            uvCounts = OpenMaya.MIntArray()
            uvCounts.setLength( numFaces )    
            uvIds = OpenMaya.MIntArray()
            uvIds.setLength( faceIndicesCount )
            
            uvCountsIndex = 0
            uvIndex = 0
            for i in range(numFaces):
                numPolygonVertices = meshFS.polygonVertexCount(i)
                uvCounts.set(numPolygonVertices, int(uvCountsIndex))
                uvCountsIndex = uvCountsIndex + 1
                
                if numPolygonVertices == 0:
                    continue
                
                indices = uv_indices[i]
                for vertexIndex in range(numPolygonVertices):
                    uvIds.set(int(indices[vertexIndex]), int(uvIndex))
                    uvIndex = uvIndex + 1
            
            meshFS.assignUVs(uvCounts, uvIds)

        meshFS.updateSurface()

        # Assign initial shading group
        initialSG = OpenMaya.MObject()
        slist = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getSelectionListByName( "initialShadingGroup", slist )
        slist.getDependNode( 0, initialSG )

        fnSG = OpenMaya.MFnSet( initialSG )
        if fnSG.restriction() == OpenMaya.MFnSet.kRenderableOnly:
            fnSG.addMember( newMesh )

    def exportAll(self, fileObject, exportOptions):
        #print( "ply::exportAll" )
        try:
            fullName = fileObject.fullName()
            self.exportAllToPath(str(fullName), 
                exportOptions=exportOptions)
        except:
            sys.stderr.write( "exportAll - Failed to write file information\n")
            raise

    # Useful to be able to pass in a path directly for debugging
    def exportAllToPath(self, exportPath, exportOptions):
        #print( "ply::exportAll" )
        try:
            self.traverseScene(str(exportPath), 
                exportOptions=exportOptions)
        except:
            sys.stderr.write( "exportAllToPath - Failed to write file information\n")
            raise

    def exportSelection(self, fileObject, exportOptions):
        #print( "ply::exportSelection" )
        try:
            exportPath = fileObject.fullName()
            self.exportSelectionToPath(exportPath, exportOptions)
        except:
            sys.stderr.write( "exportSelection - Failed to write file information\n")
            raise

    # Useful to be able to pass in a path directly for debugging
    def exportSelectionToPath(self, exportPath, exportOptions):
        #print( "ply::exportSelection" )
        try:
            slist = OpenMaya.MSelectionList()
            selPath = OpenMaya.MDagPath()
            componentObj = OpenMaya.MObject()

            OpenMaya.MGlobal.getActiveSelectionList( slist )
            useObjectForFilename = slist.length() > 1
            for i in range(slist.length()):
                slist.getDagPath(i,selPath,componentObj)
                dagPath = selPath.fullPathName()
                #print( "Selected : %s" % dagPath )

                self.traverseScene(str(exportPath), 
                    objectToExport=selPath,
                    useObjectForFilename=useObjectForFilename, 
                    exportOptions=exportOptions)
        except:
            sys.stderr.write( "exportSelectionToPath - Failed to write file information\n")
            raise

    def traverseScene(self, exportPath, 
        objectToExport=None, 
        useObjectForFilename=False,
        exportOptions=None):
        verbose = False
        if exportOptions:
            if 'verbose' in exportOptions and exportOptions['verbose'] == 'true':
                verbose=True

        #print( "exportPly::verbose : %s" % verbose )

        meshes = []
        if objectToExport:
            # reset iterator's root node to be the selected node.
            #status = dagIt.reset(startingObject.node(), 
            #                     OpenMaya.MItDag.kDepthFirst, 
            #                     OpenMaya.MFn.kInvalid )

            mFnDagNode = OpenMaya.MFnDagNode( objectToExport )
            dagPath = mFnDagNode.fullPathName()
            #print( "Export mesh for %s" % dagPath )
            meshes.append((objectToExport, mFnDagNode, dagPath))
        else:
            dagIt = OpenMaya.MItDag( OpenMaya.MItDag.kDepthFirst )

            while not dagIt.isDone():
                mFnDagNode = OpenMaya.MFnDagNode( dagIt.currentItem() )
                dagPath = mFnDagNode.fullPathName()

                mObject = dagIt.currentItem()        
                #if mObject.hasFn(OpenMaya.MFn.kTransform):
                #    mAnim = OpenMayaAnim.MAnimUtil()
                #    if mAnim.isAnimated(mObject):
                #        print( "isAnimated" )
            
                if mObject.hasFn(OpenMaya.MFn.kMesh):
                    meshes.append((mObject, mFnDagNode, dagPath))
            
                dagIt.next()
        
        for mesh in meshes:
            (mObject, mFnDagNode, dagPath) = mesh
            if verbose:
                print( "exportPly Mesh : %s" % dagPath )
            plyObject = self.exportPly(mObject, mFnDagNode, dagPath,
                exportOptions=exportOptions)

            exportFile = exportPath
            if useObjectForFilename or len(meshes) > 1:
                exportPathComponents = os.path.split(exportPath)
                exportDir = exportPathComponents[0]
                exportFile = dagPath.replace(':', '__').replace('|', '__')

                exportFile = (str(os.path.join(exportDir, exportFile)) + ".ply")

            if verbose:
                print( "Writing : %s" % exportFile )
            plyObject.write(exportFile)

    def exportPly(self, mObject, mFnDagNode, dagPath, exportOptions):
        verbose = False
        triangulate = False
        if exportOptions:
            if 'verbose' in exportOptions and exportOptions['verbose'] == 'true':
                verbose = True
            if 'triangulate' in exportOptions and exportOptions['triangulate'] == 'true':
                triangulate = True

        dagNode = OpenMaya.MDagPath()
        mFnDagNode.getPath( dagNode )
        dagNode.extendToShape()
        meshNode = OpenMaya.MFnMesh(dagNode)

        dagPath = dagNode.fullPathName()
        if verbose:
            print( "exportPly : %s" % dagPath )

        # Space to evaluate normals, point positions
        space = OpenMaya.MSpace.kWorld
        if exportOptions:
            if 'space' in exportOptions and exportOptions['space'] == 'object':
                if verbose:
                    print( "\tSpace               : %s" % "object space" )
                space = OpenMaya.MSpace.kObject
            else:
                if verbose:
                    print( "\tSpace               : %s" % "world space" )

        '''
        polygonSets = OpenMaya.MObjectArray()
        polygonComponents = OpenMaya.MObjectArray()
        isInstanced = dagNode.isInstanced()
        print( "\tInstanced           : %s" % isInstanced )
        if dagNode.isInstanced():
            instanceNum = dagNode.instanceNumber()
            print( "\tInstance Number     : %s" % instanceNum )

            meshNode.getConnectedSetsAndMembers(instanceNum, polygonSets, polygonComponents, True)
            print( "\tPolygon Sets        : %s" % polygonSets.length() )
            print( "\tPolygon Components  : %s" % polygonComponents.length() )
        '''
 
        # Get Vertices
        numVertices = meshNode.numVertices()
        if verbose:
            print( "\tVerts               : %d" % numVertices )

        points = OpenMaya.MPointArray()
        meshNode.getPoints( points, space )
        numPoints = points.length()
        if verbose:
            print( "\tPoints              : %d" % numPoints )

        # Get UVs
        us = OpenMaya.MFloatArray()
        vs = OpenMaya.MFloatArray()
        meshNode.getUVs(us, vs)
        numUVs = us.length()
        if verbose:
            print( "\tUVs                 : %d" % numUVs )

        # Get Normals
        normals = OpenMaya.MFloatVectorArray()
        meshNode.getNormals(normals, space)
        numNormals = normals.length()
        if verbose:
            print( "\tNorms               : %d" % numNormals )

        # Faces
        numFaces = meshNode.numPolygons()
        if verbose:
            print( "\tFaces               : %d" % numFaces )

        # Vertex Colors
        numColors = meshNode.numColors()

        vertexColors = None
        faceVertexColors = None
        if numColors > 0:
            vertexColors = OpenMaya.MColorArray()
            meshNode.getVertexColors(vertexColors)
            numVertexColors = vertexColors.length()
            if verbose:
                print( "\tVertex Colors       : %d" % numVertexColors )

                #for i in range(numVertexColors):
                #    print( "Color %d : %3.3f, %3.3f, %3.3f" % (
                #        i, vertexColors[i].r, vertexColors[i].g, vertexColors[i].b))

            faceVertexColors = OpenMaya.MColorArray()
            meshNode.getFaceVertexColors(faceVertexColors)
            numFaceVertexColors = faceVertexColors.length()
            if verbose:
                print( "\tFace Vert Colors    : %d" % numFaceVertexColors )

                #for i in range(numFaceVertexColors):
                #    print( "Color %d : %3.3f, %3.3f, %3.3f" % (
                #        i, faceVertexColors[i].r, faceVertexColors[i].g, faceVertexColors[i].b))

        # Per-Face data
        itMeshPoly = OpenMaya.MItMeshPolygon( mObject )

        # Check for triangulation
        hasValidTriangulation = itMeshPoly.hasValidTriangulation()
        if verbose:
            print( "\tHas Triangulation   : %s" % hasValidTriangulation )
        if hasValidTriangulation:
            triangleCount = OpenMaya.MIntArray()
            triangleIndices = OpenMaya.MIntArray()
            meshNode.getTriangles(triangleCount, triangleIndices)
        else:
            if triangulate:
                OpenMaya.MGlobal.displayWarning( "Shape %s has invalid triangulation, skipping" % dagPath )
                return None

        if verbose:
            t0 = timeit.default_timer()

        if triangulate and hasValidTriangulation:
            plyData = self.exportTriangulatedMesh(mObject, dagPath, meshNode, points, 
                us, vs, normals, faceVertexColors, triangleCount, triangleIndices, 
                exportOptions, verbose)
        else:
            plyData = self.exportMesh(mObject, dagPath, meshNode, points, us, vs, 
                normals, faceVertexColors, exportOptions, verbose)

        if verbose:
            t1 = timeit.default_timer()
            elapsed = (t1 - t0)
            print( "export elapsed : %s" % elapsed )

        return plyData

    def exportTriangulatedMesh(self, mObject, dagPath, meshNode, points, 
        us, vs, normals, faceVertexColors, triangleCount, triangleIndices,
        exportOptions, verbose=False):

        if verbose:
            print( "\texportTriangulatedMesh")

        # object-relative vert indices in a face
        polygonVertices = OpenMaya.MIntArray()
        
        # face triangle vert points
        vertPoints = OpenMaya.MPointArray()
                    
        # face triangle vert indices
        vertIndices = OpenMaya.MIntArray()

        # vertex and uv index pointers
        uvIdxPx = OpenMaya.MScriptUtil()
        uvIdxPx.createFromInt(0)
        uvIdxPtr = uvIdxPx.asIntPtr()

        colorIdxPx = OpenMaya.MScriptUtil()
        colorIdxPx.createFromInt(0)
        colorIdxPtr = colorIdxPx.asIntPtr()

        faceIndex = 0
        triangleIndex = 0
        triangleVertexIndex = 0
        totalTriangleVertices = 0

        totalTriangles = 0
        for i in range(triangleCount.length()):
            totalTriangles = totalTriangles + triangleCount[i]

        if verbose:
            print( "\t\ttotal triangles : %d" % totalTriangles )
            #print( "max total verts : %d" % len(triangulatedVertIndices) )

        # Pre-allocating
        triangulatedFaceIndices = [ ([0]*3) for i in range(totalTriangles) ]

        # Keys will be indices of points, normals, uvs and colors.
        # Values will be the index into the resulting vertex list
        triangulatedVertIndices = {}

        if verbose:
            t0 = timeit.default_timer()

        itMeshPoly = OpenMaya.MItMeshPolygon( mObject )

        # properties
        hasUVs = itMeshPoly.hasUVs()
        hasNormals = normals and normals.length() > 0
        hasColors = faceVertexColors and faceVertexColors.length() > 0

        # Step through each face
        while not itMeshPoly.isDone():
            currentFace = itMeshPoly.currentItem()
            numTriangles = triangleCount[faceIndex]

            #if verbose:
            #    print( "\t\tFace %03d, Triangles : %02d" % (faceIndex, numTriangles))

            itMeshPoly.getVertices( polygonVertices )

            # Step through each face triangle
            for currentTriangle in range(numTriangles):
                triangleVertexIndices = triangleIndices[triangleVertexIndex:(triangleVertexIndex+3)]
                #if verbose:
                #    print( "\t\tFace %03d, Triangle  : %02d, Indices : %s" % (
                #        faceIndex, currentTriangle, triangleVertexIndices))

                # get the triangle points and indices
                itMeshPoly.getTriangle( currentTriangle, vertPoints, vertIndices, OpenMaya.MSpace.kObject )

                # get a list of local indices
                localIndex = self.getLocalIndex( polygonVertices, vertIndices )

                # each vert in this triangle
                for i, vertIndex in enumerate( vertIndices ):
                    # get index to points/normals/uvs

                    # normal
                    vertNormalIndex = -1
                    if hasNormals:
                        vertNormalIndex = itMeshPoly.normalIndex( localIndex[i] )

                    # uv
                    vertUVIndex = -1
                    if hasUVs:
                        itMeshPoly.getUVIndex( localIndex[i], uvIdxPtr )
                        vertUVIndex = OpenMaya.MScriptUtil( uvIdxPtr ).asInt()

                    # color
                    vertColorIndex = -1
                    if hasColors:
                        itMeshPoly.getColorIndex( localIndex[i], colorIdxPtr )
                        vertColorIndex = OpenMaya.MScriptUtil( colorIdxPtr ).asInt()

                    indices = (vertIndices[i], vertNormalIndex, vertUVIndex, vertColorIndex)

                    # Check to see if combination of indices has already been added to the list
                    if indices in triangulatedVertIndices:
                        triangulatedVertIndex = triangulatedVertIndices[indices]
                    else:
                        triangulatedVertIndex = totalTriangleVertices
                        triangulatedVertIndices[indices] = totalTriangleVertices
                        totalTriangleVertices = totalTriangleVertices + 1

                    #if verbose:
                    #    print( "\t\t\t\tTriangle %d, Vert %d, Indices %s" % (triangleIndex, i, triangulatedVertIndex) )
                    triangulatedFaceIndices[triangleIndex][i] = triangulatedVertIndex 

                triangleVertexIndex = triangleVertexIndex + 3
                triangleIndex = triangleIndex + 1

            faceIndex = faceIndex + 1
            itMeshPoly.next()

        if verbose:
            t1 = timeit.default_timer()
            elapsed = (t1 - t0)
            print( "\t\tgather points, tri indices elapsed : %s" % elapsed )

        if verbose:
            t0 = timeit.default_timer()

        # PLY Vertex type
        vertexDType = [('x', 'f4'), ('y', 'f4'), ('z', 'f4')]
        if hasUVs:
            if verbose:
                print( "\tVertices have UVs")
            vertexDType.extend([('u', 'f4'), ('v', 'f4')])
        if hasNormals:
            if verbose:
                print( "\tVertices have Normals")
            vertexDType.extend([('nx', 'f4'), ('ny', 'f4'), ('nz', 'f4')])
        if hasColors:
            if verbose:
                print( "\tVertices have Colors")
            vertexDType.extend([('r', 'f4'), ('g', 'f4'), ('b', 'f4')])

        #vertices = np.zeros(len(triangulatedVertIndices), dtype=vertexDType)
        vertices = np.zeros(totalTriangleVertices, dtype=vertexDType)

        # Copy data to PLY vertex list
        #for i, indices in enumerate(triangulatedVertIndices):
        #for i in range(totalTriangleVertices):
        for indices, i in triangulatedVertIndices.iteritems():
            #indices = triangulatedVertIndices[i]
            vertIndex = indices[0]
            vertex = (points[vertIndex].x, points[vertIndex].y, points[vertIndex].z)

            if hasUVs:
                vertUVIndex = indices[2]
                vertex = vertex + (us[vertUVIndex], vs[vertUVIndex])

            if hasNormals:
                vertNormalIndex = indices[1]
                vertex = vertex + (normals[vertNormalIndex].x, normals[vertNormalIndex].y, normals[vertNormalIndex].z)

            if hasColors:
                vertColorIndex = indices[1]
                vertex = vertex + (faceVertexColors[vertColorIndex].r, 
                    faceVertexColors[vertColorIndex].g, 
                    faceVertexColors[vertColorIndex].b)

            vertices[i] = vertex

        # Create face data

        # Using 'object' instead of something like 
        # ('vertex_indices', 'i4', (maxVertices,))
        # allows for faces with varying numbers of vertices
        faceDtype = []
        faceDtype.append( ('vertex_indices', object) )
        faces = np.zeros(len(triangulatedFaceIndices), dtype=faceDtype)

        for i, faceIndices in enumerate(triangulatedFaceIndices):
            faceEntryIndex = 0
            faces[i][faceEntryIndex] = faceIndices

        if verbose:
            t1 = timeit.default_timer()
            elapsed = (t1 - t0)
            print( "\t\tbuild lists of points, tri elapsed : %s" % elapsed )

        if verbose:
            t0 = timeit.default_timer()

        # Build PLY data structures
        text = False
        byte_order = '='
        if exportOptions:
            if 'format' in exportOptions and exportOptions['format'] == 'text':
                text = True

        plyElements = [
                ply.PlyElement.describe(vertices, 'vertex'),
                ply.PlyElement.describe(faces, 'face')
        ]

        plyData = ply.PlyData(plyElements,
            text=text, 
            byte_order=byte_order,
            comments=[dagPath])
            
        if verbose:
            t1 = timeit.default_timer()
            elapsed = (t1 - t0)
            print( "\t\tbuild ply structures elapsed : %s" % elapsed )

        return plyData

    # converts vertex indices from object-relative to face-relative.
    def getLocalIndex(self, getVertices, getTriangle):        
        localIndex = []
        
        for gt in range(0, getTriangle.length()):
            for gv in range(0, getVertices.length()):
                if getTriangle[gt] == getVertices[gv]:
                    localIndex.append( gv )
                    break
                    
            if len(localIndex) == gt:
                localIndex.append( -1 )
                
        return localIndex

    def exportMesh(self, mObject, dagPath, meshNode, points, us, vs, normals, 
        faceVertexColors, exportOptions, verbose=False):

        if verbose:
            print( "\texportMesh")

        itMeshPoly = OpenMaya.MItMeshPolygon( mObject )
        numPerFaceVertices = 0
        while not itMeshPoly.isDone():
            currentFace = itMeshPoly.currentItem()

            numFaceVertices = itMeshPoly.polygonVertexCount()
            numPerFaceVertices = numPerFaceVertices + numFaceVertices

            itMeshPoly.next()

        if verbose:
            print( "\tPer Faces Vertices  : %d" % numPerFaceVertices )

        numPoints = points.length()
        numNormals = normals.length()
        numFaces = meshNode.numPolygons()
        numUVs = us.length()

        hasColors = faceVertexColors and faceVertexColors.length() > 0

        if (numPerFaceVertices == numNormals):
            perFacePerVertexNormals = True
            mergeNormalsWithFaces = False
            mergeNormalsWithVertices = False
        elif (numFaces == numNormals):
            perFacePerVertexNormals = False
            mergeNormalsWithFaces = True
            mergeNormalsWithVertices = False
        elif (numNormals == numPoints):
            perFacePerVertexNormals = False
            mergeNormalsWithFaces = False
            mergeNormalsWithVertices = True

        mergeUVsWithVertices = (numUVs == numPoints)

        # PLY Vertex type
        vertexDType = [('x', 'f4'), ('y', 'f4'), ('z', 'f4')]
        if mergeUVsWithVertices:
            if verbose:
                print( "\tVertices have UVs")
            vertexDType.extend([('u', 'f4'), ('v', 'f4')])
        if mergeNormalsWithVertices:
            if verbose:
                print( "\tVertices have Normals")
            vertexDType.extend([('nx', 'f4'), ('ny', 'f4'), ('nz', 'f4')])

        vertices = np.zeros(numPoints, dtype=vertexDType)

        # Copy data to PLY vertex list
        for i in range(numPoints):
            vertex = (points[i].x, points[i].y, points[i].z)
            if mergeUVsWithVertices:
                vertex = vertex + (us[i], vs[i])
            if mergeNormalsWithVertices:
                vertex = vertex + (normals[i].x, normals[i].y, normals[i].z)
            vertices[i] = vertex

        # Copy data to PLY UV list, if necessary
        if not mergeUVsWithVertices:
            if verbose:
                print( "\tUVs listed independently")
            uvs = np.zeros(numUVs, dtype=[('u', 'f4'), ('v', 'f4')])
            for i in range(us.length()):
                #print( "UV %d : %s, %s" % (i, us[i], vs[i]))
                uvs[i] = (us[i], vs[i])

        # Copy data to PLY Normals list, if necessary
        if perFacePerVertexNormals:
            if verbose:
                print( "\tNormals listed independently")
            normalsNP = np.zeros(numNormals, dtype=[('nx', 'f4'), ('ny', 'f4'), ('nz', 'f4')])
            for i in range(normals.length()):
                #print( "Normals %d : %s %s %s" % (i, 
                #    normals[i].x, normals[i].y, normals[i].z))
                normalsNP[i] = (normals[i].x, normals[i].y, normals[i].z)

        if hasColors:
            if verbose:
                print( "\tColors listed independently")
            colorsNP = np.zeros(faceVertexColors.length(), 
                dtype=[('r', 'f4'), ('g', 'f4'), ('b', 'f4')])

            # Use this later
            faceColorDict = {}
            faceColorCount = 0

            for i in range(faceVertexColors.length()):
                #if verbose:
                #    print( "Colors %d : %s %s %s" % (i, 
                #        faceVertexColors[i].r, faceVertexColors[i].g, faceVertexColors[i].b))
                color = (faceVertexColors[i].r, faceVertexColors[i].g, faceVertexColors[i].b)
                colorsNP[i] = color
                faceColorDict[color] = i

        # Create face data
        rawFaces = []
        rawFaceUVs = []
        rawFaceNormals = []
        rawFaceNormalValues = []
        rawFaceColors = []

        colorIdxPx = OpenMaya.MScriptUtil()
        colorIdxPx.createFromInt(0)
        colorIdxPtr = colorIdxPx.asIntPtr()

        # object-relative vert indices in a face
        polygonVertices = OpenMaya.MIntArray()

        itMeshPoly = OpenMaya.MItMeshPolygon( mObject )
        while not itMeshPoly.isDone():
            currentFace = itMeshPoly.currentItem()
            numFaceVertices = itMeshPoly.polygonVertexCount()

            faceVertices = []
            faceVertexUVIndices = []
            faceVertexNormalIndices = []
            faceNormal = ()
            faceVertexColorIndices = []

            # Step through 'local' vertex indices
            # vertexIndex, getUVIndex, normalIndex and getColorIndex expect 
            # local vertex indices 
            for v in range(numFaceVertices):
                vertIndex = itMeshPoly.vertexIndex(v)
                faceVertices.append( vertIndex )

                if not mergeUVsWithVertices and us.length() > 0:
                    util = OpenMaya.MScriptUtil()
                    util.createFromInt(0)
                    uv_pInt = util.asIntPtr()
                    uv_index = OpenMaya.MScriptUtil()
                    uv_index.createFromInt(0)
                    itMeshPoly.getUVIndex(v, uv_pInt)
                    vertexUVIndex = uv_index.getInt(uv_pInt)
                    faceVertexUVIndices.append( vertexUVIndex )

                if not mergeNormalsWithVertices and normals.length() > 0:
                    vertexNormalIndex = itMeshPoly.normalIndex(v)
                    if perFacePerVertexNormals:
                        faceVertexNormalIndices.append( vertexNormalIndex )                        
                    else:
                        faceNormal = (normals[vertexNormalIndex].x, 
                            normals[vertexNormalIndex].y, 
                            normals[vertexNormalIndex].z)

                if hasColors:
                    itMeshPoly.getColorIndex( v, colorIdxPtr )

                    # Going to override this as the values seem to be off
                    vertColorIndex = OpenMaya.MScriptUtil( colorIdxPtr ).asInt()

                    vertColorIndex0 = vertColorIndex

                    color = OpenMaya.MColor()
                    itMeshPoly.getColor( color, v )
                    colorTuple = (color.r, color.g, color.b)
                    if colorTuple in faceColorDict:
                        vertColorIndex = faceColorDict[colorTuple]

                    faceVertexColorIndices.append( vertColorIndex )

            rawFaces.append( faceVertices )
            rawFaceUVs.append( faceVertexUVIndices )
            rawFaceNormals.append( faceVertexNormalIndices )
            rawFaceColors.append( faceVertexColorIndices )
            rawFaceNormalValues.append( faceNormal )
            
            #if verbose:
            #    print( "Face %d Vertices : %s" % (i, faceVertices) )
            #    print( "Face %d UVs      : %s" % (i, faceVertexUVIndices) )
            #    print( "Face %d Normals  : %s" % (i, faceVertexNormalIndices) )
            #    print( "Face %d Normal   : %s" % (i, faceNormal) )
            #    print( "Face %d Colors   : %s" % (i, faceVertexColorIndices) )
            itMeshPoly.next()

        # Using 'object' instead of something like 
        # ('vertex_indices', 'i4', (maxVertices,))
        # allows for faces with varying numbers of vertices
        dtype = []
        dtype.append( ('vertex_indices', object) )
        if not mergeUVsWithVertices:
            if verbose:
                print( "\tFaces have Per-Vertex UVs")
            dtype.append(('uv_indices', object))
        if mergeNormalsWithFaces:
            if verbose:
                print( "\tFaces have single Normals")
            dtype.extend([('nx', 'f4'), ('ny', 'f4'), ('nz', 'f4')])
        elif perFacePerVertexNormals:
            if verbose:
                print( "\tFaces have Per-Vertex Normals")
            dtype.append(('normals_indices', object))
        if hasColors:
            if verbose:
                print( "\tFaces have Per-Vertex Colors")
            dtype.append(('colors_indices', object))

        #print( "Face D Type : %s" % str(dtype) )

        faces = np.zeros(numFaces, dtype=dtype)
        for i in range(numFaces):
            #print( "Face %d" % i )
            faceEntryIndex = 0
            faces[i][faceEntryIndex] = rawFaces[i]
            faceEntryIndex = faceEntryIndex + 1

            if not mergeUVsWithVertices:
                faces[i][faceEntryIndex] = rawFaceUVs[i]
                faceEntryIndex = faceEntryIndex + 1

            if mergeNormalsWithFaces:
                #print( "Normal : %3.3f, %3.3f, %3.3f" % (rawFaceNormalValues[i][0],
                #    rawFaceNormalValues[i][1], rawFaceNormalValues[i][2]) )
                faces[i][faceEntryIndex+0] = float(rawFaceNormalValues[i][0])
                faces[i][faceEntryIndex+1] = float(rawFaceNormalValues[i][1])
                faces[i][faceEntryIndex+2] = float(rawFaceNormalValues[i][2])
                faceEntryIndex = faceEntryIndex + 3
            elif perFacePerVertexNormals:
                faces[i][2] = rawFaceNormals[i]
                faceEntryIndex = faceEntryIndex + 1

            if hasColors:
                faces[i][faceEntryIndex] = rawFaceColors[i]
                faceEntryIndex = faceEntryIndex + 1

        # Build PLY data structures
        text = False
        byte_order = '='
        if exportOptions:
            if 'format' in exportOptions and exportOptions['format'] == 'text':
                text = True

        plyElements = [
                ply.PlyElement.describe(vertices, 'vertex'),
                ply.PlyElement.describe(faces, 'face')
        ]
        if not mergeUVsWithVertices:
            plyElements.insert(-1, ply.PlyElement.describe(uvs, 'uvs') )
        if perFacePerVertexNormals:
            plyElements.insert(-1, ply.PlyElement.describe(normalsNP, 'normals') )

        if hasColors:
            plyElements.insert(-1, ply.PlyElement.describe(colorsNP, 'colors') )

        plyData = ply.PlyData(plyElements,
            text=text, 
            byte_order=byte_order,
            comments=[dagPath])
            
        return plyData

# creator
def translatorCreator():
    return OpenMayaMPx.asMPxPtr( plyTranslator() )

# options
def exportOptions(parent='', action='', initialSettings='', resultCallback=''):    
    import maya.cmds as cmds
    import maya.mel as mel

    #print( 'parent  : %s' % parent )
    #print( 'action  : %s' % action )
    #print( 'initial : %s' % initialSettings )
    #print( 'resultCallback : %s' % resultCallback )

    retval = 0
    currentOptions = ''
        
    if action == 'post':
        #print( "post" )
        cmds.setParent(parent)
        cmds.columnLayout()

        # 'format' - text or binary
        formatMenu = cmds.optionMenuGrp('pexp_format', label="Format", 
            columnWidth=(1, 100))
        cmds.menuItem('Text')
        cmds.menuItem('Binary')
     
        # 'space' - world or object
        spaceMenu = cmds.optionMenuGrp('pexp_space', label="Coordinate Space", 
            columnWidth=(1, 100))
        cmds.menuItem('World')
        cmds.menuItem('Object')

        triangulatedCheckBox = cmds.checkBoxGrp('pexp_triangulate', label1="Triangulate Geometry", value1=False,
            columnWidth=(1, 100))

        verboseCheckBox = cmds.checkBoxGrp('pexp_verbose', label1="Verbose", value1=False,
            columnWidth=(1, 100))

        settings = initialSettings.split(';')
        for setting in settings:
            tokens = setting.split("=")
            if tokens[0] == 'format':
                cmds.optionMenuGrp('pexp_format', edit=True, value=tokens[1].capitalize())
            elif tokens[0] == 'space':
                cmds.optionMenuGrp('pexp_space', edit=True, value=tokens[1].capitalize())
            elif tokens[0] == 'verbose':
                cmds.checkBoxGrp('pexp_verbose', edit=True, value1=(tokens[1] == "true"))
            elif tokens[0] == 'triangulate':
                cmds.checkBoxGrp('pexp_triangulate', edit=True, value1=(tokens[1] == "true"))

        cmds.setParent( '..' )
        cmds.setParent( '..' )

        retval = 1

    elif action == 'query':
        #print( "query" )
        plyFormat = cmds.optionMenuGrp('pexp_format', query=True, value=True)
        plySpace = cmds.optionMenuGrp('pexp_space', query=True, value=True)
        plyVerbose = cmds.checkBoxGrp('pexp_verbose', query=True, value1=True)
        plyTriangulate = cmds.checkBoxGrp('pexp_triangulate', query=True, value1=True)

        currentOptions = "%s=%s;%s=%s;%s=%s;%s=%s;" % (
            "format", plyFormat.lower(), 
            "space", plySpace.lower(), 
            "verbose", ("true" if plyVerbose else "false"),
            "triangulate", ("true" if plyTriangulate else "false") )
        #print( "ply::export - current options : %s" % currentOptions )

        mel.eval(resultCallback+'("'+currentOptions+'")')
        retval = 1
    elif action == 'fileselected':
        #print( "fileselected" )
        retval = 0
    else:
        #print( "neither" )
        retval = 0

    return retval

# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        plyOptions = createMelPythonCallback("ply", "exportOptions",
            parametersList=[('string', 'parent'), 
                ('string', 'action'), 
                ('string', 'initialSettings'), 
                ('string', 'resultCallback')],
            returnType="int")

        mplugin.registerFileTranslator( kPluginTranslatorTypeName, 
            None, 
            translatorCreator,
            plyOptions,
            kPluginTranslatorDefaultOptions )
    except:
        sys.stderr.write( "Failed to register translator: %s" % kPluginTranslatorTypeName )
        raise

# uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterFileTranslator( kPluginTranslatorTypeName )
    except:
        sys.stderr.write( "Failed to deregister translator: %s" % kPluginTranslatorTypeName )
        raise
    
