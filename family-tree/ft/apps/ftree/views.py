from django.shortcuts import render

# Create your views here.
def ftree(request):
    return render(request=request, template_name='main/ftree.html')