# Generated by Django 3.2.4 on 2021-06-26 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0005_auto_20210625_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='theme_id', to='topic.theme'),
        ),
    ]
