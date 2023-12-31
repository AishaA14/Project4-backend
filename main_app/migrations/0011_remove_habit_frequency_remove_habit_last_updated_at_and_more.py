# Generated by Django 4.2.7 on 2023-11-22 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_habit_goal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='frequency',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='last_updated_at',
        ),
        migrations.AddField(
            model_name='habit',
            name='frequency_unit',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], default='daily', max_length=10),
        ),
        migrations.AlterField(
            model_name='habit',
            name='frequency_amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='habit',
            name='goal',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.goal'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
