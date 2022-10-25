# in-built
from enum import Enum
from typing import List, Dict, Any, Union

# 3rd party
from pydantic import StrictStr, StrictInt

ListOfStrings = List[StrictStr]
ListOfIntegers = List[StrictInt]
DataDict = Dict[StrictStr, Any]


class QuestionStatus(Enum):
    CREATED = 'created'
    DELETED = 'deleted'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    FLAGGED = 'flagged'
