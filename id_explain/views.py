from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        "header_selection_index": 1,
    }
    return render(request, "id_explain/home.html", context)
