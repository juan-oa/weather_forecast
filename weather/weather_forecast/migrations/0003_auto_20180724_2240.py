# Generated by Django 2.0 on 2018-07-24 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather_forecast', '0002_auto_20180724_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='forecast',
            name='date',
            field=models.DateTimeField(verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='forecast',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='weather_forecast.Region'),
        ),
    ]
