# with open("weather_data.csv","r") as data_file:
#     data = data_file.readlines()
# print(data)    
# 

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# Convert dataframe to dictionary
data_dict = data.to_dict()
print(data_dict)

# Series to column
temp_list = data["temp"].to_list()
print(temp_list)

# Average Temp
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)

# Using series method of panda
avg_temp = data["temp"].mean()
print(avg_temp)

# Max_temp
max_temp = data["temp"].max()
print(max_temp)

# another way to work with column
print(data.condition)
print(data.temp)

# to get data of particular row
print(data[data.day == "Monday"])

#  pull out data  of row where temp is max
print(data[data.temp == data.temp.max()])

# If we need to one value from particular row
monday = data[data.day == "Monday"]
print(monday.temp)
temp_far = (monday.temp * (9 / 5) ) + 32
print(temp_far, "F")

## How to create dataframe from scratch
data_dict_student = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 89, 92]
}

student_data = pandas.DataFrame(data_dict_student)
print(student_data)
student_data.to_csv("student_data")





