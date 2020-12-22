from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from quest.models import *
from django.core.exceptions import ObjectDoesNotExist

def Final(request):
        return render(request,'quest/cf.html')

def RegistrationView(request, parametro):
        if request.method == "POST":
                form = CandidatoForm(request.POST)
                if form.is_valid():
                    candidato = form.cleaned_data["user"]
                    u = Candidato(user =candidato)
                    u.save()
                    candidato = Candidato.objects.all().order_by("-id")[0]
                    p = Parametro(candidato = candidato, parametro=parametro)
                    p.save()
                    return HttpResponseRedirect("/ca")
        else:
            form = CandidatoForm()

        return render(request,'quest/cc.html', {'form': form})


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
                    return HttpResponseRedirect("/cs")
        else:
            form = AnagraficaForm()

        return render(request,'quest/ca.html', {'form': form})


def RegistrationStudView(request):
        candidato = Candidato.objects.all().order_by("-id")[0]
        if request.method == "POST":
                form = StudioForm(request.POST)
                if form.is_valid():
                    titolo = form.cleaned_data["titolo"]
                    u = Studio(candidato =candidato, titolo=titolo)
                    u.save()
                    return HttpResponseRedirect("/cs")
        else:
            form = StudioForm()

        return render(request,'quest/cs.html', {'form': form})

def RegistrationExpView(request):
        candidato = Candidato.objects.all().order_by("-id")[0]
        if request.method == "POST":
                form = EsperienzaForm(request.POST)
                if form.is_valid():
                    professione = form.cleaned_data["professione"]
                    durata = form.cleaned_data["durata"]
                    u = Esperienza(candidato =candidato, professione=professione, durata=durata)
                    u.save()
                    return HttpResponseRedirect("/ce")
        else:
            form = EsperienzaForm()

        return render(request,'quest/ce.html', {'form': form})

def RegistrationLangView(request):
        candidato = Candidato.objects.all().order_by("-id")[0]
        if request.method == "POST":
                form = LinguaForm(request.POST)
                if form.is_valid():
                    lingua = form.cleaned_data["lingua"]
                    livello = form.cleaned_data["livello"]
                    u = Lingua(candidato =candidato, lingua=lingua, livello=livello)
                    u.save()
                    return HttpResponseRedirect("/cl")
        else:
            form = LinguaForm()

        return render(request,'quest/cl.html', {'form': form})


def ProvaView(request):
        query = Risposta.objects.filter(utente__id = 5).order_by('-domanda__posizione').first()
        print(query.domanda)
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
                    return HttpResponseRedirect("/cf")
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
                    return HttpResponseRedirect("/cf")

            form = QuestionForm(initial={'questionario':questionario.id, 'domanda': questionario_domanda.domanda.id })

        return render(request,'quest/inserimento_questionario.html', {'form': form, 'testo_domanda':questionario_domanda.domanda.testo})

#---------------------------------------------------------------------------------------------------------------------------------------------------------

def RiassuntoCandidato(request):
        return render(request,'quest/riassunto_candidato.html')


def UpdateFirstLangView(request):
        id = 5
        Lingua.objects.filter(candidato__id=id).delete()
        candidato = Candidato.objects.get(id = id)
        if request.method == "POST":
                form = LinguaForm(request.POST)
                if form.is_valid():
                    lingua = form.cleaned_data["lingua"]
                    livello = form.cleaned_data["livello"]
                    u = Lingua(candidato =candidato, lingua=lingua, livello=livello)
                    u.save()
                    return HttpResponseRedirect("/usl")
        else:
            form = LinguaForm()

        return render(request,'quest/ufl.html', {'form': form})

def UpdatesecondLangView(request):
        id = 5
        candidato = Candidato.objects.get(id = id)
        if request.method == "POST":
                form = LinguaForm(request.POST)
                if form.is_valid():
                    lingua = form.cleaned_data["lingua"]
                    livello = form.cleaned_data["livello"]
                    u = Lingua(candidato =candidato, lingua=lingua, livello=livello)
                    u.save()
                    return HttpResponseRedirect("/usl")
        else:
            form = LinguaForm()

        return render(request,'quest/usl.html', {'form': form})


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
                    return HttpResponseRedirect("/use")
        else:
            form = EsperienzaForm()

        return render(request,'quest/ufe.html', {'form': form})

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
                    return HttpResponseRedirect("/use")
        else:
            form = EsperienzaForm()

        return render(request,'quest/use.html', {'form': form})

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
                    return HttpResponseRedirect("/uss")
        else:
            form = StudioForm()

        return render(request,'quest/ufs.html', {'form': form})

def UpdatesecondStudView(request):
        id = 5
        candidato = Candidato.objects.get(id = id)
        if request.method == "POST":
                form = StudioForm(request.POST)
                if form.is_valid():
                    titolo = form.cleaned_data["titolo"]
                    u = Studio(candidato =candidato, titolo=titolo)
                    u.save()
                    return HttpResponseRedirect("/uss")
        else:
            form = StudioForm()

        return render(request,'quest/uss.html', {'form': form})

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
                    return HttpResponseRedirect("/rsc")
        else:
            form = AnagraficaForm()

        return render(request,'quest/ua.html', {'form': form})
