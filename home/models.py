# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Tipo_Equipamento(models.Model):

    #__Tipo_Equipamento_FIELDS__
    descricao = models.CharField(max_length=255, null=True, blank=True)

    #__Tipo_Equipamento_FIELDS__END

    class Meta:
        verbose_name        = _("Tipo_Equipamento")
        verbose_name_plural = _("Tipo_Equipamento")


class Subtipo(models.Model):

    #__Subtipo_FIELDS__
    pk_tipo = models.ForeignKey(tipo_equipamento, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255, null=True, blank=True)

    #__Subtipo_FIELDS__END

    class Meta:
        verbose_name        = _("Subtipo")
        verbose_name_plural = _("Subtipo")


class Classificacao(models.Model):

    #__Classificacao_FIELDS__
    pk_subtipo = models.ForeignKey(subtipo, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255, null=True, blank=True)

    #__Classificacao_FIELDS__END

    class Meta:
        verbose_name        = _("Classificacao")
        verbose_name_plural = _("Classificacao")



#__MODELS__END
