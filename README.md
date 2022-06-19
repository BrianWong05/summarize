# summarize

# Installation
```
# linux  
python3 -m venv .venv
source .venv/bin/activate  
pip install -r requirements.txt  
  
# windows  
python -m venv .venv  
.venv/Scripts/activate
pip install -r requirements.txt  
```
# How to start
run
```
uvicorn api:app
```
go to http://127.0.0.1:8000/docs to see documentation

# How to use

method post  
route /sum
Requests body
```
{
    "text": str,
    "percent": float
}
```
Responses
```
{
    "outputs": ""
}
```