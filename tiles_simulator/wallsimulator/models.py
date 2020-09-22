from django.db import models

# Create your models here.
class WallTiles_18_12_Model(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    tile_number = models.CharField(max_length=128)
    light_image_url = models.CharField(max_length=1024)
    high_lighter_1_image_url = models.CharField(max_length=1024)
    high_lighter_2_image_url = models.CharField(max_length=1024, null=True, blank=True)
    high_lighter_3_image_url = models.CharField(max_length=1024, null=True, blank=True)
    dark_image_url = models.CharField(max_length=1024)
