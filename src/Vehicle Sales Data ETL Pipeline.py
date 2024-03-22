#!/usr/bin/env python
# coding: utf-8

# ## Vehicle Sales Data ETL Pipeline
# 
# New notebook

# # **Vehicle Sales Data ETL Pipeline**
# This Python Pandas ETL pipeline uses the [Vehicle Sales and Market Trends Dataset](https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data) by Syed Anwar on Kaggle. The raw data source rovides a comprehensive collection of information pertaining to the sales transactions of various vehicles.
# 
# ## **Initial Columns**
# The following columns are the original columns of the raw data set.
# + **Year** - The manufacturing year of the vehicle.
# + **Make** - The brand or manufacturer of the vehicle.
# + **Model** - The specific model of the vehicle.
# + **Trim** - Additional designation for the vehicle model.
# + **Body** - The body type of the vehicle (e.g., SUV, Sedan).
# + **Transmission** - The type of transmission in the vehicle (e.g., automatic).
# + **VIN** - Vehicle Identification Number, a unique code for each vehicle.
# + **State** - The state where the vehicle is registered.
# + **Condition** - Condition of the vehicle, possibly rated on a scale.
# + **Odometer** - The mileage or distance traveled by the vehicle.
# + **Color** - Exterior color of the vehicle.
# + **Interior** - Interior color of the vehicle.
# + **Seller** - The entity selling the vehicle.
# + **Mmr** - Manheim Market Report, possibly indicating the estimated market value of the vehicle.
# + **Sellingprice** - The price at which the vehicle was sold.
# + **Saledate** - The date and time when the vehicle was sold.

# ## **Step 1: Load raw data**

# In[110]:


import pandas as pd
import random
# Load data into pandas DataFrame from "../data/" + "car_prices.csv"
dfRaw = pd.read_csv("../data/"  + "car_prices.csv")
df = dfRaw.copy()

display(dfRaw[:250])

# Drop rows with any NULL values
df = df.dropna()


# ## **Step 2: Drop unused columns and create grain columns**

# In[111]:


# Apply title case to column names
df.columns = df.columns.str.title()

# Rename columns
df = df.rename(columns={
  "Mmr": "Market Price",
  "Saledate": "Sale Date",
  "Sellingprice": "Selling Price",
  "State": "State Code",
  "Vin": "Vehicle Identification Number",
})

# Get columns
columns = df.columns

# Drop unused columns
if "Condition" in columns:
  del df["Condition"]

# Parse Sale Date column into Datetime object
if not pd.api.types.is_datetime64_any_dtype(df["Sale Date"].dtype):
  df["Sale Date"] = df["Sale Date"].str.split(r"\s+([0-9][0-9]+\:)", expand=True)[0]
  df["Sale Date"] = pd.to_datetime(df["Sale Date"], format="%a %b %d %Y")

# Create grain columns
if "Sale Year" not in columns:
  df["Sale Year"] = df["Sale Date"].dt.year
  df["Sale Month"] = df["Sale Date"].dt.month
  df["Sale Month Name"] = df["Sale Date"].dt.month_name()
  df["Sale Day of Week"] = df["Sale Date"].dt.weekday
  df["Sale Day Name"] = df["Sale Date"].dt.day_name()

display(df[100:200])


# ## **Step 3: Transform the rest of the columns**

# In[112]:


# Transform the State Code column
df["State Code"] = df["State Code"].str.upper()
df["State"] = df["State Code"]

