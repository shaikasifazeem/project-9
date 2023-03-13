from django.shortcuts import render
def ninja2(request):
    d={'mob1':9398867596,'mob2':9346552091,'mob3':9704754533,'mob4':8886424126,'mob5':9000419578,'mob6':9182238069,'mob7':6303407458,'mob8':6363822719}
    return render(request,'ninja.html',context=d)
# Create your views here.
