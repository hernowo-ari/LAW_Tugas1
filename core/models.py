from django.db import models

# Create your models here.


class Artikel(models.Model):
    id_artikel = models.IntegerField(primary_key=True)
    judul = models.CharField(max_length=255)
    word_count = models.IntegerField()
    bluelinks_count = models.IntegerField()

    def __str__(self):
        return self.judul

class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nama_kategori

class Artikel_Kategori(models.Model):
    id_artikel = models.ForeignKey(Artikel, on_delete=models.CASCADE)
    nama_kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('id_artikel', 'nama_kategori')

    def __str__(self):
        return f"{self.id_artikel} - {self.nama_kategori}"


class Hasil_Kategori(models.Model):
    id_hasil_kat = models.AutoField(primary_key=True)
    id_kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    words_gini_score = models.FloatField(default=None)
    bluelinks_gini_score = models.FloatField(default=None)

    class Meta:
        unique_together = ('id_kategori',)

    def __str__(self):
        return f"{self.id_kategori} - {self.words_gini_score}"
