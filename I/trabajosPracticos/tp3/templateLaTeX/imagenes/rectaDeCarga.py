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
    ax.annotate('Q', (puntoQ[0], puntoQ[1]), xytext=(5, 5), 
                textcoords='offset points', fontsize=24, fontweight='bold')

ax.set_xlabel('$v_{CE}$ (V)', fontsize=24)
ax.set_ylabel('$i_C$ (mA)', fontsize=24)
ax.tick_params(axis='both', which='major', labelsize=24)
ax.set_xlim(0, 16)
ax.set_ylim(0, 17)
ax.legend(fontsize=24)

rao.tight_layout()
rao.savefig('rectaDeCargas.png', dpi=1200, bbox_inches='tight')
rao.close()
