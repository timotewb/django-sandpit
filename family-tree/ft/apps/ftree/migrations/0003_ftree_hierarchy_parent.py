# Generated by Django 4.1.7 on 2023-04-02 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftree', '0002_alter_ftree_hierarchy_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='ftree_hierarchy',
            name='parent',
            field=models.IntegerField(null=True),
        ),
    ]
