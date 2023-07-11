from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

app = Flask(__name__) #entry point



# template_path = 'C:/Users/ritti/OneDrive/Desktop/MLOps/templates'
# app = Flask(__name__, template_folder=template_path)

##Route for a home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods = ['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':            #user will give input in the data fields
        return render_template('home.html')
    else: # POST Request
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")
        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        print(results)
        return render_template('home.html',res=results[0])
        
if __name__=="__main__":
    app.run(debug=True)        
