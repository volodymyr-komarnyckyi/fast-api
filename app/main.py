from app.routers import cve_router, info_router
from fastapi import FastAPI


app = FastAPI()

# Connect routers
app.include_router(cve_router.router)
app.include_router(info_router.router)
