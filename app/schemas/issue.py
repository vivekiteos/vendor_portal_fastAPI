
from datetime import date
from typing import List, Union
from pydantic import BaseModel

class IssueBase(BaseModel):
    supplier: str
    complaint_ref: str
    priority: str
    material: str
    issue_date: Union[date, str]
    ref_grn_po: str
    action_date: Union[date, str]
    issue_title: str
    issue_desc: str
    submit_type: str


class IssueCreate(IssueBase):
    pass

class Issue(IssueBase):
    id: int
    issue_no: str
    created_date: Union[date, str]


IssueList= List[Issue]