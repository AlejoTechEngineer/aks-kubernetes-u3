#!/usr/bin/env bash
# Elimina TODO el resource group (clúster, discos, IPs, Log Analytics). Evita costos residuales.
set -euo pipefail
RG="${RG:-rg-aks-u3-demo}"
read -r -p "Se eliminará el resource group '$RG' completo. ¿Continuar? (si/no) " r
[[ "$r" == "si" ]] && az group delete --name "$RG" --yes --no-wait && echo "✔ Eliminación solicitada (en segundo plano)."
