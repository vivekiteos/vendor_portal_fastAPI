from typing import List
from pydantic import BaseModel

class suppliedMaterial(BaseModel):
    date: str
    value: str

class issueTracker(BaseModel):
    open: str
    close: str
    # high: str
    # medium: str
    # low: str

class accountDetails(BaseModel):
    open_value: str
    total_supply_value: str

class ReportBase(BaseModel):
    suppliedMaterial: List[suppliedMaterial]
    issueTracker: issueTracker
    accountDetails: accountDetails

class Report(BaseModel):
    data: ReportBase
