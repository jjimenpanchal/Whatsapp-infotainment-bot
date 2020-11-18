'''
# -*- coding: utf-8 -*-

Created on Wed Oct  2 21:51:38 2019

created By Jimen Luhar
 
'''
from classes import *

        
def getoutput(choice):
    send_message="No output"
    try:
        
        choice=int(choice)
        #send_message="No Output1"
        if len(str(abs(choice)))==5:
            try:
                send_message=""
                trainobj=Railstatus(choice)
                trainstatus=trainobj.getstatus()
                #current_status=""
                for key in trainstatus["CurrentStation"]:
                    #print("{}: {}".format(key, trainstatus["CurrentStation"][key]))
                    send_message+="\n{}: {}".format(key, trainstatus["CurrentStation"][key])
            except Exception as exc:
                return "This Train Is Not Available Due To Covid-19"
        else:
            send_message="No Such Train Available"
        return send_message
    
    except Exception as e1:
        if choice.upper()=="NEWS":
            send_message="News:\n"
            newsobj=News()
            news=newsobj.getnews()
            count=0
            for i in news:
                #print(count+1,"\nTitle:\n",i['Title'],"\nDescription:\n",i['Description'],"\n")
                send_message+="\nTitle:\n{}\nDescription:\n{}\n".format(i['Title'],i['Description'])
            return send_message
        
        
        elif choice[0].capitalize()=='T':
            team=choice[2:]
            team=team.title()
            try:
                team=int(team)
                
            except Exception as e4:
                cricketobj=Livecricket()
                score=cricketobj.displayscore(team)
                return score
        
        
    

        elif choice[0:7].upper()=="WEATHER":
            weather_obj=Weather(choice)
            cur_weather=weather_obj.getweather()
            return cur_weather
            
            
            
        elif choice.upper()=="MENU" or choice.upper()=="FEATURES":
            send_message="***Features***\n\n1.Live Cricket Scores - put command as 'T team_name' eg; T India\n\n2. Weather Report Put command as 'weather city_name' eg; weather pune \n\n3. Live Train Status Put command as 'Train_no' eg; 12140 \n\n4. News update Put command as 'News' !!!Happy to serve you!!!"




    
        
    return send_message
