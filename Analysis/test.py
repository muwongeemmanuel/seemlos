import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import numpy as np


# import a csv file by specifying the path ...............................................................#
df = pd.read_csv(r'datasets\encounter.csv', index_col=0, parse_dates=True)   # read the csv file
# put 'r' before the path string to address any special characters in the path, such as '\').
# Don't forget to put the file name at the end of the path + ".csv"
# End of import function .................................................................................#

# print(df)
# df.info()
# df.plot()
# count1 = df["Patient_Gender"].count()
# print(count1)

# date_of_visit = df["Encounter_DateTime"]
# date_of_visit.value_counts()

frequency_of_providers_attendance = df["Provider_ID"].value_counts()
print(frequency_of_providers_attendance)
#frequency_of_providers_attendance.length()
#number_of_providers_attendance.plot()
#df["Gender"].value_counts()
# df["Age"] = 2020 -

frequency_of_members_visit = df["Member_ID"].value_counts()
print(frequency_of_members_visit)

lab_orders_per_member = df[["Member_ID","lab_orders_count"]].describe()
print(lab_orders_per_member)

clinic_types = df.Clinic_Type.unique()
members = df.Member_ID.unique()
specialty = df.Specialty.unique()
providers = df.Provider_ID.unique()
print(members)
print(specialty)

#Convert the Encounter_Datetime field from string to datetime
df["datetime"] = pd.to_datetime(df["Encounter_DateTime"])
print(df["datetime"])

print(df["datetime"].min())
print(df["datetime"].max())

period_of_data_collected = df["datetime"].max() - df["datetime"].min()
print(period_of_data_collected)

# Add a new column of months only
df["month"] = df["datetime"].dt.month
print(df.head())

# What is the average lab order per clinic type per day?
lopcpd = df.groupby([df["datetime"].dt.weekday, "Clinic_Type"])["lab_orders_count"].mean()
print(lopcpd)

# What is the average number of encounter per day per clinic type
frequency_of_encounter = df["Encounter_ID"].value_counts()
# print(frequency_of_encounter)
average_encounter_per_day = df.groupby([df["datetime"].dt.weekday, "Clinic_Type"])["Encounter_ID"].value_counts()
print(average_encounter_per_day)

# Create a plot of average lab order per day
fig, axs = plt.subplots(figsize=(12, 4))
plot_of_avlopd = df.groupby([df["datetime"].dt.weekday])["lab_orders_count"].mean().plot(kind = 'bar', rot = 0,ax = axs)
plt.xlabel("Day of the Week");  # custom x label using matplotlib
plt.ylabel("Lab Orders Count");
plt.show()
print(plot_of_avlopd)

# Create a plot of total lab order per day
fig, axs = plt.subplots(figsize=(12, 4))
plot_of_tlopd = df.groupby([df["datetime"].dt.weekday])["lab_orders_count"].sum().plot(kind = 'bar', rot = 0,ax = axs)
plt.xlabel("Day of the Week");  # custom x label using matplotlib
plt.ylabel("Lab Orders Count");
plt.show()
print(plot_of_tlopd)

# Setting DateTime as the index of the table
no1 = df.set_index(df["datetime"])
print(no1.head())
all_years = no1.index.year
print(all_years)
# Pivot the table by setting an index, columns, and its values
no2 = df.pivot(index = "datetime", columns = "Encounter_ID", values= "lab_orders_count")
print(no2.head)
#no2["2005-05-20":"2010-05-21"].plot();
#plt.show()

# Manipulating textual data
df["Member_Name"] = df["Encounter_Description"].str.split(" ").str.get(0)
print(df.head())
# Create a GUI to Import a CSV File into Python ..........................................................#
# root = tk.Tk()
#
# canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
# canvas1.pack()
#
#
# def getCSV():
#     global df
#
#     import_file_path = filedialog.askopenfilename()
#     df = pd.read_csv(import_file_path)
#     #print(df)
#     df.info()
#
# browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='green', fg='white',
#                              font=('helvetica', 12, 'bold'))
# canvas1.create_window(150, 150, window=browseButton_CSV)
#
# root.mainloop()

# End of button input ....................................................................................#

# block 1 - simple stats .................................................................................#
# mean1 = df['Salary'].mean()
# sum1 = df['Salary'].sum()
# max1 = df['Salary'].max()
# min1 = df['Salary'].min()
# count1 = df['Salary'].count()
# median1 = df['Salary'].median()
# std1 = df['Salary'].std()
# var1 = df['Salary'].var()

# End of block 1 .........................................................................................#

# Select only particular columns from the dataset.........................................................#
#data = pd.DataFrame(df, columns=['Encounter_ID','Member_ID','Provider_ID','Encounter_DateTime','Encounter_Description','CC','Episode_ID','Patient_DOB','Patient_Gender','Speciality','Clinic_Type','lab_orders_count'])
#print(data)

# ------------------------ MATPLOTLIB ----------------------------------------------------------------------#
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
plt.show()