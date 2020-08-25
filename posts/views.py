from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import models
from functools import wraps
import datetime
import pytz


def home(request):
    return render(request, "home.html")


def create(request):
    if request.method == "POST":
        faceModel = models.Face()
        faceModel.eyeHeight = request.POST["eyeHeight"]
        faceModel.eyeWidth = request.POST["eyeWidth"]
        faceModel.happiness = request.POST["happiness"]
        faceModel.smileWidth = request.POST["smileWidth"]
        faceModel.published = datetime.datetime.now(tz=pytz.utc)
        faceModel.title = request.POST["title"]
        faceModel.save()

    return render(request, "create.html")


def browse(request):
    return render(request, "browse.html")


def paginator(*options):
    def paginator_decorator(func):
        @wraps(func)
        def wrapper(request, page):
            querySet = models.Face.objects.order_by(*options)

            # Make queries unique
            _set = []
            for item in querySet:
                if item not in _set:
                    _set.append(item)

            list = Paginator(_set, 3).page(page)
            max_page = Paginator(_set, 3).num_pages
            return render(request, (func.__name__[6:] + ".html").lower(), context={
                "max_page": max_page,
                "page": page,
                "list": list
            })

        return wrapper

    return paginator_decorator


@paginator("-comments", "-published")
def browseHot(request, page):
    pass


@paginator("-comments")
def browseTop(request, page):
    pass


@paginator("-published")
def browseRecent(request, page):
    pass


def detail(request, pk):
    face = get_object_or_404(models.Face, pk=pk)

    if request.method == "POST":
        comment = models.Comment()
        comment.face = face
        comment.content = request.POST["content"]
        comment.save()
        return HttpResponseRedirect(reverse("posts:detail", kwargs={  # Form Re-Submission Should NOT Happen
            "pk": pk
        }))

    return render(request, "detail.html", context={
        "face": face
    })
