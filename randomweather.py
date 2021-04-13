from random import *
from math import *
number=int(input('How many locations do you need weather data for? '))
location=[]
ptype=[]
winter_conditions=['Overcast','Heavy Snow','Blowing Snow','Sleet','Light Snow','Heavy Snow','Blowing Snow','Sleet','Light Snow','Heavy Snow','Blowing Snow','Sleet','Light Snow','Heavy Snow','Blowing Snow','Sleet','Light Snow','Heavy Snow','Blowing Snow','Sleet','Light Snow','Heavy Snow','Blowing Snow','Sleet','Light Snow']
summer_conditions=['Overcast','Thunder','Thunderstorm','Heavy Rain','Thunder','Thunderstorm','Heavy Rain','Thunder','Thunderstorm','Heavy Rain','Thunder','Thunderstorm','Heavy Rain','Thunder','Thunderstorm','Heavy Rain','Thunder','Thunderstorm','Heavy Rain']
mixed_conditions=['Overcast','Mixed Precip','Unknown Precip','Mixed Precip','Unknown Precip','Mixed Precip','Unknown Precip','Mixed Precip','Unknown Precip','Mixed Precip','Unknown Precip','Mixed Precip','Unknown Precip','Mixed Precip','Unknown Precip']
winter_warnings=['Winter Storm Watch', 'Blizzard Warning', 'Winter Storm Warning', 'Ice Storm Warning', 'Winter Weather Advisory', 'Wind Chill Advisory', 'Wind Chill Warning']
summer_warnings=['Severe Thunderstorm Watch', 'Severe Thunderstorm Warning', 'Tornado Watch', 'Excessive Heat Watch', 'Excessive Heat Warning', 'Tropical Storm Watch', 'Tropical Storm Warning', 'Hurricane Watch', 'Hurricane Warning']
other_warnings=['Red Flag Warning', 'High Wind Watch', 'High Wind Warning', 'Tornado Warning', 'Extreme Wind Warning', 'Flash Flood Watch', 'Flash Flood Warning', 'Flood Watch', 'Flood Warning']
winter_alerts=[]
summer_alerts=[]
other_alerts=[]
for i in range(0,number):
    location.append(input('Please enter location ''{}'': '.format(i+1)))
    ptype.append(input('What type of precip is ''{}'' expecting (rain, snow, or both)? '.format(location[i])))
for i in range(0,number):    
    rain=uniform(0,15)
    snow=uniform(0,69)
    wind=randint(0,269)
    rh=randint(1,100)
    winter_weather=winter_conditions[randint(0,len(winter_conditions)-1)]
    summer_weather=summer_conditions[randint(0,len(summer_conditions)-1)]
    mixed_weather=mixed_conditions[randint(0,len(mixed_conditions)-1)]
    if ptype[i].lower()=='snow':
        temp1=randint(-50,40)
        temp2=randint(-50,40)
    elif ptype[i].lower()=='rain':
        temp1=randint(30,120)
        temp2=randint(30,120)
    else:
        temp1=randint(30,40)
        temp2=randint(30,40)
    if temp1>temp2:
        max_temp=temp1
        min_temp=temp2
    else:
        max_temp=temp2
        min_temp=temp1
    windchill=int(round(35.74+(0.6215*min_temp)-(35.75*wind**0.16)+(0.4275*min_temp*wind**0.16),0))
    if rh<13 and 80<=max_temp<=112:
        heat_index=int(round((-42.379+2.04901523*max_temp+10.14333127*rh-0.22475541*max_temp*rh-0.00683783*max_temp**2-0.05481717*rh**2+0.00122874*max_temp**2*rh+0.00085282*max_temp*rh**2-0.00000199*max_temp**2*rh**2)-(((13-rh)/4)*sqrt((17-abs(max_temp-95))/17)),0))
    elif rh>85 and 80<=max_temp<=87:
        heat_index=(int(round((-42.379+2.04901523*max_temp+10.14333127*rh-0.22475541*max_temp*rh-0.00683783*max_temp**2-0.05481717*rh**2+0.00122874*max_temp**2*rh+0.00085282*max_temp*rh**2-0.00000199*max_temp**2*rh**2)+(((rh-85)/10)*((87-max_temp)/5)),0)))
    else:
        heat_index=int(round(-42.379+2.04901523*max_temp+10.14333127*rh-0.22475541*max_temp*rh-0.00683783*max_temp**2-0.05481717*rh**2+0.00122874*max_temp**2*rh+0.00085282*max_temp*rh**2-0.00000199*max_temp**2*rh**2,0))
    print('Observed weather for ''{}'.format(location[i]))
    if ptype[i].lower()=='snow':
        print('{}'.format(winter_weather))
    elif ptype[i].lower()=='rain':
        print('{}'.format(summer_weather))
    elif ptype[i].lower()=='both':
        print('{}'.format(mixed_weather))
    else:
        print('That wasn\'t an option, you dumbass.')
    print('Max temp: ''{}''°F''\n''Min Temp: ''{}''°F''\n''Max RH: ''{}''%''\n''Max Wind Gust: ''{}'' mph'.format(max_temp,min_temp,rh,wind))
    if min_temp<40:
        print('Wind Chill: ''{}''°F'.format(windchill))
    if max_temp>80:
        print('Heat Index: ''{}''°F'.format(heat_index))
    if ptype[i].lower()=='snow':
        if winter_weather.lower()=='overcast':
            print('Snowfall: 0.0 inches. Sorry, you busted.')
        else:
            print('Snowfall: ''{}'' inches'.format(round(snow,1)))
    elif ptype[i].lower()=='rain':
        if summer_weather.lower()=='overcast':
            print('Rainfall: 0.03 inches. Sorry, try again tomorrow.')
        elif summer_weather.lower()=='thunderstorm':
            print('Max hail size: ''{}'' inches'.format(round(uniform(0,7),1)))
        else:
            print('Rainfall: ''{}'' inches'.format(round(rain,2)))
    elif ptype[i].lower()=='both':
        if mixed_weather.lower()=='overcast':
            print('Snowfall: 0.1 inches''\n''Rainfall: 0.09 inches. Better luck next time.')
        else:
            print('Snowfall: ''{}'' inches''\n''Rainfall: ''{}'' inches'.format(round(snow,1),round(rain,2)))
    elif ptype[i].lower()=='cum':
        print('Precip: sticky white stuff.')
    else:
        print('That is not a valid precip type, you moron.')
    print('Active Warnings')
    if ptype[i].lower()=='snow':
        for n in range(0,randint(0,len(winter_warnings)-1)):
            print(winter_warnings[n])
        for n in range(0,randint(0,len(other_warnings)-1)):
            print(other_warnings[n])
    elif ptype[i].lower()=='rain':
        for n in range(0,randint(0,len(summer_warnings)-1)):
            print(summer_warnings[n])
        for n in range(0,randint(0,len(other_warnings)-1)):
            print(other_warnings[n])
    elif ptype[i].lower()=='both':
        for n in range(0,randint(0,len(winter_warnings)-1)):
            print(winter_warnings[n])
        for n in range(0,randint(0,len(summer_warnings)-1)):
            print(summer_warnings[n])
        for n in range(0,randint(0,len(other_warnings)-1)):
            print(other_warnings[n])
    elif ptype[i].lower()=='cum':
        print('Stop being horny.')
    else:
        print('No warnings beacuse you\'re dumb.')
    print()
