import urllib.request
import json

while True:
    myin = input("Please enter the country code or enter quit:")
    if( myin == "quit" ):                       #quit the program
        print("Thanks for searching!")
        break
    try:
        url = "https://restcountries.eu/rest/v1/alpha/"+ myin
        page = urllib.request.urlopen(url)
        content = page.read()                   #read the page
        content_string = content.decode("utf-8")#convert to string
        json_data = json.loads(content_string)  #load the data
        print(json_data["name"], json_data["capital"])
    except urllib.error.HTTPError:              #through exceptions
        print("Sorry,cannot find the country code")

#-----------------------------------------------simple output
#/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 /Users/QW/Documents/UNH/untitled8/homework5-2.py
#Please enter the country code or enter quit:de
#Germany Berlin
#Please enter the country code or enter quit:com
#Comoros Moroni
#Please enter the country code or enter quit:chi
#Sorry,cannot find the country code
#Please enter the country code or enter quit:quit
#Thanks for searching!

#Process finished with exit code 0
