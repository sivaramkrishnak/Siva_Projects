from django.core.management.base import BaseCommand
from core.models import Team, User, Activity, Workout, Leaderboard
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write(self.style.WARNING('Deleting old data...'))
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()
            Workout.objects.all().delete()

            self.stdout.write(self.style.SUCCESS('Creating teams...'))
            marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
            dc = Team.objects.create(name='DC', description='DC superheroes')

            self.stdout.write(self.style.SUCCESS('Creating users...'))
            users = [
                User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
                User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
                User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
                User.objects.create(name='Superman', email='superman@dc.com', team=dc),
                User.objects.create(name='Batman', email='batman@dc.com', team=dc),
                User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            ]

            self.stdout.write(self.style.SUCCESS('Creating workouts...'))
            workouts = [
                Workout.objects.create(name='Strength Training', description='Full body strength', suggested_for='Marvel'),
                Workout.objects.create(name='Cardio Blast', description='High intensity cardio', suggested_for='DC'),
            ]

            self.stdout.write(self.style.SUCCESS('Creating activities...'))
            Activity.objects.create(user=users[0], activity_type='Running', duration_minutes=30, calories_burned=300, date='2026-02-01')
            Activity.objects.create(user=users[1], activity_type='Cycling', duration_minutes=45, calories_burned=400, date='2026-02-02')
            Activity.objects.create(user=users[3], activity_type='Swimming', duration_minutes=60, calories_burned=500, date='2026-02-03')
            Activity.objects.create(user=users[4], activity_type='Yoga', duration_minutes=40, calories_burned=200, date='2026-02-04')

            self.stdout.write(self.style.SUCCESS('Creating leaderboards...'))
            Leaderboard.objects.create(team=marvel, total_points=700, week=1)
            Leaderboard.objects.create(team=dc, total_points=800, week=1)

            self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
