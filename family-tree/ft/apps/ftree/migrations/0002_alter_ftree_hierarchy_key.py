# Generated by Django 4.1.7 on 2023-04-02 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftree', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ftree_hierarchy',
            name='key',
            field=models.IntegerField(unique=True),
        ),
    ]
