from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models import schemas as Schemas
from services import summarize as Summarize

tags_metadata = [
    {
        "name": "",
        "description": ""
    }
]

app = FastAPI(openapi_tags=tags_metadata)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/sum')
def summarize(source: Schemas.summarize_text):
    outputs = Summarize.summarize(source.text, source.precent)
    return{"outputs": outputs}
