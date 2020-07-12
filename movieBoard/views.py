from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from movieBoard.forms import movieForm, reviewForm
from movieBoard.models import movie, review


# Create your views here.

def index(request):


    return render(request, 'movieBoard/index.html')



def list(request):
    movies = movie.objects.all()
    paginator = Paginator(movies, 5)

    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'movies': items
    }
    return render(request, 'movieBoard/list.html', context)


def create(request):
    if request.method == 'POST':
        form = movieForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/movieBoard/list/')
    form = movieForm()
    return render(request, 'movieBoard/create.html', {'form': form})

def update(request):
    if request.method == 'POST' and 'id' in request.POST:
        item = get_object_or_404(movie, pk=request.POST.get('id'))
        form = movieForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
    elif 'id' in request.GET:
        item = get_object_or_404(movie, pk=request.GET.get('id'))
        form = movieForm(instance=item)
        return render(request, 'movieBoard/update.html', {'form': form})

    return HttpResponseRedirect('/movieBoard/list/')


def detail(request, id):
    if id is not None:
        item = get_object_or_404(movie, pk=id)
        reviews = review.objects.filter(movie=item).all()
        return render(request, 'movieBoard/detail.html', {'item': item, 'reviews': reviews})

    return HttpResponseRedirect('/movieBoard/list/')


def delete(request):
    if 'id' in request.GET:
        item = get_object_or_404(movie, pk=request.GET.get('id'))
        item.delete()

    return HttpResponseRedirect('/movieBoard/list/')


def review_create(request, movie_id):
    if request.method == 'POST':
        form = reviewForm(request.POST)  #
        if form.is_valid():
            new_item = form.save()
        return redirect('movie-detail', id=movie_id)

    item = get_object_or_404(movie, pk=movie_id)
    form = reviewForm(initial={'movie': item})
    return render(request, 'movieBoard/review_create.html', {'form': form, 'item': item})


def review_delete(request, movie_id, review_id):
    item = get_object_or_404(review, pk=review_id)
    item.delete()

    return redirect('movie-detail', id=movie_id)


