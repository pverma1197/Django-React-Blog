import uuid
from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
# class BaseModelUuid(models.Model):
#     class Meta:
#         abstract = True
#     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#
#
# class BaseModel(BaseModelUuid):
#     class Meta:
#         abstract = True

class Blog(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    heading = models.CharField(max_length=100)
    article = models.TextField()
    image = models.ImageField(upload_to='blogimg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = ArrayField(models.CharField(max_length=50), null=True)
