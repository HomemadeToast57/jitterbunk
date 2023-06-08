from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect


from .models import Bunk, User

# Create your views here.
    
def main_bunk_feed(request):
    bunks = Bunk.objects.filter(Bunk.objects.all()).order_by('-pub_date')
    return render(request, 'bunk/main_feed.html', {
        'bunks': bunks
    })
    
def personal_bunk_feed(request, id):
    bunks = Bunk.objects.filter((Q(pub_date__lte=timezone.now())), (Q(from_user_id=id) | Q(to_user_id=id))).order_by('-pub_date')
    
    allusers = User.objects.exclude(id=id)

    print(len(allusers))
    return render(request, 'bunk/personal_feed.html', {
        'user': User.objects.get(id=id),
        'allusers': allusers,
        'bunks': bunks,
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

    Bunk.objects.create(from_user=from_id, to_user=to_id)
    return HttpResponseRedirect(f'/bunk/{from_id}/bunkfeed')

# def personal_bunk_feed(requst, the_params_from_url):
#     # do your query here
#     # you have aceest to request! and the dynamic parts of url
#     return render('template_blah.html', {
#         asdf: 123,
#         asdf1: 123
#     })

