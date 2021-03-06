# Generated by Django 2.2.3 on 2019-08-08 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teenager', '0005_auto_20190806_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=300)),
                ('degree', models.CharField(default='Nil', max_length=200)),
                ('field_of_study', models.CharField(default='Nil', max_length=200)),
                ('grade_or_class', models.CharField(choices=[('JSS-1', 'JSS-1'), ('JSS-2', 'JSS-2'), ('JSS-3', 'JSS-3'), ('SS-1', 'SS-1'), ('SS-2', 'SS-2'), ('SS-3', 'SS-3'), ('100L', '100L'), ('200L', '200L'), ('300L', '300L'), ('400L', '400L'), ('500L', '500L'), ('ND1', 'ND1'), ('ND-2', 'ND-2'), ('HND-1', 'HND-2')], max_length=200)),
                ('started', models.DateField(null=True)),
                ('ended', models.DateField(null=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teenager.Student')),
            ],
            options={
                'ordering': ['-updated', '-timestamp'],
            },
        ),
    ]
