# Generated by Django 3.2.3 on 2021-05-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_new_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(default='new.png', upload_to='news'),
        ),
    ]