from django.core.files.base import ContentFile
from django.test import TestCase
from django.db import IntegrityError

from restaurant.models import (
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
    Region,
)



class ArticleModelTest(TestCase):
# 테스트 클래스에서 한 번만 실행되는 메서드로, DB에 Article 객체 1개 생성
# preview_image 필드에는 PNG 파일 바이트를 ContentFile로 임시 저장

	# 테스트 메서드마다 새로운 DB 환경에서 실행됩니다.
    @classmethod # 테스트 클래스 전체에서 1번만 실행
    def setUpTestData(cls):
    # self는 인스턴스 자신이면 cls은 클래스 자신을 뜻함
    # self같이 테스트 클래스 자체를 의미하며 반드시 사용해야함

        # Article 객체 1개를 생성 (이미지 포함)
        cls.article = Article.objects.create( # INSERT쿼리
            title="테스트 칼럼 제목",
            content="테스트 칼럼 내용",
            preview_image=ContentFile(
            
        # PNG 이미지 파일이 시작될 때 반드시 포함되는 고유한 바이트 시퀀스
        # 파일 포맷 시그니처라고 검색하면 아래와 같은 Hex를 확인할수 있음
                b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A", 
                name="test-image.png"
            ),
            show_at_index=True,
            is_published=True,
        )

    def test_content(self):
# 저장된 Article 필드값이 예상대로 설정되었는지 확인
# self.article에 저장된 데이터를 꺼내서,
# title, content, show_at_index, is_published 값이 정확한지 검증
# 이미지가 article/test-image 경로로 저장되었는지 확인

        expected_data = self.article
        
        # 두 값이 같은지 확인(비교)"하는 검증 도구
        self.assertEqual(expected_data.title, "테스트 칼럼 제목")
        self.assertEqual(expected_data.content, "테스트 칼럼 내용")
        self.assertEqual(expected_data.show_at_index, True)
        self.assertEqual(expected_data.is_published, True)
        self.assertTrue(            expected_data.preview_image.name.startswith("article/test-image")
        )


class RestaurantModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):


        # Restaurant 객체 1개 생성
        cls.restaurant = Restaurant.objects.create(
            name="테스트 식당",
            address="서울시 강남구 역삼동 123-456",
            phone="+82212345678",
            description="테스트 식당 설명",
            latitude=37.123456,
            longitude=127.123456,
            rating=4.5,
            rating_count=1_000,
            is_closed=True,
        )

    def test_content(self):


        # 필드 값이 정확히 저장되었는지 확인
        expected_data = self.restaurant
        self.assertEqual(expected_data.name, "테스트 식당")
        self.assertEqual(expected_data.address, "서울시 강남구 역삼동 123-456")
        self.assertEqual(expected_data.phone, "+82212345678")
        self.assertEqual(expected_data.description, "테스트 식당 설명")
        self.assertAlmostEqual(float(expected_data.latitude), 37.123456)
        self.assertAlmostEqual(float(expected_data.longitude), 127.123456)
        self.assertEqual(expected_data.rating, 4.5)
        self.assertEqual(expected_data.rating_count, 1_000)
        self.assertEqual(expected_data.is_closed, True)


class CuisineTypeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CuisineType.objects.create(name="한식")

    def test_content(self):
        cuisine_type = CuisineType.objects.get(id=1) # SELECT 쿼리
        self.assertEqual(cuisine_type.name, "한식")



class RestaurantCategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        RestaurantCategory.objects.create(name="카페")

    def test_content(self):
        restaurant_category = RestaurantCategory.objects.get(id=1)
        self.assertEqual(restaurant_category.name, "카페")



class RestaurantImageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 식당 객체와 이미지 객체를 연결
        restaurant = Restaurant.objects.create(name="테스트 식당")
        RestaurantImage.objects.create(
            restaurant=restaurant,
            image=ContentFile(
                b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A", name="test-image.png"
            ),
        )

    def test_content(self):
        restaurant_image = RestaurantImage.objects.get(id=1)
        self.assertEqual(restaurant_image.restaurant.name, "테스트 식당")
        self.assertTrue(restaurant_image.image.name.startswith("restaurant/test-image"))



class RestaurantMenuModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        restaurant = Restaurant.objects.create(name="테스트 식당")
        RestaurantMenu.objects.create(
            restaurant=restaurant,
            name="테스트 메뉴",
            price=15_000,
        )

    def test_content(self):
        restaurant_menu = RestaurantMenu.objects.get(id=1)
        self.assertEqual(restaurant_menu.restaurant.name, "테스트 식당")
        self.assertEqual(restaurant_menu.name, "테스트 메뉴")
        self.assertEqual(restaurant_menu.price, 15_000)



class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.restaurant = Restaurant.objects.create(name="테스트 식당")
        cls.review = Review.objects.create(
            restaurant=cls.restaurant,
            rating=4,
            content="테스트 리뷰 내용",
        )

    def test_content(self):
        self.assertEqual(self.review.restaurant.name, "테스트 식당")
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(self.review.content, "테스트 리뷰 내용")



class ReviewImageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        restaurant = Restaurant.objects.create(name="테스트 식당")
        review = Review.objects.create(
            restaurant=restaurant,
            rating=4,
            content="테스트 리뷰 내용",
        )
        ReviewImage.objects.create(
            review=review,
            image=ContentFile(
                b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A", name="test-image.png"
            ),
        )

    def test_content(self):
        review_image = ReviewImage.objects.get(id=1)
        self.assertEqual(review_image.review.restaurant.name, "테스트 식당")
        self.assertTrue(review_image.image.name.startswith("review/test-image"))


class SocialChannelModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        SocialChannel.objects.create(name="Instagram")

    def test_content(self):
        social_channel = SocialChannel.objects.get(id=1)
        self.assertEqual(social_channel.name, "Instagram")



class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name="맛집")

    def test_content(self):
        tag = Tag.objects.get(id=1)
        self.assertEqual(tag.name, "맛집")


class RegionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 정상적인 지역 데이터 1건 생성
        cls.region = Region.objects.create(
            sido="서울특별시",
            sigungu="강남구",
            eupmyeondong="역삼동",
        )

    def test_content(self):
        """정상적으로 필드값이 저장되는지 확인"""
        expected = self.region
        self.assertEqual(expected.sido, "서울특별시")
        self.assertEqual(expected.sigungu, "강남구")
        self.assertEqual(expected.eupmyeondong, "역삼동")
        self.assertEqual(str(expected), "서울특별시 강남구 역삼동")




#  python manage.py test restaurant.tests






