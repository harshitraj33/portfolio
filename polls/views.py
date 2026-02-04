# from django.shortcuts import render
# from django.template import loader
# from django.http import HttpResponse
# from .models import users

# # def index(request):
# #     myusers = users.objects.all().values()
# #     template = loader.get_template('user_list.html')
# #     context = {
# #         'myusers' : myusers,
# #     }
# #     return HttpResponse(template,render(context, request))



from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index page.")
