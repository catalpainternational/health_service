from django.contrib import admin

from health_service.models import HealthFacilityType, HealthFacility
from health_service.models import OwnershipType
from health_service.lib.autocomplete_admin import FkAutocompleteAdmin


class OwnershipTypeAdmin(admin.ModelAdmin):
    model = OwnershipType


class HealthFacilityTypeAdmin(admin.ModelAdmin):
    model = HealthFacilityType


class HealthFacilityAdmin(FkAutocompleteAdmin):
    model = HealthFacility
    fields = ['name', 'code', 'type', 'area', 'parent',]
    list_filter = ('type',)
    search_fields = ['name',]
    related_search_fields = {'area': ('^name',),
                             'parent': ('^name',),}


admin.site.register(OwnershipType, OwnershipTypeAdmin)
admin.site.register(HealthFacility, HealthFacilityAdmin)
admin.site.register(HealthFacilityType, HealthFacilityTypeAdmin)
