# Generated by Django 5.0.1 on 2024-01-19 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_directorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='earnings',
            name='directorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='earnings', to='base.directorie'),
        ),
        migrations.AddField(
            model_name='expense',
            name='directorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='base.directorie'),
        ),
        migrations.AlterField(
            model_name='directorie',
            name='dashboard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directories', to='base.dashboard'),
        ),
    ]
