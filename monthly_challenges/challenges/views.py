from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


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
    "december": "brother in law's birthday",
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenge.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challange", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    respons_data = f"<ul>{list_items}</ul>"
    return HttpResponse(respons_data)


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
        return HttpResponseNotFound("This month not supported")
