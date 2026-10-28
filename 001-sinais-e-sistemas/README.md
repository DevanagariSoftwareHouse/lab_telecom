# Sinais e Sistemas — Experimento 01

Gerar uma senoide de 50 Hz amostrada a 1000 Hz durante 1 segundo e calcular a transformada discreta de Fourier via FFT real (`rfft`).

O espectro unilateral de amplitude deve apresentar um pico em 50 Hz, com amplitude aproximadamente igual a 1.

A partir da raiz do repositório, instale o ambiente com `pip install -e .` e execute:

```bash
python 001-sinais-e-sistemas/src/senoide_fft.py
```

Os resultados são exportados em SVG, PDF e PNG para `001-sinais-e-sistemas/resultados/`. As opções globais estão em `startup.py`.
