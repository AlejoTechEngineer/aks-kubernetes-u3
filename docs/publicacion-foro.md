# 📝 Publicación para el foro — Unidad 3

> Regla del foro: **no incluir datos personales**. Este texto solo expone contenido técnico y el enlace público del video/repositorio.
> Reemplaza los marcadores `[ ... ]` antes de publicar.

---

**Asunto:** Azure Kubernetes Service (AKS): despliegue de tres tipos de aplicaciones, características diferenciadoras y análisis crítico

Estimados compañeros y tutor:

Para la actividad de la Unidad 3 seleccioné **Azure Kubernetes Service (AKS)**, el servicio de orquestación Kubernetes administrado de Microsoft Azure. En el video analizo su funcionamiento y demuestro el despliegue de **tres cargas de trabajo distintas** sobre un mismo clúster:

1. **Aplicación web sin estado** (nginx): Deployment, Service `LoadBalancer`, ConfigMap, probes, autoescalado horizontal (HPA) y PodDisruptionBudget.
2. **Microservicios** (mini-aplicación propia de votación: frontend en Python sobre `python:3.12-alpine` + Redis): descubrimiento de servicios por DNS interno y escalado independiente.
3. **Base de datos con estado** (PostgreSQL): StatefulSet con volumen persistente sobre Azure Disk y prueba de supervivencia a reinicios.

Además muestro operación "día 2": autocuración, escalado, persistencia, *rolling update* sin downtime, *rollback* y autoescalado de pods con HPA. El clúster usa 2 nodos fijos `Standard_D2s_v6` por el cupo de 4 vCPU de la suscripción de prueba.

**🎥 Video:** https://youtu.be/Cu-VVzfo1dg
**📦 Repositorio con manifiestos y scripts reproducibles:** https://github.com/AlejoTechEngineer/aks-kubernetes-u3

### Ideas centrales del análisis

- **Qué resuelve AKS:** Azure administra el plano de control (API server, etcd, scheduler); el equipo se concentra en los *node pools* y las aplicaciones. Esto aplica el modelo CaaS descrito en la lectura de la Unidad 1.
- **Diferenciadores:** integración nativa con Microsoft Entra ID, Workload Identity, Azure Monitor, Azure Policy, add-ons administrados (ingress, KEDA, GitOps) y modos de operación como AKS Automatic. Niveles Free / Standard / Premium con SLA para producción en los niveles de pago.
- **Ventajas:** menor carga operativa, gobierno e identidad integrados, buen encaje con ecosistemas Microsoft/.NET.
- **Desventajas:** acoplamiento a Azure en las piezas no estándar, costos secundarios fáciles de subestimar (discos, IPs, logs, egress) y una curva de aprendizaje de Kubernetes que no desaparece por ser *managed*.

### Preguntas para el debate

1. Si la prioridad fuera **portabilidad multi-nube**, ¿qué prácticas (Helm, Kustomize, Crossplane, evitar add-ons propietarios) reducirían el *lock-in* con el que cada servicio (EKS, GKE, AKS) nos "ata" a su ecosistema?
2. ¿Qué pesa más en la decisión real de una organización: **costo total, ecosistema, SLA o experiencia del equipo**? ¿Por qué?
3. ¿Qué experiencias han tenido con los **upgrades de versión** de Kubernetes en servicios administrados?

Agradezco sus comentarios y críticas; responderé a cada aporte con argumentos y referencias.

**Referencias**
- Burns, B., Grant, B., Oppenheimer, D., Brewer, E., & Wilkes, J. (2016). Borg, Omega, and Kubernetes. *ACM Queue, 14*(1), 70–93.
- Merkel, D. (2014). Docker: lightweight Linux containers for consistent development and deployment. *Linux Journal, 2014*(239).
- Microsoft. (s. f.). *Azure Kubernetes Service (AKS) documentation*. Microsoft Learn. https://learn.microsoft.com/azure/aks/
- The Kubernetes Authors. (s. f.). *Kubernetes documentation*. https://kubernetes.io/docs/
- [Añadir aquí la lectura fundamental de la Unidad 3 con su año/autor exactos]
