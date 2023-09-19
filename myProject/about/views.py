from django.shortcuts import render

# Create your views here.

def about(request):
    if request.method == "POST":
        select = request.POST.get("select")
        name = request.POST.get("username",)
        email = request.POST.get("email",)
        return render(request, "about/about.html", {"name" : name,
                                                     "email" : email,
                                                     "select": select})
    return render(request, "about/about.html",)
    