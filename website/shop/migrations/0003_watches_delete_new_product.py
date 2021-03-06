# Generated by Django 4.0.4 on 2022-05-25 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_new_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('sex', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('UNISEX', 'unisex')], default='UNISEX', max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
        migrations.DeleteModel(
            name='New_product',
        ),
    ]
