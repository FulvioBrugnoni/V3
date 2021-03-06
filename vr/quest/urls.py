from django.urls import path
from quest    import views

urlpatterns = [
                path('1',views.V1,name ='inizio'),
                path('2',views.ProvaView,name ='login_utenti' ),
#                path('3',),
                path('4',views.RegistrationView,name ='registrazione_utenti'),
                path('5',views.RegistrationAnagView,name ='registrazioni_anagrafica'),
                path('6',views.V6,name='ingresso_studi'),
                path('7',views.RegistrationStudView,name ='registrazioni_studi'),
                path('8',views.V8,name='uscita_studi'),
                path('9',views.V9, name ='ingresso_esperienza'),
                path('10',views.RegistrationExpView,name ='registrazioni_esperienze'),
                path('11',views.V11,name='uscita_esperienze'),
                path('12',views.V12,name='ingresso_lingue'),
                path('13',views.RegistrationLangView,name ='registrazioni_lingue'),
                path('14',views.V14,name='uscita_lingue'),
                path('15',views.QuestView,name ='registrazioni_questionari'),
                path('16',views.V16,name ='fine'),
                path('17',views.V17,name ='pagina_utente'),
                path('18',views.UpdatefirstStudView,name ='upload_primo_studi'),
                path('19',views.V19,name ='upload_studi'),
                path('20',views.UpdatesecondStudView,name ='upload_secondo_studi'),
                path('21',views.UpdateFirstExpView,name ='upload_primo_esperienze'),
                path('22',views.V22,name ='upload_esperienze'),
                path('23',views.UpdateSecondExpView,name ='upload_secondo_esperienze'),
                path('24',views.UpdateFirstLangView,name ='upload_primo_lingue'),
                path('25',views.V25,name ='upload_lingue'),
                path('26',views.UpdatesecondLangView,name ='upload_secondo_lingue'),
                path('27',views.UpdateAnagView,name ='upload_anagrafica'),
#                path('28',),
#                path('29',),
#                path('30',),
#                path('31',),
                ]
