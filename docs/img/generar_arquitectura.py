"""Genera el diagrama de arquitectura AKS legible para video/VDI.

Salidas (en esta misma carpeta):
  arquitectura-1080p.png  1920x1080
  arquitectura-4k.png     3840x2160
  arquitectura.svg

Uso:  python docs/img/generar_arquitectura.py
Requiere: matplotlib (fuente Calibri, Carlito, Arial o DejaVu Sans).
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, Rectangle

OUT = Path(__file__).resolve().parent
W, H = 1920, 1080
PT = 0.72  # 1 px = 0.72 pt a 100 dpi

# Tipografía: la primera fuente disponible de la lista
_disponibles = {f.name for f in font_manager.fontManager.ttflist}
FUENTE = next(f for f in ("Calibri", "Carlito", "Arial", "DejaVu Sans") if f in _disponibles)
plt.rcParams.update({"font.family": FUENTE, "svg.fonttype": "path"})

TXT = "#111111"
GRIS = "#333333"
AZUL, AZUL_F = "#0B4F9C", "#E3EEFA"
VERDE, VERDE_F = "#1E6B24", "#E4F3E4"
ROJO, ROJO_F = "#B23A0E", "#FCE9E1"

F_LABEL, F_TITULO, F_PRINCIPAL = 28, 36, 40  # px
LW_BORDE, LW_FLECHA = 3, 4  # px

fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(H, 0)  # y crece hacia abajo, como en píxeles
ax.axis("off")
fig.patch.set_facecolor("white")

cajas = []  # (texto, x0, y0, x1, y1) para verificar que nada se corte


def rect(x0, y0, x1, y1, borde, relleno="white", lw=LW_BORDE):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor=relleno,
                           edgecolor=borde, linewidth=lw * PT, joinstyle="miter"))


def texto(x, y, s, size=F_LABEL, bold=False, color=TXT, ha="center", va="center", limite=None):
    t = ax.text(x, y, s, fontsize=size * PT, fontweight="bold" if bold else "normal",
                color=color, ha=ha, va=va, linespacing=1.15)
    if limite:
        cajas.append((t, *limite))
    return t


def caja(x0, y0, x1, y1, titulo, detalle=None, borde=GRIS, relleno="white"):
    rect(x0, y0, x1, y1, borde, relleno)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    lim = (x0 + 8, y0 + 4, x1 - 8, y1 - 4)
    if detalle:
        texto(cx, cy - 2, titulo, bold=True, va="bottom", limite=lim)
        texto(cx, cy + 2, detalle, va="top", limite=lim)
    else:
        texto(cx, cy, titulo, bold=True, limite=lim)


def zona(x0, y0, x1, y1, titulo, borde, relleno, size=F_TITULO, lateral=False):
    rect(x0, y0, x1, y1, borde, relleno)
    if lateral:  # título en una franja a la izquierda, arriba
        texto(x0 + 20, y0 + 15, titulo, size=size, bold=True, color=borde,
              ha="left", va="top", limite=(x0, y0, x1, y1))
    else:
        texto(x0 + 20, y0 + 12, titulo, size=size, bold=True, color=borde,
              ha="left", va="top", limite=(x0, y0, x1, y1))


def flecha(p0, p1, punta=True, discontinua=False, color=TXT):
    ax.add_patch(FancyArrowPatch(
        p0, p1, arrowstyle="-|>" if punta else "-", mutation_scale=34 * PT,
        linewidth=LW_FLECHA * PT, color=color, shrinkA=0, shrinkB=0,
        linestyle=(0, (4, 2.5)) if discontinua else "-", joinstyle="miter"))


def linea(xs, ys, color=TXT):
    ax.plot(xs, ys, color=color, linewidth=LW_FLECHA * PT, solid_capstyle="butt")


# ---------------------------------------------------------------- título
texto(40, 48, "Arquitectura de la solución en Azure Kubernetes Service (AKS)",
      size=F_PRINCIPAL, bold=True, ha="left", limite=(40, 20, 1880, 80))

# ---------------------------------------------------------------- actores
caja(40, 220, 320, 350, "Ingeniero", "kubectl · az cli\nportal")
caja(40, 905, 320, 1035, "Usuario final", "Internet")

# ---------------------------------------------------------------- plano de control
zona(360, 95, 1240, 425, "Plano de control · administrado por Azure", AZUL, AZUL_F)
caja(400, 240, 660, 330, "kube-apiserver", borde=AZUL)
for y0, nombre in ((165, "etcd"), (255, "scheduler"), (345, "controller-manager")):
    caja(760, y0, 1200, y0 + 60, nombre, borde=AZUL)
linea([660, 710], [285, 285])
linea([710, 710], [195, 375])
for y in (195, 285, 375):
    linea([710, 760], [y, y])

# ---------------------------------------------------------------- leyenda
rect(1280, 95, 1880, 425, GRIS)
texto(1300, 107, "Leyenda", size=F_TITULO, bold=True, ha="left", va="top",
      limite=(1280, 95, 1880, 425))
items = [
    (AZUL, AZUL_F, "Plano de control (lo opera Azure)"),
    (VERDE, VERDE_F, "Plano de datos (compartido)"),
    (ROJO, ROJO_F, "Servicios administrados de Azure"),
]
for i, (borde, relleno, s) in enumerate(items):
    y = 185 + i * 50
    rect(1305, y - 16, 1355, y + 16, borde, relleno)
    texto(1375, y, s, ha="left", limite=(1280, 95, 1870, 425))
flecha((1305, 335), (1360, 335))
texto(1375, 335, "Petición / tráfico", ha="left", limite=(1280, 95, 1870, 425))
flecha((1305, 385), (1360, 385), discontinua=True)
texto(1375, 385, "Telemetría / identidad", ha="left", limite=(1280, 95, 1870, 425))

# ---------------------------------------------------------------- plano de datos
zona(360, 470, 1880, 800,
     "Plano de datos · Node pool (VM Scale Set + Cluster Autoscaler)", VERDE, VERDE_F)
zona(390, 545, 710, 775, "namespace web", VERDE, "white", size=F_TITULO)
zona(750, 545, 1450, 775, "namespace vote", VERDE, "white", size=F_TITULO)
zona(1490, 545, 1850, 775, "namespace data", VERDE, "white", size=F_TITULO)
caja(430, 615, 680, 745, "nginx ×3–10", "HPA + PDB", borde=VERDE, relleno=VERDE_F)
caja(780, 615, 1020, 745, "azure-vote-front", "×2", borde=VERDE, relleno=VERDE_F)
caja(1170, 615, 1420, 745, "azure-vote-back", "Redis · ClusterIP", borde=VERDE, relleno=VERDE_F)
caja(1510, 615, 1830, 745, "postgres-0", "StatefulSet\nPVC 1 GiB", borde=VERDE, relleno=VERDE_F)
flecha((1020, 680), (1170, 680))
texto(1095, 668, "DNS\ninterno", va="bottom", limite=(1025, 600, 1165, 680))

# ---------------------------------------------------------------- servicios de Azure
zona(360, 875, 1880, 1060, "Servicios\nde Azure", ROJO, ROJO_F, lateral=True)
caja(580, 905, 950, 1035, "Azure Load Balancer", "IP pública", borde=ROJO)
caja(990, 905, 1270, 1035, "Azure Monitor", "Container Insights", borde=ROJO)
caja(1310, 905, 1600, 1035, "Microsoft Entra ID", "Workload Identity", borde=ROJO)
caja(1640, 905, 1850, 1035, "Managed Disk", "managed-csi", borde=ROJO)

# ---------------------------------------------------------------- relaciones
flecha((320, 285), (400, 285))            # Ingeniero -> kube-apiserver
flecha((530, 330), (530, 470))            # kube-apiserver -> node pool
flecha((320, 1010), (580, 1010))            # Usuario -> Load Balancer
flecha((640, 905), (640, 745))            # Load Balancer -> nginx
flecha((900, 905), (900, 745))            # Load Balancer -> azure-vote-front
linea([1745, 1745], [745, 905])           # postgres-0 --- Managed Disk
flecha((1130, 800), (1130, 905), discontinua=True)   # métricas y logs -> Monitor
texto(1145, 836, "métricas y logs", ha="left", limite=(1140, 805, 1440, 870))
flecha((1455, 905), (1455, 800), discontinua=True)   # Entra ID -> pods
texto(1470, 836, "identidad", ha="left", limite=(1465, 805, 1730, 870))


# ---------------------------------------------------------------- verificación
def verificar():
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    inv = ax.transData.inverted()
    errores = []
    for t, x0, y0, x1, y1 in cajas:
        bb = t.get_window_extent(r)
        (ax0, ay1), (ax1, ay0) = inv.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)])
        if ax0 < x0 or ax1 > x1 or ay0 < y0 or ay1 > y1:
            errores.append(f"{t.get_text()!r}: texto ({ax0:.0f},{ay0:.0f})-({ax1:.0f},{ay1:.0f}) "
                           f"fuera de ({x0},{y0})-({x1},{y1})")
    return errores


if __name__ == "__main__":
    print("Fuente:", FUENTE)
    problemas = verificar()
    for p in problemas:
        print("TEXTO CORTADO:", p)
    fig.savefig(OUT / "arquitectura-1080p.png", dpi=100, facecolor="white")
    fig.savefig(OUT / "arquitectura-4k.png", dpi=200, facecolor="white")
    fig.savefig(OUT / "arquitectura.svg", facecolor="white")
    print("OK" if not problemas else f"{len(problemas)} problema(s)")
