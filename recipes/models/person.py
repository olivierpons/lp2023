from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    social_networks = models.ManyToManyField(
        "SocialNetwork", related_name="persons",
        through="PersonSocialNetwork"
    )
    # template
    # {% for p_r_s in user.person.social_networks.all %}
    #   {{ p_r_s.social_network }} : {{ p_r_s.account }}
    # {% endif %}

class Phone(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    no_tel = models.CharField(max_length=200, default=None, blank=True, null=True)


class SocialNetwork(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True, null=True)
    # template SocialNetworkDetail
    # {% for p_r_s in object.persons.all %}
    #   {{ p_r_s.person }}
    # {% endif %}


class PersonSocialNetwork(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    social_network = models.ForeignKey(SocialNetwork, on_delete=models.CASCADE)
    account = models.CharField(max_length=200, default=None, blank=True, null=True)


# https://docs.djangoproject.com/en/4.1/topics/signals/
@receiver(post_save, sender=User)
def my_post_save_user_handler(sender, instance, created, **kwargs):
    if created:  # a User = physical -> create the associated person:
        Person.objects.create(user=instance)
