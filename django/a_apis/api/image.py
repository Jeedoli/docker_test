from a_apis.models.image import Image
from a_apis.schema.image import ImageResponse
from a_apis.service.image import ImageService
from ninja import File, Form, Router
from ninja.errors import HttpError
from ninja.files import UploadedFile

from django.core.files.uploadedfile import UploadedFile

router = Router(tags=["이미지"])


# 이미지 업로드
@router.post("/upload", response=ImageResponse)
def upload_image(
    request,
    *,
    image: UploadedFile = File(...),
):
    try:
        result = ImageService.upload_image(image)
        return {"success": True, "data": result}
    except ValueError as e:
        raise HttpError(400, str(e))
    except Exception as e:
        raise HttpError(500, "서버 에러가 발생했습니다.")


# 이미지 목록 조회
@router.get("/list", response=ImageResponse)
def list_images(request):
    images = (
        Image.objects.all()
        .values("id", "image_url", "created_at", "updated_at")
        .order_by("-created_at")
    )
    return {"success": True, "data": list(images)}
