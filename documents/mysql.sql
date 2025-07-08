-- 데이터베이스 생성
CREATE DATABASE DB_NAME CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- 로컬 사용자 생성 및 권한 부여
CREATE USER 'DB_USER'@'localhost' IDENTIFIED BY 'DB_PASSWORD';
GRANT ALL PRIVILEGES ON DB_NAME.* TO 'DB_USER'@'localhost';

-- 원격 접속 사용자 생성 및 권한 부여
CREATE USER 'DB_USER'@'%' IDENTIFIED BY 'DB_PASSWORD';
GRANT ALL PRIVILEGES ON DB_NAME.* TO 'DB_USER'@'%';







CREATE TABLE article (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL COMMENT '게시글 제목',
    preview_image VARCHAR(255) COMMENT '미리보기 이미지',
    content TEXT NOT NULL COMMENT '본문 내용',
    show_at_index BOOLEAN DEFAULT FALSE COMMENT '메인페이지 노출 여부',
    is_published BOOLEAN DEFAULT FALSE COMMENT '게시 여부',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '생성일',
    modified_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일'
) COMMENT='칼럼';

CREATE TABLE cuisine_type (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL COMMENT '음식 종류명'
) COMMENT='음식 종류';

CREATE TABLE restaurant_category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL COMMENT '카테고리명',
    cuisine_type_id INT COMMENT '연결된 음식 종류',
    FOREIGN KEY (cuisine_type_id) REFERENCES cuisine_type(id)
) COMMENT='가게 카테고리';

CREATE TABLE restaurant (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL COMMENT '음식점 이름',
    branch_name VARCHAR(100) COMMENT '지점명',
    description TEXT COMMENT '음식점 설명',
    address VARCHAR(255) NOT NULL COMMENT '주소',
    feature VARCHAR(255) NOT NULL COMMENT '특징 요약',
    is_closed BOOLEAN DEFAULT FALSE COMMENT '폐업 여부',
    latitude DECIMAL(16,12) DEFAULT 0.0000 COMMENT '위도',
    longitude DECIMAL(16,12) DEFAULT 0.0000 COMMENT '경도',
    phone VARCHAR(16) COMMENT '전화번호 (E.164 포맷)',
    rating DECIMAL(3,2) DEFAULT 0.0 COMMENT '평점',
    rating_count INT UNSIGNED DEFAULT 0 COMMENT '평가수',
    start_time TIME COMMENT '영업 시작 시간',
    end_time TIME COMMENT '영업 종료 시간',
    last_order_time TIME COMMENT '라스트 오더 시간',
    category_id INT COMMENT '가게 카테고리',
    FOREIGN KEY (category_id) REFERENCES restaurant_category(id)
) COMMENT='레스토랑';

CREATE TABLE tag (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL COMMENT '태그 이름'
) COMMENT='태그';

CREATE TABLE restaurant_tags (
    id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT NOT NULL,
    tag_id INT NOT NULL,
    FOREIGN KEY (restaurant_id) REFERENCES restaurant(id),
    FOREIGN KEY (tag_id) REFERENCES tag(id),
    UNIQUE KEY unique_restaurant_tag (restaurant_id, tag_id)
) COMMENT='레스토랑-태그 M:N 관계';

CREATE TABLE restaurant_image (
    id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT NOT NULL COMMENT '해당 이미지의 레스토랑',
    is_representative BOOLEAN DEFAULT FALSE COMMENT '대표 이미지 여부',
    `order` INT UNSIGNED COMMENT '정렬 순서',
    name VARCHAR(100) COMMENT '이미지 이름',
    image VARCHAR(100) NOT NULL COMMENT '이미지 경로',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '생성일',
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일',
    FOREIGN KEY (restaurant_id) REFERENCES restaurant(id)
) COMMENT='가게 이미지';

CREATE TABLE restaurant_menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT NOT NULL COMMENT '해당 메뉴의 레스토랑',
    name VARCHAR(100) NOT NULL COMMENT '메뉴명',
    price INT UNSIGNED DEFAULT 0 COMMENT '가격',
    image VARCHAR(100) COMMENT '메뉴 이미지',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '생성일',
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일',
    FOREIGN KEY (restaurant_id) REFERENCES restaurant(id)
) COMMENT='가게 메뉴';

CREATE TABLE social_channel (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL COMMENT 'SNS 채널명'
) COMMENT='소셜채널';

CREATE TABLE review (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL COMMENT '리뷰 제목',
    author VARCHAR(100) NOT NULL COMMENT '작성자',
    profile_image VARCHAR(100) COMMENT '프로필 이미지',
    content TEXT NOT NULL COMMENT '리뷰 내용',
    rating SMALLINT UNSIGNED NOT NULL COMMENT '1~5점',
    restaurant_id INT NOT NULL COMMENT '대상 음식점',
    social_channel_id INT COMMENT 'SNS 채널',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '생성일',
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일',
    FOREIGN KEY (restaurant_id) REFERENCES restaurant(id),
    FOREIGN KEY (social_channel_id) REFERENCES social_channel(id)
) COMMENT='리뷰';

CREATE TABLE review_image (
    id INT AUTO_INCREMENT PRIMARY KEY,
    review_id INT NOT NULL COMMENT '대상 리뷰',
    name VARCHAR(100) NOT NULL COMMENT '이미지 이름',
    image VARCHAR(100) NOT NULL COMMENT '이미지 경로',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '생성일',
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일',
    FOREIGN KEY (review_id) REFERENCES review(id)
) COMMENT='리뷰이미지';
