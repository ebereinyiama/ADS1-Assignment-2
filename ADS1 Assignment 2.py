# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

### 10 countries of the world were selected and analyzed for 9 different indicators

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


### Selecting the 12 countries analyzed for access to electricity from transposed dataframe

access_electricity = df_electric_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]

### Removing the NaN

access_electricity = access_electricity.dropna()
access_electricity = access_electricity.reset_index()
access_electricity = access_electricity.drop(columns="index")
print("list of countries and their % population access to electricity: \n", access_electricity)

### line plot for access to electricity(% of population)

access_electricity.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", 
                                                          "b-", "r-", "k-", "m-"], title="Access to electricity (% of population)", figsize=(10,8))

plt.xticks(rotation=45.0)
plt.legend(bbox_to_anchor=(1, 1))
plt.xlabel('Year')
plt.ylabel('% of Population')
plt.show()

### (2) Agricultural land - the second indicator analyzed

def agricultural_land(agric):
    """creating a function to return two dataframes for agricultural land; original dataframe and transposed dataframe"""
    
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


### selecting the 12 countries being analyzed

agric_land = df_agric_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]

agric_land = agric_land.dropna()
agric_land = agric_land.reset_index()
agric_land = agric_land.drop(columns="index")
print("list of the 12 countries and their agricultural land area: \n", agric_land)

### line plot for agricultural land from year 2000

agric_land = agric_land.iloc[39:, :]
agric_land.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", 
                                                          "b-", "r-", "k-", "m-"], title="Agricultural land (% of land area)", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.legend(bbox_to_anchor=(1, 1))
plt.xlabel('Year')
plt.ylabel('% of land area')
plt.show()



### (3) CO2 Emission; the third indicator

def CO2_emission(CO2):
    """Creating a funtion to return 2 dataframes for CO2 emission"""
    
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

### Selecting the 12 countries for CO2 emission.

CO2Emission = df_CO2_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]
CO2Emission = CO2Emission.dropna()
CO2Emission = CO2Emission.reset_index()
CO2Emission = CO2Emission.drop(columns="index")
print("the CO2 emission from the 12 countries are: \n", CO2Emission)

### line plot for CO2 emission from year 2000

CO2Emission = CO2Emission.iloc[10:, :]
CO2Emission.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", 
                                                          "b-", "r-", "k-", "m-"], title="CO2 Emission (kt)", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.legend(bbox_to_anchor=(1, 1))
plt.xlabel('Year')
plt.ylabel('CO2 Emission')
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

### Selecting the 12 countries for Forest area

ForestArea = df_forest_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]
ForestArea = ForestArea.dropna()
ForestArea = ForestArea.reset_index()
ForestArea = ForestArea.drop(columns="index")

print("The forest area of the 12 countries: \n", ForestArea)

### line plot for forest area from year 2000

ForestArea = ForestArea.iloc[8:, :]
ForestArea.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", 
                                                          "b-", "r-", "k-", "m-"], title="Forest Area (% of land area)", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.legend(bbox_to_anchor=(1, 1))
plt.xlabel('Year')
plt.ylabel('Forest Area')
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

### Selecting the 12 countries for Population growth

annual_population = df_population_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]
annual_population = annual_population.dropna()
annual_population = annual_population.reset_index()
annual_population = annual_population.drop(columns="index")
print("the annual percentage of population growth is: \n", annual_population)

### Line plot for annual percentage of population growth from year 2000

annual_population = annual_population.iloc[39:, :]
annual_population.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", 
                                                          "b-", "r-", "k-", "m-"], title="Population growth (% annual)", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.legend(bbox_to_anchor=(1, 1))
plt.xlabel('Year')
plt.ylabel('population growth')
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

### Selecting the 12 countries for Renewable energy consumption

