from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from quest.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

def V1(request):
        azienda = AziendaLingua.objects.filter(candidatoparametro__parametro = 2).first().id
        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
        testo = Testo.objects.filter(lingua = lingua, slide =1)
        tab = {'tab': testo, 'passo_destra':reverse('registrazione_utenti'), 'passo_sinistra':'/2'}
        return render(request,'quest/richiesta_inserimento.html',tab)

def V6(request):
        azienda = AziendaLingua.objects.filter(candidatoparametro__parametro = 2).first().id
        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
        testo = Testo.objects.filter(lingua = lingua, slide =6)
        tab = {'tab': testo, 'passo_destra':reverse('registrazioni_studi'), 'passo_sinistra': reverse('ingresso_esperienza')}
        return render(request,'quest/richiesta_inserimento.html',tab)

def V8(request):
        azienda = AziendaLingua.objects.filter(candidatoparametro__parametro = 2).first().id
        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
        testo = Testo.objects.filter(lingua = lingua, slide =8)
        tab = {'tab': testo, 'passo_destra':reverse('registrazioni_studi'), 'passo_sinistra': reverse('ingresso_esperienza')}
        return render(request,'quest/richiesta_inserimento.html',tab)

def V9(request):
        azienda = AziendaLingua.objects.filter(candidatoparametro__parametro = 2).first().id
        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
        testo = Testo.objects.filter(lingua = lingua, slide =9)
        tab = {'tab': testo, 'passo_destra':reverse('registrazioni_esperienze'), 'passo_sinistra': reverse('ingresso_lingue')}
        return render(request,'quest/richiesta_inserimento.html',tab)

def V11(request):
        azienda = AziendaLingua.objects.filter(candidatoparametro__parametro = 2).first().id
        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
        testo = Testo.objects.filter(lingua = lingua, slide =11)
        tab = {'tab': testo, 'passo_destra':reverse('registrazioni_esperienze'), 'passo_sinistra': reverse('ingresso_lingue')}
        return render(request,'quest/richiesta_inserimento.html',tab)

def V12(request):
        azienda = AziendaLingua.objects.filter(candidatoparametro__parametro = 2).first().id
        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
        testo = Testo.objects.filter(lingua = lingua, slide =12)
        tab = {'tab': testo, 'passo_destra':reverse('registrazioni_lingue'), 'passo_sinistra': reverse('registrazioni_questionari')}
        return render(request,'quest/richiesta_inserimento.html',tab)

def V14(request):
        azienda = AziendaLingua.objects.filter(candidatoparametro__parametro = 2).first().id
        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
        testo = Testo.objects.filter(lingua = lingua, slide =14)
        tab = {'tab': testo, 'passo_destra':reverse('registrazioni_lingue'), 'passo_sinistra': reverse('registrazioni_questionari')}
        return render(request,'quest/richiesta_inserimento.html',tab)

def V16(request):
        azienda = AziendaLingua.objects.filter(candidatoparametro__parametro = 2).first().id
        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
        testo = Testo.objects.filter(lingua = lingua, slide =16)
        tab = {'tab': testo}
        return render(request,'quest/richiesta_inserimento.html',tab)

def V17(request):
        azienda = AziendaLingua.objects.filter(candidatoparametro__parametro = 2).first().id
        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
        testo = Testo.objects.filter(lingua = lingua, slide =17)
        tab = {'tab': testo}
        return render(request,'quest/pagina_utente.html',tab)

def V19(request):
        azienda = AziendaLingua.objects.filter(candidatoparametro__parametro = 2).first().id
        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
        testo = Testo.objects.filter(lingua = lingua, slide =19)
        tab = {'tab': testo, 'passo_destra':reverse('upload_secondo_studi'), 'passo_sinistra': reverse('pagina_utente')}
        return render(request,'quest/richiesta_inserimento.html',tab)

def V22(request):
        azienda = AziendaLingua.objects.filter(candidatoparametro__parametro = 2).first().id
        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
        testo = Testo.objects.filter(lingua = lingua, slide =22)
        tab = {'tab': testo, 'passo_destra':reverse('upload_secondo_esperienze'), 'passo_sinistra': reverse('pagina_utente')}
        return render(request,'quest/richiesta_inserimento.html',tab)

def V25(request):
        azienda = AziendaLingua.objects.filter(candidatoparametro__parametro = 2).first().id
        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
        testo = Testo.objects.filter(lingua = lingua, slide =25)
        tab = {'tab': testo, 'passo_destra':reverse('upload_secondo_lingue'), 'passo_sinistra': reverse('pagina_utente')}
        return render(request,'quest/richiesta_inserimento.html',tab)

#---------------------------------------------------------------------------------------------------------


