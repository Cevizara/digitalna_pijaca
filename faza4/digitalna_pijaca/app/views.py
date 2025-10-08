from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Mesto, Korisnik

# Create your views here.
def pocetna(request):
    mesta = Mesto.objects.all()
    context = {
        'mesta': mesta,
        'korisnik': request.user
    }
    return render(request, 'index.html', context)


def prijava(request):
    if request.method == "POST":
        email = request.POST.get("email")
        sifra = request.POST.get("sifra")
        
        user = authenticate(request, username=email, password=sifra)  # Koristimo email kao username
        if user is not None:
            login(request, user)
            return redirect("pocetna")  # ili neki drugi URL
        else:
            messages.error(request, "Pogrešan email ili lozinka.")
    
    return render(request, "prijava.html")


def registracija(request):
    if request.method == "POST":
        email = request.POST.get("email")
        sifra = request.POST.get("sifra")
        ime = request.POST.get("ime")
        uloga = request.POST.get("uloga", "kupac")  # default je kupac

        if Korisnik.objects.filter(email=email).exists():
            messages.error(request, "Email već postoji.")
        else:
            user = Korisnik.objects.create_user(
                email=email,
                sifra=sifra,
                ime=ime,
                uloga=uloga
            )
            login(request, user)
            return redirect("pocetna")
    
    return render(request, "registracija.html")

def odjava(request):
    logout(request)
    return redirect('pocetna')