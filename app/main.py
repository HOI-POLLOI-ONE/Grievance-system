
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI(
    title="grienace system",
    description="a web application where grievances are closed with whole verification n proofs",
    version="1.0.0"
    
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")

def root():
    return{
        "message":"the systen is running ",
        "status":"done"
    }





