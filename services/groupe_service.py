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


def add_users_to_groupe(db, groupe_id: int, user_email: str):
    # Récupère le groupe par son ID
    groupe = db.query(Groupe).filter(Groupe.id == groupe_id).first()

    if not groupe:
        raise HTTPException(status_code=404, detail='Groupe not found')

    # Récupère les utilisateurs à ajouter
    db_user = db.query(User).filter(User.email == user_email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')

    groupe.users.append(db_user)
    db.commit()  # Sauvegarde les changements
    db.refresh(groupe)  # Rafraîchit le groupe pour refléter les modifications
    return groupe.users


def get_groupes_for_user(db, user_unique_id: str):
    user = db.query(User).filter(User.unique_id == user_unique_id).first()
    return user.groupes


def supprimer_groupe(groupe_id, db):
    db_groupe = db.query(Groupe).filter(Groupe.id == groupe_id).first()
    if db_groupe is None:
        raise HTTPException(status_code=404, detail='Groupe not found')
    db.delete(db_groupe)
    db.commit()
    return {"message": "Groupe deleted", "status": True}
