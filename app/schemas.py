from pydantic import BaseModel
from typing import List

class CVE(BaseModel):
    cveID: str
    vendorProject: str
    product: str
    vulnerabilityName: str
    dateAdded: str
    shortDescription: str
    requiredAction: str
    dueDate: str
    knownRansomwareCampaignUse: str
    notes: str
    cwes: List[str]
