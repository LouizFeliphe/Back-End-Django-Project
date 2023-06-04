from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList


# Create your views here.


def index(response):
   if not response.user.is_authenticated:
        message = "Você precisa estar logado para acessar a página 'VIEW'"
        return render(response,"main/list.html",{"message":message})

   else:
        item = Item.objects.filter(todolist__user=response.user)
        return render(response, "main/list.html",{"query":item})
        """if response.method == "POST":
       if response.POST.get("save") == "save":
           for item in query.item_set.all():
               print(response.POST.get("c" + str(item.id)))
               if response.POST.get("c" + str(item.id)) == "clicked":
                   print("hello")
                   item.complete = True
                   item.save()
               else:
                   item.complete = False
                   item.save()
    if response.POST.get("add") == "add":
        print("hello")
        txt = response.POST.get("new")
        if len(txt) > 2:
            query.item_set.create(text=txt,complete=False)"""


                
       


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist_set.create(name=n)
        return redirect("/lista")
    else:
        form = CreateNewList()
    return render(response,"main/create.html", {"form": form})

def ola(response):
    return render(response,"main/ola.html",{"response":response})  
 
def k(response):
    if not response.user.is_authenticated:
        message = "Você precisa estar logado para acessar a página 'Create'"
        return render(response,"main/k.html",{"message":message})
    if response.method == "POST":
        name = response.user.todolist_set.create(name=response.POST.get("name"))
        item = name.item_set.create(text=response.POST.get("itemName"),complete=False)
        return redirect("/lista")
    else:
        return render(response,"main/k.html",{})