RenewableEnergy = df_energy_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]
RenewableEnergy = RenewableEnergy.dropna()
RenewableEnergy = RenewableEnergy.reset_index()
RenewableEnergy = RenewableEnergy.drop(columns="index")

print("the countries and their renewable energy cosumption: \n", RenewableEnergy)

### line plot for renewable energy consumption from year 2000

RenewableEnergy = RenewableEnergy.iloc[10:, :]
RenewableEnergy.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", 
                                                          "b-", "r-", "k-", "m-"], title="Renewable Energy Consumption", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.legend(bbox_to_anchor=(1, 1))
plt.xlabel('Year')
plt.ylabel('% of total energy consumption')
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

### Selecting the 12 countries for Total greenhouse emission analysis

total_greenhouse = df_greenhouse_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]
total_greenhouse = total_greenhouse.dropna()
total_greenhouse = total_greenhouse.reset_index()
total_greenhouse = total_greenhouse.drop(columns="index")

print("The Total Greenhouse Emission from the countries are: \n", total_greenhouse)

### line plot for Total Greenhouse emission from year 2000

total_greenhouse = total_greenhouse.iloc[10:, :]
total_greenhouse.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", 
                                                          "b-", "r-", "k-", "m-"], title="Total Greenhouse Emission", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.legend(bbox_to_anchor=(1, 1))
plt.xlabel('Year')
plt.ylabel('Greenhouse emission')
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

### Selecting the 12 countries for manufacturing

manufacturingGDP = df_manufacturing_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]
manufacturingGDP = manufacturingGDP.dropna()
manufacturingGDP = manufacturingGDP.reset_index()
manufacturingGDP = manufacturingGDP.drop(columns="index")

print("The Manufacturing, value added % of GDP of the countries: \n", manufacturingGDP)

### line plot for Manufacturing value added % of GDP

manufacturingGDP.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", 
                                                          "b-", "r-", "k-", "m-"], title="Manufacturing value added of % GDP", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.legend(bbox_to_anchor=(1, 1))
plt.xlabel('Year')
plt.ylabel('value added % of GDP')
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

### Selecting the 12 countries for Arable land (% of land area)

ArableLand = df_arable_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]
ArableLand = ArableLand.dropna()
ArableLand = ArableLand.reset_index()
ArableLand = ArableLand.drop(columns="index")

print("The Arable land of the countries evaluated: \n", ArableLand)

### line plot for Arable land

ArableLand = ArableLand.iloc[8:, :]
ArableLand.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", 
                                                          "b-", "r-", "k-", "m-"], title="Arable land (% of land area)", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.legend(bbox_to_anchor=(1, 1))
plt.xlabel('Year')
plt.ylabel('Arable land')
plt.show()


### (10) Population total; the tenth indicator

def population_total(population):
    """defining a function to return 2 dataframes for annual % of population growth"""
    
    df_10 = pd.read_csv(population, skiprows=4)
    df_10 = df_10.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)
    df_population_total = df_10
    df_population_total_transpose = pd.DataFrame.transpose(df_10)
    df_population_total_transpose = df_population_total_transpose.rename(columns=df_population_total_transpose.iloc[0])
    df_population_total_transpose = df_population_total_transpose.drop(index=df_population_total_transpose.index[0], axis=0)
    df_population_total_transpose = df_population_total_transpose.reset_index()
    df_population_total_transpose = df_population_total_transpose.rename(columns={"index":"Year"})
    
    return df_population_total, df_population_total_transpose

df_total_population, df_total_population_t = population_total("Population total.csv")

### Selecting the 12 countries for Population total

