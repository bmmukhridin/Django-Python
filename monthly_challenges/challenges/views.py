from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string


monthly_challenge = {
    "january": "Mehran birthday!",
    "february": "Free Month!",
    "march": "Mironshoh birthday",
    "april": "Dad's birthday",
    "may": "momth's birthday",
    "june": "my birthday",
    "july": "brother and Safina's birthday",
    "avgust": "Jon's birthday",
    "september": "max's birthday",
    "october": "Mansur brother birthday",
    "november": "my wife's birthday",
    "december": None,
}

# Create your views here.


def index(request):
    months = list(monthly_challenge.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_number_challenges_by_number(request, month):
    try:
        forword_month = list(monthly_challenge.keys())
        if month > len(forword_month):
            return HttpResponseNotFound("Invalid month!")
        return HttpResponse(forword_month[month])
    except:
        return HttpResponseNotFound("This month not supported")


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
        raise Http404("404.html")
        # data_resposne = render_to_string("404.html")
        # return HttpResponseNotFound(data_resposne)
