from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from backend_test.models import ActivityPeriod, User
from random import randrange, randint, choice
import names
import pytz
import string

class Command(BaseCommand):
    help = 'Creates Data'

    def random_date(self, start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)
    
    def random_activity_periods(self):
        num_activities = randint(1,10)
        activities = []

        start_date = datetime.strptime('1/1/2010', '%m/%d/%Y')
        end_date = datetime.now()

        for _ in range(num_activities):
            start_time = self.random_date(start_date, end_date)
            end_time = self.random_date(start_time, end_date)

            period = {
                'start_time' : start_time, 
                'end_time' : end_time
            }

            activity = ActivityPeriod(**period)
            activity.save()
            activities.append(activity)

        activities.sort(key = lambda x: x.start_time)
        return activities

    def get_random_id(self):
        letters_and_digits = string.ascii_uppercase + string.digits
        result_str = ''.join((choice(letters_and_digits) for i in range(10)))
        return result_str

    def populate_db(self):
        activities = self.random_activity_periods()

        user = {
            'id': self.get_random_id(),
            'real_name': names.get_full_name(),
            'tz': pytz.all_timezones[randint(0, 591)],
        }
        
        users = User(**user)
        users.save()
        users.activity_periods.add(*activities)

    def handle(self, *args, **options):
        data = randint(6,12)
        for _ in range(data):
            self.populate_db()
        
        self.stdout.write(self.style.SUCCESS('Data created successfully.'))