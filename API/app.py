from flask import Flask, request, jsonify, abort, render_template
##
import tensorflow as tf
# import keras
# from tensorflow import keras
##
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Dropout, LSTM
##
##
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, LSTM
##
# import tensorflow as tf
# import keras as keras
# #import keras
# import keras.backend as K
# from keras.models import Model, Sequential, load_model
# from keras.layers import Dense, Embedding, Dropout, Input, Concatenate, LSTM
import time
import pickle as pickle
# from sklearn.externals import joblib
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # return '<h1>SEEM LOS API</h1>'
    return render_template("index.html")

@app.route('/model', methods=['GET'])
def model():
    return {
        'Author' : 'Emmanuel',
        'Team' : 'BSE20-25'
    }

@app.route('/forecast', methods=['POST'])
def forecast():
    return {
        'Author' : 'Emmanuel',
        'Team' : 'BSE20-25'
    }


@app.route('/dailyforecast', methods=['POST'])
def dailyforecast():
    # model = pickle.load(open("../Model/encounter_model_LSTM.pkl", "rb"))
    # model = joblib.load('../Model/encounter_model_LSTM.pkl')
    model = load_model('../Model/encounter_model_LSTM.h5')
    # Export Pandas DataFrame to a CSV File
    dailyEncounter = pd.read_csv("../Datasets/Encounter/Cleaned/dailyEncounter.csv")
    #setting index as date
    dailyEncounter['Date'] = pd.to_datetime(dailyEncounter.Date,format='%Y-%m-%d')
    dailyEncounter.index = dailyEncounter['Date']
    dailyEncounter.drop('Date', axis=1, inplace=True)
    #Converting the dataframe to a numpy array
    dataset = dailyEncounter.values
    #Get teh last 60 day closing price 
    last_60_days = dailyEncounter[-60:].values
    #Scale the all of the data to be values between 0 and 1
    scaler = MinMaxScaler(feature_range=(0, 1)) 
    scaled_data = scaler.fit_transform(dataset)
    #Scale the data to be values between 0 and 1
    last_60_days_scaled = scaler.transform(last_60_days)
    #Create an empty list
    X_test = []
    #Append the past 60 days
    X_test.append(last_60_days_scaled)
    #Convert the X_test data set to a numpy array
    X_test = np.array(X_test)
    #Reshape the data
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    #Get the predicted scaled price
    pred_price = model.predict(X_test)
    #undo the scaling 
    pred_price = scaler.inverse_transform(pred_price)
    # # convert numpy array to dictionary
    # prediction = dic = dict(enumerate(pred_price.flatten(), 1))
    # convert numpy array to json
    prediction = pred_price. tolist()
    prediction = json.dumps(prediction)
    return prediction

@app.route('/multidailyforecast', methods=['POST'])
def multidailyforecast():
    days = int(request.json["Days"])
    if (days > 60):
        return {
            "failed" : "More days specified, the model can only accurately forecast upto a maximum of 60 days"
        }
    # model = pickle.load(open("../Model/encounter_model_LSTM.pkl", "rb"))
    # model = joblib.load('../Model/encounter_model_LSTM.pkl')
    model = load_model('../Model/daily_encounter_model_LSTM.h5')
    # Export Pandas DataFrame to a CSV File
    dailyEncounter = pd.read_csv("../Datasets/Encounter/Cleaned/dailyEncounter.csv")
    #setting index as date
    dailyEncounter['Date'] = pd.to_datetime(dailyEncounter.Date,format='%Y-%m-%d')
    dailyEncounter.index = dailyEncounter['Date']
    dailyEncounter.drop('Date', axis=1, inplace=True)
    #Converting the dataframe to a numpy array
    dataset = dailyEncounter.values
    #Scale the all of the data to be values between 0 and 1
    scaler = MinMaxScaler(feature_range=(0, 1)) 
    daily_scaled_data = scaler.fit_transform(dataset)
    # #Get the predicted scaled price
    data_len = len(dataset)
    #Test data set
    loaded_test_data = daily_scaled_data[data_len - days - 60: , : ]
    #Create the x_test and y_test data sets
    x_test = []
    # y_test =  dataset[training_data_len : , : ]
    #Get all of the rows from index 1603 to the rest and all of the columns (in this case it's only column 'Close'), so 2003 - 1603 = 400 rows of data
    for i in range(60,len(loaded_test_data)):
        x_test.append(loaded_test_data[i-60:i,0])
    #Convert x_test to a numpy array 
    x_test = np.array(x_test)
    #Reshape the data into the shape accepted by the LSTM
    x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1],1))
    #Getting the models predicted price values
    pred_price = model.predict(x_test)
    #undo the scaling 
    pred_price = scaler.inverse_transform(pred_price)
    prediction = pred_price. tolist()
    prediction = json.dumps(prediction)
    return prediction

if __name__ == '__main__':
    app.run(debug=True)

# export FLASK_DEBUG = 1
# export FLASK_APP = main.py
# export FLASK_ENV = development
# flask run