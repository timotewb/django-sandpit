from django.shortcuts import render

def index(request):
    context=dict()
    return render(request=request, template_name="index.html", context=context)

def example01(request):
    context=dict()
    return render(request=request, template_name="example01.html", context=context)

def example02(request):
    context=dict()
    return render(request=request, template_name="example02.html", context=context)

def example03(request):
    context=dict()
    return render(request=request, template_name="example03.html", context=context)

def kindsofmodels(request):
    context=dict()
    return render(request=request, template_name="kindsofmodels.html", context=context)