import matplotlib.pyplot as plt
import numpy as np

vCeMax = 20
iCMax = 20

vCe = np.linspace(0, vCeMax, 1000)

iCDc = 11.6 - (11.6/17.4) * vCe
iCAc = 16.5690 - (16.5690/9.9414) * vCe

pointQVce = 4.97
pointQIc = 8.2857

plt.figure(figsize=(10, 8))
plt.plot(vCe, iCDc, 'b-', linewidth=2, label='Recta de carga DC')
plt.plot(vCe, iCAc, 'r-', linewidth=2, label='Recta de carga AC')
plt.plot(pointQVce, pointQIc, 'ko', markersize=8, label='Punto Q')

plt.xlim(0, vCeMax)
plt.ylim(0, iCMax)
plt.xlabel('V_CE [V]')
plt.ylabel('I_C [mA]')
plt.title('Rectas de Carga DC y AC')
plt.grid(True, alpha=0.3)
plt.legend()

plt.annotate(f'Q({pointQVce:.3f}V, {pointQIc:.3f}mA)', 
             xy=(pointQVce, pointQIc), 
             xytext=(pointQVce-3, pointQIc+2),
             arrowprops=dict(arrowstyle='->', color='black'))

plt.tight_layout()
plt.show()
