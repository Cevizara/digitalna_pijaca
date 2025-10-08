from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Korisnik
from .forms import CustomUserCreationForm

class KorisnikAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = Korisnik
    list_display = ('email', 'ime', 'uloga', 'is_staff', 'is_superuser')
    search_fields = ('email', 'ime')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'sifra', 'ime', 'uloga', 'fk_mesto')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'ime', 'sifra', 'uloga', 'fk_mesto', 'is_staff', 'is_superuser')}
        ),
    )

admin.site.register(Korisnik, KorisnikAdmin)
