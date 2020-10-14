from django.contrib import admin

# Register your models here.

from .models import Person, Link, Movie

admin.site.register(Person)
admin.site.register(Link)
admin.site.register(Movie)
