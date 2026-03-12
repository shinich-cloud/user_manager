from app.database import Base, engine
from app import models

def main():
    Base.metadata.create_all(bind=engine)
    print("OK")

if __name__ == "__main__":
    main()
