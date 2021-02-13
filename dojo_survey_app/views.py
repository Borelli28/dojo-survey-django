from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, "index.html")


def survey(request):
    # Use session to store POST data in DB, so we can use it even when it redirects to another page
    request.session['name'] = request.POST['name']
    request.session['email'] = request.POST['email']
    request.session['location'] = request.POST['location']
    request.session['favorite_language'] = request.POST['favorite_language']
    request.session['comment'] = request.POST['comment']

    return redirect("/result")


def success(request):

    return render(request, "result.html")
