from sqlalchemy import func
from sqlalchemy.orm import Session
from app import models

def count_open_issues_by_user(db: Session, userId: str):
    return db.query(func.count(models.Issue.id)).filter(
        models.Issue.userId == userId,
        models.Issue.status == 'pending'
    ).scalar()

def count_closed_issues_by_user(db: Session, userId: str):
    return db.query(func.count(models.Issue.id)).filter(
        models.Issue.userId == userId,
        models.Issue.status == 'closed'
    ).scalar()

def count_high_issues_by_user(db: Session, userId: str):
    return db.query(func.count(models.Issue.id)).filter(
        models.Issue.userId == userId,
        models.Issue.priority == 'High'
    ).scalar()

def count_med_issues_by_user(db: Session, userId: str):
    return db.query(func.count(models.Issue.id)).filter(
        models.Issue.userId == userId,
        models.Issue.priority == 'Medium'
    ).scalar()


def count_low_issues_by_user(db: Session, userId: str):
    return db.query(func.count(models.Issue.id)).filter(
        models.Issue.userId == userId,
        models.Issue.priority == 'Low'
    ).scalar()