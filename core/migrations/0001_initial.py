# Generated by Django 4.1.3 on 2024-03-08 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id_artikel', models.IntegerField(primary_key=True, serialize=False)),
                ('judul', models.CharField(max_length=255)),
                ('word_count', models.IntegerField()),
                ('bluelinks_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id_kategori', models.AutoField(primary_key=True, serialize=False)),
                ('nama_kategori', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hasil_Kategori',
            fields=[
                ('id_hasil_kat', models.AutoField(primary_key=True, serialize=False)),
                ('words_gini_score', models.FloatField(default=None)),
                ('bluelinks_gini_score', models.FloatField(default=None)),
                ('id_kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.kategori')),
            ],
            options={
                'unique_together': {('id_kategori',)},
            },
        ),
        migrations.CreateModel(
            name='Artikel_Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_artikel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.artikel')),
                ('nama_kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.kategori')),
            ],
            options={
                'unique_together': {('id_artikel', 'nama_kategori')},
            },
        ),
    ]
