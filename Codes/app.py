'''
# -*- coding: utf-8 -*-

Created on Wed Oct  2 21:51:38 2019

created By Jimen Luhar
 
'''

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from getoutput import *

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    #resp=MassagingResponse()
    
    output=getoutput(msg)
       
    #Create reply
    resp = MessagingResponse()
    resp.message("{}".format(output))
    return str(resp)

    

if __name__ == "__main__":
    app.run(debug=True)
    
 #http://api.weatherstack.com/current?access_key=157e6ccff6fa4f7b62edaf3b1ac8bb02&query=New%20York