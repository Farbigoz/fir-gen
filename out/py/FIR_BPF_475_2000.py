# LENGTH_FIR_BPF_475 2000 taps
# fs = 2000 Hz

f_475 = [
	     0,      0,      0,      0,      0,      0,      0,      0, 
	     0,      0,      0,      0,      0,      0,      1,      0, 
	    -1,      0,      1,      0,      0,     -1,      0,      1, 
	     0,     -1,      0,      1,      0,     -1,      0,      1, 
	     0,     -1,      0,      1,      0,     -1,     -1,      1, 
	     1,     -1,     -1,      0,      1,      0,     -1,      0, 
	     1,      0,     -1,      0,      1,      0,      0,      0, 
	     0,      0,      0,      0,      0,      0,      0,      0, 
	     0,      0,      0,      0,      0,      0,      0,      0, 
	     0,      0,      0,      0,      0,      0,      0,      0, 
	     0,      0,     -1,      0,      1,      0,     -1,      0, 
	     1,      0,     -2,      0,      2,      0,     -2,      0, 
	     2,      1,     -1,     -1,      1,      1,     -1,     -2, 
	     0,      2,      0,     -2,      0,      2,      0,     -2, 
	     0,      1,      0,     -1,      0,      1,      1,     -1, 
	    -1,      0,      1,      0,     -1,      0,      0,      0, 
	     0,      0,      0,      0,      0,      0,      0,      0, 
	     0,      0,      0,      0,      0,      0,      0,     -1, 
	     0,      1,      0,     -1,      0,      2,      0,     -2, 
	     0,      2,      0,     -2,     -1,      2,      1,     -2, 
	    -2,      2,      2,     -1,     -3,      1,      3,      0, 
	    -3,      0,      3,      0,     -3,      0,      3,      1, 
	    -2,     -1,      2,      2,     -2,     -2,      1,      2, 
	    -1,     -2,      0,      2,      0,     -1,      0,      1, 
	     0,     -1,      0,      0,      0,      0,      0,      0, 
	     0,      0,      0,      0,      0,      0,      1,      0, 
	    -1,      0,      2,      0,     -2,      0,      2,      1, 
	    -2,     -1,      2,      2,     -2,     -3,      2,      3, 
	    -1,     -4,      1,      4,      0,     -5,      0,      5, 
	     1,     -5,     -1,      4,      2,     -4,     -3,      3, 
	     3,     -3,     -4,      2,      4,     -1,     -4,      0, 
	     4,      0,     -4,      0,      3,      0,     -3,     -1, 
	     2,      1,     -1,     -1,      1,      1,      0,      0, 
	     0,      0,      0,      0,      0,      0,      0,      1, 
	     0,     -2,      0,      2,      1,     -2,     -2,      2, 
	     3,     -2,     -4,      2,      4,     -1,     -5,      1, 
	     6,      0,     -6,      0,      7,      1,     -7,     -3, 
	     6,      4,     -6,     -5,      5,      6,     -4,     -7, 
	     3,      7,     -2,     -7,      0,      7,      0,     -7, 
	    -1,      6,      2,     -5,     -3,      5,      3,     -3, 
	    -3,      2,      3,     -2,     -3,      1,      2,      0, 
	    -2,      0,      1,      0,      0,      0,      0,      0, 
	     1,      1,     -1,     -1,      2,      2,     -2,     -4, 
	     2,      5,     -1,     -6,      0,      7,      0,     -8, 
	    -1,      8,      3,     -8,     -4,      8,      6,     -7, 
	    -7,      6,      9,     -5,    -10,      3,     11,     -2, 
	   -11,      0,     11,      1,    -11,     -3,     10,      4, 
	    -9,     -5,      8,      6,     -6,     -7,      5,      7, 
	    -3,     -7,      2,      7,      0,     -6,      0,      5, 
	     0,     -3,     -1,      2,      1,     -1,      0,      0, 
	     0,      0,      1,     -1,     -2,      1,      4,      0, 
	    -5,      0,      6,      0,     -8,     -2,      8,      4, 
	    -9,     -6,      9,      8,     -8,    -10,      7,     12, 
	    -5,    -13,      4,     14,     -1,    -15,      0,     16, 
	     3,    -15,     -5,     14,      8,    -13,    -10,     11, 
	    11,     -9,    -12,      7,     13,     -5,    -13,      2, 
	    13,      0,    -12,     -1,     10,      2,     -9,     -3, 
	     7,      4,     -5,     -4,      3,      3,     -2,     -2, 
	     0,      0,      0,      0,      0,     -2,      0,      4, 
	     1,     -6,     -2,      7,      4,     -8,     -6,      8, 
	     9,     -8,    -11,      7,     14,     -5,    -16,      3, 
	    18,      0,    -19,     -2,     20,      5,    -19,     -9, 
	    19,     12,    -17,    -15,     15,     17,    -12,    -19, 
	     9,     20,     -6,    -21,      2,     21,      0,    -20, 
	    -3,     18,      6,    -16,     -8,     13,      9,    -10, 
	   -10,      8,     10,     -5,     -9,      3,      7,     -1, 
	    -5,      0,      3,      0,     -1,      0,     -1,     -1, 
	     3,      2,     -5,     -5,      6,      8,     -6,    -11, 
	     5,     14,     -4,    -17,      2,     19,      0,    -21, 
	    -4,     22,      8,    -22,    -12,     22,     16,    -20, 
	   -20,     17,     24,    -14,    -27,     10,     29,     -5, 
	   -30,      1,     30,      3,    -29,     -8,     27,     12, 
	   -24,    -15,     21,     18,    -17,    -19,     13,     20, 
	    -9,    -19,      5,     18,     -2,    -16,      0,     13, 
	     2,    -10,     -3,      6,      2,     -3,     -1,      0, 
	     0,      1,      3,     -2,     -6,      3,     10,     -2, 
	   -14,      0,     17,      2,    -20,     -6,     22,     10, 
	   -23,    -15,     23,     20,    -21,    -26,     19,     30, 
	   -15,    -34,     10,     38,     -4,    -39,     -1,     40, 
	     8,    -39,    -14,     37,     20,    -34,    -25,     29, 
	    29,    -24,    -32,     18,     34,    -12,    -34,      6, 
	    33,     -1,    -30,     -3,     27,      7,    -23,     -9, 
	    18,     10,    -13,    -10,      9,      8,     -5,     -6, 
	     2,      2,      0,      1,      0,     -6,      0,     11, 
	     2,    -15,     -6,     18,     11,    -20,    -16,     21, 
	    22,    -20,    -29,     18,     35,    -14,    -40,      8, 
	    45,     -1,    -48,     -5,     50,     14,    -49,    -22, 
	    47,     30,    -43,    -38,     38,     44,    -31,    -49, 
	    23,     52,    -15,    -53,      6,     53,      2,    -50, 
	    -9,     46,     16,    -41,    -21,     34,     24,    -27, 
	   -25,     20,     25,    -13,    -23,      7,     19,     -3, 
	   -14,      0,      8,      0,     -2,      0,     -3,     -2, 
	     8,      7,    -12,    -13,     15,     20,    -16,    -28, 
	    14,     35,    -11,    -43,      5,     49,      2,    -54, 
	   -11,     57,     21,    -58,    -32,     56,     43,    -52, 
	   -53,     46,     62,    -37,    -70,     27,     75,    -15, 
	   -78,      3,     79,      9,    -76,    -21,     71,     31, 
	   -64,    -40,     56,     47,    -45,    -51,     35,     52, 
	   -24,    -51,     14,     48,     -5,    -42,     -1,     35, 
	     6,    -26,     -8,     17,      7,     -9,     -4,      1, 
	    -1,      4,      9,     -7,    -18,      8,     28,     -6, 
	   -38,      1,     48,      6,    -55,    -16,     61,     29, 
	   -64,    -43,     64,     57,    -60,    -72,     52,     85, 
	   -42,    -97,     28,    106,    -13,   -112,     -4,    114, 
	    22,   -113,    -40,    107,     57,    -98,    -73,     86, 
	    85,    -71,    -94,     54,     99,    -37,   -100,     19, 
	    97,     -3,    -91,    -10,     81,     21,    -69,    -28, 
	    55,     32,    -41,    -31,     27,     27,    -15,    -18, 
	     6,      7,      0,      5,     -1,    -20,     -1,     35, 
	     8,    -48,    -20,     59,     35,    -66,    -54,     69, 
	    75,    -67,    -97,     60,    118,    -47,   -138,     29, 
	   154,     -6,   -166,    -20,    173,     49,   -174,    -79, 
	   169,    109,   -157,   -137,    139,    162,   -115,   -182, 
	    87,    196,    -56,   -203,     24,    203,      7,   -196, 
	   -38,    183,     64,   -164,    -85,    140,    100,   -113, 
	  -107,     85,    107,    -58,   -100,     34,     85,    -15, 
	   -64,      2,     39,      3,    -11,      0,    -16,    -13, 
	    42,     35,    -63,    -66,     78,    104,    -83,   -147, 
	    78,    193,    -61,   -239,     31,    283,     11,   -320, 
	   -66,    349,    132,   -366,   -207,    369,    287,   -355, 
	  -370,    324,    452,   -275,   -529,    208,    597,   -124, 
	  -653,     26,    693,     83,   -714,   -202,    714,    325, 
	  -691,   -448,    645,    567,   -576,   -677,    485,    773, 
	  -375,   -851,    249,    909,   -109,   -942,    -37,    950, 
	   187,   -931,   -336,    885,    478,   -815,   -608,    721, 
	   721,   -608,   -815,    478,    885,   -336,   -931,    187, 
	   950,    -37,   -942,   -109,    909,    249,   -851,   -375, 
	   773,    485,   -677,   -576,    567,    645,   -448,   -691, 
	   325,    714,   -202,   -714,     83,    693,     26,   -653, 
	  -124,    597,    208,   -529,   -275,    452,    324,   -370, 
	  -355,    287,    369,   -207,   -366,    132,    349,    -66, 
	  -320,     11,    283,     31,   -239,    -61,    193,     78, 
	  -147,    -83,    104,     78,    -66,    -63,     35,     42, 
	   -13,    -16,      0,    -11,      3,     39,      2,    -64, 
	   -15,     85,     34,   -100,    -58,    107,     85,   -107, 
	  -113,    100,    140,    -85,   -164,     64,    183,    -38, 
	  -196,      7,    203,     24,   -203,    -56,    196,     87, 
	  -182,   -115,    162,    139,   -137,   -157,    109,    169, 
	   -79,   -174,     49,    173,    -20,   -166,     -6,    154, 
	    29,   -138,    -47,    118,     60,    -97,    -67,     75, 
	    69,    -54,    -66,     35,     59,    -20,    -48,      8, 
	    35,     -1,    -20,     -1,      5,      0,      7,      6, 
	   -18,    -15,     27,     27,    -31,    -41,     32,     55, 
	   -28,    -69,     21,     81,    -10,    -91,     -3,     97, 
	    19,   -100,    -37,     99,     54,    -94,    -71,     85, 
	    86,    -73,    -98,     57,    107,    -40,   -113,     22, 
	   114,     -4,   -112,    -13,    106,     28,    -97,    -42, 
	    85,     52,    -72,    -60,     57,     64,    -43,    -64, 
	    29,     61,    -16,    -55,      6,     48,      1,    -38, 
	    -6,     28,      8,    -18,     -7,      9,      4,     -1, 
	     1,     -4,     -9,      7,     17,     -8,    -26,      6, 
	    35,     -1,    -42,     -5,     48,     14,    -51,    -24, 
	    52,     35,    -51,    -45,     47,     56,    -40,    -64, 
	    31,     71,    -21,    -76,      9,     79,      3,    -78, 
	   -15,     75,     27,    -70,    -37,     62,     46,    -53, 
	   -52,     43,     56,    -32,    -58,     21,     57,    -11, 
	   -54,      2,     49,      5,    -43,    -11,     35,     14, 
	   -28,    -16,     20,     15,    -13,    -12,      7,      8, 
	    -2,     -3,      0,     -2,      0,      8,      0,    -14, 
	    -3,     19,      7,    -23,    -13,     25,     20,    -25, 
	   -27,     24,     34,    -21,    -41,     16,     46,     -9, 
	   -50,      2,     53,      6,    -53,    -15,     52,     23, 
	   -49,    -31,     44,     38,    -38,    -43,     30,     47, 
	   -22,    -49,     14,     50,     -5,    -48,     -1,     45, 
	     8,    -40,    -14,     35,     18,    -29,    -20,     22, 
	    21,    -16,    -20,     11,     18,     -6,    -15,      2, 
	    11,      0,     -6,      0,      1,      0,      2,      2, 
	    -6,     -5,      8,      9,    -10,    -13,     10,     18, 
	    -9,    -23,      7,     27,     -3,    -30,     -1,     33, 
	     6,    -34,    -12,     34,     18,    -32,    -24,     29, 
	    29,    -25,    -34,     20,     37,    -14,    -39,      8, 
	    40,     -1,    -39,     -4,     38,     10,    -34,    -15, 
	    30,     19,    -26,    -21,     20,     23,    -15,    -23, 
	    10,     22,     -6,    -20,      2,     17,      0,    -14, 
	    -2,     10,      3,     -6,     -2,      3,      1,      0, 
	     0,     -1,     -3,      2,      6,     -3,    -10,      2, 
	    13,      0,    -16,     -2,     18,      5,    -19,     -9, 
	    20,     13,    -19,    -17,     18,     21,    -15,    -24, 
	    12,     27,     -8,    -29,      3,     30,      1,    -30, 
	    -5,     29,     10,    -27,    -14,     24,     17,    -20, 
	   -20,     16,     22,    -12,    -22,      8,     22,     -4, 
	   -21,      0,     19,      2,    -17,     -4,     14,      5, 
	   -11,     -6,      8,      6,     -5,     -5,      2,      3, 
	    -1,     -1,      0,     -1,      0,      3,      0,     -5, 
	    -1,      7,      3,     -9,     -5,     10,      8,    -10, 
	   -10,      9,     13,     -8,    -16,      6,     18,     -3, 
	   -20,      0,     21,      2,    -21,     -6,     20,      9, 
	   -19,    -12,     17,     15,    -15,    -17,     12,     19, 
	    -9,    -19,      5,     20,     -2,    -19,      0,     18, 
	     3,    -16,     -5,     14,      7,    -11,     -8,      9, 
	     8,     -6,     -8,      4,      7,     -2,     -6,      1, 
	     4,      0,     -2,      0,      0,      0,      0,      0, 
	    -2,     -2,      3,      3,     -4,     -5,      4,      7, 
	    -3,     -9,      2,     10,     -1,    -12,      0,     13, 
	     2,    -13,     -5,     13,      7,    -12,     -9,     11, 
	    11,    -10,    -13,      8,     14,     -5,    -15,      3, 
	    16,      0,    -15,     -1,     14,      4,    -13,     -5, 
	    12,      7,    -10,     -8,      8,      9,     -6,     -9, 
	     4,      8,     -2,     -8,      0,      6,      0,     -5, 
	     0,      4,      1,     -2,     -1,      1,      0,      0, 
	     0,      0,     -1,      1,      2,     -1,     -3,      0, 
	     5,      0,     -6,      0,      7,      2,     -7,     -3, 
	     7,      5,     -7,     -6,      6,      8,     -5,     -9, 
	     4,     10,     -3,    -11,      1,     11,      0,    -11, 
	    -2,     11,      3,    -10,     -5,      9,      6,     -7, 
	    -7,      6,      8,     -4,     -8,      3,      8,     -1, 
	    -8,      0,      7,      0,     -6,     -1,      5,      2, 
	    -4,     -2,      2,      2,     -1,     -1,      1,      1, 
	     0,      0,      0,      0,      0,      1,      0,     -2, 
	     0,      2,      1,     -3,     -2,      3,      2,     -3, 
	    -3,      3,      5,     -3,     -5,      2,      6,     -1, 
	    -7,      0,      7,      0,     -7,     -2,      7,      3, 
	    -7,     -4,      6,      5,     -5,     -6,      4,      6, 
	    -3,     -7,      1,      7,      0,     -6,      0,      6, 
	     1,     -5,     -1,      4,      2,     -4,     -2,      3, 
	     2,     -2,     -2,      1,      2,      0,     -2,      0, 
	     1,      0,      0,      0,      0,      0,      0,      0, 
	     0,      0,      1,      1,     -1,     -1,      1,      2, 
	    -1,     -3,      0,      3,      0,     -4,      0,      4, 
	     0,     -4,     -1,      4,      2,     -4,     -3,      3, 
	     3,     -3,     -4,      2,      4,     -1,     -5,      1, 
	     5,      0,     -5,      0,      4,      1,     -4,     -1, 
	     3,      2,     -3,     -2,      2,      2,     -1,     -2, 
	     1,      2,      0,     -2,      0,      2,      0,     -1, 
	     0,      1,      0,      0,      0,      0,      0,      0, 
	     0,      0,      0,      0,      0,      0,     -1,      0, 
	     1,      0,     -1,      0,      2,      0,     -2,     -1, 
	     2,      1,     -2,     -2,      2,      2,     -1,     -2, 
	     1,      3,      0,     -3,      0,      3,      0,     -3, 
	     0,      3,      1,     -3,     -1,      2,      2,     -2, 
	    -2,      1,      2,     -1,     -2,      0,      2,      0, 
	    -2,      0,      2,      0,     -1,      0,      1,      0, 
	    -1,      0,      0,      0,      0,      0,      0,      0, 
	     0,      0,      0,      0,      0,      0,      0,      0, 
	     0,      0,      0,     -1,      0,      1,      0,     -1, 
	    -1,      1,      1,      0,     -1,      0,      1,      0, 
	    -2,      0,      2,      0,     -2,      0,      2,      0, 
	    -2,     -1,      1,      1,     -1,     -1,      1,      2, 
	     0,     -2,      0,      2,      0,     -2,      0,      1, 
	     0,     -1,      0,      1,      0,     -1,      0,      0, 
	     0,      0,      0,      0,      0,      0,      0,      0, 
	     0,      0,      0,      0,      0,      0,      0,      0, 
	     0,      0,      0,      0,      0,      0,      0,      0, 
	     0,      0,      0,      1,      0,     -1,      0,      1, 
	     0,     -1,      0,      1,      0,     -1,     -1,      1, 
	     1,     -1,     -1,      0,      1,      0,     -1,      0, 
	     1,      0,     -1,      0,      1,      0,     -1,      0, 
	     1,      0,     -1,      0,      0,      1,      0,     -1, 
	     0,      1,      0,      0,      0,      0,      0,      0, 
	     0,      0,      0,      0,      0,      0,      0,      0
]
