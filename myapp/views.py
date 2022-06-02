from django.shortcuts import render
from .forms import LoanForm
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import pickle


def prediction(request):
    predicted = 'here is prediction'
    df = ''
    form = LoanForm()
    if request.method == 'POST':
        form = LoanForm(request.POST)

        if form.is_valid():
                cd = form.cleaned_data
                gender = cd['gender']
                married = cd['married']
                dependents = cd['dependents']
                education = cd['education']
                self_employed = cd['self_employed']
                applicantincome = cd['applicantincome']
                coapplicantincome = cd['coapplicantincome']
                loanamount = cd['loanamount']
                loan_amount_term = cd['loan_amount_term']
                credit_history = cd['credit_history']
                property_area = cd['property_area']

                df = pd.DataFrame({
                    'gender':gender,
                    'married':married,
                    'dependents':dependents,
                    'education':education,
                    'self_employed':self_employed,
                    'applicantincome':applicantincome,
                    'coapplicantincome':coapplicantincome,
                    'loanamount':loanamount,
                    'loan_amount_term':loan_amount_term,
                    'credit_history':credit_history,
                    'property_area':property_area,
             },index=[0])

                    # Label Encoding
                encoding = LabelEncoder()
                df.gender = encoding.fit_transform(df.gender)
                df.married = encoding.fit_transform(df.married)
                df.education = encoding.fit_transform(df.education)
                df.self_employed = encoding.fit_transform(df.self_employed)
                df.property_area = encoding.fit_transform(df.property_area)
                

                # # Data Scaling
                df = MinMaxScaler().fit_transform(df)

                #load the model Random Forest
                loaded_model = pickle.load(open('E:\Projects_django\TheProject_env\loan_prediction\model_RF.pkl', 'rb'))
                predicted = loaded_model.predict(df)
                



    return render(request,'index.html',{
        'inputform':form,
        'predict':predicted,
        
    })


