/////////////////////////////////////////////////////////////
// Created by: Synopsys DC Expert(TM) in wire load mode
// Version   : K-2015.06-SP5
// Date      : Tue Oct 12 16:52:17 2021
/////////////////////////////////////////////////////////////


module circ ( a, b, r );
  input [8:0] a;
  input [8:0] b;
  output [8:0] r;
  wire   n284, n285, n286, n287, n288, n289, n290, n291, n292, n293, n294,
         n295, n296, n297, n298, n299, n300, n301, n302, n304, n305, n306,
         n307, n308, n309, n310, n311, n312, n313, n314, n315, n316, n317,
         n318, n319, n320, n321, n322, n323, n324, n325, n326, n327, n328,
         n329, n330, n331, n332, n333, n334, n335, n336, n337, n338, n339,
         n340, n341, n342, n343, n344, n345, n346, n347, n348, n349, n350,
         n351, n352, n353, n354, n355, n356, n357, n358, n359, n360, n361,
         n362, n363, n364, n365, n366, n367, n368, n369, n370, n371, n372,
         n373, n374, n375, n376, n377, n378, n379, n380, n381, n382, n383,
         n384, n385, n386, n387, n388, n389, n390, n391, n392, n393, n394,
         n395, n396, n397, n398, n399, n400, n401, n402, n403, n404, n405,
         n406, n407, n408, n409, n410, n411, n412, n413, n414, n415, n416,
         n417, n418, n419, n420, n421, n422, n423, n424, n425, n426, n427,
         n428, n429, n430, n431, n432, n433, n434, n435, n436, n437, n438,
         n439, n440, n441, n442, n443, n444, n445, n446, n447, n448, n449,
         n450, n451, n452, n453, n454, n463;

