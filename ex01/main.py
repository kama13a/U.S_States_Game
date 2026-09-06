# TODO figure out how many gray , red and black squirrels then take this data and create the DataFrame

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260906.csv")


red = data[data["Primary Fur Color"] == "Cinnamon"]
gray = data[data["Primary Fur Color"] == "Gray"]
black = data[data["Primary Fur Color"] == "Black"]


n_gray = len(gray)
n_black = len(black)
n_red = len(red)
dic = {
    "Colors": ["Gray", "Black", "Red"],
    "Counts": [n_gray, n_black, n_red]
}

colors = pandas.DataFrame(dic)
colors.to_csv("squirrel_count.csv")
