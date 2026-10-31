# 💬 Comentarios a compañeros y respuestas — Guía de alto nivel

> **Rúbrica (20 pts):** 20 = analizas y comentas **con justificación bibliográfica** las ventajas y desventajas del servicio de **tres** compañeros.
> 15 = dos compañeros · 10 = uno con bibliografía · 5 = uno sin bibliografía.
> 👉 **Meta: comentar a 3 compañeros** (si puedes, 4, por si alguno no cumple), cada uno con **al menos 2 fuentes**.

> ⚠️ Esto es una **guía y banco de argumentos**, no un comentario para pegar tal cual. Debes ver cada video y
> personalizar con detalles *concretos* de lo que mostró el compañero (un comentario genérico se nota y pierde puntos).
> Los datos de precios/SLA/funciones cambian: **verifica en la documentación oficial** antes de citarlos.

---

## 1 · Método de 5 pasos (≈ 25 min por compañero)

1. **Ver el video con una hoja de notas** (3 columnas: *servicio y componentes · lo que mostró · lo que faltó*).
2. **Reconocer** algo específico y bien hecho (p. ej. "mostraste el HPA reaccionando al minuto 9").
3. **Analizar ventajas y desventajas del servicio que eligió** (no del tuyo): mínimo 2 y 2.
4. **Contrastar con tu servicio (AKS)** en 1–2 dimensiones: costo, identidad, red, portabilidad, operación.
5. **Cerrar con una pregunta abierta** que invite al debate (así se genera el "debate académico" que pide la actividad).

## 2 · Estructura del comentario (150–250 palabras)

```
Hola [nombre], excelente trabajo con [servicio]. [Reconocimiento específico del video, con minuto].

Ventajas que identifico: (1) ... (2) ... [fuente].
Desventajas / riesgos: (1) ... (2) ... [fuente].

Comparado con AKS, [contraste puntual en 1–2 dimensiones].

Una pregunta para el debate: [pregunta abierta].

Referencias: [APA, 2–3 fuentes]
```

**Tono:** respetuoso, argumentado, crítico pero constructivo. Evita "está mal"; usa "una limitación a considerar es…" o "¿qué ocurriría si…?".

---

## 3 · Banco de argumentos por servicio (verifica cada dato antes de usarlo)

### Amazon EKS (AWS)
| Ventajas | Desventajas / riesgos |
|---|---|
| Integración con IAM, VPC, ELB/ALB, EBS/EFS, CloudWatch; mayor cuota de mercado cloud → muchos casos y talento disponible | Suele requerir **más configuración manual** (add-ons, red, controladores) que otras opciones; la curva de entrada es mayor |
| Opciones de cómputo: nodos administrados, Fargate (serverless), Karpenter, y modo automatizado (*EKS Auto Mode*) | El **plano de control tiene tarifa por clúster** además del cómputo |
| Pods con IPs de la VPC (VPC CNI): integración de red muy directa | Consumo alto de IPs de la VPC si no se planifica; límites de pods por nodo según tipo de instancia |
| Fuerte para ecosistemas AWS (RDS, SQS, S3, IAM Roles for Service Accounts / Pod Identity) | Acoplamiento a AWS en identidad, red y storage; versiones con ventanas de soporte (soporte extendido con costo adicional) |

**Contraste con AKS:** identidad (Entra ID/Workload Identity vs IAM/IRSA o Pod Identity), costo del plano de control (AKS Free vs tarifa fija de EKS), red (CNI Overlay vs VPC CNI).

### Google Kubernetes Engine (GKE)
| Ventajas | Desventajas / riesgos |
|---|---|
| Kubernetes nació en Google a partir de la experiencia con Borg (Burns et al., 2016) → madurez e innovación temprana | Mayor dependencia de GCP (IAM, VPC, Cloud Logging) |
| Modo **Autopilot** (Google gestiona nodos; se paga por recursos de pods) y modo Standard | Autopilot impone restricciones (privilegios, DaemonSets, ciertos *hostPath*) |
| Canales de versiones (rapid/regular/stable) con upgrades administrados; networking avanzado (Dataplane V2) | Menor presencia en organizaciones centradas en Microsoft; integración con Windows menos central |
| Fuertes capacidades de multiclúster / malla de servicios administrada | La facturación (Autopilot vs Standard, tarifa de gestión) requiere análisis cuidadoso |

**Contraste con AKS:** modelo "Autopilot vs AKS Automatic", madurez de upgrades, integración con identidad corporativa.

### Otros posibles (OpenShift/ARO/ROSA, IBM Cloud Kubernetes Service, DigitalOcean DOKS, Oracle OKE, Rancher/RKE2)
| Ventajas | Desventajas / riesgos |
|---|---|
| OpenShift: plataforma "batteries-included" (CI/CD, registry, seguridad por defecto, SCC) | Licenciamiento/costo superior; se aparta de Kubernetes "vanilla" en ciertos aspectos |
| DOKS/OKE/IBM: costos o integraciones específicas, simplicidad (DOKS) | Ecosistema de servicios gestionados más reducido; menos opciones empresariales |
| Rancher/RKE2: gestión multiclúster y on-premise/híbrido | Mayor carga operativa propia (tú administras el plano de control) |

