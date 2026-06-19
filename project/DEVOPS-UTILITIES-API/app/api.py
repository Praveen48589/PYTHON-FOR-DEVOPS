from fastapi import FastAPI   # Importing FastApi class from library
from routers import metrics, aws
app = FastAPI(
    title="Internal Devops Utilities API",
    description="This is an Internal Utilities App for Monitoring metrics , AWS Usage, Log Analysing etc",
    version="1.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")       
def hello():
    """
    This is Hello API Just for Testing
    """

    return {"message":"Hello buddy"}

app.include_router(metrics.router)
app.include_router(aws.router, prefix="/aws")
