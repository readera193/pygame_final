@call C:\ProgramData\Anaconda3\Scripts\activate.bat C:\ProgramData\Anaconda3

pip install --upgrade --user pip
pip install pygame
pip install python-dotenv
pip install mysql-connector-python

copy .env.example .env

@pause