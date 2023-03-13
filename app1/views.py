from django.shortcuts import render
def ninja(request):
    di={'school':'zphs'}
    return render(request,'ninja.html',context=di)

