#Claire Liu
#SoftDev1 pd06
#K09 -- Solidify
#2018-09-20


from flask import Flask                                                         
app=Flask(__name__)                                                             
@app.route("/")                                                                 
def hello_world():                                                              
    print("about to print __name__...")                                         
    print(__name__)                                                             
    return """<b><h1 font-size="10rem" font-color=red> poopoo </h1></b>"""      
if __name__=="__main__":                                                        
    app.debug=True                                                              
    app.run()                                                                   
                     
