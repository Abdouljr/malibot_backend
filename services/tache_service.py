from fastapi import HTTPException

from models.groupe import Groupe
from models.tache import TacheBase, Tache, TacheDTO


def add(tache: TacheBase, db):
    db_groupe = db.query(Groupe).filter(Groupe.id == tache.groupe_id).first()
    print(db_groupe)
    print(tache)
    if db_groupe is None:
        raise HTTPException(status_code=404, detail='Groupe not found')
    db_tache = Tache(**tache.model_dump())
    db_tache.groupe = db_groupe
    db.add(db_tache)
    db.commit()
    db.refresh(db_tache)
    return db_tache


def update(tache: TacheDTO, db):
    db_tache = db.query(Tache).filter(Tache.id == tache.id).first()
    if db_tache is None:
        raise HTTPException(status_code=404, detail='Tache not found')

    db_tache.titre = tache.titre
    db_tache.date_echeance = tache.date_echeance
    db_tache.fait = tache.fait
    db.commit()
    db.refresh(db_tache)
    return db_tache


def get_by_groupe(groupe_id: int, db):
    taches = db.query(Tache).filter(Tache.groupe_id == groupe_id).all()
    return taches


def delete(tache_id, db):
    db_tache = db.query(Tache).filter(Tache.id == tache_id).first()
    if db_tache is None:
        raise HTTPException(status_code=404, detail='Tache not found')
    db.delete(db_tache)
    db.commit()
    return {"message": "Tache deleted", "status": True}
