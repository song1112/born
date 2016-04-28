from django.shortcuts import render
from django.shortcuts import render_to_response

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    return render_to_response('login.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        account = request.POST['account']
        password = request.POST['']
        password = request.POST['']
