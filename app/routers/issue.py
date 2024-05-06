from app.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.issue import IssueCreate, Issue, IssueList
from app.services import issue as service_issue

router = APIRouter()

@router.post("", response_model=Issue)
def create_issue(issue: IssueCreate, db: Session = Depends(get_db)):
    userId ="USER07"
    return service_issue.create_issue(db, issue, userId)

@router.post("/close_issue")
def close_issue(issueId: int, db: Session = Depends(get_db)):
    userId ="USER07"
    return service_issue.close_issue(db, issueId, userId)


@router.post("/comments")
def add_comment(issueId: int, comment: str, db: Session = Depends(get_db)):
    userId ="USER07"
    return service_issue.add_comment(db, issueId, userId)


@router.get("/comments")
def get_comments(issueId: int, db: Session = Depends(get_db)):
    userId ="USER07"
    return service_issue.get_issue_comments(db, issueId)

@router.get("", response_model=IssueList)
def get_issue(db: Session = Depends(get_db)):
    userId ="USER07"
    issue_list = service_issue.get_issue_by_user_id(db, userId)
    return issue_list
