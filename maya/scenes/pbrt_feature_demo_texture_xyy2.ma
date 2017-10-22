//Maya ASCII 2016 scene
//Name: pbrt_feature_demo_texture_xyy2.ma
//Codeset: UTF-8
file -rdi 1 -ns ":" -rfn "pbrt_feature_demo_baseRN" -op "v=0;" -typ "mayaAscii"
		 "scenes/pbrt_feature_demo_base.ma";
file -rdi 2 -ns ":" -rfn "MitsubaSphereRN" -op "v=0;" -typ "mayaAscii" "MitsubaSphere.ma";
file -r -ns ":" -dr 1 -rfn "pbrt_feature_demo_baseRN" -op "v=0;" -typ "mayaAscii"
		 "scenes/pbrt_feature_demo_base.ma";
requires maya "2016";
requires -nodeType "PBRTRenderSettings" -nodeType "PBRTxyY" -nodeType "PBRTUberMaterial"
		 "PBRTForMaya.py" "1.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2016";
fileInfo "version" "2016";
fileInfo "cutIdentifier" "201510022200-973226";
fileInfo "osv" "Mac OS X 10.9.6";
createNode transform -s -n "persp";
	rename -uid "419FB081-5F45-6952-EE9F-84BE79578418";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 4.2648349603712781 10.88172958724515 -23.398167623275601 ;
	setAttr ".r" -type "double3" -30.338352729544887 165.39999999999765 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "56120C1B-564D-7A61-9BCE-079737727E65";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".fl" 34.999999999999986;
	setAttr ".coi" 22.132045291878637;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -0.54999999999999982 -0.29728714626260533 -4.9137315221061399 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "CE376AD5-2141-2831-5F0F-44A16ABE005F";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 100.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "00DDC2E1-CE45-8D85-D1C6-A4BDEC621534";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "2E87EB18-144D-E853-682E-E3902E69F217";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 100.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "21F6AD9C-4B4B-5190-2CF7-8C9CDECAB013";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "5BD11948-5B4B-EC45-5869-228AED4F2E05";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 100.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "16E50EFD-2948-45B2-66C6-5FADA15569B5";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "MacbethChart";
	rename -uid "185C8B74-FE4C-9823-21F8-3A9F40665B06";
	setAttr ".t" -type "double3" 0 1.3 -4.5 ;
	setAttr ".r" -type "double3" -75 0 0 ;
	setAttr ".s" -type "double3" 1.6 1.6 1.6 ;
createNode transform -n "macbethChip24" -p "MacbethChart";
	rename -uid "0BCFBA4A-C04C-64EE-342E-FAAFD6A3B8AD";
	setAttr ".t" -type "double3" -2.75 0 -1.6500000000000001 ;
createNode mesh -n "macbethChipShape1" -p "macbethChip24";
	rename -uid "78AAB418-5B49-AE53-1B04-5B8B76B5E29F";
	setAttr -k off ".v";
	setAttr -s 24 ".iog";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "macbethChip23" -p "MacbethChart";
	rename -uid "22F702B9-4349-093D-7C15-0F8B76190370";
	setAttr ".t" -type "double3" -1.6500000000000004 0 -1.6500000000000001 ;
createNode transform -n "macbethChip22" -p "MacbethChart";
	rename -uid "59774FCB-D74D-3E1B-1F01-499FE46402C6";
	setAttr ".t" -type "double3" -0.54999999999999982 0 -1.6500000000000001 ;
createNode transform -n "macbethChip21" -p "MacbethChart";
	rename -uid "E05FDF2F-4C4C-F5E9-053E-3E82FC0F36DC";
	setAttr ".t" -type "double3" 0.54999999999999982 0 -1.6500000000000001 ;
createNode transform -n "macbethChip20" -p "MacbethChart";
	rename -uid "28C94870-C74E-D20B-B468-0CA200CAE28D";
	setAttr ".t" -type "double3" 1.65 0 -1.6500000000000001 ;
createNode transform -n "macbethChip19" -p "MacbethChart";
	rename -uid "8C13D310-E547-7BE9-4E05-1C84E10A2B03";
	setAttr ".t" -type "double3" 2.75 0 -1.6500000000000001 ;
createNode transform -n "macbethChip18" -p "MacbethChart";
	rename -uid "AFEEA1D9-D44E-B336-17B6-0C9F5AB67F3C";
	setAttr ".t" -type "double3" -2.75 0 -0.55 ;
createNode transform -n "macbethChip17" -p "MacbethChart";
	rename -uid "59CDAFFE-2E4C-12CC-3BA2-8EA7919A9B4D";
	setAttr ".t" -type "double3" -1.6500000000000004 0 -0.55 ;
createNode transform -n "macbethChip16" -p "MacbethChart";
	rename -uid "7611E3A1-5641-6A02-4C23-DFB40AF6DD5C";
	setAttr ".t" -type "double3" -0.54999999999999982 0 -0.55 ;
createNode transform -n "macbethChip15" -p "MacbethChart";
	rename -uid "053CAE98-1546-C4DC-CDC5-6E9E59AAA549";
	setAttr ".t" -type "double3" 0.54999999999999982 0 -0.55 ;
createNode transform -n "macbethChip14" -p "MacbethChart";
	rename -uid "C8D8DD67-1545-48E7-4DAE-C4A6EA92724C";
	setAttr ".t" -type "double3" 1.65 0 -0.55 ;
createNode transform -n "macbethChip13" -p "MacbethChart";
	rename -uid "1F281B67-B747-F722-BA04-949C3581A98E";
	setAttr ".t" -type "double3" 2.75 0 -0.55 ;
createNode transform -n "macbethChip12" -p "MacbethChart";
	rename -uid "63EEC5A9-CE47-8784-4850-499F3B3B5B02";
	setAttr ".t" -type "double3" -2.75 0 0.55 ;
createNode transform -n "macbethChip11" -p "MacbethChart";
	rename -uid "AA3D502F-AB43-19D2-0292-F1A043271EB2";
	setAttr ".t" -type "double3" -1.6500000000000004 0 0.55 ;
createNode transform -n "macbethChip10" -p "MacbethChart";
	rename -uid "B16425A4-894C-BD9D-6E23-D9ADB4FF288F";
	setAttr ".t" -type "double3" -0.54999999999999982 0 0.55 ;
createNode transform -n "macbethChip9" -p "MacbethChart";
	rename -uid "FDEEB696-4E4B-C6B4-6C51-539D611EB638";
	setAttr ".t" -type "double3" 0.54999999999999982 0 0.55 ;
createNode transform -n "macbethChip8" -p "MacbethChart";
	rename -uid "0AAF4F5E-2A4D-82EF-84D2-37905059189C";
	setAttr ".t" -type "double3" 1.65 0 0.55 ;
createNode transform -n "macbethChip7" -p "MacbethChart";
	rename -uid "B38F2A9A-B241-6F12-3F6C-3FB974F11744";
	setAttr ".t" -type "double3" 2.75 0 0.55 ;
createNode transform -n "macbethChip6" -p "MacbethChart";
	rename -uid "A1213658-044E-95C3-0F6C-A2AF19153E9A";
	setAttr ".t" -type "double3" -2.75 0 1.6500000000000001 ;
createNode transform -n "macbethChip5" -p "MacbethChart";
	rename -uid "67BA81B8-944C-315A-8967-31B4862A8E83";
	setAttr ".t" -type "double3" -1.65 0 1.6500000000000001 ;
createNode transform -n "macbethChip4" -p "MacbethChart";
	rename -uid "BB34D4A3-5C45-B2E6-F9B6-3DB6005631ED";
	setAttr ".t" -type "double3" -0.54999999999999993 0 1.6500000000000001 ;
createNode transform -n "macbethChip3" -p "MacbethChart";
	rename -uid "DAC65DB6-654B-E590-8526-168360F2FAD6";
	setAttr ".t" -type "double3" 0.55 0 1.6500000000000001 ;
createNode transform -n "macbethChip2" -p "MacbethChart";
	rename -uid "71B092AE-C54F-06B9-69E4-1DB073862DDF";
	setAttr ".t" -type "double3" 1.6500000000000001 0 1.6500000000000001 ;
createNode transform -n "macbethChip1" -p "MacbethChart";
	rename -uid "354EA633-8B40-A4A9-BFF7-DA9B14FE43BB";
	setAttr ".t" -type "double3" 2.75 0 1.6500000000000001 ;
createNode transform -n "macbethBacking" -p "MacbethChart";
	rename -uid "413171BB-3A46-5B78-CD69-908C4E6FCE86";
	setAttr ".t" -type "double3" 0 -0.01 0 ;
	setAttr ".s" -type "double3" 6.7 1 4.6 ;
