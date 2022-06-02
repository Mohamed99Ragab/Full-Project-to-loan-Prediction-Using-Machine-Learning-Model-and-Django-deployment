from random import choices
from secrets import choice
from django import forms

Gender =(
    ("Male", "Male"),
    ("Female", "Female"),
)

Married =(
    ("Yes", "Yes"),
    ("No", "No"),
)

Dependents =(
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
)
Education =(
    ("Graduate", "Graduate"),
    ("Not Graduate", "Not Graduate"),
)

Self_Employed =(
    ("Yes", "Yes"),
    ("No", "No"),
)

Credit_History =(
    (0, 0),
    (1, 1),
)

Property_Area =(
    ("Rural", "Rural"),
    ("Semiurban", "Semiurban"),
    ("Urban","Urban")
)

class LoanForm(forms.Form):
    gender = forms.ChoiceField(choices=Gender)
    married = forms.ChoiceField(choices=Married)
    dependents = forms.ChoiceField(choices=Dependents)
    education = forms.ChoiceField(choices=Education)
    self_employed = forms.ChoiceField(choices=Self_Employed)
    applicantincome = forms.DecimalField()
    coapplicantincome = forms.DecimalField()
    loanamount = forms.DecimalField()
    loan_amount_term = forms.DecimalField()
    credit_history = forms.ChoiceField(choices=Credit_History)
    property_area = forms.ChoiceField(choices=Property_Area)
