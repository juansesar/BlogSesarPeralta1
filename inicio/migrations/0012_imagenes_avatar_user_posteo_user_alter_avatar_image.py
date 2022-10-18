# Generated by Django 4.1 on 2022-10-18 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inicio', '0011_delete_imagenes_alter_avatar_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='imagenes')),
            ],
        ),
        migrations.AddField(
            model_name='avatar',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='posteo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