createNode mesh -n "macbethBackingShape" -p "macbethBacking";
	rename -uid "4F89EB51-E643-5D78-2428-C7A61BE6D8C6";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 121 ".uvst[0].uvsp[0:120]" -type "float2" 0 0 0.1 0 0.2 0 0.30000001
		 0 0.40000001 0 0.5 0 0.60000002 0 0.69999999 0 0.80000001 0 0.90000004 0 1 0 0 0.1
		 0.1 0.1 0.2 0.1 0.30000001 0.1 0.40000001 0.1 0.5 0.1 0.60000002 0.1 0.69999999 0.1
		 0.80000001 0.1 0.90000004 0.1 1 0.1 0 0.2 0.1 0.2 0.2 0.2 0.30000001 0.2 0.40000001
		 0.2 0.5 0.2 0.60000002 0.2 0.69999999 0.2 0.80000001 0.2 0.90000004 0.2 1 0.2 0 0.30000001
		 0.1 0.30000001 0.2 0.30000001 0.30000001 0.30000001 0.40000001 0.30000001 0.5 0.30000001
		 0.60000002 0.30000001 0.69999999 0.30000001 0.80000001 0.30000001 0.90000004 0.30000001
		 1 0.30000001 0 0.40000001 0.1 0.40000001 0.2 0.40000001 0.30000001 0.40000001 0.40000001
		 0.40000001 0.5 0.40000001 0.60000002 0.40000001 0.69999999 0.40000001 0.80000001
		 0.40000001 0.90000004 0.40000001 1 0.40000001 0 0.5 0.1 0.5 0.2 0.5 0.30000001 0.5
		 0.40000001 0.5 0.5 0.5 0.60000002 0.5 0.69999999 0.5 0.80000001 0.5 0.90000004 0.5
		 1 0.5 0 0.60000002 0.1 0.60000002 0.2 0.60000002 0.30000001 0.60000002 0.40000001
		 0.60000002 0.5 0.60000002 0.60000002 0.60000002 0.69999999 0.60000002 0.80000001
		 0.60000002 0.90000004 0.60000002 1 0.60000002 0 0.69999999 0.1 0.69999999 0.2 0.69999999
		 0.30000001 0.69999999 0.40000001 0.69999999 0.5 0.69999999 0.60000002 0.69999999
		 0.69999999 0.69999999 0.80000001 0.69999999 0.90000004 0.69999999 1 0.69999999 0
		 0.80000001 0.1 0.80000001 0.2 0.80000001 0.30000001 0.80000001 0.40000001 0.80000001
		 0.5 0.80000001 0.60000002 0.80000001 0.69999999 0.80000001 0.80000001 0.80000001
		 0.90000004 0.80000001 1 0.80000001 0 0.90000004 0.1 0.90000004 0.2 0.90000004 0.30000001
		 0.90000004 0.40000001 0.90000004 0.5 0.90000004 0.60000002 0.90000004 0.69999999
		 0.90000004 0.80000001 0.90000004 0.90000004 0.90000004 1 0.90000004 0 1 0.1 1 0.2
		 1 0.30000001 1 0.40000001 1 0.5 1 0.60000002 1 0.69999999 1 0.80000001 1 0.90000004
		 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 121 ".vt[0:120]"  -0.5 -1.110223e-16 0.5 -0.40000001 -1.110223e-16 0.5
		 -0.30000001 -1.110223e-16 0.5 -0.19999999 -1.110223e-16 0.5 -0.099999994 -1.110223e-16 0.5
		 0 -1.110223e-16 0.5 0.10000002 -1.110223e-16 0.5 0.19999999 -1.110223e-16 0.5 0.30000001 -1.110223e-16 0.5
		 0.40000004 -1.110223e-16 0.5 0.5 -1.110223e-16 0.5 -0.5 -8.8817843e-17 0.40000001
		 -0.40000001 -8.8817843e-17 0.40000001 -0.30000001 -8.8817843e-17 0.40000001 -0.19999999 -8.8817843e-17 0.40000001
		 -0.099999994 -8.8817843e-17 0.40000001 0 -8.8817843e-17 0.40000001 0.10000002 -8.8817843e-17 0.40000001
		 0.19999999 -8.8817843e-17 0.40000001 0.30000001 -8.8817843e-17 0.40000001 0.40000004 -8.8817843e-17 0.40000001
		 0.5 -8.8817843e-17 0.40000001 -0.5 -6.6613384e-17 0.30000001 -0.40000001 -6.6613384e-17 0.30000001
		 -0.30000001 -6.6613384e-17 0.30000001 -0.19999999 -6.6613384e-17 0.30000001 -0.099999994 -6.6613384e-17 0.30000001
		 0 -6.6613384e-17 0.30000001 0.10000002 -6.6613384e-17 0.30000001 0.19999999 -6.6613384e-17 0.30000001
		 0.30000001 -6.6613384e-17 0.30000001 0.40000004 -6.6613384e-17 0.30000001 0.5 -6.6613384e-17 0.30000001
		 -0.5 -4.4408918e-17 0.19999999 -0.40000001 -4.4408918e-17 0.19999999 -0.30000001 -4.4408918e-17 0.19999999
		 -0.19999999 -4.4408918e-17 0.19999999 -0.099999994 -4.4408918e-17 0.19999999 0 -4.4408918e-17 0.19999999
		 0.10000002 -4.4408918e-17 0.19999999 0.19999999 -4.4408918e-17 0.19999999 0.30000001 -4.4408918e-17 0.19999999
		 0.40000004 -4.4408918e-17 0.19999999 0.5 -4.4408918e-17 0.19999999 -0.5 -2.2204459e-17 0.099999994
		 -0.40000001 -2.2204459e-17 0.099999994 -0.30000001 -2.2204459e-17 0.099999994 -0.19999999 -2.2204459e-17 0.099999994
		 -0.099999994 -2.2204459e-17 0.099999994 0 -2.2204459e-17 0.099999994 0.10000002 -2.2204459e-17 0.099999994
		 0.19999999 -2.2204459e-17 0.099999994 0.30000001 -2.2204459e-17 0.099999994 0.40000004 -2.2204459e-17 0.099999994
		 0.5 -2.2204459e-17 0.099999994 -0.5 0 0 -0.40000001 0 0 -0.30000001 0 0 -0.19999999 0 0
		 -0.099999994 0 0 0 0 0 0.10000002 0 0 0.19999999 0 0 0.30000001 0 0 0.40000004 0 0
		 0.5 0 0 -0.5 2.2204466e-17 -0.10000002 -0.40000001 2.2204466e-17 -0.10000002 -0.30000001 2.2204466e-17 -0.10000002
		 -0.19999999 2.2204466e-17 -0.10000002 -0.099999994 2.2204466e-17 -0.10000002 0 2.2204466e-17 -0.10000002
		 0.10000002 2.2204466e-17 -0.10000002 0.19999999 2.2204466e-17 -0.10000002 0.30000001 2.2204466e-17 -0.10000002
		 0.40000004 2.2204466e-17 -0.10000002 0.5 2.2204466e-17 -0.10000002 -0.5 4.4408918e-17 -0.19999999
		 -0.40000001 4.4408918e-17 -0.19999999 -0.30000001 4.4408918e-17 -0.19999999 -0.19999999 4.4408918e-17 -0.19999999
		 -0.099999994 4.4408918e-17 -0.19999999 0 4.4408918e-17 -0.19999999 0.10000002 4.4408918e-17 -0.19999999
		 0.19999999 4.4408918e-17 -0.19999999 0.30000001 4.4408918e-17 -0.19999999 0.40000004 4.4408918e-17 -0.19999999
		 0.5 4.4408918e-17 -0.19999999 -0.5 6.6613384e-17 -0.30000001 -0.40000001 6.6613384e-17 -0.30000001
		 -0.30000001 6.6613384e-17 -0.30000001 -0.19999999 6.6613384e-17 -0.30000001 -0.099999994 6.6613384e-17 -0.30000001
		 0 6.6613384e-17 -0.30000001 0.10000002 6.6613384e-17 -0.30000001 0.19999999 6.6613384e-17 -0.30000001
		 0.30000001 6.6613384e-17 -0.30000001 0.40000004 6.6613384e-17 -0.30000001 0.5 6.6613384e-17 -0.30000001
		 -0.5 8.881785e-17 -0.40000004 -0.40000001 8.881785e-17 -0.40000004 -0.30000001 8.881785e-17 -0.40000004
		 -0.19999999 8.881785e-17 -0.40000004 -0.099999994 8.881785e-17 -0.40000004 0 8.881785e-17 -0.40000004
		 0.10000002 8.881785e-17 -0.40000004 0.19999999 8.881785e-17 -0.40000004 0.30000001 8.881785e-17 -0.40000004
		 0.40000004 8.881785e-17 -0.40000004 0.5 8.881785e-17 -0.40000004 -0.5 1.110223e-16 -0.5
		 -0.40000001 1.110223e-16 -0.5 -0.30000001 1.110223e-16 -0.5 -0.19999999 1.110223e-16 -0.5
		 -0.099999994 1.110223e-16 -0.5 0 1.110223e-16 -0.5 0.10000002 1.110223e-16 -0.5 0.19999999 1.110223e-16 -0.5
		 0.30000001 1.110223e-16 -0.5 0.40000004 1.110223e-16 -0.5 0.5 1.110223e-16 -0.5;
	setAttr -s 220 ".ed";
	setAttr ".ed[0:165]"  0 1 0 0 11 0 1 2 0 1 12 1 2 3 0 2 13 1 3 4 0 3 14 1
		 4 5 0 4 15 1 5 6 0 5 16 1 6 7 0 6 17 1 7 8 0 7 18 1 8 9 0 8 19 1 9 10 0 9 20 1 10 21 0
		 11 12 1 11 22 0 12 13 1 12 23 1 13 14 1 13 24 1 14 15 1 14 25 1 15 16 1 15 26 1 16 17 1
		 16 27 1 17 18 1 17 28 1 18 19 1 18 29 1 19 20 1 19 30 1 20 21 1 20 31 1 21 32 0 22 23 1
		 22 33 0 23 24 1 23 34 1 24 25 1 24 35 1 25 26 1 25 36 1 26 27 1 26 37 1 27 28 1 27 38 1
		 28 29 1 28 39 1 29 30 1 29 40 1 30 31 1 30 41 1 31 32 1 31 42 1 32 43 0 33 34 1 33 44 0
		 34 35 1 34 45 1 35 36 1 35 46 1 36 37 1 36 47 1 37 38 1 37 48 1 38 39 1 38 49 1 39 40 1
		 39 50 1 40 41 1 40 51 1 41 42 1 41 52 1 42 43 1 42 53 1 43 54 0 44 45 1 44 55 0 45 46 1
		 45 56 1 46 47 1 46 57 1 47 48 1 47 58 1 48 49 1 48 59 1 49 50 1 49 60 1 50 51 1 50 61 1
		 51 52 1 51 62 1 52 53 1 52 63 1 53 54 1 53 64 1 54 65 0 55 56 1 55 66 0 56 57 1 56 67 1
		 57 58 1 57 68 1 58 59 1 58 69 1 59 60 1 59 70 1 60 61 1 60 71 1 61 62 1 61 72 1 62 63 1
		 62 73 1 63 64 1 63 74 1 64 65 1 64 75 1 65 76 0 66 67 1 66 77 0 67 68 1 67 78 1 68 69 1
		 68 79 1 69 70 1 69 80 1 70 71 1 70 81 1 71 72 1 71 82 1 72 73 1 72 83 1 73 74 1 73 84 1
		 74 75 1 74 85 1 75 76 1 75 86 1 76 87 0 77 78 1 77 88 0 78 79 1 78 89 1 79 80 1 79 90 1
		 80 81 1 80 91 1 81 82 1 81 92 1 82 83 1 82 93 1 83 84 1 83 94 1 84 85 1 84 95 1 85 86 1
		 85 96 1 86 87 1;
	setAttr ".ed[166:219]" 86 97 1 87 98 0 88 89 1 88 99 0 89 90 1 89 100 1 90 91 1
		 90 101 1 91 92 1 91 102 1 92 93 1 92 103 1 93 94 1 93 104 1 94 95 1 94 105 1 95 96 1
		 95 106 1 96 97 1 96 107 1 97 98 1 97 108 1 98 109 0 99 100 1 99 110 0 100 101 1 100 111 1
		 101 102 1 101 112 1 102 103 1 102 113 1 103 104 1 103 114 1 104 105 1 104 115 1 105 106 1
		 105 116 1 106 107 1 106 117 1 107 108 1 107 118 1 108 109 1 108 119 1 109 120 0 110 111 0
		 111 112 0 112 113 0 113 114 0 114 115 0 115 116 0 116 117 0 117 118 0 118 119 0 119 120 0;
	setAttr -s 100 -ch 400 ".fc[0:99]" -type "polyFaces" 
		f 4 0 3 -22 -2
		mu 0 4 0 1 12 11
		f 4 2 5 -24 -4
		mu 0 4 1 2 13 12
		f 4 4 7 -26 -6
		mu 0 4 2 3 14 13
		f 4 6 9 -28 -8
		mu 0 4 3 4 15 14
		f 4 8 11 -30 -10
		mu 0 4 4 5 16 15
		f 4 10 13 -32 -12
		mu 0 4 5 6 17 16
		f 4 12 15 -34 -14
		mu 0 4 6 7 18 17
		f 4 14 17 -36 -16
		mu 0 4 7 8 19 18
		f 4 16 19 -38 -18
		mu 0 4 8 9 20 19
		f 4 18 20 -40 -20
		mu 0 4 9 10 21 20
		f 4 21 24 -43 -23
		mu 0 4 11 12 23 22
		f 4 23 26 -45 -25
		mu 0 4 12 13 24 23
		f 4 25 28 -47 -27
		mu 0 4 13 14 25 24
		f 4 27 30 -49 -29
		mu 0 4 14 15 26 25
		f 4 29 32 -51 -31
		mu 0 4 15 16 27 26
		f 4 31 34 -53 -33
		mu 0 4 16 17 28 27
		f 4 33 36 -55 -35
		mu 0 4 17 18 29 28
		f 4 35 38 -57 -37
		mu 0 4 18 19 30 29
		f 4 37 40 -59 -39
		mu 0 4 19 20 31 30
		f 4 39 41 -61 -41
		mu 0 4 20 21 32 31
		f 4 42 45 -64 -44
		mu 0 4 22 23 34 33
		f 4 44 47 -66 -46
		mu 0 4 23 24 35 34
		f 4 46 49 -68 -48
		mu 0 4 24 25 36 35
		f 4 48 51 -70 -50
		mu 0 4 25 26 37 36
		f 4 50 53 -72 -52
		mu 0 4 26 27 38 37
		f 4 52 55 -74 -54
		mu 0 4 27 28 39 38
		f 4 54 57 -76 -56
		mu 0 4 28 29 40 39
		f 4 56 59 -78 -58
		mu 0 4 29 30 41 40
		f 4 58 61 -80 -60
		mu 0 4 30 31 42 41
		f 4 60 62 -82 -62
		mu 0 4 31 32 43 42
		f 4 63 66 -85 -65
		mu 0 4 33 34 45 44
		f 4 65 68 -87 -67
		mu 0 4 34 35 46 45
		f 4 67 70 -89 -69
		mu 0 4 35 36 47 46
		f 4 69 72 -91 -71
		mu 0 4 36 37 48 47
		f 4 71 74 -93 -73
		mu 0 4 37 38 49 48
		f 4 73 76 -95 -75
		mu 0 4 38 39 50 49
		f 4 75 78 -97 -77
		mu 0 4 39 40 51 50
		f 4 77 80 -99 -79
		mu 0 4 40 41 52 51
		f 4 79 82 -101 -81
		mu 0 4 41 42 53 52
		f 4 81 83 -103 -83
		mu 0 4 42 43 54 53
		f 4 84 87 -106 -86
		mu 0 4 44 45 56 55
		f 4 86 89 -108 -88
		mu 0 4 45 46 57 56
		f 4 88 91 -110 -90
		mu 0 4 46 47 58 57
		f 4 90 93 -112 -92
		mu 0 4 47 48 59 58
		f 4 92 95 -114 -94
		mu 0 4 48 49 60 59
		f 4 94 97 -116 -96
		mu 0 4 49 50 61 60
		f 4 96 99 -118 -98
		mu 0 4 50 51 62 61
		f 4 98 101 -120 -100
		mu 0 4 51 52 63 62
		f 4 100 103 -122 -102
		mu 0 4 52 53 64 63
		f 4 102 104 -124 -104
		mu 0 4 53 54 65 64
		f 4 105 108 -127 -107
		mu 0 4 55 56 67 66
		f 4 107 110 -129 -109
		mu 0 4 56 57 68 67
		f 4 109 112 -131 -111
		mu 0 4 57 58 69 68
		f 4 111 114 -133 -113
		mu 0 4 58 59 70 69
		f 4 113 116 -135 -115
		mu 0 4 59 60 71 70
		f 4 115 118 -137 -117
		mu 0 4 60 61 72 71
		f 4 117 120 -139 -119
		mu 0 4 61 62 73 72
		f 4 119 122 -141 -121
		mu 0 4 62 63 74 73
		f 4 121 124 -143 -123
		mu 0 4 63 64 75 74
		f 4 123 125 -145 -125
		mu 0 4 64 65 76 75
		f 4 126 129 -148 -128
		mu 0 4 66 67 78 77
		f 4 128 131 -150 -130
		mu 0 4 67 68 79 78
		f 4 130 133 -152 -132
		mu 0 4 68 69 80 79
		f 4 132 135 -154 -134
		mu 0 4 69 70 81 80
		f 4 134 137 -156 -136
		mu 0 4 70 71 82 81
		f 4 136 139 -158 -138
		mu 0 4 71 72 83 82
		f 4 138 141 -160 -140
		mu 0 4 72 73 84 83
		f 4 140 143 -162 -142
		mu 0 4 73 74 85 84
		f 4 142 145 -164 -144
		mu 0 4 74 75 86 85
		f 4 144 146 -166 -146
		mu 0 4 75 76 87 86
		f 4 147 150 -169 -149
		mu 0 4 77 78 89 88
		f 4 149 152 -171 -151
		mu 0 4 78 79 90 89
		f 4 151 154 -173 -153
		mu 0 4 79 80 91 90
		f 4 153 156 -175 -155
		mu 0 4 80 81 92 91
		f 4 155 158 -177 -157
		mu 0 4 81 82 93 92
		f 4 157 160 -179 -159
		mu 0 4 82 83 94 93
		f 4 159 162 -181 -161
		mu 0 4 83 84 95 94
		f 4 161 164 -183 -163
		mu 0 4 84 85 96 95
		f 4 163 166 -185 -165
		mu 0 4 85 86 97 96
		f 4 165 167 -187 -167
		mu 0 4 86 87 98 97
		f 4 168 171 -190 -170
		mu 0 4 88 89 100 99
		f 4 170 173 -192 -172
		mu 0 4 89 90 101 100
		f 4 172 175 -194 -174
		mu 0 4 90 91 102 101
		f 4 174 177 -196 -176
		mu 0 4 91 92 103 102
		f 4 176 179 -198 -178
		mu 0 4 92 93 104 103
		f 4 178 181 -200 -180
		mu 0 4 93 94 105 104
		f 4 180 183 -202 -182
		mu 0 4 94 95 106 105
		f 4 182 185 -204 -184
		mu 0 4 95 96 107 106
		f 4 184 187 -206 -186
		mu 0 4 96 97 108 107
		f 4 186 188 -208 -188
		mu 0 4 97 98 109 108
		f 4 189 192 -211 -191
		mu 0 4 99 100 111 110
		f 4 191 194 -212 -193
		mu 0 4 100 101 112 111
		f 4 193 196 -213 -195
		mu 0 4 101 102 113 112
		f 4 195 198 -214 -197
		mu 0 4 102 103 114 113
		f 4 197 200 -215 -199
		mu 0 4 103 104 115 114
		f 4 199 202 -216 -201
		mu 0 4 104 105 116 115
		f 4 201 204 -217 -203
		mu 0 4 105 106 117 116
		f 4 203 206 -218 -205
		mu 0 4 106 107 118 117
		f 4 205 208 -219 -207
		mu 0 4 107 108 119 118
		f 4 207 209 -220 -209
		mu 0 4 108 109 120 119;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip1" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip2" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip3" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip4" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip5" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip6" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip7" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip8" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip9" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip10" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip11" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip12" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip13" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip14" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip15" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip16" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip17" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip18" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip19" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip20" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip21" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip22" ;
