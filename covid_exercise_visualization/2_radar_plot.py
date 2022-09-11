# -*- coding: utf-8 -*-

# Use the pygal radar (see http://www.pygal.org/en/latest/documentation/types/radar.html) to plot:
# the covid cases of "Switzerland", "Italy", "Germany", "Belgium", "Singapore", "France" and "Finland" (or others)
# From April 2020 until December 2020 with a radar plot
#
# Get the data from the delivered csv files und data "/data/04-01-2020.csv" for example
# Use the python "csv" Library
#
# Use and complete (if necessary) the prepared functions and feel free to add more functions yourself
#

import pygal
import csv


# 1 Step - The runner
def run_exercise():
    """
    This is the default runner for this exercise
    """

    countries_list = ["Switzerland", "Italy", "Germany", "France", "Finland"]

    month = '06-01-2020'

    x_labels = ['Confirmed', 'Recovered', 'Active', 'Deaths']
    plot_data_list = get_data_plot_lists(countries_list, month)

    title = "Covid Radar for " + month

    write_plot_to_browser(title, x_labels, plot_data_list)


# 2. Step - Processor
def get_data_plot_lists(countries_list, month_list):
    """
    prepares the data structure containing the data which will be printed

    :param countries_list: the list of countries of interest
    :param month_list: the list of months of interest
    :return: list with all the needed data
    """

    plot_data_list = []

    for country in countries_list:
        print("Processing: " + country)
        plot_data_list.append([country, get_covid_characteristic_country_numbers(country, month_list)])

    return plot_data_list


# 3. Step - Data combining
def get_covid_characteristic_country_numbers(country, month):
    """ returns the data for the radar plot (in this case for the 5 categories) for the given country

    :param country: the country of interest
    :param month: the month of interst
    :return: returns a combined list with the covid cases and all characteristics
    """

    data = []

    data.append(get_covid_cases_by_characteristic(country, month, 'Confirmed'))
    data.append(get_covid_cases_by_characteristic(country, month, 'Recovered'))
    data.append(get_covid_cases_by_characteristic(country, month, 'Active'))
    data.append(get_covid_cases_by_characteristic(country, month, 'Deaths'))

    return data


# 4. Step - Detail Function
def get_covid_cases_by_characteristic(country, month, characteristic):
    """
    Returns the Covid Cases for the given country & month.

    :param country: the country of interest
    :param month: the month of interest
    :param characteristic: the characteristic of interest
    :return: single number of a covid characteristic by country and month
    """

    data_source = 'data/' + month + '.csv'
    with open(data_source, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Country_Region'] == country:
                return int(row[characteristic])
        return 'None'


# 5. Step - Browser plotting
def write_plot_to_browser(plot_title, x_labels_map, list_plot_data):
    """
    :param plot_title: Title of the chart. For example "Browser usage evolution (in %)"
    :param x_labels_map: For example map(str, range(2002, 2013))
    :param list_plot_data:
    list_plot_data = ['Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1],
                     ['Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3],
                     ... ]
    :return: picture in default web browser
    """

    radar_chart = pygal.Radar()
    radar_chart.title = plot_title
    radar_chart.x_labels = x_labels_map

    for plot_data in list_plot_data:
        values = plot_data[1]
        radar_chart.add(plot_data[0], values)

    radar_chart.render_in_browser()


if __name__ == '__main__':
    run_exercise()