# Population Analysis

This repository contains a Python script for analyzing world population data from 1960 to 2017. The script reads data from a CSV file and provides functionalities to check population data for specific countries and years, calculate population changes, and determine the country with the highest population change over a specified period.

Important note: packages such as pandas and numpy were not used out of pre-choice to complete the task without them.

## Files

- `population_analysis.py`: The main Python script for population analysis.
- `world_population.csv`: The CSV file containing world population data.

## Functions

1. `check_year(year)`: Checks if a given year is within the range of 1960 to 2017.
2. `check_years(year1, year2)`: Checks if two given years are within the range of 1960 to 2017 and that year2 is greater than or equal to year1.
3. `break_world_pop_line(line)`: Prints the data of a specific line from the world population CSV file.
4. `check_country(world_pop_file, country)`: Checks if a given country is valid and exists in the world population CSV file.
5. `country_pop(world_pop_file, country, year)`: Returns the population of a given country in a specified year.
6. `pop_change(world_pop_file, country, year1, year2)`: Calculates the population change of a given country between two specified years.
7. `max_pop_change(world_pop_file, year1, year2)`: Determines the country with the highest population change between two specified years.

## Usage

Run the script and enter the country and years when prompted:

```sh
Enter country, year1, year2:
