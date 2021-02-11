import random
from random_timestamp import random_timestamp
from django.core.management import BaseCommand
from activity.models import CHOICE_TZ, Profile, ActivityPeriod


class Command(BaseCommand):
    help = "This is custom commands"

    def handle(self, *args, **option):
        for i in range(10):
            l = ['Allah', 'Nadeem', 'Kaleem', 'Ansari', 'hello1', 'MoNadeem', 'MOKaleem', 'AnasAnsari', 'Aslam1221',
                 'sahil11', 'Rihan232', 'Mumtaz', 'Emtiyaz', 'faiyyaz', 'Nafees', 'Aasif Bhai', 'Arshad Bhai',
                 'Ayaz', 'Pradeep', 'Monish', 'Rajeev', ]
            profile = Profile(
                real_name=random.choice(l),
                tz=CHOICE_TZ[i],
            )
            profile.save()
            for j in range(2):
                activity = ActivityPeriod(
                    profile=profile,
                    start_time=random_timestamp(),
                    end_time=random_timestamp(),

                )
                activity.save()
        self.stdout.write(self.style.SUCCESS("Added Success !"))
