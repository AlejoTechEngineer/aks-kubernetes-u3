# 🎬 Guion del video — Azure Kubernetes Service (AKS)

> **Formato:** solo pantalla + voz (sin cámara). **Duración objetivo:** 15–18 min (mínimo exigido: 10).
> **Criterio de la rúbrica que cubre:** Excelente (20/20) = servicio en la nube + características
> diferenciadoras + ventajas y desventajas + **ejemplos de despliegue de diferentes aplicaciones**.

## ✅ Checklist previo a grabar

- [ ] Clúster creado **antes** (`scripts/01-crear-cluster.sh`, tarda 5–10 min). En el video se *muestra* el comando y el portal, no se espera.
- [ ] Un recurso extra creado desde el portal (solo para mostrar el asistente "Create Kubernetes cluster") sin confirmar la creación.
- [ ] Terminal con fuente grande (≥ 18 pt), tema oscuro, `alias k=kubectl`.
- [ ] Segunda terminal con `kubectl get pods -A -w` para ver los cambios en vivo.
- [ ] Pestañas listas: portal de Azure (panel del clúster), diagrama de arquitectura (`README.md`), tabla comparativa.
- [ ] Notificaciones del sistema silenciadas; sin datos personales ni suscripciones/IDs visibles (oculta el ID de suscripción).
- [ ] Prueba de audio de 20 s. Graba en 1080p, 30 fps (OBS Studio).
- [ ] Publicar en YouTube como **Público** (o No listado) y probar el enlace en una ventana de incógnito.

---

## ⏱️ Línea de tiempo

| Minuto | Bloque | Qué se ve en pantalla |
|---|---|---|
| 00:00–01:00 | 1. Apertura y objetivo | Diapositiva/README con título |
| 01:00–03:00 | 2. De Kubernetes a AKS + arquitectura | Diagrama mermaid del README |
| 03:00–05:30 | 3. Características diferenciadoras | Portal de Azure (panel del clúster) |
| 05:30–07:00 | 4. Creación del clúster | `01-crear-cluster.sh` + asistente del portal |
| 07:00–09:00 | 5. App 1 · Web stateless (nginx) | Terminal + navegador |
| 09:00–10:30 | 6. App 2 · Microservicios (votación propia: Python + Redis) | Terminal + navegador |
| 10:30–12:00 | 7. App 3 · Base de datos stateful (PostgreSQL) | Terminal + portal (disco) |
| 12:00–14:30 | 8. Operación Day-2 | `03-demos-operativos.sh` |
| 14:30–15:30 | 9. Observabilidad y seguridad | Portal: Insights, Policy, RBAC |
| 15:30–17:30 | 10. Ventajas, desventajas y comparativa | `docs/comparativa-aks-eks-gke.md` |
| 17:30–18:30 | 11. Cierre y preguntas al foro | Pantalla final |

---

## 1 · Apertura (0:00–1:00)

**Narración:**
> "Hola, en este video presento Azure Kubernetes Service, el servicio de Kubernetes administrado de Microsoft Azure,
> para el módulo de Contenerización de Aplicaciones de Software, Unidad 3. Vamos a ver tres cosas: primero,
> cómo funciona y qué lo diferencia; segundo, cómo desplegar **tres tipos distintos de aplicaciones** —una web sin estado,
> unos microservicios y una base de datos con estado—; y tercero, un análisis honesto de sus ventajas y desventajas
> frente a otras opciones como EKS y GKE."

## 2 · De Kubernetes a AKS (1:00–3:00)

**Mostrar:** diagrama de arquitectura del README.

**Ideas clave a narrar:**
- Kubernetes automatiza **despliegue, escalado y operación** de contenedores (Burns et al., 2016) — conectar con la Unidad 1: los contenedores resuelven empaquetado y portabilidad; el orquestador resuelve la **operación a escala**.
- **Plano de control** (API server, etcd, scheduler, controller-manager): en AKS lo **administra Azure**; el usuario no ve ni paga las VM del plano de control en el nivel Free.
- **Plano de datos**: *node pools* (VM Scale Sets) donde corren los pods; ahí sí hay responsabilidad compartida (tamaño, parches de SO según canal de actualización, etc.).
- Modelo de responsabilidad compartida → es la razón de ser de un servicio *managed*.
- Mencionar el vínculo con el material de la unidad 1: los proveedores CaaS líderes (EKS, GKE, AKS, IBM Cloud) ofrecen exactamente este modelo.

## 3 · Características diferenciadoras (3:00–5:30)

**Mostrar:** panel del clúster en el portal, recorriendo el menú izquierdo.

