from django.shortcuts import render
from . import forms, models
import json
from django.http import HttpResponse

# Create your views here.
def ftree(request):

    pd = models.Ftree_Hierarchy.objects.values('key','name','title','pic','parent')
    for d in list(pd):
        if d['parent'] == None:
            d.pop('parent')

    people_data = json.dumps(list(pd))
    context = {
        "people_data":people_data,
    }
    return render(request, 'ftree/ftree.html', context)

def addPerson(request):

    if request.POST:
        if not request.POST.get("parent"):
            p = None
        else:
            p = request.POST.get("parent")
        m = models.Ftree_Hierarchy(
            key = request.POST.get("key"),
            name = request.POST.get("name"),
            title = request.POST.get("title"),
            pic = request.POST.get("pic"),
            parent = p
        )
        m.save()

    add_person_form = forms.AddPerson()
    context = {
        "add_person_form": add_person_form
    }
    return render(request, "ftree/add_person.html", context)

def saveData(request):
    print("Run: ftree:saveData")

    data = json.loads(request.body.decode("utf-8"))['nodeDataArray']
    print(data)

    # m = models.Ftree_Hierarchy.all().delete()
    for d in data:
        if 'parent' not in d:
            d.parent = None
        


    return HttpResponse(request.body)