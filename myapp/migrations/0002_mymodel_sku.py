# Generated by Django 4.2.9 on 2024-01-15 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='sku',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]