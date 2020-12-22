from django.db import models
from datetime import datetime


class Questionario(models.Model):

    name = models.CharField(max_length=256, unique=True)

    class Meta:
            db_table ='questionario'
            verbose_name ='questionario'
            verbose_name_plural ='questionari'
    def __str__(self):
        return self.name


class Domanda(models.Model):

    chiave= models.CharField(max_length=6, unique=True)
    testo = models.CharField(max_length=256, unique=True)

    class Meta:
            db_table ='domanda'
            verbose_name ='domanda'
            verbose_name_plural ='domande'
    def __str__(self):
        return self.chiave

class QuestionarioDomanda(models.Model):

    questionario= models.ForeignKey(Questionario, on_delete=models.PROTECT)
    domanda = models.ForeignKey(Domanda, on_delete=models.PROTECT)
    posizione =models.PositiveSmallIntegerField()

    class Meta:
            db_table ='questionario_domanda'
            verbose_name ='questionario_domanda'
            verbose_name_plural ='questionari_domanda'

            unique_together = [['questionario','domanda'],['questionario','posizione'],]

    def __str__(self):
        return f"{self.questionario.name}-{self.domanda.chiave} "

class Candidato(models.Model):

    user= models.CharField(max_length=15)

    class Meta:
            db_table ='candidato'
            verbose_name ='candidato'
            verbose_name_plural ='candidati'
    def __str__(self):
        return self.nome

class Anagrafica(models.Model):

    candidato = models.ForeignKey(Candidato, on_delete=models.PROTECT)
    nome = models.CharField(max_length=25)
    cognome = models.CharField(max_length=25)
    codicefiscale = models.CharField(max_length=10)
    eta = models.IntegerField()
    gender = models.CharField(max_length=1)
    stato =models.CharField(max_length=20)
    provincia =models.CharField(max_length=20)
    comune =models.CharField(max_length=20)

    class Meta:
            db_table ='anagrafica'
            verbose_name ='anagrafica'
            verbose_name_plural ='anagrafiche'
    def __str__(self):
        return self.nome

class Studio(models.Model):

    candidato = models.ForeignKey(Candidato, on_delete=models.PROTECT)
    titolo = models.CharField(max_length=25)

    class Meta:
            db_table ='titolo'
            verbose_name ='titolo'
            verbose_name_plural ='titoli'
    def __str__(self):
        return self.nome

class Esperienza(models.Model):

    candidato = models.ForeignKey(Candidato, on_delete=models.PROTECT)
    professione = models.CharField(max_length=25)
    durata = models.IntegerField()

    class Meta:
            db_table ='eseperienza'
            verbose_name ='esperienza'
            verbose_name_plural ='esperienze'
    def __str__(self):
        return self.nome

class Lingua(models.Model):

    candidato = models.ForeignKey(Candidato, on_delete=models.PROTECT)
    lingua = models.CharField(max_length=25)
    livello = models.CharField(max_length=25)

    class Meta:
            db_table ='lingua'
            verbose_name ='lingua'
            verbose_name_plural ='lingue'
    def __str__(self):
        return self.nome


ANS_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
)

class Risposta(models.Model):

    utente= models.ForeignKey(Candidato, on_delete=models.PROTECT)
    domanda = models.ForeignKey(QuestionarioDomanda, on_delete=models.PROTECT)
    valutazione =models.CharField(max_length=1,choices=ANS_CHOICES)

    class Meta:
            db_table ='risposta'
            verbose_name ='risposta'
            verbose_name_plural ='risposte'

            unique_together = [['utente','domanda'],]

    def __str__(self):
        return self.utente.nome


class Azienda(models.Model):

    azienda = models.CharField(max_length=25, unique=True)
    lingua = models.CharField(max_length=25)

    class Meta:
            db_table ='azienda'
            verbose_name ='azienda'
            verbose_name_plural ='aziende'

    def __str__(self):
        return self.nome

class CandidatoAzienda(models.Model):

    candidato = models.ForeignKey(Candidato, on_delete=models.PROTECT)
    azienda = models.ForeignKey(Azienda, on_delete=models.PROTECT)
    giorno = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
            db_table ='candidato_azienda'
            verbose_name ='candidato_azienda'
            verbose_name_plural ='candidato_aziende'

    def __str__(self):
        return self.nome

class Testo(models.Model):

    testo = models.CharField(max_length=25)
    posizione = models.CharField(max_length=25)
    lingua = models.CharField(max_length=25)

    class Meta:
            db_table ='testo'
            verbose_name ='testo'
            verbose_name_plural ='testi'

    def __str__(self):
        return self.nome

class Parametro(models.Model):

    candidato = models.ForeignKey(Candidato, on_delete=models.PROTECT)
    parametro = models.CharField(max_length=25)

    class Meta:
            db_table ='parametro'
            verbose_name ='parametro'
            verbose_name_plural ='parametri'
    def __str__(self):
        return self.nome
