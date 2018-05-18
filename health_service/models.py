from django.db import models
from django.utils.translation import ugettext_lazy as _

from simple_locations.models import Area, Point


class OwnershipType(models.Model):
    """
    i.e. the health facility may be public, private, NGO, faith-based
    """

    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = _("Ownership Type")
        verbose_name_plural = _("Ownership Types")
        app_label = 'health_service'

    def __unicode__(self):
        return self.name


class HealthFacilityType(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = _("Health Facility Type")
        verbose_name_plural = _("Health Facility Types")
        app_label = 'health_service'

    def __unicode__(self):
        return self.name


class HealthFacility(models.Model):
    ownership_type = models.ForeignKey(OwnershipType, blank=True, null=True)
    location = models.ForeignKey(Point, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='facility')
    catchment_areas = models.ManyToManyField(Area, related_name='catchment+')
    area = models.ForeignKey(Area, null=True, blank=True, related_name='healthfacility',)

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=64, blank=True, null=False)
    type = models.ForeignKey(HealthFacilityType, blank=True, null=True)

    class Meta:
        verbose_name = _("Health Facility")
        verbose_name_plural = _("Health Facilities")
        app_label = 'health_service'

    def __unicode__(self):
        return u"%s %s" % (self.type, self.name)

    def is_root(self):
        if self.parent is None:
            return True
        else:
            return False

    def get_children(self):
        children = self._default_manager.filter(parent=self)
        return children

    def get_descendants(self):
        descendants = children = self.get_children()

        for child in children:
            if child.has_children:
                descendants = descendants | child.descendants
        return descendants

    def get_ancestors(self):
        ancestors = self._default_manager.none()
        facility = self.parent
        while facility.is_child_node:
            ancestors = ancestors | self._default_manager.filter(pk=facility.pk)
            facility = facility.parent
        return ancestors

    @property
    def is_child_node(self):
        if self.parent:
            return True
        else:
            return False

    @property
    def has_children(self):
        children = self._default_manager.filter(parent=self).count()
        if children > 0:
            return True
        else:
            return False

    @property
    def children(self):
        return self.get_children()

    @property
    def descendants(self):
        return self.get_descendants()

    @property
    def ancestors(self):
        return self.get_ancestors()
