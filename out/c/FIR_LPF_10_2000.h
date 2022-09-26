/**
 * @file	FIR_LPF_10_2000.h
 */

#ifndef __FIR_LPF_10_2000_H__
#define __FIR_LPF_10_2000_H__

#define LENGTH_FIR_LPF_10 100


static int16_t firLPF_10coeff[LENGTH_FIR_LPF_10] = {
	   33,    34,    36,    39,    42,    47,    52,    59, 
	   66,    75,    84,    94,   105,   118,   131,   145, 
	  160,   175,   192,   209,   227,   245,   264,   283, 
	  303,   322,   342,   363,   383,   403,   422,   442, 
	  461,   480,   498,   515,   532,   548,   563,   577, 
	  590,   602,   613,   623,   631,   638,   643,   648, 
	  650,   652,   652,   650,   648,   643,   638,   631, 
	  623,   613,   602,   590,   577,   563,   548,   532, 
	  515,   498,   480,   461,   442,   422,   403,   383, 
	  363,   342,   322,   303,   283,   264,   245,   227, 
	  209,   192,   175,   160,   145,   131,   118,   105, 
	   94,    84,    75,    66,    59,    52,    47,    42, 
	   39,    36,    34,    33, 

};


#endif /* __FIR_LPF_10_2000_H__ */
