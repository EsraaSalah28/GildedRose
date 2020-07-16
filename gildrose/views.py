from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from gildrose.forms import ItemForm
from gildrose.models import Item


##Index View (Home Page)
#Route '/' (localhost:8000)
def index(request):
    return render(request,'index.html')


##Create View
#Route '/create' (as per urls.py)
#If: this view is called with "POST" request then the form is validated
#and saved to database, and then redirected to route '/show'.
#Else: it will render the contact form in index.html and display it.
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


##Show View
#Route '/show'
#Retrieve all contacts data from database and send it to 'show.html' to be rendered.
def show(request):
    itemData = Item.objects.all()
    return render(request,"show.html",{'itemData':itemData })