from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect


from .models import Bunk, User

# Create your views here.
    
def main_bunk_feed(request):
    bunks = Bunk.objects.all().order_by('-pub_date')
    
    return render(request, 'bunk/main_feed.html', {
        'bunks': bunks
    })
    
def personal_bunk_feed(request, id):
    user = User.objects.get(id=id)

    bunk_list = list(Bunk.objects.filter((Q(pub_date__lte=timezone.now())), (Q(from_user_id=id) | Q(to_user_id=id))).order_by('-pub_date'))

    incoming_bunk_list = [bunk for bunk in bunk_list if bunk.to_user == user]
    
    outgoing_bunk_list = [bunk for bunk in bunk_list if bunk.from_user == user]
    
    allusers = User.objects.exclude(id=id)

    print(len(allusers))
    return render(request, 'bunk/personal_feed.html', {
        'user': user,
        'incoming_bunk_list': incoming_bunk_list,
        'outgoing_bunk_list': outgoing_bunk_list,
        'allusers': allusers,
    })

def user_list(request):
    print("Hello World!")
    users = User.objects.all().order_by('-pub_date')
    return render(request, 'bunk/users.html', {
        'users': users
    })

def submit_bunk(request):
    from_id = request.POST['from_user']
    to_id = request.POST['to_user']
    
    print(from_id, to_id)

    new_bunk = Bunk.objects.create(from_user=User.objects.get(id=from_id), to_user=User.objects.get(id=to_id))

    new_bunk.save()

    return HttpResponseRedirect(f'/bunk/{from_id}/bunkfeed')

def create_user(request):
    username = request.POST['username']
    photo = request.POST['photo']

    user = User.objects.create(username=username, photo=photo)
    user.save()

    return HttpResponseRedirect(f'/bunk/users')


