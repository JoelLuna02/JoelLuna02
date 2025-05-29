import os
import dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dotenv.load_dotenv()

def get_database_uri():
    """Se genera la URL de la base de datos desde las variables de entorno."""
    db_engine = os.getenv("DB_ENGINE", "sqlite3")
    if db_engine == "postgresql":
        user = os.getenv("DB_USER", "user")
        password = os.getenv("DB_PASSWORD", "password")
        host = os.getenv("DB_HOST", "localhost")
        port = os.getenv("DB_PORT", "5432")
        name = os.getenv("DB_NAME", "database")
        return f"postgresql://{user}:{password}@{host}:{port}/{name}"
    else:
        name = os.getenv("DB_NAME", "db.sqlite3")
        return f"sqlite:///{name}"

DATABASE_URI = get_database_uri()
engine = create_engine(DATABASE_URI, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URI else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Crea una sesión de base de datos."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
