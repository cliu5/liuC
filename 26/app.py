#Claire Liu 
#SoftDev1 PD6
#K26: Getting More REST
#2018-11-14  

from flask import Flask, render_template
import urllib.request
import json
import ssl

context = ssl._create_unverified_context()

app=Flask(__name__)

@app.route("/")
def root():
    urlData = "https://api.darksky.net/forecast/"
    key="05b582b1b877c93d2e9c83ad56f7da98/"
    latitude="40.7128,"
    longitude="-74.0060"
    webURL = urllib.request.urlopen(urlData+key+latitude+longitude,context=context)
    data = webURL.read()
    data = json.loads(data)
    print("------------")
    print(data)
    print("-----------")
    print(data['timezone'])
    '''
    print(title)
    author=data['articles'][4]['author']
    url=data['articles'][4]['url']
    urlToImage=data['articles'][4]['urlToImage'] 

    return render_template( "index.html", _title = title, _author=author, _url=url, _urlToImage=urlToImage)
    
    
    '''
if __name__ == "__main__":
    app.debug = True
    app.run()

