surface ptexcolor(string mapname=""; string filter="gaussian"; 
		  float Ka = .2, Kd = .8;
		  varying float __faceindex=0)
{
    Oi = 1;
    if (mapname != "") {
	Ci = ptexture(mapname, 0, __faceindex, "fill", -1, "filter", filter, "lerp", 1);
	if (Ci[1] == -1) { Ci[1] = Ci[2] = Ci[0]; }
    } else {
	Ci = .5;
    }
    Ci *= Kd * clamp((normalize(N) . normalize(-I)), 0, 1) + Ka;
}
