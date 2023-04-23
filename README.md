# Commuity 

# on Window
## Activate environment python 
    python -m venv venv

    ./venv/Scripts/activate 
## install library
    pip install -r requirements.txt
## migrate models to database 
    alembic upgrade head
## run project 
    uvicorn app.main:app --reload
# on Linux, MacOS
## activate environment python
    poetry shell
## install library 
    poetry install
## migrate models to database 
    alembic upgrade head
## run project 
    uvicorn app.main:app --reload