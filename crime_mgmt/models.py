from django.db import models

# Create your models here.
class my_user(models.Model):
    user_type = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, primary_key=True, null=False)
    password = models.CharField(max_length=16,null=False)

    def __str__(self):
        return self.user_name

class police_station(models.Model):
    police_station_name = models.CharField(max_length=50)
    police_station_code = models.CharField(max_length=50,primary_key=True)
    creation_date = models.DateField()

    def __str__(self):
        return self.police_station_code + " " + self.police_station_name

class police(models.Model):
    police_station_code = models.ForeignKey(police_station, on_delete=models.CASCADE)
    police_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    mobile_number = models.BigIntegerField()
    Address = models.TextField()
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.police_id + " " + self.name

class crime_category(models.Model):
    category_name = models.CharField(max_length=100, primary_key=True)
    category_desc = models.TextField()
    creation_date = models.DateField()

    def __str__(self):
        return self.category_name

class criminal(models.Model):
    police_station = models.ForeignKey(police_station, on_delete=models.CASCADE)
    crime_type = models.ForeignKey(crime_category, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    prison = models.CharField(max_length=100)
    court = models.CharField(max_length=100)
    id = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=50)
    number = models.BigIntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    dob = models.DateField()
    email = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    pincode = models.IntegerField()

    photo = models.FileField(upload_to="media/",max_length=500,null=True,default=None)

    def __str__(self):
        return self.id + " " + self.name

class fir(models.Model):
    FIR_no = models.CharField(max_length=100)
    police_station = models.ForeignKey(police_station, on_delete=models.CASCADE)
    crime_type = models.ForeignKey(crime_category, on_delete=models.CASCADE)
    accused_name = models.CharField(max_length=50)
    applicant_name = models.CharField(max_length=50)
    parentage = models.CharField(max_length=100)
    number = models.BigIntegerField()
    address = models.TextField()
    relation_with_accussed = models.CharField(max_length=100)
    purpose = models.TextField()
    fir_date = models.DateField()
    final_status = models.CharField(max_length=50, default=None)
    police_remark = models.TextField(default=None)
    police_date = models.DateField(default=None)
    section_of_law = models.CharField(max_length=100,default=None)
    investigation_officer_name = models.CharField(max_length=100,default=None)
    investigation_details = models.TextField(default=None)

    def __str__(self):
        return self.FIR_no

