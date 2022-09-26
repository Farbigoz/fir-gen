from scipy.signal import firwin


# Расчет коэффициентов FIR


def bpf_fir(ntaps, lowcut, highcut, fs):
    nyq = 0.5 * fs
    taps = firwin(ntaps, [lowcut, highcut], nyq=nyq, pass_zero=False, scale=False)

    return taps


def lpf_fir(ntaps, fcut, fs):
    nyq = 0.5 * fs
    taps = firwin(ntaps, fcut, nyq=nyq)

    return taps


def hpf_fir(ntaps, fcut, fs):
    nyq = 0.5 * fs
    taps = firwin(ntaps, fcut, nyq=nyq, pass_zero=False)

    return taps
