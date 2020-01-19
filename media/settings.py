from django.conf import settings
from settings import os

# Media config
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(settings.BASE_DIR, "media")
