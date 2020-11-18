'''
# -*- coding: utf-8 -*-

Created on Wed Oct  2 21:51:38 2019

created By Jimen Luhar
 
'''

import requests
from datetime import date
from datetime import datetime
#from flask import Flask, request
#from twilio.twiml.messaging_response import MessagingResponse






class Weather:
    def __init__(self,city):
        #self.city="Pune"
        
        if city.upper()=='WEATHER':
            self.city="Pune"
    
        else:
            self.city=city.split()[1]
        
        self.link="http://api.weatherstack.com/current?access_key=157e6ccff6fa4f7b62edaf3b1ac8bb02&query={}".format(self.city)

    
    def getweather(self):
        resp=requests.get(self.link).json()
        cur_weather=""        
        try:
            for key in resp["current"]:
                if key!="weather_icons":
                    cur_weather+="{} : {}\n".format(key,resp["current"][key])
            
        
        except : 
            cur_weather="City Invalid"#Developed By Atharva Sagale
        
        return cur_weather


class News:
    def __init__(self):
        self.news_link='https://newsapi.org/v2/top-headlines?country=in&apiKey=53e767e922d44b5984a597ce57e04b2e'
        #self.apikey="53e767e922d44b5984a597ce57e04b2e"
        #self.todaydate=date.today()
        #self.topic=topic
        #self.para={'q':self.topic,"from":self.todaydate,"sortBy":"publishedAt","apiKey":self.apikey}
        #getnews()
    
    def getnews(self):
        response=requests.get(self.news_link).json()
        news=[]
        title=''
        description=''
        content=''
        count=0
        temp=0
        for i in response['articles']:
            if (temp==0):
                temp+=1
                continue

            #if i['source']['name']=='Indianexpress.com':
            news_dict={'Title':i['title'],'Description':i['description'],'Content':i['content']}
            news.append(news_dict)
            count+=1
            if count==5:
                break
        return news
        
class Railstatus:
    def __init__(self,number):
        self.number=number
        #self.apikey="b5eee7839096d6a69e44dec6940e2742"
        self.link="https://indianrailapi.com/api/v2/livetrainstatus/apikey/b5eee7839096d6a69e44dec6940e2742/trainnumber/{}/date/{}/".format(self.number,datetime.today().strftime('%Y%m%d'))
        #self.todaydate=date.today()
        #self.para={"apiKey":self.apikey,"trainnumber":self.number,"date":self.todaydate}
        
        
    def getstatus(self):
        response=requests.get(self.link).json()
        return response
        

        
        
        
class Livecricket:
    def __init__(self):
        """
        Declaring the endpoints, apikey
        """
        self.url_get_all_matches = "http://cricapi.com/api/matches"
        self.url_get_score="http://cricapi.com/api/cricketScore"
        self.unique_id = ""#"1166965"  # unique to every match     http://cricapi.com/api/matches/?apikey=IBVtU2pHIHaAs3kKnAXmEPXP8Lw1
        self.api_key = "IBVtU2pHIHaAs3kKnAXmEPXP8Lw1"#YOUR_CRICAPI_KEY


    def displayscore(self,team):
        self.team=team
        """
        Returns Indian cricket teams match id, if the match is Live
        :return:
        """
        uri_params = {"apikey": self.api_key}
        resp = requests.get(self.url_get_all_matches, params=uri_params)
        resp_dict = resp.json()
        uid_found=0
        for i in resp_dict['matches']:
            if (i['team-1'] == team or i['team-2'] == team) and i['matchStarted']:
                #todays_date = datetime.today().strftime('%Y-%m-%d')
                #todays_date = "2019-09-28"
                #if datetime.today().strftime('%Y-%m-%d') == i['date'].split("T")[0]:
                uid_found=1
                self.unique_id=i['unique_id']
                    #print(self.unique_id)
                break
        if not uid_found:
            self.unique_id=-1

        send_data=self.get_score(self.unique_id)
        return send_data
    
    
    def get_score(self,unique_id):
        data="" #stores the cricket match data
        if unique_id == -1:
            data="No {} matches today".format(self.team)
        else:
            uri_params = {"apikey": self.api_key, "unique_id": self.unique_id}
            resp=requests.get(self.url_get_score,params=uri_params)
            data_json=resp.json()
            #print(data_json)
            try:
                data="\nHere's the score : \n"+ "\n" + data_json['stat'] +'\n' + data_json['score']
            except KeyError as e:
                data="Something went wrong"
        return data