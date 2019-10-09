from batting_average.models import Matches
from django.core.management.base import BaseCommand
from django.db import IntegrityError, transaction

class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **kwargs):
        # Since the CSV headers match the model fields,
        # you only need to provide the file's path (or a Python file object)
    
        try:
            insert_count = Matches.objects.from_csv('/home/lokesh/PythonProjects/matches.csv', drop_constraints=False, drop_indexes=False)
            print ("{} records inserted".format(insert_count))
        except IntegrityError:
            print('something went wrong with atomic transaction')