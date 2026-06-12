from django.db import models

from accounts.models import Organisation  # or "accounts.Organisation" if you prefer string reference


class Project(models.Model):

    class Status(models.TextChoices):
        PLANNING = "planning", "Planning"
        ACTIVE = "active", "Active"
        COMPLETED = "completed", "Completed"

    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    name = models.CharField(max_length=200)
    description = models.TextField()

    start_date = models.DateField()
    end_date = models.DateField()

    budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    amount_spent = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PLANNING
    )

    def __str__(self):
        return self.name


class Cohort(models.Model):

    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name