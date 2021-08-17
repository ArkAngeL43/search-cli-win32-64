import os
import sys 
import time 
import webbrowser


def art():
    print(''' 
________________________________________
current search queries are the following|
________________________________________|
        ''')

def cls():
    os.system('cls')

def CS(X):
    time.sleep(X)
    cls()

cls()
art()
print(" [+] Amazon ")
time.sleep(0.1)
print(" [+] Google ")
time.sleep(0.1)
print(" [+] Youtube ")
time.sleep(1)
A = str(input(" what website would you like to search? => "))
cls()




if 'amazon' in A:
            CS(1)
            print(" [!] ok, now what is the content you would like to search  ")
            B = str(input(" => "))
            url = (f" https://www.amazon.com/s?k={B} ")
            webbrowser.open(url)

elif 'Youtube' in A:
               CS(1)
               print(" [+] alright then, what is the content you would like to search? ")
               B = str(input(" =>  "))
               url = (f"https://www.youtube.com/results?search_query={B}")
               webbrowser.open(url)

elif 'youtube' in A:
               CS(1)
               print(" [+] alright then, what is the content you would like to search? ")
               print(" EX | kalle hallden ")
               B = str(input(" =>  "))
               url = (f"https://www.youtube.com/results?search_query={B}")
               webbrowser.open(url)


elif 'google' in A:
              CS(1)
              print(" [+] alright then, what is the content you would like to search? ")
              B = str(input(" =>  "))
              url = (f" https://www.google.com/search?q={B}")
              webbrowser.open(url)

elif 'Google' in A:
              CS(1)
              print(" [+] alright then, what is the content you would like to search? ")
              B = str(input(" =>  "))
              url = (f"https://www.google.com/search?q={B}")
              webbrowser.open(url)

elif 'Amazon' in A:
              time.sleep(1)
              os.system(' clear ')
              print(" [!] ok, now what is the content you would like to search  ")
              B = str(input(" => "))
              url = (f" https://www.amazon.com/s?k={B} ")
              webbrowser.open(url)