parent -s -nc -r -add "|MacbethChart|macbethChip24|macbethChipShape1" "macbethChip23" ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "2388A990-804B-C83A-53FD-75B50FFD90B4";
	setAttr -s 34 ".lnk";
	setAttr -s 34 ".slnk";
createNode displayLayerManager -n "layerManager";
	rename -uid "F3C54437-6C43-1515-3696-1793A779FD71";
createNode displayLayer -n "defaultLayer";
	rename -uid "C511759B-A943-ACFF-9870-E3A2C5601981";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "14E9D5E5-DE4C-2FF3-BB47-B48AB8C717DF";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "5E551EF0-6C46-AAAA-F7BB-59BC058797EA";
	setAttr ".g" yes;
createNode reference -n "pbrt_feature_demo_baseRN";
	rename -uid "28AF6165-2446-44C3-8C92-5CABE40F60EA";
	setAttr -s 3 ".phl";
	setAttr ".phl[1]" 0;
	setAttr ".phl[2]" 0;
	setAttr ".phl[3]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"pbrt_feature_demo_baseRN"
		"MitsubaSphereRN" 0
		"pbrt_feature_demo_baseRN" 0
		"MitsubaSphereRN" 5
		2 "|MitsubaSphere" "visibility" " 1"
		3 "|MitsubaSphere|Mesh1|Mesh1Shape.instObjGroups" "PBRTUberMaterial1SG.dagSetMembers" 
		"-na"
		3 "|MitsubaSphere|Mesh|MeshShape.instObjGroups" "PBRTUberMaterial1SG.dagSetMembers" 
		"-na"
		5 3 "pbrt_feature_demo_baseRN" "|MitsubaSphere|Mesh1|Mesh1Shape.instObjGroups" 
		"pbrt_feature_demo_baseRN.placeHolderList[1]" "PBRTUberMaterial1SG.dsm"
		5 3 "pbrt_feature_demo_baseRN" "|MitsubaSphere|Mesh|MeshShape.instObjGroups" 
		"pbrt_feature_demo_baseRN.placeHolderList[2]" "PBRTUberMaterial1SG.dsm"
		"pbrt_feature_demo_baseRN" 16
		2 "|referenceCamera1" "rotatePivot" " -type \"double3\" 0 0 0"
		2 "|referenceCamera1" "rotatePivotTranslate" " -type \"double3\" 0 0 0"
		2 "|referenceCamera1|referenceCamera1Shape" "displayGateMask" " 1"
		2 "|referenceCamera1|referenceCamera1Shape" "displayFilmGate" " 1"
		2 "|referenceCamera1|referenceCamera1Shape" "displayResolution" " 0"
		2 "|materialSphere" "visibility" " 1"
		2 "PBRTInfiniteLight1" "luminance" " -type \"float3\" 1 1 1"
		2 "hyperShadePrimaryNodeEditorSavedTabsInfo" "tabGraphInfo[0].nodeInfo" " -s 6"
		
		3 "|materialSphere|materialSphereShape.instObjGroups" "PBRTUberMaterial1SG.dagSetMembers" 
		"-na"
		3 "PBRTMatteMaterial1SG.message" "hyperShadePrimaryNodeEditorSavedTabsInfo.tabGraphInfo[0].nodeInfo[0].dependNode" 
		""
		3 "pbrt_grey18.message" "hyperShadePrimaryNodeEditorSavedTabsInfo.tabGraphInfo[0].nodeInfo[1].dependNode" 
		""
		3 "pbrt_ground.message" "hyperShadePrimaryNodeEditorSavedTabsInfo.tabGraphInfo[0].nodeInfo[2].dependNode" 
		""
		3 "PBRTMatteMaterial2SG.message" "hyperShadePrimaryNodeEditorSavedTabsInfo.tabGraphInfo[0].nodeInfo[3].dependNode" 
		""
		3 "checker1.message" "hyperShadePrimaryNodeEditorSavedTabsInfo.tabGraphInfo[0].nodeInfo[4].dependNode" 
		""
		3 "place2dTexture3.message" "hyperShadePrimaryNodeEditorSavedTabsInfo.tabGraphInfo[0].nodeInfo[5].dependNode" 
		""
		5 3 "pbrt_feature_demo_baseRN" "|materialSphere|materialSphereShape.instObjGroups" 
		"pbrt_feature_demo_baseRN.placeHolderList[3]" "PBRTUberMaterial1SG.dsm";
	setAttr ".ptag" -type "string" "";
lockNode -l 1 ;
createNode PBRTRenderSettings -s -n "defaultPBRTRenderGlobals";
	rename -uid "D92BE0C5-7246-B907-F516-7CA1E5D15D08";
	setAttr ".smpl" -type "string" "Halton";
	setAttr ".smps" 1024;
	setAttr ".kt" yes;
