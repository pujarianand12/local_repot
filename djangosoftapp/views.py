from django.shortcuts import render
def home(request):
    return render(request,'inh_home.html')
def contact(request):
    return render(request,'inh_contact.html')
def services(request):
    return render(request,'inh_services.html')
def gallery(request):
    return render(request,'inh_gallery.html')