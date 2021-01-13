# Generated by Django 3.1 on 2021-01-07 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testo',
            name='lingua',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.lingua'),
        ),
        migrations.CreateModel(
            name='Linguaconosciuta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lingua', models.CharField(max_length=25)),
                ('livello', models.CharField(max_length=25)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.candidato')),
            ],
            options={
                'verbose_name': 'lingua_conosciuta',
                'verbose_name_plural': 'lingue_conosciuta',
                'db_table': 'lingua_conosciuta',
            },
        ),
    ]