createNode script -n "uiConfigurationScriptNode1";
	rename -uid "87BB582C-134E-341E-8956-D4B3F7D338C0";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"top\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n"
		+ "                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n"
		+ "                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n"
		+ "                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 1\n                -height 1\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n"
		+ "            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n"
		+ "            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"side\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n"
		+ "                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n"
		+ "                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n"
		+ "                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 1\n                -height 1\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n"
		+ "            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n"
		+ "            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n"
		+ "            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n"
		+ "                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n"
		+ "                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n"
		+ "                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 1\n                -height 1\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n"
		+ "            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n"
		+ "            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n"
		+ "            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"referenceCamera1\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 0\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n"
		+ "                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n"
		+ "                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n"
		+ "                -captureSequenceNumber -1\n                -width 726\n                -height 583\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"referenceCamera1\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 0\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n"
		+ "            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n"
		+ "            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n"
		+ "            -captureSequenceNumber -1\n            -width 726\n            -height 583\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            outlinerEditor -e \n                -docTag \"isolOutln_fromSeln\" \n                -showShapes 1\n                -showReferenceNodes 1\n                -showReferenceMembers 1\n                -showAttributes 0\n                -showConnected 0\n                -showAnimCurvesOnly 0\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 1\n"
		+ "                -showAssets 1\n                -showContainedOnly 1\n                -showPublishedAsConnected 0\n                -showContainerContents 1\n                -ignoreDagHierarchy 0\n                -expandConnections 0\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 0\n                -highlightActive 1\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"defaultSetFilter\" \n                -showSetMembers 1\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n"
		+ "                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 0\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n"
		+ "            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n"
		+ "            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"graphEditor\" -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n"
		+ "                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n"
		+ "                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n"
		+ "                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n"
		+ "                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n"
		+ "                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n"
		+ "                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dopeSheetPanel\" -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n"
		+ "                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n"
		+ "                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n"
		+ "                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n"
		+ "                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n"
		+ "                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"clipEditorPanel\" -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n"
		+ "                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"sequenceEditorPanel\" -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n"
		+ "                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n"
		+ "                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n"
		+ "                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"visorPanel\" -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n"
		+ "\t\t\t$panelName = `scriptedPanel -unParent  -type \"createNodePanel\" -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"polyTexturePlacementPanel\" -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" == $panelName) {\n"
		+ "\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"renderWindowPanel\" -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\tscriptedPanel -e -to $panelName;\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"blendShapePanel\" (localizedPanelLabel(\"Blend Shape\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tblendShapePanel -unParent -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels ;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tblendShapePanel -edit -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynRelEdPanel\" -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"relationshipPanel\" -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"referenceEditorPanel\" -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"componentEditorPanel\" -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynPaintScriptedPanelType\" -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"scriptEditorPanel\" -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\tscriptedPanel -e -to $panelName;\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"profilerPanel\" -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"Stereo\" -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels `;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n"
		+ "                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n"
		+ "                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n"
		+ "                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "string $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n"
		+ "                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n"
		+ "                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n"
		+ "                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperShadePanel\" -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab -1\n                -editorMode \"default\" \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab -1\n                -editorMode \"default\" \n"
		+ "                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-defaultImage \"\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"vertical2\\\" -ps 1 22 100 -ps 2 78 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Outliner\")) \n\t\t\t\t\t\"outlinerPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\\\"Outliner\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\noutlinerEditor -e \\n    -docTag \\\"isolOutln_fromSeln\\\" \\n    -showShapes 1\\n    -showReferenceNodes 1\\n    -showReferenceMembers 1\\n    -showAttributes 0\\n    -showConnected 0\\n    -showAnimCurvesOnly 0\\n    -showMuteInfo 0\\n    -organizeByLayer 1\\n    -showAnimLayerWeight 1\\n    -autoExpandLayers 1\\n    -autoExpand 0\\n    -showDagOnly 1\\n    -showAssets 1\\n    -showContainedOnly 1\\n    -showPublishedAsConnected 0\\n    -showContainerContents 1\\n    -ignoreDagHierarchy 0\\n    -expandConnections 0\\n    -showUpstreamCurves 1\\n    -showUnitlessCurves 1\\n    -showCompounds 1\\n    -showLeafs 1\\n    -showNumericAttrsOnly 0\\n    -highlightActive 1\\n    -autoSelectNewObjects 0\\n    -doNotSelectNewObjects 0\\n    -dropIsParent 1\\n    -transmitFilters 0\\n    -setFilter \\\"defaultSetFilter\\\" \\n    -showSetMembers 1\\n    -allowMultiSelection 1\\n    -alwaysToggleSelect 0\\n    -directSelect 0\\n    -displayMode \\\"DAG\\\" \\n    -expandObjects 0\\n    -setsIgnoreFilters 1\\n    -containersIgnoreFilters 0\\n    -editAttrName 0\\n    -showAttrValues 0\\n    -highlightSecondary 0\\n    -showUVAttrsOnly 0\\n    -showTextureNodesOnly 0\\n    -attrAlphaOrder \\\"default\\\" \\n    -animLayerFilterOptions \\\"allAffecting\\\" \\n    -sortOrder \\\"none\\\" \\n    -longNames 0\\n    -niceNames 1\\n    -showNamespace 1\\n    -showPinIcons 0\\n    -mapMotionTrails 0\\n    -ignoreHiddenAttribute 0\\n    -ignoreOutlinerColor 0\\n    $editorName\"\n"
		+ "\t\t\t\t\t\"outlinerPanel -edit -l (localizedPanelLabel(\\\"Outliner\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\noutlinerEditor -e \\n    -docTag \\\"isolOutln_fromSeln\\\" \\n    -showShapes 1\\n    -showReferenceNodes 1\\n    -showReferenceMembers 1\\n    -showAttributes 0\\n    -showConnected 0\\n    -showAnimCurvesOnly 0\\n    -showMuteInfo 0\\n    -organizeByLayer 1\\n    -showAnimLayerWeight 1\\n    -autoExpandLayers 1\\n    -autoExpand 0\\n    -showDagOnly 1\\n    -showAssets 1\\n    -showContainedOnly 1\\n    -showPublishedAsConnected 0\\n    -showContainerContents 1\\n    -ignoreDagHierarchy 0\\n    -expandConnections 0\\n    -showUpstreamCurves 1\\n    -showUnitlessCurves 1\\n    -showCompounds 1\\n    -showLeafs 1\\n    -showNumericAttrsOnly 0\\n    -highlightActive 1\\n    -autoSelectNewObjects 0\\n    -doNotSelectNewObjects 0\\n    -dropIsParent 1\\n    -transmitFilters 0\\n    -setFilter \\\"defaultSetFilter\\\" \\n    -showSetMembers 1\\n    -allowMultiSelection 1\\n    -alwaysToggleSelect 0\\n    -directSelect 0\\n    -displayMode \\\"DAG\\\" \\n    -expandObjects 0\\n    -setsIgnoreFilters 1\\n    -containersIgnoreFilters 0\\n    -editAttrName 0\\n    -showAttrValues 0\\n    -highlightSecondary 0\\n    -showUVAttrsOnly 0\\n    -showTextureNodesOnly 0\\n    -attrAlphaOrder \\\"default\\\" \\n    -animLayerFilterOptions \\\"allAffecting\\\" \\n    -sortOrder \\\"none\\\" \\n    -longNames 0\\n    -niceNames 1\\n    -showNamespace 1\\n    -showPinIcons 0\\n    -mapMotionTrails 0\\n    -ignoreHiddenAttribute 0\\n    -ignoreOutlinerColor 0\\n    $editorName\"\n"
		+ "\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -camera \\\"referenceCamera1\\\" \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"wireframe\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 0\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 726\\n    -height 583\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -camera \\\"referenceCamera1\\\" \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"wireframe\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 0\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 726\\n    -height 583\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        setFocus `paneLayout -q -p1 $gMainPane`;\n        sceneUIReplacement -deleteRemaining;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode1";
	rename -uid "21634A6A-D843-E882-7584-40999D4261B6";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode PBRTUberMaterial -n "pbrt_uber1";
	rename -uid "EE2D7CA5-3247-8B4C-DEC9-43AF6BF54090";
	setAttr ".ks" -type "float3" 0.75 0.75 0.75 ;
	setAttr ".r" 0.02500000037252903;
createNode shadingEngine -n "PBRTUberMaterial2SG";
	rename -uid "7CF63616-7A4A-F856-4FD4-7B9AFDA31C98";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo4";
	rename -uid "40CF218A-764E-00E2-50A1-3EB2D2531D68";
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "9145015B-4B40-1325-0B57-4FBFA3E3F8A8";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -160.98990601898842 -980.32561331508543 ;
	setAttr ".tgi[0].vh" -type "double2" 846.5355157842771 67.045446638591912 ;
	setAttr -s 4 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 278.57144165039062;
	setAttr ".tgi[0].ni[0].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[0].nvs" 2098;
	setAttr ".tgi[0].ni[1].x" 557.14288330078125;
	setAttr ".tgi[0].ni[1].y" -92.857139587402344;
	setAttr ".tgi[0].ni[1].nvs" 1923;
	setAttr ".tgi[0].ni[2].x" 24.676553726196289;
	setAttr ".tgi[0].ni[2].y" -79.903671264648438;
	setAttr ".tgi[0].ni[2].nvs" 1923;
	setAttr ".tgi[0].ni[3].x" -236.75201416015625;
	setAttr ".tgi[0].ni[3].y" -99.903671264648438;
	setAttr ".tgi[0].ni[3].nvs" 1923;
createNode place2dTexture -n "place2dTexture2";
	rename -uid "E4D3FCCC-784A-BDFB-E1C3-21BED72F63C7";
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo2";
	rename -uid "885F0DD5-4C42-53A4-4B38-5C947EDCFABA";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -113.45431743790029 -783.52084021470989 ;
	setAttr ".tgi[0].vh" -type "double2" 1109.43642071827 487.73280849000946 ;
	setAttr -s 4 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 522.85711669921875;
	setAttr ".tgi[0].ni[0].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[0].nvs" 2098;
	setAttr ".tgi[0].ni[1].x" 801.4285888671875;
	setAttr ".tgi[0].ni[1].y" -88.571426391601562;
	setAttr ".tgi[0].ni[1].nvs" 1923;
	setAttr ".tgi[0].ni[2].x" 249.91358947753906;
	setAttr ".tgi[0].ni[2].y" -63.360588073730469;
	setAttr ".tgi[0].ni[2].nvs" 2098;
	setAttr ".tgi[0].ni[3].x" 1.4285714626312256;
	setAttr ".tgi[0].ni[3].y" -108.57142639160156;
	setAttr ".tgi[0].ni[3].nvs" 1923;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo3";
	rename -uid "3334FCC4-2E4E-4F7A-34D2-A389B03EB4DF";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -218.62522589891992 -671.81777603791943 ;
	setAttr ".tgi[0].vh" -type "double2" 647.53505916202357 228.59743555085777 ;
	setAttr -s 4 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 278.57144165039062;
	setAttr ".tgi[0].ni[0].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[0].nvs" 2098;
	setAttr ".tgi[0].ni[1].x" 557.14288330078125;
	setAttr ".tgi[0].ni[1].y" -92.857139587402344;
	setAttr ".tgi[0].ni[1].nvs" 1923;
	setAttr ".tgi[0].ni[2].x" -4.3889875411987305;
	setAttr ".tgi[0].ni[2].y" -53.143684387207031;
	setAttr ".tgi[0].ni[2].nvs" 1923;
	setAttr ".tgi[0].ni[3].x" -265.81756591796875;
	setAttr ".tgi[0].ni[3].y" -73.143684387207031;
	setAttr ".tgi[0].ni[3].nvs" 1923;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo4";
	rename -uid "05F36156-C54B-B27D-29FE-7DA705DF8375";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -113.45431743790033 -783.52084021471001 ;
	setAttr ".tgi[0].vh" -type "double2" 1109.43642071827 487.7328084900098 ;
	setAttr -s 4 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 522.85711669921875;
	setAttr ".tgi[0].ni[0].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[0].nvs" 2098;
	setAttr ".tgi[0].ni[1].x" 801.4285888671875;
	setAttr ".tgi[0].ni[1].y" -92.857139587402344;
	setAttr ".tgi[0].ni[1].nvs" 1923;
	setAttr ".tgi[0].ni[2].x" 219.97465515136719;
	setAttr ".tgi[0].ni[2].y" -95.602523803710938;
	setAttr ".tgi[0].ni[2].nvs" 2098;
	setAttr ".tgi[0].ni[3].x" -40.025352478027344;
	setAttr ".tgi[0].ni[3].y" -135.60252380371094;
	setAttr ".tgi[0].ni[3].nvs" 1923;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo5";
	rename -uid "678DB48A-9E4E-391C-E005-B6A583063163";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -113.65736201378404 -792.7798308486183 ;
	setAttr ".tgi[0].vh" -type "double2" 1126.3228311622731 496.23912702931665 ;
	setAttr -s 4 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 538.5714111328125;
	setAttr ".tgi[0].ni[0].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[0].nvs" 2098;
	setAttr ".tgi[0].ni[1].x" 817.14288330078125;
	setAttr ".tgi[0].ni[1].y" -92.857139587402344;
	setAttr ".tgi[0].ni[1].nvs" 1923;
	setAttr ".tgi[0].ni[2].x" 262.85714721679688;
	setAttr ".tgi[0].ni[2].y" -97.142860412597656;
	setAttr ".tgi[0].ni[2].nvs" 1923;
	setAttr ".tgi[0].ni[3].x" 1.4285714626312256;
	setAttr ".tgi[0].ni[3].y" -112.85713958740234;
	setAttr ".tgi[0].ni[3].nvs" 1923;
createNode PBRTUberMaterial -n "pbrt_uber2";
	rename -uid "1DC852A6-5C46-0433-0BCD-DEA017850E8B";
createNode shadingEngine -n "PBRTUberMaterial3SG";
	rename -uid "1F1E2428-0143-67A3-BE1B-3489EDB671F7";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo5";
	rename -uid "F18362E9-A546-92CC-3A7E-1880617A5B17";
createNode PBRTUberMaterial -n "pbrt_uber3";
	rename -uid "D8A327ED-8A41-38AB-A247-CE851420030E";
createNode shadingEngine -n "PBRTUberMaterial4SG";
	rename -uid "7C7255F3-9B45-C77D-E7C2-D2B384D437E8";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo6";
	rename -uid "1C499807-3B45-6185-3164-33897B562EBC";
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo6";
	rename -uid "67A75EB2-A340-D00F-D42C-50B747884760";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -113.45431743790003 -1212.3824112511543 ;
	setAttr ".tgi[0].vh" -type "double2" 1125.3425778494118 75.406451646390252 ;
	setAttr -s 12 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 531.9840087890625;
	setAttr ".tgi[0].ni[0].y" -833.59576416015625;
	setAttr ".tgi[0].ni[0].nvs" 2098;
	setAttr ".tgi[0].ni[1].x" 265.99200439453125;
	setAttr ".tgi[0].ni[1].y" -512.343994140625;
	setAttr ".tgi[0].ni[1].nvs" 1923;
	setAttr ".tgi[0].ni[2].x" 804.56341552734375;
	setAttr ".tgi[0].ni[2].y" -516.62969970703125;
	setAttr ".tgi[0].ni[2].nvs" 1923;
	setAttr ".tgi[0].ni[3].x" 271.98397827148438;
	setAttr ".tgi[0].ni[3].y" -925.0242919921875;
	setAttr ".tgi[0].ni[3].nvs" 1923;
	setAttr ".tgi[0].ni[4].x" 4.5634250640869141;
	setAttr ".tgi[0].ni[4].y" -532.343994140625;
	setAttr ".tgi[0].ni[4].nvs" 1923;
	setAttr ".tgi[0].ni[5].x" 810.555419921875;
	setAttr ".tgi[0].ni[5].y" -920.73858642578125;
	setAttr ".tgi[0].ni[5].nvs" 1923;
	setAttr ".tgi[0].ni[6].x" 525.99200439453125;
	setAttr ".tgi[0].ni[6].y" -425.201171875;
	setAttr ".tgi[0].ni[6].nvs" 2098;
	setAttr ".tgi[0].ni[7].x" 522.85711669921875;
	setAttr ".tgi[0].ni[7].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[7].nvs" 2098;
	setAttr ".tgi[0].ni[8].x" 1.4285714626312256;
	setAttr ".tgi[0].ni[8].y" -112.85713958740234;
	setAttr ".tgi[0].ni[8].nvs" 1923;
	setAttr ".tgi[0].ni[9].x" 262.85714721679688;
	setAttr ".tgi[0].ni[9].y" -97.142860412597656;
	setAttr ".tgi[0].ni[9].nvs" 1923;
	setAttr ".tgi[0].ni[10].x" 801.4285888671875;
	setAttr ".tgi[0].ni[10].y" -97.142860412597656;
	setAttr ".tgi[0].ni[10].nvs" 1923;
	setAttr ".tgi[0].ni[11].x" 10.555420875549316;
	setAttr ".tgi[0].ni[11].y" -945.0242919921875;
	setAttr ".tgi[0].ni[11].nvs" 1923;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo7";
	rename -uid "0CB59E95-5C44-2BE2-AEB5-E38FE0C2A81B";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -32.567630957879459 -1466.613643455998 ;
	setAttr ".tgi[0].vh" -type "double2" 1340.5094396601783 -39.234089819147556 ;
	setAttr -s 9 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 559.259521484375;
	setAttr ".tgi[0].ni[0].y" -845.2127685546875;
	setAttr ".tgi[0].ni[0].nvs" 2098;
	setAttr ".tgi[0].ni[1].x" 825.36260986328125;
	setAttr ".tgi[0].ni[1].y" -500.78121948242188;
	setAttr ".tgi[0].ni[1].nvs" 1923;
	setAttr ".tgi[0].ni[2].x" 837.8309326171875;
	setAttr ".tgi[0].ni[2].y" -936.641357421875;
	setAttr ".tgi[0].ni[2].nvs" 1923;
	setAttr ".tgi[0].ni[3].x" 546.79119873046875;
	setAttr ".tgi[0].ni[3].y" -405.06695556640625;
	setAttr ".tgi[0].ni[3].nvs" 2098;
	setAttr ".tgi[0].ni[4].x" 522.85711669921875;
	setAttr ".tgi[0].ni[4].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[4].nvs" 2098;
	setAttr ".tgi[0].ni[5].x" 801.4285888671875;
	setAttr ".tgi[0].ni[5].y" -92.857139587402344;
	setAttr ".tgi[0].ni[5].nvs" 1923;
	setAttr ".tgi[0].ni[6].x" 263.26327514648438;
	setAttr ".tgi[0].ni[6].y" -445.62838745117188;
	setAttr ".tgi[0].ni[6].nvs" 2098;
	setAttr ".tgi[0].ni[7].x" 257.45401000976562;
	setAttr ".tgi[0].ni[7].y" -911.39324951171875;
	setAttr ".tgi[0].ni[7].nvs" 2098;
	setAttr ".tgi[0].ni[8].x" 223.53575134277344;
	setAttr ".tgi[0].ni[8].y" -65.595947265625;
	setAttr ".tgi[0].ni[8].nvs" 2098;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo8";
	rename -uid "FA16B9E3-0247-10A5-A6EE-468ACB27CC50";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -32.567630957879459 -1466.613643455998 ;
	setAttr ".tgi[0].vh" -type "double2" 1340.5094396601783 -39.234089819147556 ;
	setAttr -s 9 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 559.259521484375;
	setAttr ".tgi[0].ni[0].y" -845.2127685546875;
	setAttr ".tgi[0].ni[0].nvs" 2098;
	setAttr ".tgi[0].ni[1].x" 825.36260986328125;
	setAttr ".tgi[0].ni[1].y" -500.78121948242188;
	setAttr ".tgi[0].ni[1].nvs" 1923;
	setAttr ".tgi[0].ni[2].x" 837.8309326171875;
	setAttr ".tgi[0].ni[2].y" -936.641357421875;
	setAttr ".tgi[0].ni[2].nvs" 1923;
	setAttr ".tgi[0].ni[3].x" 546.79119873046875;
	setAttr ".tgi[0].ni[3].y" -405.06695556640625;
	setAttr ".tgi[0].ni[3].nvs" 2098;
	setAttr ".tgi[0].ni[4].x" 522.85711669921875;
	setAttr ".tgi[0].ni[4].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[4].nvs" 2098;
	setAttr ".tgi[0].ni[5].x" 801.4285888671875;
	setAttr ".tgi[0].ni[5].y" -92.857139587402344;
	setAttr ".tgi[0].ni[5].nvs" 1923;
	setAttr ".tgi[0].ni[6].x" 263.26327514648438;
	setAttr ".tgi[0].ni[6].y" -445.62838745117188;
	setAttr ".tgi[0].ni[6].nvs" 2098;
	setAttr ".tgi[0].ni[7].x" 257.45401000976562;
	setAttr ".tgi[0].ni[7].y" -911.39324951171875;
	setAttr ".tgi[0].ni[7].nvs" 2098;
	setAttr ".tgi[0].ni[8].x" 223.53575134277344;
	setAttr ".tgi[0].ni[8].y" -65.595947265625;
	setAttr ".tgi[0].ni[8].nvs" 2098;
createNode PBRTxyY -n "PBRTxyySample1";
	rename -uid "1C1708B1-2941-38B1-EBBE-8EB362A910CC";
	setAttr ".pre" 9;
createNode PBRTxyY -n "PBRTxyySample2";
	rename -uid "EE138EAF-4A43-AEE8-757C-BDA59EB56A04";
	setAttr ".pre" 16;
createNode PBRTxyY -n "PBRTxyySample3";
	rename -uid "9DC8F17D-BF4D-C70D-8CF9-F0A39023AB23";
	setAttr ".pre" 15;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo9";
	rename -uid "8EA38400-8D48-6A0D-886D-43A2B54A3DE1";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -270.18437842251285 -1213.7551643066945 ;
	setAttr ".tgi[0].vh" -type "double2" 1038.3397555830004 146.51851172163595 ;
	setAttr -s 9 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 289.24456787109375;
	setAttr ".tgi[0].ni[0].y" -862.1558837890625;
	setAttr ".tgi[0].ni[0].nvs" 2098;
	setAttr ".tgi[0].ni[1].x" 561.05084228515625;
	setAttr ".tgi[0].ni[1].y" -499.40277099609375;
	setAttr ".tgi[0].ni[1].nvs" 1923;
	setAttr ".tgi[0].ni[2].x" 567.81597900390625;
	setAttr ".tgi[0].ni[2].y" -949.29876708984375;
	setAttr ".tgi[0].ni[2].nvs" 1923;
	setAttr ".tgi[0].ni[3].x" 282.47943115234375;
	setAttr ".tgi[0].ni[3].y" -412.25991821289062;
	setAttr ".tgi[0].ni[3].nvs" 2098;
	setAttr ".tgi[0].ni[4].x" 278.57144165039062;
	setAttr ".tgi[0].ni[4].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[4].nvs" 2098;
	setAttr ".tgi[0].ni[5].x" 557.14288330078125;
	setAttr ".tgi[0].ni[5].y" -92.857139587402344;
	setAttr ".tgi[0].ni[5].nvs" 1923;
	setAttr ".tgi[0].ni[6].x" 17.568376541137695;
	setAttr ".tgi[0].ni[6].y" -749.75238037109375;
	setAttr ".tgi[0].ni[6].nvs" 2098;
	setAttr ".tgi[0].ni[7].x" 3.8153998851776123;
	setAttr ".tgi[0].ni[7].y" 89.546363830566406;
	setAttr ".tgi[0].ni[7].nvs" 2098;
	setAttr ".tgi[0].ni[8].x" 7.7421441078186035;
	setAttr ".tgi[0].ni[8].y" -312.16937255859375;
	setAttr ".tgi[0].ni[8].nvs" 2098;
createNode polyPlane -n "polyPlane1";
	rename -uid "33D977E3-CF42-874C-C5F4-5E9EB38A9E88";
	setAttr ".cuv" 2;
createNode PBRTUberMaterial -n "pbrt_macbeth1";
	rename -uid "67A75A36-E84E-0DED-BD3B-1295B85C6125";
createNode shadingEngine -n "PBRTUberMaterial5SG";
	rename -uid "0C997D39-5043-1287-FD1D-D1986015D02A";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo8";
	rename -uid "66722071-F747-EEAE-16CC-9CBC0D38A019";
createNode PBRTUberMaterial -n "pbrt_macbeth3";
	rename -uid "3072E9EB-1D4D-ECDB-5038-50BC5EC9E164";
createNode shadingEngine -n "PBRTUberMaterial6SG";
	rename -uid "1CE75F39-0747-3E5F-34DA-CD9BA85D28B6";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo9";
	rename -uid "487A97E0-9C43-3110-D1EF-DCA6CF446E23";
createNode PBRTUberMaterial -n "pbrt_macbeth2";
	rename -uid "7713DF04-EC43-7322-A7CE-C589A04F30BA";
createNode shadingEngine -n "PBRTUberMaterial7SG";
	rename -uid "E2DD7D2F-9C44-2A85-33C3-84AEE38E6B73";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo10";
	rename -uid "D2ED8461-3B43-32A5-186C-C1B748A99572";
createNode PBRTUberMaterial -n "pbrt_macbeth4";
	rename -uid "3193DE29-0446-24C1-DAAF-DFB09EBB55B5";
createNode shadingEngine -n "PBRTUberMaterial8SG";
	rename -uid "D3A9C21D-1144-D231-6C57-1A96C1AFE8D2";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo11";
	rename -uid "ABE988CD-6242-C55C-EE11-A5828DAF08C1";
createNode PBRTUberMaterial -n "pbrt_macbeth5";
	rename -uid "EA03288B-AC4B-CDDF-EF8A-4885ABAD5BEE";
createNode shadingEngine -n "PBRTUberMaterial9SG";
	rename -uid "01F102D9-8246-FB5D-EEF6-489E5174223F";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo12";
	rename -uid "1D3D6F9A-254B-AD54-1B3F-358124E570FF";
createNode PBRTUberMaterial -n "pbrt_macbeth6";
	rename -uid "5C4CEB9E-B34E-E733-D6A3-E9ADA86ACE0E";
createNode shadingEngine -n "PBRTUberMaterial10SG";
	rename -uid "C7C769B4-CC46-AD85-15BF-80A1BCE050A0";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo13";
	rename -uid "65E126B3-D647-BC81-E43C-70B52DBBE259";
createNode PBRTUberMaterial -n "pbrt_macbeth7";
	rename -uid "EBBBA8DA-BE4E-3CCC-5F6D-959AC36D61E5";
createNode shadingEngine -n "PBRTUberMaterial11SG";
	rename -uid "E659F747-C643-7214-F513-6AAAC400D600";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo14";
	rename -uid "AE747B17-5140-FA58-EDFC-BF88D0B83205";
createNode PBRTUberMaterial -n "pbrt_macbeth8";
	rename -uid "9A83211F-444C-6E01-D188-C88CB9805A74";
createNode shadingEngine -n "PBRTUberMaterial12SG";
	rename -uid "69953CD7-2740-4F24-95C6-A5B01DD84D44";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo15";
	rename -uid "07FFA5F2-5E46-C6E3-26D1-B0898284BD8F";
createNode PBRTUberMaterial -n "pbrt_macbeth9";
	rename -uid "08F4694F-1948-1D97-783D-0F95D19706ED";
createNode shadingEngine -n "PBRTUberMaterial13SG";
	rename -uid "D061B856-3446-D01A-40C2-A886B90B2000";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo16";
	rename -uid "6B188CAA-0140-57F6-BBFE-5A886BB589EA";
createNode PBRTUberMaterial -n "pbrt_macbeth10";
	rename -uid "6C6F9014-054B-62FD-F679-A28AB69E29F5";
createNode shadingEngine -n "PBRTUberMaterial14SG";
	rename -uid "C6E558B5-204A-8FCD-A64D-54ADD8E0F816";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo17";
	rename -uid "BFAB88DF-2F4A-7821-D622-21B6E26176B7";
createNode PBRTUberMaterial -n "pbrt_macbeth11";
	rename -uid "C4D44E44-A842-FBA6-6CBC-47B532D57A8F";
createNode shadingEngine -n "PBRTUberMaterial15SG";
	rename -uid "C297C835-0246-DEF1-9848-BB90E79A82E8";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo18";
	rename -uid "69B90645-AC4A-804F-2E98-FEBDCDAD8912";
createNode PBRTUberMaterial -n "pbrt_macbeth12";
	rename -uid "6206987F-0B48-1133-F520-E8B7DCCFA308";
createNode shadingEngine -n "PBRTUberMaterial16SG";
	rename -uid "CA52AC44-634F-0688-1EF4-5BAD8D6AC9FA";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo19";
	rename -uid "F70E3900-6240-6B7D-C190-A9BA43097E5B";
createNode PBRTUberMaterial -n "pbrt_macbeth13";
	rename -uid "DF6235E6-0449-8CC2-B2E9-6A9B93F8993D";
createNode shadingEngine -n "PBRTUberMaterial17SG";
	rename -uid "D04F9C5D-D540-3FD1-D35B-8CB70C654B31";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo20";
	rename -uid "43D2C7EF-414C-6038-8060-19A89B7C44BB";
createNode PBRTUberMaterial -n "pbrt_macbeth14";
	rename -uid "E17ADEF1-6546-00CE-810B-34AFC417B383";
createNode shadingEngine -n "PBRTUberMaterial18SG";
	rename -uid "E94493B9-8B4D-DF5B-4FFC-9DA2074C3DC2";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo21";
	rename -uid "D2CD4C97-E849-6BD4-B4E9-17BBCE966285";
createNode PBRTUberMaterial -n "pbrt_macbeth15";
	rename -uid "1C115FD3-454D-53FF-5EC1-EEA1E52E206B";
createNode shadingEngine -n "PBRTUberMaterial19SG";
	rename -uid "9E0D580E-3544-2ACE-9796-88982A090A7B";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo22";
	rename -uid "EF746ED7-C040-DB70-335E-94A74E658DB7";
createNode PBRTUberMaterial -n "pbrt_macbeth16";
	rename -uid "CEB407BD-0D40-F7DB-1838-0C8C6C44FA98";
createNode shadingEngine -n "PBRTUberMaterial20SG";
	rename -uid "96230762-3D48-344E-7971-24BF9BAE25C5";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo23";
	rename -uid "83CD7899-2045-CE73-6B82-4C9F1C7EACB3";
createNode PBRTUberMaterial -n "pbrt_macbeth17";
	rename -uid "1F727C13-4B46-0407-5DA7-B0A565BF7E08";
createNode shadingEngine -n "PBRTUberMaterial21SG";
	rename -uid "79B25330-5940-7267-B038-A89A45F9FB24";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo24";
	rename -uid "2B90F822-EE44-C27F-46F7-9C9333C8ADE4";
createNode PBRTUberMaterial -n "pbrt_macbeth18";
	rename -uid "C3A21F53-A34F-1CB7-3FB3-A6887CAFA3B3";
createNode shadingEngine -n "PBRTUberMaterial22SG";
	rename -uid "BDC11110-7447-1022-D7AD-2EAA006591D2";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo25";
	rename -uid "8F4C2340-4743-BF06-2201-50BDB8AD7051";
createNode PBRTUberMaterial -n "pbrt_macbeth19";
	rename -uid "2EEC7767-E54A-766B-AD7F-0494888489A1";
createNode shadingEngine -n "PBRTUberMaterial23SG";
	rename -uid "5C3B5ED8-0C40-7150-460F-2498F83759FA";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo26";
	rename -uid "B65FAED4-1546-6FD4-9CB7-E4A9CB7AEDFC";
createNode PBRTUberMaterial -n "pbrt_macbeth20";
	rename -uid "D004BE54-F84B-E6BA-B065-07A97FD987E4";
createNode shadingEngine -n "PBRTUberMaterial24SG";
	rename -uid "F38B923B-F440-43DC-AB50-6A9A78D73893";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo27";
	rename -uid "74B09B14-E841-D04C-BBAD-9EAF73A7010C";
createNode PBRTUberMaterial -n "pbrt_macbeth21";
	rename -uid "C383B0DA-BB4F-1F39-2313-10A7B56FD866";
createNode shadingEngine -n "PBRTUberMaterial25SG";
	rename -uid "782A80C8-D347-352C-1558-E89959FA73CF";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo28";
	rename -uid "FC6F9AB9-3E42-302D-99A2-339003BCB873";
createNode PBRTUberMaterial -n "pbrt_macbeth22";
	rename -uid "43CBF0E8-734A-876E-E005-A386412A63BB";
createNode shadingEngine -n "PBRTUberMaterial26SG";
	rename -uid "5D1677FC-224A-7476-3A9A-23A80DFF05BB";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo29";
	rename -uid "F77B8CA9-854B-ADEB-763D-8A8B0BF9121C";
createNode PBRTUberMaterial -n "pbrt_macbeth23";
	rename -uid "0A12B313-ED4E-F42B-6AB2-49AF2C16B8EE";
createNode shadingEngine -n "PBRTUberMaterial27SG";
	rename -uid "A0219F72-7E40-E01E-8D33-D393DB9FB95C";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo30";
	rename -uid "96FB8BC3-BD4D-77F9-292B-57A512888AA5";
createNode PBRTUberMaterial -n "pbrt_macbeth24";
	rename -uid "4C86E53A-B54B-9C68-F186-D59C6A047079";
createNode shadingEngine -n "PBRTUberMaterial28SG";
	rename -uid "735D530C-4648-3B63-C6DE-14AE39CAE5FB";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo31";
	rename -uid "B1EE6E11-B844-8424-99F2-39B70C658C5B";
createNode PBRTUberMaterial -n "pbrt_macbeth_backing";
	rename -uid "53D277D3-4344-8AB2-1522-8EA65BD763EB";
	setAttr ".kd" -type "float3" 0.0099999998 0.0099999998 0.0099999998 ;
createNode shadingEngine -n "PBRTUberMaterial29SG";
	rename -uid "341FAD0F-4A4B-1623-6B8D-83BA483CFE61";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo32";
	rename -uid "3EEF4665-F04D-CF71-A941-C8847F8C6D57";
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo10";
	rename -uid "8705E85C-3740-583F-B8DD-1FACB26A8FFB";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -833.24977338005488 -1727.2833953310901 ;
	setAttr ".tgi[0].vh" -type "double2" 1779.2339240092979 988.51886636179586 ;
	setAttr -s 50 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 784.765625;
	setAttr ".tgi[0].ni[0].y" 262.15924072265625;
	setAttr ".tgi[0].ni[0].nvs" 2098;
	setAttr ".tgi[0].ni[1].x" 1061.1455078125;
	setAttr ".tgi[0].ni[1].y" 159.67532348632812;
	setAttr ".tgi[0].ni[1].nvs" 1923;
	setAttr ".tgi[0].ni[2].x" 797.91510009765625;
	setAttr ".tgi[0].ni[2].y" -472.215087890625;
	setAttr ".tgi[0].ni[2].nvs" 2098;
	setAttr ".tgi[0].ni[3].x" 1076.486572265625;
	setAttr ".tgi[0].ni[3].y" -567.92938232421875;
	setAttr ".tgi[0].ni[3].nvs" 1923;
	setAttr ".tgi[0].ni[4].x" 793.53192138671875;
	setAttr ".tgi[0].ni[4].y" -121.36731719970703;
	setAttr ".tgi[0].ni[4].nvs" 2098;
	setAttr ".tgi[0].ni[5].x" 1072.1033935546875;
	setAttr ".tgi[0].ni[5].y" -208.51017761230469;
	setAttr ".tgi[0].ni[5].nvs" 1923;
	setAttr ".tgi[0].ni[6].x" -559.44366455078125;
	setAttr ".tgi[0].ni[6].y" -273.3502197265625;
	setAttr ".tgi[0].ni[6].nvs" 2098;
	setAttr ".tgi[0].ni[7].x" -280.8721923828125;
	setAttr ".tgi[0].ni[7].y" -364.77877807617188;
	setAttr ".tgi[0].ni[7].nvs" 1923;
	setAttr ".tgi[0].ni[8].x" -815.590576171875;
	setAttr ".tgi[0].ni[8].y" -348.51983642578125;
	setAttr ".tgi[0].ni[8].nvs" 2098;
	setAttr ".tgi[0].ni[9].x" -280.8721923828125;
	setAttr ".tgi[0].ni[9].y" -369.06448364257812;
	setAttr ".tgi[0].ni[9].nvs" 1923;
	setAttr ".tgi[0].ni[10].x" -564.56658935546875;
	setAttr ".tgi[0].ni[10].y" 111.52684783935547;
	setAttr ".tgi[0].ni[10].nvs" 2130;
	setAttr ".tgi[0].ni[11].x" -280.8721923828125;
	setAttr ".tgi[0].ni[11].y" 25.221216201782227;
	setAttr ".tgi[0].ni[11].nvs" 1923;
	setAttr ".tgi[0].ni[12].x" 35.462078094482422;
	setAttr ".tgi[0].ni[12].y" 401.45651245117188;
	setAttr ".tgi[0].ni[12].nvs" 2098;
	setAttr ".tgi[0].ni[13].x" -280.8721923828125;
	setAttr ".tgi[0].ni[13].y" 29.506931304931641;
	setAttr ".tgi[0].ni[13].nvs" 1923;
	setAttr ".tgi[0].ni[14].x" -220.68484497070312;
	setAttr ".tgi[0].ni[14].y" 432.19415283203125;
	setAttr ".tgi[0].ni[14].nvs" 2098;
	setAttr ".tgi[0].ni[15].x" -280.8721923828125;
	setAttr ".tgi[0].ni[15].y" 25.221216201782227;
	setAttr ".tgi[0].ni[15].nvs" 1923;
	setAttr ".tgi[0].ni[16].x" -823.27496337890625;
	setAttr ".tgi[0].ni[16].y" 39.847576141357422;
	setAttr ".tgi[0].ni[16].nvs" 2098;
	setAttr ".tgi[0].ni[17].x" -280.8721923828125;
	setAttr ".tgi[0].ni[17].y" 20.935503005981445;
	setAttr ".tgi[0].ni[17].nvs" 1923;
	setAttr ".tgi[0].ni[18].x" 1133.0128173828125;
	setAttr ".tgi[0].ni[18].y" -1485.9794921875;
	setAttr ".tgi[0].ni[18].nvs" 2098;
	setAttr ".tgi[0].ni[19].x" 1431.2640380859375;
	setAttr ".tgi[0].ni[19].y" -1022.0900268554688;
	setAttr ".tgi[0].ni[19].nvs" 1923;
	setAttr ".tgi[0].ni[20].x" 26.028228759765625;
	setAttr ".tgi[0].ni[20].y" -1141.584228515625;
	setAttr ".tgi[0].ni[20].nvs" 2098;
	setAttr ".tgi[0].ni[21].x" -325.15158081054688;
	setAttr ".tgi[0].ni[21].y" -23.343883514404297;
	setAttr ".tgi[0].ni[21].nvs" 1923;
	setAttr ".tgi[0].ni[22].x" -249.48794555664062;
	setAttr ".tgi[0].ni[22].y" -1004.677490234375;
	setAttr ".tgi[0].ni[22].nvs" 2098;
	setAttr ".tgi[0].ni[23].x" -325.15158081054688;
	setAttr ".tgi[0].ni[23].y" -427.62960815429688;
	setAttr ".tgi[0].ni[23].nvs" 1923;
	setAttr ".tgi[0].ni[24].x" -564.36358642578125;
	setAttr ".tgi[0].ni[24].y" -786.93206787109375;
	setAttr ".tgi[0].ni[24].nvs" 2098;
	setAttr ".tgi[0].ni[25].x" -325.15158081054688;
	setAttr ".tgi[0].ni[25].y" -440.48672485351562;
	setAttr ".tgi[0].ni[25].nvs" 1923;
	setAttr ".tgi[0].ni[26].x" 493.42172241210938;
	setAttr ".tgi[0].ni[26].y" -1107.99609375;
	setAttr ".tgi[0].ni[26].nvs" 2098;
	setAttr ".tgi[0].ni[27].x" -325.15158081054688;
	setAttr ".tgi[0].ni[27].y" -436.20101928710938;
	setAttr ".tgi[0].ni[27].nvs" 1923;
	setAttr ".tgi[0].ni[28].x" 747.19537353515625;
	setAttr ".tgi[0].ni[28].y" -1141.1671142578125;
	setAttr ".tgi[0].ni[28].nvs" 2098;
	setAttr ".tgi[0].ni[29].x" 1291.443115234375;
	setAttr ".tgi[0].ni[29].y" -888.834716796875;
	setAttr ".tgi[0].ni[29].nvs" 1923;
	setAttr ".tgi[0].ni[30].x" 1012.8717041015625;
	setAttr ".tgi[0].ni[30].y" -1146.0870361328125;
	setAttr ".tgi[0].ni[30].nvs" 2098;
	setAttr ".tgi[0].ni[31].x" 1291.443115234375;
	setAttr ".tgi[0].ni[31].y" -888.834716796875;
	setAttr ".tgi[0].ni[31].nvs" 1923;
	setAttr ".tgi[0].ni[32].x" 1319.97021484375;
	setAttr ".tgi[0].ni[32].y" -1250.7247314453125;
	setAttr ".tgi[0].ni[32].nvs" 2098;
	setAttr ".tgi[0].ni[33].x" 1416.504150390625;
	setAttr ".tgi[0].ni[33].y" -741.921630859375;
	setAttr ".tgi[0].ni[33].nvs" 1923;
	setAttr ".tgi[0].ni[34].x" 161.72352600097656;
	setAttr ".tgi[0].ni[34].y" -1511.430419921875;
	setAttr ".tgi[0].ni[34].nvs" 2098;
	setAttr ".tgi[0].ni[35].x" 440.29495239257812;
	setAttr ".tgi[0].ni[35].y" -1607.144775390625;
	setAttr ".tgi[0].ni[35].nvs" 1923;
	setAttr ".tgi[0].ni[36].x" 4.2857141494750977;
	setAttr ".tgi[0].ni[36].y" -414.28570556640625;
	setAttr ".tgi[0].ni[36].nvs" 2098;
	setAttr ".tgi[0].ni[37].x" 282.85714721679688;
	setAttr ".tgi[0].ni[37].y" -505.71429443359375;
	setAttr ".tgi[0].ni[37].nvs" 1923;
	setAttr ".tgi[0].ni[38].x" 471.67922973632812;
	setAttr ".tgi[0].ni[38].y" -139.18666076660156;
	setAttr ".tgi[0].ni[38].nvs" 2098;
	setAttr ".tgi[0].ni[39].x" -263.25527954101562;
	setAttr ".tgi[0].ni[39].y" -1421.8729248046875;
	setAttr ".tgi[0].ni[39].nvs" 1923;
	setAttr ".tgi[0].ni[40].x" -541.82672119140625;
	setAttr ".tgi[0].ni[40].y" -1334.7301025390625;
	setAttr ".tgi[0].ni[40].nvs" 2098;
	setAttr ".tgi[0].ni[41].x" -263.25527954101562;
	setAttr ".tgi[0].ni[41].y" -1421.8729248046875;
	setAttr ".tgi[0].ni[41].nvs" 1923;
	setAttr ".tgi[0].ni[42].x" 78.084686279296875;
	setAttr ".tgi[0].ni[42].y" 28.091018676757812;
	setAttr ".tgi[0].ni[42].nvs" 2098;
	setAttr ".tgi[0].ni[43].x" 282.85714721679688;
	setAttr ".tgi[0].ni[43].y" -97.142860412597656;
	setAttr ".tgi[0].ni[43].nvs" 1923;
	setAttr ".tgi[0].ni[44].x" 215.8427734375;
	setAttr ".tgi[0].ni[44].y" -616.4200439453125;
	setAttr ".tgi[0].ni[44].nvs" 2098;
	setAttr ".tgi[0].ni[45].x" 282.85714721679688;
	setAttr ".tgi[0].ni[45].y" -92.857139587402344;
	setAttr ".tgi[0].ni[45].nvs" 1923;
	setAttr ".tgi[0].ni[46].x" 474.93893432617188;
	setAttr ".tgi[0].ni[46].y" 352.8065185546875;
	setAttr ".tgi[0].ni[46].nvs" 2098;
	setAttr ".tgi[0].ni[47].x" 881.4285888671875;
	setAttr ".tgi[0].ni[47].y" -88.571426391601562;
	setAttr ".tgi[0].ni[47].nvs" 1923;
	setAttr ".tgi[0].ni[48].x" 600;
	setAttr ".tgi[0].ni[48].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[48].nvs" 2098;
	setAttr ".tgi[0].ni[49].x" 878.5714111328125;
	setAttr ".tgi[0].ni[49].y" -97.142860412597656;
	setAttr ".tgi[0].ni[49].nvs" 1923;
createNode PBRTxyY -n "PBRTxyy1";
	rename -uid "66FD81E7-4343-FAAE-51DE-7E8ADDF38FC6";
	setAttr ".pre" 5;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo11";
	rename -uid "95082F8E-EE4A-7227-EC65-0DB42ED9F01A";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -15.857918624521334 -615.476166019365 ;
	setAttr ".tgi[0].vh" -type "double2" 687.28646337291946 115.47618588757912 ;
createNode PBRTxyY -n "PBRTxyy2";
	rename -uid "8DAD87FD-5D4E-D7C3-C390-DC963642DCA5";
	setAttr ".pre" 6;
createNode PBRTxyY -n "PBRTxyy3";
	rename -uid "72547802-3C48-70F9-AC23-849925B47814";
	setAttr ".pre" 7;
createNode PBRTxyY -n "PBRTxyy4";
	rename -uid "ABE13C0B-074D-1411-9700-EEB3BF3D3461";
	setAttr ".pre" 8;
createNode PBRTxyY -n "PBRTxyy5";
	rename -uid "AAFA66B9-AE4D-1655-DBA5-D59A2FA9E163";
	setAttr ".pre" 9;
createNode PBRTxyY -n "PBRTxyy6";
	rename -uid "ABA859FB-2942-95AD-F2F2-BD92D6F51CC0";
	setAttr ".pre" 10;
createNode PBRTxyY -n "PBRTxyy7";
	rename -uid "530EFF1D-A54E-76B4-5ACF-B4B1E325661A";
	setAttr ".pre" 11;
createNode PBRTxyY -n "PBRTxyy8";
	rename -uid "DFD1D375-7D4A-D45C-7319-718E71AB34B7";
	setAttr ".pre" 12;
createNode PBRTxyY -n "PBRTxyy9";
	rename -uid "2ADF417A-F345-F8B0-EE7D-8DA3D915536E";
	setAttr ".pre" 13;
createNode PBRTxyY -n "PBRTxyy10";
	rename -uid "8F28EDC9-904A-534D-0C54-E5B4EC791947";
	setAttr ".pre" 14;
createNode PBRTxyY -n "PBRTxyy11";
	rename -uid "780C5572-9E47-19CA-414F-7BA9470DE972";
	setAttr ".pre" 15;
createNode PBRTxyY -n "PBRTxyy12";
	rename -uid "4F300E72-4D47-5BE4-9702-AFA8FF674DF7";
	setAttr ".pre" 16;
createNode PBRTxyY -n "PBRTxyy13";
	rename -uid "A7CF960E-BF4B-3965-543F-9181F82CFA4C";
	setAttr ".pre" 17;
createNode PBRTxyY -n "PBRTxyy14";
	rename -uid "FCD3B80B-364F-0F42-62B9-878F5F30699A";
	setAttr ".pre" 18;
createNode PBRTxyY -n "PBRTxyy15";
	rename -uid "AC67A5EC-824B-A123-A92B-729E36E41BEE";
	setAttr ".pre" 19;
createNode PBRTxyY -n "PBRTxyy16";
	rename -uid "46C5C68C-3048-5C08-948A-6BB2B782E216";
	setAttr ".pre" 20;
createNode PBRTxyY -n "PBRTxyy17";
	rename -uid "CF067DAF-7C4D-A522-18ED-128B81D86B10";
	setAttr ".pre" 21;
createNode PBRTxyY -n "PBRTxyy18";
	rename -uid "20D02CE8-C04E-4E69-A6DC-D9B2A1552957";
	setAttr ".pre" 22;
createNode PBRTxyY -n "PBRTxyy19";
	rename -uid "03955D4C-E24F-AEFF-756E-048AF9183226";
	setAttr ".pre" 23;
createNode PBRTxyY -n "PBRTxyy20";
	rename -uid "6875B9E3-E040-C91E-F248-68B5AD2539DB";
	setAttr ".pre" 24;
createNode PBRTxyY -n "PBRTxyy21";
	rename -uid "D2285FC4-2746-5D5F-F9F9-2E821D8BB983";
	setAttr ".pre" 25;
createNode PBRTxyY -n "PBRTxyy22";
	rename -uid "F5C6370E-4847-DC6A-0B5E-85B52C136573";
	setAttr ".pre" 26;
createNode PBRTxyY -n "PBRTxyy23";
	rename -uid "07373500-9149-21D8-83D7-20896C997F81";
	setAttr ".pre" 27;
createNode PBRTxyY -n "PBRTxyy24";
	rename -uid "864DDC4C-7843-14E7-510D-34A52D9B66E3";
	setAttr ".pre" 28;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 34 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 36 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 30 ".u";
select -ne :defaultRenderingList1;
	setAttr -s 2 ".r";
select -ne :lightList1;
select -ne :defaultTextureList1;
	setAttr -s 2 ".tx";
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".ren" -type "string" "PBRT";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :defaultLightSet;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
connectAttr "pbrt_feature_demo_baseRN.phl[1]" "PBRTUberMaterial4SG.dsm" -na;
connectAttr "pbrt_feature_demo_baseRN.phl[2]" "PBRTUberMaterial3SG.dsm" -na;
connectAttr "pbrt_feature_demo_baseRN.phl[3]" "PBRTUberMaterial2SG.dsm" -na;
connectAttr "polyPlane1.out" "|MacbethChart|macbethChip24|macbethChipShape1.i";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial3SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial4SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial5SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial6SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial7SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial8SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial9SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial10SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial11SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial12SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial13SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial14SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial15SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial16SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial17SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial18SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial19SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial20SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial21SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial22SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial23SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial24SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial25SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial26SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial27SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial28SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "PBRTUberMaterial29SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial3SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial4SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial5SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial6SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial7SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial8SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial9SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial10SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial11SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial12SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial13SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial14SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial15SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial16SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial17SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial18SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial19SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial20SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial21SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial22SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial23SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial24SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial25SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial26SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial27SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial28SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "PBRTUberMaterial29SG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "PBRTxyySample3.oc" "pbrt_uber1.kd";
connectAttr "pbrt_uber1.oc" "PBRTUberMaterial2SG.ss";
connectAttr "PBRTUberMaterial2SG.msg" "materialInfo4.sg";
connectAttr "pbrt_uber1.msg" "materialInfo4.m";
connectAttr "pbrt_uber1.msg" "materialInfo4.t" -na;
connectAttr "pbrt_uber1.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo1.tgi[0].ni[0].dn"
		;
connectAttr "PBRTUberMaterial2SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo1.tgi[0].ni[1].dn"
		;
connectAttr "pbrt_uber1.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo2.tgi[0].ni[0].dn"
		;
connectAttr "PBRTUberMaterial2SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo2.tgi[0].ni[1].dn"
		;
connectAttr "place2dTexture2.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo2.tgi[0].ni[3].dn"
		;
connectAttr "pbrt_uber1.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo3.tgi[0].ni[0].dn"
		;
connectAttr "PBRTUberMaterial2SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo3.tgi[0].ni[1].dn"
		;
connectAttr "pbrt_uber1.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo4.tgi[0].ni[0].dn"
		;
connectAttr "PBRTUberMaterial2SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo4.tgi[0].ni[1].dn"
		;
connectAttr "pbrt_uber1.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo5.tgi[0].ni[0].dn"
		;
connectAttr "PBRTUberMaterial2SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo5.tgi[0].ni[1].dn"
		;
connectAttr "PBRTxyySample2.oc" "pbrt_uber2.kd";
connectAttr "pbrt_uber2.oc" "PBRTUberMaterial3SG.ss";
connectAttr "PBRTUberMaterial3SG.msg" "materialInfo5.sg";
connectAttr "pbrt_uber2.msg" "materialInfo5.m";
connectAttr "pbrt_uber2.msg" "materialInfo5.t" -na;
connectAttr "PBRTxyySample1.oc" "pbrt_uber3.kd";
connectAttr "pbrt_uber3.oc" "PBRTUberMaterial4SG.ss";
connectAttr "PBRTUberMaterial4SG.msg" "materialInfo6.sg";
connectAttr "pbrt_uber3.msg" "materialInfo6.m";
connectAttr "pbrt_uber3.msg" "materialInfo6.t" -na;
connectAttr "pbrt_uber3.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo6.tgi[0].ni[0].dn"
		;
connectAttr "PBRTUberMaterial2SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo6.tgi[0].ni[2].dn"
		;
connectAttr "PBRTUberMaterial4SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo6.tgi[0].ni[5].dn"
		;
connectAttr "pbrt_uber1.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo6.tgi[0].ni[6].dn"
		;
connectAttr "pbrt_uber2.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo6.tgi[0].ni[7].dn"
		;
connectAttr "PBRTUberMaterial3SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo6.tgi[0].ni[10].dn"
		;
connectAttr "pbrt_uber3.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo7.tgi[0].ni[0].dn"
		;
connectAttr "PBRTUberMaterial2SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo7.tgi[0].ni[1].dn"
		;
connectAttr "PBRTUberMaterial4SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo7.tgi[0].ni[2].dn"
		;
connectAttr "pbrt_uber1.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo7.tgi[0].ni[3].dn"
		;
connectAttr "pbrt_uber2.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo7.tgi[0].ni[4].dn"
		;
connectAttr "PBRTUberMaterial3SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo7.tgi[0].ni[5].dn"
		;
connectAttr "pbrt_uber3.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo8.tgi[0].ni[0].dn"
		;
connectAttr "PBRTUberMaterial2SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo8.tgi[0].ni[1].dn"
		;
connectAttr "PBRTUberMaterial4SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo8.tgi[0].ni[2].dn"
		;
connectAttr "pbrt_uber1.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo8.tgi[0].ni[3].dn"
		;
connectAttr "pbrt_uber2.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo8.tgi[0].ni[4].dn"
		;
connectAttr "PBRTUberMaterial3SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo8.tgi[0].ni[5].dn"
		;
connectAttr "pbrt_uber3.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo9.tgi[0].ni[0].dn"
		;
connectAttr "PBRTUberMaterial2SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo9.tgi[0].ni[1].dn"
		;
connectAttr "PBRTUberMaterial4SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo9.tgi[0].ni[2].dn"
		;
connectAttr "pbrt_uber1.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo9.tgi[0].ni[3].dn"
		;
connectAttr "pbrt_uber2.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo9.tgi[0].ni[4].dn"
		;
connectAttr "PBRTUberMaterial3SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo9.tgi[0].ni[5].dn"
		;
connectAttr "PBRTxyySample1.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo9.tgi[0].ni[6].dn"
		;
connectAttr "PBRTxyySample2.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo9.tgi[0].ni[7].dn"
		;
connectAttr "PBRTxyySample3.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo9.tgi[0].ni[8].dn"
		;
connectAttr "PBRTxyy1.oc" "pbrt_macbeth1.kd";
connectAttr "pbrt_macbeth1.oc" "PBRTUberMaterial5SG.ss";
connectAttr "|MacbethChart|macbethChip1|macbethChipShape1.iog" "PBRTUberMaterial5SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial5SG.msg" "materialInfo8.sg";
connectAttr "pbrt_macbeth1.msg" "materialInfo8.m";
connectAttr "pbrt_macbeth1.msg" "materialInfo8.t" -na;
connectAttr "PBRTxyy3.oc" "pbrt_macbeth3.kd";
connectAttr "pbrt_macbeth3.oc" "PBRTUberMaterial6SG.ss";
connectAttr "|MacbethChart|macbethChip3|macbethChipShape1.iog" "PBRTUberMaterial6SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial6SG.msg" "materialInfo9.sg";
connectAttr "pbrt_macbeth3.msg" "materialInfo9.m";
connectAttr "pbrt_macbeth3.msg" "materialInfo9.t" -na;
connectAttr "PBRTxyy2.oc" "pbrt_macbeth2.kd";
connectAttr "pbrt_macbeth2.oc" "PBRTUberMaterial7SG.ss";
connectAttr "|MacbethChart|macbethChip2|macbethChipShape1.iog" "PBRTUberMaterial7SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial7SG.msg" "materialInfo10.sg";
connectAttr "pbrt_macbeth2.msg" "materialInfo10.m";
connectAttr "pbrt_macbeth2.msg" "materialInfo10.t" -na;
connectAttr "PBRTxyy4.oc" "pbrt_macbeth4.kd";
connectAttr "pbrt_macbeth4.oc" "PBRTUberMaterial8SG.ss";
connectAttr "|MacbethChart|macbethChip4|macbethChipShape1.iog" "PBRTUberMaterial8SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial8SG.msg" "materialInfo11.sg";
connectAttr "pbrt_macbeth4.msg" "materialInfo11.m";
connectAttr "pbrt_macbeth4.msg" "materialInfo11.t" -na;
connectAttr "PBRTxyy5.oc" "pbrt_macbeth5.kd";
connectAttr "pbrt_macbeth5.oc" "PBRTUberMaterial9SG.ss";
connectAttr "|MacbethChart|macbethChip5|macbethChipShape1.iog" "PBRTUberMaterial9SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial9SG.msg" "materialInfo12.sg";
connectAttr "pbrt_macbeth5.msg" "materialInfo12.m";
connectAttr "pbrt_macbeth5.msg" "materialInfo12.t" -na;
connectAttr "PBRTxyy6.oc" "pbrt_macbeth6.kd";
connectAttr "pbrt_macbeth6.oc" "PBRTUberMaterial10SG.ss";
connectAttr "|MacbethChart|macbethChip6|macbethChipShape1.iog" "PBRTUberMaterial10SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial10SG.msg" "materialInfo13.sg";
connectAttr "pbrt_macbeth6.msg" "materialInfo13.m";
connectAttr "pbrt_macbeth6.msg" "materialInfo13.t" -na;
connectAttr "PBRTxyy7.oc" "pbrt_macbeth7.kd";
connectAttr "pbrt_macbeth7.oc" "PBRTUberMaterial11SG.ss";
connectAttr "|MacbethChart|macbethChip7|macbethChipShape1.iog" "PBRTUberMaterial11SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial11SG.msg" "materialInfo14.sg";
connectAttr "pbrt_macbeth7.msg" "materialInfo14.m";
connectAttr "pbrt_macbeth7.msg" "materialInfo14.t" -na;
connectAttr "PBRTxyy8.oc" "pbrt_macbeth8.kd";
connectAttr "pbrt_macbeth8.oc" "PBRTUberMaterial12SG.ss";
connectAttr "|MacbethChart|macbethChip8|macbethChipShape1.iog" "PBRTUberMaterial12SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial12SG.msg" "materialInfo15.sg";
connectAttr "pbrt_macbeth8.msg" "materialInfo15.m";
connectAttr "pbrt_macbeth8.msg" "materialInfo15.t" -na;
connectAttr "PBRTxyy9.oc" "pbrt_macbeth9.kd";
connectAttr "pbrt_macbeth9.oc" "PBRTUberMaterial13SG.ss";
connectAttr "|MacbethChart|macbethChip9|macbethChipShape1.iog" "PBRTUberMaterial13SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial13SG.msg" "materialInfo16.sg";
connectAttr "pbrt_macbeth9.msg" "materialInfo16.m";
connectAttr "pbrt_macbeth9.msg" "materialInfo16.t" -na;
connectAttr "PBRTxyy10.oc" "pbrt_macbeth10.kd";
connectAttr "pbrt_macbeth10.oc" "PBRTUberMaterial14SG.ss";
connectAttr "|MacbethChart|macbethChip10|macbethChipShape1.iog" "PBRTUberMaterial14SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial14SG.msg" "materialInfo17.sg";
connectAttr "pbrt_macbeth10.msg" "materialInfo17.m";
connectAttr "pbrt_macbeth10.msg" "materialInfo17.t" -na;
connectAttr "PBRTxyy11.oc" "pbrt_macbeth11.kd";
connectAttr "pbrt_macbeth11.oc" "PBRTUberMaterial15SG.ss";
connectAttr "|MacbethChart|macbethChip11|macbethChipShape1.iog" "PBRTUberMaterial15SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial15SG.msg" "materialInfo18.sg";
connectAttr "pbrt_macbeth11.msg" "materialInfo18.m";
connectAttr "pbrt_macbeth11.msg" "materialInfo18.t" -na;
connectAttr "PBRTxyy12.oc" "pbrt_macbeth12.kd";
connectAttr "pbrt_macbeth12.oc" "PBRTUberMaterial16SG.ss";
connectAttr "|MacbethChart|macbethChip12|macbethChipShape1.iog" "PBRTUberMaterial16SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial16SG.msg" "materialInfo19.sg";
connectAttr "pbrt_macbeth12.msg" "materialInfo19.m";
connectAttr "pbrt_macbeth12.msg" "materialInfo19.t" -na;
connectAttr "PBRTxyy13.oc" "pbrt_macbeth13.kd";
connectAttr "pbrt_macbeth13.oc" "PBRTUberMaterial17SG.ss";
connectAttr "|MacbethChart|macbethChip13|macbethChipShape1.iog" "PBRTUberMaterial17SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial17SG.msg" "materialInfo20.sg";
connectAttr "pbrt_macbeth13.msg" "materialInfo20.m";
connectAttr "pbrt_macbeth13.msg" "materialInfo20.t" -na;
connectAttr "PBRTxyy14.oc" "pbrt_macbeth14.kd";
connectAttr "pbrt_macbeth14.oc" "PBRTUberMaterial18SG.ss";
connectAttr "|MacbethChart|macbethChip14|macbethChipShape1.iog" "PBRTUberMaterial18SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial18SG.msg" "materialInfo21.sg";
connectAttr "pbrt_macbeth14.msg" "materialInfo21.m";
connectAttr "pbrt_macbeth14.msg" "materialInfo21.t" -na;
connectAttr "PBRTxyy15.oc" "pbrt_macbeth15.kd";
connectAttr "pbrt_macbeth15.oc" "PBRTUberMaterial19SG.ss";
connectAttr "|MacbethChart|macbethChip15|macbethChipShape1.iog" "PBRTUberMaterial19SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial19SG.msg" "materialInfo22.sg";
connectAttr "pbrt_macbeth15.msg" "materialInfo22.m";
connectAttr "pbrt_macbeth15.msg" "materialInfo22.t" -na;
connectAttr "PBRTxyy16.oc" "pbrt_macbeth16.kd";
connectAttr "pbrt_macbeth16.oc" "PBRTUberMaterial20SG.ss";
connectAttr "|MacbethChart|macbethChip16|macbethChipShape1.iog" "PBRTUberMaterial20SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial20SG.msg" "materialInfo23.sg";
connectAttr "pbrt_macbeth16.msg" "materialInfo23.m";
connectAttr "pbrt_macbeth16.msg" "materialInfo23.t" -na;
connectAttr "PBRTxyy17.oc" "pbrt_macbeth17.kd";
connectAttr "pbrt_macbeth17.oc" "PBRTUberMaterial21SG.ss";
connectAttr "|MacbethChart|macbethChip17|macbethChipShape1.iog" "PBRTUberMaterial21SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial21SG.msg" "materialInfo24.sg";
connectAttr "pbrt_macbeth17.msg" "materialInfo24.m";
connectAttr "pbrt_macbeth17.msg" "materialInfo24.t" -na;
connectAttr "PBRTxyy18.oc" "pbrt_macbeth18.kd";
connectAttr "pbrt_macbeth18.oc" "PBRTUberMaterial22SG.ss";
connectAttr "|MacbethChart|macbethChip18|macbethChipShape1.iog" "PBRTUberMaterial22SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial22SG.msg" "materialInfo25.sg";
connectAttr "pbrt_macbeth18.msg" "materialInfo25.m";
connectAttr "pbrt_macbeth18.msg" "materialInfo25.t" -na;
connectAttr "PBRTxyy19.oc" "pbrt_macbeth19.kd";
connectAttr "pbrt_macbeth19.oc" "PBRTUberMaterial23SG.ss";
connectAttr "|MacbethChart|macbethChip19|macbethChipShape1.iog" "PBRTUberMaterial23SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial23SG.msg" "materialInfo26.sg";
connectAttr "pbrt_macbeth19.msg" "materialInfo26.m";
connectAttr "pbrt_macbeth19.msg" "materialInfo26.t" -na;
connectAttr "PBRTxyy20.oc" "pbrt_macbeth20.kd";
connectAttr "pbrt_macbeth20.oc" "PBRTUberMaterial24SG.ss";
connectAttr "|MacbethChart|macbethChip20|macbethChipShape1.iog" "PBRTUberMaterial24SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial24SG.msg" "materialInfo27.sg";
connectAttr "pbrt_macbeth20.msg" "materialInfo27.m";
connectAttr "pbrt_macbeth20.msg" "materialInfo27.t" -na;
connectAttr "PBRTxyy21.oc" "pbrt_macbeth21.kd";
connectAttr "pbrt_macbeth21.oc" "PBRTUberMaterial25SG.ss";
connectAttr "|MacbethChart|macbethChip21|macbethChipShape1.iog" "PBRTUberMaterial25SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial25SG.msg" "materialInfo28.sg";
connectAttr "pbrt_macbeth21.msg" "materialInfo28.m";
connectAttr "pbrt_macbeth21.msg" "materialInfo28.t" -na;
connectAttr "PBRTxyy22.oc" "pbrt_macbeth22.kd";
connectAttr "pbrt_macbeth22.oc" "PBRTUberMaterial26SG.ss";
connectAttr "|MacbethChart|macbethChip22|macbethChipShape1.iog" "PBRTUberMaterial26SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial26SG.msg" "materialInfo29.sg";
connectAttr "pbrt_macbeth22.msg" "materialInfo29.m";
connectAttr "pbrt_macbeth22.msg" "materialInfo29.t" -na;
connectAttr "PBRTxyy23.oc" "pbrt_macbeth23.kd";
connectAttr "pbrt_macbeth23.oc" "PBRTUberMaterial27SG.ss";
connectAttr "|MacbethChart|macbethChip23|macbethChipShape1.iog" "PBRTUberMaterial27SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial27SG.msg" "materialInfo30.sg";
connectAttr "pbrt_macbeth23.msg" "materialInfo30.m";
connectAttr "pbrt_macbeth23.msg" "materialInfo30.t" -na;
connectAttr "PBRTxyy24.oc" "pbrt_macbeth24.kd";
connectAttr "pbrt_macbeth24.oc" "PBRTUberMaterial28SG.ss";
connectAttr "|MacbethChart|macbethChip24|macbethChipShape1.iog" "PBRTUberMaterial28SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial28SG.msg" "materialInfo31.sg";
connectAttr "pbrt_macbeth24.msg" "materialInfo31.m";
connectAttr "pbrt_macbeth24.msg" "materialInfo31.t" -na;
connectAttr "pbrt_macbeth_backing.oc" "PBRTUberMaterial29SG.ss";
connectAttr "macbethBackingShape.iog" "PBRTUberMaterial29SG.dsm" -na;
connectAttr "PBRTUberMaterial29SG.msg" "materialInfo32.sg";
connectAttr "pbrt_macbeth_backing.msg" "materialInfo32.m";
connectAttr "pbrt_macbeth_backing.msg" "materialInfo32.t" -na;
connectAttr "pbrt_macbeth1.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[0].dn"
		;
connectAttr "PBRTUberMaterial5SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[1].dn"
		;
connectAttr "pbrt_macbeth3.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[2].dn"
		;
connectAttr "PBRTUberMaterial6SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[3].dn"
		;
connectAttr "pbrt_macbeth2.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[4].dn"
		;
connectAttr "PBRTUberMaterial7SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[5].dn"
		;
connectAttr "pbrt_macbeth4.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[6].dn"
		;
connectAttr "PBRTUberMaterial8SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[7].dn"
		;
connectAttr "pbrt_macbeth5.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[8].dn"
		;
connectAttr "PBRTUberMaterial9SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[9].dn"
		;
connectAttr "pbrt_macbeth6.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[10].dn"
		;
connectAttr "PBRTUberMaterial10SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[11].dn"
		;
connectAttr "pbrt_macbeth7.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[12].dn"
		;
connectAttr "PBRTUberMaterial11SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[13].dn"
		;
connectAttr "pbrt_macbeth8.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[14].dn"
		;
connectAttr "PBRTUberMaterial12SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[15].dn"
		;
connectAttr "pbrt_macbeth9.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[16].dn"
		;
connectAttr "PBRTUberMaterial13SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[17].dn"
		;
connectAttr "pbrt_macbeth10.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[18].dn"
		;
connectAttr "PBRTUberMaterial14SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[19].dn"
		;
connectAttr "pbrt_macbeth11.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[20].dn"
		;
connectAttr "PBRTUberMaterial15SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[21].dn"
		;
connectAttr "pbrt_macbeth12.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[22].dn"
		;
connectAttr "PBRTUberMaterial16SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[23].dn"
		;
connectAttr "pbrt_macbeth13.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[24].dn"
		;
connectAttr "PBRTUberMaterial17SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[25].dn"
		;
connectAttr "pbrt_macbeth14.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[26].dn"
		;
connectAttr "PBRTUberMaterial18SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[27].dn"
		;
connectAttr "pbrt_macbeth15.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[28].dn"
		;
connectAttr "PBRTUberMaterial19SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[29].dn"
		;
connectAttr "pbrt_macbeth16.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[30].dn"
		;
connectAttr "PBRTUberMaterial20SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[31].dn"
		;
connectAttr "pbrt_macbeth17.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[32].dn"
		;
connectAttr "PBRTUberMaterial21SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[33].dn"
		;
connectAttr "pbrt_macbeth18.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[34].dn"
		;
connectAttr "PBRTUberMaterial22SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[35].dn"
		;
connectAttr "pbrt_macbeth19.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[36].dn"
		;
connectAttr "PBRTUberMaterial23SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[37].dn"
		;
connectAttr "pbrt_macbeth20.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[38].dn"
		;
connectAttr "PBRTUberMaterial24SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[39].dn"
		;
connectAttr "pbrt_macbeth21.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[40].dn"
		;
connectAttr "PBRTUberMaterial25SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[41].dn"
		;
connectAttr "pbrt_macbeth22.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[42].dn"
		;
connectAttr "PBRTUberMaterial26SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[43].dn"
		;
connectAttr "pbrt_macbeth23.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[44].dn"
		;
connectAttr "PBRTUberMaterial27SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[45].dn"
		;
connectAttr "pbrt_macbeth24.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[46].dn"
		;
connectAttr "PBRTUberMaterial28SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[47].dn"
		;
connectAttr "pbrt_macbeth_backing.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[48].dn"
		;
connectAttr "PBRTUberMaterial29SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo10.tgi[0].ni[49].dn"
		;
connectAttr "PBRTUberMaterial2SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial3SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial4SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial5SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial6SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial7SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial8SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial9SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial10SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial11SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial12SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial13SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial14SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial15SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial16SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial17SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial18SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial19SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial20SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial21SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial22SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial23SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial24SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial25SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial26SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial27SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial28SG.pa" ":renderPartition.st" -na;
connectAttr "PBRTUberMaterial29SG.pa" ":renderPartition.st" -na;
connectAttr "pbrt_uber1.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_uber2.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_uber3.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth1.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth3.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth2.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth4.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth5.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth6.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth7.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth8.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth9.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth10.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth11.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth12.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth13.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth14.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth15.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth16.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth17.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth18.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth19.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth20.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth21.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth22.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth23.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth24.msg" ":defaultShaderList1.s" -na;
connectAttr "pbrt_macbeth_backing.msg" ":defaultShaderList1.s" -na;
connectAttr "place2dTexture2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyySample1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyySample2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyySample3.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy3.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy4.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy5.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy6.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy7.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy8.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy9.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy10.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy11.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy12.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy13.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy14.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy15.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy16.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy17.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy18.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy19.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy20.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy21.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy22.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy23.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "PBRTxyy24.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of pbrt_feature_demo_texture_xyy2.ma
