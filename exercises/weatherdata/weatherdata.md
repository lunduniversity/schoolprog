Use real weather data to calculate how the yearly average temperature has changed over the last 100 years.
==========================================================================================================

We will in this exercise use a computer to analyze large amounts of data.

In fetchdata.py there exists two public functions:
- get\_stations()
    + returns a list that contains all weather stations avaliable that has dayly averages.
- get\_data(station\_id)
    + returns a list with all datapoints on the format ((year, month, day), average\_temperatue)

# TODO
- Export to CSV-file(s)?
- Create a function for reading the csv-file. (or caching)
- Instructions for calculating yearly average (standard deviation) for a station.
- Make some nice plots:
    + Plot all data points for a year for a single station
    + Create a dayly average from multiple stations and plot this average for a year
    + Create an average for each year of a station and plot this.
    + Create an average for each year of multiple stations and plot this.
- Download more data from SMHI by exploring their API
- Download more data from other sources?
