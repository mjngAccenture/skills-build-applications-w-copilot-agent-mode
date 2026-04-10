from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Workout


class Command(BaseCommand):
    help = "Populate the octofit_db database with safe test data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Clearing existing data...")

        # Borrado en orden defensivo
        try:
            Workout.objects.all().delete()
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"Could not clear Workout data: {e}"))

        try:
            Team.objects.all().delete()
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"Could not clear Team data: {e}"))

        try:
            User.objects.all().delete()
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"Could not clear User data: {e}"))

        self.stdout.write("Creating safe seed data...")

        # Create teams
        marvel = Team.objects.create(name="Marvel")
        dc = Team.objects.create(name="DC")

        # Create users
        ironman = User.objects.create_user(
            username="ironman",
            email="ironman@marvel.com",
            password="password",
        )
        captainamerica = User.objects.create_user(
            username="captainamerica",
            email="cap@marvel.com",
            password="password",
        )
        batman = User.objects.create_user(
            username="batman",
            email="batman@dc.com",
            password="password",
        )
        superman = User.objects.create_user(
            username="superman",
            email="superman@dc.com",
            password="password",
        )

        # Create workouts
        Workout.objects.create(
            name="Super Strength",
            description="Strength workout for heroes",
        )
        Workout.objects.create(
            name="Stealth Moves",
            description="Agility workout for heroes",
        )

        # Avisos explícitos: se omiten relaciones complejas por compatibilidad con Djongo
        self.stdout.write(
            self.style.WARNING(
                "Skipped Team.members ManyToMany population due to Djongo/MongoDB ObjectId compatibility limitations."
            )
        )
        self.stdout.write(
            self.style.WARNING(
                "Skipped Activity seed data due to ForeignKey/ObjectId compatibility limitations."
            )
        )
        self.stdout.write(
            self.style.WARNING(
                "Skipped Leaderboard seed data due to ForeignKey/ObjectId compatibility limitations."
            )
        )
        self.stdout.write(
            self.style.WARNING(
                "Skipped Workout.suggested_for ManyToMany population due to Djongo/MongoDB ObjectId compatibility limitations."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Database populated successfully with safe base data: teams, users, and workouts."
            )
        )