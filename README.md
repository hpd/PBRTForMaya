PBRTForMaya
=

A [Maya](http://www.autodesk.com/products/maya) plugin for the [PBRT v3](http://www.pbrt.org/) renderer.


Supported Features
-

**Renderer**: PBRT v3 from the 'book' or 'master' branch.

**Materials**: Fourier, Glass, Hair, KD Subsurface, Matte, Metal, Mirror, Mix, Plastic, Substrate, Subsurface, Translucent, Uber, Disney

**Lights / Emitters**: Point, Spot, Directional, Object Area Light, Infinite (IBL), Goniometric

**Textures**: Mix, Scale and File with UV offset and scale, Constant, FBM, Marble, UV, Windy, Wrinkled

**Participating Media Models**: Homogeneous and Heterogeneous, with and without surface geometry, attached to specific geometry or global

**Cameras**: Perspective, Orthographic, Realistic Perspective, Environment (Spherical).

**Integrators**: Path Tracer, Bidirectional Path Tracer, Direct Lighting, Metropolis Light Transport, Stochastic Progressive Photon Map, Volumetric Path Tracer, Whitted Path Tracer

**Accelerator** : KD Tree, BVH

**Samplers** : Halton, Max Min, Random, Sobol, Stratified, Low Discrepancy (Zero Two)

**Films / Output Drivers** : OpenEXR (.exr), TGA (.tga), Portable Float Map (.pfm)

**Miscellaneous** : Motion Blur, color parameter specification as Black Body, XYZ or xyY

Notes
-

Render settings default to faster renderers. Adjusting the Sampler 'Pixel Samples' control will drive render quality and time.

Rendering isn't interactive. Once you start the render, you'll have to wait for it to finish to see the full frame's results. PBRT doesn't write out intermediate results or individual tiles.

For PBRT materials, volumes and lights, check the Hypershade under Maya/Surface, Maya/Volumetric, Maya/Lights and Maya/Utilities.

PBRT supports textures in the following formats: EXR, TGA, PNG and PFM. Ptex is supported if using a build from the master branch. If Maya's texture colorspace controls is set to 'sRGB', PBRT's gamma boolean will be set True. Otherwise, gamma will be set False, assuming that the texture contains linear data.

There is no default lighting in PBRT. You'll need to set up a lighting environment. Maya point, spot and directional lights can be created as normal. To treat an object as an area light, assign the PBRTDiffuseAreaLight shader as the Material for the object. PBRT Infinite (IBL) lights should be created in the Hypershade. Goniometric and Projector lights are created with specific configurations of the Maya spot light. See the example scenes for usage.

To set up participating media / volumetric scattering, assign one of the Participating Media models to a Material's Shading Group's 'Volume Material' slot. Be sure to use the Volumetric Path Tracer Integrator when rendering with Participating Media.

For Heterogeneous media, there are a number of constraints on the the scene:

	- The .pbrt file containing the density grid has an embedded name. The Maya PBRTHeterogeneousMedium node's name must match this embedded name. In the example file, "smoke" is the name of the volumetric node in the Maya scene as well as the name embedded in the .pbrt file. A modification to PBRT to takea file of density values would be even better.

	- A script for exporting density grids into this format is needed. The example grid is copied from the pbrt-v3-scenes archive.

	- The transforms on the geometry that has the heterogeneous medium assigned don't affect the density grid. Use the 'Bounding Box Lower Override' and 'Bounding Box Upper Override' attributes to place the medium. In the example scenes, the enclosing volume's bounding box min and max are connected to these attributes.

	- PBRT seems to be finicky about rendering heterogenous medium elements. Getting the error "Fatal Error: HaltonSampler can only sample 1000 dimensions" is not uncommon when rendering a medium without a surface material that is large in screen space.

To create global homogeneous media, create a nurbs object, name it 'globalVolume' and assign a PBRTHomogeneousMedium shader.

Usage
-

- Load the plugin using Python command
	- cmds.loadPlugin( "/path/where/you/downloaded/PBRTForMaya.py" )

- Unload the plugin using Python command
	- cmds.unloadPlugin( "PBRTForMaya" )

- ***VERY IMPORTANT*** 
- The first field in the Render Settings 'PBRT Common' tab is the path to the 'pbrt' binary. You must set this to be able to render. The setting can be specified using the PBRT_PATH environment variable, as described below, or manually from the Render Settings UI. The path will be retained in a file's Render Settings so the value only has to be specified the first time you set up a scene.

	- OSX: ex. /usr/local/bin/pbrt

	- Linux: ex. /usr/local/bin/pbrt

	- Windows: ex. C:/path/where/you/compiled/pbrt.exe

- The second field in the Render Settings 'PBRT Common' tab is the path to the 'oiiotool' binary. This setting is optional for general rendering use, but must be set to be able to use Maya's render region functionality. The setting can be specified using the OIIOTOOL_PATH environment variable, as described below, or manually from the Render Settings UI. The path will be retained in a file's Render Settings so the value only has to be specified the first time you set up a scene.

- Geometry export can go through the OBJ format or the [PLY polygonal geometry format](http://paulbourke.net/dataformats/ply/). PLY export depends on the [plyfile](https://pypi.python.org/pypi/plyfile) Python package. 

	- Use 'pip' to install the plyfile Python package with the following command:

		- pip install plyfile


Installation and Application Environment
- 

The path to the PBRT binary has to be specified, either in the Render Settings manually or by using the Maya.env or other environment setup file.

- To set the value in the Maya.env or in your shell environment, set the PBRT_PATH environment variable to  

	- OSX: ex. PBRT_PATH = /usr/local/bin/pbrt

	- Linux: ex. PBRT_PATH = /usr/local/bin/pbrt

	- Windows: ex. PBRT_PATH = C:/path/where/you/compiled/pbrt.exe

In order to render in Batch mode, you'll need to set two additional environment variables

- MAYA_RENDER_DESC_PATH has to point to the folder containing the PBRTRenderer.xml file.

- MAYA_PLUG_IN_PATH has to point to the PBRTForMaya plug-ins folder

- Example Maya.env settings for Windows:

	- MAYA_RENDER_DESC_PATH = C:\path\to\PBRTForMaya

	- MAYA_PLUG_IN_PATH = C:\path\to\PBRTForMaya\plug-ins

***VERY IMPORTANT*** 
If your scene contains animation on the parameters of the PBRT lights, materials or volumes and you are using Maya 2016 or later, you will need to set the following environment variable

- MAYA_RELEASE_PYTHON_GIL = 1

- Without this setting, Maya will lock up.

- [Discussion on Python Programming for Autodesk Maya Google Group](https://groups.google.com/forum/?hl=en#!topic/python_inside_maya/Zk7FKPu7J_A)


In order for the Maya render region functionality to work, the path to the [OpenImageIO](https://github.com/OpenImageIO/oiio) 'oiiotool' binary has to be specified, either in the Render Settings manually or by using the Maya.env or other environment setup file.

- To set the value in the Maya.env or in your shell environment, set the OIIOTOOL_PATH environment variable to  

	- Windows: OIIOTOOL_PATH = C:\path\to\oiiotool.exe

	- Mac: OIIOTOOL_PATH = /path/to/oiiotool

	- Linux: OIIOTOOL_PATH = /path/to/oiiotool

- Resources for OpenImageIO include

	- [OpenImageIO github](https://github.com/OpenImageIO/oiio)

	- [Prebuilt Windows binaries](http://www.lfd.uci.edu/~gohlke/pythonlibs/#openimageio)

	- [Build instructions for Linux and OSX](https://github.com/OpenImageIO/oiio/blob/master/INSTALL)


Maya.env
-

Maya.env files can be saved in the following folders

- Windows: C:\Users\\*username*\\Documents\maya\<mayaVersion>

- Mac: /Users/*username*/Library/Preferences/Autodesk/maya/<mayaVersion>

- Linux: /home/*username*/maya/<mayaVersion>

*Autodesk Reference links*

- [Setting the Maya.env](http://help.autodesk.com/view/MAYAUL/2016/ENU/?guid=GUID-8EFB1AC1-ED7D-4099-9EEE-624097872C04)

- [Brief description of MAYA_RENDER_DESC_PATH](http://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2016/ENU/Maya/files/GUID-AF8A7EA4-DEEF-49EF-A18C-CDA72B4F9E1E-htm.html)


Rendering in Batch
-
Rendering an animation in Batch mode works, with a couple of caveats

- Batch renders can't be canceled from the UI

References
-

- [PBRT](http://www.pbrt.org/)

- [PBRT Example Scenes](http://www.pbrt.org/gallery.html)

- [PBRT Discussion Group](https://groups.google.com/forum/#!forum/pbrt)

- [PBRT Respository](https://github.com/mmp/pbrt-v3)

- [Example Goniometric Light Files](http://resources.mpi-inf.mpg.de/mpimodel/v1.0/luminaires/index.html)

- [OpenMaya renderer integrations](https://github.com/haggi/OpenMaya)

- [Source of test mesh geometry](http://graphics.cs.williams.edu/data/meshes.xml)

	- Material preview scene by Jonas Pilo

- [Ptex Example Files](http://ptex.us/samples.html)

- [MeshLab: A tool for working with various geometry formats](http://meshlab.sourceforge.net/)

	- [Github repo](https://github.com/cnr-isti-vclab/meshlab)

- [The PLY format](http://paulbourke.net/dataformats/ply/)

- [plyfile - A Python package for reading PLY files](https://pypi.python.org/pypi/plyfile)

	- [Github repo](https://github.com/dranjan/python-plyfile)

Testing
-

This plugin was tested with Maya 2016 on OSX Yosemite, Windows 7 and CentOS 7 Linux.

