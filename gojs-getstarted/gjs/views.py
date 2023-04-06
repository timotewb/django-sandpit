from django.shortcuts import render

def example01(request):
    context=dict()
    return render(request=request, template_name="example01.html", context=context)