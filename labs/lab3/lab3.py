num_roads = eval(input("How many roads were surveyed? "))
total_num_cars = 0
for i in range(1, num_roads + 1):
    print("How many days was road", i, "surveyed? ", end="")
    days_surveyed = eval(input())
    num_cars_on_day = 0
    for j in range(1, days_surveyed + 1):
        print("\tHow many cars traveled on day", str(j) + "? ", end="")
        val_on_day = eval(input())
        num_cars_on_day += val_on_day
        total_num_cars += val_on_day
    print("Road", i, "average vehicles per day:", num_cars_on_day / days_surveyed)
print("Total number of vehicles traveled on all roads:", total_num_cars)
avg_cars_per_road = round(total_num_cars / num_roads, 2)
print("Average number of vehicles per road:", avg_cars_per_road)
