# Generated by Django 4.1.3 on 2022-11-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_jogos_imagem_alter_comentario_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resenha',
            name='imagem_resenha',
            field=models.ImageField(blank=True, null=True, upload_to='askon/resenhas'),
        ),
    ]