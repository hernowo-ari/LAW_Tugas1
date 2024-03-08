from rest_framework import serializers
from .models import Artikel, Kategori, Artikel_Kategori, Hasil_Kategori

class ArtikelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artikel
        fields = ['id_artikel', 'judul', 'word_count', 'bluelinks_count']

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['id_kategori', 'nama_kategori']

class ArtikelKategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artikel_Kategori
        fields = ['id_artikel', 'nama_kategori']

class HasilKategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hasil_Kategori
        fields = ['id_hasil_kat', 'id_kategori', 'words_gini_score', 'bluelinks_gini_score']