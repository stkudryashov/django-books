# Generated by Django 3.1.7 on 2021-04-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='Author', max_length=255, verbose_name='автор'),
            preserve_default=False,
        ),
    ]
