from django import forms

class CandidatoForm(forms.Form):
        user = forms.CharField(label='user', max_length=25)

class AnagraficaForm(forms.Form):
        nome = forms.CharField(label='nome', max_length=25)
        cognome = forms.CharField(label='cognome', max_length=25)
        codicefiscale = forms.CharField(label='codicefiscale', max_length=10)
        eta = forms.IntegerField()
        gender = forms.CharField(label='gender', max_length=1)
        stato = forms.CharField(label='stato', max_length=20)
        provincia = forms.CharField(label='provincia', max_length=20)
        comune = forms.CharField(label='comune', max_length=20)


class EsperienzaForm(forms.Form):
        professione = forms.CharField(label='professione', max_length=25)
        durata = forms.IntegerField()

class StudioForm(forms.Form):
        titolo = forms.CharField(label='titolo', max_length=25)

class LinguaForm(forms.Form):
        lingua = forms.CharField(label='lingua', max_length=25)
        livello = forms.CharField(label='livello', max_length=25)

class QuestionForm(forms.Form):
    questionario = forms.IntegerField()
    domanda = forms.IntegerField()
#     valutazione = forms.CharField()
    CHOICES=[('1','1'),
             ('2','2')]
    valutazione = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
