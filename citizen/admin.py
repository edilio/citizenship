from django.contrib import admin

from .models import Category, Question, Answer

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('index', 'name')
    list_display_links = ('index', 'name')


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('index', 'category', 'question', 'answers')
    list_display_links = ('index', 'category', 'question')
    list_filter = ('category', )
    search_fields = ('question', )

    inlines = [AnswerInline]