from django.db import models
from django.urls import reverse
from persons.models import Person

class Promoter(models.Model):

    SCHOOL_LEVEL_CHOICES = [
        ('pri', 'Primaria'),
        ('sec', 'Secundaria'),
        ('pre', 'Pre-universitario'),
        ('uni', 'Universitario'),
    ]

    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    age = models.PositiveIntegerField('Edad')
    school_level = models.CharField('Nivel Escolar', max_length=3, choices=SCHOOL_LEVEL_CHOICES)
    occupation = models.CharField('Ocupación', max_length=150, null=True, blank=True)
    address = models.TextField('Dirección', null=True, blank=True)
    phone_or_place = models.CharField('Teléfono o lugar', max_length=220, null=True, blank=True)

    class Meta:
        verbose_name = 'Promovente'
        verbose_name_plural = 'Promoventes'
    
    def __str__(self):
        return f'{self.person.name} {self.person.last_name}'
    
    def get_absolute_url(self):
        """
        returns the detail view of an object given its id
        for now is meant to be triggered in the create and update views
        """
        return reverse('promoters_detail', kwargs={'pk': self.pk})