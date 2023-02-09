from datetime import datetime

from pydantic import BaseModel, Field, validator
from typing import List, Optional

from schemas.game import GameBaseDB


class RecommendCreate(BaseModel):
    userid: int
    gameid: int


class RecommendBaseDB(BaseModel):
    gameid: int

    class Config:
        orm_mode = True


class RecommendInfoDB(BaseModel):
    game: GameBaseDB

    class Config:
        orm_mode = True