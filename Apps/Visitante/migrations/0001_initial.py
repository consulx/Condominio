# Generated by Django 2.1.2 on 2018-11-23 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Propietario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=30)),
                ('app', models.CharField(max_length=30)),
                ('apm', models.CharField(max_length=30)),
                ('tmp_estadia', models.TimeField()),
                ('mod_ing', models.CharField(choices=[('AUTO', 'Automovil'), ('PIE', 'Caminando'), ('BICI', 'Bicicleta')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id_propietario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Propietario.Propietario')),
            ],
        ),
    ]