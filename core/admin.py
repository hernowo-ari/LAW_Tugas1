from django.contrib import admin
from .models import Artikel, Kategori, Artikel_Kategori, Hasil_Kategori

# Register your models here.



# Register your models here.
admin.site.register(Artikel)
admin.site.register(Kategori)
admin.site.register(Artikel_Kategori)
admin.site.register(Hasil_Kategori)