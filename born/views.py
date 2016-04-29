from django.shortcuts import render
from django.shortcuts import render_to_response

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return render_to_response('index.html')
