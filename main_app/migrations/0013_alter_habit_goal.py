# Generated by Django 4.2.7 on 2023-11-22 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_task_delete_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='goal',
            field=models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.goal'),
        ),
    ]