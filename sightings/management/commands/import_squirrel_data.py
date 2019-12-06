import csv
from django.core.management import BaseCommand
from sightings.models  import show
class Command(BaseCommand):
    help = 'Import Data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        import datetime
        path = kwargs['path']
        with open(path) as f:
            reader = csv.reader(f)
            next(reader)
            for item in reader:
                for i in (15,16,17,18,19,21,22,23,24,25,26,27,28):
                    if item[i] == 'false':
                        item[i] = False
                    else:
                        item[i] = True

                longitude = item[0]
                latitude = item[1]
                unique_squirrel_id = item[2]
                shift = item[4]
                date = datetime.datetime.strptime(item[5],"%m%d%Y").strftime("%Y-%m-%d")
                age = item[7]
                primary_fur_color = item[8]
                location = item[12]
                specific_location = item[14]
                running = item[15]
                chasing = item[16]
                climbing = item[17]
                eating = item[18]
                foraging = item[19]
                other_activities = item[20]
                kuks = item[21]
                quaas = item[22]
                moans = item[23]
                tail_flags = item[24]
                tail_twitches = item[25]
                approaches = item[26]
                indifferent = item[27]
                run_from = item[28]

                new_show = show(Longitude = longitude, Latitude = latitude,Unique_squirrel_id = unique_squirrel_id, Shift = shift, Date = date, Age = age,
                                Primary_fur_color = primary_fur_color, Location = location, Specific_location = specific_location,
                                Running = running, Chasing = chasing, Climbing = climbing, Eating = eating, Foraging = foraging,
                                Other_activities = other_activities, Kuks = kuks, Quaas=quaas, Moans=moans, Tail_flags = tail_flags, 
                                Tail_twitches = tail_twitches, Approaches = approaches, Indifferent = indifferent, Runs_from = run_from)

                new_show.save()
