
from pydantic import BaseModel

class EventBase(BaseModel):
    id:int

class EventIn(BaseModel):
    type:str | None = None
    detail:str
    class Config:
        orm_mode = True

class EventDb(EventIn,EventBase):
    timestamp:str
    player_id:int
    class Config:
        orm_mode = True

class PlayerDb(BaseModel):
    id:int

class PlayerBase(BaseModel):
    name:str
    class Config:
        orm_mode=True

class PlayerIn(PlayerBase,PlayerDb):
    None

class PlayerEvent(PlayerIn):
    events:list[EventDb]
    class Config:
        orm_mode = True
