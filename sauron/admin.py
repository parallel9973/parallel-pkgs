from django.contrib import admin
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .views import *
from django.urls import reverse

admin.site.register(DonwloadFileModel)
admin.site.register(ResultFileModel)