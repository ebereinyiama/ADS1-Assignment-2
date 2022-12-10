# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
iport seaborn as sns
import matplotlib.pyplot as plt

### 14 countries of the world were selected and analyzed for 9 different indicators

### Having a look at a sample of the original data set before preprocessing

Access_to_electricity = pd.read_csv("Access to electricity.csv")

print("a sample of original data set from Worldbank: \n", Access_to_electricity)


### Creating function for each of the 9 indicators being investigated. 

### (1) Access to electricity

def electricity(electric):
    """This function returns two dataframes(one with years as columns and one with countries as columns);
    This function also drops some rows and columns of the original dataset and resets index on the
    transposed dataset.
    """
    
    df_1 = pd.read_csv(electric, skiprows=4)
    df_1 = df_1.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)
    df_electricity = df_1
    df_electricity_transpose = pd.DataFrame.transpose(df_1)
    df_electricity_transpose = df_electricity_transpose.rename(columns=df_electricity_transpose.iloc[0])
    df_electricity_transpose = df_electricity_transpose.drop(index=df_electricity_transpose.index[0], axis=0)
    df_electricity_transpose = df_electricity_transpose.reset_index()
    df_electricity_transpose = df_electricity_transpose.rename(columns={"index":"Year"})
    
    return df_electricity, df_electricity_transpose

df_electric, df_electric_t = electricity("Access to electricity.csv")

print()
print("original data is: \n",  df_electric)
print("transposed data is: \n",  df_electric_t)


### Selecting the 14 countries for access to electricity

access_electricity = df_electric_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia']]

### Removing the NaN

access_electricity = access_electricity.dropna()
access_electricity = access_electricity.reset_index()
access_electricity = access_electricity.drop(columns="index")
print("list of countries and access to electricity: \n", access_electricity)

### line plot for access to electricity
access_electricity.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", "k:", 
                                                         "b-", "r-", "k-", "m-", "c-."], title="Access to Electricity", figsize=(10,8))

plt.xticks(rotation=45.0)
plt.show()



### (2) Agricultural land - the second indicator

def agricultural_land(agric):
    """creating a function to return two dataframes for agricultural land"""
    
    df_2 = pd.read_csv(agric, skiprows=4)
    df_2 = df_2.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)
    df_agricultural_land = df_2
    df_agricultural_land_transpose = pd.DataFrame.transpose(df_2)
    df_agricultural_land_transpose = df_agricultural_land_transpose.rename(columns=df_agricultural_land_transpose.iloc[0])
    df_agricultural_land_transpose = df_agricultural_land_transpose.drop(index=df_agricultural_land_transpose.index[0], axis=0)
    df_agricultural_land_transpose = df_agricultural_land_transpose.reset_index()
    df_agricultural_land_transpose = df_agricultural_land_transpose.rename(columns={"index":"Year"})
    
    return df_agricultural_land, df_agricultural_land_transpose

df_agric, df_agric_t = agricultural_land("Agricultural land.csv")


### selecting the 14 countries being analyzed

agric_land = df_agric_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia']]

agric_land = agric_land.dropna()
agric_land = agric_land.reset_index()
agric_land = agric_land.drop(columns="index")
print("list of countries and their agricultural land: \n", agric_land)

### line plot for agricultural land from year 2000

agric_land = agric_land.iloc[39:, :]
agric_land.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", "k:", 
                                                         "b-", "r-", "k-", "m-", "c-."], title="Agricultural land", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.show()



### (3) CO2 Emission; the third indicator

def CO2_emission(CO2):
    """Creating a funtion to return dataframes for CO2 emission"""
    
    df_3 = pd.read_csv(CO2, skiprows=4)
    df_3 = df_3.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)
    df_CO2_emission = df_3
    df_CO2_emission_transpose = pd.DataFrame.transpose(df_3)
    df_CO2_emission_transpose = df_CO2_emission_transpose.rename(columns=df_CO2_emission_transpose.iloc[0])
    df_CO2_emission_transpose = df_CO2_emission_transpose.drop(index=df_CO2_emission_transpose.index[0], axis=0)
    df_CO2_emission_transpose = df_CO2_emission_transpose.reset_index()
    df_CO2_emission_transpose = df_CO2_emission_transpose.rename(columns={"index":"Year"})
    
    return df_CO2_emission, df_CO2_emission_transpose

df_CO2, df_CO2_t = CO2_emission("CO2 emission.csv")

###Selecting the 14 countries for CO2 emission.

CO2Emission = df_CO2_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia']]
CO2Emission = CO2Emission.dropna()
CO2Emission = CO2Emission.reset_index()
CO2Emission = CO2Emission.drop(columns="index")
print("the CO2 emission from the 14 countries are: \n", CO2Emission)

### line plot for CO2 emission from year 2000

