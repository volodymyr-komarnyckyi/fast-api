from app.services import load_cve_data, get_recent_cve, get_new_cve, get_known_ransomware_cve
from fastapi import APIRouter, HTTPException
from app.models import CVEListResponse


router = APIRouter(tags=["CVE"])


# Endpoint to get CVE for last 10 days
@router.get("/get/all", response_model=CVEListResponse)
def get_all_cve():
    cve_data = load_cve_data()

    if 'vulnerabilities' not in cve_data:
        raise HTTPException(status_code=500, detail="vulnerabilities key not found in JSON response")

    recent_cve = get_recent_cve(cve_data)

    return {"count": len(recent_cve), "vulnerabilities": recent_cve}


# Endpoint to get 10 newest CVE
@router.get("/get/new", response_model=CVEListResponse)
def get_new_cve_endpoint():
    cve_data = load_cve_data()

    if 'vulnerabilities' not in cve_data:
        raise HTTPException(status_code=500, detail="vulnerabilities key not found in JSON response")

    new_cve = get_new_cve(cve_data)

    return {"count": len(new_cve), "vulnerabilities": new_cve}


# Endpoint to get CVE with "Known" ransomware campaign use
@router.get("/get/known", response_model=CVEListResponse)
def get_known_ransomware_cve_endpoint():
    cve_data = load_cve_data()

    if 'vulnerabilities' not in cve_data:
        raise HTTPException(status_code=500, detail="vulnerabilities key not found in JSON response")

    known_ransomware_cve = get_known_ransomware_cve(cve_data)

    return {"count": 10, "vulnerabilities": known_ransomware_cve[:10]}
