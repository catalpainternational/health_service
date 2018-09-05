from django.contrib import admin
from django.urls import resolve

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
    fields = ['name', 'code', 'type', 'ownership_type', 'catchment_areas', 'location', 'area', ]
    raw_id_fields = ('ownership_type', 'catchment_areas', 'location', 'area', 'type',)
    extra = 1
    show_change_link = True

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        resolved = resolve(request.path_info)
        if resolved.args:
            parent = self.parent_model.objects.get(pk=resolved.args[0])
            kwargs['queryset'] = parent.get_children()  # or any queryset based on parent's attributes
            return super(HealthFacilityChildrenInline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class HealthFacilityAdmin(ForeignKeyAutocompleteAdmin):
    model = HealthFacility
    list_display = ('name', 'code', 'type', 'area', 'parent',)
    fields = ['name', 'code', 'type', 'area', 'parent',]
    list_filter = ('type',)
    search_fields = ['name',]
    inlines = [HealthFacilityChildrenInline]
    related_search_fields = {'area': ('^name',),
                             'parent': ('^name',),}


admin.site.register(OwnershipType, OwnershipTypeAdmin)
admin.site.register(HealthFacility, HealthFacilityAdmin)
admin.site.register(HealthFacilityType, HealthFacilityTypeAdmin)
