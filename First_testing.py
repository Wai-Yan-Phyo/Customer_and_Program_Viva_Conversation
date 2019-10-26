#This Program is created by Wai Yan Phyo : 26.10.2019
#For customer and program viva speech 


## Library import-------------------------------------#
from __future__ import print_function
from espeak import espeak
from playsound import playsound
import subprocess


import random
import time 
import sys 
import speech_recognition as sr
#-----------------------------------------------------#

#Create Dict for Menu Items and its value-------------#
Dict = { 'breakfast sandwich':'1500',
         'hamburger':'1800',
          'hot dog':'1200',
          'hot.':'1200',
          'noodle soup':'2000',
          'hot coffee':'500',
          'iced coffee':'1000',
          'ice coffee':'1000',
          'milk':'800',
           'ice cream':'1000',
           'lime juice':'800',
           'Fried Chicken':'1700',
           'french fries':'1200',
           'fried meatball':'1500',

          }
#-----------------------------------------------------#

#Create list for store list---------------------------#
Store_list = []

recognizer = sr.Recognizer()
microphone = sr.Microphone()

##Speech to Text Function-----------------------------#
def recon_speech_for_mic(recognizer,microphone):
    
    #check recognizer and microphone type

    if not isinstance(recognizer,sr.Recognizer):
       raise TypeError (" recognizer must be Recognizer instance")

    if not isinstance(microphone,sr.Microphone):
       raise TypeError ("microphone must be Microphone instance")

    with microphone as source:
         recognizer.adjust_for_ambient_noise(source)
         audio = recognizer.listen(source)

    response = { "success":True,"error":None,"transcription":None }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
        
        print(response)

    except sr.RequestError:
           response["success"] = False
           response["error"] = "API unavailable"
    except sr.UnknownValueError:
          response["error"] = "Unable to recognize speech"

    
    return response

## Speak output Function------------------------------------------------#
def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output



## Text to Speech Function ----------------------------------------------#
def Text_to_Speech(text):
    
    user_speech = text
    
    if user_speech == "finish":
       f1 = 'Thank For Your Order Sir'
       c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f1) 
       Bill = str(sum(Store_list))
       Bill_speech = 'Since You Prove Your Bill is %s'%(Bill)
       c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(Bill_speech) 
       execute_unix(c)

    elif user_speech == 'hello':
         #f2 = 'milk is great'
         #c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f2)
         playsound('./voice/Tin.mp3')
         #Order_value = Dict[user_speech]
         #Store_list.append(int(Order_value))
         

    elif user_speech == 'breakfast sandwich':
         
         #f4 = "Yes It's really great"
         #c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f4)
         playsound('./voice/Breakfast sandwich.mp3')
         Order_value = Dict[user_speech]
         Store_list.append(int(Order_value))

    elif user_speech == 'hamburger':
         #f5 = 'Good'
         #c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f5)
         playsound('./voice/Humburger.mp3')
         Order_value = Dict[user_speech]
         Store_list.append(int(Order_value))

    elif user_speech == 'hot dog':
         #f6 = 'Good for You'
         #c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f6)
         playsound('./voice/Hotdog.mp3')
         Order_value = Dict[user_speech]
         Store_list.append(int(Order_value))
    elif user_speech == 'hot.':
         #f6 = 'Good for You'
         #c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f6)
         playsound('./voice/Hotdog.mp3')
         Order_value = Dict[user_speech]
         Store_list.append(int(Order_value))
    
    elif user_speech == 'noodle soup':
         #f7 = 'ice cream is awesome'
         #c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f7)
         playsound('./voice/Noodle.mp3')
         Order_value = Dict[user_speech]
         Store_list.append(int(Order_value))

    elif user_speech == 'hot coffee':
         #f7 = 'ice cream is awesome'
         #c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f7)
         playsound('./voice/hot coffee.mp3')
         Order_value = Dict[user_speech]
         Store_list.append(int(Order_value))
    elif user_speech == 'iced coffee':
         #f7 = 'ice cream is awesome'
         #c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f7)
         playsound('./voice/ice coffee.mp3')
         Order_value = Dict[user_speech]
         Store_list.append(int(Order_value))
    elif user_speech == 'ice coffee':
         #f7 = 'ice cream is awesome'
         #c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f7)
         playsound('./voice/ice coffee.mp3')
         Order_value = Dict[user_speech]
         Store_list.append(int(Order_value))
    elif user_speech == 'milk':
         #f7 = 'ice cream is awesome'
         #c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f7)
         playsound('./voice/Milk.mp3')
         Order_value = Dict[user_speech]
         Store_list.append(int(Order_value))
    elif user_speech == 'ice cream':
         #f7 = 'ice cream is awesome'
         #c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f7)
         playsound('./voice/ice cream.mp3')
         Order_value = Dict[user_speech]
         Store_list.append(int(Order_value))
    elif user_speech == 'lime juice':
         #f7 = 'ice cream is awesome'
         #c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f7)
         playsound('./voice/lime juice.mp3')
         Order_value = Dict[user_speech]
         Store_list.append(int(Order_value))
    elif user_speech == 'Fried Chicken':
         #f7 = 'ice cream is awesome'
         #c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f7)
         playsound('./voice/fried chicken.mp3')
         Order_value = Dict[user_speech]
         Store_list.append(int(Order_value))
    elif user_speech == 'french fries':
         #f7 = 'ice cream is awesome'
         #c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f7)
         playsound('./voice/french fries.mp3')
         Order_value = Dict[user_speech]
         Store_list.append(int(Order_value))
    elif user_speech == 'fried meatball':
         #f7 = 'ice cream is awesome'
         #c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f7)
         playsound('./voice/fried meatball.mp3')
         Order_value = Dict[user_speech]
         Store_list.append(int(Order_value))





    elif user_speech == 'song for me':
         playsound('./Phillip Phillips - Gone, Gone, Gone.mp3')
    else:
         playsound('./voice/sry.mp3')
        # f3 = "Sorry i don't understand Please Say again"
         
         #c = 'espeak -ven+f4 -k20 -s150 -p80 --punct="<characters>" "%s" 2>>/dev/null'%(f3)
#    return execute_unix(c)

if __name__ == "__main__":
   
   text = 'No'
   while text != "My Order is Done":
         response = recon_speech_for_mic(recognizer,microphone)
         text = response["transcription"]
         
         Text_to_Speech(text)
   

