from flask import Flask , request ,render_template ,jsonify
import pandas as pd 
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

scaler=pickle.load(open('Model/scaler11.pkl','rb'))
model=pickle.load(open('Model/log_reg.pkl','rb'))
application = Flask(__name__)

app=application

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/islegendary", methods=['GET','POST'])

def predict_datapoint():
    if request.method=='POST':
        Total=int(request.form.get("Total"))
        HP = float(request.form.get('HP'))
        Attack = float(request.form.get('Attack'))
        Defense = float(request.form.get('Defense'))
        Sp_Atk = float(request.form.get('Sp_Atk'))
        Sp_Def = float(request.form.get('Sp_Def'))
        Speed = float(request.form.get('Speed'))
        Catch_Rate = float(request.form.get('Catch_Rate'))

        new_data=scaler.transform([[Total,HP,Attack,Defense,Sp_Atk,Sp_Def,Speed,Catch_Rate]])
        predict=model.predict(new_data)
       
        if predict[0] ==1 :
            result = 'LEGENDARY'
        else:
            result ='NON-LEGENDARY'
            
        return render_template('single_prediction.html',result=result)

    else:
        return render_template('home.html')
        
if __name__=="__main__":
    app.run(host="0.0.0.0")
