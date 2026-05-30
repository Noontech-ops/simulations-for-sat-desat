import os
import matplotlib.pyplot as plt
import os

os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'figures'), exist_ok=True)
fig_path = os.path.join(os.path.dirname(__file__), '..', 'figures', 'validation_literature_vs_simulation.png')

# Data
temps = [273, 298]
literature = [17.2, 11.7]
simulation = [36.69, 10.74]

# Plot
try:
    plt.style.use('seaborn-whitegrid')
except Exception:
    try:
        import seaborn as sns
        sns.set_style('whitegrid')
    except Exception:
        plt.style.use('default')
fig, ax = plt.subplots(figsize=(6, 4))

import numpy as np
x = np.arange(len(temps))
width = 0.35

bars1 = ax.bar(x - width/2, literature, width, label='Literature (Huang et al.)', color='#2b8cbe')
bars2 = ax.bar(x + width/2, simulation, width, label='Simulation (pyIAST)', color='#f03b20')

# Labels and title
ax.set_xlabel('Temperature (K)')
ax.set_ylabel('CH4/N2 Selectivity')
ax.set_title('Al-Fum CH4/N2 Selectivity: Literature vs Simulation')
# Subtitle via text
ax.text(0.5, 1.02, 'Validation of pyIAST model against Huang et al.', transform=ax.transAxes, ha='center', fontsize=9)

ax.set_xticks(x)
ax.set_xticklabels([str(t) for t in temps])
ax.legend()

# Value labels
def autolabel(bars, ax):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 6),
                    textcoords='offset points',
                    ha='center', va='bottom', fontsize=8)

autolabel(bars1, ax)
autolabel(bars2, ax)

plt.tight_layout()
plt.savefig(os.path.abspath(fig_path), dpi=300)
print('Saved', fig_path)
