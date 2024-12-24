from django.shortcuts import render
from .forms import BMICalculatorForm, BMRForm

# Create your views here.

def health_calculator(request):
    bmi = None # Default değerler
    bmr = None
    tdee = None
    result_message = None

    bmi_form = BMICalculatorForm() # Formları gösteriyorum
    bmr_form = BMRForm()

    if request.method == 'POST':
        # BMI Formu Gönderildiyse
        if 'bmi_submit' in request.POST:
            bmi_form = BMICalculatorForm(request.POST)
            if bmi_form.is_valid():
                height = bmi_form.cleaned_data['height'] / 100 # Form verileri kullanıcıdan alındığında, Django bu verileri kontrol eder (Boş olup olmadığını, doğru türde olup olmadığını vsvs)
                weight = bmi_form.cleaned_data['weight'] # Doğrulama işlemleri başarılı olduktan sonra cleaned_data içinde saklar
                bmi = weight / (height ** 2)
                bmi = round(bmi, 2) # BMI'yi virgülden sonra 2 basamakla sınırlandır
                if bmi < 18.5:
                    result_message = "You are underweight."
                elif 18.5 <= bmi <= 24.9:
                    result_message = "Your weight is normal."
                elif 25 <= bmi <= 29.9:
                    result_message = "You are overweight."
                else:
                    result_message = "You are obese."

        # BMR Formu Gönderildiyse
        elif 'bmr_submit' in request.POST:
            bmr_form = BMRForm(request.POST)
            if bmr_form.is_valid():
                gender = bmr_form.cleaned_data['gender']
                weight = bmr_form.cleaned_data['weight']
                height = bmr_form.cleaned_data['height']
                age = bmr_form.cleaned_data['age']
                activity_level = float(bmr_form.cleaned_data['activity_level'])

                if gender == 'male':
                    bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
                elif gender == 'female':
                    bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

                bmr = round(bmr, 2)  # BMR'yi virgülden sonra 2 basamakla sınırlandır
                tdee = bmr * activity_level
                tdee = round(tdee, 2)  # TDEE'yi virgülden sonra 2 basamakla sınırlandır

    context = {
        'bmi_form': bmi_form,
        'bmr_form': bmr_form,
        'bmi': bmi,
        'result_message': result_message,
        'bmr': bmr,
        'tdee': tdee,
    }
    return render(request, 'bmi/health_calculator.html', context)