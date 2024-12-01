from fastapi import APIRouter

router = APIRouter(tags=["Info"])


@router.get("/info")
def info():
    return {
        "app_name": "UD CVE API",
        "author": "Done by Volodymyr Komarnytskyi",
        "description": "API for CVE"
    }
