"""Experimento 01: senoide e espectro de amplitude unilateral."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

FS = 1000  # Hz
FREQUENCIA = 50  # Hz
DURACAO = 1.0  # s

amostras = int(FS * DURACAO)
tempo = np.arange(amostras) / FS
sinal = np.sin(2 * np.pi * FREQUENCIA * tempo)

frequencias = np.fft.rfftfreq(amostras, d=1 / FS)
espectro = np.abs(np.fft.rfft(sinal)) / amostras
if amostras % 2 == 0:
    espectro[1:-1] *= 2
else:
    espectro[1:] *= 2

figura, eixos = plt.subplots(2, 1, figsize=(10, 7))
eixos[0].plot(tempo, sinal)
eixos[0].set(xlabel='Tempo (s)', ylabel='Amplitude', title='Senoide de 50 Hz')
eixos[0].grid(True)
eixos[1].plot(frequencias, espectro)
eixos[1].set(xlabel='Frequência (Hz)', ylabel='Amplitude', title='Espectro unilateral (FFT)')
eixos[1].set_xlim(0, 150)
eixos[1].grid(True)
figura.tight_layout()
saida = Path(__file__).resolve().parent.parent / 'resultados' / 'senoide_fft.png'
saida.parent.mkdir(parents=True, exist_ok=True)
figura.savefig(saida, dpi=150)
print(f'Gráfico salvo em: {saida}')
