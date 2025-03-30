from django.shortcuts import render, redirect
from django.views import View
from jarvishchef.forms import RecipeForm
from jarvishchef.langchain import ask_jarvish_chef

# Create your views here.


class Home(View):
    def get(self, request):
        ai_recipe = request.session.get("ai_recipe", "")
        form = RecipeForm()
        return render(
            request, "jarvishchef/home.html", {"form": form, "ai_recipe": ai_recipe}
        )

    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe_message = form.cleaned_data["recipe_message"]
            # print(recipe_message)
            ai_res_recipe = ask_jarvish_chef(recipe_message)
            request.session["ai_recipe"] = ai_res_recipe
        form = RecipeForm()
        return redirect("/")
