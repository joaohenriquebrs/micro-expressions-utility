#!/usr/bin/env bash
# Telemetria de memória (mprof). Gate alvo: pico de RAM < 2.5 GB durante o processamento.
set -euo pipefail

echo "[mprof_check] O gate de memória será habilitado no Sprint 2, quando existir o worker"
echo "[mprof_check] de processamento de vídeo. Comando alvo:"
echo "[mprof_check]   mprof run app/workers/processor.py && mprof peak  # deve ser < 2.5 GB"
echo "[mprof_check] SKIPPED — ainda não há pipeline para medir."
