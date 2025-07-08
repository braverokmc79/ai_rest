from django.contrib import admin

from .models import (
    Article,
    CuisineType,
    Restaurant,
    RestaurantCategory,
    RestaurantImage,
    RestaurantMenu,
    Review,
    ReviewImage,
    SocialChannel,
    Tag,
)

admin.site.register(Article)
admin.site.register(Restaurant)
admin.site.register(CuisineType)
admin.site.register(RestaurantCategory)
admin.site.register(RestaurantImage)
admin.site.register(RestaurantMenu)
admin.site.register(Review)
admin.site.register(ReviewImage)
admin.site.register(SocialChannel)
admin.site.register(Tag)
