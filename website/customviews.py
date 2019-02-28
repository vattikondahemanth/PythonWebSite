from django.shortcuts import redirect


def redirect_view(self):
    response = redirect('/admin/')
    return response

#-----------------------------