from django import forms
from .models import Activity
from exercise.models import Exercise

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['gender', 'age_group', 'exercise_duration', 'calories_per_minute']
        # 'exercise_id' gerekli değil çünkü exercise_id, Activity modelinin bir alanı değil, form üzerinde tanımladığınız özel bir ChoiceField 

    gender = forms.ChoiceField(choices=Activity.ACTIVITY_CHOICES, widget=forms.RadioSelect)
    age_group = forms.ChoiceField(choices=Activity.AGE_CHOICES, widget=forms.RadioSelect)
    exercise_id = forms.ChoiceField(
        choices=[],  # Egzersiz seçenekleri `__init__` içerisinde doldurulacak
        label="Exercise",
    )

    exercise_duration = forms.IntegerField(
        label="Exercise Duration (minute)",  
        min_value=1,  
        required=True  
    )

    calories_per_minute = forms.IntegerField(
        required=False,  # Başlangıçta kullanıcı tarafından girilmesine gerek yok
        widget=forms.HiddenInput() # Görünmez hale getirilir
    )


    def __init__(self, *args, **kwargs):
        default_exercises = kwargs.pop('default_exercises', []) # kwargs (Key Value Arguments): 'name = enes' şeklinde alır [] olursa zorunlu, () olursa zorunlu değil  
        custom_exercises = kwargs.pop('custom_exercises', []) # args: 'enes' şeklinde alır, değerin null olmadığından eminsek [] kullanılabilir yoksa hata verir
        super().__init__(*args, **kwargs)

        # Egzersiz seçeneklerini doldurur
        exercises = [(exercise.id, exercise.title) for exercise in default_exercises]
        exercises += [(exercise.id, exercise.title) for exercise in custom_exercises]
        self.fields['exercise_id'].choices = exercises


    def set_calories_per_minute(self, exercise_id):
        try:
            exercise = Exercise.objects.get(id=exercise_id)
            self.instance.calories_per_minute = exercise.cals_per_minute
            self.instance.exercise = exercise
        except Exercise.DoesNotExist:
            self.instance.calories_per_minute = 0
