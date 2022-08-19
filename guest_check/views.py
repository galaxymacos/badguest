from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        "header_selection_index": 0,
    }
    return render(request, "guest_check/home.html", context)
