from django.db import models


class Image(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    uploaded_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
