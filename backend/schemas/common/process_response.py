# in-built
from typing import Optional

from fastapi import status
# 3rd party
from pydantic import BaseModel, StrictBool, StrictStr, StrictInt

# in-built
from config.type_hints import DataDict


class ProcessResponse(BaseModel):
    is_success: StrictBool
    reason: Optional[StrictStr] = None
    response_data: DataDict = dict()
    code: StrictInt = status.HTTP_200_OK


class SimpleResponse(BaseModel):
    message: StrictStr


class HTTPError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "HTTPException raised."},
        }
