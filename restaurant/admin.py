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


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "show_at_index",
        "is_published",
        "created_at",
        "modified_at",
    ]
    fields = ["title", "preview_image", "content", "show_at_index", "is_published"]
    search_fields = ["title"]
    list_filter = ["show_at_index", "is_published"]
    date_hierarchy = "created_at"
    actions = ["make_published"]

    @admin.action(description="선택한 컬럼을 공개상태로 변경합니다.")
    def make_published(self, request, queryset):
        queryset.update(is_published=True)


class RestaurantMenuInline(admin.TabularInline):
    model = RestaurantMenu
    extra = 1


class RestaurantImageInline(admin.TabularInline):
    model = RestaurantImage
    extra = 1


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "branch_name",
        "is_closed",
        "phone",
        "rating",
        "rating_count",
    ]
    fields = [
        "name",
        "branch_name",
        "category",
        "is_closed",
        "phone",
        "latitude",
        "longitude",
        "tags",
    ]
    readonly_fields = ["rating", "rating_count"]
    search_fields = ["name", "branch_name", "tags__name"]
    list_filter = ["tags"]
    autocomplete_fields = ["tags"]
    inlines = [RestaurantMenuInline, RestaurantImageInline]

    def get_inline_instances(self, request, obj=None):
        return super().get_inline_instances(request, obj) if obj else []


@admin.register(RestaurantCategory)
class RestaurantCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    fields = ["cuisine_type", "name"]


class ReviewImageInline(admin.TabularInline):
    model = ReviewImage
    extra = 1


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "restaurant_name", "author", "rating", "content_partial"]
    inlines = [ReviewImageInline]

    def get_inline_instances(self, request, obj=None):
        return super().get_inline_instances(request, obj) if obj else []


@admin.register(SocialChannel)
class SocialChannelAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    fields = ["name"]


# 등록만 필요한 모델은 아래처럼 한 줄로 간단히
admin.site.register(CuisineType)


# admin.py

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]  # autocomplete_fields에 필요함






admin.site.register(RestaurantImage)
admin.site.register(RestaurantMenu)
admin.site.register(ReviewImage)
