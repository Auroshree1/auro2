from django.shortcuts import render

# Create your views here.
def auro2(request):
    d={'name':'auro','age':23}
    return render(request,'auro2.html',d)
