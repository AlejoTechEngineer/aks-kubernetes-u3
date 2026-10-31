# 🧠 Mapa mental — Servicios de orquestación Kubernetes en la nube

> **Rúbrica (10 pts):**
> 10 = análisis claro + estructura definida + completo + aporta análisis propio sobre lo que mostraron los compañeros ·
> 9 = análisis, estructura no definida · 6 = recoge lo aportado, estructura definida · 3 = solo lista servicios · 0 = no presenta.
>
> **Claves para el 10/10:** (1) un **nodo por cada servicio elegido por los compañeros** (no solo el tuyo),
> (2) **las mismas ramas hijas en todos** (estructura definida y comparable),
> (3) una rama **"Análisis propio"** con conclusiones que *no* están en los videos (comparativa, recomendación por escenario).

## Versión base (completa con tu servicio; añade los de los compañeros)

```mermaid
mindmap
  root((Kubernetes gestionado en la nube))
    AKS Azure
      Funcionamiento
        Plano de control administrado por Azure
        Node pools en VM Scale Sets
        kubectl y az aks
      Componentes
        API server etcd scheduler
        Azure CNI Overlay
        Managed Disks y Azure Files
        Azure Container Registry
      Diferenciadores
        Microsoft Entra ID y Azure RBAC
        Workload Identity
        Azure Monitor Insights
        Azure Policy
        AKS Automatic
      Ventajas
        Menor carga operativa
        Ecosistema Microsoft y NET
        Free tier para pruebas
      Desventajas
        Acoplamiento a Azure
        Costos secundarios
        Complejidad de K8s persiste
      Despliegue
        Web stateless
        Microservicios
        StatefulSet con disco
    EKS AWS
      Funcionamiento
      Componentes
      Diferenciadores
      Ventajas
      Desventajas
      Despliegue
    GKE Google
      Funcionamiento
      Componentes
      Diferenciadores
      Ventajas
      Desventajas
      Despliegue
    Otro servicio de companero
      Funcionamiento
      Componentes
      Diferenciadores
      Ventajas
      Desventajas
      Despliegue
    Analisis propio
      Criterios de decision
        Costo
        Ecosistema
        Portabilidad
        Curva de aprendizaje
        Madurez de upgrades
      Recomendacion por escenario
        Organizacion Microsoft
        Startup en AWS
        Cargas de datos e IA
        Multi nube
      Riesgos comunes
        Lock in
        FinOps
        Seguridad de secretos
      Conclusiones
```

## 🔧 Procedimiento para completarlo (después de ver los videos)

1. Crea una **hoja de captura** por servicio con las seis ramas fijas: *Funcionamiento · Componentes · Diferenciadores · Ventajas · Desventajas · Despliegue*.
2. Mientras ves cada video, escribe en cada rama **1–3 frases cortas con lo que realmente mostró** el compañero (así el mapa "muestra lo aportado").
3. Sustituye los nodos vacíos de `EKS`, `GKE` y `Otro servicio` por esas frases; duplica el bloque por cada servicio nuevo.
4. En **"Análisis propio"** agrega tu valor: compara, detecta patrones (p. ej. "los tres servicios administran el plano de control pero difieren en quién gestiona los nodos") y da recomendaciones por escenario.
5. Verifica que **ninguna rama quede vacía** (rúbrica: "se ve completo").

## 🖼️ Cómo obtener la imagen para el foro

- **Rápido:** pega el bloque `mermaid` en <https://mermaid.live> y exporta **PNG/SVG**.
- **Alternativa visual:** reconstruirlo en XMind, Miro, draw.io o Canva con la misma estructura (centro → 5 ramas principales → 6 sub-ramas fijas).
- Sube la imagen en el hilo del foro **y** enlaza el archivo `.md` del repositorio.

> Consejo: usa **un color por servicio** y mantén el orden de las sub-ramas idéntico en todos; es lo que hace que la "estructura esté definida".
