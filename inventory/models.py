from statistics import mode
from django.db import models
from django.db.models import QuerySet
from django.utils import timezone

# Create your models here.
class BaseModelQuerySet(QuerySet):
    """
    Prevents objects from being hard-deleted. Instead, sets the
    ``date_deleted``, effectively soft-deleting the object.
    """

    def soft_delete(self):
        for obj in self:
            obj.is_delete = True
            obj.deleted_on = timezone.now()
            obj.save()

    def undelete(self):
        for obj in self:
            obj.is_delete = False
            obj.deleted_on = None
            obj.save()


class BaseModelManager(models.Manager):
    """
    Only exposes objects that have NOT been soft-deleted.
    """

    def get_queryset(self):
        return BaseModelQuerySet(self.model, using=self._db).filter(
            deleted_on__isnull=True
        )

class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(null=True, blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    objects = BaseModelManager()
    original_objects = models.Manager()

    def soft_delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.deleted_on = timezone.now()
        self.save()

    def undelete(self):
        self.is_delete = False
        self.deleted_on = None
        self.save()

class Supplier(BaseModel):
    name = models.CharField(null=False, max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"

class Inventory(BaseModel):
    name = models.CharField(null=False, max_length=100)
    description = models.CharField(null=True, blank=True, max_length=100)
    note = models.TextField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    availability = models.BooleanField(default=False)
    supplier = models.ManyToManyField(
        Supplier, 
        blank=True,
        related_name='supplier'
    )

    def __str__(self) -> str:
        return f"{self.name}"
