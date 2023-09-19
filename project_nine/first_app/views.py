from django.shortcuts import render

# Create your views here.


def home(request):
    response = render(request, "home.html")
    response.set_cookie("name", "Rahim")
    return response


def get_cookie(request):
    name = request.COOKIES.get("name")
    print(request.COOKIES)
    return render(request, "home.html", {'name': name})


def set_session(request):
    data = {
        "name": "Rahim",
        "age": 23,
        "language": "Bangla"
    }
    request.session.update(data)
    return render(request, "home.html")
    