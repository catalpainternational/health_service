from modeltranslation.translator import translator, TranslationOptions
from .models import HealthFacilityType


@translator.register(HealthFacilityType)
class HealthFacilityTypeTranslationOptions(TranslationOptions):
    fields = ('name', )