| Característica | Qué decir | Dónde mostrarla |
|---|---|---|
| **Niveles de servicio (Free / Standard / Premium)** | Free: sin SLA, ideal para dev/test. Standard: SLA del API server (99,95 % con zonas de disponibilidad; 99,9 % sin ellas). Premium: añade soporte extendido a largo plazo (LTS). | *Overview → Pricing tier* |
| **AKS Automatic** | Modo "opinado": Azure preconfigura nodos, red, escalado y seguridad; usa nivel Standard. Menos control, menos operación. | Asistente de creación |
| **Integración con Microsoft Entra ID + Azure RBAC** | Identidad corporativa para `kubectl` y control de acceso unificado. | *Access control* |
| **Workload Identity** | Los pods acceden a Azure (Key Vault, Storage) con identidades federadas, **sin secretos**. | *Security* |
| **Azure Monitor / Container Insights** | Métricas y logs integrados sin instalar Prometheus propio. | *Insights* |
| **Azure Policy / Defender for Containers** | Gobierno y seguridad como código sobre el clúster. | *Policies* |
| **Node pools y autoscaler** | Pools con distintas VM (incluye GPU, Spot, Windows). Cluster Autoscaler escala nodos. | *Node pools* |
| **Add-ons administrados** | Application Routing (ingress NGINX), KEDA, GitOps con Flux, Key Vault CSI driver. | *Extensions + applications* |
| **Actualizaciones controladas** | Canales de upgrade y ventanas de mantenimiento. | *Cluster configuration* |

> 💡 **Tip de calidad:** no leas la tabla; muestra 5–6 de estas pantallas con una frase de valor cada una.

## 4 · Creación del clúster (5:30–7:00)

**Mostrar:** `scripts/01-crear-cluster.sh` en el editor + el asistente del portal (sin confirmar).

**Narración (explicar cada parámetro clave):**
- `--tier free` → control plane sin costo ni SLA (demo); en producción `--tier standard`.
- `--node-count 2` + `--enable-cluster-autoscaler --min-count 2 --max-count 4` → capacidad elástica de nodos.
- `--network-plugin azure --network-plugin-mode overlay` → Azure CNI Overlay: los pods usan un rango privado y **no consumen IPs de la VNet**.
- `--enable-oidc-issuer --enable-workload-identity` → base para identidades sin secretos.
- `--enable-addons monitoring` → Container Insights.
- Terminar con `az aks get-credentials` y `kubectl get nodes -o wide` (clúster ya creado: "aquí lo tengo listo, la creación tardó ~7 minutos").

## 5 · App 1 — Web stateless (7:00–9:00)

```bash
kubectl apply -f k8s/00-namespaces.yaml
kubectl apply -f k8s/10-web-nginx.yaml
kubectl get all -n web
kubectl get svc -n web web-nginx -w      # esperar la EXTERNAL-IP
```

**Qué narrar mientras se aplica:**
- Un único YAML crea: ConfigMap, Deployment (3 réplicas), Service `LoadBalancer`, HPA y PDB.
- El Service tipo `LoadBalancer` hace que AKS cree un **Azure Load Balancer con IP pública** automáticamente → integración nativa con la nube.
- *Probes*, *requests/limits* y `securityContext` (no root, sin escalado de privilegios): "esto no es decoración, es lo que hace al despliegue apto para producción".
- Namespace con `pod-security.kubernetes.io/enforce: restricted`: si intentara correr un pod privilegiado, **sería rechazado**. (Opcional: mostrar un rechazo en vivo.)

**Mostrar en el navegador:** refrescar varias veces; el nombre del pod cambia → **balanceo de carga**.

## 6 · App 2 — Microservicios (9:00–10:30)

```bash
kubectl apply -f k8s/20-azure-vote.yaml
kubectl get pods,svc -n vote
kubectl exec -n vote deploy/azure-vote-front -- sh -c "getent hosts azure-vote-back || nslookup azure-vote-back"
```

**Narrar:**
- Dos microservicios con responsabilidades distintas: **frontend** propio en Python sobre `python:3.12-alpine` (Service `LoadBalancer`) y **backend Redis** (Service `ClusterIP`, solo interno).
- **Descubrimiento de servicios por DNS**: el front encuentra a Redis con el nombre `azure-vote-back` — sin IPs, sin configuración manual.
- Escalado **independiente**: `kubectl scale deploy/azure-vote-front -n vote --replicas=4` → se relaciona con la ventaja de microservicios vista en la Unidad 1 (escalar solo lo que lo necesita).
- Votar en la app 3–4 veces para mostrar que funciona.

## 7 · App 3 — Base de datos stateful (10:30–12:00)

```bash
# (el Secret lo crea 02-desplegar.sh; aquí mostrar solo el concepto)
kubectl get statefulset,pvc,pv -n data
kubectl get storageclass
```

