from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from gildrose.forms import ItemForm
from gildrose.models import Item
from gildrose import qualityChecker


def index(request):
    return render(request,'index.html')


def create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ItemForm()
    return render(request,'create.html',{'form':form})


def show(request):
    if request.method == 'GET':
        itemData = Item.objects.all()
    return render(request, "show.html", {'itemData': itemData })

def update(request):
    itemData = Item.objects.all()
    form = ItemForm(request.POST)
    for item in itemData:
        if item.itemType == 'AgedBrie':
            qualityChecker.AgedBrie(item.name, item.sellIn, item.qaulityValue).update_quality()
        elif item.itemType == "Sulfuras":
            qualityChecker.Sulfuras(item.name, item.sellIn, item.qaulityValue).update_quality()
        elif item.itemType == "Backstage":
            qualityChecker.Backstage(item.name, item.sellIn, item.qaulityValue).update_quality()
        elif item.itemType == "Conjured":
            qualityChecker.Conjured(item.name, item.sellIn, item.qaulityValue).update_quality()
        else:
            qualityChecker.RegularItem(item.name, item.sellIn, item.qaulityValue).update_quality()
    if form.is_valid():
        form.save()


