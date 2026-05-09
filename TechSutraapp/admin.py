from django.contrib import admin
from .models import *


admin.site.register(Department)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Resource)
admin.site.register(UserRegistrationData)
admin.site.register(PlatformReview)


@admin.register(VideoLecture)
class VideoLectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'get_department', 'uploaded_by', 'created_at')
    list_filter = ('subject__semester__department', 'subject', 'created_at')
    search_fields = ('title', 'description', 'subject__name')
    ordering = ('-created_at',)

    def get_department(self, obj):
        return obj.subject.semester.department.name
    get_department.short_description = 'Department'