from django.http import HttpResponse


def home(request):
    return HttpResponse('''
                        <h1>Home</h1>
                        <a href = "/courses/">courses</a>
                        <a href = "/contact/">contact</a>
                        <a href = "/about/">about</a>
                        <a href = "/feedback/">feedback</a>
                        ''')