---

## 4 · Bibliografía sugerida (formato APA 7) — solo fuentes verificables

- Burns, B., Grant, B., Oppenheimer, D., Brewer, E., & Wilkes, J. (2016). Borg, Omega, and Kubernetes. *ACM Queue, 14*(1), 70–93.
- Burns, B., Beda, J., Hightower, K., & Evenson, L. (2022). *Kubernetes: Up & Running* (3.ª ed.). O'Reilly Media.
- Merkel, D. (2014). Docker: lightweight Linux containers for consistent development and deployment. *Linux Journal, 2014*(239).
- Boettiger, C. (2015). An introduction to Docker for reproducible research. *ACM SIGOPS Operating Systems Review, 49*(1), 71–79.
- The Kubernetes Authors. (s. f.). *Kubernetes documentation*. https://kubernetes.io/docs/
- Microsoft. (s. f.). *Azure Kubernetes Service (AKS) documentation*. https://learn.microsoft.com/azure/aks/
- Amazon Web Services. (s. f.). *Amazon EKS User Guide*. https://docs.aws.amazon.com/eks/
- Google Cloud. (s. f.). *Google Kubernetes Engine documentation*. https://cloud.google.com/kubernetes-engine/docs
- **Lectura fundamental de la Unidad 3** (cítala siempre: la rúbrica pide "con base en los recursos de la unidad").

> Para la fecha de acceso de las páginas web, usa el día en que las consultes (formato APA: "Recuperado el día de mes de año, de URL").

---

## 5 · Ejemplo de comentario (**plantilla ilustrativa — adaptar al video real**)

> Hola [Nombre], gracias por tu presentación sobre **Amazon EKS**; me pareció muy útil que mostraras [detalle concreto del video, min X] porque ilustra cómo se integra el balanceador con el servicio.
>
> **Ventajas:** la integración con IAM y VPC permite aplicar el principio de mínimo privilegio a nivel de pod, algo especialmente valioso en entornos regulados (Kubernetes Authors, s. f.; AWS, s. f.). Además, contar con varias opciones de cómputo (nodos administrados, Fargate) permite ajustar el nivel de operación que el equipo quiere asumir.
> **Desventajas:** como señalas, la configuración inicial exige más piezas (add-ons, red, controladores), lo que eleva la curva de aprendizaje; y el plano de control tiene un costo fijo por clúster que en entornos de muchos clústeres pequeños puede pesar en el presupuesto.
>
> **Contraste con AKS:** en mi caso, el nivel Free permite experimentar sin costo de gestión del plano de control, pero sin SLA; en EKS no existe un equivalente directo, lo que cambia la estrategia para entornos de desarrollo.
>
> ¿Consideras que el costo adicional de gestión se compensa con la integración IAM en tu escenario? ¿Qué estrategia usarías para reducir el acoplamiento con AWS?
>
> *Referencias:* The Kubernetes Authors. (s. f.). *Kubernetes documentation*. https://kubernetes.io/docs/ · Amazon Web Services. (s. f.). *Amazon EKS User Guide*. https://docs.aws.amazon.com/eks/

---

## 6 · Responder a los aportes recibidos (Participación 3)

**Regla:** responde **a todos**, con argumentos, dentro de las 24–48 h posteriores al comentario, y siempre aporta algo nuevo (dato, fuente, ejemplo).

```
Gracias, [nombre], por tu observación sobre [punto exacto].

[Si tiene razón]  Tienes razón en que [...]; ampliaría el punto con [dato/fuente].
[Si discrepas con respeto]  Entiendo tu perspectiva; sin embargo, [argumento + fuente]. Quizá la diferencia está en [supuesto/escenario].

[Aporte nuevo: cómo se resolvería en la práctica, comando, configuración o referencia].

¿Cómo lo ves en un escenario de [caso específico]?
```

**Ejemplos de objeciones previsibles y cómo abordarlas**

| Objeción probable | Respuesta argumentada |
|---|---|
| "AKS te ata a Azure" | Cierto en piezas propietarias (identidad, storage class, add-ons). Mitigación: manifiestos estándar, Helm/Kustomize, evitar CRDs propietarios, IaC con Terraform/Bicep, y probar la portabilidad en CI. |
| "El Free tier no sirve para producción" | Exacto: sin SLA financiero. Se usa para dev/test; producción → Standard (SLA del API server, 99,95 % con zonas). Verifica la cifra vigente en la documentación. |
| "Kubernetes es excesivo para esta app" | Válido; para cargas simples, PaaS de contenedores (p. ej. Azure Container Apps, Cloud Run) reduce la operación. K8s se justifica con muchos servicios, necesidades de control fino o portabilidad. |
| "¿Por qué no usar Docker Compose?" | Compose resuelve el entorno de un solo host; no ofrece autocuración multi-nodo, rolling updates ni autoescalado (Unidad 2 vs Unidad 3). |
| "¿Y la seguridad de los secretos?" | En la demo se genera el Secret al vuelo; en producción: Key Vault + CSI driver + Workload Identity, y cifrado en reposo. |
