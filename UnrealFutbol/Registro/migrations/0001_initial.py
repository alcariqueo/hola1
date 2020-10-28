# Generated by Django 3.1.2 on 2020-10-10 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('FechaN', models.DateField(blank=True, null=True)),
                ('Telefono', models.IntegerField(max_length=9)),
                ('password', models.CharField(max_length=6)),
                ('passwordC', models.CharField(max_length=6)),
            ],
        ),
    ]
