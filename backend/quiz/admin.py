from django.contrib import admin

from .models import Question, Choice, Quiz


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline,]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Quiz)
