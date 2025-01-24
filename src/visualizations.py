import pandas as pd
import os
import matplotlib.pyplot as plt

# Crear carpeta para guardar los gráficos
def create_plots_folder():
    if not os.path.exists('plots'):
        os.makedirs('plots')
        print("Plots folder created.")
    else:
        print("Plots folder already exists.")

# Paleta de colores llamativa
COLORS = {
    'bar1': '#FF5733',  # Naranja vibrante
    'bar2': '#33FF57',  # Verde brillante
    'bar3': '#3357FF',  # Azul llamativo
    'pie': ['#FF5733', '#33FF57', '#FFC300'],  # Colores vivos para pastel
}

# 1. Países con mayor proporción de oro
def plot_countries_with_highest_gold_ratio():
    df = pd.read_csv('output/countries_with_highest_gold_ratio.csv')
    plt.figure(figsize=(10, 6))
    plt.barh(df['TeamCountry'], df['GoldRatio'], color=COLORS['bar1'])
    plt.title('Top 5 Countries by Gold Medal Ratio (%)', fontsize=16, fontweight='bold')
    plt.xlabel('Gold Medal Ratio (%)', fontsize=12)
    plt.ylabel('Countries', fontsize=12)
    plt.tight_layout()
    plt.savefig('plots/countries_with_highest_gold_ratio.png')
    print("Saved: plots/countries_with_highest_gold_ratio.png")

# 2. Países con más deportes
def plot_countries_with_most_sports():
    df = pd.read_csv('output/countries_with_most_sports.csv')
    plt.figure(figsize=(10, 6))
    plt.bar(df['Country'], df['TotalSports'], color=COLORS['bar2'])
    plt.title('Top 5 Countries with Most Sports Participation', fontsize=16, fontweight='bold')
    plt.xlabel('Countries', fontsize=12)
    plt.ylabel('Number of Sports', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.tight_layout()
    plt.savefig('plots/countries_with_most_sports.png')
    print("Saved: plots/countries_with_most_sports.png")

# 3. Países sin medallas
def plot_countries_without_medals():
    df = pd.read_csv('output/countries_without_medals.csv')
    plt.figure(figsize=(8, 6))
    plt.bar(df['Country'], [1] * len(df), color=COLORS['bar3'])
    plt.title('Countries Without Medals', fontsize=16, fontweight='bold')
    plt.xlabel('Countries', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks([])
    plt.tight_layout()
    plt.savefig('plots/countries_without_medals.png')
    print("Saved: plots/countries_without_medals.png")

# 4. Distribución de tipos de medallas
def plot_medal_type_distribution():
    df = pd.read_csv('output/medal_type_distribution.csv')
    plt.figure(figsize=(8, 8))
    plt.pie(
        [df['TotalGold'][0], df['TotalSilver'][0], df['TotalBronze'][0]],
        labels=['Gold', 'Silver', 'Bronze'],
        autopct='%1.1f%%',
        colors=COLORS['pie'],
        textprops={'fontsize': 12}
    )
    plt.title('Medal Type Distribution', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('plots/medal_type_distribution.png')
    print("Saved: plots/medal_type_distribution.png")

# 5. Deportes más competitivos
def plot_most_competitive_sports():
    df = pd.read_csv('output/most_competitive_sports.csv')
    plt.figure(figsize=(10, 6))
    plt.bar(df['Sport'], df['TotalAthletes'], color=COLORS['bar1'])
    plt.title('Most Competitive Sports by Athlete Count', fontsize=16, fontweight='bold')
    plt.xlabel('Sports', fontsize=12)
    plt.ylabel('Total Athletes', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.tight_layout()
    plt.savefig('plots/most_competitive_sports.png')
    print("Saved: plots/most_competitive_sports.png")

# 6. Países más exitosos por rango
def plot_most_successful_countries_by_rank():
    df = pd.read_csv('output/most_successful_countries_by_rank.csv')
    plt.figure(figsize=(10, 6))
    plt.barh(df['TeamCountry'], df['Rank'], color=COLORS['bar2'])
    plt.title('Most Successful Countries by Rank', fontsize=16, fontweight='bold')
    plt.xlabel('Rank', fontsize=12)
    plt.ylabel('Countries', fontsize=12)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('plots/most_successful_countries_by_rank.png')
    print("Saved: plots/most_successful_countries_by_rank.png")

# 7. Países con más medallas
def plot_top_countries_by_medals():
    df = pd.read_csv('output/top_countries_by_medals.csv')
    plt.figure(figsize=(10, 6))
    plt.barh(df['TeamCountry'], df['TotalMedals'], color=COLORS['bar3'])
    plt.title('Top 5 Countries by Total Medals', fontsize=16, fontweight='bold')
    plt.xlabel('Total Medals', fontsize=12)
    plt.ylabel('Countries', fontsize=12)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('plots/top_countries_by_medals.png')
    print("Saved: plots/top_countries_by_medals.png")

# 8. Resumen de medallas totales
def plot_total_medals_summary():
    df = pd.read_csv('output/total_medals_summary.csv')
    medal_counts = [df['TotalGold'][0], df['TotalSilver'][0], df['TotalBronze'][0]]
    plt.figure(figsize=(8, 6))
    plt.bar(['Gold', 'Silver', 'Bronze'], medal_counts, color=COLORS['pie'])
    plt.title('Total Medals Summary', fontsize=16, fontweight='bold')
    plt.xlabel('Medal Type', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.tight_layout()
    plt.savefig('plots/total_medals_summary.png')
    print("Saved: plots/total_medals_summary.png")

if __name__ == '__main__':
    print("Generating visualizations...")
    create_plots_folder()

    # Ejecutar funciones para cada gráfico
    plot_countries_with_highest_gold_ratio()
    plot_countries_with_most_sports()
    plot_countries_without_medals()
    plot_medal_type_distribution()
    plot_most_competitive_sports()
    plot_most_successful_countries_by_rank()
    plot_top_countries_by_medals()
    plot_total_medals_summary()
    
    print("All visualizations saved in the 'plots' folder.")
