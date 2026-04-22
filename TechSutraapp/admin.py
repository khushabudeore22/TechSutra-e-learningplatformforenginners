from django.contrib import admin
from .models import *

admin.site.register(Department)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Resource)
admin.site.register(UserRegistrationData)
admin.site.register(PlatformReview)