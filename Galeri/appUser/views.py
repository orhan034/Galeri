from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from appMy.models import *
# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        harfet = False
        for harf in username:
            if harf == '@':
                harfet = True
        if username[-4:] == '.com' and harfet:
            try:
                user = User.objects.get(email = username)
                username = user.username
            except:
                messages.warning(request, 'E-posta adresi bulunamıyor!')
                return redirect('loginUser')
            
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'Kullanıcı adı veya şifre hatalı!')
            return redirect('loginUser')
    return render(request, 'user/login.html')

def registerUser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        harfup = False
        harfnum = False
        if password1 == password2:
            for harf in password1:
                if harf.isupper():
                    harfup = True
                if harf.isnumeric():
                    harfnum = True
            if harfup and harfnum and len(password1)>=6:
                if not User.objects.filter(username=username).exists():
                    if not User.objects.filter(email=email).exists():
                        user = User.objects.create_user(first_name= name,
                                                            last_name = surname, email=email,
                                                            username=username,password=password1)
                        user.save()

                        userprofils = Profil(user=user)
                        userprofils.save()

                        return redirect('loginUser')
                    else:
                        messages.warning(request, 'Bu email zaten kullanılıyor!')
                        return redirect('registerUser')          
                else:
                    messages.warning(request, 'Bu kullanıcı adı alınmış!')
                    return redirect('registerUser')  
            else:
                messages.warning(request, 'Şifreler en az 6 karakter olmalı!')
                messages.warning(request, 'Şifreler en az bir büyük harf içermeli!')
                messages.warning(request, 'Şifreler rakam içermeli!')
                return redirect('registerUser')               
        else:
            messages.warning(request, 'Şifreler aynı değils!')
            return redirect('registerUser')            
    return render(request, 'user/register.html')

def logoutUser(request):
    logout(request)
    return redirect('index')

def profil(request):
    ctagorys = Category.objects.all()
    user = User.objects.get(username = request.user)
    profils = Profil.objects.get(user = user)
    photo = Photo.objects.all()
    if request.method == 'POST':
        if request.POST.get('formbutton') == 'sifreChange':
            password = request.POST.get('password')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            user = User.objects.get(username = request.user)

            if user.check_password(password):
                if password1==password2:
                    user.set_password(password1)
                    user.save()
                    return redirect('loginUser')
                else:
                    messages.warning(request, 'Şifreler aynı değil!')
            else:
                messages.warning(request, 'Kullanımda olan şifreniz yanlış!')

        if request.POST.get('formbutton')== 'profilChange':
            birthday = request.POST.get('birthday')
            age = request.POST.get('age')
            website = request.POST.get('website')
            degree = request.POST.get('degree')
            email = request.POST.get('email')
            address = request.POST.get('address')
            job = request.POST.get('job')
            phone = request.POST.get('phone')
            text = request.POST.get('text')
            
            image = request.FILES.get('image')
            if image is None:
                image = profils.image
            profils.birthday = birthday
            profils.age = age
            profils.phone = phone
            profils.website = website
            profils.degree = degree
            profils.email = email
            profils.city = address
            profils.job = job
            profils.text = text
            profils.image = image

            profils.save()
            user.save()
            return redirect('profil')
        if request.POST.get('formbutton')== 'photoChange':
            category = request.POST.get('category')
            title = request.POST.get('title')
            text = request.POST.get('text')
            image = request.FILES.get('image')
            photos = Photo(category=category,title=title,tetx = text,
                        image=image, user = request.user)
            photos.save()
                
            
    contact = {
        'ctagorys':ctagorys,
        'profils':profils,
        'photo':photo,
        
    }
    return render(request, 'user/profil.html', contact)

