from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from register.models import User


def item_infor(request):
    return render(request, 'item_infor.html')


def index(request):
    return render(request, '../static/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password)
        if user:
            return JsonResponse({'res': 1})
        else:
            return JsonResponse({'res': 0})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_again = request.POST.get('again_password')
        user = User.objects.filter(username=username)
        if not user and password == password_again:
            User.objects.create(username=username, password=password)
            return JsonResponse({'res': 1})
        elif not user and password_again != password:
            return JsonResponse({'res': -1})
        else:
            return JsonResponse({'res': 0})


def forget_pwd(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_again = request.POST.get('again_password')
        user = User.objects.filter(username=username)
        if user and password == password_again:
            User.objects.filter(username=username).update(password=password)
            return JsonResponse({'res': 1})
        elif user and password_again != password:
            return JsonResponse({'res': -1})
        else:
            return JsonResponse({'res': 0})
