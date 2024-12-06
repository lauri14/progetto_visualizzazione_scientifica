import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Dati
years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
eu27 = [23.5, 21.8, 20.1, 18.0, 16.1, 15.1, 16.8, 16.6, 14.5, 14.5]
italy = [42.7, 40.3, 37.8, 34.7, 32.2, 29.1, 29.7, 29.7, 23.7, 22.7]

# Crea il grafico
plt.figure(figsize=(12, 7))

# Applica uno stile Seaborn (opzionale)
sns.set_theme(style="whitegrid") 

# Linee dei dati
plt.plot(years, eu27, marker='o', label='EU27 Youth Unemployment (%)', color='#1f77b4', linewidth=2)
plt.plot(years, italy, marker='o', label='Italy Youth Unemployment (%)', color='#d62728', linewidth=2)

# Evidenziazione delle differenze
plt.fill_between(years, eu27, italy, where=(np.array(italy) > np.array(eu27)), 
                 color='#FFC04C', alpha=0.4, label='Difference (Italy > EU27)')

# Etichette personalizzate
for i, (y_eu, y_it) in enumerate(zip(eu27, italy)):
    if not np.isnan(y_it) and not np.isnan(y_eu):
        plt.text(years[i], y_it + 1, f"{y_it:.1f}%", color='#d62728', fontsize=10, ha='center')
        plt.text(years[i], y_eu - 1, f"{y_eu:.1f}%", color='#1f77b4', fontsize=10, ha='center')

# Titolo e descrizione
plt.title('Youth Unemployment Rates in Italy vs EU27 (2014-2023)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Unemployment Rate (%)', fontsize=14)

# Personalizzazione degli assi
plt.xticks(years, fontsize=12, rotation=45)
plt.yticks(np.arange(10, 50, 5), fontsize=12)
plt.ylim(10, 50)

# Legenda e griglia
plt.legend(fontsize=12, loc='upper right', frameon=True, shadow=True)
plt.grid(visible=True, linestyle='--', alpha=0.6)

# Firma del grafico
plt.annotate('Source: Eurostat', xy=(0.99, 0.01), xycoords='axes fraction', fontsize=10, ha='right', color='gray')

# Mostra il grafico
plt.tight_layout()
plt.show()
