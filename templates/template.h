/**
 * @file	{fileName}
 */

#ifndef __FIR_{type}_{freq}_{samplerate}_H__
#define __FIR_{type}_{freq}_{samplerate}_H__

#define LENGTH_FIR_{type}_{freq} {tapCount}


static {numType} fir{type}_{freq}coeff[LENGTH_FIR_{type}_{freq}] = {{
{tapsTable}
}};


#endif /* __FIR_{type}_{freq}_{samplerate}_H__ */
