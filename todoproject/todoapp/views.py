from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .forms import taskform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class taskdetailview(DetailView):
    model = task
    template_name = 'detail1.html'
    context_object_name = 'task1'

class taskupdateview(UpdateView):
    model = task
    template_name = 'update1.html'
    context_object_name = 'task1'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


class taskdeleteview(DetailView):
    model = task
    template_name = 'delete1.html'
    success_url = reverse_lazy('cbvhome')


class tasklistview(ListView):
    model=task
    template_name = 'home.html'
    context_object_name = 'task1'


# Create your views here.
def home(request):
    task1=task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        date=request.POST.get('date','')
        priority=request.POST.get('priority','')
        Task=task(name=name,priority=priority,date=date)
        Task.save()
    return render(request,'home.html',{'task1':task1})
#
# def detail(request):
#
#     return render(request,'detail.html',{)

def delete(request,taskid):
    task1=task.objects.get(id=taskid)
    if request.method=='POST':
        task1.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task1=task.objects.get(id=id)
    fm=taskform(request.POST or None,instance=task1)
    if fm.is_valid():
        fm.save()
        return redirect('/')
    return render(request,'update.html', {'fm':fm,'task1':task1})
