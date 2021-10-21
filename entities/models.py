from django.db import models
from django.urls import reverse
from organisms.models import Organism


class Entity(models.Model):
    name = models.CharField('Nombre', max_length=250)
    address = models.TextField('Dirección')
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """
        returns the detail view of an object given its id
        for now is meant to be triggered in the create and update views
        """
        return reverse('entities_detail', kwargs={'pk': self.pk})