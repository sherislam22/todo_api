# Generated by Django 3.2.9 on 2021-11-07 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('creates', models.DateField(default='2021=11-07')),
                ('due_date', models.DateField(default='2021=11-07')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.category')),
            ],
        ),
    ]
