from random import *
number=int(input('How many locations do you need weather data for? '))
location=[]
ptype=[]
temp1=[]
temp2=[]
rain=[]
snow=[]
wind=[]
windchill=[]
heat_index=[]
max_temp=[]
min_temp=[]
winter_conditions=['Overcast','Heavy Snow','Blowing Snow','Sleet','Light Snow','Heavy Snow','Blowing Snow','Sleet','Light Snow','Heavy Snow','Blowing Snow','Sleet','Light Snow','Heavy Snow','Blowing Snow','Sleet','Light Snow','Heavy Snow','Blowing Snow','Sleet','Light Snow','Heavy Snow','Blowing Snow','Sleet','Light Snow']
summer_conditions=['Overcast','Thunder','Thunderstorm','Heavy Rain','Thunder','Thunderstorm','Heavy Rain','Thunder','Thunderstorm','Heavy Rain','Thunder','Thunderstorm','Heavy Rain','Thunder','Thunderstorm','Heavy Rain','Thunder','Thunderstorm','Heavy Rain']
mixed_conditions=['Overcast','Mixed Precip','Unknown Precip','Mixed Precip','Unknown Precip','Mixed Precip','Unknown Precip','Mixed Precip','Unknown Precip','Mixed Precip','Unknown Precip','Mixed Precip','Unknown Precip','Mixed Precip','Unknown Precip']
winter_weather=[]
summer_weather=[]
mixed_weather=[]
for i in range(0,number):
    location.append(input('Please enter location ''{}'': '.format(i+1)))
    ptype.append(input('What type of precip is ''{}'' expecting (rain, snow, or both)? '.format(location[i])))
    rain.append(uniform(0,15))
    snow.append(uniform(0,69))
    wind.append(randint(0,269))
    winter_weather.append(winter_conditions[randint(0,len(winter_conditions))])
    summer_weather.append(summer_conditions[randint(0,len(summer_conditions))])
    mixed_weather.append(mixed_conditions[randint(0,len(mixed_conditions))])
    if ptype[i].lower()=='snow':
        temp1.append(randint(-50,40))
        temp2.append(randint(-50,40))
    elif ptype[i].lower()=='rain':
        temp1.append(randint(30,120))
        temp2.append(randint(30,120))
    else:
        temp1.append(randint(30,40))
        temp2.append(randint(30,40))
    if temp1[i]>temp2[i]:
        max_temp.append(temp1[i])
        min_temp.append(temp2[i])
    else:
        max_temp.append(temp2[i])
        min_temp.append(temp1[i])
    windchill.append(randint(-100,min_temp[i]))
    heat_index.append(randint(max_temp[i],169))
for i in range(0,number):
    print('Observed weather for ''{}'.format(location[i]))
    if ptype[i].lower()=='snow':
        print('{}'.format(winter_weather[i]))
    elif ptype[i].lower()=='rain':
        print('{}'.format(summer_weather[i]))
    elif ptype[i].lower()=='both':
        print('{}'.format(mixed_weather[i]))
    else:
        print('That wasn\'t an option, you dumbass.')
    print('Max temp: ''{}''°F''\n''Min Temp: ''{}''°F''\n''Max Wind Gust: ''{}'.format(max_temp[i],min_temp[i],wind[i]))
    if min_temp[i]<40:
        print('Wind Chill: ''{}''°F'.format(windchill[i]))
    if max_temp[i]>80:
        print('Heat Index: ''{}''°F'.format(heat_index[i]))
    if ptype[i].lower()=='snow':
        if winter_weather[i].lower()=='overcast':
            print('Snowfall: 0.0 inches. Sorry, you busted.''\n')
        else:
            print('Snowfall: ''{}'' inches''\n'.format(round(snow[i],1)))
    elif ptype[i].lower()=='rain':
        if summer_weather[i].lower()=='overcast':
            print('Rainfall: 0.03 inches. Sorry, try again tomorrow.''\n')
        else:
            print('Rainfall: ''{}'' inches''\n'.format(round(rain[i],2)))
    elif ptype[i].lower()=='both':
        if mixed_weather[i].lower()=='overcast':
            print('Snowfall: 0.1 inches''\n''Rainfall: 0.09 inches. Better luck next time.''\n')
        else:
            print('Snowfall: ''{}'' inches''\n''Rainfall: ''{}'' inches''\n'.format(round(snow[i],1),round(rain[i],2)))
    elif ptype[i].lower()=='cum':
        print('Precip: sticky white stuff.''\n')
    else:
        print('That is not a valid precip type, you moron.''\n')
