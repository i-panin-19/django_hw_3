from django.core.management import BaseCommand

from shop.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = [
            {'name': 'Рыба', 'description': 'Замороженная, соленая'},
            {'name': 'Мясо', 'description': 'Замороженное, свежее'},
            {'name': 'Газировка', 'description': 'Минеральная, сладкие напитки'}
        ]

        category_for_create = list()
        for item in category_list:
            category_for_create.append(
                Category(**item)
            )

        Category.objects.bulk_create(category_for_create)
