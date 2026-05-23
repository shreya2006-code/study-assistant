from fastapi import FastAPI
from app.core.settings import settings
from app.db.database import engine
from app.db.database import Base
from app.models.user import User

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)
print("Database Connected Successfully!")

Base.metadata.create_all(bind=engine)



@app.get("/")
def home():
    return {
        "message": f"{settings.APP_NAME} Running",
        "debug": settings.DEBUG
    }