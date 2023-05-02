import csv
from pathlib import Path
from django.core.management.base import BaseCommand
from django.db import models
from store.models.product import Products
from store.models.category import Category


class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('/store/data/Development.csv', type=str)

    def handle(self, *args, **options):
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/store/data/Development.csv', newline='') as f:
            reader = csv.reader(f)
            next(reader) # skip header row
            for row in reader:
                category = Category.objects.create(rating=row[7])
                product = Products.objects.create(title=row[1], price_detail_amount=row[15], category=category, url=row[2])
                self.stdout.write(self.style.SUCCESS(f'Product {product.title} created!'))
        category.categorize() # categorize the categories after importing data

