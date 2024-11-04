from fastapi import HTTPException
from configurations.database_config import SessionLocal
from models.role import RoleBase, Role
from services.auth_service import create_default_admin


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


def delete(role_id, db):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if db_role is None:
        raise HTTPException(status_code=404, detail='Role not found')
    db.delete(db_role)
    db.commit()
    return {"message": "Role deleted", "status": True}


def init():
    default_roles = ['ADMIN', 'USER']
    session = SessionLocal()
    for role_name in default_roles:
        db_role = session.query(Role).filter_by(name=role_name).first()
        if not db_role:
            db_role = Role(name=role_name)
            session.add(db_role)
    session.commit()
    create_default_admin()

