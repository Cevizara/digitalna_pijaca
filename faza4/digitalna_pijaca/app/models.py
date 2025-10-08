# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class KorisnikManager(BaseUserManager):
    def create_user(self, email, sifra, **extra_fields):
        if not email:
            raise ValueError('Email mora biti unet')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(sifra)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, sifra, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, sifra, **extra_fields)

class Korisnik(AbstractBaseUser, PermissionsMixin):
    id_korisnik = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    sifra = models.CharField(max_length=255)
    ime = models.CharField(max_length=255)
    uloga = models.CharField(max_length=7)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    adresa = models.CharField(max_length=255, blank=True, null=True)
    opis = models.TextField(blank=True, null=True)
    fk_mesto = models.ForeignKey('Mesto', models.DO_NOTHING, db_column='fk_mesto', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['ime']

    objects = KorisnikManager()

    class Meta:
        db_table = 'korisnik'


class Mesto(models.Model):
    id_mesto = models.AutoField(primary_key=True)
    naziv = models.CharField(unique=True, max_length=45)

    class Meta:
        db_table = 'mesto'

class Kategorija(models.Model):
    id_kategorija = models.AutoField(primary_key=True)
    putanja_slike = models.CharField(max_length=255, blank=True, null=True)
    naziv = models.CharField(unique=True, max_length=45)
    vrsta = models.CharField(max_length=20)

    class Meta:
        db_table = 'kategorija'

class Obavestenje(models.Model):
    id_obavestenje = models.AutoField(primary_key=True)
    sadrzaj = models.TextField(blank=True, null=True)
    datum_kreiranja = models.DateTimeField(blank=True, null=True)
    vidljivost = models.IntegerField()
    fk_admin = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='fk_admin', blank=True, null=True)
    fk_zahtev = models.ForeignKey('Zahtev', models.DO_NOTHING, db_column='fk_zahtev', blank=True, null=True)

    class Meta:
        db_table = 'obavestenje'


class Proizvod(models.Model):
    id_proizvod = models.AutoField(primary_key=True)
    naziv = models.CharField(max_length=100)
    opis = models.TextField(blank=True, null=True)
    putanja_slike = models.CharField(max_length=255, blank=True, null=True)
    nacin_uzgoja = models.CharField(max_length=8)
    dostupnost = models.IntegerField()
    datum_kreiranja = models.DateTimeField()
    fk_domacin = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='fk_domacin')
    fk_kategorija = models.ForeignKey(Kategorija, models.DO_NOTHING, db_column='fk_kategorija', blank=True, null=True)

    class Meta:
        db_table = 'proizvod'


class Zahtev(models.Model):
    id_zahtev = models.AutoField(primary_key=True)
    prilozeni_telefon = models.CharField(max_length=20)
    prilozena_adresa = models.CharField(max_length=255)
    status = models.CharField(max_length=8)
    komentar = models.TextField(blank=True, null=True)
    datum_kreiranja = models.DateTimeField()
    datum_obrade = models.DateTimeField(blank=True, null=True)
    fk_kupac = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='fk_kupac')
    fk_admin = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='fk_admin', related_name='zahtev_fk_admin_set', blank=True, null=True)
    fk_prilozeno_mesto = models.ForeignKey(Mesto, models.DO_NOTHING, db_column='fk_prilozeno_mesto', blank=True, null=True)

    class Meta:
        db_table = 'zahtev'
