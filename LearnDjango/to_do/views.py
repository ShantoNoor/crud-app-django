from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList
from .forms import TodoForm

# Create your views here.
def to_do_list_view(request):
    return render(request, 'todo_list.html', {
        'todo_list': TodoList.objects.all()
    })

def to_do_create_view(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            TodoList.objects.create(
                title=form.cleaned_data.get('title'),
                status=form.cleaned_data.get('status')
            )
            return redirect('to_do:to_do_list')

    return render(request, 'todo_create.html', {'form': form})

def to_do_update_view(request, pk):
    obj = get_object_or_404(TodoList, id=pk)
    form = TodoForm(instance=obj)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            for key in form.cleaned_data.keys():
                if key == 'title' and obj.title != form.cleaned_data['title']:
                    obj.title = form.cleaned_data['title']
                if key == 'status' and obj.status != form.cleaned_data['status']:
                    obj.status = form.cleaned_data['status']
            
            obj.save()
            return redirect('to_do:to_do_list')

    return render(request, 'todo_update.html', {'form':form})

def to_do_delete_view(request, pk):
    obj = get_object_or_404(TodoList, id=pk)
    
    render(request, 'todo_delete.html', {
        'title': obj.title
    })

    obj.delete()
    return redirect('to_do:to_do_list')
