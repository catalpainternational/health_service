from django.contrib import admin

from health_service.models import HealthFacilityType, HealthFacility
from health_service.models import OwnershipType

try:
    # optionally use django_extensions' ForeignKeyAutocompleteAdmin if available
    from django_extensions.admin import ForeignKeyAutocompleteAdmin
except ImportError:
    ForeignKeyAutocompleteAdmin = admin.ModelAdmin


class OwnershipTypeAdmin(admin.ModelAdmin):
    model = OwnershipType


class HealthFacilityTypeAdmin(admin.ModelAdmin):
    model = HealthFacilityType


class HealthFacilityChildrenInline(admin.TabularInline):
    model = HealthFacility
    fields = ['name', 'code', 'type', 'area', 'catchment_areas']
    raw_id_fields = ('area', 'catchment_areas')
    extra = 0
    show_change_link = True


class HealthFacilityAdmin(ForeignKeyAutocompleteAdmin):
    model = HealthFacility
    list_display = ('name', 'code', 'type', 'area', 'parent')
    fields = ['name', 'code', 'type', 'area', 'parent', 'catchment_areas']
    raw_id_fields = ('area', 'catchment_areas')
    list_filter = ('type',)
    search_fields = ['name']
    inlines = [HealthFacilityChildrenInline]
    related_search_fields = {'area': ('^name',),
                             'parent': ('^name',)}


admin.site.register(OwnershipType, OwnershipTypeAdmin)
admin.site.register(HealthFacility, HealthFacilityAdmin)
admin.site.register(HealthFacilityType, HealthFacilityTypeAdmin)