def RegistrationView(request):
        if request.method == "POST":
                form = CandidatoForm(request.POST)
                if form.is_valid():
                    candidato = form.cleaned_data["user"]
                    u = Candidato(user =candidato)
                    u.save()
                    return HttpResponseRedirect(reverse('registrazioni_anagrafica'))
        else:
            form = CandidatoForm()

        return render(request,'quest/registrazione_utente.html', {'form': form})


def RegistrationAnagView(request):
        candidato = Candidato.objects.all().order_by("-id")[0]
        if request.method == "POST":
                form = AnagraficaForm(request.POST)
                if form.is_valid():
                    nome = form.cleaned_data["nome"]
                    cognome = form.cleaned_data["cognome"]
                    codicefiscale = form.cleaned_data["codicefiscale"]
                    eta = form.cleaned_data["eta"]
                    gender = form.cleaned_data["gender"]
                    stato = form.cleaned_data["stato"]
                    provincia = form.cleaned_data["provincia"]
                    comune = form.cleaned_data["comune"]
                    u = Anagrafica(candidato =candidato, nome=nome, cognome=cognome, codicefiscale=codicefiscale,
                                eta =eta, gender=gender, stato=stato, provincia=provincia, comune=comune)
                    u.save()
                    return HttpResponseRedirect(reverse('ingresso_studi'))
        else:
            form = AnagraficaForm()

        return render(request,'quest/registrazione_utente.html', {'form': form})


def RegistrationStudView(request):
        candidato = Candidato.objects.all().order_by("-id")[0]
        if request.method == "POST":
                form = StudioForm(request.POST)
                if form.is_valid():
                    titolo = form.cleaned_data["titolo"]
                    u = Studio(candidato =candidato, titolo=titolo)
                    u.save()
                    return HttpResponseRedirect(reverse('uscita_studi'))
        else:
            form = StudioForm()

        return render(request,'quest/registrazione_utente.html', {'form': form})

def RegistrationExpView(request):
        candidato = Candidato.objects.all().order_by("-id")[0]
        if request.method == "POST":
                form = EsperienzaForm(request.POST)
                if form.is_valid():
                    professione = form.cleaned_data["professione"]
                    durata = form.cleaned_data["durata"]
                    u = Esperienza(candidato =candidato, professione=professione, durata=durata)
                    u.save()
                    return HttpResponseRedirect(reverse('uscita_esperienze'))
        else:
            form = EsperienzaForm()

        return render(request,'quest/registrazione_utente.html', {'form': form})

def RegistrationLangView(request):
        candidato = Candidato.objects.all().order_by("-id")[0]
        if request.method == "POST":
                form = LinguaForm(request.POST)
                if form.is_valid():
                    lingua = form.cleaned_data["lingua"]
                    livello = form.cleaned_data["livello"]
                    u = Linguaconosciuta(candidato =candidato, lingua=lingua, livello=livello)
                    u.save()
                    return HttpResponseRedirect(reverse('uscita_lingue'))
        else:
            form = LinguaForm()

        return render(request,'quest/registrazione_utente.html', {'form': form})


def ProvaView(request):
#        query = Risposta.objects.filter(utente__id = 5).order_by('-domanda__posizione').first()
#         print(query.domanda)
        return render(request,'quest/prova.html')


def QuestView(request):
        utente = Candidato.objects.all().order_by("-id")[0]
        if request.method == "POST":
            form = QuestionForm(request.POST)
            if form.is_valid():
                valutazione= form.cleaned_data["valutazione"]
                questionario_id= form.cleaned_data["questionario"]
                domanda_id= form.cleaned_data["domanda"]
                questionario_domanda =QuestionarioDomanda.objects.get(questionario__id =questionario_id, domanda__id = domanda_id)
                v = Risposta(utente=utente,domanda=questionario_domanda ,valutazione=valutazione)
                v.save()
                try:
                    questionario_domanda =QuestionarioDomanda.objects \
                        .get(questionario =questionario_domanda.questionario,
                        posizione=questionario_domanda.posizione +1 )
                    form = QuestionForm(initial={'questionario':questionario_domanda.questionario.id, 'domanda': questionario_domanda.domanda.id })
                except ObjectDoesNotExist:
                    return HttpResponseRedirect(reverse('fine'))
        else:
            questionario = Questionario.objects.get(id=1)
            risposte = Risposta.objects.filter(domanda__questionario =questionario, utente=utente).order_by('-domanda__posizione')
#            print(risposte)
            if len(risposte) == 0:
                questionario_domanda =QuestionarioDomanda.objects.filter(questionario =questionario).order_by('posizione').first()

            else:
                ultima_questionario_domanda = risposte.first().domanda
                try:
                    questionario_domanda =QuestionarioDomanda.objects \
                        .get(questionario =ultima_questionario_domanda.questionario,
                            posizione=ultima_questionario_domanda.posizione +1 )
                except ObjectDoesNotExist:
                    return HttpResponseRedirect(reverse('fine'))

            form = QuestionForm(initial={'questionario':questionario.id, 'domanda': questionario_domanda.domanda.id })

        return render(request,'quest/15.html', {'form': form, 'testo_domanda':questionario_domanda.domanda.testo})