CO2Emission = CO2Emission.iloc[10:, :]
CO2Emission.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", "k:", 
                                                         "b-", "r-", "k-", "m-", "c-."], title="CO2 Emission", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.show()



### (4) Forest area; the fourth indicator analyzed

def forest_area(forest):
    """Creating a function to return 2 dataframes for forest area indicator"""
    
    df_4 = pd.read_csv(forest, skiprows=4)
    df_4 = df_4.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)
    df_forest_area = df_4
    df_forest_area_transpose = pd.DataFrame.transpose(df_4)
    df_forest_area_transpose = df_forest_area_transpose.rename(columns=df_forest_area_transpose.iloc[0])
    df_forest_area_transpose = df_forest_area_transpose.drop(index=df_forest_area_transpose.index[0], axis=0)
    df_forest_area_transpose = df_forest_area_transpose.reset_index()
    df_forest_area_transpose = df_forest_area_transpose.rename(columns={"index":"Year"})
    
    return df_forest_area, df_forest_area_transpose

df_forest, df_forest_t = forest_area("Forest area.csv")

### Selecting the 14 countries for Forest area

ForestArea = df_forest_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia']]
ForestArea = ForestArea.dropna()
ForestArea = ForestArea.reset_index()
ForestArea = ForestArea.drop(columns="index")

print("The forest area of the 14 countries: \n", ForestArea)

### line plot for forest area from year 2000

ForestArea = ForestArea.iloc[8:, :]
ForestArea.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", "k:", 
                                                         "b-", "r-", "k-", "m-", "c-."], title="Forest Area", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.show()



### (5) Population growth (annual %); the fifth indicator

def population_growth(population):
    """defining a function to return 2 dataframes for annual % of population growth"""
    
    df_5 = pd.read_csv(population, skiprows=4)
    df_5 = df_5.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)
    df_population_growth = df_5
    df_population_growth_transpose = pd.DataFrame.transpose(df_5)
    df_population_growth_transpose = df_population_growth_transpose.rename(columns=df_population_growth_transpose.iloc[0])
    df_population_growth_transpose = df_population_growth_transpose.drop(index=df_population_growth_transpose.index[0], axis=0)
    df_population_growth_transpose = df_population_growth_transpose.reset_index()
    df_population_growth_transpose = df_population_growth_transpose.rename(columns={"index":"Year"})
    
    return df_population_growth, df_population_growth_transpose

df_population, df_population_t = population_growth("Population growth.csv")

### Selecting the 14 countries for Population growth

annual_population = df_population_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia']]
annual_population = annual_population.dropna()
annual_population = annual_population.reset_index()
annual_population = annual_population.drop(columns="index")
print("the annual percentage of population growth is: \n", annual_population)

### Line plot for annual percentage of population growth from year 2000

annual_population = annual_population.iloc[39:, :]
annual_population.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", "k:", 
                                                         "b-", "r-", "k-", "m-", "c-."], title="Population growth % annual", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.show()



### (6) Renewable energy consumption; the sixth indicator

def renewable_energy(energy):
    """defining a function to return the dataframes for renewable energy"""
    
    df_6 = pd.read_csv(energy, skiprows=4)
    df_6 = df_6.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)
    df_renewable_energy = df_6
    df_renewable_energy_transpose = pd.DataFrame.transpose(df_6)
    df_renewable_energy_transpose = df_renewable_energy_transpose.rename(columns=df_renewable_energy_transpose.iloc[0])
    df_renewable_energy_transpose = df_renewable_energy_transpose.drop(index=df_renewable_energy_transpose.index[0], axis=0)
    df_renewable_energy_transpose = df_renewable_energy_transpose.reset_index()
    df_renewable_energy_transpose = df_renewable_energy_transpose.rename(columns={"index":"Year"})
    
    return df_renewable_energy, df_renewable_energy_transpose

df_energy, df_energy_t = renewable_energy("Renewable energy consumption.csv")

### Selecting the 14 countries for Renewable energy consumption

RenewableEnergy = df_energy_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia']]
RenewableEnergy = RenewableEnergy.dropna()
RenewableEnergy = RenewableEnergy.reset_index()
RenewableEnergy = RenewableEnergy.drop(columns="index")

print("the countries and their renewable energy cosumption are: \n", RenewableEnergy)

### line plot for renewable energy consumption from year 2000

RenewableEnergy = RenewableEnergy.iloc[10:, :]
RenewableEnergy.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", "k:", 
                                                         "b-", "r-", "k-", "m-", "c-."], title="Renewable Energy Consumption", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.show()



### (7) Total greenhouse emission; the seventh indicator investigated

