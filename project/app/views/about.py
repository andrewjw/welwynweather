from datetime import date

from django.shortcuts import render_to_response

def about(req):
    return render_to_response("html/about.html", { "today": date.today() })
