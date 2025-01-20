import boto3
from a_apis.models.image import Image

from django.conf import settings


class ImageService:
    MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5MB in bytes

    @staticmethod
    def upload_image(file) -> dict:
        # 파일 크기 검증
        if file.size > ImageService.MAX_IMAGE_SIZE:
            raise ValueError("이미지 크기는 5MB를 초과할 수 없습니다.")

        # S3에 자동 업로드된 파일의 URL 가져오기
        file_url = f"{settings.MEDIA_URL}{file.name}"

        # DB에 저장
        image = Image.objects.create(image_url=file_url)

        return {
            "id": image.id,
            "image_url": image.image_url,
            "created_at": image.created_at,
            "updated_at": image.updated_at,
        }
