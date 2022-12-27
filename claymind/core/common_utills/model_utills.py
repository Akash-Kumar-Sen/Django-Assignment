import uuid
from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE

class BaseModel(SafeDeleteModel):
    """Base model for safedelete from admin panel
    """
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta(object):
        """this is an abstract model
        """
        abstract = True  # this is an abstract model

    def is_deleted(self, *args, **kwargs):
        """creating is_deleted param
        """
        return self.deleted is not None

class TimeStampedModel(BaseModel):
    '''
    Base model that stores created_at and modified_at
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        """this is an abstract model
        """
        abstract = True


class UUIDTimeStampedModel(TimeStampedModel):
    '''
    Base model that stores created_at, modified_at, and id (which is
    a uuid string).
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta(object):
        """this is an abstract model
        """
        abstract = True 
