from dataclasses import dataclass
from math import gcd

demoinput: str = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

input1: str = """Button A: X+82, Y+46
Button B: X+39, Y+96
Prize: X=5749, Y=7450

Button A: X+14, Y+60
Button B: X+74, Y+21
Prize: X=10194, Y=19178

Button A: X+89, Y+80
Button B: X+53, Y+11
Prize: X=4306, Y=3724

Button A: X+30, Y+97
Button B: X+96, Y+59
Prize: X=8490, Y=6082

Button A: X+57, Y+14
Button B: X+22, Y+50
Prize: X=3485, Y=8690

Button A: X+61, Y+38
Button B: X+17, Y+39
Prize: X=1363, Y=17185

Button A: X+59, Y+17
Button B: X+29, Y+63
Prize: X=8420, Y=12284

Button A: X+11, Y+27
Button B: X+47, Y+35
Prize: X=14723, Y=4967

Button A: X+44, Y+20
Button B: X+37, Y+65
Prize: X=14633, Y=15285

Button A: X+91, Y+17
Button B: X+34, Y+50
Prize: X=5769, Y=4395

Button A: X+47, Y+14
Button B: X+22, Y+65
Prize: X=17994, Y=7827

Button A: X+32, Y+64
Button B: X+27, Y+11
Prize: X=17241, Y=7817

Button A: X+21, Y+18
Button B: X+14, Y+63
Prize: X=1288, Y=4572

Button A: X+86, Y+44
Button B: X+11, Y+49
Prize: X=18047, Y=17733

Button A: X+43, Y+99
Button B: X+82, Y+42
Prize: X=7481, Y=9297

Button A: X+39, Y+68
Button B: X+76, Y+37
Prize: X=3134, Y=2408

Button A: X+90, Y+23
Button B: X+38, Y+40
Prize: X=5268, Y=4254

Button A: X+61, Y+19
Button B: X+18, Y+70
Prize: X=1755, Y=4861

Button A: X+31, Y+70
Button B: X+45, Y+14
Prize: X=16388, Y=6444

Button A: X+17, Y+52
Button B: X+94, Y+82
Prize: X=5699, Y=5306

Button A: X+85, Y+30
Button B: X+12, Y+67
Prize: X=8775, Y=14385

Button A: X+68, Y+44
Button B: X+21, Y+72
Prize: X=6816, Y=8616

Button A: X+13, Y+82
Button B: X+55, Y+14
Prize: X=6198, Y=9132

Button A: X+95, Y+40
Button B: X+41, Y+78
Prize: X=4673, Y=5794

Button A: X+73, Y+12
Button B: X+31, Y+82
Prize: X=6721, Y=8180

Button A: X+93, Y+34
Button B: X+43, Y+85
Prize: X=9341, Y=8126

Button A: X+94, Y+72
Button B: X+31, Y+78
Prize: X=7143, Y=5634

Button A: X+45, Y+20
Button B: X+18, Y+39
Prize: X=10628, Y=1994

Button A: X+15, Y+40
Button B: X+43, Y+21
Prize: X=6780, Y=17190

Button A: X+21, Y+63
Button B: X+59, Y+14
Prize: X=5143, Y=4519

Button A: X+57, Y+11
Button B: X+44, Y+95
Prize: X=5617, Y=6188

Button A: X+70, Y+18
Button B: X+30, Y+62
Prize: X=2120, Y=1848

Button A: X+60, Y+23
Button B: X+18, Y+41
Prize: X=500, Y=9002

Button A: X+28, Y+87
Button B: X+84, Y+13
Prize: X=6020, Y=2585

Button A: X+28, Y+64
Button B: X+84, Y+53
Prize: X=6244, Y=7878

Button A: X+89, Y+17
Button B: X+67, Y+91
Prize: X=10354, Y=4402

Button A: X+59, Y+28
Button B: X+28, Y+63
Prize: X=14323, Y=14046

Button A: X+47, Y+42
Button B: X+85, Y+11
Prize: X=2117, Y=1567

Button A: X+14, Y+66
Button B: X+66, Y+19
Prize: X=3296, Y=14714

Button A: X+35, Y+35
Button B: X+15, Y+62
Prize: X=2695, Y=4998

Button A: X+85, Y+81
Button B: X+91, Y+14
Prize: X=12689, Y=5620

Button A: X+53, Y+23
Button B: X+11, Y+30
Prize: X=3471, Y=15279

Button A: X+72, Y+15
Button B: X+19, Y+65
Prize: X=15964, Y=6225

Button A: X+59, Y+42
Button B: X+14, Y+31
Prize: X=11945, Y=7202

Button A: X+35, Y+49
Button B: X+34, Y+11
Prize: X=3605, Y=17723

Button A: X+18, Y+41
Button B: X+90, Y+58
Prize: X=4464, Y=3847

Button A: X+11, Y+69
Button B: X+72, Y+24
Prize: X=1631, Y=9329

Button A: X+15, Y+56
Button B: X+58, Y+27
Prize: X=5778, Y=15709

Button A: X+59, Y+18
Button B: X+11, Y+41
Prize: X=5050, Y=1655

Button A: X+12, Y+55
Button B: X+65, Y+12
Prize: X=5219, Y=15812

Button A: X+15, Y+66
Button B: X+64, Y+20
Prize: X=9440, Y=4976

Button A: X+75, Y+60
Button B: X+19, Y+56
Prize: X=3877, Y=5468

Button A: X+69, Y+26
Button B: X+31, Y+58
Prize: X=4008, Y=2344

Button A: X+32, Y+49
Button B: X+35, Y+16
Prize: X=18624, Y=2377

Button A: X+24, Y+61
Button B: X+44, Y+15
Prize: X=18716, Y=12216

Button A: X+22, Y+14
Button B: X+31, Y+99
Prize: X=2111, Y=2691

Button A: X+85, Y+38
Button B: X+23, Y+42
Prize: X=3807, Y=4842

Button A: X+94, Y+21
Button B: X+58, Y+83
Prize: X=11592, Y=6372

Button A: X+80, Y+25
Button B: X+72, Y+90
Prize: X=11272, Y=6965

Button A: X+15, Y+66
Button B: X+56, Y+15
Prize: X=3020, Y=15701

Button A: X+54, Y+19
Button B: X+31, Y+74
Prize: X=18505, Y=3156

Button A: X+53, Y+58
Button B: X+98, Y+20
Prize: X=12117, Y=6106

Button A: X+73, Y+27
Button B: X+18, Y+53
Prize: X=4995, Y=7502

Button A: X+51, Y+92
Button B: X+48, Y+24
Prize: X=5313, Y=8708

Button A: X+77, Y+39
Button B: X+15, Y+37
Prize: X=2120, Y=1456

Button A: X+51, Y+14
Button B: X+35, Y+75
Prize: X=2947, Y=13748

Button A: X+65, Y+58
Button B: X+18, Y+88
Prize: X=2527, Y=7938

Button A: X+18, Y+65
Button B: X+75, Y+29
Prize: X=6096, Y=6536

Button A: X+69, Y+11
Button B: X+32, Y+49
Prize: X=921, Y=937

Button A: X+31, Y+14
Button B: X+16, Y+36
Prize: X=12402, Y=3752

Button A: X+16, Y+55
Button B: X+79, Y+35
Prize: X=16357, Y=10790

Button A: X+17, Y+79
Button B: X+51, Y+11
Prize: X=2522, Y=15780

Button A: X+96, Y+53
Button B: X+11, Y+79
Prize: X=2765, Y=2037

Button A: X+13, Y+35
Button B: X+55, Y+16
Prize: X=15677, Y=7185

Button A: X+69, Y+21
Button B: X+11, Y+31
Prize: X=13547, Y=12335

Button A: X+62, Y+33
Button B: X+24, Y+54
Prize: X=19048, Y=19724

Button A: X+50, Y+26
Button B: X+46, Y+75
Prize: X=3206, Y=2229

Button A: X+59, Y+18
Button B: X+13, Y+38
Prize: X=12291, Y=15210

Button A: X+69, Y+25
Button B: X+64, Y+91
Prize: X=4336, Y=2656

Button A: X+11, Y+75
Button B: X+87, Y+33
Prize: X=6088, Y=7338

Button A: X+44, Y+27
Button B: X+18, Y+43
Prize: X=8784, Y=11197

Button A: X+24, Y+42
Button B: X+43, Y+15
Prize: X=2897, Y=16025

Button A: X+29, Y+22
Button B: X+17, Y+92
Prize: X=3923, Y=8276

Button A: X+92, Y+19
Button B: X+16, Y+49
Prize: X=8208, Y=2015

Button A: X+70, Y+11
Button B: X+80, Y+97
Prize: X=5080, Y=4091

Button A: X+64, Y+14
Button B: X+46, Y+60
Prize: X=8112, Y=5370

Button A: X+69, Y+90
Button B: X+96, Y+20
Prize: X=12678, Y=6120

Button A: X+15, Y+40
Button B: X+26, Y+12
Prize: X=11312, Y=2164

Button A: X+93, Y+17
Button B: X+72, Y+69
Prize: X=9810, Y=4641

Button A: X+45, Y+64
Button B: X+96, Y+42
Prize: X=3663, Y=4926

Button A: X+13, Y+48
Button B: X+54, Y+29
Prize: X=16985, Y=7860

Button A: X+42, Y+13
Button B: X+23, Y+42
Prize: X=13359, Y=18121

Button A: X+19, Y+47
Button B: X+48, Y+27
Prize: X=3839, Y=1802

Button A: X+47, Y+41
Button B: X+91, Y+11
Prize: X=7256, Y=3526

Button A: X+23, Y+11
Button B: X+21, Y+52
Prize: X=18260, Y=5745

Button A: X+36, Y+21
Button B: X+27, Y+86
Prize: X=3420, Y=6210

Button A: X+34, Y+13
Button B: X+15, Y+93
Prize: X=1090, Y=4780

Button A: X+79, Y+74
Button B: X+14, Y+53
Prize: X=7146, Y=9047

Button A: X+14, Y+55
Button B: X+69, Y+34
Prize: X=19724, Y=11485

Button A: X+96, Y+25
Button B: X+82, Y+90
Prize: X=9474, Y=6380

Button A: X+54, Y+18
Button B: X+26, Y+51
Prize: X=13600, Y=4676

Button A: X+20, Y+91
Button B: X+78, Y+58
Prize: X=2690, Y=4817

Button A: X+74, Y+17
Button B: X+32, Y+38
Prize: X=3744, Y=1044

Button A: X+12, Y+27
Button B: X+47, Y+20
Prize: X=11144, Y=18230

Button A: X+51, Y+25
Button B: X+48, Y+99
Prize: X=4710, Y=6988

Button A: X+14, Y+41
Button B: X+70, Y+44
Prize: X=5520, Y=10029

Button A: X+92, Y+15
Button B: X+13, Y+28
Prize: X=5044, Y=1340

Button A: X+24, Y+52
Button B: X+55, Y+24
Prize: X=3454, Y=1964

Button A: X+78, Y+25
Button B: X+16, Y+72
Prize: X=12718, Y=6761

Button A: X+74, Y+34
Button B: X+21, Y+62
Prize: X=18700, Y=14050

Button A: X+30, Y+60
Button B: X+75, Y+32
Prize: X=7680, Y=4976

Button A: X+27, Y+12
Button B: X+31, Y+73
Prize: X=2279, Y=3974

Button A: X+18, Y+73
Button B: X+37, Y+29
Prize: X=3052, Y=6809

Button A: X+51, Y+92
Button B: X+86, Y+13
Prize: X=10073, Y=4810

Button A: X+73, Y+39
Button B: X+23, Y+56
Prize: X=9456, Y=11104

Button A: X+12, Y+27
Button B: X+42, Y+18
Prize: X=12344, Y=10214

Button A: X+18, Y+81
Button B: X+78, Y+71
Prize: X=1866, Y=6997

Button A: X+18, Y+55
Button B: X+72, Y+23
Prize: X=2250, Y=1556

Button A: X+39, Y+80
Button B: X+59, Y+17
Prize: X=1583, Y=11801

Button A: X+88, Y+13
Button B: X+14, Y+31
Prize: X=6900, Y=2003

Button A: X+52, Y+15
Button B: X+65, Y+99
Prize: X=5161, Y=5100

Button A: X+43, Y+18
Button B: X+24, Y+59
Prize: X=6996, Y=4216

Button A: X+12, Y+45
Button B: X+89, Y+46
Prize: X=1788, Y=3252

Button A: X+58, Y+13
Button B: X+13, Y+30
Prize: X=7634, Y=1040

Button A: X+56, Y+37
Button B: X+20, Y+41
Prize: X=5824, Y=16583

Button A: X+22, Y+75
Button B: X+97, Y+75
Prize: X=5634, Y=5400

Button A: X+14, Y+52
Button B: X+69, Y+33
Prize: X=8994, Y=6580

Button A: X+23, Y+25
Button B: X+89, Y+15
Prize: X=962, Y=310

Button A: X+71, Y+31
Button B: X+38, Y+66
Prize: X=2683, Y=4383

Button A: X+12, Y+56
Button B: X+82, Y+26
Prize: X=9342, Y=1066

Button A: X+92, Y+54
Button B: X+18, Y+94
Prize: X=3494, Y=6306

Button A: X+72, Y+12
Button B: X+11, Y+63
Prize: X=18134, Y=1166

Button A: X+14, Y+33
Button B: X+29, Y+15
Prize: X=3054, Y=3701

Button A: X+75, Y+33
Button B: X+14, Y+43
Prize: X=10584, Y=1723

Button A: X+17, Y+58
Button B: X+93, Y+39
Prize: X=4310, Y=5521

Button A: X+11, Y+41
Button B: X+62, Y+17
Prize: X=6413, Y=5063

Button A: X+84, Y+26
Button B: X+63, Y+87
Prize: X=12873, Y=10667

Button A: X+55, Y+16
Button B: X+60, Y+98
Prize: X=7585, Y=6556

Button A: X+40, Y+15
Button B: X+62, Y+76
Prize: X=7676, Y=6993

Button A: X+17, Y+48
Button B: X+44, Y+12
Prize: X=4442, Y=4940

Button A: X+52, Y+26
Button B: X+23, Y+36
Prize: X=18641, Y=19070

Button A: X+76, Y+23
Button B: X+11, Y+49
Prize: X=7585, Y=18903

Button A: X+21, Y+50
Button B: X+87, Y+42
Prize: X=6072, Y=3888

Button A: X+92, Y+75
Button B: X+14, Y+75
Prize: X=4490, Y=8175

Button A: X+38, Y+92
Button B: X+91, Y+29
Prize: X=6685, Y=6045

Button A: X+78, Y+32
Button B: X+32, Y+45
Prize: X=9476, Y=6023

Button A: X+88, Y+25
Button B: X+58, Y+82
Prize: X=6636, Y=4113

Button A: X+17, Y+35
Button B: X+33, Y+16
Prize: X=8497, Y=13145

Button A: X+62, Y+19
Button B: X+15, Y+62
Prize: X=7008, Y=7656

Button A: X+20, Y+41
Button B: X+64, Y+27
Prize: X=10788, Y=7175

Button A: X+53, Y+20
Button B: X+14, Y+51
Prize: X=3313, Y=294

Button A: X+11, Y+51
Button B: X+63, Y+21
Prize: X=5928, Y=2544

Button A: X+82, Y+25
Button B: X+12, Y+58
Prize: X=1356, Y=13090

Button A: X+21, Y+36
Button B: X+73, Y+17
Prize: X=2470, Y=2504

Button A: X+22, Y+11
Button B: X+27, Y+87
Prize: X=2789, Y=6172

Button A: X+29, Y+87
Button B: X+29, Y+18
Prize: X=3654, Y=4269

Button A: X+12, Y+39
Button B: X+59, Y+28
Prize: X=9823, Y=5016

Button A: X+26, Y+48
Button B: X+66, Y+36
Prize: X=3612, Y=2376

Button A: X+81, Y+49
Button B: X+27, Y+76
Prize: X=3159, Y=2627

Button A: X+75, Y+50
Button B: X+11, Y+28
Prize: X=496, Y=14908

Button A: X+20, Y+92
Button B: X+25, Y+17
Prize: X=3415, Y=8751

Button A: X+12, Y+79
Button B: X+77, Y+48
Prize: X=6910, Y=6024

Button A: X+58, Y+23
Button B: X+33, Y+94
Prize: X=6765, Y=5191

Button A: X+82, Y+30
Button B: X+16, Y+66
Prize: X=8750, Y=13526

Button A: X+18, Y+97
Button B: X+81, Y+40
Prize: X=2610, Y=5342

Button A: X+56, Y+31
Button B: X+18, Y+33
Prize: X=15854, Y=3584

Button A: X+18, Y+75
Button B: X+79, Y+54
Prize: X=5979, Y=4275

Button A: X+15, Y+43
Button B: X+68, Y+12
Prize: X=8745, Y=11629

Button A: X+42, Y+48
Button B: X+97, Y+31
Prize: X=6191, Y=2843

Button A: X+83, Y+52
Button B: X+15, Y+49
Prize: X=6363, Y=6323

Button A: X+16, Y+57
Button B: X+75, Y+22
Prize: X=1047, Y=7798

Button A: X+61, Y+13
Button B: X+11, Y+64
Prize: X=5183, Y=6222

Button A: X+15, Y+41
Button B: X+30, Y+14
Prize: X=15785, Y=13791

Button A: X+12, Y+97
Button B: X+75, Y+22
Prize: X=2541, Y=2428

Button A: X+11, Y+50
Button B: X+74, Y+27
Prize: X=7792, Y=3070

Button A: X+30, Y+67
Button B: X+95, Y+39
Prize: X=6235, Y=3708

Button A: X+32, Y+11
Button B: X+19, Y+45
Prize: X=18406, Y=8177

Button A: X+79, Y+29
Button B: X+20, Y+83
Prize: X=4987, Y=4857

Button A: X+45, Y+18
Button B: X+14, Y+45
Prize: X=16507, Y=4184

Button A: X+16, Y+82
Button B: X+90, Y+22
Prize: X=8376, Y=6030

Button A: X+46, Y+15
Button B: X+61, Y+77
Prize: X=2174, Y=1280

Button A: X+19, Y+55
Button B: X+93, Y+50
Prize: X=9312, Y=6350

Button A: X+17, Y+79
Button B: X+63, Y+65
Prize: X=5862, Y=6970

Button A: X+31, Y+83
Button B: X+54, Y+12
Prize: X=14576, Y=5378

Button A: X+88, Y+54
Button B: X+17, Y+95
Prize: X=1771, Y=2017

Button A: X+26, Y+86
Button B: X+69, Y+12
Prize: X=14373, Y=13266

Button A: X+65, Y+96
Button B: X+86, Y+11
Prize: X=7587, Y=8073

Button A: X+51, Y+36
Button B: X+12, Y+97
Prize: X=2241, Y=7956

Button A: X+52, Y+15
Button B: X+25, Y+58
Prize: X=15713, Y=4698

Button A: X+13, Y+34
Button B: X+45, Y+32
Prize: X=15474, Y=19026

Button A: X+74, Y+30
Button B: X+11, Y+24
Prize: X=6123, Y=2580

Button A: X+11, Y+56
Button B: X+76, Y+69
Prize: X=1697, Y=6096

Button A: X+67, Y+52
Button B: X+20, Y+73
Prize: X=3230, Y=6013

Button A: X+17, Y+77
Button B: X+71, Y+13
Prize: X=16933, Y=6943

Button A: X+81, Y+11
Button B: X+29, Y+29
Prize: X=6822, Y=1152

Button A: X+68, Y+28
Button B: X+13, Y+31
Prize: X=801, Y=18587

Button A: X+16, Y+58
Button B: X+89, Y+18
Prize: X=2508, Y=5436

Button A: X+12, Y+31
Button B: X+55, Y+15
Prize: X=3103, Y=18364

Button A: X+34, Y+89
Button B: X+44, Y+33
Prize: X=6642, Y=11141

Button A: X+44, Y+61
Button B: X+29, Y+11
Prize: X=9381, Y=18594

Button A: X+82, Y+32
Button B: X+20, Y+90
Prize: X=7492, Y=4732

Button A: X+30, Y+13
Button B: X+39, Y+68
Prize: X=2618, Y=12606

Button A: X+77, Y+14
Button B: X+20, Y+79
Prize: X=12763, Y=9703

Button A: X+84, Y+15
Button B: X+45, Y+48
Prize: X=2682, Y=2637

Button A: X+46, Y+11
Button B: X+37, Y+62
Prize: X=4774, Y=3374

Button A: X+28, Y+90
Button B: X+69, Y+42
Prize: X=5075, Y=4986

Button A: X+58, Y+77
Button B: X+68, Y+13
Prize: X=11488, Y=7601

Button A: X+59, Y+16
Button B: X+40, Y+45
Prize: X=7255, Y=3880

Button A: X+43, Y+80
Button B: X+50, Y+13
Prize: X=15185, Y=9080

Button A: X+90, Y+44
Button B: X+24, Y+39
Prize: X=3108, Y=1983

Button A: X+21, Y+48
Button B: X+57, Y+26
Prize: X=12572, Y=2756

Button A: X+22, Y+71
Button B: X+75, Y+23
Prize: X=13814, Y=6179

Button A: X+11, Y+51
Button B: X+31, Y+21
Prize: X=1287, Y=1917

Button A: X+74, Y+12
Button B: X+77, Y+77
Prize: X=10944, Y=7968

Button A: X+46, Y+27
Button B: X+47, Y+88
Prize: X=7855, Y=9504

Button A: X+44, Y+19
Button B: X+15, Y+53
Prize: X=9301, Y=13143

Button A: X+46, Y+12
Button B: X+43, Y+47
Prize: X=4552, Y=1760

Button A: X+17, Y+78
Button B: X+68, Y+64
Prize: X=8177, Y=13462

Button A: X+51, Y+83
Button B: X+96, Y+11
Prize: X=3612, Y=1957

Button A: X+21, Y+69
Button B: X+90, Y+16
Prize: X=5028, Y=3374

Button A: X+31, Y+61
Button B: X+66, Y+26
Prize: X=6720, Y=6160

Button A: X+26, Y+52
Button B: X+37, Y+21
Prize: X=13191, Y=9105

Button A: X+16, Y+50
Button B: X+40, Y+33
Prize: X=4272, Y=5990

Button A: X+66, Y+19
Button B: X+12, Y+71
Prize: X=16502, Y=11026

Button A: X+30, Y+76
Button B: X+28, Y+13
Prize: X=3082, Y=2362

Button A: X+42, Y+21
Button B: X+21, Y+51
Prize: X=13724, Y=10367

Button A: X+22, Y+92
Button B: X+44, Y+28
Prize: X=2134, Y=3464

Button A: X+28, Y+52
Button B: X+51, Y+14
Prize: X=2024, Y=14856

Button A: X+25, Y+66
Button B: X+54, Y+22
Prize: X=12836, Y=15962

Button A: X+23, Y+70
Button B: X+47, Y+16
Prize: X=7650, Y=2830

Button A: X+18, Y+66
Button B: X+72, Y+19
Prize: X=1196, Y=3397

Button A: X+29, Y+15
Button B: X+36, Y+61
Prize: X=9465, Y=15953

Button A: X+51, Y+15
Button B: X+48, Y+81
Prize: X=4248, Y=6600

Button A: X+64, Y+29
Button B: X+11, Y+39
Prize: X=6295, Y=2340

Button A: X+68, Y+47
Button B: X+15, Y+33
Prize: X=18136, Y=961

Button A: X+92, Y+94
Button B: X+87, Y+17
Prize: X=9292, Y=2880

Button A: X+62, Y+25
Button B: X+11, Y+25
Prize: X=19491, Y=6700

Button A: X+75, Y+94
Button B: X+92, Y+31
Prize: X=13142, Y=10064

Button A: X+34, Y+18
Button B: X+28, Y+62
Prize: X=1036, Y=1492

Button A: X+11, Y+38
Button B: X+25, Y+16
Prize: X=5213, Y=3818

Button A: X+15, Y+47
Button B: X+69, Y+17
Prize: X=16763, Y=18079

Button A: X+41, Y+22
Button B: X+18, Y+35
Prize: X=17705, Y=13969

Button A: X+68, Y+43
Button B: X+14, Y+32
Prize: X=12198, Y=19404

Button A: X+79, Y+48
Button B: X+44, Y+81
Prize: X=7347, Y=8751

Button A: X+43, Y+84
Button B: X+42, Y+25
Prize: X=6289, Y=8007

Button A: X+30, Y+12
Button B: X+29, Y+67
Prize: X=908, Y=1582

Button A: X+11, Y+50
Button B: X+46, Y+22
Prize: X=17910, Y=5982

Button A: X+28, Y+80
Button B: X+99, Y+45
Prize: X=9426, Y=9330

Button A: X+73, Y+19
Button B: X+21, Y+76
Prize: X=10297, Y=17714

Button A: X+49, Y+21
Button B: X+11, Y+32
Prize: X=15269, Y=14303

Button A: X+50, Y+27
Button B: X+26, Y+58
Prize: X=2826, Y=10468

Button A: X+74, Y+19
Button B: X+21, Y+68
Prize: X=10664, Y=1843

Button A: X+87, Y+64
Button B: X+24, Y+68
Prize: X=3699, Y=3728

Button A: X+82, Y+75
Button B: X+83, Y+18
Prize: X=15921, Y=9060

Button A: X+61, Y+89
Button B: X+44, Y+16
Prize: X=7025, Y=7165

Button A: X+65, Y+12
Button B: X+14, Y+79
Prize: X=9924, Y=15125

Button A: X+47, Y+17
Button B: X+11, Y+50
Prize: X=2510, Y=1271

Button A: X+13, Y+48
Button B: X+78, Y+24
Prize: X=7514, Y=6360

Button A: X+33, Y+15
Button B: X+27, Y+44
Prize: X=12251, Y=1519

Button A: X+48, Y+12
Button B: X+29, Y+80
Prize: X=3561, Y=13392

Button A: X+55, Y+17
Button B: X+11, Y+42
Prize: X=396, Y=933

Button A: X+37, Y+74
Button B: X+49, Y+11
Prize: X=16070, Y=17579

Button A: X+88, Y+65
Button B: X+30, Y+92
Prize: X=8824, Y=9032

Button A: X+26, Y+60
Button B: X+54, Y+18
Prize: X=2530, Y=1254

Button A: X+57, Y+84
Button B: X+38, Y+14
Prize: X=11520, Y=3210

Button A: X+45, Y+19
Button B: X+16, Y+52
Prize: X=671, Y=11161

Button A: X+13, Y+75
Button B: X+93, Y+12
Prize: X=9072, Y=5130

Button A: X+44, Y+12
Button B: X+13, Y+26
Prize: X=19008, Y=11828

Button A: X+14, Y+33
Button B: X+64, Y+47
Prize: X=13826, Y=2890

Button A: X+68, Y+23
Button B: X+22, Y+61
Prize: X=19608, Y=4101

Button A: X+54, Y+28
Button B: X+23, Y+49
Prize: X=2428, Y=3780

Button A: X+71, Y+30
Button B: X+21, Y+49
Prize: X=6965, Y=3906

Button A: X+50, Y+94
Button B: X+76, Y+46
Prize: X=10720, Y=10950

Button A: X+46, Y+11
Button B: X+24, Y+55
Prize: X=6506, Y=5940

Button A: X+33, Y+81
Button B: X+64, Y+22
Prize: X=7202, Y=4844

Button A: X+42, Y+83
Button B: X+86, Y+40
Prize: X=11738, Y=10981

Button A: X+94, Y+61
Button B: X+13, Y+36
Prize: X=1997, Y=1544

Button A: X+41, Y+50
Button B: X+73, Y+15
Prize: X=7911, Y=4910

Button A: X+78, Y+20
Button B: X+14, Y+64
Prize: X=6564, Y=4216

Button A: X+15, Y+44
Button B: X+35, Y+22
Prize: X=2630, Y=7360

Button A: X+17, Y+95
Button B: X+60, Y+71
Prize: X=3272, Y=9563

Button A: X+23, Y+77
Button B: X+44, Y+12
Prize: X=3902, Y=8834

Button A: X+32, Y+68
Button B: X+42, Y+13
Prize: X=17370, Y=11105

Button A: X+17, Y+73
Button B: X+54, Y+17
Prize: X=11630, Y=7982

Button A: X+15, Y+87
Button B: X+64, Y+26
Prize: X=2356, Y=1928

Button A: X+67, Y+19
Button B: X+17, Y+81
Prize: X=3736, Y=6392

Button A: X+59, Y+17
Button B: X+25, Y+35
Prize: X=3982, Y=2426

Button A: X+22, Y+58
Button B: X+61, Y+30
Prize: X=957, Y=15354

Button A: X+89, Y+38
Button B: X+39, Y+84
Prize: X=9885, Y=10686"""


