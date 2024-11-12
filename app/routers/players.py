from fastapi import APIRouter, HTTPException,status, Depends
from ..database.players_crud import all_players,player_by_id,save_player,get_player_events
from ..database.events_crud import make_event,get_event
from ..database.schemas import PlayerBase,PlayerEvent,EventIn,EventDb,PlayerIn
from ..database.database import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.get('/players', response_model=list[PlayerIn])
def get_players(db: Session = Depends(get_db)):
    return all_players(db)


@router.post('/players', response_model=PlayerIn,status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerBase, db: Session = Depends(get_db)):
    return save_player(player_in, db)


@router.get('/players/{id}', response_model=PlayerEvent)
def get_players_id(id: int, db: Session = Depends(get_db)):
    player_info = player_by_id(db, id)
    if player_info is None:
        raise HTTPException(status_code=404, detail='player not found!')
    
    player_events = get_player_events(db,player_info.id,typestr=None)

    return PlayerEvent(id = player_info.id, name = player_info.name, events = player_events)


@router.get('/events',response_model=list[EventDb])
def get_events(type:str|None=None, db: Session = Depends(get_db)):
    return get_event(db,type)


@router.get('/players/{id}/events',response_model=list[EventDb])
def get_id_events(id:int,type:str|None=None, db:Session=Depends(get_db)):
    
    return get_player_events(db=db,id=id,typestr=type)


@router.post('/players/{id}/events',response_model=EventDb,status_code=status.HTTP_201_CREATED)
def post_event(id:int,event_in:EventIn, db: Session = Depends(get_db)):
    player_info = player_by_id(db, id)
    if player_info is None:
        raise HTTPException(status_code=404, detail='player not found!')
    
    return make_event(id=id,event_in= event_in,db= db) 
    