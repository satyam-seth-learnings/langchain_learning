from django.shortcuts import render, redirect
from django.views import View
from jarvishchef.forms import RecipeForm

# Create your views here.


class Home(View):
    def get(self, request):
        form = RecipeForm()
        return render(request, "jarvishchef/home.html", {"form": form})

    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe_message = form.cleaned_data["recipe_message"]
            print(recipe_message)
        form = RecipeForm()
        return redirect("/")
