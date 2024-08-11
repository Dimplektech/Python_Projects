import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240810.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[gray_squirrel_count,red_squirrel_count,black_squirrel_count]
}

squr_data = pandas.DataFrame(data_dict) # Convert to DataFrame
print(squr_data)
squr_data.to_csv("squirrel_count.csv") # Convert Dataframe to CSV

