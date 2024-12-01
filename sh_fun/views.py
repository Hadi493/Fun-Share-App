from django.shortcuts import render
from .models import Fun
from .forms import FunForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def all_fun(request):
    return render(request, 'all_fun.html')


def fun_list(request):
    funs = Fun.objects.all().order_by('-created_at')
    return render(request, 'fun_list.html', {'funs': funs})

def create_fun(request):
    if request.method == 'POST':
        form = FunForm(request.POST, request.FILES)
        if form.is_valid():
            fun = form.save(commit=False)
            fun.user = request.user
            fun.save()
            return redirect('fun_list')
    else:
        form = FunForm()
    return render(request, 'create_fun.html', {'form': form})

def fun_edit(request, fun_id):
    fun = get_object_or_404(Fun, pk=fun_id, user = request.user)
    if request.method == 'POST':
        form = FunForm(request.POST, request.FILES, instance=fun)
        if form.is_valid():
            fun = form.save(commit=False)
            fun.user = request.user
            fun.save()
            return redirect('fun_list')
    else:
        form = FunForm(instance=fun)
    return render(request, 'create_fun.html', {'form': form})

def fun_detail(request, fun_id):
    fun = get_object_or_404(Fun, pk=fun_id)
    return render(request, 'fun_detail.html', {'fun': fun})

def fun_delete(request, fun_id):
    fun = get_object_or_404(Fun, pk=fun_id, user = request.user)
    if request.method == 'POST':
        fun.delete()
        return redirect('fun_list')
    return render(request, 'fun_delete.html', {'fun': fun})