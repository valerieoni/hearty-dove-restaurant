# Generated by Django 3.2.13 on 2022-06-22 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_auto_20220622_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='menu.category'),
        ),
    ]
