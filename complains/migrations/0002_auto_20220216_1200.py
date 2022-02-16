# Generated by Django 3.2 on 2022-02-16 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
        ('persons', '0002_alter_person_last_name'),
        ('promoters', '0002_alter_promoter_person'),
        ('complains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='belonging_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belonging_entity', to='entities.entity', verbose_name='Persona'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='demmanded_entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demmanded_entity', to='entities.entity', verbose_name='Entidad'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='demmanded_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persons.person', verbose_name='Persona'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='promoter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promoters.promoter', verbose_name='Promovente'),
        ),
    ]