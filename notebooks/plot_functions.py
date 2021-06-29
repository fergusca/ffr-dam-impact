#!/usr/bin/env python
# coding: utf-8

# # This .py module contains functions for plotting in the blog notebook and can be used throughout the repository.

# In[1]:


# Import needed for functions to run
import seaborn as sns

# Dam colors to use throughout plotting
dam_color = {'Irrigation': 'black',
             'Hydroelectricity': 'red',
             'Water supply': 'blue',
             'Flood control': 'yellow',
             'Navigation': 'orange',
             'Other expanded': 'magenta'}


# In[2]:


# List functions needed to run code

def dam_type_plot(dam_continent, continent_name, plt_ax, ylim=700, dam_color = dam_color):
    """Take the continent df, continent name, and indicated subplot axis, and create a subplot barplot.

    Parameters
    -----------
    dam_continent : dataFrame
        GRanD dataframe subset by continent.
    continent_name : string
        String of continent name.
    plt_ax : variable
        Variable name indicating which matplotlib axis to plot on.
    ylim : integer
        Integer value for y-axis limit. Default value is 700.
    dam_color : list
        List of colors to use as color labels throughout the plot.

    Returns
    -----------
    plt_ax : matplotlib axis
        Matplotlib axis for plotting on a subplot.
    """

    # Loop through df, grouped by main use and create subplot
    for ctype, dam in dam_continent.groupby("MAIN_RED"):
        color_dam = dam_color[ctype]
        label = ctype
        dam_count = dam.count()
        plt_ax.bar(ctype,
                dam_count["GRAND_ID"],
                color=color_dam,
                label=label)
        plt_ax.set(ylabel="Count")
        plt_ax.set_ylim(0, ylim)
        plt_ax.set_title(continent_name, fontsize=30)
    plt_ax.grid(axis="y")

    return plt_ax

def dam_box_plot(dam_continent, continent_name, plt_ax, yvar, ylab, dam_color = dam_color):
    """Take the continent df, continent name, and indicated subplot axis, and create a subplot boxplot.

    Parameters
    -----------
    dam_continent : dataFrame
        GRanD dataframe subset by continent.
    continent_name : string
        String of continent name.
    plt_ax : variable
        Variable name indicating which matplotlib axis to plot on.
    dam_color : list
        List of colors to use as color labels throughout the plot.

    Returns
    -----------
    plt_ax : matplotlib axis
        Matplotlib axis for plotting on a subplot.
    """

    # Pre process df
    dam_continent = dam_continent.sort_values('MAIN_RED')
    # Loop through df, grouped by main use and create subplot
    sns.boxplot(x="MAIN_RED", y= yvar,
                data=dam_continent, palette=dam_color, ax=plt_ax)
    plt_ax.xaxis.set_tick_params(rotation=45)
    plt_ax.set(xlabel="", ylabel= ylab) #"ln_DIS_AVG_LS", "Average Discharge in liters/sec (ln)"
    plt_ax.set_title(continent_name, fontsize=30)

    return plt_ax

def order_scat_plot(dam_continent, continent_name, plt_ax, ylim = 350, dam_color = dam_color):
    """Take the continent df, continent name, and indicated subplot axis, and 
    create a subplot scatterplot of dam types by river order on x-axis and 
    counts on y-axis.

    Parameters
    -----------
    dam_continent : dataFrame
        GRanD dataframe subset by continent.
    continent_name : string
        String of continent name.
    plt_ax : variable
        Variable name indicating which matplotlib axis to plot on.
    ylim : integer
        Integer value for y-axis limit. Default value is 350.
    dam_color : list
        List of colors to use as color labels throughout the plot.

    Returns
    -----------
    plt_ax : matplotlib axis
        Matplotlib axis for plotting on a subplot.
    """

    # Loop through df, grouped by main use and create subplot
    for ctype, dam in dam_continent.groupby("MAIN_RED"):
        color_dam = dam_color[ctype]
        label = ctype
        order_df = dam.groupby("RIV_ORD").count().reset_index()
        plt_ax.scatter(order_df["RIV_ORD"],
                order_df["MAIN_RED"],
                color=color_dam,
                label=label)
        plt_ax.set(xlabel="River Order")
        plt_ax.set(ylabel="Count")
        plt_ax.set_ylim(0, ylim)
        plt_ax.set_title(continent_name, fontsize=30)
    plt_ax.grid(axis="y")

    return plt_ax