assign n284 = ~n325;
assign n285 = ~n352;
assign n286 = ~n348;
assign n287 = ~n344;
assign n288 = ~n340;
assign n289 = ~n336;
assign n290 = ~n332;
assign n291 = ~n410;
assign n292 = ~n403;
assign n293 = ~n402;
assign n294 = ~n394;
assign n295 = ~n393;
assign n296 = ~n385;
assign n297 = ~n384;
assign n298 = ~n376;
assign n299 = ~n375;
assign n300 = ~n367;
assign n301 = ~n366;
assign n302 = ~n326;
assign n304 = ~a[8];
assign n305 = ~n427;
assign n306 = ~a[7];
assign n307 = ~a[6];
assign n308 = ~a[5];
assign n309 = ~a[4];
assign n310 = ~a[3];
assign n311 = ~a[2];
assign n312 = ~a[1];
assign n313 = ~a[0];
assign n314 = ~b[8];
assign n315 = ~b[7];
assign n316 = ~b[6];
assign n317 = ~b[5];
assign n318 = ~b[4];
assign n319 = ~b[3];
assign n320 = ~b[2];
assign n321 = ~b[1];
assign n322 = ~b[0];
assign r[8] = n323 & n324;
assign n324 = n325 | n326;
assign n323 = n327 | n328;
assign n328 = a[8] & n314;
assign n327 = b[8] & n304;
assign r[0] = n329 | n330;
assign n330 = a[0] & n322;
assign n329 = b[0] & n313;
assign r[1] = n331 & n290;
assign n331 = n333 | n334;
assign r[2] = n335 & n289;
assign n335 = n337 | n338;
assign r[3] = n339 & n288;
assign n339 = n341 | n342;
assign r[4] = n343 & n287;
assign n343 = n345 | n346;
assign r[5] = n347 & n286;
assign n347 = n349 | n350;
assign r[6] = n351 & n285;
assign n351 = n353 | n354;
assign r[7] = n355 & n284;
assign n325 = n356 & n357;
assign n355 = n357 | n356;
assign n356 = n358 | n359;
assign n359 = n360 & n302;
assign n326 = n360 & n361;
assign n361 = n306 | n315;
assign n360 = n362 | n363;
assign n363 = b[7] & n364;
assign n362 = n463 & a[7];
assign n358 = n306 & n315;
assign n357 = n352 | n365;
assign n365 = n366 & n367;
assign n352 = n354 & n353;
assign n353 = n368 | n369;
assign n369 = n301 & n367;
assign n368 = n300 & n366;
assign n366 = n370 | n371;
assign n371 = b[6] & n364;
assign n370 = n463 & a[6];
assign n367 = n372 | n373;
assign n373 = n364 & n307;
assign n372 = n463 & n316;
assign n354 = n348 | n374;
assign n374 = n375 & n376;
assign n348 = n350 & n349;
assign n349 = n377 | n378;
assign n378 = n299 & n376;
assign n377 = n298 & n375;
assign n375 = n379 | n380;
assign n380 = b[5] & n364;
assign n379 = n463 & a[5];
assign n376 = n381 | n382;
assign n382 = n364 & n308;
assign n381 = n463 & n317;
assign n350 = n344 | n383;
assign n383 = n384 & n385;
assign n344 = n346 & n345;
assign n345 = n386 | n387;
assign n387 = n297 & n385;
assign n386 = n296 & n384;
assign n384 = n388 | n389;
assign n389 = b[4] & n364;
assign n388 = n463 & a[4];
assign n385 = n390 | n391;
assign n391 = n364 & n309;
assign n390 = n463 & n318;
assign n346 = n340 | n392;
assign n392 = n393 & n394;
assign n340 = n342 & n341;
assign n341 = n395 | n396;
assign n396 = n295 & n394;
assign n395 = n294 & n393;
assign n393 = n397 | n398;
assign n398 = b[3] & n364;
assign n397 = n463 & a[3];
assign n394 = n399 | n400;
assign n400 = n364 & n310;
assign n399 = n463 & n319;
assign n342 = n336 | n401;
assign n401 = n402 & n403;
assign n336 = n338 & n337;
assign n337 = n404 | n405;
assign n405 = n293 & n403;
assign n404 = n292 & n402;
assign n402 = n406 | n407;
assign n407 = b[2] & n364;
assign n406 = n463 & a[2];
assign n403 = n408 | n409;
assign n409 = n364 & n311;
assign n408 = n463 & n320;
assign n338 = n332 | n410;
assign n332 = n334 & n333;
assign n333 = n291 & n411;
assign n411 = n412 | n413;
assign n410 = n412 & n413;
assign n413 = n414 | n415;
assign n415 = b[1] & n364;
assign n414 = n463 & a[1];
assign n412 = n416 | n417;
assign n417 = n364 & n312;
assign n416 = n463 & n321;
assign n334 = n418 | n419;
assign n419 = n420 | n421;
assign n421 = n364 & n313;
assign n420 = n463 & n322;
assign n364 = n422 | n423;
assign n423 = n424 & n304;
assign n422 = b[8] & n425;
assign n425 = n424 | n304;
assign n424 = n426 & n305;
assign n427 = n428 | n429;
assign n429 = n430 & a[6];
assign n430 = n431 & n316;
assign n428 = n432 & n433;
assign n433 = n434 | n435;
assign n435 = a[5] & n436;
assign n434 = n437 & n317;
assign n437 = a[5] | n436;
assign n436 = n438 | n439;
assign n439 = a[4] & n440;
assign n438 = n441 & n318;
assign n441 = a[4] | n440;
assign n440 = n442 | n443;
assign n443 = n444 | n445;
assign n445 = n446 & a[2];
assign n446 = n447 & n320;
assign n444 = n448 & n449;
assign n449 = n450 | n451;
assign n451 = a[1] & n321;
assign n450 = a[0] & n452;
assign n452 = a[1] | n321;
assign n448 = n453 & n447;
assign n447 = a[3] | n319;
assign n453 = a[2] | n320;
assign n442 = a[3] & n319;
assign n432 = n454 & n431;
assign n431 = a[7] | n315;
assign n454 = a[6] | n316;
assign n426 = n306 | b[7];
assign n418 = b[0] & a[0];
assign n463 = ~n364;
endmodule

