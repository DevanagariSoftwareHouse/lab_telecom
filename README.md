# Lab Telecom

Laboratórios reproduzíveis de Engenharia de Telecomunicações em Python.

Versão inicial: **0.0.0**. Diretórios seguem `NNN-nome-do-laboratorio`.

## Ambiente compartilhado

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python 001-sinais-e-sistemas/src/senoide_fft.py
```

O `startup.py` define a política global de exportação. A função `lab_telecom.export.save_figure` salva cada figura nos formatos SVG, PDF e PNG, com 300 dpi para saídas rasterizadas.

## Laboratório 001 — Sinais e Sistemas

O experimento gera uma senoide de 50 Hz, calcula sua FFT e exporta os gráficos para `001-sinais-e-sistemas/resultados/`.
