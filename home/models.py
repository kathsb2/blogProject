from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):

    uid = models.UUIDField(primary_key=True, editable=False, default = uuid.uuid4)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Blog(BaseModel):
    title = models.CharField(max_length=500)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "blogs")
    hero_image = models.ImageField(upload_to = "blogs",  null=True)

    def __str__(self) -> str:
        return self.title

class Comment(BaseModel):
    user = models.ForeignKey(User, related_name = 'comments', on_delete = models.CASCADE)
    post = models.ForeignKey(Blog, related_name = 'comments', on_delete = models.CASCADE)
    body = models.TextField()

    def __str__(self) -> str:
        return self.body

