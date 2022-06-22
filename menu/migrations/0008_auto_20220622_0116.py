# Generated by Django 3.2.13 on 2022-06-22 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20220622_0012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drinkcategory',
            options={'verbose_name_plural': 'drink categories'},
        ),
        migrations.AlterField(
            model_name='meal',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_category', to='menu.category'),
        ),
    ]
