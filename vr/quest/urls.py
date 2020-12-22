from django.urls import path
from quest    import views

urlpatterns = [ path('cf',views.Final),
                path('cc/<parametro>',views.RegistrationView),
                path('ca',views.RegistrationAnagView),
                path('cs',views.RegistrationStudView),
                path('cl',views.RegistrationLangView),
                path('ce',views.RegistrationExpView),
                path('completaquest',views.QuestView),
                path('prova',views.ProvaView),
                path('ufl',views.UpdateFirstLangView),
                path('usl',views.UpdatesecondLangView),
                path('rsc',views.RiassuntoCandidato),
                path('ufs',views.UpdatefirstStudView),
                path('uss',views.UpdatesecondStudView),
                path('ufe',views.UpdateFirstExpView),
                path('use',views.UpdateSecondExpView),
                path('ufa',views.UpdateAnagView),
                ]
