import json
from django.core.management.base import BaseCommand
from models import Ingredient  # замените на своё


class Command(BaseCommand):
    help = 'Load ingredients from JSON file'

    def handle(self, *args, **kwargs):
        with open('backend/data/ingredients.json', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                Ingredient.objects.get_or_create(
                    name=item['name'],
                    measurement_unit=item['measurement_unit']
                )
        self.stdout.write(self.style.SUCCESS(
            'Successfully loaded ingredients')
        )
