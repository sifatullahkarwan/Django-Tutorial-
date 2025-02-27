# Signals are used to perform any action on modification of a model instance.
# The signals are utilities that help us to connect events with actions.\

# type of signal
# pre_save/post_save: This signal works before/after the method save().
# pre_delete/post_delete: This signal works before after deleting a model’s instance (method delete()) this signal is thrown.
# pre_init/post_init: This signal is thrown before/after instantiating a model (__init__() method).


# Note :This signal cod is use When a new User instance is created, it automatically creates a corresponding Profile instance (create_profile function) and saves it (save_profile function).
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver#A decorator for connecting receivers to signals. 
from . models import Profile

@receiver(post_save,sender = User)# when user save then send this signal by reciever 
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

#receiver – The function who receives the signal and does something.
# sender – Sends the signal
# created — Checks whether the model is created or not
# instance — created model instance
# **kwargs –wildcard keyword arguments

@receiver(post_save,sender = User)
def save_profile(sender, instance,**kwargs):
    instance.profile.save()
    # Another way to connect the signal with the function:
    #  connect the signals file with the app.py file ready function in order to use them. 