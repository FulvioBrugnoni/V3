from django.db import models
from quest.models import Candidato, Azienda


class Recruiter(models.Model):

    utente = models.CharField(max_length=25, unique=True)

    class Meta:
            db_table ='recruiter'
            verbose_name ='recruiter'
            verbose_name_plural ='recruiters'
    def __str__(self):
        return self.nome


class Algoritmo(models.Model):

    algoritmo = models.CharField(max_length=25, unique=True)

    class Meta:
            db_table ='algoritmo'
            verbose_name ='algoritmo'
            verbose_name_plural ='algoritmi'
    def __str__(self):
        return self.nome


class AlgoritmoRecruiter(models.Model):

    algoritmo = models.ForeignKey(Algoritmo, on_delete=models.PROTECT)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.PROTECT)
    azienda = models.ForeignKey(Azienda, on_delete=models.PROTECT)
    stato = models.BooleanField()

    class Meta:
            db_table ='algoritmo_recruiter'
            verbose_name ='algoritmo_recruiter'
            verbose_name_plural ='algoritmo_recruiters'
    def __str__(self):
        return self.nome

class PrevisioneCorrente(models.Model):

    candidato = models.ForeignKey(Candidato, on_delete=models.PROTECT)
    algoritmo = models.ForeignKey(Algoritmo, on_delete=models.PROTECT)
    previsione = models.DecimalField( max_digits = 5, decimal_places = 2)
    esito = models.BooleanField()

    class Meta:
            db_table ='previsione_corrente'
            verbose_name ='previsione_corrente'
            verbose_name_plural ='previsioni_corrente'

            unique_together = [['candidato','algoritmo']]

    def __str__(self):
        return f"{self.nome.recruiter}-{self.previsione_corrente.candidato} "


class PrevisioneStraordinaria(models.Model):

    candidato = models.ForeignKey(Candidato, on_delete=models.PROTECT)
    algoritmo = models.ForeignKey(Algoritmo, on_delete=models.PROTECT)
    previsione = models.DecimalField( max_digits = 5, decimal_places = 2)
    esito = models.BooleanField()

    class Meta:
            db_table ='previsione_straordinaria'
            verbose_name ='previsione_straordinaria'
            verbose_name_plural ='previsioni_straordinari'

            unique_together = [['candidato','algoritmo']]

    def __str__(self):
        return f"{self.nome.recruiter}-{self.previsione_straordinaria.candidato} "
