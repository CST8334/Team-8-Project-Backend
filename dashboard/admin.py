from django.contrib import admin

from .models import Creator
from .models import Brand
from .models import CreatorYoutubeChannel
from .models import AdCard
from .models import CreatorAdCard

# Register your models here.
admin.site.register(Creator)
admin.site.register(Brand)
admin.site.register(CreatorYoutubeChannel)
admin.site.register(AdCard)
admin.site.register(CreatorAdCard)
