import time
from fastapi import FastAPI
from code.databases.mysql_session import engine, Base, SessionLocal
from code.routers.trad import router as trad_router
from sqlalchemy.exc import OperationalError
from code.utils.seed_morse import seed_morse_dictionary

app = FastAPI(title="Traduction API", version="1.0.0")

def init_db():
    retries = 10
    while retries > 0:
        try:
            Base.metadata.create_all(bind=engine)
            print("Base de données connectée et tables créées avec succès !")
            return
        except OperationalError as e:
            retries -= 1
            if retries == 0:
                print("Erreur critique : Impossible de joindre la base de données.")
                raise e
            time.sleep(5)

init_db()

db = SessionLocal()
try:
    seed_morse_dictionary(db)
finally:
    db.close()

app.include_router(trad_router)

@app.get("/")
def index():
    return {"msg": "Devops - projet de Jacques Lin"}
