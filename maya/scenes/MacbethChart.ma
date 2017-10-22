//Maya ASCII 2016 scene
//Name: MacbethChart.ma
//Codeset: UTF-8
requires maya "2016";
requires -nodeType "PBRTUberMaterial" "PBRTForMaya.py" "1.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2016";
fileInfo "version" "2016";
fileInfo "cutIdentifier" "201510022200-973226";
fileInfo "osv" "Mac OS X 10.9.6";
createNode transform -n "MacbethChart";
	rename -uid "185C8B74-FE4C-9823-21F8-3A9F40665B06";
	setAttr ".t" -type "double3" 0 1.3 -4.5 ;
	setAttr ".r" -type "double3" -75.478316681892196 0 0 ;
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
	setAttr -s 24 ".iog";
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
createNode polyPlane -n "polyPlane1";
	rename -uid "33D977E3-CF42-874C-C5F4-5E9EB38A9E88";
	setAttr ".cuv" 2;
createNode materialInfo -n "materialInfo31";
	rename -uid "B1EE6E11-B844-8424-99F2-39B70C658C5B";
createNode shadingEngine -n "PBRTUberMaterial28SG";
	rename -uid "735D530C-4648-3B63-C6DE-14AE39CAE5FB";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth24";
	rename -uid "4C86E53A-B54B-9C68-F186-D59C6A047079";
createNode materialInfo -n "materialInfo30";
	rename -uid "96FB8BC3-BD4D-77F9-292B-57A512888AA5";
createNode shadingEngine -n "PBRTUberMaterial27SG";
	rename -uid "A0219F72-7E40-E01E-8D33-D393DB9FB95C";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth23";
	rename -uid "0A12B313-ED4E-F42B-6AB2-49AF2C16B8EE";
createNode materialInfo -n "materialInfo29";
	rename -uid "F77B8CA9-854B-ADEB-763D-8A8B0BF9121C";
createNode shadingEngine -n "PBRTUberMaterial26SG";
	rename -uid "5D1677FC-224A-7476-3A9A-23A80DFF05BB";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth22";
	rename -uid "43CBF0E8-734A-876E-E005-A386412A63BB";
createNode materialInfo -n "materialInfo28";
	rename -uid "FC6F9AB9-3E42-302D-99A2-339003BCB873";
createNode shadingEngine -n "PBRTUberMaterial25SG";
	rename -uid "782A80C8-D347-352C-1558-E89959FA73CF";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth21";
	rename -uid "C383B0DA-BB4F-1F39-2313-10A7B56FD866";
createNode materialInfo -n "materialInfo27";
	rename -uid "74B09B14-E841-D04C-BBAD-9EAF73A7010C";
createNode shadingEngine -n "PBRTUberMaterial24SG";
	rename -uid "F38B923B-F440-43DC-AB50-6A9A78D73893";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth20";
	rename -uid "D004BE54-F84B-E6BA-B065-07A97FD987E4";
createNode materialInfo -n "materialInfo26";
	rename -uid "B65FAED4-1546-6FD4-9CB7-E4A9CB7AEDFC";
createNode shadingEngine -n "PBRTUberMaterial23SG";
	rename -uid "5C3B5ED8-0C40-7150-460F-2498F83759FA";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth19";
	rename -uid "2EEC7767-E54A-766B-AD7F-0494888489A1";
createNode materialInfo -n "materialInfo25";
	rename -uid "8F4C2340-4743-BF06-2201-50BDB8AD7051";
createNode shadingEngine -n "PBRTUberMaterial22SG";
	rename -uid "BDC11110-7447-1022-D7AD-2EAA006591D2";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth18";
	rename -uid "C3A21F53-A34F-1CB7-3FB3-A6887CAFA3B3";
createNode materialInfo -n "materialInfo24";
	rename -uid "2B90F822-EE44-C27F-46F7-9C9333C8ADE4";
createNode shadingEngine -n "PBRTUberMaterial21SG";
	rename -uid "79B25330-5940-7267-B038-A89A45F9FB24";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth17";
	rename -uid "1F727C13-4B46-0407-5DA7-B0A565BF7E08";
createNode materialInfo -n "materialInfo23";
	rename -uid "83CD7899-2045-CE73-6B82-4C9F1C7EACB3";
createNode shadingEngine -n "PBRTUberMaterial20SG";
	rename -uid "96230762-3D48-344E-7971-24BF9BAE25C5";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth16";
	rename -uid "CEB407BD-0D40-F7DB-1838-0C8C6C44FA98";
