# Generated by Django 3.0.2 on 2020-01-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200113_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