def greenhouse_emission(greenhouse):
    """The function to return two dataframes for Total greenhouse emission"""
    
    df_7 = pd.read_csv(greenhouse, skiprows=4)
    df_7 = df_7.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)
    df_greenhouse_emission = df_7
    df_greenhouse_emission_transpose = pd.DataFrame.transpose(df_7)
    df_greenhouse_emission_transpose = df_greenhouse_emission_transpose.rename(columns=df_greenhouse_emission_transpose.iloc[0])
    df_greenhouse_emission_transpose = df_greenhouse_emission_transpose.drop(index=df_greenhouse_emission_transpose.index[0], axis=0)
    df_greenhouse_emission_transpose = df_greenhouse_emission_transpose.reset_index()
    df_greenhouse_emission_transpose = df_greenhouse_emission_transpose.rename(columns={"index":"Year"})
    
    return df_greenhouse_emission, df_greenhouse_emission_transpose

df_greenhouse, df_greenhouse_t = greenhouse_emission("Total greenhouse emission.csv")

### Selecting the 14 countries for Total greenhouse emission analysis

total_greenhouse = df_greenhouse_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia']]
total_greenhouse = total_greenhouse.dropna()
total_greenhouse = total_greenhouse.reset_index()
total_greenhouse = total_greenhouse.drop(columns="index")

print("The Total Greenhouse Emission from the countries are: \n", total_greenhouse)

### line plot for Total Greenhouse emission from year 2000

total_greenhouse = total_greenhouse.iloc[10:, :]
total_greenhouse.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", "k:", 
                                                         "b-", "r-", "k-", "m-", "c-."], title="Total Greenhouse Emission", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.show()



### (8) Manufacturing, value added (% of GDP); the 8th indicator

def manufacturing_gdp(manufacturing):
    
    """creating a function to return the original dataset and the transposed dataset"""
    
    df_8 = pd.read_csv(manufacturing, skiprows=4)
    df_8 = df_8.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)
    df_manufacturing_gdp = df_8
    df_manufacturing_gdp_transpose = pd.DataFrame.transpose(df_8)
    df_manufacturing_gdp_transpose = df_manufacturing_gdp_transpose.rename(columns=df_manufacturing_gdp_transpose.iloc[0])
    df_manufacturing_gdp_transpose = df_manufacturing_gdp_transpose.drop(index=df_manufacturing_gdp_transpose.index[0], axis=0)
    df_manufacturing_gdp_transpose = df_manufacturing_gdp_transpose.reset_index()
    df_manufacturing_gdp_transpose = df_manufacturing_gdp_transpose.rename(columns={"index":"Year"})
    
    return df_manufacturing_gdp, df_manufacturing_gdp_transpose

df_manufacturing, df_manufacturing_t = manufacturing_gdp("Manufacturing and gdp.csv")

### Selecting the 14 countries for manufacturing

manufacturingGDP = df_manufacturing_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia']]
manufacturingGDP = manufacturingGDP.dropna()
manufacturingGDP = manufacturingGDP.reset_index()
manufacturingGDP = manufacturingGDP.drop(columns="index")

print("The Manufacturing, value added % of GDP of the countries: \n", manufacturingGDP)

### line plot for Manufacturing value added % of GDP

manufacturingGDP.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", "k:", 
                                                         "b-", "r-", "k-", "m-", "c-."], title="Manufacturing value added of % GDP", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.show()



### (9) Arable land; the ninth indicator assessed

def arable_land(arable):
    """Defining a function for Arable land indicator"""
    
    df_9 = pd.read_csv(arable, skiprows=4)
    df_9 = df_9.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)
    df_arable_land = df_9
    df_arable_land_transpose = pd.DataFrame.transpose(df_9)
    df_arable_land_transpose = df_arable_land_transpose.rename(columns=df_arable_land_transpose.iloc[0])
    df_arable_land_transpose = df_arable_land_transpose.drop(index=df_arable_land_transpose.index[0], axis=0)
    df_arable_land_transpose = df_arable_land_transpose.reset_index()
    df_arable_land_transpose = df_arable_land_transpose.rename(columns={"index":"Year"})
    
    return df_arable_land, df_arable_land_transpose

df_arable, df_arable_t = arable_land("Arable land.csv")

### Selecting the 14 countries for Arable land

ArableLand = df_arable_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia']]
ArableLand = ArableLand.dropna()
ArableLand = ArableLand.reset_index()
ArableLand = ArableLand.drop(columns="index")

print("The Arable land of the countries evaluated: \n", ArableLand)

### line plot for Arable land

ArableLand = ArableLand.iloc[8:, :]
ArableLand.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Netherlands', 
                        'Ireland', 'Lithuania', 'Central African Republic', 'Croatia', 'Kenya', 'Chad', 
                        'Morocco', 'Indonesia'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", "k:", 
                                                         "b-", "r-", "k-", "m-", "c-."], title="Arable land", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.show()










