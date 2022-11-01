# Generated by Django 4.1.3 on 2022-11-01 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actividad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre: ')),
            ],
        ),
        migrations.AlterField(
            model_name='actividad',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividad.estado'),
        ),
    ]
