# Generated by Django 3.2.4 on 2021-06-25 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0002_auto_20210625_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='topic.theme'),
        ),
    ]