from django.db import models
from django import forms
from django.contrib.auth.models import User


# Create your models here.
class Bunk(models.Model):
    """ Bunk model, contains 2 users and time bunked """
    from_user = models.ForeignKey(User, related_name='from_user')
    to_user = models.ForeignKey(User, related_name='to_user')
    time = models.DateTimeField('time bunked')

    def __unicode__(self):
        return "%s bunked %s" % (self.from_user.username,
                                 self.to_user.username)


class UserProfile(models.Model):
    """ UserProfile contains a django auth User objects and an image """
    user = models.OneToOneField(User)
    photo = models.ImageField(upload_to='/static/img',
                              default='/static/img/None/img.jpeg'
                              )

    def __unicode__(self):
        return self.user.username


class BunkForm(forms.Form):
    """
    When someone is bunked,
    you use a BunkForm containing all users possible

    """
    usernames = forms.ChoiceField(choices=[(userProfile.user.username,
    	userProfile.user.username) for userProfile in UserProfile.objects.all() if not userProfile.user.username == "karel"])