###################################################################################
#Youtube viewbot
#Made By Johnathan Heatherman/Vesuvian Hecktor/BlackHatVes
#I am not responsible for what you do with this code
from art import*
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH   = "/usr/bin/chromedriver"
windows = []

def new():
    print("What would you like to do")
    command = str(input('"New Link"? or "New bot acc"?'))
    command = command.upper()
    if command == "NEW LINK":
            newlink = str(input("Please Enter your link below\n"))
            with open("link.txt", "a") as l:
                newlink = newlink + "\n"
                l.writelines(newlink)
                l.close()
    if command == "NEW BOT ACC":
            newacc  = str(input("Please enter your new email:"))
            with open("email.txt", "a") as e:
                newacc  = newacc + "\n"
                e.writelines(newacc)
                e.close
            newpass = str(input("Please enter the password for the new acc:"))
            with open("Passwords.txt", "a") as p:
                newpass = newpass + "\n"
                p.writellines(newpass)
                p.close



def GetLogIn():
    with open("email.txt", "r") as e:
        email = []
        for line in e:
            striplist = line.strip()
            line_list = str(striplist)
            email.append(line_list)
    with open ("Passwords.txt", "r") as p:
        Pass = []
        for line in p:
            striplist = line.strip()
            line_list = str(striplist)
            Pass.append(line_list)

    return email, Pass



def YouTubeLinks():# gets the links for the videos you wish to bot
    with open("link.txt", "r") as l:# opens the txt file
        links = []# list to add them too
        for line in l:#for every link in the file
            striplist = line.strip() #stripper pole
            line_list = str(striplist)# lines and strippers
            links.append(line_list) #adds the file to the list
    return links #returns the list like a karen with trying to get free stuff



def YouTubeLike():
    LikeButton = driver.find_elements(By.xpath("//div[@id='info']//ytd-toggle-button-renderer[1]//a[1]//yt-icon-button[1]//button[1]//yt-icon[1]")) #finds that like button below
    LikeButton.click()# smashes that mf like button


def YouTubeComments():
    pass



    
def EmailLogin(email, Pass, windows):
    driver = webdriver.Chrome(PATH)
   
    
    for e, p in zip(email, Pass):
        e = e
        p = p
        driver.get("https://accounts.google.com/ServiceLogin/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3D%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=AddSession")
        #yeah i know big ass link
        element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id ="identifierId"]'))
    )
        loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]') #finds username buton
        loginBox.send_keys(e) #types email
  
        nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]') #finds next button 
        nextButton[0].click()#clicks next button
        element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id ="password"]/div[1]/div / div[1]/input'))
    )
  
        passWordBox = driver.find_element_by_xpath('//*[@id ="password"]/div[1]/div / div[1]/input') #finds password button 
        passWordBox.send_keys(p) #enters password
        element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id ="passwordNext"]'))
    )
  
        nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]') #finds next button 
        nextButton[0].click()#clicks next button
        current_window = driver.current_window_handle # gets the current window for later use
        windows.append(current_window) # Stores the handel for later use
        driver.switch_to.new_window('tab')# creates a new tab
    return driver



def YouTubeViewer2(url, typee, driver, windows):
    for win in windows: #for every window/tab we opened
        win = win#alsways make sure
        driver.switch_to.window(win) #switches windows to the correct one
        driver.get(url) #goes to the video and plays it
        if typee == 1:  #for both likes and comments
            YoutubeLike()
            YouTubeComments()
        if typee == 2: #just comments
            YouTubeComments()
        if typee == 3: #just likes
            YouTubeLike()
            
        


        
def YouTubeViewer(url, windows, driver):
    for win in windows: #for every window/tab we opened
        win = win #alsways make sure
        driver.switch_to.window(win) #switches windows to the correct one
        driver.get(url) #goes to the video and plays it



def main():# Most the stuff in here is pretty basic just 2 if statements
    todo = str(input('would you like to: "modify lists" or: "start the bot"?\n'))
    todo = todo.upper() #makes my input case insensitive
    if todo == "MODIFY LISTS":
        new()
        main()#loop back here to run the script
    if todo == "START THE BOT":
        print("Would you like \nlikes and comments1 \ncomments2\nlikes3\nor just views4")
        typee = int(input("1, 2, 3, 4: "))
        email, Pass  = GetLogIn() #Fetches the log in credentials
        links        = YouTubeLinks()# grabs the videos you wish to bot
        driver = EmailLogin(email, Pass, windows)#logs into the email
        for url in links:
            url = str(url)
            if typee == 4:#just views
                YouTubeViewer(url, windows, driver)
            if typee == 3 or typee == 2 or typee == 1:
                YoutubeViewer2(links, typee)#the combination of both or each one
            elif typee > 4 and typee < 1 and typee == str(typee):
                print("Invalid input please try again")
                main()
            time.sleep(1200)#waits 20 mins beofre switching to a new vid
    elif todo != "MODIFY LISTS" and todo != "START THE BOT":
        print("invalid input please try again")
        main()



banner = text2art("YT Fertalizer", font = "rand")
print (banner)
print ("""
Art by John Eidson
              (      )
              ~(^^^^)~
               ) @@ \~_          |\
              /     | \        \~ /
             ( 0  0  ) \        | |       Hey
              ---___/~  \       | |           Hiya
               /'__/ |   ~-_____/ |                Doin?
o          _   ~----~      ___---~
  O       //     |         |
         ((~\  _|         -|                Oops! I mean MOOOOOOO
   o  O //-_ \/ |        ~  |
        ^   \_ /         ~  |
               |          ~ |
               |     /     ~ |
               |     (       |
                \     \      /\               -John Eidson-
               / -_____-\   \ ~~-*
               |  /       \  \       .==.
               / /         / /       |  |
             /~  |      //~  |       |__|
             ~~~~        ~~~~
             """)                                             # Just a cute ass smoking cow i found online



print("Made By Johnathan Heatherman/Vesuvian Hecktor/BlackHatVes")
print("       I am not responsible for what you do with this code   ")  
print("Hello Welcome To YT Fertalizer\nThis program adds some fertalizer so kickstart organic growth!")
main()








