from core.models import PersonData
from import_export import resources

class PersonDataResource(resources.ModelResource):

    class Meta:
        model = PersonData