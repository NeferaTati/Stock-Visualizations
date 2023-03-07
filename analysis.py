import csv
import statistics as stats
import matplotlib.pyplot as plt


AAPL_data = []
with open("AAPL.csv", "r") as infile:
    reader = csv.DictReader(infile)
   
    for row in reader:
        AAPL_data.append(row)
i = 0
AAPL_stdev = []
while i < len(AAPL_data):
    if i + 1 >= len(AAPL_data) or i + 2 >= len(AAPL_data) or i + 3 >= len(AAPL_data) or i + 4 >= len(AAPL_data):
        break
    day1 = float(AAPL_data[i]['price'])
    day2 = float(AAPL_data[i + 1]['price'])
    day3 = float(AAPL_data[i + 2]['price'])
    day4 = float(AAPL_data[i + 3]['price'])
    day5 = float(AAPL_data[i + 4]['price'])
    print(AAPL_data[i])
    
    fivedays = stats.pstdev([day1,day2,day3,day4,day5])

    AAPL_stdev.append(fivedays)
    i += 5



#print(AAPL_stdev)

fig, ax = plt.subplots()   
plt.plot(AAPL_stdev, linestyle = 'dashed')  
plt.savefig("apple_stdev.png")


COUR_data = []
with open("COUR.csv", "r") as infile:
    reader = csv.DictReader(infile)
   
    for row in reader:
        COUR_data.append(row)
i = 0
COUR_stdev = []
while i < len(COUR_data):
    if i + 1 >= len(COUR_data) or i + 2 >= len(COUR_data) or i + 3 >= len(COUR_data) or i + 4 >= len(COUR_data):
        break
    day1 = float(COUR_data[i]['price'])
    day2 = float(COUR_data[i + 1]['price'])
    day3 = float(COUR_data[i + 2]['price'])
    day4 = float(COUR_data[i + 3]['price'])
    day5 = float(COUR_data[i + 4]['price'])
    print(COUR_data[i])
    
    fivedays2 = stats.pstdev([day1,day2,day3,day4,day5])

    COUR_stdev.append(fivedays2)
    i += 5



print(COUR_stdev)

fig, ax = plt.subplots()
plt.plot(COUR_stdev, linestyle = 'dashed')  
plt.savefig("COUR_stdev.png")


AMZN_data = []
with open("AMZN.csv", "r") as infile:
    reader = csv.DictReader(infile)
   
    for row in reader:
        AMZN_data.append(row)
i = 0
AMZN_stdev = []
while i < len(AMZN_data):
    if i + 1 >= len(AMZN_data) or i + 2 >= len(AMZN_data) or i + 3 >= len(AMZN_data) or i + 4 >= len(AMZN_data):
        break
    day1 = float(AMZN_data[i]['price'])
    day2 = float(AMZN_data[i + 1]['price'])
    day3 = float(AMZN_data[i + 2]['price'])
    day4 = float(AMZN_data[i + 3]['price'])
    day5 = float(AMZN_data[i + 4]['price'])
    print(AMZN_data[i])
    
    fivedayz = stats.pstdev([day1,day2,day3,day4,day5])

    AMZN_stdev.append(fivedayz)
    i += 5



print(AMZN_stdev)

fig, ax = plt.subplots()   
plt.plot(AMZN_stdev, linestyle = 'dashed')  
plt.savefig("AMZN_stdev.png")

GOOG_data = []
with open("GOOG.csv", "r") as infile:
    reader = csv.DictReader(infile)
   
    for row in reader:
        GOOG_data.append(row)
i = 0
GOOG_stdev = []
while i < len(GOOG_data):
    if i + 1 >= len(GOOG_data) or i + 2 >= len(GOOG_data) or i + 3 >= len(GOOG_data) or i + 4 >= len(GOOG_data):
        break
    day1 = float(GOOG_data[i]['price'])
    day2 = float(GOOG_data[i + 1]['price'])
    day3 = float(GOOG_data[i + 2]['price'])
    day4 = float(GOOG_data[i + 3]['price'])
    day5 = float(GOOG_data[i + 4]['price'])
    print(GOOG_data[i])
    
    fivedayz2 = stats.pstdev([day1,day2,day3,day4,day5])

    GOOG_stdev.append(fivedayz2)
    i += 5



print(GOOG_stdev)

fig, ax = plt.subplots() 
plt.plot(GOOG_stdev, linestyle = 'dashed')  
plt.savefig("GOOG_stdev.png")


NFLX_data = []
with open("NFLX.csv", "r") as infile:
    reader = csv.DictReader(infile)
   
    for row in reader:
        NFLX_data.append(row)
i = 0
NFLX_stdev = []
while i < len(NFLX_data):
    if i + 1 >= len(NFLX_data) or i + 2 >= len(NFLX_data) or i + 3 >= len(NFLX_data) or i + 4 >= len(NFLX_data):
        break
    day1 = float(NFLX_data[i]['price'])
    day2 = float(NFLX_data[i + 1]['price'])
    day3 = float(NFLX_data[i + 2]['price'])
    day4 = float(NFLX_data[i + 3]['price'])
    day5 = float(NFLX_data[i + 4]['price'])
    print(NFLX_data[i])
    
    fivedayz3 = stats.pstdev([day1,day2,day3,day4,day5])

    NFLX_stdev.append(fivedayz3)
    i += 5



print(NFLX_stdev)

fig, ax = plt.subplots() 
plt.plot(NFLX_stdev, linestyle = 'dashed')  
plt.savefig("NFLX_stdev.png")

