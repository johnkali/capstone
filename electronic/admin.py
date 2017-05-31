from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'second_name',
        'third_name',
        'id_number',
        'district_of_birth',
        'date_of_birth',
        'gender',
    )
    list_display_links = ('first_name',)


admin.site.register(Person, PersonAdmin)
