from django.urls import path
from quest    import views

urlpatterns = [
                path('1',views.V1),
#                path('2',),
#                path('3',),
                path('4',views.RegistrationView),
                path('5',views.RegistrationAnagView),
                path('6',views.V6),
                path('7',views.RegistrationStudView),
                path('8',views.V8),
                path('9',views.V9),
                path('10',views.RegistrationExpView),
                path('11',views.V11),
                path('12',views.V12),
                path('13',views.RegistrationLangView),
                path('14',views.V14),
                path('15',views.QuestView),
                path('16',views.V16),
                path('17',views.V17),
                path('18',views.UpdatefirstStudView),
                path('19',views.V19),
                path('20',views.UpdatesecondStudView),
                path('21',views.UpdateFirstExpView),
                path('22',views.V22),
                path('23',views.UpdateSecondExpView),
                path('24',views.UpdateFirstLangView),
                path('25',views.V25),
                path('26',views.UpdatesecondLangView),
                path('27',views.UpdateAnagView),
#                path('28',),
#                path('29',),
#                path('30',),
#                path('31',),
                ]
