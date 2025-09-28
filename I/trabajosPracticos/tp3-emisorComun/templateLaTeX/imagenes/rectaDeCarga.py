import matplotlib.pyplot as rao
import numpy as manolo

def calcularPuntoInterseccion(x1, y1, x2, y2, x3, y3, x4, y4):
    denominador = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominador == 0:
        return None
    
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominador
    puntoX = x1 + t * (x2 - x1)
    puntoY = y1 + t * (y2 - y1)
    return puntoX, puntoY

fig, ax = rao.subplots(figsize=(10, 8))

rectaCaX = manolo.array([0, 8.49])
rectaCaY = manolo.array([15.58, 0])

rectaCcX = manolo.array([0, 15])
rectaCcY = manolo.array([10.86, 0])

puntoQ = calcularPuntoInterseccion(rectaCaX[0], rectaCaY[0], rectaCaX[1], rectaCaY[1],
                                  rectaCcX[0], rectaCcY[0], rectaCcX[1], rectaCcY[1])

ax.plot(rectaCaX, rectaCaY, 'r-', linewidth=2, label='recta de carga CA')
ax.plot(rectaCcX, rectaCcY, 'b-', linewidth=2, label='recta CC')

if puntoQ:
    ax.plot(puntoQ[0], puntoQ[1], 'ko', markersize=8)
    
    # Líneas de puntos para mostrar las coordenadas
    ax.axvline(x=puntoQ[0], color='gray', linestyle='--', alpha=0.7)
    ax.axhline(y=puntoQ[1], color='gray', linestyle='--', alpha=0.7)
    
    # Anotación del punto Q con sus coordenadas
    ax.annotate(f'Q({puntoQ[0]:.2f}, {puntoQ[1]:.2f})', 
                (puntoQ[0], puntoQ[1]), xytext=(10, 10), 
                textcoords='offset points', fontsize=20, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

ax.set_xlabel('$v_{CE}$ (V)', fontsize=24)
ax.set_ylabel('$i_C$ (mA)', fontsize=24)
ax.tick_params(axis='both', which='major', labelsize=24)
ax.set_xlim(0, 16)
ax.set_ylim(0, 17)
ax.legend(fontsize=24)

rao.tight_layout()
rao.savefig('rectaDeCargas.png', dpi=1200, bbox_inches='tight')
rao.close()
