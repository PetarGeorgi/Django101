from django.shortcuts import render


def index(req):

    context = {
        'name' : 'Doncho'
    }

    return render(req, 'index.html', context)
