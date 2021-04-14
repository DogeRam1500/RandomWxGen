#!/usr/bin/python
from random import *
from math import *
#input number of locations
number=int(input('How many locations do you need weather data for? '))
#list of locations and expected precip
location=[]
ptype=[]
#list of conditions
winter_conditions=['Overcast']*2+['OMGThundersnowOMG']*3+['Heavy Snow']*8+['Blowing Snow']*8+['Sleet']*5+['Light Snow']*10+['Freezing Rain']*3
summer_conditions=['Overcast']*2+['Thunder']*2+['Thunderstorm']*15+['Heavy Rain']*15+['Mist']*2+['Hail']*10
mixed_conditions=['Overcast']*2+['Mixed Precip']*18+['Unknown Precip']*19
no_precip_conditions=['Overcast','Thunder','Mist']
#list of warnings
winter_warnings=['Winter Storm Watch', 'Winter Storm Warning', 'Winter Weather Advisory', 'Wind Chill Advisory']
summer_warnings=['Severe Thunderstorm Watch', 'Tornado Watch', 'Excessive Heat Watch', 'Tropical Storm Watch', 'Hurricane Watch']
other_warnings=['High Wind Watch', 'Tornado Warning', 'Flash Flood Watch', 'Flood Watch']
contexual_warnings=['Gorilla Hail','Blizzard Warning','Wind Chill Warning','Severe Thunderstorm Warning','Excessive Heat Warning','Tropical Storm Warning','Hurricane Warning','Red Flag Warning','High Wind Warning','Extreme Wind Warning','Flash Flood Warning','Flood Warning','Ice Storm Warning']
#input locations and expected precip
for i in range(0,number):
    location.append(input('Please enter location ''{}'': '.format(i+1)))
    ptype.append(input('What type of precip is ''{}'' expecting (rain, snow, both, or none)? '.format(location[i])).casefold())
#generate data
for i in range(0,number):    
#generate random conditions
    winter_weather=choice(winter_conditions)
    summer_weather=choice(summer_conditions)
    mixed_weather=choice(mixed_conditions)
    no_precip_weather=choice(no_precip_conditions)
    rh=randint(1,100)
    windchill='none'
    heat_index='none'
    rainfall='none'
    snowfall='none'
    hail='none'
#generate contextual values for "snow"
    if ptype[i]=='snow':
        temp1=randint(-50,40)
        temp2=randint(-50,40)
        if temp1>temp2:
            max_temp=temp1
            min_temp=temp2
        else:
            max_temp=temp2
            min_temp=temp1
#generate contexual winds and precips
        if winter_weather=='Overcast':
            wind=randint(0,42)
            snowfall=round(uniform(0,0.5),1)
        elif winter_weather=='OMGthundersnowOMG':
            wind=randint(0,169)
            snowfall=round(uniform(0,69),1)
        elif winter_weather=='Thundersnow':
            wind=randint(0,169)
            snowfall=round(uniform(0,69),1)
        elif winter_weather=='Heavy Snow':
            wind=randint(0,101)
            snowfall=round(uniform(0,69),1)
        elif winter_weather=='Blowing Snow':
            wind=randint(0,169)
            snowfall=round(uniform(0,19),1)
        elif winter_weather=='Sleet':
            wind=randint(0,101)
            snowfall=round(uniform(0,6),1)
        elif winter_weather=='Light Snow':
            wind=randint(0,101)
            snowfall=round(uniform(0,19),1)
        elif winter_weather=='Freezing Rain':
            wind=randint(0,101)
            rainfall=round(uniform(0,3),2)
