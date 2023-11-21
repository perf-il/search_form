call %~dp0venv\Scripts\activate
pip install -r requirements.txt

start main.py

pytest -rA

echo tests finished
pause