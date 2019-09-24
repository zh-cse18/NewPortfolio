from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from PortfolioApp.models import HeroArea, MyDetail, Education, Experience, Contact, Mywork, TechnicalSkill, WorkSumarry, \
    MyActivity


def index(request):
    # form = ContactForm(request.POST or None)
    # if request.method == 'POST':
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.save()
    #         return redirect('index')
    #
    # else:
    #     form = ContactForm()

    if request.method == "POST":
         post = Contact()
         post.name = request.POST.get('name')
         post.email = request.POST.get('email')
         post.sub = request.POST.get('subject')
         post.message = request.POST.get('message')
         if post.message and post.name and post.email and post.sub:
              post.save()
              if post:
                  return redirect('index')
              else:
                  return HttpResponse('Sending Fail.Try Again')

    context = {
          'post': get_object_or_404(HeroArea),
          'details': get_object_or_404(MyDetail),
          'education': Education.objects.all(),
          'experience': Experience.objects.all(),
          'mywork': Mywork.objects.all(),
          'technical_skill': TechnicalSkill.objects.all(),
          'work': get_object_or_404(WorkSumarry),
          'my_activity': MyActivity.objects.all(),


     }
    return render(request, 'index.html', context)


# def contact_info(request):
#     if request.method == "POST":
#          post = Contact()
#          post.name = request.POST.get('name')
#          post.email = request.POST.get('email')
#          post.subject = request.POST.get('sub')
#          post.message = request.POST.get('message')
#          if post.message and post.name and post.email and post.subject:
#              post.save()
#              if post:
#                  return redirect('form')
#
#     return render(request, 'index.html')
    # return render(request, 'form.html')

#
# def contact_info(request):
#     form = ContactForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         return redirect('index')
#     else:
#        form = ContactForm()
#
#     return render(request, 'index.html', {'form': form})

# def contact_info(request):
#
#
#         name = request.POST.get['name']
#         email = request.POST.get['email']
#         subject = request.POST.get['sub']
#         message = request.POST.get['message']
#
#         context= {
#             'form': name
#         }
#
#         return render(request, 'form.html',context)


def contact(request):
    name = 'Zahid Hassan'
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('index')

    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form, 'name': name})