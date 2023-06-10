from django.shortcuts import render

# Create your views here.
def infoTableView(request):
    return render(request, "infotable/table.html")


