import csv
from django.core.management import BaseCommand
from sightings.models  import show
class Command(BaseCommand):
    help = 'Export Data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
         path = kwargs['path']
         with open(path,'w') as f:
             writer = csv.writer(f)
             head = ['longitude','latitude','unique_squirrel_id',
                     'shift','date','age','primary_fur_color',
                     'location','speicific_location','running',
                     'chasing','climbing','eating','foraging',
                     'other_activities','kuks','quaas',
                     'moans','tail_flags','tail_twitches',
                     'approaches','indifferent','run_from']

             writer.writerow(head)

             Data = show.objects.all()
             
             for item in Data:

                 writer.writerow([item.Longitude,item.Latitude,item.Unique_squirrel_id,
                    item.Shift,item.Date,item.Age,item.Primary_fur_color,item.Location,
                    item.Specific_location,item.Running,item.Chasing,item.Climbing,
                    item.Eating,item.Foraging,item.Other_activities,item.Kuks,
                    item.Quaas,item.Moans,item.Tail_flags,item.Tail_twitches,
                    item.Approaches,item.Indifferent,item.Runs_from])
