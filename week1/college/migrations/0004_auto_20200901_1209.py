# Generated by Django 3.0.8 on 2020-09-01 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_auto_20200901_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='college_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='college.College'),
        ),
        migrations.AlterField(
            model_name='student',
            name='stream_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='college.Stream'),
        ),
    ]