# Generated by Django 4.0.4 on 2022-05-26 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_phones_alter_watches_options_alter_watches_brand_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchesMechanism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mechanism', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='watches',
            name='mechanism',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.watchesmechanism'),
        ),
    ]
