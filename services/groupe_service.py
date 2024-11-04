from fastapi import HTTPException

from models.groupe import GroupeBase, Groupe
from models.user import User


def add(user_unique_id, groupe: GroupeBase, db):
    db_user = db.query(User).filter(User.unique_id == user_unique_id).first()
    db_groupe = Groupe(**groupe.model_dump())
    db_groupe.users = []
    db_groupe.users.append(db_user)
    db.add(db_groupe)
    db.commit()
    db.refresh(db_groupe)
    return db_groupe


def get_all(db):
    groupes = db.query(Groupe).all()
    return groupes


def supprimer_groupe(groupe_id, db):
    db_groupe = db.query(Groupe).filter(Groupe.id == groupe_id).first()
    if db_groupe is None:
        raise HTTPException(status_code=404, detail='Groupe not found')
    db.delete(db_groupe)
    db.commit()
    return {"message": "Groupe deleted", "status": True}
