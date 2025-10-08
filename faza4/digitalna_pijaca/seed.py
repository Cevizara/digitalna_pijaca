import random
from datetime import datetime, timedelta
from app.models import Kategorija, Korisnik, Mesto, Obavestenje, Proizvod, Zahtev

# ---- 1. Kreiraj mesta ----
mesta_nazivi = ["Beograd", "Novi Sad", "Niš", "Kragujevac"]
mesta = [Mesto.objects.create(naziv=naziv) for naziv in mesta_nazivi]

# ---- 2. Kreiraj korisnike ----
korisnici = []

# Kupci
for i in range(3):
    k = Korisnik.objects.create_user(
        email=f"kupac{i}@example.com",
        sifra="123",
        ime=f"Kupac{i}",
        uloga="kupac",
        fk_mesto=random.choice(mesta)
    )
    korisnici.append(k)

# Domaćini
for i in range(2):
    d = Korisnik.objects.create_user(
        email=f"domacin{i}@example.com",
        sifra="123",
        ime=f"Domaćin{i}",
        uloga="domacin",
        telefon=f"06{random.randint(10000000,99999999)}"[:20],  # ograničavanje na max_length
        adresa=f"Adresa domaćina {i}",
        opis=f"Opis domaćina {i}",
        fk_mesto=random.choice(mesta)
    )
    korisnici.append(d)

# Administrator
admin = Korisnik.objects.create_superuser(
    email="admin@example.com",
    sifra="123",
    ime="Administrator",
    uloga="admin",
    telefon="0600000000",
    adresa="Adresa admina",
    opis="Administrator sistema",
    fk_mesto=random.choice(mesta)
)
korisnici.append(admin)

# ---- 3. Kreiraj kategorije ----
kategorije_nazivi = ["Voće", "Povrće", "Mlečni proizvodi", "Meso"]
kategorije = []
for naziv in kategorije_nazivi:
    k = Kategorija.objects.create(
        naziv=naziv,
        vrsta="proizvod",
        putanja_slike=f"/images/{naziv.lower()}.jpg"
    )
    kategorije.append(k)

# ---- 4. Kreiraj proizvode (samo domaćini imaju proizvode) ----
proizvodi = []
for domacin in [k for k in korisnici if k.uloga == "domacin"]:
    for i in range(3):
        p = Proizvod.objects.create(
            naziv=f"{domacin.ime} - Proizvod{i}",
            opis=f"Opis proizvoda {i} domaćina {domacin.ime}",
            putanja_slike=f"/images/{domacin.ime.lower()}_proizvod{i}.jpg",
            nacin_uzgoja=random.choice(["organski", "prskano"]),
            dostupnost=random.randint(0, 1),
            datum_kreiranja=datetime.now() - timedelta(days=random.randint(0, 30)),
            fk_domacin=domacin,
            fk_kategorija=random.choice(kategorije)
        )
        proizvodi.append(p)

# ---- 5. Kreiraj zahteve ----
zahtevi = []
for kupac in [k for k in korisnici if k.uloga == "kupac"]:
    z = Zahtev.objects.create(
        prilozeni_telefon=f"06{random.randint(10000000,99999999)}"[:20],
        prilozena_adresa=f"Adresa zahteva {kupac.ime}",
        status=random.choice(["novo", "odobreno", "odbijeno"]),
        komentar=f"Komentar zahteva {kupac.ime}",
        datum_kreiranja=datetime.now() - timedelta(days=random.randint(0, 10)),
        datum_obrade=None if random.random() < 0.5 else datetime.now(),
        fk_kupac=kupac,
        fk_admin=admin if random.random() < 0.5 else None,
        fk_prilozeno_mesto=random.choice(mesta)
    )
    zahtevi.append(z)

# ---- 6. Kreiraj obavestenja ----
for i in range(5):
    Obavestenje.objects.create(
        sadrzaj=f"Obavestenje {i} za test",
        datum_kreiranja=datetime.now() - timedelta(days=random.randint(0, 5)),
        vidljivost=1,
        fk_admin=admin,
        fk_zahtev=random.choice(zahtevi)
    )

print("Test podaci sa korisničkim ulogama uspešno generisani!")
