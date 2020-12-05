# ------- In this exercise, we’ll visualize the encounter dataset: ---------#
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
#%matplotlib inline
#import plotly.plotly as py
import chart_studio.plotly as py
#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
import plotly.graph_objs as go
pyo.offline.init_notebook_mode()

df = pd.read_csv('datasets/encounter.csv')

# ----- DATA CLEANING ------------------------------------------------------------------------------------------#
#Convert the Encounter_Datetime field from string to datetime
df['datetime'] = pd.to_datetime(df['Encounter_DateTime']).dt.date.astype('datetime64[ns]')

# -----Another way is to convert types of columns while reading the data.
# To do this, pass a list of columns’ names which should be treated as date columns to `parse_dates` parameter of `read_csv` method. This way they will be formatted in a readable way:
#df = pd.read_csv('datasets/encounter.csv', parse_dates=['Encounter_DateTime'])

# --- Another new feature may be ‘WeekDay’ — a weekday of an appointment. With this feature, we can analyze in relation to weekdays.---------#
df['WeekDay'] = df['datetime'].apply(lambda x: x.weekday())
replace_map = {'WeekDay': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday'}}
df.replace(replace_map, inplace=True)

# -- Similarly, add ‘Month’, ‘Hour’ features: -------------------------------------------------------------#
df['Month'] = df['datetime'].dt.month_name()
df['Hour'] = df['datetime'].dt.hour

# Add a new field for member name
df["Member_Name"] = df["Encounter_Description"].str.split(" ").str.get(0)

# --- Dealing with missing values
# Let’s check whether there are null values in each column in this elegant way: -------------------------------------------------------------------------#
#print(df.isnull().sum())

#--- Still, what are the strategies to address missing values?
#Analyzing existing techniques and approaches, I’ve come to the conclusion that the most popular strategies for dealing with missing data are:
#Leaving them as they are.
#Removing them with dropna().
#Filling NA/NaN values with fillna().
#Replacing missing values with expected values (mean) or zeros.
#Dropping a column in case the number of its missing values exceeds a certain threshold (e.g., > 50% of values).

# ----- Let’s remove some columns that we will not need so as to make data processing faster: In this case i'm dropping all fields with NA------#
df.drop(['Provider_Org','CC', 'Facility_Name', 'Specialty', 'SOAP_Note', 'consult_ordered'], axis=1, inplace=True)

# Let’s check again whether there are null values in each column in this elegant way: -------------------------------------------------------------------------#
#print(df.isnull().sum())

# Now we have no fields with NA

# --- Exploring the dataset -------------------------------------------------------------------------------------------------#


# --- Check unique values in some of  the columns --------------------------------------------------------------------------------#
print("Unique Values in 'Encounter_ID '", list(df.Encounter_ID .unique()))
print("Unique Values in 'Member_ID'", list(df.Member_ID.unique()))
print("Unique Values in 'Provider_ID '", list(df.Provider_ID .unique()))
print("Unique Values in 'Provider_NPI'", list(df.Provider_NPI.unique()))
print("Unique Values in 'Clinic_ID '", list(df.Clinic_ID .unique()))
print("Unique Values in 'Patient_Gender '", list(df.Patient_Gender .unique()))
print("Unique Values in 'Provider_Name'", list(df.Provider_Name.unique()))
print("Unique Values in 'Clinic_Type'", list(df.Clinic_Type.unique()))
print("Unique Values in 'lab_orders_count'", list(df.lab_orders_count.unique()))
print("Unique Values in 'lab_results_count'", list(df.lab_results_count.unique()))
print("Unique Values in 'medication_orders_count'", list(df.medication_orders_count.unique()))
print("Unique Values in 'medication_fulfillment_count'", list(df.medication_fulfillment_count.unique()))
print("Unique Values in 'vital_sign_count'", list(df.vital_sign_count.unique()))
print("Unique Values in 'therapy_orders_count'", list(df.therapy_orders_count.unique()))
print("Unique Values in 'therapy_actions_count'", list(df.therapy_actions_count.unique()))
print("Unique Values in 'immunization_count'", list(df.immunization_count.unique()))
print("Unique Values in 'Has_Appt'", list(df.Has_Appt.unique()))
print("Unique Values in 'Disposition'", list(df.Disposition.unique()))
print("Unique Values in 'Member_Name'", list(df.Member_Name.unique()))

# ----- Drop more unnecessary columns ------#
df.drop(['Provider_NPI', 'Clinic_ID'], axis=1, inplace=True)

# --- Take a look at basic statistics of the numerical features: -----------------------------------------------------------#
df.describe()

#--------- Plotting data ---------------------------------------------------------------------------------------------------#
#-----------Check patients distribution by gender.
labels = df['Patient_Gender'].value_counts().index
values = df['Patient_Gender'].value_counts().values

colors = ['#eba796', '#96ebda']

fig = {'data' : [{'type' : 'pie',
                  'name' : "Patients by Gender: Pie chart",
                 'labels' : df['Patient_Gender'].value_counts().index,
                 'values' : df['Patient_Gender'].value_counts().values,
                 'direction' : 'clockwise',
                 'marker' : {'colors' : ['#9cc359', '#e96b5c']}}], 'layout' : {'title' : 'Patients by Gender'}}

pyo.iplot(fig)

# --------------End of plot --------------------------------------------------------------------------------------------------#

#-----------Check encounter distribution based on clinc Type visited.
labels = df['Clinic_Type'].value_counts().index
values = df['Clinic_Type'].value_counts().values

colors = ['#eba796', '#96ebda']

fig = {'data' : [{'type' : 'pie',
                  'name' : "Patients by Clinic Type: Pie chart",
                 'labels' : df['Clinic_Type'].value_counts().index,
                 'values' : df['Clinic_Type'].value_counts().values,
                 'direction' : 'clockwise',
                 'marker' : {'colors' : ['#9cc359', '#e96b5c']}}], 'layout' : {'title' : 'Patients Distribution By Clinic Type'}}

pyo.iplot(fig)

# --------------End of plot --------------------------------------------------------------------------------------------------#

#-----------Check encounter distribution based on disposition.
labels = df['Disposition'].value_counts().index
values = df['Disposition'].value_counts().values

colors = ['#eba796', '#96ebda']

fig = {'data' : [{'type' : 'pie',
                  'name' : "Patients by Disposition: Pie chart",
                 'labels' : df['Disposition'].value_counts().index,
                 'values' : df['Disposition'].value_counts().values,
                 'direction' : 'clockwise',
                 'marker' : {'colors' : ['#9cc359', '#e96b5c']}}], 'layout' : {'title' : 'Patient Encounter Distribution by Disposition '}}

pyo.iplot(fig)

# --------------End of plot --------------------------------------------------------------------------------------------------#