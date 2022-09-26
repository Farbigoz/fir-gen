from typing import List

from PyQt5.QtWidgets import QWidget, QVBoxLayout

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT

from scipy.signal import freqz


from src.firGen import bpf_fir


class SignalPlotter(QWidget):
    def __init__(self):
        super().__init__()

        self.fig = plt.figure(1, figsize=(12, 9))

        self.figCanvas = FigureCanvasQTAgg(self.fig)
        self.toolbar = NavigationToolbar2QT(self.figCanvas, self)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.figCanvas)

        self.setLayout(layout)

    def plotLowPass(self, fCut, samplerate, taps):
        self.fig.clear()

        # First plot the desired ideal response as a green(ish) rectangle.
        rect = plt.Rectangle((0, 0), fCut, -90, facecolor="#60ff60", alpha=0.2)
        plt.gca().add_patch(rect)

        # Plot the frequency response
        w, h = freqz(list(map(lambda x: x * 0x7fff, taps)), 1, worN=10000)
        plt.plot((samplerate * 0.5 / np.pi) * w,
                 20 * np.log10(abs(h)) - 90,
                 label="Hamming window")

        plt.xlim(0, fCut + 100)
        plt.ylim(-90, 5)
        plt.grid(True)
        plt.legend()
        plt.xlabel('Частота (Гц)')
        plt.ylabel('Коефф передачи')
        plt.title('АЧХ FIR , %d  Гц %d taps, fs = %d Hz' % (fCut, len(taps), samplerate))

        self.figCanvas.draw()

    def plotBandPass(self, loCut, hiCut, samplerate, taps):
        self.fig.clear()

        # First plot the desired ideal response as a green(ish) rectangle.
        rect = plt.Rectangle((loCut, 0),
                             hiCut - loCut,
                             -90,
                             facecolor="#60ff60",
                             alpha=0.2)
        plt.gca().add_patch(rect)

        # Plot the frequency response
        w, h = freqz(list(map(lambda x: x * 0x7fff, taps)), 1, worN=10000)
        plt.plot((samplerate * 0.5 / np.pi) * w,
                 20 * np.log10(abs(h)) - 90,
                 label="Hamming window")

        plt.xlim(loCut - 100, hiCut + 100)
        plt.ylim(-90, 5)
        plt.grid(True)
        plt.legend()
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Gain')
        plt.title('АЧХ FIR фильтра, %d - %d  Гц %d taps, fs = %d Hz' %
                  (loCut, hiCut, len(taps), samplerate))

        self.figCanvas.draw()




