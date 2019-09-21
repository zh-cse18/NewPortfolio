from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from PortfolioApp.models import HeroArea, MyDetail, Education, Experience


def index(request):
    context = {
          'post': get_object_or_404(HeroArea),
          'details': get_object_or_404(MyDetail),
          'education': Education.objects.all(),
          'experience': Experience.objects.all()
     }
    return render(request, 'index.html', context)


def contact_info(request):
    if request.method == 'POST':
        name = request.POST.get['name']
        email = request.POST.get['email']
        subject = request.POST.get['sub']
        message = request.POST.get['message']


