import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv').set_index('date')
df.index = pd.to_datetime(df.index)


# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
    ]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20, 5))

    ax.plot(df.index.values,
       df['value'],
       color='red')

    ax.set(xlabel="Date",
       ylabel="Page Views",
       title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.resample('M').mean()
    df_bar['Year'] = pd.to_datetime(df_bar.index.values).year
    df_bar['Month'] = pd.to_datetime(df_bar.index.values).month_name()
    months_in_order = ['January', 'February', 'March', 'April', 'May', 'June',
                        'July', 'August', 'September', 'October', 'November', 'December']
    pivot_df = df_bar.pivot(index='Year', columns='Month', values='value')
    pivot_df = pivot_df[months_in_order]

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(7, 7))
    pivot_df.plot(kind='bar', ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Average Daily Page Views for Each Month Grouped by Year')
    ax.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    sns.boxplot(x='month', y='value', data=df_box, ax=ax[1], order=[
                'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
