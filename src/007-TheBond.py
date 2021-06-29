#author: Sayyed Viquar Ahmed 
import pyfiglet
from igdox import dox
import os
from googlesearch import search
import phonenumbers as p
from phonenumbers import carrier
from phonenumbers import geocoder
import json 
import time 
from urllib.request import urlopen
import requests
import sys
import urllib
import logging
from username import *

     
def check(inputt):
    try:
        print("\n")
        #inputt = str(input("Ussername : "))
        acc = dox(inputt)
        print("[*] Username: " + inputt)
        
        print("[-] Id : " + str(acc.user_id()))
        
        print("[*] Url : " + str(acc.url()))
        print("[*] Number of Post  : " + str(acc.posts()))
        
        print("[*] Followers : " + str(acc.followers()))
        
        print("[*] Number of following :\t    " + str(acc.following()))
    
        print("[*] Bio : " + str(acc.bio()))    
        
        if acc.private() == False:
            print("[*] Private Account : No")
        else:
            print("[*] Private Account : Yes")
            if acc.verified() == False:
                print("[*] Verified: No")
            else:
                print("[*] Verified : Yes")
                print(acc.verified())
                
        print('\n')
        return None
    except urllib.error.HTTPError as e:
        print("User not found")
        return ("User not found")
         
def web_search(query):
    print("\n")
    try :
        i = 0
        for j in search(query, tld="co.in", num=40, stop=40, pause=2): 
            print(j)
            i += 1
        #tis is just t raise error when search holds no results
        if i ==0:
            print("outloop")
            raise StopIteration
        return None
    except StopIteration:
        print("Can't Search your Query")
        return("Can't Search your Query")


def number(no):
    print("\n")
    try:
        #no = str (input("Enter number : \t"))
        ph_no = p .parse(no)
        geo_location = geocoder.description_for_number(ph_no,'en')
        no_carrier = carrier.name_for_number(ph_no,'en')
        print ("Country : ",geo_location)
        print ("Sim Provider : ", no_carrier)
        return None
    except Exception :
        print("No data found for this number")
        return("No data found for this number")

def find_ip(ip):
    try :
        #ip=str(input ("Enter Ip address "))
        url="http://ip-api.com/json/"+ip

        values = json.load(urlopen(url))
        print("[*] Ip Address : ",values['query'])
        print("[*] Country :\t ",values['country'])
        print("[*] City : ",values['city'])
        return None
    except Exception as e:
        print("\n Can't find the information for the given ip address ")
        return("\n Can't find the information for the given ip address ")

     
# main function 
if  __name__=="__main__":
  
    banner=pyfiglet.figlet_format("007-The Bond", font="slant")
    print(banner)
    
    
    print(" \t Script by DeadShot0x7  V 2.0")
    print("\n \n")
    print("DeadShot0x7 will not be responsible for the  Loss you have made ,Enter y or n")
    ans=str(input(">>>>>>>>>"))
    if ans == 'y' or ans =="yes" or ans=="Y":
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info("Yes I'm Responsbile for the loss I have done ")
        
        
    while(1):
        os.system("clear") 
        banner=pyfiglet.figlet_format("007-The Bond", font="slant")
        print(banner)
    
    
        print(" \t Script by DeadShot0x7  V 2.0")
        print("\n \n")
        print("1.Instagram \t 2.Search")
        print("3.Phoneloopkup \t 4.Iplookup")
        print("5.Update \t 6.Search username Across the Social Media")
        print("7.Exit")
        a=int(input("Select your option :\t"))
        if a == 1:
            inputt = str(input("Ussername : "))
            check(inputt)
        if a ==2:
            query = str ( input ("Search :")  )
            web_search(query)
        if a == 3:
            no = str (input("Enter number with country code : \t"))
            number(no)
        if a == 4:
            ip=str(input ("Enter Ip address "))
            find_ip(ip)
        if a == 5:
            try :
                os .system("git pull")
            except Exception as e:
                print("Check your Internet Connection or No repository found")
        if a == 6:
            name=str(input ("Enter Username"))
            instagram(name)
            facebook(name)
            pinterest(name)
            
            
            
        if a == 7:
            print("Closing the application in 10 second")
            time.sleep(1)
            break

    

       
    



    
