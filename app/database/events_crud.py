from fastapi import HTTPException
from .schemas import EventIn
from sqlalchemy.orm import Session
from . import models
import datetime

def make_event(event_in:EventIn , db:Session,id:int):
    event = models.Event(**event_in.dict(),player_id=id,timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    if event.type != "level_started" and event.type != "level_solved":
        raise HTTPException(status_code=400)
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def get_event(db:Session,type:str):
    if type is None:
        return db.query(models.Event).all()
    if type != "level_started" and type != "level_solved":
        raise HTTPException(status_code=400)
    return db.query(models.Event).filter(models.Event.type == type).all()