#---------------------------------------------------------------------------------------------------------------------------------------------------------

def RiassuntoCandidato(request):
        return render(request,'quest/riassunto_candidato.html')


def UpdateFirstLangView(request):
        id = 5
        Linguaconosciuta.objects.filter(candidato__id=id).delete()
        candidato = Candidato.objects.get(id = id)
        if request.method == "POST":
                form = LinguaForm(request.POST)
                if form.is_valid():
                    lingua = form.cleaned_data["lingua"]
                    livello = form.cleaned_data["livello"]
                    u = Linguaconosciuta(candidato =candidato, lingua=lingua, livello=livello)
                    u.save()
                    return HttpResponseRedirect(reverse('upload_lingue'))
        else:
            form = LinguaForm()

        return render(request,'quest/registrazione_utente.html', {'form': form})

def UpdatesecondLangView(request):
        id = 5
        candidato = Candidato.objects.get(id = id)
        if request.method == "POST":
                form = LinguaForm(request.POST)
                if form.is_valid():
                    lingua = form.cleaned_data["lingua"]
                    livello = form.cleaned_data["livello"]
                    u = Linguaconosciuta(candidato =candidato, lingua=lingua, livello=livello)
                    u.save()
                    return HttpResponseRedirect(reverse('upload_lingue'))
        else:
            form = LinguaForm()

        return render(request,'quest/registrazione_utente.html', {'form': form})


def UpdateFirstExpView(request):
        id = 5
        Esperienza.objects.filter(candidato__id=id).delete()
        candidato = Candidato.objects.get(id = id)
        if request.method == "POST":
                form = EsperienzaForm(request.POST)
                if form.is_valid():
                    professione = form.cleaned_data["professione"]
                    durata = form.cleaned_data["durata"]
                    u = Esperienza(candidato =candidato, professione=professione, durata=durata)
                    u.save()
                    return HttpResponseRedirect(reverse('upload_esperienze'))
        else:
            form = EsperienzaForm()

        return render(request,'quest/registrazione_utente.html', {'form': form})

def UpdateSecondExpView(request):
        id = 5
        candidato = Candidato.objects.get(id = id)
        if request.method == "POST":
                form = EsperienzaForm(request.POST)
                if form.is_valid():
                    professione = form.cleaned_data["professione"]
                    durata = form.cleaned_data["durata"]
                    u = Esperienza(candidato =candidato, professione=professione, durata=durata)
                    u.save()
                    return HttpResponseRedirect(reverse('upload_esperienze'))
        else:
            form = EsperienzaForm()

        return render(request,'quest/registrazione_utente.html', {'form': form})

def UpdatefirstStudView(request):
        id = 5
        Studio.objects.filter(candidato__id=id).delete()
        candidato = Candidato.objects.get(id = id)
        if request.method == "POST":
                form = StudioForm(request.POST)
                if form.is_valid():
                    titolo = form.cleaned_data["titolo"]
                    u = Studio(candidato =candidato, titolo=titolo)
                    u.save()
                    return HttpResponseRedirect(reverse('upload_studi'))
        else:
            form = StudioForm()

        return render(request,'quest/registrazione_utente.html', {'form': form})

def UpdatesecondStudView(request):
        id = 5
        candidato = Candidato.objects.get(id = id)
        if request.method == "POST":
                form = StudioForm(request.POST)
                if form.is_valid():
                    titolo = form.cleaned_data["titolo"]
                    u = Studio(candidato =candidato, titolo=titolo)
                    u.save()
                    return HttpResponseRedirect(reverse('upload_studi'))
        else:
            form = StudioForm()

        return render(request,'quest/registrazione_utente.html', {'form': form})

def UpdateAnagView(request):
        id = 5
        Anagrafica.objects.filter(candidato__id=id).delete()
        candidato = Candidato.objects.get(id = id)
        if request.method == "POST":
                form = AnagraficaForm(request.POST)
                if form.is_valid():
                    nome = form.cleaned_data["nome"]
                    cognome = form.cleaned_data["cognome"]
                    codicefiscale = form.cleaned_data["codicefiscale"]
                    eta = form.cleaned_data["eta"]
                    gender = form.cleaned_data["gender"]
                    stato = form.cleaned_data["stato"]
                    provincia = form.cleaned_data["provincia"]
                    comune = form.cleaned_data["comune"]
                    u = Anagrafica(candidato =candidato, nome=nome, cognome=cognome, codicefiscale=codicefiscale,
                                eta =eta, gender=gender, stato=stato, provincia=provincia, comune=comune)
                    u.save()
                    return HttpResponseRedirect(reverse('pagina_utente'))
        else:
            form = AnagraficaForm()

        return render(request,'quest/registrazione_utente.html', {'form': form})
