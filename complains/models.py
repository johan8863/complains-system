from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from entities.models import Entity
from persons.models import Person
from promoters.models import Promoter


class Complain(models.Model):
    reception_date = models.DateField('Fecha de recepción')
    promoter = models.ForeignKey(Promoter, on_delete=models.CASCADE, verbose_name=Promoter._meta.verbose_name)
    demmanded_entity = models.ForeignKey(Entity, null=True, blank=True, on_delete=models.CASCADE, related_name='demmanded_entity', verbose_name=Entity._meta.verbose_name)
    demmanded_person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE, verbose_name=Person._meta.verbose_name)
    management_level = models.CharField('Nivel de dirección que involucra', max_length=220)
    belonging_entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='belonging_entity', verbose_name=Person._meta.verbose_name)
    problem = models.TextField('Planteamiento')
    
    class Meta:
        verbose_name = 'Queja'
        verbose_name_plural = 'Quejas'
        ordering = ['-reception_date']
    
    def __str__(self):
        promoter_str = self.promoter if self.promoter else '...'
        demmannded_entity_str = self.demmanded_entity if self.demmanded_entity else '...'
        demmanded_person_str = self.demmanded_person if self.demmanded_person else '...'
        return f'{self.reception_date} - Promovente: {promoter_str} - Entidad demandada: {demmannded_entity_str} - Persona demandada: {demmanded_person_str}'

    def get_absolute_url(self):
        """
        returns the detail view of an object given its id
        for now is meant to be triggered in the create and update views
        """
        return reverse('complains_detail', kwargs={'pk': self.pk})        


@receiver(post_save, sender=Complain)
def set_demmanded_person(sender, instance, *args, **kwargs):
    if instance.demmanded_person:
        instance.demmanded_person.demmanded = True
        instance.demmanded_person.save()