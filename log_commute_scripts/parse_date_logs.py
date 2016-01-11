import time
import datetime
import matplotlib.pyplot as plt


punchin_lines = open('punch_in.txt','r').readlines()
punchout_lines = open('punch_out.txt','r').readlines()

times = []
days_dict = {}
months_dict = {}
years_dict = {}
for i in range(len(punchin_lines)):
    start = time.mktime(datetime.datetime.strptime(punchin_lines[i].strip(),"%a %b %d %H:%M:%S EST %Y").timetuple())
    end = time.mktime(datetime.datetime.strptime(punchout_lines[i].strip(),"%a %b %d %H:%M:%S EST %Y").timetuple())
    
    day = punchin_lines[i].split(" ")[0].strip()
    month = punchin_lines[i].split(" ")[1].strip()
    year = punchin_lines[i].split(" ")[-1].strip()
    dt = end - start
    times.append(dt)
    if day not in days_dict.keys():
        days_dict[day] = []
    days_dict[day].append(dt)
    
    if month not in months_dict.keys():
        months_dict[month] = []
    months_dict[month].append(dt)

    if year not in years_dict.keys():
        years_dict[year] = []
    years_dict[year].append(dt)
    
    
    
    print dt,'secs'
    print day,month,year
    #print dt/60,',min'
    #print dt/3600,',hrs'
    
plt.figure()
plt.plot(range(len(times)),times)
plt.title('trips')

for day in days_dict.keys():
    plt.figure()
    plt.title(day)
    plt.plot(range(len(days_dict[day])),days_dict[day])
    
for month in months_dict.keys():
    plt.figure()
    plt.title(month)
    plt.plot(range(len(months_dict[month])),months_dict[month])
    
for year in years_dict.keys():
    plt.figure()
    plt.title(year)
    plt.plot(range(len(years_dict[year])),years_dict[year])
    
plt.show()