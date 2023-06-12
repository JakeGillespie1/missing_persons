from django.shortcuts import render

# Create your views here.
def infoTableView(request, context):
    context = {}
    return render(request, "infotable/table.html")


