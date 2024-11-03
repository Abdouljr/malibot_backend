from fastapi import HTTPException

from models.role import RoleBase, Role


def add(role: RoleBase, db):
    role.name = role.name.upper()
    db_role = Role(**role.model_dump())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def get_all(db):
    roles = db.query(Role).all()
    return roles


def supprimer_role(role_id, db):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if db_role is None:
        raise HTTPException(status_code=404, detail='Role not found')
    db.delete(db_role)
    db.commit()
    return {"message": "Role deleted", "status": True}
