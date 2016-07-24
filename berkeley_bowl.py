import sys
import requests
import os
import re
import smtplib
import datetime
import time
import schedule
#from twilio.rest import TwilioRestClient

url = 'http://www.berkeleybowl.com/daily-hot-soup'
#accountSID = 'AC8e9e4720dde5d46e24cfc39dec4f166d'
#authToken = '9aa18abac5beaa28fca1321d46f5bc32'
#twilioCli = TwilioRestClient(accountSID, authToken)

count = 0
def gumbo_day(url): #checks bbowl to see if gumbo is on the menu and sends email
  text = os.popen('curl %s | lynx -stdin -dump'  %url).read()
  text = re.sub('[^a-zA-Z ]', '', text) # returns only alpha char
  text = re.sub('\s\s+', ' ', text) #strips extra spaces and tabs
  text = text.lower() #converts to lowercase
  if 'gumbo' in text: # checks if gumbo is in text
    output = ':), it"s GUMBO DAY.'
  else:
    output = 'No Gumbo, find another reason to live'

#later add call input to so pw is not stored in code
  smtpObj = smtplib.SMTP('smtp.gmail.com', 587) 
  smtpObj.ehlo()
  smtpObj. starttls()
  smtpObj.login('treverboles@gmail.com', 'Drake264')
  smtpObj.sendmail('treverboles@gmail.com', 'kimmer.tran@gmail.com', output)
  smtpObj.quit()
  count += 1
  return None

schedule.every().day.at('10:00').do(gumbo_day)

while count < 4 :
  schedule.run_pending()
  time.sleep(1)
