from django import forms

class BMICalculatorForm(forms.Form):
    height = forms.FloatField(label='Height (cm)', min_value=0.1)
    weight = forms.FloatField(label='Weight (kg)', min_value=1)

class BMRForm(forms.Form):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    ACTIVITY_LEVELS = [
        (1.2, 'Sedentary (Little to no exercise/sports)'),
        (1.375, 'Lightly active (Light exercise/sports 1-3 days/week)'),
        (1.55, 'Moderately active (Moderate exercise/sports 3-5 days/week)'),
        (1.725, 'Very active (Hard exercise/sports 6-7 days/week)'),
        (1.9, 'Extra active (Very hard exercise or a physical job)'),
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Gender")
    weight = forms.FloatField(label="Weight (kg)")
    height = forms.FloatField(label="Height (cm)")
    age = forms.IntegerField(label="Age")
    activity_level = forms.ChoiceField(
        choices=ACTIVITY_LEVELS, 
        label="Activity Level",
        widget=forms.Select()
    )