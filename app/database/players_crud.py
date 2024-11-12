from fastapi import HTTPException
from .schemas import PlayerBase
from sqlalchemy.orm import Session
from . import models


def all_players(db: Session):
    return db.query(models.Player).all()


def player_by_id(db: Session, id: int):
    player = db.query(models.Player).filter(models.Player.id == id).first()
    if player is None:
        raise HTTPException(status_code=404, detail='player not found!')
    return player

def get_player_events(db:Session,id:int,typestr:str):
    player_id = player_by_id(db, id)
    if player_id is None:
        raise HTTPException(status_code=404, detail='player not found!')
    
    if typestr is None:
        events = db.query(models.Event).filter(models.Event.player_id == id).all()
        return events
    
    if typestr != "level_started" and typestr != "level_solved":
        raise HTTPException(status_code=400)
    
    if type(typestr) is str:
        events = db.query(models.Event).filter(models.Event.player_id == id,models.Event.type == typestr).all()
        return events
    else: raise HTTPException(status_code=422)

def save_player(player_in: PlayerBase, db: Session):
    if type(player_in.name) is str and len(player_in.name) != 0:
        player = models.Player(**player_in.dict())
        db.add(player)
        db.commit()
        db.refresh(player)
        return player
    else:
        raise HTTPException(status_code=422)
