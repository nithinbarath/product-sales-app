# in-built
import os
import traceback
from datetime import datetime

# 3rd party
import pendulum
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError

# custom
from schemas.common.process_response import ProcessResponse



def make_response(execution: ProcessResponse, response: BaseModel = None):
    try:
        print(execution.response_data)
        if execution.is_success:
            if response is None:
                return JSONResponse(
                    content=execution.response_data,
                    status_code=execution.code
                )
            else:
                return JSONResponse(
                    content=response.dict(),
                    status_code=execution.code
                )

        else:
            raise HTTPException(
                detail=execution.response_data or execution.reason,
                status_code=execution.code
            )
    except ValidationError as e:
        raise HTTPException(
            detail=str(e),
            status_code=status.HTTP_400_BAD_REQUEST
        )