def is_whole_positive(a, b):
    """
    Check if dividing a by b results in a whole positive number.

    Parameters:
    a (int): The dividend, can be positive or negative.
    b (int): The divisor, can be positive or negative.

    Returns:
    bool: True if a / b is a whole positive number, False otherwise.
    """
    if a == 0:
        return True

    if b == 0:
        # Division by zero is undefined
        return False

    if a % b != 0:
        # a is not exactly divisible by b
        return False

    result = a // b  # Integer division
    if result > 0:
        return True
    else:
        return False


@dataclass
class MachineSetup:
    P_x: int
    P_y: int

    a_x: int
    a_y: int

    b_x: int
    b_y: int

    test_injected_a_count: int | None = None
    test_injected_b_count: int | None = None

    def _try_guessing(self) -> tuple[int, int] | None:
        a_b_solutions = []
        best_score = 9999999
        best_solution = None

        for b in list(range(1, 50000))[::-1]:
            a = (self.P_x - (self.b_x * b))
            if a % self.a_x == 0:
                a_count = a // self.a_x

                # check if the result satisfies the equation2
                if self.P_y == (self.a_y * a_count) + (self.b_y * b):
                    a_b_solutions.append((a_count, b))

        for a, b in a_b_solutions:
            score = a * 3 + b * 1
            if score < best_score:
                best_score = score
                best_solution = (a, b)

        return best_solution

    def find_optimal_counts(self):
        objective_coeff_a: int = 3
        objective_coeff_b: int = 1

        a_x = self.a_x
        a_y = self.a_y
        b_x = self.b_x
        b_y = self.b_y
        P_x = self.P_x
        P_y = self.P_y

        # Step 1: Verify Linear Dependence
        D = a_x * b_y - a_y * b_x

        if D != 0:
            # Equations are independent; check if the unique solution has integer values
            a_count = (P_x * b_y - P_y * b_x) / D
            b_count = (a_x * P_y - a_y * P_x) / D

            if a_count.is_integer() and b_count.is_integer() and a_count >= 0 and b_count >= 0:
                return (int(a_count), int(b_count))
            else:
                # Unique solution exists but not integer or non-negative
                return None

        else:
            # D == 0; equations are either dependent or inconsistent
            # Check consistency: ratios of coefficients and constants should be equal
            consistent = False
            if (a_x == 0 and a_y == 0 and P_x == 0 and P_y == 0):
                consistent = True
            elif a_x == 0 and a_y == 0:
                if b_x != 0 and b_y != 0:
                    consistent = (P_x / b_x == P_y / b_y)
                elif b_x == 0 and b_y == 0:
                    consistent = (P_x == 0 and P_y == 0)
                else:
                    consistent = False
            elif b_x == 0 and b_y == 0:
                if a_x != 0 and a_y != 0:
                    consistent = (P_x / a_x == P_y / a_y)
                elif a_x == 0 and a_y == 0:
                    consistent = (P_x == 0 and P_y == 0)
                else:
                    consistent = False
            else:
                # Both a_x and b_x are non-zero, check the ratios
                ratio1 = a_x / a_y if a_y != 0 else None
                ratio2 = b_x / b_y if b_y != 0 else None
                ratio3 = P_x / P_y if P_y != 0 else None

                # All ratios must be equal
                if ratio1 is not None and ratio2 is not None and ratio3 is not None:
                    consistent = (abs(ratio1 - ratio2) < 1e-9) and (abs(ratio1 - ratio3) < 1e-9)
                else:
                    # Handle cases where some ratios are undefined (division by zero)
                    consistent = False

            if not consistent:
                # Inconsistent system; no solution
                return None

            # Step 2: Parametrize the Solution
            # Express a in terms of b using Equation 1: a = (P_x - b_x * b) / a_x
            # Ensure that a is integer and non-negative

            if a_x != 0:
                # Find a particular solution (a0, b0)
                # Find b0 such that (P_x - b_x * b0) is divisible by a_x
                b0 = None
                for b_candidate in range(0, P_x // b_x + 1):
                    if (P_x - b_x * b_candidate) % a_x == 0:
                        a_candidate = (P_x - b_x * b_candidate) // a_x
                        if a_candidate >= 0:
                            b0 = b_candidate
                            a0 = a_candidate
                            break
                if b0 is None:
                    # No valid solution exists
                    return None

                # Calculate step sizes
                common_gcd = gcd(a_x, b_x)
                delta_a = b_x // common_gcd
                delta_b = a_x // common_gcd

                # General Solution: a = a0 - k * delta_a, b = b0 + k * delta_b
                # k must be integer such that a >=0 and b >=0

                # Objective Function: 3*a + b = 3*(a0 - k*delta_a) + (b0 + k*delta_b) = 3*a0 + b0 + k*(-3*delta_a + delta_b)

                coeff_k = -3 * delta_a + delta_b

                # Determine feasible range for k
                k_min = 0
                k_max = min(a0 // delta_a if delta_a != 0 else 0,
                            (P_x - a_x * a0) // b_x if b_x != 0 else 0)
                # To ensure a >=0 and b >=0:
                k_max_a = a0 // delta_a if delta_a != 0 else 0
                k_max_b = ((P_x - a_x * a0) // b_x) if b_x != 0 else 0
                k_max = a0 // delta_a if delta_a != 0 else 0
                # To find the maximum k such that a >=0 and b >=0
                k_max_a = a0 // delta_a if delta_a != 0 else float('inf')
                k_max_b = ((P_x - a_x * a0) // b_x) if b_x != 0 else float('inf')
                k_max = min(k_max_a, k_max_b)
                if k_max == float('inf'):
                    k_max = 0  # Only k=0 is possible
                else:
                    k_max = int(k_max)

                # Now, determine the optimal k based on the sign of coeff_k
                if coeff_k > 0:
                    # Objective increases with k; minimize k
                    optimal_k = 0
                elif coeff_k < 0:
                    # Objective decreases with k; maximize k
                    optimal_k = k_max
                else:
                    # Objective is constant; any k is optimal
                    optimal_k = 0

                # Compute the optimal a and b
                a_opt = a0 - optimal_k * delta_a
                b_opt = b0 + optimal_k * delta_b

                # Verify non-negativity
                if a_opt < 0 or b_opt < 0:
                    return None

                # Verify the second equation
                if a_y * a_opt + b_y * b_opt != P_y:
                    return None

                return (a_opt, b_opt)

            elif b_x != 0:
                # Similar approach: express b in terms of a using Equation 1
                a0 = None
                for a_candidate in range(0, P_x // a_x + 1):
                    if (P_x - a_x * a_candidate) % b_x == 0:
                        b_candidate = (P_x - a_x * a_candidate) // b_x
                        if b_candidate >= 0:
                            a0 = a_candidate
                            b0 = b_candidate
                            break
                if a0 is None:
                    return None

                # Calculate step sizes
                common_gcd = gcd(a_x, b_x)
                delta_a = b_x // common_gcd
                delta_b = a_x // common_gcd

                # General Solution: a = a0 + k * delta_a, b = b0 - k * delta_b
                # k must be integer such that a >=0 and b >=0

                # Objective Function: 3*a + b = 3*(a0 + k*delta_a) + (b0 - k*delta_b) = 3*a0 + b0 + k*(3*delta_a - delta_b)

                coeff_k = 3 * delta_a - delta_b

                # Determine feasible range for k
                # To ensure b >=0:
                if delta_b == 0:
                    if b0 < 0:
                        return None
                    k_max = 0
                else:
                    k_max = b0 // delta_b

                # Determine k_min based on a >=0
                if delta_a == 0:
                    if a0 < 0:
                        return None
                    k_min = 0
                else:
                    # a = a0 + k * delta_a >=0
                    # If delta_a >0, no lower bound on k (other than k >=0)
                    # If delta_a <0, k <= a0 / |delta_a|
                    if delta_a > 0:
                        k_min = 0
                    else:
                        k_min = max(0, (-a0) // delta_a)

                # Find the optimal k based on the sign of coeff_k
                if coeff_k > 0:
                    # Objective increases with k; minimize k
                    optimal_k = 0
                elif coeff_k < 0:
                    # Objective decreases with k; maximize k
                    optimal_k = k_max
                else:
                    # Objective is constant; any k is optimal
                    optimal_k = 0

                # Compute the optimal a and b
                a_opt = a0 + optimal_k * delta_a
                b_opt = b0 - optimal_k * delta_b

                # Verify non-negativity
                if a_opt < 0 or b_opt < 0:
                    return None

                # Verify the second equation
                if a_y * a_opt + b_y * b_opt != P_y:
                    return None

                return (a_opt, b_opt)

            else:
                # Both a_x and b_x are zero
                # Equations reduce to 0 = P_x and 0 = P_y
                # Already checked consistency earlier
                # Now, any (a, b) that satisfies a_y * a + b_y * b = P_y
                # Find the pair that minimizes 3*a + b

                if a_y == 0 and b_y == 0:
                    if P_y == 0:
                        # Any (a, b) is a solution; minimal objective is (0,0)
                        return (0, 0)
                    else:
                        # No solution exists
                        return None

                if a_y != 0:
                    # Express a in terms of b
                    a0 = None
                    for b_candidate in range(0, P_y // b_y + 1):
                        if (P_y - b_y * b_candidate) % a_y == 0:
                            a_candidate = (P_y - b_y * b_candidate) // a_y
                            if a_candidate >= 0:
                                a0 = a_candidate
                                b0 = b_candidate
                                break
                    if a0 is None:
                        return None

                    # Calculate step sizes
                    common_gcd = gcd(a_y, b_y)
                    delta_a = b_y // common_gcd
                    delta_b = a_y // common_gcd

                    # General Solution: a = a0 - k * delta_a, b = b0 + k * delta_b
                    # Objective: 3*a + b = 3*(a0 - k*delta_a) + (b0 + k*delta_b) = 3*a0 + b0 + k*(-3*delta_a + delta_b)

                    coeff_k = -3 * delta_a + delta_b

                    # Determine feasible k
                    k_max_a = a0 // delta_a if delta_a != 0 else 0
                    k_max_b = (P_y - a_y * a0) // b_y if b_y != 0 else 0
                    k_max = min(k_max_a, k_max_b) if delta_a != 0 else 0

                    # Optimal k based on coeff_k
                    if coeff_k > 0:
                        optimal_k = 0
                    elif coeff_k < 0:
                        optimal_k = k_max
                    else:
                        optimal_k = 0

                    # Compute optimal a and b
                    a_opt = a0 - optimal_k * delta_a
                    b_opt = b0 + optimal_k * delta_b

                    # Verify non-negativity
                    if a_opt < 0 or b_opt < 0:
                        return None

                    # Verify second equation
                    if a_y * a_opt + b_y * b_opt != P_y:
                        return None

                    return (a_opt, b_opt)

                elif b_y != 0:
                    # Express b in terms of a
                    b0 = None
                    for a_candidate in range(0, P_y // a_y + 1):
                        if (P_y - a_y * a_candidate) % b_y == 0:
                            b_candidate = (P_y - a_y * a_candidate) // b_y
                            if b_candidate >= 0:
                                a0 = a_candidate
                                b0 = b_candidate
                                break
                    if b0 is None:
                        return None

                    # Calculate step sizes
                    common_gcd = gcd(a_y, b_y)
                    delta_a = b_y // common_gcd
                    delta_b = a_y // common_gcd

                    # General Solution: a = a0 + k * delta_a, b = b0 - k * delta_b
                    # Objective: 3*a + b = 3*(a0 + k*delta_a) + (b0 - k*delta_b) = 3*a0 + b0 + k*(3*delta_a - delta_b)

                    coeff_k = 3 * delta_a - delta_b

                    # Determine feasible k
                    if delta_b != 0:
                        k_max = b0 // delta_b
                    else:
                        k_max = 0

                    # Optimal k based on coeff_k
                    if coeff_k > 0:
                        optimal_k = 0
                    elif coeff_k < 0:
                        optimal_k = k_max
                    else:
                        optimal_k = 0

                    # Compute optimal a and b
                    a_opt = a0 + optimal_k * delta_a
                    b_opt = b0 - optimal_k * delta_b

                    # Verify non-negativity
                    if a_opt < 0 or b_opt < 0:
                        return None

                    # Verify second equation
                    if a_y * a_opt + b_y * b_opt != P_y:
                        return None

                    return (a_opt, b_opt)

                else:
                    # Both a_y and b_y are zero
                    if P_y == 0:
                        # Any (a, b) is a solution; minimal objective is (0,0)
                        return (0, 0)
                    else:
                        # No solution exists
                        return None

    def get_a_b_press_count(self) -> tuple[int, int] | None:
        # b_count_fraction_upper = (self.P_y * self.a_x) - (self.P_x * self.a_y)
        # b_count_fraction_lower = (self.b_y * self.a_x) - (self.b_x * self.a_y)
        #
        # if not is_whole_positive(b_count_fraction_upper, b_count_fraction_lower):
        #     return self._try_guessing()
        #
        # if b_count_fraction_lower == 0:
        #     return self._try_guessing()
        #
        # b_count = b_count_fraction_upper // b_count_fraction_lower
        #
        # a_count_fraction_upper = self.P_x - (self.b_x * b_count)
        # a_count_fraction_lower = self.a_x
        #
        # if not is_whole_positive(a_count_fraction_upper, a_count_fraction_lower):
        #     return self._try_guessing()
        # if a_count_fraction_lower == 0:
        #     return self._try_guessing()
        # a_count = a_count_fraction_upper // a_count_fraction_lower

        # return a_count, b_count
        return self.find_optimal_counts()

    def __str__(self):
        test_injected_txt = f", {self.test_injected_a_count = }, {self.test_injected_b_count = }" if self.test_injected_a_count is not None or self.test_injected_b_count is not None else ""
        return f"Prize: ({self.P_x}, {self.P_y}), A: ({self.a_x}, {self.a_y}), B: ({self.b_x}, {self.b_y})" + test_injected_txt