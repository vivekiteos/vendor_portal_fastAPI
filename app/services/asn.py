from app.services import sap_api as sap

def get_asn(asn_id):
    return sap.call_get_asn_api(asn_id)


def create_asn(createASN):
    return sap.call_create_asn_api(createASN)


# def po_to_asn(db: Session, issue: IssueCreate, userId: str):
#     issue_date = datetime.strptime(issue.issue_date, "%d/%m/%Y").date()
#     action_date = datetime.strptime(issue.action_date, "%d/%m/%Y").date()
#     db_issue = models.Issue(
#         issue_no = generate_random_issue_no(),
#         userId= userId,
#         supplier= issue.supplier,
#         complaint_ref= issue.complaint_ref,
#         priority= issue.priority,
#         material= issue.material,
#         issue_date= issue_date,
#         ref_grn_po= issue.ref_grn_po,
#         action_date= action_date,
#         issue_title= issue.issue_title,
#         issue_desc= issue.issue_desc,
#         submit_type= issue.submit_type,
#     )
#     db.add(db_issue)
#     db.flush()
#     db.refresh(db_issue)
#     db.commit()
#     return db_issue