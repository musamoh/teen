# Generated by Django 2.2.3 on 2019-08-31 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teenager', '0006_institution'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('FEMALE', 'FEMALE'), ('MALE', 'MALE')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]