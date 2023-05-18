from django.db import models

# Create your models here.
Water = [
        ('Succulents and cacti', 'Succulents and cacti'),
        ('Drought tolerant plants', 'Drought-tolerant plants'),
        ('Moisture loving plants', 'Moisture-loving plants'),
    ]
Sun = [
        ('Full sun plants', 'Full sun plants'),
        ('Partial sun partial shade plants', 'Partial sun/partial shade plants'),
        ('Shade loving plants', 'Shade-loving plants'),
    ]
Soil = [
        ('Neutral soil plants', 'Neutral soil plants'),
        ('Alkaline soil plants', 'Alkaline soil plants'),
        ('Acidic soil plants', 'Acidic soil plants'),
    ]
leaf_type = [
        ('Flat leaves', 'Flat leaves'),
        ('Curly leaves', 'Curly leaves'),
        ('Serrated leaves', 'Serrated leaves'),
        ('Semi circular leaves', 'Semi-circular leaves'),
        ('Triangular leaves', 'Triangular leaves'),
        ('Variegated leaves', 'Variegated leaves'),
        ('Tree leaves', 'Tree leaves'),
        ('Dark green leaves', 'Dark green leaves'),
        ('Ascending leaves', 'Ascending leaves'),
        ('Circular leaves', 'Circular leaves'),
    ]



class Plants(models.Model):
    scientific_name  = models.CharField(max_length=200)
    home  = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    water = models.CharField(max_length=200, choices=Water)
    sun = models.CharField(max_length=200, choices=Sun)
    soil = models.CharField(max_length=200, choices=Soil)
    leaf_type = models.CharField(max_length=200, choices=leaf_type)
    image = models.ImageField(upload_to='static/images')


    def __str__(self):
        return self.scientific_name
