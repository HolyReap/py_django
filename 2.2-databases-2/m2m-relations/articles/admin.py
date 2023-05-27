from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


    
class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        check = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data['is_main']:
                check += 1
        if check == 0:
            raise ValidationError('Укажите основной Тэг')
        if check > 1:
            raise ValidationError('Допускается один основной Тэг')
        # check = [f.cleaned_data['is_main'] for f in self.forms if f.cleaned_data['is_main']]
        # print(check)
        # if len(check) == 0:
        #     raise ValidationError('Укажите основной Тэг')
        # if len(check) > 1:
        #     raise ValidationError('Допускается один основной Тэг')
        return super().clean()  # вызываем базовый код переопределяемого метода

class ArtTagInline(admin.TabularInline):
    model = Scope
    extra = 0
    inlines = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','text','published_at','image']
    inlines = [ArtTagInline]


@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    
@admin.register(Scope)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article','tag','is_main']