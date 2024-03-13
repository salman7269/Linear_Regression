from flask import Flask, request, jsonify
import config
from project.utils import Economic_Index
import numpy as np

app=Flask(__name__)
@app.route("/")
def get_home():
    return "Hello Welcome to Enonomic_Index_Project."

@app.route("/predicted_index_price",methods= ["POST","GET"])
def get_Index_price():
    if request.method=="POST":
        data=request.form
        print("User Input Data: ",data)

        Interest_rate=eval(data["interest_rate"])
        Unemployment_rate=eval(data["unemployment_rate"])

        Eco_obj=Economic_Index(Interest_rate,Unemployment_rate)
        ind_price=Eco_obj.get_predicted_index_price()
        return jsonify({"Result":f"Predicted Index Price is {ind_price[0]}"})
    
if __name__=="__main__":
    app.run()
        