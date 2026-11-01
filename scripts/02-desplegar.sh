#!/usr/bin/env bash
# Despliega las tres aplicaciones de la demo sobre el clúster activo.
set -euo pipefail
cd "$(dirname "$0")/.."

echo ">> Namespaces + cuotas"
kubectl apply -f k8s/00-namespaces.yaml

echo ">> App 1: web nginx (stateless)"
kubectl apply -f k8s/10-web-nginx.yaml

echo ">> App 2: votación (microservicios: Python + Redis)"
kubectl apply -f k8s/20-azure-vote.yaml

echo ">> App 3: PostgreSQL (stateful)"
# El Secret se genera al vuelo: nunca se guarda la contraseña en el repositorio
kubectl create secret generic pg-credentials -n data \
  --from-literal=password="$(openssl rand -base64 18)" \
  --dry-run=client -o yaml | kubectl apply -f -
kubectl apply -f k8s/30-postgres-statefulset.yaml

echo ">> Esperando a que todo quede disponible..."
kubectl rollout status deployment/web-nginx -n web --timeout=180s
kubectl rollout status deployment/azure-vote-back -n vote --timeout=180s
kubectl rollout status deployment/azure-vote-front -n vote --timeout=180s
kubectl rollout status statefulset/postgres -n data --timeout=240s

echo
kubectl get pods,svc -A -l app.kubernetes.io/part-of=aks-u3 -o wide || true
kubectl get svc -n web web-nginx
kubectl get svc -n vote azure-vote-front
kubectl get pvc -n data
