import csv
import statistics

with open("DATA475_lab_rectangles_data.csv", newline='') as f:
    reader = csv.reader(f)
    next(reader)

    #list comprehension
    areas = [float(row[1]) * float(row[2]) for row in reader]

#create a dictionary to store data values

info = {
        "Minimum Area" : min(areas),
        "Maximum Area" : max(areas),
        "Total Count" : len(areas),
        "Total Area" : sum(areas),
        "Average Area" : statistics.mean(areas),
    }

for key, value in info.items():
    print(f"{key} is {value}")


with open("summary_class.csv", mode="w", newline="") as f:
    writer= csv.writer(f)
    writer.writerow(info.keys())
    writer.writerow(info.values())