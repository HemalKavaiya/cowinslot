# Generated by Django 3.1.5 on 2021-08-10 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.IntegerField(choices=[(0, 'disabled'), (1, 'active')], default=1),
        ),
    ]
