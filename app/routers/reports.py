from app.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.routers import auth
from app.schemas.inventory import Inventory, Createinventory
from app.schemas.reports import Report, ReportBase, accountDetails, issueTracker, suppliedMaterial
from app.schemas.user import User
from app.services import reports as service_reports, issue as service_issue

router = APIRouter()

@router.get("", response_model=Report)
def get_rep(db: Session = Depends(get_db), current_user: User = Depends(auth.authorized_user)):
    userId = current_user.userId
    if current_user.role.lower() =="buyer":
        pending_count = service_reports.count_open_issues_by_user(db, userId)
        closed_count = service_reports.count_closed_issues_by_user(db, userId)
        high = service_reports.count_high_issues_by_user(db, userId)
        med = service_reports.count_med_issues_by_user(db, userId)
        low = service_reports.count_low_issues_by_user(db, userId)
        issue_tracker = issueTracker(open=str(pending_count), close=str(closed_count), high=str(high), medium=str(med), low=str(low))
        supplied_material = []
        account_details = accountDetails(open_value="1234", total_supply_value="2342345")
        return Report(
            data=ReportBase(
                suppliedMaterial=supplied_material,
                issueTracker=issue_tracker,
                accountDetails=account_details
            )
        )
    else:
        pending_count = "5"
        closed_count = "15"
        high = "3"
        med = "5"
        low = "5"
        issue_tracker = issueTracker(open=str(pending_count), close=str(closed_count), high=str(high), medium=str(med), low=str(low))
        supplied_material = []
        account_details = accountDetails(open_value="145234", total_supply_value="2342345")
        return Report(
            data=ReportBase(
                suppliedMaterial=supplied_material,
                issueTracker=issue_tracker,
                accountDetails=account_details
            )
        )
    


