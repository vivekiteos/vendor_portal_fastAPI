from datetime import datetime
from sqlalchemy.orm import Session
from app import models
from app.schemas.issue import IssueCreate
from app.internal import security
from app.services.common import generate_random_issue_no

def create_issue(db: Session, issue: IssueCreate, userId: str):
    db_issue = models.Issue(
        issue_no = generate_random_issue_no(),
        userId= userId,
        supplier= issue.supplier,
        complaint_ref= issue.complaint_ref,
        priority= issue.priority,
        material= issue.material,
        issue_date= issue.issue_date,
        ref_grn_po= issue.ref_grn_po,
        action_date= issue.action_date,
        issue_title= issue.issue_title,
        issue_desc= issue.issue_desc,
        submit_type= issue.submit_type,
        status= "pending"
    )
    db.add(db_issue)
    db.flush()
    db.refresh(db_issue)
    db.commit()
    return db_issue

def get_issue_by_user_id(db: Session, userId: str):
    return db.query(models.Issue).filter(
        models.Issue.userId == userId
    ).all()

def close_issue(db: Session, issueId: int, userId: str):
    issue = db.query(models.Issue).filter(
        models.Issue.id == issueId
    ).first()
    if(issueId != None):
        issue.status ="closed"
        db.commit()
        db.refresh(issue)


def get_issue_comments(db: Session, issueId: int):
    return db.query(models.IssueComments).filter(
        models.IssueComments.issueId == issueId
    ).all()


def add_comment(db: Session, issueId: int, comment: str, userId: str):
    db_issue = models.IssueComments(
        userId= userId,
        issueId= issueId,
        comments= comment
    )
    db.add(db_issue)
    db.flush()
    db.refresh(db_issue)
    db.commit()
    return db_issue