from django.shortcuts import render

# Create your views here.
def indexPageView(request, context):
    context = {}
    return render(request, "index.html")
