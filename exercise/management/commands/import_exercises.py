import json
from django.core.management.base import BaseCommand
from exercise.models import Exercise
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Imports exercises from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **kwargs):
        json_file_path = kwargs['json_file']

        # Open the JSON file and read the data
        try:
            with open(json_file_path, 'r') as file: # read file
                data = json.load(file)

            for item in data:
                user = None  # Varsayılan olarak user=None
                if item.get('user'):  # Eğer 'user' varsa, kullanıcıyı bulmaya çalış
                    try:
                        user = User.objects.get(username=item['user'])
                    except ObjectDoesNotExist:
                        self.stdout.write(self.style.ERROR(f"User {item['user']} not found"))
                        continue

                # Create Exercise object
                try:
                    exercise = Exercise(
                        user=user,
                        title=item['title'], # kwargs (Key Value Arguments): 'name = enes' şeklinde alır [] olursa zorunlu, () olursa zorunlu değil  
                        description=item['description'], # args: 'enes' şeklinde alır, değerin null olmadığından eminsek [] kullanılabilir yoksa hata verir
                        cals_per_minute=item.get('cals_per_minute', 0.0), # Varsayılan olarak 0.0 
                        image=item.get('image', 'images/no_image.png'), # Default image if none provided
                        is_default=item['is_default']
                    )
                    exercise.save()
                    self.stdout.write(self.style.SUCCESS(f"Successfully imported exercise: {exercise.title}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Failed to save exercise: {item['title']}. Error: {e}"))
        
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found: {json_file_path}"))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR(f"Error decoding JSON in file: {json_file_path}"))