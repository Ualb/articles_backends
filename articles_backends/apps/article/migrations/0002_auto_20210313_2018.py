# Generated by Django 3.1.7 on 2021-03-14 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='code',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
