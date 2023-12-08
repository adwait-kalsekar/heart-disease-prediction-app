from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import pandas as pd

from .data_preprocessing import preprocessing
from .models import Info, Prediction

# Create your views here.

def index(request):
    return render(request, "ml_classifier/home.html")

@csrf_exempt
def predict(request):
    hosted_url = "https://5325-128-6-37-144.ngrok-free.app/predict"
    context = { "hosted_url": hosted_url }
    if request.method == 'POST':
        try:
            pred_obj = Prediction()

            # Get JSON request
            data = request.POST.dict()

            pred_obj.name = data['name']

            del data['csrfmiddlewaretoken']
            del data['name']

            # Load model data
            model, col_names = preprocessing.load_model_data()

            # Convert JSON to Pandas DF
            df = pd.DataFrame(data, index=[0])
            df.reindex(columns=col_names)

            # Clean and encode data according to the model
            encoded_df = preprocessing.encode_data(df)

            # Predict Results
            prediction = list(model.predict(encoded_df))
            probability = list(model.predict_proba(encoded_df))
            
            final_prediction = '{0:.2f}'.format(probability[0][prediction[0]] * 100)

            pred_obj.age = data["age"]
            pred_obj.gender = "Female" if data["sex"] == "0" else "Male"
            pred_obj.prediction = "No" if prediction[0] == 0 else "Yes"
            pred_obj.probability = final_prediction

            pred_obj.save()
            

            print(prediction, probability[0][prediction[0]])

            context["prediction"] = f"has a {final_prediction}% probability of not having a Heart Disease" if prediction[0] == 0 else f"has a {final_prediction}% probability of having a Heart Disease"
            #context["prediction"] = f"has a {probability[0][prediction[0]]}% probability of a Heart Disease"
            context["data"] = data
        
        except Exception as err:
            print("Error", err)

    return render(request, "ml_classifier/predict.html", context)

def view_project(request):
    return render(request, "ml_classifier/project.html")

def view_eda(request):
    context = {}
    try:
        info = Info.objects.filter(category="eda")
        context = {"info": info}
    except Exception as err:
        print("Error", err)
    return render(request, "ml_classifier/results.html", context)

def view_results(request):
    context = {}
    try:
        info = Info.objects.filter(category="ml")
        context = {"info": info}
    except Exception as err:
        print("Error", err)
    return render(request, "ml_classifier/results.html", context)

def view_eval(request):
    context = {}
    try:
        info = Info.objects.filter(category="eval")
        context = {"info": info}
    except Exception as err:
        print("Error", err)
    return render(request, "ml_classifier/eval.html", context)

def view_table(request):
    context = {}
    try:
        predictions = Prediction.objects.all()
        context = { "predictions": predictions }
    except Exception as err:
        print(err)
    return render(request, "ml_classifier/table.html", context)

def view_data_dictionary(request):
    return render(request, "ml_classifier/data_dictionary.html")

def view_team(request):
    return render(request, "ml_classifier/team.html")