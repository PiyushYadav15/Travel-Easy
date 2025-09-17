
# Create your views here.
from django.shortcuts import render,get_object_or_404, redirect
from .models import Destination,Category
from django.contrib.auth.decorators import login_required
from .forms import DestinationForm,CategoryForm
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.contrib import messages
# from django.contrib.auth import login

def home(request):
    return render(request,'home.html')

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('category_list')
        
    else:
        form = CategoryForm()
    return render(request,'create_category.html',{'form':form})

def category_list(request):
    data=Category.objects.all()
    return render(request,'category_list.html',{'data':data})

def photo_create(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form=DestinationForm()
    return render(request,'photo_create.html',{'form':form})
@login_required
def photo_list(request):
    cid= request.GET.get('category_id')
    data=Category.objects.all()
    if cid:
        data1=Destination.objects.filter(category_id=cid)
    else:
        data1=Destination.objects.all()
    return render (request,'photo_list.html',{'data':data,'data1':data1})

def photo_detail(request, pk):
    photo = get_object_or_404(Destination, pk=pk)
    guides = photo.guides.all()  # related_name='guides'
    return render(request, 'photo_detail.html', {'photo': photo, 'guides': guides})

def photo_update(request,pid):
    photo=get_object_or_404(Destination,id=pid)
    if request.method=='POST':
        form=DestinationForm(request.POST,request.FILES,instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form=DestinationForm(instance=photo)
    return render(request,'photo_update.html',{'form':form}) 

def photo_delete(request,pid):
    photo=get_object_or_404(Destination,id=pid)
    if request.method=='POST':
        photo.is_deleted=True
        photo.deleted_at=timezone.now()
        photo.save()
        return redirect('photo_list')
    return render(request,'photo_delete.html',{'photo':photo})

def photo_history(request):
    data=Destination.objects.filter(is_deleted=True)
    return render(request,'photo_history.html',{'data':data})

def restore(request,pid):
    data=get_object_or_404(Destination,id=pid,is_deleted=True)
    if request.method=='POST':
        data.is_deleted=False
        data.deleted_at=None
        data.save()

        return redirect ('photo_history')
    return render(request,'restore.html',{'data':data})

def permanent(request, pid):
    data = get_object_or_404(Destination, id=pid)
    if request.method == 'POST':
        data.delete()  # Permanently delete the photo from the database
        return redirect('photo_list')
    
    return render(request, 'permanent.html',{'data': data})






