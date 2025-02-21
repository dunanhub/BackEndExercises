from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm

def home(request):
    return redirect('todo_lists')

def todo_lists(request):
    lists = TodoList.objects.all()
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_lists')
    else:
        form = TodoListForm()
    return render(request, 'todoss/todo_lists.html', {'lists': lists, 'form': form})

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', id=id)
    else:
        form = TodoForm(initial={'todo_list': todo_list})
    return render(request, 'todoss/todo_list_detail.html', {'todo_list': todo_list, 'form': form})

def delete_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect('todo_lists')

def edit_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', id=id)
    else:
        form = TodoListForm(instance=todo_list)
    return render(request, 'todoss/edit_todo_list.html', {'form': form})

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect('todo_list_detail', id=todo_list_id)

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', id=todo.todo_list.id)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todoss/edit_todo.html', {'form': form})