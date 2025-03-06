from django.http import Http404
from urllib.request import Request
from django.shortcuts import render
from markdown2 import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request : Request, title):
    content = util.get_entry(title)
    if(content is None):
        raise Http404("La pagina buscada no existe")
    else:
        return render(request,"encyclopedia/entry.html", {
            "title": title,
            "content" : markdown(content)
        })