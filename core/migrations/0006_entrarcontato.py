# Generated by Django 4.0.4 on 2022-05-25 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_delete_entrarcontato'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntrarContato',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('motivo', models.CharField(max_length=50)),
            ],
        ),
    ]