total_population = df_total_population_t[['Year', 'Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]
total_population = total_population.dropna()
total_population = total_population.reset_index()
total_population = total_population.drop(columns="index")
print("the total population of countries: \n", total_population)

### Line plot for total population from year 2000

total_population = total_population.iloc[40:, :]
total_population.plot("Year", ['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil'], style = ["g-", "r:", "k--", "b-.", "y-", "g-.", "c--", "m:", 
                                                          "b-", "r-", "k-", "m-"], title="Total population", figsize=(10,8))
plt.xticks(rotation=45.0)
plt.legend(bbox_to_anchor=(1, 1))
plt.xlabel('Year')
plt.ylabel('total population')
plt.show()




### Barchart plots for some indicators - interval of 10 years

### 1. Agricultural land

df_agric_bar = df_agric[['Country Name', '1990', '2000', '2010', '2020']]
df_agric_bar = df_agric_bar.set_index('Country Name')
df_agric_bar = df_agric_bar.loc[['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]
print(df_agric_bar)

df_agric_bar.plot(kind ='bar')
plt.title('Agricultural (land % of land area)')
plt.xlabel('Countries')
plt.ylabel('% of land area')
plt.show()


### 2. CO2 Emission

df_CO2_bar = df_CO2[['Country Name', '1990', '2000', '2010', '2020']]
df_CO2_bar = df_CO2_bar.set_index('Country Name')
df_CO2_bar = df_CO2_bar.loc[['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]

df_CO2_bar.plot(kind ='bar')
plt.title('CO2 Emission (kt)')
plt.xlabel('Countries')
plt.ylabel('CO2 Emission')
plt.show()


### 3. Forest Area

df_forest_bar = df_forest[['Country Name', '1990', '2000', '2010', '2020']]
df_forest_bar = df_forest_bar.set_index('Country Name')
df_forest_bar = df_forest_bar.loc[['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]

df_forest_bar.plot(kind ='bar')
plt.title('Forest area (% of land area)')
plt.xlabel('Countries')
plt.ylabel('forest area')
plt.show()


### 4. Renewable Energy

df_energy_bar = df_energy[['Country Name', '1990', '2000', '2010', '2020']]
df_energy_bar = df_energy_bar.set_index('Country Name')
df_energy_bar = df_energy_bar.loc[['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]

df_energy_bar.plot(kind ='bar')
plt.title('Renewable energy consumption')
plt.xlabel('Countries')
plt.ylabel('Renewable energy')
plt.show()


### 5. Total Greenhouse Emission

df_greenhouse_bar = df_greenhouse[['Country Name', '1990', '2000', '2010', '2020']]
df_greenhouse_bar = df_greenhouse_bar.set_index('Country Name')
df_greenhouse_bar = df_greenhouse_bar.loc[['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]

df_greenhouse_bar.plot(kind ='bar')
plt.title('Total greenhouse emission')
plt.xlabel('Countries')
plt.ylabel('greenhouse emission')
plt.show()



### 6. Arable Land

df_arable_bar = df_arable[['Country Name', '1990', '2000', '2010', '2020']]
df_arable_bar = df_arable_bar.set_index('Country Name')
df_arable_bar = df_arable_bar.loc[['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]

df_arable_bar.plot(kind ='bar')
plt.title('Arable land (% of land area)')
plt.xlabel('Countries')
plt.ylabel('arable land')
plt.show()


### 7. Annual population growth

df_population_bar = df_population[['Country Name', '1990', '2000', '2010', '2020']]
df_population_bar = df_population_bar.set_index('Country Name')
df_population_bar = df_population_bar.loc[['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]

df_population_bar.plot(kind ='bar')
plt.title('Annual % population growth')
plt.xlabel('Countries')
plt.ylabel('population growth')
plt.show()


### 8. Total population

df_total_population_bar = df_total_population[['Country Name', '1990', '2000', '2010', '2020']]
df_total_population_bar = df_total_population_bar.set_index('Country Name')
df_total_population_bar = df_total_population_bar.loc[['Nigeria', 'Algeria', 'Australia', 'Denmark', 'Singapore', 'Ireland', 
                                    'Croatia', 'Kenya', 'Chad', 'Morocco', 'Indonesia', 'Brazil']]

df_total_population_bar.plot(kind ='bar')
plt.title('Total Population')
plt.xlabel('Countries')
plt.ylabel('Population')
plt.legend(loc='center')
plt.show()



### Correlation of indicators for different countries
### Kendall correlation was applied because it is robust to outliers

df_agric_corr = df_agric_t.set_index('Year')
df_CO2_corr = df_CO2_t.set_index('Year')
df_energy_corr = df_energy_t.set_index('Year')
df_forest_corr = df_forest_t.set_index('Year')
df_greenhouse_corr = df_greenhouse_t.set_index('Year')
df_arable_corr = df_arable_t.set_index('Year')
df_population_corr = df_population_t.set_index('Year')
df_electric_corr = df_electric_t.set_index('Year')

### Correlation of indicators for Nigeria years 2010 to 2020

nigeria = pd.DataFrame({'Agricultural land':df_agric_corr['Nigeria'],
'CO2 emission':df_CO2_corr['Nigeria'], 'Renewable energy':df_energy_corr['Nigeria'], 'Forest area':df_forest_corr['Nigeria'], 
'Total greenhouse':df_greenhouse_corr['Nigeria'], 'Arable land':df_arable_corr['Nigeria'], 
'Population growth':df_population_corr['Nigeria'], 'Access to electricity':df_electric_corr['Nigeria']},
['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'])

#print(nigeria)

nigeria = nigeria.astype('float64').corr() #converting the dataframe to float type
print('The correlation of indicators for country Nigeria: \n', nigeria)

nigeria = nigeria.astype('float64').corr()
sns.set_palette("bright")
plt.figure(figsize=(8,5))
sns.heatmap(nigeria.corr(method="kendall"), annot = True, cmap = 'YlGn')
plt.title('Indicators correlation for Nigeria')
plt.show()


### Nigeria; years 2000 to 2010
nigeria2 = pd.DataFrame({'Agricultural land':df_agric_corr['Nigeria'],
'CO2 emission':df_CO2_corr['Nigeria'], 'Renewable energy':df_energy_corr['Nigeria'], 'Forest area':df_forest_corr['Nigeria'], 
'Total greenhouse':df_greenhouse_corr['Nigeria'], 'Arable land':df_arable_corr['Nigeria'], 
'Population growth':df_population_corr['Nigeria'], 'Access to electricity':df_electric_corr['Nigeria']},
['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010'])

nigeria2 = nigeria2.astype('float64').corr()
sns.set_palette("bright")
plt.figure(figsize=(8,5))
sns.heatmap(nigeria2.corr(method="kendall"), annot = True, cmap = 'YlGn')
plt.title('Indicators correlation for Nigeria')
plt.show()


### Correlation of indicators for Indonesia, 2010 to 2020

indonesia = pd.DataFrame({'Agricultural land':df_agric_corr['Indonesia'],
'CO2 emission':df_CO2_corr['Indonesia'], 'Renewable energy':df_energy_corr['Indonesia'], 'Forest area':df_forest_corr['Indonesia'], 
'Total greenhouse':df_greenhouse_corr['Indonesia'], 'Arable land':df_arable_corr['Indonesia'], 
'Population growth':df_population_corr['Indonesia'], 'Access to electricity':df_electric_corr['Indonesia']},
['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'])

print(indonesia)

indonesia = indonesia.astype('float64').corr()
sns.set_palette("bright")
plt.figure(figsize=(8,5))
sns.heatmap(indonesia.corr(method="kendall"), annot = True, cmap = 'Set3')
plt.title('Indicators correlation for Indonesia')
plt.show()

### Indonesia 2000 to 2010

indonesia2 = pd.DataFrame({'Agricultural land':df_agric_corr['Indonesia'],
'CO2 emission':df_CO2_corr['Indonesia'], 'Renewable energy':df_energy_corr['Indonesia'], 'Forest area':df_forest_corr['Indonesia'], 
'Total greenhouse':df_greenhouse_corr['Indonesia'], 'Arable land':df_arable_corr['Indonesia'], 
'Population growth':df_population_corr['Indonesia'], 'Access to electricity':df_electric_corr['Indonesia']},
['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010'])

indonesia2 = indonesia2.astype('float64').corr()
sns.set_palette("bright")
plt.figure(figsize=(8,5))
sns.heatmap(indonesia2.corr(method="kendall"), annot = True, cmap = 'Set3')
plt.title('Indicators correlation for Indonesia2')
plt.show()


### Correlation of indicators for Australia 2010 to 2020

australia = pd.DataFrame({'Agricultural land':df_agric_corr['Australia'],
'CO2 emission':df_CO2_corr['Australia'], 'Renewable energy':df_energy_corr['Australia'], 'Forest area':df_forest_corr['Australia'], 
'Total greenhouse':df_greenhouse_corr['Australia'], 'Arable land':df_arable_corr['Australia'], 
'Population growth':df_population_corr['Australia'], 'Access to electricity':df_electric_corr['Australia']},
['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'])

australia = australia.astype('float64').corr()
sns.set_palette("bright")
plt.figure(figsize=(8,5))
sns.heatmap(australia.corr(method="kendall"), annot = True, cmap = 'Pastel2')
plt.title('Indicators correlation for Australia')
plt.show()

### Australia 2000 to 2010

australia2 = pd.DataFrame({'Agricultural land':df_agric_corr['Australia'],
'CO2 emission':df_CO2_corr['Australia'], 'Renewable energy':df_energy_corr['Australia'], 'Forest area':df_forest_corr['Australia'], 
'Total greenhouse':df_greenhouse_corr['Australia'], 'Arable land':df_arable_corr['Australia'], 
'Population growth':df_population_corr['Australia'], 'Access to electricity':df_electric_corr['Australia']},
['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010'])

australia2 = australia2.astype('float64').corr()
sns.set_palette("bright")
plt.figure(figsize=(8,5))
sns.heatmap(australia2.corr(method="kendall"), annot = True, cmap = 'Pastel2')
plt.title('Indicators correlation for Australia')
plt.show()


### Correlation of indicators for Kenya; 2010 to 2020

kenya = pd.DataFrame({'Agricultural land':df_agric_corr['Kenya'],
'CO2 emission':df_CO2_corr['Kenya'], 'Renewable energy':df_energy_corr['Kenya'], 'Forest area':df_forest_corr['Kenya'], 
'Total greenhouse':df_greenhouse_corr['Kenya'], 'Arable land':df_arable_corr['Kenya'], 
'Population growth':df_population_corr['Kenya'], 'Access to electricity':df_electric_corr['Kenya']},
['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'])

kenya = kenya.astype('float64').corr()
sns.set_palette("bright")
plt.figure(figsize=(8,5))
sns.heatmap(kenya.corr(method="kendall"), annot = True, cmap = 'Pastel2')
plt.title('Indicators correlation for Kenya')
plt.show()

### Kenya; 2000 to 2010

kenya2 = pd.DataFrame({'Agricultural land':df_agric_corr['Kenya'],
'CO2 emission':df_CO2_corr['Kenya'], 'Renewable energy':df_energy_corr['Kenya'], 'Forest area':df_forest_corr['Kenya'], 
'Total greenhouse':df_greenhouse_corr['Kenya'], 'Arable land':df_arable_corr['Kenya'], 
'Population growth':df_population_corr['Kenya'], 'Access to electricity':df_electric_corr['Kenya']},
['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010'])

kenya2 = kenya2.astype('float64').corr()
sns.set_palette("bright")
plt.figure(figsize=(8,5))
sns.heatmap(kenya2.corr(method="kendall"), annot = True, cmap = 'Pastel2')
plt.title('Indicators correlation for Kenya')
plt.show()
