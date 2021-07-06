from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = []

class users():
    def __init__(self, name):
        self.list = []
    

    

def filter(s):
    p = "'name': ['"
    p2 = "']}>"
    begin = s.find(p) + len(p)
    finish = s.find(p2)
    return(s[begin:finish])
def filter2(s):
    p = "'task': ['"
    p2 = "']}>"
    begin = s.find(p) + len(p)
    finish = s.find(p2)
    return(s[begin:finish])

def filter3(s):
    p = "'nbr': ['"
    p2 = "']}>"
    begin = s.find(p) + len(p)
    finish = s.find(p2)
    return(s[begin:finish])


def home(request):
    return render(request, "homepage/home.html")

def about(request):
    return render(request, "homepage/about.html")

class todo:

    def delete(request):

        if len(tasks) == 0:
            return render(request, "homepage/todo.html",{
            "task1": filter3(str(request.POST)),
            "tasks": tasks,
            })
        else:

            taskNbr = int(filter3(str(request.POST)))
            tasks.pop(taskNbr)

            return render(request, "homepage/todo.html",{
                 "task1": filter3(str(request.POST)),
                 "tasks": tasks,
            
             })

    def todo1(request):


        if request.method == 'POST':
         
            tasks.append(filter2(str(request.POST)))

            return render(request, "homepage/todo.html",{
                "task1": filter2(str(request.POST)),
                "tasks": tasks,
                
           
        })
        else:
            return render(request, "homepage/todo.html", {
                "task1": filter2(str(request.POST)),
                "tasks": tasks,
                
        
        })


def account(request):
    if request.method == 'POST':
        
        
    
       return render(request, "homepage/account.html",{
            "Name": filter(str(request.POST)), 
            "status": 1,
           
        })
    else:
        return render(request, "homepage/account.html", {
            "status":0,
        
        })


def add(request):

    return render(request, "homepage/add.html")

