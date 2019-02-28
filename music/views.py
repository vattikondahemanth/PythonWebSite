from django.http import HttpResponse


def index(self):
    return HttpResponse("<h1>This is music index page</h1><button value='fff' text='dssd'>dsf</button>?")


