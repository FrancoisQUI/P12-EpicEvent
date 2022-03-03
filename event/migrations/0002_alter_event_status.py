# Generated by Django 4.0.2 on 2022-03-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('OE', 'Over Event'), ('PE', 'Pending Event'), ('FE', 'Future Event')], default='FE', max_length=2),
        ),
    ]