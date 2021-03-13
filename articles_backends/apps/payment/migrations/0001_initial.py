# Generated by Django 3.1.7 on 2021-03-13 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payment',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PaymentDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('codeArticle', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='article', to='article.article')),
                ('idPayment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='payment', to='payment.payment')),
            ],
            options={
                'verbose_name': 'Payment Detail',
                'verbose_name_plural': 'Details',
                'ordering': ['id'],
            },
        ),
    ]
