from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.http import HttpResponse
from pets.models import Author, Post
from .forms import AddPostViaModel
from datetime import datetime

def pets(request):
    all = Post.objects.all()
    viewed_post = request.session.get('viewed_posts', {})
    return render(request, 'pets.html', {'posts': all, 'viewed_posts': viewed_post})

def cats(request):
    all = Post.objects.filter(pet_type='c')
    viewed_posts = request.session.get('viewed_posts', {})
    return render(request, 'cats.html', {'posts': all, 'viewed_posts': viewed_posts})

def dogs(request):
    all = Post.objects.filter(pet_type='d')
    viewed_posts = request.session.get('viewed_posts', {})
    return render(request, 'dogs.html', {'posts': all, 'viewed_posts': viewed_posts})

def post(request, id):
    try:
        post = Post.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse('<h1>There is no post with this id</h1>')

    viewed_posts = request.session.get('viewed_posts', {})
    viewed_posts[id] = id
    request.session['viewed_posts'] = viewed_posts
    return render(request, 'post.html', {'post': post})

def add_post(request):
    if request.method == 'POST':
        form = AddPostViaModel(request.POST, request.FILES)

        if form.is_valid():
            post_ent = Post()
            post_ent.pet_type = form.cleaned_data['pet_type']
            post_ent.title = form.cleaned_data['title']
            post_ent.content = form.cleaned_data['content']
            post_ent.breed = form.cleaned_data['breed']
            post_ent.contact_person = form.cleaned_data.get('contact_person')
            post_ent.tel = form.cleaned_data['tel']
            post_ent.locality = form.cleaned_data['locality']
            post_ent.price = form.cleaned_data['price']
            post_ent.image = form.cleaned_data['image']

            post_ent.issued = datetime.now()
            post_ent.author = Author.objects.get(email = request.user.email)

            post_ent.save()
            return redirect('pets')
    else:
        form = AddPostViaModel()
    return render(request, 'add_post.html', {'form': form})

def my_posts(request):
    all = Post.objects.filter(author = Author.objects.get(email=request.user.email))
    viewed_posts = request.session.get('viewed_posts', {})
    return render(request, 'my_posts.html', {'posts': all, 'viewed_posts': viewed_posts})

