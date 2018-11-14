#Claire Liu + Addison Huang
#SoftDev1 PD6
#K24: A RESTful Journey Skyward
#2018-11-13  

from flask import Flask, render_template
import urllib.request
import json
import ssl

 #Taken from Cathy's QAF post
context = ssl._create_unverified_context()

app=Flask(__name__)

@app.route("/")
def root():
    urlData = "https://api.nasa.gov/planetary/apod?api_key=wv7X1ZwzclmKH1VSh8sqjgoYeip2bc6rl2tAXtJS"
    
    webURL = urllib.request.urlopen(urlData,context=context)
    
    data = webURL.read()
    print(data)
    #CONVERSION TO JSON
    #encoding = webURL.info().get_content_charset('utf-8')
    data = json.loads(data)
    #print(dic)
    #print (dic['url'])
    img_data=data['url']
    return render_template( "index.html", url = img_data)
    
    
    
if __name__ == "__main__":
    app.debug = True
    app.run()

