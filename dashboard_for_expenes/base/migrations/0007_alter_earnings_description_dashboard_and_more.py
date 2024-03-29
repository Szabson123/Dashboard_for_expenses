# Generated by Django 4.2.6 on 2024-01-17 11:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0006_alter_expense_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earnings',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('target', models.DecimalField(decimal_places=2, max_digits=30)),
                ('data', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='earnings',
            name='dashboard',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='base.dashboard'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='dashboard',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='base.dashboard'),
            preserve_default=False,
        ),
    ]
