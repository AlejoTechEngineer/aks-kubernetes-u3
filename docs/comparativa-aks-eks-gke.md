# ⚖️ Comparativa AKS · EKS · GKE

> Los valores económicos, SLA y funciones **cambian con frecuencia**. Esta tabla describe *tendencias de diseño*;
> antes de citar cifras en el video o el foro, confirma en la documentación oficial y anota la fecha de consulta.

## Matriz técnica

| Dimensión | **AKS** (Azure) | **EKS** (AWS) | **GKE** (Google Cloud) |
|---|---|---|---|
| Plano de control | Administrado por Azure | Administrado por AWS | Administrado por Google |
| Costo del plano de control | Nivel **Free** sin costo de gestión (sin SLA); **Standard/Premium** con tarifa por clúster y SLA | Tarifa por clúster | Depende del modo y la configuración (revisar capa gratuita vigente) |
| SLA del API server | Free: ninguno; Standard: 99,95 % con zonas de disponibilidad, 99,9 % sin ellas | SLA publicado por AWS | SLA según modo/regional vs zonal |
| Modo "casi sin nodos" | **AKS Automatic** (preconfigurado, nivel Standard) | **EKS Auto Mode** | **Autopilot** |
| Identidad de usuarios | Microsoft Entra ID + Azure RBAC | IAM (+ mapeo a RBAC de K8s) | Google IAM |
| Identidad de pods | Workload Identity (federada) | IRSA / EKS Pod Identity | Workload Identity Federation |
| Red de pods | Azure CNI (Overlay o VNet), kubenet como opción heredada | VPC CNI (IPs de la VPC) | VPC-native; Dataplane V2 (Cilium) |
| Almacenamiento block | Azure Disk (CSI, `managed-csi`) | EBS (CSI) | Persistent Disk (CSI) |
| Observabilidad nativa | Azure Monitor / Container Insights | CloudWatch Container Insights | Cloud Operations (Logging/Monitoring) |
| Escalado de nodos | Cluster Autoscaler / Node Auto Provisioning | Cluster Autoscaler / **Karpenter** | Cluster Autoscaler / Node Auto-provisioning |
| Contenedores Windows | Soporte maduro | Soportado | Soportado (menor foco) |
| Fortaleza percibida | Ecosistema Microsoft, identidad corporativa, .NET | Amplitud de servicios y comunidad | Madurez y origen de Kubernetes, multiclúster |
| Riesgo principal | Acoplamiento a Entra/Azure en piezas no estándar | Más piezas que configurar; consumo de IPs | Restricciones de Autopilot; menor encaje en org. Microsoft |

## Matriz de decisión ponderada (ejemplo editable)

Asigna pesos según el escenario (suman 100). Puntúa 1–5 cada servicio con evidencia.

| Criterio | Peso | AKS | EKS | GKE |
|---|---:|---:|---:|---:|
| Integración con el ecosistema actual de la organización | 30 | | | |
| Costo total (cómputo + gestión + datos + observabilidad) | 20 | | | |
| Operación y madurez de upgrades | 15 | | | |
| Seguridad e identidad | 15 | | | |
| Portabilidad / riesgo de lock-in | 10 | | | |
| Experiencia previa del equipo | 10 | | | |
| **Total ponderado** | **100** | | | |

> Úsala en la rama "Análisis propio" del mapa mental: es lo que convierte la lista de servicios en **análisis**.

## Principios que se repiten en los tres (útil para la conclusión)

1. El **plano de control es administrado**; el plano de datos es responsabilidad compartida.
2. Los manifiestos de Kubernetes (Deployment, Service, StatefulSet, HPA…) son **portables**; lo que no se porta son identidad, red, storage classes y add-ons propietarios.
3. El costo real está en **nodos, discos, IPs, tráfico saliente y observabilidad**, no solo en la tarifa del clúster.
4. Para cargas simples, un PaaS de contenedores (Azure Container Apps, Cloud Run, App Runner) puede ser más racional que Kubernetes.
