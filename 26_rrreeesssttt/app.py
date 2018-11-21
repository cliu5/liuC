#Claire Liu 
#SoftDev1 PD6
#K26: Getting More REST
#2018-11-14  

from flask import Flask, render_template
import urllib.request
import json
import ssl
import random

context = ssl._create_unverified_context()

app=Flask(__name__)

@app.route("/")
def met():
    urlData = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"
    num=436535
    webURL = urllib.request.urlopen(urlData+str(num),context=context)
    data = webURL.read()
    data = json.loads(data)
    print("------------")
    print(data)
    print("-----------")
    imageURL=data['primaryImage']
    print(imageURL)
    department=data['department']
    title=data['title']
    location=data['repository']
    medium=data['medium']
    objectURL=data['objectURL']
    print(imageURL)
    return render_template( "index.html", _title = title, _department=department, thisImage=imageURL,_location=location,_medium=medium,_objectURL=objectURL)
    
@app.route("/poem")
def poem():
    urlData="https://www.poemist.com/api/v1/randompoems"
    webURL=urllib.request.urlopen(urlData,context=context)
    data=webURL.read()
    data=json.loads(data)
    print("------------")
    print(data)
    print("-----------")
    title=data[0]['title']
    poem=data[0]['content']
    urlPoem=data[0]['url']
    poet=data[0]['poet']['name']
    return render_template("poem.html",_title=title,_poem=poem,_urlPoem=urlPoem,_poet=poet)

@app.route("/advice")
def advice():
    urlData="https://api.adviceslip.com/advice"
    webURL=urllib.request.urlopen(urlData,context=context)
    data=webURL.read()
    data=json.loads(data)
    print("------------")
    print(data)
    print("-----------")
    advice=data['slip']['advice']
    slip=data['slip']['slip_id']
    return render_template("advice.html",_advice=advice,_slip=slip)


@app.route("/google")
def google():
#https://www.googleapis.com/customsearch/v1?key=INSERT_YOUR_API_KEY&cx=017576662512468239146:omuauf_lfve&q=lectures
    
    urlData="https://www.googleapis.com/customsearch/v1?key="
    key="AIzaSyDLFqAoBs-xQCm9XPVAlTsTa0jG8ewM57k"
    urlData2="&cx=009364855531151632334:atzshazndou&q=dog"
    webURL=urllib.request.urlopen(urlData+key+urlData2,context=context)
    data=webURL.read()
    data=json.loads(data)
    print("------------")
    #print(data)
    print(data['items'][0]['title'])
    print("-----------")
    title=data['items'][0]['title']
    return render_template("google.html",_title=title)


if __name__ == "__main__":
    app.debug = True
    app.run()

