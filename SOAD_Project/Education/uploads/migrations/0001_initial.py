# Generated by Django 3.1.3 on 2020-12-10 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('subject', models.CharField(max_length=25)),
                ('school_name', models.CharField(max_length=50)),
                ('remarks', models.CharField(max_length=50)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('notes_file', models.FileField(default='Unnamed File', upload_to='files/notes')),
                ('file_url', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
