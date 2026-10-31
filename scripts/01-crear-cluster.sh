#!/usr/bin/env bash
# Crea el clúster AKS de la demo (Unidad 3 - Contenerización de Aplicaciones de Software).
# Requisitos: Azure CLI autenticado (az login) y kubectl instalado.
# Nota: los flags de `az aks create` evolucionan; ante un error revisa `az aks create --help`.
set -euo pipefail

RG="${RG:-rg-aks-u3-demo}"
LOCATION="${LOCATION:-eastus2}"
CLUSTER="${CLUSTER:-aks-u3-demo}"
NODE_SIZE="${NODE_SIZE:-Standard_B2s}"   # si hay error de cuota/SKU: Standard_D2s_v5

echo "▶ Resource group: $RG ($LOCATION)"
az group create --name "$RG" --location "$LOCATION" --output none

echo "▶ Creando clúster AKS (tarda ~5-10 min, conviene crearlo ANTES de grabar)..."
az aks create \
  --resource-group "$RG" \
  --name "$CLUSTER" \
  --location "$LOCATION" \
  --tier free \
  --node-count 2 \
  --node-vm-size "$NODE_SIZE" \
  --enable-cluster-autoscaler --min-count 2 --max-count 4 \
  --network-plugin azure --network-plugin-mode overlay \
  --enable-managed-identity \
  --enable-oidc-issuer --enable-workload-identity \
  --enable-addons monitoring \
  --generate-ssh-keys

echo "▶ Credenciales de kubectl"
az aks get-credentials --resource-group "$RG" --name "$CLUSTER" --overwrite-existing

kubectl get nodes -o wide
echo "✔ Clúster listo. Recuerda ejecutar scripts/99-limpiar.sh al terminar para no generar costos."
