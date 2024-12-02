from fastapi import APIRouter, HTTPException
from app.models import CVEListResponse
from app.db import (
    get_known_ransomware_cve,
    get_all_cve,
    get_new_cve,
    search_cve,
    init_db,
)
import json

router = APIRouter(tags=["CVE"])


@router.get("/init-db")
def initialize_database():
    import os
    try:
        file_path = "/home/volodymyr/FastAPI/exploits.json"
        with open(file_path, "r") as file:
            data = json.load(file)["vulnerabilities"]
        init_db(data)
        return {"status": "Database initialized successfully"}
    except FileNotFoundError:
        current_path = os.getcwd()
        raise HTTPException(
            status_code=404,
            detail=f"File exploits.json not found in {current_path}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error initializing database: {str(e)}"
        )


# Endpoint to get CVE for last 10 days
@router.get("/get/all", response_model=CVEListResponse)
def get_all_cve_endpoint():
    data = get_all_cve()
    if not data:
        raise HTTPException(status_code=404, detail="No CVEs found")
    return {"count": len(data), "vulnerabilities": [hit["_source"] for hit in data]}


# Endpoint to get 10 newest CVE
@router.get("/get/new", response_model=CVEListResponse)
def get_new_cve_endpoint():
    data = get_new_cve()
    if not data:
        raise HTTPException(status_code=404, detail="No new CVEs found")
    return {"count": len(data), "vulnerabilities": [hit["_source"] for hit in data]}


# Endpoint to get CVE with "Known" ransomware campaign use
@router.get("/get/known", response_model=CVEListResponse)
def get_known_ransomware_cve_endpoint():
    data = get_known_ransomware_cve()
    if not data:
        raise HTTPException(status_code=404, detail="No ransomware-related CVEs found")
    return {"count": len(data), "vulnerabilities": [hit["_source"] for hit in data]}


@router.get("/get", response_model=CVEListResponse)
def search_cve_endpoint(query: str):
    data = search_cve(query)
    if not data:
        raise HTTPException(status_code=404, detail="No matching CVEs found")
    return {"count": len(data), "vulnerabilities": [hit["_source"] for hit in data]}
