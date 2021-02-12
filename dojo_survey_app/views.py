from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, "index.html")


def survey(request):
    print("Got survey information....................")
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']

    return redirect("/result")

def success(request):

    return render(request, "result.html")



