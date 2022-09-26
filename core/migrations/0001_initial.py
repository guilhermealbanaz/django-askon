# Generated by Django 4.1.1 on 2022-09-25 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('idade', models.IntegerField()),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senha', models.CharField(max_length=45)),
                ('data', models.DateField(verbose_name='data de nascimento')),
                ('email', models.CharField(max_length=120)),
                ('fone', models.CharField(max_length=12)),
                ('typeuser', models.BooleanField(default=False)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Resenha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=5000, verbose_name='descrição da resenha')),
                ('data', models.DateTimeField(verbose_name='data da publicação')),
                ('links', models.CharField(max_length=500)),
                ('jogo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.jogos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Curtidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('resenha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.resenha')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=150)),
                ('data', models.DateTimeField()),
                ('resenha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.resenha')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.usuario')),
            ],
        ),
    ]