#generate contextual values for "rain"
    elif ptype[i]=='rain':
        temp1=randint(30,120)
        temp2=randint(30,120)
        if temp1>temp2:
            max_temp=temp1
            min_temp=temp2
        else:
            max_temp=temp2
            min_temp=temp1
        if summer_weather=='Overcast':
            wind=randint(0,42)
            rainfall=round(uniform(0,0.05),2)
        elif summer_weather=='Thunder':
            wind=randint(0,69)
            rainfall=round(uniform(0,1),2)
        elif summer_weather=='Thunderstorm':
            wind=randint(0,269)
            rainfall=round(uniform(0,15),2)
        elif summer_weather=='Heavy Rain':
            wind=randint(0,101)
            rainfall=round(uniform(0,15),2)
        elif summer_weather=='Mist':
            wind=randint(0,42)
            rainfall=round(uniform(0,0.05),2)
        elif summer_weather=='Hail':
            wind=randint(0,269)
            rainfall=round(uniform(0,15),2)
            hail=round(uniform(0,7),1)
#generate contextual values for "both"
    elif ptype[i]=='both':
        temp1=randint(30,40)
        temp2=randint(30,40)
        if temp1>temp2:
            max_temp=temp1
            min_temp=temp2
        else:
            max_temp=temp2
            min_temp=temp1
        if mixed_weather=='Overcast':
            wind=randint(0,42)
            rainfall=round(uniform(0,0.05),2)
            snowfall=round(uniform(0,0.5),1)
        elif mixed_weather=='Mixed Precip':
            wind=randint(0,101)
            rainfall=round(uniform(0,5),2)
            snowfall=round(uniform(0,19),1)
        elif mixed_weather=='Unknown Precip':
            wind=randint(0,101)
            rainfall=round(uniform(0,5),2)
            snowfall=round(uniform(0,19),1)
#generate contextual values for "None"
    elif ptype[i]=='none':
        extreme=choice(['hot','cold'])
        if extreme=='hot':
                temp1=randint(70,120)
                temp2=randint(70,120)
                if temp1>temp2:
                    max_temp=temp1
                    min_temp=temp2
                else:
                    max_temp=temp2
                    min_temp=temp1
        else:
                temp1=randint(-50,20)
                temp2=randint(-50,20)
                if temp1>temp2:
                    max_temp=temp1
                    min_temp=temp2
                else:
                    max_temp=temp2
                    min_temp=temp1
        if no_precip_weather=='Overcast':
            wind=randint(0,42)
        elif no_precip_weather=='Thunder':
            wind=randint(0,69)
        else:
            wind=randint(0,42)
    elif ptype[i]=='cum':
        temp1=randint(-50,120)
        temp2=randint(-50,120)
        wind=69
        if temp1>temp2:
            max_temp=temp1
            min_temp=temp2
        else:
            max_temp=temp2
            min_temp=temp1    
#calculate windchill if min<40
    if min_temp<40:
        windchill=int(round(35.74+(0.6215*min_temp)-(35.75*wind**0.16)+(0.4275*min_temp*wind**0.16),0))
#calculate heat index if temp>80
    if max_temp>=80:
        if rh<13 and 80<=max_temp<=112:
            heat_index=int(round((-42.379+2.04901523*max_temp+10.14333127*rh-0.22475541*max_temp*rh-0.00683783*max_temp**2-0.05481717*rh**2+0.00122874*max_temp**2*rh+0.00085282*max_temp*rh**2-0.00000199*max_temp**2*rh**2)-(((13-rh)/4)*sqrt((17-abs(max_temp-95))/17)),0))
        elif rh>85 and 80<=max_temp<=87:
            heat_index=int(round((-42.379+2.04901523*max_temp+10.14333127*rh-0.22475541*max_temp*rh-0.00683783*max_temp**2-0.05481717*rh**2+0.00122874*max_temp**2*rh+0.00085282*max_temp*rh**2-0.00000199*max_temp**2*rh**2)+(((rh-85)/10)*((87-max_temp)/5)),0))
        else:
            heat_index=int(round(-42.379+2.04901523*max_temp+10.14333127*rh-0.22475541*max_temp*rh-0.00683783*max_temp**2-0.05481717*rh**2+0.00122874*max_temp**2*rh+0.00085282*max_temp*rh**2-0.00000199*max_temp**2*rh**2,0))
