import json
from django.contrib import admin
from main.models import *
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    list_display = ('name', 'title', 'created_date')
    search_fields = ('name', 'title')
    summernote_fields = ('summary',)


@admin.register(TechnicalSkill)
class TechnicalSkillAdmin(SummernoteModelAdmin):
    list_display = ('title',)
    summernote_fields = ('content',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'degree', 'field')
    search_fields = ('school', 'degree', 'field')


@admin.register(Experience)
class ExperienceAdmin(SummernoteModelAdmin):
    list_display = ('company', 'title')
    summernote_fields = ('task',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization')


@admin.register(SoftSkill)
class SoftSkillAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Honor)
class HonorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Background)
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ('name',)