# Create State column from State Code
def state(data):
  match data:
    case "AL":
        return "Alabama"
    case "AK":
        return "Alaska"
    case "AZ":
        return "Arizona"
    case "AR":
        return "Arkansas"
    case "CA":
        return "California"
    case "CO":
        return "Colorado"
    case "CT":
        return "Connecticut"
    case "DE":
        return "Delaware"
    case "FL":
        return "Florida"
    case "GA":
        return "Georgia"
    case "HI":
        return "Hawaii"
    case "ID":
        return "Idaho"
    case "IL":
        return "Illinois"
    case "IN":
        return "Indiana"
    case "IA":
        return "Iowa"
    case "KS":
        return "Kansas"
    case "KY":
        return "Kentucky"
    case "LA":
        return "Louisiana"
    case "ME":
        return "Maine"
    case "MD":
        return "Maryland"
    case "MA":
        return "Massachusetts"
    case "MI":
        return "Michigan"
    case "MN":
        return "Minnesota"
    case "MS":
        return "Mississippi"
    case "MO":
        return "Missouri"
    case "MT":
        return "Montana"
    case "NE":
        return "Nebraska"
    case "NV":
        return "Nevada"
    case "NH":
        return "New Hampshire"
    case "NJ":
        return "New Jersey"
    case "NM":
        return "New Mexico"
    case "NY":
        return "New York"
    case "NC":
        return "North Carolina"
    case "ND":
        return "North Dakota"
    case "OH":
        return "Ohio"
    case "OK":
        return "Oklahoma"
    case "OR":
        return "Oregon"
    case "PA":
        return "Pennsylvania"
    case "RI":
        return "Rhode Island"
    case "SC":
        return "South Carolina"
    case "SD":
        return "South Dakota"
    case "TN":
        return "Tennessee"
    case "TX":
        return "Texas"
    case "UT":
        return "Utah"
    case "VT":
        return "Vermont"
    case "VA":
        return "Virginia"
    case "WA":
        return "Washington"
    case "WV":
        return "West Virginia"
    case "WI":
        return "Wisconsin"
    case "WY":
        return "Wyoming"
    case "DC":
        return "District of Columbia"
    case "PR":
        return "Puerto Rico"
    case "VI":
        return "Virgin Islands"
    case other:
        return "Unknown State"
df["State"] = df["State"].apply(lambda x: state(x))

# Transform Transmission column
df["Transmission"] = df["Transmission"].str.title()

# Transform Color column
df["Color"] = df["Color"].str.title()
colors = df["Color"].unique().tolist()
if "—" in colors: colors.remove("—")
df["Color"] = df["Color"].str.replace("—", random.choice(colors))

# Transform Interior column
df["Interior"] = df["Interior"].str.title()
interiors = df["Interior"].unique().tolist()
if "—" in interiors: interiors.remove("—")
df["Interior"] = df["Interior"].str.replace("—", random.choice(interiors))

# Transform Seller column
df["Seller"] = df["Seller"].str.title()

display(df[100:200])


# ## **Step 4: Write the cleaned and transformed data into CSV file**
# 
# ### **Final Columns**
# The following columns are the final columns comprising the output data set.
# + **Year** - The manufacturing year of the vehicle.
# + **Make** - The brand or manufacturer of the vehicle.
# + **Model** - The specific model of the vehicle.
# + **Trim** - Additional designation for the vehicle model.
# + **Body** - The body type of the vehicle (e.g., SUV, Sedan).
# + **Transmission** - The type of transmission in the vehicle (e.g., automatic).
# + **Vehicle Identification Number** - A unique code designated to each vehicle.
# + **State Code** - The two-letter code of the state where the vehicle is registered.
# + **Odometer** - The mileage or distance traveled by the vehicle.
# + **Color** - Exterior color of the vehicle.
# + **Interior** - Interior color of the vehicle.
# + **Seller** - The entity selling the vehicle.
# + **Market Price** - The estimated market value of the vehicle based on the Manheim Market Report.
# + **Selling Price** - The price at which the vehicle was sold.
# + **Sale Date** - The date and time when the vehicle was sold.
# 
# ### **Grain Columns**
# The following columns are implemented to introduce more granularity into the final data set.
# + **State** - The state where the vehicle is registered.
# + **Sale Year** - Year the vehicle was sold.
# + **Sale Month** - Month number the vehicle was sold.
# + **Sale Month Name** - Name of the month the vehicle was sold.
# + **Sale Day of Week** - Day of week the vehicle was sold.
# + **Sale Day Name** - Name of the day the vehicle was sold.
# + **Sale Month Short Name** - Short name of the month the vehicle was sold.

# In[113]:


# Write to CSV
df.to_csv("../data/" + "Vehicle Sales Data Final.csv", encoding='utf-8', index=False)

# display(df.loc[:100])

