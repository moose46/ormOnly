from django.db import models




class Base(models.Model):
    created_at = models.DateTimeField("createdAt",auto_now_add=True)
    updatedAt = models.DateTimeField("updatedAt", auto_now=True )

    class Meta:
        abstract = True


# Create your models here.
class Track(Base):
    name = models.CharField(
        max_length=50,
        blank=False
    )
    length = models.IntegerField()
    configuration = models.CharField(max_length=50,
        blank=False,default='n/a'
    )
    id = models.BigAutoField(
        primary_key=True
    )
    class Meta:
        constraints = [models.UniqueConstraint(fields=['name'], name='unique_name')]