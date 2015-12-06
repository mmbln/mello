# member/views
# -*- coding: utf-8 -*-



import sys, os, re, shutil
from PIL import Image
from stat import *

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings

from .forms import MemberForm
from .models import Member


#----------------------------------------------------------------
# utils
#----------------------------------------------------------------

def generate_password():
    # TODO use random generator
    return ('123')

def store_new_image(user_id, image_file):
    images_dir = os.path.join(os.path.dirname(__file__), 'images')
    # delete old file
    img_list = os.listdir(images_dir)
    pattern = re.compile("^%d_.*" % user_id)
    for f in img_list:
        if pattern.match(f):
            os.remove(os.path.join(images_dir, f))
    # make a new filename
    new_file_name = "%d_%s" % (user_id, os.path.basename(image_file))
    shutil.move(image_file, os.path.join(image_dir, new_file_name))
    
#----------------------------------------------------------------
# views
#----------------------------------------------------------------

def view_member_list(request):
    members = Member.objects.all()
    return render(request, 'member_list.html', {'members': members})

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            # All data entered correctly, save the data
            temp_password = generate_password()
            login_name = form.cleaned_data['login_name']
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            member_img = form.cleaned_data['member_img']
            
            if form.cleaned_data['admin']:
                user = Member.objects.create_superuser(email=email,
                                                login_name=login_name,
                                                password=temp_password,
                                                full_name=full_name)
            else:
                user = Member.objects.create_user(email=email,
                                           login_name=login_name,
                                           password=temp_password,
                                           full_name=full_name)
            # store the image
            path_of_new_image = os.path.join(settings.MEDIA_ROOT, member_img)
            store_new_image(user.id, path_of_new_image)
            
            # TODO send email to user
            return HttpResponseRedirect(reverse('member_list'))
        else:
            # Show form with errors
            pass
    else:
        form = MemberForm()
    
    return render(request, 'member_new.html', {'form': form})

def edit_member(request):
    form = MemberForm()
    return render(request, 'member_new.html')

def show_img(request,id):
    # TODO check if allowed to access the pictures
    images_dir = os.path.join(os.path.dirname(__file__), 'images')
    default_picture = os.path.join(os.path.dirname(__file__), '0_.png')
    try:
        if int(id) == 0:
            f = open(default_picture,"rb")
            response = HttpResponse(f.read(), content_type="image/png")
        else:
            pattern = re.compile("^%s_.*" % id)
            # if file not found fallback to default
            file_path = default_picture

            # search the image directory
            file_list = os.listdir(images_dir)
            for f in file_list:
                if pattern.match(f):
                    file_path = os.path.join(images_dir, f)
                    break
            #
            picture = Image.open(file_path).resize((150,150))
            response = HttpResponse(content_type="image/png")
            picture.save(response, "PNG")
            
    except:
        picture = Image.new("RGB", (150,150), "red")
        response = HttpResponse(content_type="image/png")
        picture.save(response, "PNG")
        
    return response
