from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.forms import ValidationError


# 게시글(칼럼) 모델
class Article(models.Model):
    title = models.CharField(max_length=100, db_index=True, help_text="게시글 제목")
    preview_image = models.ImageField(
        upload_to="article", null=True, blank=True, help_text="미리보기 이미지"
    )
    content = models.TextField(help_text="본문 내용")
    show_at_index = models.BooleanField(default=False, help_text="메인페이지 노출 여부")
    is_published = models.BooleanField(default=False, help_text="게시 여부")
    created_at = models.DateTimeField("생성일", auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "칼럼(Article)"
        verbose_name_plural = "칼럼(Articles)"

    def __str__(self):
        return f"{self.id} - {self.title}"


# 음식점 모델
class Restaurant(models.Model):
    name = models.CharField(
        "이름", max_length=100, db_index=True, help_text="음식점 이름"
    )
    branch_name = models.CharField(
        "지점", max_length=100, db_index=True, null=True, blank=True, help_text="지점명"
    )
    description = models.TextField(
        "설명", null=True, blank=True, help_text="음식점 설명"
    )
    address = models.CharField("주소", max_length=255, db_index=True, help_text="주소")
    feature = models.CharField("특징", max_length=255, help_text="특징 요약")
    is_closed = models.BooleanField("폐업 여부", default=False)
    latitude = models.DecimalField(
        "위도", max_digits=16, decimal_places=12, db_index=True, default="0.0000"
    )
    longitude = models.DecimalField(
        "경도", max_digits=16, decimal_places=12, db_index=True, default="0.0000"
    )
    phone = models.CharField(
        "전화번호", max_length=16, help_text="E.164 포맷", blank=True, null=True
    )
    rating = models.DecimalField("평점", max_digits=3, decimal_places=2, default="0.0")
    rating_count = models.PositiveIntegerField("평가수", default=0)
    start_time = models.TimeField("영업 시작 시간", null=True, blank=True)
    end_time = models.TimeField("영업 종료 시간", null=True, blank=True)
    last_order_time = models.TimeField("라스트 오더 시간", null=True, blank=True)
    category = models.ForeignKey(
        "RestaurantCategory",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="가게 카테고리",
    )
    tags = models.ManyToManyField("Tag", blank=True, help_text="연결된 태그")

    class Meta:
        verbose_name = "레스토랑(Restaurant)"
        verbose_name_plural = "레스토랑(Restaurants)"

    def __str__(self):
        return f"{self.name} {self.branch_name}" if self.branch_name else f"{self.name}"


# 음식 종류 모델
class CuisineType(models.Model):
    name = models.CharField("이름", max_length=20, help_text="음식 종류명")

    class Meta:
        verbose_name = "음식 종류(CuisineType)"
        verbose_name_plural = "음식 종류(CuisineTypes)"

    def __str__(self):
        return self.name


# 레스토랑 카테고리
class RestaurantCategory(models.Model):
    name = models.CharField("이름", max_length=20, help_text="카테고리명")
    cuisine_type = models.ForeignKey(
        "CuisineType",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="연결된 음식 종류",
    )

    class Meta:
        verbose_name = "가게 카테고리(RestaurantCategory)"
        verbose_name_plural = "가게 카테고리(RestaurantCategories)"

    def __str__(self):
        return self.name


# 레스토랑 이미지 모델
class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, help_text="해당 이미지의 레스토랑"
    )
    is_representative = models.BooleanField("대표 이미지 여부", default=False)
    order = models.PositiveIntegerField("순서", null=True, blank=True)
    name = models.CharField("이름", max_length=100, null=True, blank=True)
    image = models.ImageField("이미지", max_length=100, upload_to="restaurant")
    created_at = models.DateTimeField("생성일", auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField("수정일", auto_now=True, db_index=True)

    class Meta:
        verbose_name = "가게 이미지(RestaurantImage)"
        verbose_name_plural = "가게 이미지(RestaurantImages)"

    def __str__(self):
        return f"{self.id}:{self.image}"

    def clean(self):
        images = self.restaurant.restaurantimage_set.filter(is_representative=True)
        if self.is_representative and images.exclude(id=self.id).count() > 0:
            raise ValidationError("대표 이미지는 1개만 지정 가능합니다.")


# 레스토랑 메뉴 모델
class RestaurantMenu(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, help_text="해당 메뉴의 레스토랑"
    )
    name = models.CharField("이름", max_length=100, help_text="메뉴명")
    price = models.PositiveIntegerField("가격", default=0)
    image = models.ImageField(
        "이미지", upload_to="restaurant-menu", null=True, blank=True
    )
    created_at = models.DateTimeField("생성일", auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField("수정일", auto_now=True, db_index=True)

    class Meta:
        verbose_name = "가게 메뉴(RestaurantMenu)"
        verbose_name_plural = "가게 메뉴(RestaurantMenus)"

    def __str__(self):
        return self.name


# 리뷰 모델
class Review(models.Model):
    title = models.CharField("제목", max_length=100)
    author = models.CharField("작성자", max_length=100)
    profile_image = models.ImageField(
        "프로필 이미지", upload_to="review-profile", blank=True, null=True
    )
    content = models.TextField("내용")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], help_text="1~5점"
    )
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, help_text="대상 음식점"
    )
    social_channel = models.ForeignKey(
        "SocialChannel",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="SNS 채널",
    )
    created_at = models.DateTimeField("생성일", auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField("수정일", auto_now=True, db_index=True)

    class Meta:
        verbose_name = "리뷰(Review)"           # 단수 이름 (관리자 페이지 등에서 사용)
        verbose_name_plural = "리뷰(Reviews)"    # 복수 이름
        ordering = ["-created_at"]      # 기본 정렬: 최신순

    def __str__(self):
        return f"{self.author}:{self.title}"

    @property
    def restaurant_name(self):    #연결된 음식점 객체의 이름만 바로 review.restaurant_name으로 접근 가능
        return self.restaurant.name

    @property
    def content_partial(self):   # Review.content_partial 사용 시 자동으로 잘린 요약 내용이 반환됨
        return self.content[:20]


# 리뷰 이미지
class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, help_text="대상 리뷰")
    name = models.CharField(max_length=100, help_text="이미지 이름")
    image = models.ImageField(max_length=100, upload_to="review")
    created_at = models.DateTimeField("생성일", auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField("수정일", auto_now=True, db_index=True)

    class Meta:
        verbose_name = "리뷰이미지(ReviewImage)"
        verbose_name_plural = "리뷰이미지(ReviewImages)"

    def __str__(self):
        return f"{self.id}:{self.image}"


# SNS 채널
class SocialChannel(models.Model):
    name = models.CharField("이름", max_length=100, help_text="SNS 채널명")

    class Meta:
        verbose_name = "소셜채널(SocialChannel)"
        verbose_name_plural = "소셜채널(SocialChannels)"

    def __str__(self):
        return self.name


# 태그
class Tag(models.Model):
    name = models.CharField("이름", max_length=100, help_text="태그 이름")

    class Meta:
        verbose_name = "태그(Tag)"
        verbose_name_plural = "태그(Tags)"

    def __str__(self):
        return self.name
