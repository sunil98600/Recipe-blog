from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        recipe_image = request.FILES.get('image') 
        recipe_name = request.POST.get('name', 'default')
        recipe_desc = request.POST.get('desc', 'default')

        recipe.objects.create(
            recipe_name=recipe_name,
            recipe_desc=recipe_desc,
            recipe_image=recipe_image
        )

    queryset = recipe.objects.all()
    context = {'recipes': queryset}

    return render(request, 'recipe/index.html', context)