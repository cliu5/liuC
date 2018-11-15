#Claire Liu 
#SoftDev1 PD6
#K25: Getting More REST
#2018-11-14  

from flask import Flask, render_template
import urllib.request
import json
import ssl

context = ssl._create_unverified_context()

app=Flask(__name__)

@app.route("/")
def root():
    urlData = "https://newsapi.org/v2/everything?sources=buzzfeed&apiKey="
    key="c068ae23da9846c0b6d2c1bc2852dc2b"
    webURL = urllib.request.urlopen(urlData+key,context=context)
    
    data = webURL.read()
    print(data)
    #CONVERSION TO JSON
    #encoding = webURL.info().get_content_charset('utf-8')
    data = json.loads(data)
    #print(dic)
    #print (dic['url'])
    print("------------")
    print(data)
    print("-----------")
    
    title=data['articles'][4]['title']
    print(title)
    author=data['articles'][4]['author']
    url=data['articles'][4]['url']
    urlToImage=data['articles'][4]['urlToImage']    
    return render_template( "index.html", _title = title, _author=author, _url=url, _urlToImage=urlToImage)
    
    
    
if __name__ == "__main__":
    app.debug = True
    app.run()

