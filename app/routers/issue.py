from app.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.issue import IssueCreate, Issue, IssueList
from app.services import issue as service_issue

router = APIRouter()

@router.post("", response_model=Issue)
def create_user(issue: IssueCreate, db: Session = Depends(get_db)):
    userId ="USER07"
    return service_issue.create_issue(db, issue, userId)


@router.get("", response_model=IssueList)
def create_user(db: Session = Depends(get_db)):
    userId ="USER07"
    issue_list = service_issue.get_issue_by_user_id(db, userId)
    return issue_list
