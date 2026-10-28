# Lab Telecom

Laboratórios reproduzíveis de Engenharia de Telecomunicações em Python.

Convenção de diretórios: `NNN-nome-do-laboratorio`, com três dígitos, letras minúsculas, sem acentos e palavras separadas por hífens.

## Laboratório 001 — Sinais e Sistemas

Experimento: gerar uma senoide, calcular sua FFT e visualizar o sinal no tempo e seu espectro.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python 001-sinais-e-sistemas/src/senoide_fft.py
```

O gráfico será salvo em `001-sinais-e-sistemas/resultados/senoide_fft.png`.
