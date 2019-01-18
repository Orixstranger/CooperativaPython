# Generated by Django 2.1.2 on 2019-01-17 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('nombres', models.CharField(max_length=70)),
                ('apellidos', models.CharField(max_length=70)),
                ('genero', models.CharField(choices=[('f', 'Femenino'), ('m', 'Masculino')], default='m', max_length=15)),
                ('estadoCivil', models.CharField(choices=[('soltero', 'Solter@'), ('casado', 'Casad@'), ('viudo', 'Viud@'), ('divorciado', 'Divorciad@'), ('unionLibre', 'Unión Libre')], default='soltero', max_length=15)),
                ('fechaNacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=100, unique=True)),
                ('telefono', models.CharField(max_length=10)),
                ('celular', models.CharField(max_length=10)),
                ('direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('cuenta_id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=20, unique=True)),
                ('estado', models.BooleanField(default=True)),
                ('fechaApertura', models.DateField(auto_now_add=True)),
                ('saldo', models.DecimalField(decimal_places=3, max_digits=10)),
                ('tipoCuenta', models.CharField(choices=[('corriente', 'Corriente'), ('ahorros', 'Ahorro'), ('nomina', 'Nómina'), ('valores', 'Valores')], default='ahorros', max_length=30)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('transaccion_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.CharField(choices=[('retiro', 'Retiro'), ('deposito', 'Depósito')], default='deposito', max_length=30)),
                ('valor', models.DecimalField(decimal_places=3, max_digits=10)),
                ('descripcion', models.TextField()),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Cuenta')),
            ],
        ),
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('transferencia_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('valor', models.DecimalField(decimal_places=3, max_digits=10)),
                ('descripcion', models.TextField()),
                ('cuenta1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuenta1', to='modelo.Cuenta')),
                ('cuenta2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuenta2', to='modelo.Cuenta')),
            ],
        ),
    ]
