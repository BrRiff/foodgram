import os
import json
from django.core.management.base import BaseCommand
from django.conf import settings
from recipes.models import Ingredient  # замените на вашу модель


class Command(BaseCommand):
    help = 'Load ingredients from JSON file'

    def handle(self, *args, **kwargs):
        path = os.path.join(
            settings.BASE_DIR, 'data', 'ingredients.json'
        )
        with open(path, encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            Ingredient.objects.create(**item)
            self.stdout.write(self.style.SUCCESS(f"Added {item}"))
