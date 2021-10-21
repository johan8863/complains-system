from django.db import models
from django.urls import reverse


class Organism(models.Model):
    name = models.CharField('Nombre', max_length=20)

    class Meta:
        verbose_name = 'Organismo'
        verbose_name_plural = 'Organismos'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """
        returns the detail view of an object given its id
        for now is meant to be triggered in the create and update views
        """
        return reverse('organisms_detail', kwargs={'pk': self.pk})