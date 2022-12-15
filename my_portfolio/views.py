from django.shortcuts import render
from my_portfolio.models import Home, About, Work, Contact


def home(request):
    print(dir(request))
    home_obj = Home.objects.all().first()
    data_set = []
    data_obj = home_obj.section.all()
    for i in data_obj:
        data_set.append(i.data_words)

    context = {
        "home_data": home_obj,
        "data_set": data_set,
    }

    return render(request, 'main/index.html', context)


def about(request):
    img = Home.objects.all().first().showcase_image
    abouts = About.objects.all().first()
    context = {
        "img": img,
        "about": abouts
    }
    return render(request, 'main/about.html', context)


def work(request):
    img = Home.objects.all().first().showcase_image
    work = Work.objects.all()
    context = {
        "img": img,
        "work": work,
    }
    return render(request, 'main/work.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        Contact.objects.create(name=name, email=email, subject=subject, phone=phone, message=message)
        
    img = Home.objects.all().first().showcase_image
    context = {
        "img": img,
        "work": work,
    }
    return render(request, 'main/contact.html', context)