createNode materialInfo -n "materialInfo22";
	rename -uid "EF746ED7-C040-DB70-335E-94A74E658DB7";
createNode shadingEngine -n "PBRTUberMaterial19SG";
	rename -uid "9E0D580E-3544-2ACE-9796-88982A090A7B";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth15";
	rename -uid "1C115FD3-454D-53FF-5EC1-EEA1E52E206B";
createNode materialInfo -n "materialInfo21";
	rename -uid "D2CD4C97-E849-6BD4-B4E9-17BBCE966285";
createNode shadingEngine -n "PBRTUberMaterial18SG";
	rename -uid "E94493B9-8B4D-DF5B-4FFC-9DA2074C3DC2";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth14";
	rename -uid "E17ADEF1-6546-00CE-810B-34AFC417B383";
createNode materialInfo -n "materialInfo20";
	rename -uid "43D2C7EF-414C-6038-8060-19A89B7C44BB";
createNode shadingEngine -n "PBRTUberMaterial17SG";
	rename -uid "D04F9C5D-D540-3FD1-D35B-8CB70C654B31";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth13";
	rename -uid "DF6235E6-0449-8CC2-B2E9-6A9B93F8993D";
createNode materialInfo -n "materialInfo19";
	rename -uid "F70E3900-6240-6B7D-C190-A9BA43097E5B";
createNode shadingEngine -n "PBRTUberMaterial16SG";
	rename -uid "CA52AC44-634F-0688-1EF4-5BAD8D6AC9FA";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth12";
	rename -uid "6206987F-0B48-1133-F520-E8B7DCCFA308";
createNode materialInfo -n "materialInfo18";
	rename -uid "69B90645-AC4A-804F-2E98-FEBDCDAD8912";
createNode shadingEngine -n "PBRTUberMaterial15SG";
	rename -uid "C297C835-0246-DEF1-9848-BB90E79A82E8";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth11";
	rename -uid "C4D44E44-A842-FBA6-6CBC-47B532D57A8F";
createNode materialInfo -n "materialInfo17";
	rename -uid "BFAB88DF-2F4A-7821-D622-21B6E26176B7";
createNode shadingEngine -n "PBRTUberMaterial14SG";
	rename -uid "C6E558B5-204A-8FCD-A64D-54ADD8E0F816";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth10";
	rename -uid "6C6F9014-054B-62FD-F679-A28AB69E29F5";
createNode materialInfo -n "materialInfo16";
	rename -uid "6B188CAA-0140-57F6-BBFE-5A886BB589EA";
createNode shadingEngine -n "PBRTUberMaterial13SG";
	rename -uid "D061B856-3446-D01A-40C2-A886B90B2000";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth9";
	rename -uid "08F4694F-1948-1D97-783D-0F95D19706ED";
createNode materialInfo -n "materialInfo15";
	rename -uid "07FFA5F2-5E46-C6E3-26D1-B0898284BD8F";
createNode shadingEngine -n "PBRTUberMaterial12SG";
	rename -uid "69953CD7-2740-4F24-95C6-A5B01DD84D44";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth8";
	rename -uid "9A83211F-444C-6E01-D188-C88CB9805A74";
createNode materialInfo -n "materialInfo14";
	rename -uid "AE747B17-5140-FA58-EDFC-BF88D0B83205";
createNode shadingEngine -n "PBRTUberMaterial11SG";
	rename -uid "E659F747-C643-7214-F513-6AAAC400D600";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth7";
	rename -uid "EBBBA8DA-BE4E-3CCC-5F6D-959AC36D61E5";
createNode materialInfo -n "materialInfo13";
	rename -uid "65E126B3-D647-BC81-E43C-70B52DBBE259";
createNode shadingEngine -n "PBRTUberMaterial10SG";
	rename -uid "C7C769B4-CC46-AD85-15BF-80A1BCE050A0";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth6";
	rename -uid "5C4CEB9E-B34E-E733-D6A3-E9ADA86ACE0E";
createNode materialInfo -n "materialInfo12";
	rename -uid "1D3D6F9A-254B-AD54-1B3F-358124E570FF";
createNode shadingEngine -n "PBRTUberMaterial9SG";
	rename -uid "01F102D9-8246-FB5D-EEF6-489E5174223F";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth5";
	rename -uid "EA03288B-AC4B-CDDF-EF8A-4885ABAD5BEE";
