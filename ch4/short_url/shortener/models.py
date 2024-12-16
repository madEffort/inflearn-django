import random
import string

from django.db import models


class ShortURL(models.Model):
    code = models.CharField(max_length=8, unique=True, db_index=True)
    original_url = models.URLField(max_length=200)
    access_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "shortener"
        db_table = "short_url"

    @staticmethod
    def generate_code():
        characters = string.ascii_letters + string.digits  # 대소문자 알파벳 + 숫자
        return ''.join(random.choices(characters, k=8))
