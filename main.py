from fastapi import FastAPI
import uvicorn
from app import reg, oformcard

app = FastAPI()

app.include_router(reg.router)
app.include_router(oformcard.router)

uvicorn.run(app)
