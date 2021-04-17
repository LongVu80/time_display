from django.shortcuts import render
from time import localtime, strftime
    
def index(request):
    context = {
        "date": strftime("%a, %m-%d-%Y and the time is: %I:%M%p", localtime()),
    }
    return render(request,'index.html', context)