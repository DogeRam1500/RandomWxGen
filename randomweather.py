from random import *
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
    windchill=randint(-100,min_temp)
    heat_index=randint(max_temp,169)
    print('Observed weather for ''{}'.format(location[i]))
    if ptype[i].lower()=='snow':
        print('{}'.format(winter_weather))
    elif ptype[i].lower()=='rain':
        print('{}'.format(summer_weather))
    elif ptype[i].lower()=='both':
        print('{}'.format(mixed_weather))
    else:
        print('That wasn\'t an option, you dumbass.')
    print('Max temp: ''{}''°F''\n''Min Temp: ''{}''°F''\n''Max Wind Gust: ''{}'.format(max_temp,min_temp,wind))
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
    if ptype[i].lower()=='rain':
        for n in range(0,randint(0,len(summer_warnings)-1)):
            print(summer_warnings[n])
        for n in range(0,randint(0,len(other_warnings)-1)):
            print(other_warnings[n])
    if ptype[i].lower()=='both':
        for n in range(0,randint(0,len(winter_warnings)-1)):
            print(winter_warnings[n])
        for n in range(0,randint(0,len(summer_warnings)-1)):
            print(summer_warnings[n])
        for n in range(0,randint(0,len(other_warnings)-1)):
            print(other_warnings[n])
    print()
