# Generated by Django 4.1 on 2022-10-13 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0007_imagenes_delete_datos_personales'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(max_length=100)),
                ('cuerpo', models.CharField(max_length=500)),
                ('fecha', models.DateField()),
            ],
        ),
    ]