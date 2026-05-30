import os
import matplotlib.pyplot as plt
import numpy as np

os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'figures'), exist_ok=True)
fig_path = os.path.join(os.path.dirname(__file__), '..', 'figures', 'ch4_n2_selectivity_vs_temperature.png')

# Data
temps = np.array([273, 298, 313])
selectivity = np.array([36.69, 10.74, 62.85])

# Styling
try:
    plt.style.use('seaborn-whitegrid')
except Exception:
    try:
        import seaborn as sns
        sns.set_style('whitegrid')
    except Exception:
        plt.style.use('default')

plt.rcParams.update({'font.size': 10, 'font.family': 'sans-serif'})

fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(temps, selectivity, marker='o', linestyle='-', color='#1f77b4', linewidth=1.5, markersize=6)

# Value labels
for x, y in zip(temps, selectivity):
    ax.annotate(f'{y:.2f}', xy=(x, y), xytext=(0, 8), textcoords='offset points', ha='center', fontsize=9)

# Vertical dashed validation line at 298K
ax.axvline(298, color='gray', linestyle='--', linewidth=1)
ax.text(298, ax.get_ylim()[1]*0.95, 'Validation Temperature', rotation=90, va='top', ha='right', fontsize=9, color='gray')

# Annotations
ax.annotate('Matches literature (~11.7)', xy=(298, 10.74), xytext=(300, 20), arrowprops=dict(arrowstyle='->', lw=0.8), fontsize=9)
ax.annotate('Possible N2 interpolation instability', xy=(313, 62.85), xytext=(305, 50), arrowprops=dict(arrowstyle='->', lw=0.8), fontsize=9)

ax.set_xlabel('Temperature (K)')
ax.set_ylabel('CH4/N2 Selectivity')
ax.set_title('Al-Fum CH4/N2 Selectivity vs Temperature')
ax.text(0.5, 1.02, 'pyIAST prediction using experimental CH4 and N2 isotherms', transform=ax.transAxes, ha='center', fontsize=9)

ax.grid(True, linestyle=':', linewidth=0.6)
ax.set_xticks(temps)

# Bottom note
plt.subplots_adjust(bottom=0.18)
fig.text(0.5, 0.02, '273 K and 313 K should be interpreted cautiously due to low-loading N2 interpolation effects.', ha='center', fontsize=8)

plt.tight_layout()
plt.savefig(os.path.abspath(fig_path), dpi=300)
print('Saved', fig_path)
