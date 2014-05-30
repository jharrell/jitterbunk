from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.utils import timezone

from bunks.models import Bunk, UserProfile, BunkForm


def index(request):
    latest_bunk_list = Bunk.objects.order_by('-time')[:10]
    userProfiles = UserProfile.objects.all()
    context = {'latest_bunk_list': latest_bunk_list,
               'userProfiles': userProfiles}
    return render(request, 'bunks/index.html', context)


def bunk(request):
    """ When someone is bunked, this code runs """
    if request.method == 'POST':
        form = BunkForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['usernames']
            karel = User.objects.get(username="karel")
            to_user = User.objects.get(username=username)
            newBunk = Bunk(from_user=karel,
                           to_user=to_user,
                           time=timezone.now())
            newBunk.save()
            return HttpResponseRedirect('/bunks/')
    else:
        """ displays normal bunk page """
        form = BunkForm()
        userProfiles = UserProfile.objects.all()
        context = {'userProfiles': userProfiles, 'form': form}
        return render(request, 'bunks/bunk.html', context)


def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    bunkList = []
    for b in Bunk.objects.all():
        if b.from_user == user or b.to_user == user:
            bunkList.append(b)
    context = {'user': user, 'bunkList': bunkList}
    return render(request,
                  'bunks/detail.html',
                  context
                  )
