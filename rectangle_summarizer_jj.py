import csv
import math
import statistics

#open a csv file with csv.reader that contains id, width and length

with open("DATA475_lab_rectangles_data.csv", newline='') as f:
    reader = csv.reader(f)
    next(reader)

# reader it the iterator
# calculate areas

    areas = []
    # areas = {}
    for row in reader:

        ## convert string in csv file to float to allow for math

        width = float(row[1])
        length = float(row[2])

        ## calculation of area
        area = width * length
        ##append all area values in a list

        areas.append(area)
        #area[row[0]] = area


    print(f"min area is {min(areas)}")
    print(f"max area is {max(areas)}")
    print(f"mean area is {statistics.mean(areas)}")
    print(f"total area is {math.fsum(areas)}")

# counting the rows in the csv file
with open("DATA475_lab_rectangles_data.csv", newline='') as f:
    count = sum(1 for line in f)
    print(f"total count is {count-1}")
    

# open a (new) file to write
import csv
file_to_output = open('summary_rectangles.csv','w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(["Total Count", "Total Area", "Average Area", "Maximum Area", "Minimum Area"])
csv_writer.writerow([count-1,math.fsum(areas),statistics.mean(areas),max(areas),min(areas)],)




