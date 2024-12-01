from pydantic import BaseModel
from typing import List


# Models for output
class CVEItem(BaseModel):
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

    class Config:
        from_attributes = True


class CVEListResponse(BaseModel):
    count: int
    vulnerabilities: List[CVEItem]

    class Config:
        from_attributes = True
