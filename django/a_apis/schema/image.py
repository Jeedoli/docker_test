from datetime import datetime
from typing import Optional

from ninja import Field, Schema


class ImageSchema(Schema):
    """이미지 기본 스키마"""

    id: int = Field(..., description="이미지 ID")
    image_url: str = Field(..., description="이미지 URL")
    created_at: datetime = Field(..., description="등록일")
    updated_at: datetime = Field(..., description="수정일")


class ImageResponse(Schema):
    """이미지 응답 스키마"""

    success: bool = Field(..., description="성공 여부")
    message: Optional[str] = Field(None, description="응답 메시지")
    data: Optional[ImageSchema] = Field(None, description="이미지 데이터")
