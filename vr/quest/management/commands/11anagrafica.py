from django.core.management.base import BaseCommand, CommandError
from quest.models import *
from recruiter.models import *
import csv
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    BASEDIR = '/Users/fulvio/Desktop/virtual2/vr/csv/'
    def handle(self,*args,**kwargs):

        with open(self.BASEDIR+'Anagrafica.csv') as csv_file:
            csv_reader = csv.reader(csv_file,delimiter=',')
            counter = 0

            for row in csv_reader:
                self.stdout.write(f'Elemento {row[0]} letto')
                if counter ==0:
                    counter += 1
                    continue
                try:
                    candidato = Candidato.objects.get(id =row[0])
                except ObjectDoesNotExist:
                    self.stderr.write(f'Elemento {row[0]} non presente nel db')
                    continue
                try:
                    importazione = Anagrafica(candidato=candidato,
                                                    nome = row[1],
                                                    cognome = row[2],
                                                    codicefiscale = row[3],
                                                    eta = row[4],
                                                    gender = row[5],
                                                    stato =row[6],
                                                    provincia =row[7],
                                                    comune =row[8])
                    importazione.save()
                    self.stdout.write(f'Elemento {importazione.id} inserito')
                except IntegrityError:
                    self.stderr.write(f'Elemento già presente')
