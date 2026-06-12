from django.db import models
from django_countries.fields import CountryField
from django.conf import settings

class OrganisationQuerySet(models.QuerySet):

    def for_user(self, user):
        return self.filter(membership__user=user)

# name, logo, owner, country
class Organisation(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(blank=True, null=True)
    # using the django defined user from django conf. Also sets owner to null when the user is deleted. (later logic; change the owner)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    # using the django_countries app that is installed
    country = CountryField(blank_label="(Select country)") 

    # for finding users that are members
    objects = OrganisationQuerySet.as_manager()
    
    def __str__(self):
        return self.name
    
class Membership(models.Model):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        MEMBER = "member", "Member"
        VIEWER = "viewer", "Viewer"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.MEMBER
    )

    def __str__(self):
        return f"{self.user} - {self.organisation} ({self.role})"