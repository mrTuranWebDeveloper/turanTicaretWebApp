# Generated by Django 4.2 on 2023-07-16 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0004_serino_urun_seri_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltKategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='urun',
            name='seri_no',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='urunler.serino'),
        ),
        migrations.AddField(
            model_name='urun',
            name='altKategori',
            field=models.ManyToManyField(blank=True, to='urunler.altkategori'),
        ),
    ]
