# Generated by Django 3.2.7 on 2021-10-20 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bestBefore', models.DateField()),
                ('location', models.CharField(choices=[('N', 'North'), ('E', 'East'), ('S', 'South'), ('W', 'West')], default=0, max_length=1)),
                ('brew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.brew')),
            ],
        ),
    ]
