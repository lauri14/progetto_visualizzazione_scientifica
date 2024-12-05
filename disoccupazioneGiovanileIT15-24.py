import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Usa un tema più esteticamente gradevole
sns.set_theme(style="whitegrid")

# Caricare il dataset
file_path = 'C:/Users/laura/Desktop/uni/3Anno/visualizzazione_scientifica/disoccupazione_giovanile_Italia_15-24.csv'  # Cambia con il tuo file
data = pd.read_csv(file_path)

# Filtrare colonne rilevanti
filtered_data = data[['TIME', 'Sesso', 'Value']].dropna()

# Estrarre l'anno da TIME
filtered_data['Anno'] = filtered_data['TIME'].str[:4]  # Primi 4 caratteri per l'anno

# Calcolare la media per ogni anno e sesso
aggregated_data = filtered_data.groupby(['Anno', 'Sesso'], as_index=False)['Value'].mean()

# Pivot per organizzare i dati
pivot_data = aggregated_data.pivot(index='Anno', columns='Sesso', values='Value')

# Creare il grafico con miglioramenti estetici
plt.figure(figsize=(12, 6))

# Linee personalizzate per maschi e femmine
sns.lineplot(data=pivot_data['maschi'], label='Maschi', color='#1f77b4', linewidth=3)
sns.lineplot(data=pivot_data['femmine'], label='Femmine', color='#ff1493', linewidth=3)

# Aggiungi titolo e etichette
plt.title('Tendenze Annuali del Tasso di Disoccupazione (18-29 anni)', fontsize=16, fontweight='bold', family='Arial')
plt.xlabel('Anno', fontsize=12, fontweight='bold', family='Arial')
plt.ylabel('Tasso di Disoccupazione (%)', fontsize=12, fontweight='bold', family='Arial')

# Miglioramento della leggibilità con griglie
plt.grid(True, linestyle='dashdot', alpha=0.5)

# Legenda
plt.legend(title='Sesso', loc='upper right', fontsize=12)

# Aggiungere annotazioni su punti significativi
# Esempio di annotazione:
# plt.annotate('Picco massimo', xy=(2013, 25), xytext=(2014, 27),
#              arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

# Aggiustamenti per una visualizzazione migliore
plt.tight_layout()

# Mostrare il grafico
plt.show()