createNode materialInfo -n "materialInfo11";
	rename -uid "ABE988CD-6242-C55C-EE11-A5828DAF08C1";
createNode shadingEngine -n "PBRTUberMaterial8SG";
	rename -uid "D3A9C21D-1144-D231-6C57-1A96C1AFE8D2";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth4";
	rename -uid "3193DE29-0446-24C1-DAAF-DFB09EBB55B5";
createNode materialInfo -n "materialInfo9";
	rename -uid "487A97E0-9C43-3110-D1EF-DCA6CF446E23";
createNode shadingEngine -n "PBRTUberMaterial6SG";
	rename -uid "1CE75F39-0747-3E5F-34DA-CD9BA85D28B6";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth3";
	rename -uid "3072E9EB-1D4D-ECDB-5038-50BC5EC9E164";
createNode materialInfo -n "materialInfo10";
	rename -uid "D2ED8461-3B43-32A5-186C-C1B748A99572";
createNode shadingEngine -n "PBRTUberMaterial7SG";
	rename -uid "E2DD7D2F-9C44-2A85-33C3-84AEE38E6B73";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth2";
	rename -uid "7713DF04-EC43-7322-A7CE-C589A04F30BA";
createNode materialInfo -n "materialInfo8";
	rename -uid "66722071-F747-EEAE-16CC-9CBC0D38A019";
createNode shadingEngine -n "PBRTUberMaterial5SG";
	rename -uid "0C997D39-5043-1287-FD1D-D1986015D02A";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth1";
	rename -uid "67A75A36-E84E-0DED-BD3B-1295B85C6125";
createNode materialInfo -n "materialInfo32";
	rename -uid "3EEF4665-F04D-CF71-A941-C8847F8C6D57";
