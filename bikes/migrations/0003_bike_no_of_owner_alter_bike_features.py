# Generated by Django 4.0.4 on 2022-04-29 15:56

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0002_alter_bike_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='no_of_owner',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bike',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Disc Break', 'Disc Break'), ('ABS', 'ABS'), ('Power Break', 'Power Break'), ('Fuel Injection', 'Fuel Injection'), ('Dual-Channel ABS', 'Dual-Channel ABS'), ('Rear Lift Prevention', 'Rear Lift Prevention'), ('Adjustable Suspension', 'Adjustable Suspension'), ('Hazard Lights Motorcycle', 'Hazard Lights Motorcycle')], max_length=100),
        ),
    ]
