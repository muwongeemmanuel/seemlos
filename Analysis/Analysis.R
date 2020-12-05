#----Import employee dataset from the datasets folder using the readr package and store it as employee---------------------------------#
library(readr)
employee <- read_csv("datasets/employee.csv")
View(employee)

#---Create a bar plot of the age column in the employee dataset------------------------------------------------------------------------#
barplot(employee$Age)

#---View the summary of the employee dataset after storing it as a dataframe------------------------------------------------------------#
employee_summary <- summary.data.frame(employee)
View(employee_summary)
