# Generated by Django 4.0.4 on 2022-05-05 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]