import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

csv_url = 'epa-sea-level.csv'

def draw_plot():
    plt.figure(figsize=(10, 6))
    plt.style.use('ggplot')

    # Read data from file
    df = pd.read_csv(csv_url)

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'],s=8, c="darkblue")

    # Create first line of best fit
    years_extended = list(range(1880,2050 + 1))
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(
        years_extended, 
        [year * res.slope + res.intercept for year in years_extended], 
        'r', 
        label='fitted line from the data of 1880 - 2013'
    )

    # Create second line of best fit
    years_extended = list(range(2000,2050 + 1))
    res = linregress(
        df.loc[df['Year'] >= 2000]['Year'],
        df.loc[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    )
    plt.plot(
        years_extended, 
        [year * res.slope + res.intercept for year in years_extended],
        'purple',
        label='fitted line from the data of 2000 - 2013'
    )

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel("Year")
    plt.xticks(list(range(1850,2076,25)))
    plt.xlim([1850, 2080])
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    plt.grid(True, ls='--',c='gray')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()