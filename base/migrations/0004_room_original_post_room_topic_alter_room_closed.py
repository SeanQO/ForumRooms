# Generated by Django 4.1.6 on 2023-03-25 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='original_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.post'),
        ),
        migrations.AddField(
            model_name='room',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.topic'),
        ),
        migrations.AlterField(
            model_name='room',
            name='closed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
