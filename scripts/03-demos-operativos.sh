#!/usr/bin/env bash
# Demos "Day-2" para el video: autocuración, escalado, HPA, rolling update y rollback.
# Cada paso espera un Enter para que puedas narrar antes de ejecutar.
set -euo pipefail

paso() { echo; echo "▶ $*"; read -r -p "   [Enter para ejecutar] " _; }

paso "1) Autocuración: eliminar un pod y ver cómo el ReplicaSet lo recrea"
POD=$(kubectl get pods -n web -o jsonpath='{.items[0].metadata.name}')
kubectl delete pod "$POD" -n web --wait=false
kubectl get pods -n web -w --request-timeout=20s || true

paso "2) Escalado manual a 5 réplicas"
kubectl scale deployment/web-nginx -n web --replicas=5
kubectl get pods -n web -o wide

paso "3) Persistencia: escribir en PostgreSQL, matar el pod y verificar que el dato sigue"
kubectl exec -n data postgres-0 -- psql -U demo -d appdb \
  -c "CREATE TABLE IF NOT EXISTS u3(msg text); INSERT INTO u3 VALUES ('sobrevivo al reinicio');"
kubectl delete pod postgres-0 -n data
kubectl wait --for=condition=Ready pod/postgres-0 -n data --timeout=180s
kubectl exec -n data postgres-0 -- psql -U demo -d appdb -c "SELECT * FROM u3;"

paso "4) Rolling update sin downtime (cambio de imagen)"
kubectl set image deployment/web-nginx nginx=nginxinc/nginx-unprivileged:1.27-alpine -n web
kubectl rollout status deployment/web-nginx -n web
kubectl rollout history deployment/web-nginx -n web

paso "5) Rollback a la revisión anterior"
kubectl rollout undo deployment/web-nginx -n web
kubectl rollout status deployment/web-nginx -n web

paso "6) HPA: generar carga y observar el autoescalado (abre otra terminal con 'kubectl get hpa -n web -w')"
kubectl create deployment load-gen --image=busybox:1.36 --replicas=3 -- \
  /bin/sh -c 'while true; do wget -q -O- http://web-nginx.web.svc.cluster.local/ >/dev/null; done'
echo "   Observa: kubectl get hpa,pods -n web -w   (el HPA tarda ~1-2 min en reaccionar)"
read -r -p "   [Enter cuando termines de mostrar el escalado para detener la carga] " _
kubectl delete deployment load-gen
echo "✔ Demos completadas."
