from flask import Flask,url_for,request,render_template
#import pandas as pd
import joblib

model=joblib.load("Linear_Regression_Model.lb")
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/prediction',methods=['GET','POST'])
def prediction():
    if request.method=="POST":
        Brand=int(request.form['brand_name'])
        Ownership=int(request.form['ownership'])
        Kms_driven=int(request.form['kms_driven'])
        Age=int(request.form['age'])
        Power=int(request.form['power'])

        unseen_data=[[Ownership,Brand,Kms_driven,Age,Power]] #x_variables
        
        predict=model.predict(unseen_data)[0] #passing data to model


        return render_template("output.html",prediction=round(predict[0],2))
    
    

if __name__=="__main__":
    app.run(debug=True)