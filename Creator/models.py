from django.db import models

class creator_product_request(models.Model):
    creator_user_id = models.IntegerField() # Foreign key?
    request_type = models.fields.CharField(max_length=255)
