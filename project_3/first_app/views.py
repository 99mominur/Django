from django.shortcuts import render

# Create your views here.


def contact(request):
    return render(request, "./first_app/index.html", {"courses" :[
        {
            "id" : 1,
            "c_name" :"c", 
            "t_name" :"Rahim"
        },
        {
            "id" : 2,
            "c_name" :"c++", 
            "t_name" :"Kahim"
        },
        {
            "id" : 3,
            "c_name" :"python", 
            "t_name" :"Fahim"
        },
    ]
    })
