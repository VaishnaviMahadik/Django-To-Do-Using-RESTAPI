from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from django import forms

# Create your views here.
def index(request):
	task = Task.objects.all()
	form = TaskForm()
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'task':task,'form':form}
	return render(request,'task/index.html',context)

def update(request,pk):
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST,instance=task)
		if form.is_valid():
			form.save()
			return redirect('index')

	context = {'form':form}
	return render(request,'task/update.html',context)


def delete(request,pk):
	task = Task.objects.get(id=pk)
	if request.method == 'POST':
		task.delete()
		return redirect('index')
	context = {'task':task}
	return render(request,'task/delete.html',context)