#print data
    print('Observed weather for ''{}'.format(location[i]))
#print observed conditions based on ptype
    if ptype[i]=='snow':
        print('{}'.format(winter_weather))
    elif ptype[i]=='rain':
        print('{}'.format(summer_weather))
    elif ptype[i]=='both':
        print('{}'.format(mixed_weather))
    elif ptype[i]=='none':
        print('{}'.format(no_precip_weather))
    elif ptype[i]=='cum':
        print('Horny today, aren\'t we?')
#print max temp, min temp, wind gust, max rh
    print('Max temp: ''{}''°F''\n''Min Temp: ''{}''°F''\n''Wind Gust: ''{}'' mph''\n''Max RH: ''{}''%'.format(max_temp,min_temp,wind,rh))
#print windchill if it exists
    if windchill!='none':
        print('Wind Chill: ''{}''°F'.format(windchill))
#print heat index
    if heat_index!='none':
        print('Heat Index: ''{}''°F'.format(heat_index))
#print precip
    if ptype[i]=='rain':
        if summer_weather!='Hail':
            print('Rainfall: ''{}'' inches'.format(rainfall))
        else:
            print('Rainfall: ''{}'' inches''\n''Max Hail Size: ''{}'' inches'.format(rainfall,hail))
    elif ptype[i]=='snow':
        if winter_weather!='Freezing Rain':
            if winter_weather=='Sleet':
                print('Sleetfall: ''{}'' inches'.format(snowfall))
            else:
                print('Snowfall: ''{}'' inches'.format(snowfall))
        else:
            print('Freezing Rain Accretion: ''{}'' inches'.format(rainfall))
    elif ptype[i]=='both':
        print('Snowfall: ''{}'' inches''\n''Rainfall: ''{}'' inches'.format(snowfall,rainfall))
    elif ptype[i]=='none':
        print('No precip')
    elif ptype[i]=='cum':
        print('Precip: sticky white stuff.')
    else:
        print('That wasn\'t a choice, you dumbass')
#print contextual warnings
    if snowfall!='none':
        if snowfall>=10 and wind>=35:
            print(contexual_warnings[1])
    if hail!='none':
        if hail>=6:
            print(contexual_warnings[0])
    if windchill!='none':
        if windchill<=20:
            print(contexual_warnings[2])
    if ptype[i]=='rain' or ptype[i]=='snow':
        if winter_weather=='OMGThundersnowOMG' or summer_weather=='Thunderstorm':
            if wind>=65:
                print(contexual_warnings[2])
    if heat_index!='none':
        if heat_index>=105:
            print(contexual_warnings[3])
    if ptype[i]=='snow':
        if winter_weather=='Freezing Rain':
            if rainfall>=1:
                print(contexual_warnings[13])
    if ptype[i]=='rain':
        if rainfall>=2 and wind>=63:
            print(contexual_warnings[4])
        elif rainfall>=2 and wind>=74:
            print(contexual_warnings[5])
    if ptype[i]=='none':
        if rh<=15 and wind>=15:
            print(contexual_warnings[6])
    if 58<=wind<=115:
        print(contexual_warnings[7])
    if wind>115:
        print(contexual_warnings[8])
    if rainfall!='none':
        if 2<=rainfall<=6:
            print(contexual_warnings[10])
        if rainfall>6:
            print(contexual_warnings[9])
#print random alerts
    if ptype[i]=='cum':
        print('Stop being horny.')
    elif ptype[i]=='rain' or ptype[i]=='snow' or ptype[i]=='both' or ptype[i]=='none':
        for n in range (0,len(other_warnings)-1):
            print(other_warnings[n])
        if ptype[i]=='snow':
            for n in range(0,len(winter_warnings)-1):
                print(winter_warnings[n])
        elif ptype[i]=='rain':
            for n in range(0,len(summer_warnings)-1):
                print(summer_warnings[n])
    else:
        print('No warnings because you\'re dumb.')
#add new line betwen cities
    print()            
