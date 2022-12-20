from email.message import EmailMessage
from django.shortcuts import render, redirect
from .forms import FormContact
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    form_contact = FormContact()
    
    if request.method == "POST":
        form_contact = FormContact(data=request.POST)
        
        if form_contact.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            contact = request.POST.get("contact")
            
            email = EmailMessage(
                "Mensaje desde la App de contacto",
                "El usuario: {} con dirección: {} que manda el siguiente mensaje:\n\n {}".format(name, email, contact),
                "",["gatitoproflama@gmail.com"], reply_to=[email]
                )
            
            try:
                email.send()

                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?invalid")

            
    return render(request, "contact/contact.html", {'form_contact':form_contact})

