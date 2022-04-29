from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.db.models import BigAutoField



class bike(models.Model):
    state_choice = (
    ('AP','Andhra Pradesh'),
    ('AR','Arunachal Pradesh'),
    ('AS','Assam'),
    ('BR','Bihar'),
    ('CG','Chhattisgarh'),
    ('GA','Goa'),
    ('GJ','Gujarat'),
    ('HR','Haryana'),
    ('HP','Himachal Pradesh'),
    ('JK','Jammu and Kashmir'),
    ('JH','Jharkhand'),
    ('KA','Karnataka'),	
    ('KL','Kerala'),
    ('MP','Madhya Pradesh'),
    ('MH','Maharashtra'),
    ('MN','Manipur'),
    ('ML','Meghalaya'),
    ('MZ','Mizoram'),
    ('NL','Nagaland'),
    ('OD','Odisha'),
    ('PB','Punjab'),
    ('RJ','Rajasthan'),	
    ('SK','Sikkim'),
    ('TN','Tamil Nadu'),	
    ('TS','Telangana'),	
    ('TR','Tripura'),
    ('UP','Uttar Pradesh'),
    ('UK','Uttarakhand'),
    ('WB','West Bengal'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
        ('Disc Break', 'Disc Break'),
        ('ABS', 'ABS'),
        ('Power Break', 'Power Break'),
        ('Fuel Injection', 'Fuel Injection'),
        ('Dual-Channel ABS', 'Dual-Channel ABS'),
        ('Rear Lift Prevention', 'Rear Lift Prevention'),
        ('Adjustable Suspension', 'Adjustable Suspension'),
        ('Hazard Lights Motorcycle', 'Hazard Lights Motorcycle'),
    )
    bike_title = models.CharField(max_length=100)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'),choices=year_choice)
    price = models.IntegerField()
    color = models.CharField(max_length=100)
    description = RichTextField()
    bike_photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    bike_photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    bike_photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    bike_photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices, max_length=100)
    miles = models.IntegerField()
    vih_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    no_of_owner = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.bike_title