**Narrar:**
- Diferencia clave **Deployment vs StatefulSet**: identidad estable (`postgres-0`), almacenamiento propio por réplica, orden de arranque.
- El `volumeClaimTemplate` pide 1 GiB con `managed-csi` → AKS crea un **Azure Managed Disk** y lo monta; **mostrarlo en el portal** (grupo de recursos `MC_...` → disco).
- Credenciales: Secret generado al vuelo, **nunca en el repositorio**; en producción → Key Vault + CSI driver + Workload Identity.
- Prueba de persistencia: se ejecuta en el bloque 8 (paso 3 del script de demos).

## 8 · Operación Day-2 (12:00–14:30)

Ejecutar `scripts/03-demos-operativos.sh` y narrar cada paso:

1. **Autocuración** — borrar un pod → el ReplicaSet lo recrea al instante. *"Declaro el estado deseado, Kubernetes lo reconcilia."*
2. **Escalado manual** — 3 → 5 réplicas; ver cómo se reparten entre nodos (`-o wide`).
3. **Persistencia** — insertar fila en PostgreSQL, matar `postgres-0`, verificar que el dato sobrevive.
4. **Rolling update** — cambiar imagen sin downtime (`maxUnavailable: 0`); `rollout history`.
5. **Rollback** — `kubectl rollout undo`.
6. **HPA** — generar carga; mostrar `kubectl get hpa -n web -w` subiendo de 3 réplicas hacia arriba. Si no hay recursos en los nodos, los pods quedan *Pending* y el **Cluster Autoscaler** añade un nodo (muy buen momento para explicar la diferencia entre HPA y Cluster Autoscaler).

> ⏱️ Si el HPA tarda, corta el video en edición (o narra el concepto mientras espera ~1–2 min).

## 9 · Observabilidad y seguridad (14:30–15:30)

**Mostrar en el portal:**
- *Insights* → CPU/memoria por nodo/pod y los pods recién escalados.
- *Logs* → una consulta KQL simple (p. ej. `ContainerLogV2 | take 20`).
- *Policies* o *Microsoft Defender* → mencionar gobierno y seguridad.
- RBAC de Kubernetes + Entra ID: "no compartimos un kubeconfig de administrador; cada persona entra con su identidad".

## 10 · Ventajas, desventajas y comparativa (15:30–17:30)

Mostrar tabla de `docs/comparativa-aks-eks-gke.md` y narrar con equilibrio:

**Ventajas**
- Plano de control administrado (menos carga operativa).
- Integración profunda con Entra ID, Azure Monitor, Policy, ACR y Key Vault.
- Buen soporte de cargas Windows y entornos .NET / empresas con ecosistema Microsoft.
- Free tier para aprender y probar; Standard con SLA para producción.
- Kubernetes certificado: portabilidad de manifiestos (CNCF).

**Desventajas / riesgos**
- **Acoplamiento a Azure** en piezas no estándar (identidad, redes, storage classes, add-ons) → la portabilidad real baja si se abusa de ellas.
- Costos fáciles de subestimar: nodos, discos, IP públicas, Log Analytics, tráfico de salida; el SLA del API server es de pago.
- **Complejidad de Kubernetes sigue ahí:** AKS no elimina la necesidad de entender redes, RBAC, requests/limits y upgrades.
- Responsabilidad compartida: los *node pools* y el ciclo de upgrades siguen siendo del equipo.
- Cambios frecuentes en flags/APIs del CLI y versiones de Kubernetes con ventanas de soporte limitadas.

**Cuándo elegirlo / cuándo no** → "Lo elegiría si la organización ya vive en Azure/Microsoft 365/Entra ID; lo evaluaría con cuidado si el requisito principal es multi-nube sin acoplamiento o si el equipo no tiene capacidad para operar Kubernetes (en ese caso considerar PaaS tipo Container Apps)."

## 11 · Cierre (17:30–18:30)

> "Resumiendo: AKS quita la parte más pesada de operar Kubernetes, pero no la responsabilidad de diseñar bien.
> Dejo el repositorio con todos los manifiestos y scripts para reproducir esta demo. Para el debate me interesa saber:
> ¿qué criterio pesa más en su elección entre AKS, EKS y GKE —costo, ecosistema, portabilidad o curva de aprendizaje—?
> Gracias, y quedo atento a sus comentarios."

---

## 🧯 Plan B si algo falla en la grabación

| Problema | Solución |
|---|---|
| EXTERNAL-IP en `<pending>` > 3 min | Cuota de IPs públicas: usar `kubectl port-forward svc/web-nginx -n web 8080:80` |
| Pod en `ImagePullBackOff` | Verificar nombre/tag de la imagen y salida a internet; en la App 2 el frontend usa `python:3.12-alpine` (la imagen `azure-vote-front:v1` ya no existe en el registro) |
| PVC en `Pending` | `kubectl describe pvc -n data`; verificar `kubectl get storageclass` |
| HPA muestra `<unknown>` | Esperar 1–2 min (metrics-server) y confirmar `resources.requests` definidos |
| Error de cuota de VM | Cambiar `NODE_SIZE` (p. ej. `Standard_D2s_v5`) o región |
