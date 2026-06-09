from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Organisation, Membership


@receiver(post_save, sender=Organisation)
def create_owner_membership(sender, instance, created, **kwargs):
    if created and instance.owner:
        Membership.objects.create(
            user=instance.owner,
            organisation=instance,
            role=Membership.Role.ADMIN
        )