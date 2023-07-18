from django.contrib import admin
from django.urls import path,include
from crime_mgmt import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('login/<type>',views.login,name='login'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('police_dashboard/',views.police_dashboard,name='police_dashboard'),
    path('user_dashboard/',views.user_dashboard,name='user_dashboard'),

    # Police station menu urls
    path('add_police_station/',views.add_police_station,name='add_police_station'),
    path('add_police_station/<detail>',views.add_police_station_data,name='add_police_station_data'),
    path('manage_police_station/',views.manage_police_station,name='manage_police_station'),

    # Police menu urls
    path('add_police/',views.add_police,name='add_police'),
    path('add_police/<detail>',views.add_police_data,name='add_police_data'),
    path('manage_police/',views.manage_police,name='manage_police'),

    #Crime category urls
    path('add_crime_category/',views.add_crime_category,name='add_crime_category'),
    path('manage_crime_category/',views.manage_crime_category,name='manage_crime_category'),
    path('update_crime_category/',views.update_crime_category,name='update_crime_category'),

    # Criminal urls
    path('add_criminals/',views.add_criminals,name='add_criminals'),
    path('manage_criminals/',views.manage_criminals,name='manage_criminals'),
    path('update_criminals/<type>',views.update_criminals,name='update_criminals'),

    # fir form
    path('fir_form/',views.fir_form,name='fir_form'),
    path('fir_history/',views.fir_history,name='fir_history'),
    path('fir_details/',views.fir_details,name='fir_details'),
    path('user_chargesheet/',views.user_chargesheet,name='user_chargesheet'),
    path('police_fir/',views.police_fir,name='police_fir'),
    path('police_chargesheet/',views.police_chargesheet,name='police_chargesheet')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)