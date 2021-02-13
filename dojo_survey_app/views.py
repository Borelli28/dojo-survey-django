from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, "index.html")


# def survey(request):
#     name_form = request.POST['name']
#     email_form = request.POST['email']
#     location_form = request.POST['location']
#     favorite_lang_form = request.POST['favorite_language']
#     comments_form = request.POST['comment']

#     context = {
#         "name": name_form,
#         "email": email_form,
#         "location": location_form,
#         "favorite_lang": favorite_lang_form,
#         "comments": comments_form
#     }
#     print(context)

#     return redirect("/result", context)

def success(request):
    name_form = request.POST['name']
    email_form = request.POST['email']
    location_form = request.POST['location']
    favorite_lang_form = request.POST['favorite_language']
    comments_form = request.POST['comment']

    context = {
        "name": name_form,
        "email": email_form,
        "location": location_form,
        "favorite_lang": favorite_lang_form,
        "comments": comments_form
    }

    print(context)

    return render(request, "result.html", context)
