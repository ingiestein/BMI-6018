# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 09:47:55 2021

@author: u6026797
"""
#%% libraries
import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib import colormaps
import seaborn as sns

#%% data

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
file_path = "time_series_covid19_confirmed_US.csv"

# Rather than download the data with each run, I downloaded it locally. try for the local path, else download it.
data_path = os.path.join(os.getcwd(),file_path) if os.path.isfile(file_path) else url
covid_df = pd.read_csv(url, index_col=0)

#%% Instructions
'''
Overall instructions:
As described in the homework description, each graphic you make must:
   1. Have a thoughtful title
   2. Have clearly labelled axes 
   3. Be legible
   4. Not be a pie chart
I should be able to run your .py file and recreate the graphics without error.
As per usual, any helper variables or columns you create should be thoughtfully
named.
'''
#Helper function for sorting the date by State.
def state_sort(state):
    state_df = covid_df[covid_df['Province_State'].str.contains(rf'{state}', na=False)]


    state_ts = state_df.melt(
        id_vars=['Admin2'],  # Admin2 = county name
        value_vars=[col for col in state_df.columns if '/' in col],  # all date columns
        var_name='Date',
        value_name='Cases'  # or 'Deaths' if you're plotting deaths
    )

    # Step 2: Convert the date column from string like '1/22/20' → real datetime
    state_ts['Date'] = pd.to_datetime(state_ts['Date'], format='%m/%d/%y')

    # Step 3: Clean county name (Admin2 is usually the county)
    state_ts['County'] = state_ts['Admin2'].fillna('Unknown')

    # Step 4: Sort by date
    state_ts = state_ts.sort_values(['County', 'Date'])
    return state_ts

def get_top_county(state_ts):
    latest_loc = state_ts.loc[state_ts["Date"]==state_ts["Date"].max()]
    top_county=latest_loc.loc[latest_loc["Cases"].idxmax(),'County']
    return top_county

def viz_1():
    # %% viz 1
    '''
    Create a visualization that shows all of the counties in Utah as a time series,
    similar to the one shown in slide 22 during the lecture. The graphic should
    -Show cases over time
    -Have all counties plotted in a background color (something like grey)
    -Have a single county plotted in a contrasting color (something not grey)
    -Have well formatted dates as the X axis
    '''

    utah_ts = state_sort("Utah")

    vis_1_fig, vis_1_ax = plt.subplots(figsize=(14, 8))


    top_county = get_top_county(utah_ts)

    top_county_ts = utah_ts.loc[utah_ts["County"]==top_county]
    top_county_ts.pivot(index="Date",columns="County",values="Cases").plot(linewidth=2.5,
                                                                      color="red",
                                                                      ax=vis_1_ax,
                                                                      legend=f'{top_county}')

    utah_ts = utah_ts[utah_ts["County"]!=top_county]
    utah_ts.pivot(index="Date", columns="County",values="Cases").plot(linewidth=2.5,
                                                                      color="lightgray",
                                                                      ax=vis_1_ax,
                                                                      legend=False)

    plt.title('COVID-19 Cases by County in Utah')
    plt.ylabel('Cases')
    plt.xlabel('Date')
    vis_1_ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))


    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # moves legend outside
    plt.tight_layout()
    plt.show()




#%% viz 2
'''
Create a visualization that shows the contrast between the county in Utah with
the most cases to date to a county in Florida with the most cases to date.
The graphic should:
-Have only two counties plotted
-Highlight the difference between the two comparison counties
You may use any style of graphic you like as long as it is effective (dense)
and readable
'''

def vis_2():
    vis_2_fig, vis_2_ax = plt.subplots(figsize=(14, 8))

    florida_ts = state_sort("Florida")
    utah_ts = state_sort("Utah")

    utah_top_county = get_top_county(utah_ts)
    florida_top_county = get_top_county(florida_ts)

    utah_top_county_ts = utah_ts.loc[utah_ts["County"]==utah_top_county]
    utah_top_county_ts.pivot(index="Date",columns="County",values="Cases").plot(linewidth=2.5,
                                                                      color="red",
                                                                      ax=vis_2_ax,
                                                                      legend=f'{utah_top_county}, UTAH')

    florida_top_county_ts = florida_ts.loc[florida_ts["County"]==florida_top_county]
    florida_top_county_ts.pivot(index="Date",columns="County",values="Cases").plot(linewidth=2.5,
                                                                      color="blue",
                                                                      ax=vis_2_ax,
                                                                      legend=f'{florida_top_county}, FLORIDA')

    plt.title(f'Top Country COVID-19 Cases:{utah_top_county}, UT vs {florida_top_county}, FL')
    plt.ylabel('Cases')
    plt.xlabel('Date')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # moves legend outside
    vis_2_ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))
    plt.tight_layout()
    plt.show()


#%% viz 3
'''
Create a visualization that shows BOTH the running total of cases for a single
county AND the daily new cases. The graphic should:
-Use two y-axes (https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)
-Use color to contrast the two series being plotted
-Have well formatted dates as the X axis
'''
def vis_3():
    utah_ts = state_sort("Utah")
    top_county = get_top_county(utah_ts)

    top_df = utah_ts[utah_ts["County"] == top_county].copy()
    top_df = top_df.sort_values("Date")
    top_df["New_Cases"] = top_df["Cases"].diff().fillna(top_df["Cases"])  # ← correct first day

    fig, ax1 = plt.subplots(figsize=(14, 8))


    color_cumulative = "#1f77b4"
    ax1.plot(top_df["Date"], top_df["Cases"],
             color=color_cumulative, linewidth=3.5, label="Cumulative Cases")
    ax1.set_xlabel("Date", fontsize=12)
    ax1.set_ylabel("Cumulative Cases", color=color_cumulative, fontsize=14)
    ax1.tick_params(axis="y", labelcolor=color_cumulative)
    ax1.grid(True, alpha=0.3)

    # === Right axis: Daily new cases (bars) ===
    ax2 = ax1.twinx()
    color_new = "#d62728"  # strong red
    ax2.bar(top_df["Date"], top_df["New_Cases"],
            color=color_new, alpha=0.5, width=1.0, label="Daily New Cases")
    ax2.set_ylabel("Daily New Cases", color=color_new, fontsize=14)
    ax2.tick_params(axis="y", labelcolor=color_new)
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))


    # === Title and combined legend ===
    fig.suptitle(f"{top_county} County, Utah — COVID-19 Cases Over Time",
                 fontsize=16, fontweight="bold")

    # Combine legends from both axes
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2,
               loc="upper left", frameon=True, fancybox=True)

    # Final layout
    plt.tight_layout()
    plt.show()

#%% viz 4
'''
Create a visualization that shows a stacked bar chart of county contributions
to a given state's total cases. You may choose any state (or states).
(https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py)
The graphic should:
-Have a single column delineate a state
-Have each 'slice' or column compontent represent a county
'''

def viz_4():
    utah_ts = state_sort("Utah")
    utah_ts["Date"] = pd.to_datetime(utah_ts["Date"], format="%m/%d/%y")
    utah_daily = utah_ts.sort_values(['County', 'Date'])

    utah_pivot = utah_daily.pivot(index='Date', columns='County', values='Cases')

    cmap = colormaps['nipy_spectral']
    colors = [cmap(1. * i / len(utah_pivot.columns)) for i in range(len(utah_pivot.columns))]

    fig, ax = plt.subplots(figsize=(16, 9))

    utah_pivot.plot.bar(stacked=True, ax=ax, width=0.8, color=colors)

    ax.set_title('Utah COVID-19 Cumulative Cases By County Contribution')
    ax.set_ylabel('Cases',fontsize=10)
    ax.set_xlabel('Date',fontsize=10)

    handles, labels = ax.get_legend_handles_labels()

    ax.legend(handles, labels,
              title='County (Total Cases)',
              bbox_to_anchor=(1.02, 1), loc='upper left',
              frameon=False)

    monthly_ticks = utah_pivot.index.to_series().resample('MS').first()

    tick_positions = [utah_pivot.index.get_loc(date) for date in monthly_ticks]
    ax.set_xticks(tick_positions)
    ax.set_xticklabels([
        date.strftime('%b %Y') if date.month in [1,5,9] else ''
        for date in monthly_ticks
    ], rotation=45, ha='right', fontsize=10)

    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

    plt.tight_layout()
    plt.show()
#%% extra credit (5 points)
'''
Use Seaborn to create a grouped box plot of all reported states. Each boxplot
should be a distinct state. Have the states ordered from most cases (FL) to fewest 
cases. (https://seaborn.pydata.org/examples/grouped_boxplot.html)
'''
def viz_5():

    state_ts = covid_df.melt(
        id_vars=['Province_State',"Admin2"],  # Admin2 = county name
        value_vars=[col for col in covid_df.columns if '/' in col],  # all date columns
        var_name='Date',
        value_name='Cases'  # or 'Deaths' if you're plotting deaths
    )

    state_ts["Date"] = pd.to_datetime(state_ts["Date"],format="%m/%d/%y")
    latest_by_county = state_ts.sort_values('Date').groupby(["Province_State","Admin2"]).last()["Cases"].reset_index().rename(columns={"Cases":"Total_Cases"})
    print(latest_by_county)

    state_totals = latest_by_county.groupby("Province_State")["Total_Cases"].sum().reset_index().rename(columns={"Total_Cases":"State_Total_Cases"}).sort_values("State_Total_Cases", ascending=False)
    print(state_totals)

    # THE FIXED, BEAUTIFUL VERSION
    fig, ax = plt.subplots(figsize=(14, 8))

    sns.boxplot(x="Province_State", y="State_Total_Cases", hue="State_Total_Cases", ax=ax, data=state_totals)
    plt.title("COVID-19 Cases By State")
    plt.xticks(rotation=90)
    ax.set_ylabel('Total Cases',fontsize=10)
    ax.set_xlabel('State',fontsize=10)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # viz_1()
    # vis_2()
    # vis_3()
    # viz_4()
    viz_5()