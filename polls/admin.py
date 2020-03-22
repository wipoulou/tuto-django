from django.contrib import admin
from polls.models import *

admin.site.register(Question)
admin.site.register(Choice)
