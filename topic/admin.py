from django.contrib import admin

# Register your models here.
from .models import Question, Answer, Theme

admin.site.register(Theme)
admin.site.register(Question)
admin.site.register(Answer)
