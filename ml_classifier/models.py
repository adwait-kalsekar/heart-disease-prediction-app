from django.db import models
import uuid

# Create your models here.

class Info(models.Model):
    CATEGORY_TYPE = (
        ('ml', 'Machine Learning'),
        ('eda', 'Visualization'),
        ('eval', 'Evaluation'),
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(max_length=200)
    category = models.CharField(max_length=100, choices=CATEGORY_TYPE)

    def __str__(self):
        return self.name
    

class Prediction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    prediction = models.CharField(max_length=10)
    probability = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name