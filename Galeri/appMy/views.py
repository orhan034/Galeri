from django.shortcuts import render, redirect
from .models import *
from appUser.models import *
# Create your views here.

def index(request):
    ctagorys = Category.objects.all()
    photos = Photo.objects.all().order_by('?')[:12]

    contact = {
        'ctagorys':ctagorys,
        'photos':photos,
    }
    return render(request, 'index.html', contact)

def gallerySingle(request,id):
    ctagorys = Category.objects.all()
    photo = Photo.objects.get(id = id)
    comments = Comment.objects.filter(photo =photo) 
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        comment = Comment(title=title,text=text, photo=photo, user = request.user)
        comment.save()
        return redirect('gallerySingle', id)
    contact = {
        'ctagorys':ctagorys,
        'photo':photo,
        'comments':comments,
    }
    return render(request, 'gallery-single.html', contact)

def contact(request):
    ctagorys = Category.objects.all()
    user = User.objects.get(username = request.user)
    profils = Profil.objects.get(user = user)
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        text = request.POST['text']
        contact = Contact(name = name, email = email,
                          subject = subject,text = text, user = request.user)
        contact.save()
        return render('contact')
        
    contact = {
        'ctagorys':ctagorys,
        'profils':profils,
    }
    return render(request, 'contact.html', contact)


def gallery(request,id):
    ctagorys = Category.objects.all()
    catagorys = Category.objects.get(id = id)
    photocategory = Photo.objects.filter(category = id)
    contact = {
        'catagorys':catagorys,
        'photocategory':photocategory,
        'ctagorys':ctagorys,
    }
    return render(request, 'gallery.html', contact)

def sampleInnerPage(request):
    ctagorys = Category.objects.all()
    contact = {
        'ctagorys':ctagorys,
    }
    return render(request, 'sample-inner-page.html', contact)

def services(request):
    ctagorys = Category.objects.all()
    contact = {
        'ctagorys':ctagorys,
    }
    return render(request, 'services.html', contact)