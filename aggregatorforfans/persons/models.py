from django.db import models

# Create your models here.


class Person(models.Model):
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    GENDER_LIST = (
        ("F", "Female"),
        ("M", "Male"),
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_LIST, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    RACE_LIST = (
        ("A", "Asian"),
        ("B", "Black"),
        ("I", "Indian"),
        ("L", "Latino"),
        ("M", "Middle Eastern"),
        ("W", "White"),
    )
    race = models.CharField(
        max_length=1, choices=RACE_LIST, blank=True, null=True)

    def __str__(self):
        return self.name


class Link(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    website = models.URLField(blank=True, null=True, max_length=255)
    instagram = models.URLField(blank=True, null=True, max_length=255)
    twitter = models.URLField(blank=True, null=True, max_length=255)

    def __str__(self):
        return self.person.name + " links"


class Movie(models.Model):
    person = models.ManyToManyField(Person)
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=255)

    def __str__(self):
        return self.title
