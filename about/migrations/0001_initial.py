# Generated by Django 3.1.6 on 2021-03-05 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('detail', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Executive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('role', models.CharField(db_index=True, max_length=200)),
                ('hobby', models.CharField(db_index=True, max_length=200)),
                ('contact', models.CharField(db_index=True, max_length=200)),
                ('facebook', models.CharField(db_index=True, max_length=200)),
                ('twitter', models.CharField(db_index=True, max_length=200)),
                ('instagram', models.CharField(db_index=True, max_length=200)),
                ('pictur', models.ImageField(blank=True, upload_to='images/%Y/%m/%d')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
