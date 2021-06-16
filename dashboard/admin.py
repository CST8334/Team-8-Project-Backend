from django.contrib import admin

from .models import Influencer
from .models import Brand
from .models import InfluencerYoutubeChannel
from .models import AdCard
from .models import InfluencerAdCard

# Register your models here.
admin.site.register(Influencer)
admin.site.register(Brand)
admin.site.register(InfluencerYoutubeChannel)
admin.site.register(AdCard)
admin.site.register(InfluencerAdCard)
