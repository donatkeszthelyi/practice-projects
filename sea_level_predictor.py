import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.7, color='purple')
    ax.grid(True)

    # Create first line of best fit
    years_extended = pd.array(range(1880, 2051, 1))                       
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line = intercept + slope * years_extended
    plt.plot(years_extended, line, color='green', linewidth=2)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    years_extended2000 = pd.array(range(2000, 2051, 1))                       
    slope2000, intercept2000, r_value2000, p_value2000, std_err2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    line2000 = intercept2000 + slope2000 * years_extended2000
    plt.plot(years_extended2000, line2000, color = 'blue', linewidth=2)

    # Add labels and title
    ax.set(xlabel='Year',
        ylabel='Sea Level (inches)',
        title='Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()