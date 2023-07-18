from django.contrib import admin
from crime_mgmt.models import police_station,my_user, police, crime_category,criminal,fir

class user_admin(admin.ModelAdmin):
    list_display = ('user_type','user_name','password')


class police_station_admin(admin.ModelAdmin):
    list_display = ('police_station_name','police_station_code','creation_date')

# class police_admin(admin.ModelAdmin):
#     list_display= ('police_station_code', 'police_id', 'name', 'email', 'mobile_number', 'address', 'password')


admin.site.register(my_user,user_admin)
admin.site.register(police_station, police_station_admin)
admin.site.register(police)
admin.site.register(crime_category)
admin.site.register(criminal)
admin.site.register(fir)
