from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "first_app/home.html", context={"name": "Mominur Rahman", "age": 23, "marks": 89,
                                                           "courses": [
                                                               {
                                                                   "id": 1,
                                                                   "c_name": "c",
                                                                   "t_name": "Rahim"
                                                               },
                                                               {
                                                                   "id": 2,
                                                                   "c_name": "c++",
                                                                   "t_name": "Kahim"
                                                               },
                                                               {
                                                                   "id": 3,
                                                                   "c_name": "python",
                                                                   "t_name": "Fahim"
                                                               },
                                                           ]})


def about(request):
    return render(request, "first_app/about.html")
