from django.db import models
from django.urls import reverse


class Person(models.Model):
    SEX_CHOICES = [
        ('m', 'Masculino'),
        ('f', 'Femenino'),
    ]

    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellidos', max_length=250)
    sex = models.CharField('Sexo', max_length=1, choices=SEX_CHOICES)
    demmanded = models.BooleanField(editable=False, default=False)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return f'{self.name} - {self.last_name}'
    
    def get_absolute_url(self):
        """
        returns the detail view of an object given its id
        for now is meant to be triggered in the create and update views
        """
        return reverse('persons_detail', kwargs={'pk': self.pk})