# Generated by Django 4.0.5 on 2022-06-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_watches_company_alter_watches_mechanism_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchescompany',
            name='company',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]