createNode shadingEngine -n "PBRTUberMaterial29SG";
	rename -uid "341FAD0F-4A4B-1623-6B8D-83BA483CFE61";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode PBRTUberMaterial -n "pbrt_macbeth_backing";
	rename -uid "53D277D3-4344-8AB2-1522-8EA65BD763EB";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "BC726E40-5E4E-482A-6AB8-60AD9D91C9D7";
	setAttr -s 34 ".lnk";
	setAttr -s 34 ".slnk";
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
	setAttr -s 6 ".u";
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
connectAttr "polyPlane1.out" "|MacbethChart|macbethChip24|macbethChipShape1.i";
connectAttr "PBRTUberMaterial28SG.msg" "materialInfo31.sg";
connectAttr "pbrt_macbeth24.msg" "materialInfo31.m";
connectAttr "pbrt_macbeth24.msg" "materialInfo31.t" -na;
connectAttr "pbrt_macbeth24.oc" "PBRTUberMaterial28SG.ss";
connectAttr "|MacbethChart|macbethChip24|macbethChipShape1.iog" "PBRTUberMaterial28SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial27SG.msg" "materialInfo30.sg";
connectAttr "pbrt_macbeth23.msg" "materialInfo30.m";
connectAttr "pbrt_macbeth23.msg" "materialInfo30.t" -na;
connectAttr "pbrt_macbeth23.oc" "PBRTUberMaterial27SG.ss";
connectAttr "|MacbethChart|macbethChip23|macbethChipShape1.iog" "PBRTUberMaterial27SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial26SG.msg" "materialInfo29.sg";
connectAttr "pbrt_macbeth22.msg" "materialInfo29.m";
connectAttr "pbrt_macbeth22.msg" "materialInfo29.t" -na;
connectAttr "pbrt_macbeth22.oc" "PBRTUberMaterial26SG.ss";
connectAttr "|MacbethChart|macbethChip22|macbethChipShape1.iog" "PBRTUberMaterial26SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial25SG.msg" "materialInfo28.sg";
connectAttr "pbrt_macbeth21.msg" "materialInfo28.m";
connectAttr "pbrt_macbeth21.msg" "materialInfo28.t" -na;
connectAttr "pbrt_macbeth21.oc" "PBRTUberMaterial25SG.ss";
connectAttr "|MacbethChart|macbethChip21|macbethChipShape1.iog" "PBRTUberMaterial25SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial24SG.msg" "materialInfo27.sg";
connectAttr "pbrt_macbeth20.msg" "materialInfo27.m";
connectAttr "pbrt_macbeth20.msg" "materialInfo27.t" -na;
connectAttr "pbrt_macbeth20.oc" "PBRTUberMaterial24SG.ss";
connectAttr "|MacbethChart|macbethChip20|macbethChipShape1.iog" "PBRTUberMaterial24SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial23SG.msg" "materialInfo26.sg";
connectAttr "pbrt_macbeth19.msg" "materialInfo26.m";
connectAttr "pbrt_macbeth19.msg" "materialInfo26.t" -na;
connectAttr "pbrt_macbeth19.oc" "PBRTUberMaterial23SG.ss";
connectAttr "|MacbethChart|macbethChip19|macbethChipShape1.iog" "PBRTUberMaterial23SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial22SG.msg" "materialInfo25.sg";
connectAttr "pbrt_macbeth18.msg" "materialInfo25.m";
connectAttr "pbrt_macbeth18.msg" "materialInfo25.t" -na;
connectAttr "pbrt_macbeth18.oc" "PBRTUberMaterial22SG.ss";
connectAttr "|MacbethChart|macbethChip18|macbethChipShape1.iog" "PBRTUberMaterial22SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial21SG.msg" "materialInfo24.sg";
connectAttr "pbrt_macbeth17.msg" "materialInfo24.m";
connectAttr "pbrt_macbeth17.msg" "materialInfo24.t" -na;
connectAttr "pbrt_macbeth17.oc" "PBRTUberMaterial21SG.ss";
connectAttr "|MacbethChart|macbethChip17|macbethChipShape1.iog" "PBRTUberMaterial21SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial20SG.msg" "materialInfo23.sg";
connectAttr "pbrt_macbeth16.msg" "materialInfo23.m";
connectAttr "pbrt_macbeth16.msg" "materialInfo23.t" -na;
connectAttr "pbrt_macbeth16.oc" "PBRTUberMaterial20SG.ss";
connectAttr "|MacbethChart|macbethChip16|macbethChipShape1.iog" "PBRTUberMaterial20SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial19SG.msg" "materialInfo22.sg";
connectAttr "pbrt_macbeth15.msg" "materialInfo22.m";
connectAttr "pbrt_macbeth15.msg" "materialInfo22.t" -na;
connectAttr "pbrt_macbeth15.oc" "PBRTUberMaterial19SG.ss";
connectAttr "|MacbethChart|macbethChip15|macbethChipShape1.iog" "PBRTUberMaterial19SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial18SG.msg" "materialInfo21.sg";
connectAttr "pbrt_macbeth14.msg" "materialInfo21.m";
connectAttr "pbrt_macbeth14.msg" "materialInfo21.t" -na;
connectAttr "pbrt_macbeth14.oc" "PBRTUberMaterial18SG.ss";
connectAttr "|MacbethChart|macbethChip14|macbethChipShape1.iog" "PBRTUberMaterial18SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial17SG.msg" "materialInfo20.sg";
connectAttr "pbrt_macbeth13.msg" "materialInfo20.m";
connectAttr "pbrt_macbeth13.msg" "materialInfo20.t" -na;
connectAttr "pbrt_macbeth13.oc" "PBRTUberMaterial17SG.ss";
connectAttr "|MacbethChart|macbethChip13|macbethChipShape1.iog" "PBRTUberMaterial17SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial16SG.msg" "materialInfo19.sg";
connectAttr "pbrt_macbeth12.msg" "materialInfo19.m";
connectAttr "pbrt_macbeth12.msg" "materialInfo19.t" -na;
connectAttr "pbrt_macbeth12.oc" "PBRTUberMaterial16SG.ss";
connectAttr "|MacbethChart|macbethChip12|macbethChipShape1.iog" "PBRTUberMaterial16SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial15SG.msg" "materialInfo18.sg";
connectAttr "pbrt_macbeth11.msg" "materialInfo18.m";
connectAttr "pbrt_macbeth11.msg" "materialInfo18.t" -na;
connectAttr "pbrt_macbeth11.oc" "PBRTUberMaterial15SG.ss";
connectAttr "|MacbethChart|macbethChip11|macbethChipShape1.iog" "PBRTUberMaterial15SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial14SG.msg" "materialInfo17.sg";
connectAttr "pbrt_macbeth10.msg" "materialInfo17.m";
connectAttr "pbrt_macbeth10.msg" "materialInfo17.t" -na;
connectAttr "pbrt_macbeth10.oc" "PBRTUberMaterial14SG.ss";
connectAttr "|MacbethChart|macbethChip10|macbethChipShape1.iog" "PBRTUberMaterial14SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial13SG.msg" "materialInfo16.sg";
connectAttr "pbrt_macbeth9.msg" "materialInfo16.m";
connectAttr "pbrt_macbeth9.msg" "materialInfo16.t" -na;
connectAttr "pbrt_macbeth9.oc" "PBRTUberMaterial13SG.ss";
connectAttr "|MacbethChart|macbethChip9|macbethChipShape1.iog" "PBRTUberMaterial13SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial12SG.msg" "materialInfo15.sg";
connectAttr "pbrt_macbeth8.msg" "materialInfo15.m";
connectAttr "pbrt_macbeth8.msg" "materialInfo15.t" -na;
connectAttr "pbrt_macbeth8.oc" "PBRTUberMaterial12SG.ss";
connectAttr "|MacbethChart|macbethChip8|macbethChipShape1.iog" "PBRTUberMaterial12SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial11SG.msg" "materialInfo14.sg";
connectAttr "pbrt_macbeth7.msg" "materialInfo14.m";
connectAttr "pbrt_macbeth7.msg" "materialInfo14.t" -na;
connectAttr "pbrt_macbeth7.oc" "PBRTUberMaterial11SG.ss";
connectAttr "|MacbethChart|macbethChip7|macbethChipShape1.iog" "PBRTUberMaterial11SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial10SG.msg" "materialInfo13.sg";
connectAttr "pbrt_macbeth6.msg" "materialInfo13.m";
connectAttr "pbrt_macbeth6.msg" "materialInfo13.t" -na;
connectAttr "pbrt_macbeth6.oc" "PBRTUberMaterial10SG.ss";
connectAttr "|MacbethChart|macbethChip6|macbethChipShape1.iog" "PBRTUberMaterial10SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial9SG.msg" "materialInfo12.sg";
connectAttr "pbrt_macbeth5.msg" "materialInfo12.m";
connectAttr "pbrt_macbeth5.msg" "materialInfo12.t" -na;
connectAttr "pbrt_macbeth5.oc" "PBRTUberMaterial9SG.ss";
connectAttr "|MacbethChart|macbethChip5|macbethChipShape1.iog" "PBRTUberMaterial9SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial8SG.msg" "materialInfo11.sg";
connectAttr "pbrt_macbeth4.msg" "materialInfo11.m";
connectAttr "pbrt_macbeth4.msg" "materialInfo11.t" -na;
connectAttr "pbrt_macbeth4.oc" "PBRTUberMaterial8SG.ss";
connectAttr "|MacbethChart|macbethChip4|macbethChipShape1.iog" "PBRTUberMaterial8SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial6SG.msg" "materialInfo9.sg";
connectAttr "pbrt_macbeth3.msg" "materialInfo9.m";
connectAttr "pbrt_macbeth3.msg" "materialInfo9.t" -na;
connectAttr "pbrt_macbeth3.oc" "PBRTUberMaterial6SG.ss";
connectAttr "|MacbethChart|macbethChip3|macbethChipShape1.iog" "PBRTUberMaterial6SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial7SG.msg" "materialInfo10.sg";
connectAttr "pbrt_macbeth2.msg" "materialInfo10.m";
connectAttr "pbrt_macbeth2.msg" "materialInfo10.t" -na;
connectAttr "pbrt_macbeth2.oc" "PBRTUberMaterial7SG.ss";
connectAttr "|MacbethChart|macbethChip2|macbethChipShape1.iog" "PBRTUberMaterial7SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial5SG.msg" "materialInfo8.sg";
connectAttr "pbrt_macbeth1.msg" "materialInfo8.m";
connectAttr "pbrt_macbeth1.msg" "materialInfo8.t" -na;
connectAttr "pbrt_macbeth1.oc" "PBRTUberMaterial5SG.ss";
connectAttr "|MacbethChart|macbethChip1|macbethChipShape1.iog" "PBRTUberMaterial5SG.dsm"
		 -na;
connectAttr "PBRTUberMaterial29SG.msg" "materialInfo32.sg";
connectAttr "pbrt_macbeth_backing.msg" "materialInfo32.m";
connectAttr "pbrt_macbeth_backing.msg" "materialInfo32.t" -na;
connectAttr "pbrt_macbeth_backing.oc" "PBRTUberMaterial29SG.ss";
connectAttr "macbethBackingShape.iog" "PBRTUberMaterial29SG.dsm" -na;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
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
// End of MacbethChart.ma
