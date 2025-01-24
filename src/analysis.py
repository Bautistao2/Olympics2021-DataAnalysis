import sqlite3
import pandas as pd
import os

def execute_query(query, db_name='olympics.db'):
    """
    Executes an SQL query and returns the result as a pandas DataFrame.
    """
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def save_to_csv(df, file_name):
    """
    Saves a pandas DataFrame to a CSV file.
    """
    df.to_csv(file_name, index=False)
    print(f"Data saved to {file_name}")

def top_countries_by_medals():
    """
    Retrieves the top 10 countries with the most total medals.
    """
    query = """
    SELECT TeamCountry, Total AS TotalMedals
    FROM Medals
    ORDER BY TotalMedals DESC
    LIMIT 10;
    """
    df = execute_query(query)
    save_to_csv(df, 'output/top_countries_by_medals.csv')

def countries_with_most_sports():
    """
    Retrieves the top 10 countries with the most diversity in sports (distinct disciplines).
    """
    query = """
    SELECT Country, COUNT(DISTINCT Discipline) AS TotalSports
    FROM Athletes
    GROUP BY Country
    ORDER BY TotalSports DESC
    LIMIT 10;
    """
    df = execute_query(query)
    save_to_csv(df, 'output/countries_with_most_sports.csv')

def medal_type_distribution():
    """
    Retrieves the distribution of gold, silver, and bronze medals.
    """
    query = """
    SELECT 
        SUM(Gold) AS TotalGold, 
        SUM(Silver) AS TotalSilver, 
        SUM(Bronze) AS TotalBronze
    FROM Medals;
    """
    df = execute_query(query)
    save_to_csv(df, 'output/medal_type_distribution.csv')

def most_competitive_sports():
    """
    Retrieves the sports with the highest number of athletes.
    """
    query = """
    SELECT Discipline AS Sport, COUNT(*) AS TotalAthletes
    FROM Athletes
    GROUP BY Discipline
    ORDER BY TotalAthletes DESC
    LIMIT 10;
    """
    df = execute_query(query)
    save_to_csv(df, 'output/most_competitive_sports.csv')

def countries_without_medals():
    """
    Retrieves the countries that did not win any medals.
    """
    query = """
    SELECT DISTINCT A.Country
    FROM Athletes A
    LEFT JOIN Medals M ON A.Country = M.TeamCountry
    WHERE M.TeamCountry IS NULL;
    """
    df = execute_query(query)
    save_to_csv(df, 'output/countries_without_medals.csv')

def countries_with_highest_gold_ratio():
    """
    Retrieves the top 10 countries with the highest ratio of gold medals to total medals.
    """
    query = """
    SELECT TeamCountry, Gold, Total, 
           ROUND((Gold * 1.0 / Total) * 100, 2) AS GoldRatio
    FROM Medals
    WHERE Total > 0
    ORDER BY GoldRatio DESC
    LIMIT 10;
    """
    df = execute_query(query)
    save_to_csv(df, 'output/countries_with_highest_gold_ratio.csv')

def total_medals_summary():
    """
    Summarizes the total number of medals awarded across all countries.
    """
    query = """
    SELECT 
        SUM(Gold) AS TotalGold, 
        SUM(Silver) AS TotalSilver, 
        SUM(Bronze) AS TotalBronze, 
        SUM(Total) AS GrandTotal
    FROM Medals;
    """
    df = execute_query(query)
    save_to_csv(df, 'output/total_medals_summary.csv')

if __name__ == '__main__':
    print("Running advanced queries...")
    
    # Create output directory if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')
    
    # Execute analysis functions
    top_countries_by_medals()
    countries_with_most_sports()
    medal_type_distribution()
    most_competitive_sports()
    countries_without_medals()
    countries_with_highest_gold_ratio()
    total_medals_summary()
    
    print("All queries executed and results saved to the 'output' folder.")
