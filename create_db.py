from app.database import Base, engine

print("Erstelle Datenbanktabellen...")
Base.metadata.create_all(bind=engine)
print("Datenbanktabellen wurden erfolgreich erstellt.")