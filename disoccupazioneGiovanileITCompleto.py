import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Usa un tema più esteticamente gradevole
sns.set_theme(style="whitegrid")

# Caricare i dati (modifica i percorsi dei file)
file_path_15_24 = 'C:/Users/laura/Desktop/uni/3Anno/visualizzazione_scientifica/disoccupazione_giovanile_Italia_15-24.csv' # Sostituisci con il percorso del primo file
file_path_18_29 = 'C:/Users/laura/Desktop/uni/3Anno/visualizzazione_scientifica/disoccupazione_giovanile_Italia_18-29.csv'  # Sostituisci con il percorso del secondo file

# Caricare i dati
data_15_24 = pd.read_csv(file_path_15_24)
data_18_29 = pd.read_csv(file_path_18_29)

# Filtrare le colonne rilevanti
data_15_24_filtered = data_15_24[['TIME', 'Sesso', 'Value']].dropna()
data_18_29_filtered = data_18_29[['TIME', 'Sesso', 'Value']].dropna()

# Estrarre l'anno da TIME
data_15_24_filtered['Anno'] = data_15_24_filtered['TIME'].str[:4]
data_18_29_filtered['Anno'] = data_18_29_filtered['TIME'].str[:4]

# Calcolare la media per il gruppo di età 18-24 e per il gruppo 15-29 separatamente
# Per il dataset 15-24 anni, possiamo usare i dati così come sono
# Per il dataset 18-29 anni, calcoliamo la media tra i 18-24 anni (inclusi)

# Gruppo 18-24 anni per dataset 18-29 (media dei dati)
data_18_29_filtered_18_24 = data_18_29_filtered[data_18_29_filtered['Anno'].between('2018', '2024')]

# Unire i dati dei gruppi 15-24 e 18-29
combined_data = pd.concat([data_15_24_filtered, data_18_29_filtered_18_24])

# Calcolare la media per ogni anno, sesso
aggregated_combined_data = combined_data.groupby(['Anno', 'Sesso'], as_index=False)['Value'].mean()

# Pivot per organizzare i dati
pivot_combined_data = aggregated_combined_data.pivot(index='Anno', columns='Sesso', values='Value')

# Calcolare la media tra maschi e femmine per ogni anno
pivot_combined_data['Media'] = pivot_combined_data.mean(axis=1)

# Creare il grafico con miglioramenti estetici
plt.figure(figsize=(14, 7))

# Linea per la media tra maschi e femmine per il periodo 15-29 anni
sns.lineplot(data=pivot_combined_data['Media'], label='Media Maschi e Femmine 15-29', color='#32CD32', linewidth=3)

# Aggiungi una linea orizzontale tratteggiata per evidenziare il picco
picco = pivot_combined_data['Media'].max()  # Identifica il valore massimo come picco
picco_anno = pivot_combined_data['Media'].idxmax()  # Trova l'anno corrispondente al picco

# Aggiungi la linea orizzontale tratteggiata
plt.axhline(y=picco, color='red', linestyle='--', label=f'Picco: {picco:.2f}%')

# Aggiungi un punto sul picco
plt.scatter(picco_anno, picco, color='black', zorder=5, label=f'Punto Picco ({picco_anno}, {picco:.2f}%)')

# Aggiungi titolo e etichette
plt.title('Tendenze Annuali del Tasso di Disoccupazione (15-29 anni) - Media Maschi e Femmine', fontsize=16, fontweight='bold', family='Arial')
plt.xlabel('Anno', fontsize=12, fontweight='bold', family='Arial')
plt.ylabel('Tasso di Disoccupazione (%)', fontsize=12, fontweight='bold', family='Arial')

# Miglioramento della leggibilità con griglie
plt.grid(True, linestyle='dashdot', alpha=0.5)

# Legenda
plt.legend(title='Legenda', loc='upper right', fontsize=12)

# Aggiustamenti per una visualizzazione migliore
plt.tight_layout()

# Mostrare il grafico
plt.show()