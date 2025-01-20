from a_common.models import CommonModel

from django.db import models


class Image(CommonModel):
    image_url = models.URLField(verbose_name="이미지 URL")

    class Meta:
        db_table = "images"
        ordering = ["-created_at"]

    def __str__(self):
        return self.image_url
