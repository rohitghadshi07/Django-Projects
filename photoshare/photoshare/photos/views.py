from django.shortcuts import render, redirect

# Create your views here.
from .models import Category, Photo


def gallery(request):
    category = request.GET.get('category')
    print('category:',category)
    
    deleted_photo = request.GET.get('deleted')
    print(deleted_photo)
    
    Photo.objects.filter(id=deleted_photo).delete()
     
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)    
    
    categories = Category.objects.all()

    context = { 'categories':categories, 'photos': photos }
    return render(request,'photos/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id = pk)
    context = {'photo':photo}
    return render(request,'photos/photo.html', context)

def addPhoto(request):
    categories = Category.objects.all()
    
    if request.method == 'POST':
        data = request.POST
        print(data)
        image = request.FILES.get('image')
        print(image)
        
        if data['category'] != 'none':
            category = Category.objects.get(id= data['category'])
        elif data['category_new'] != '':
            category = Category.objects.get_or_create(name=data['category_new'])[0]
        else:
            category = None
        
        Photo.objects.create(
            category = category,
            description = data['description'],
            image = image
        )
        
        return redirect('gallery')
    
    context = { 'categories':categories }
    return render(request,'photos/add.html', context)