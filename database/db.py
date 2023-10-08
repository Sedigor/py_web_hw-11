from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import configparser


this_folder_path = os.path.dirname(os.path.abspath(__file__))
init_file = os.path.join(this_folder_path, 'config.ini')

config = configparser.ConfigParser()
config.read(init_file)

driver = config.get('DB', 'driver')
user = config.get('DB', 'user')
password = config.get('DB', 'password')
dbname = config.get('DB', 'dbname')
host = config.get('DB', 'host')
port = config.get('DB', 'port')


SQLALCHEMY_DATABASE_URL = f"{driver}{user}:{password}@{host}:{port}/{dbname}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# autocommit - це режим, коли кожна операція з базою даних автоматично підтверджується (комітиться). Тобто будь-які зміни, які ви вносите до бази даних, відразу ж стають активними і не можуть бути скасовані. За замовчуванням для роботи з SQLAlchemy увімкнено режим автокомміту.

# Параметр autoflush - це режим, коли будь-які зміни, які ви вносите в об'єкти сесії, автоматично відправляються в базу даних. Іншими словами, будь-які зміни, які ви вносите в об'єкти, відразу ж стають активними і можуть бути помітні в базі даних. За замовчуванням для роботи з SQLAlchemy увімкнено режим автоскидання.


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()