from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK data
nltk.download('punkt')

app = FastAPI()

class TextRequest(BaseModel):
    text: str

class TokenCountResponse(BaseModel):
    token_count: int

@app.post("/token_count", response_model=TokenCountResponse)
def get_token_count(request: TextRequest):
    if len(request.text.strip()) == 0:
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    # Tokenize the text
    tokens = word_tokenize(request.text)
    token_count = len(tokens)
    
    return TokenCountResponse(token_count=token_count)

# Example route to check if the API is running
@app.get("/")
def read_root():
    return {"message": "Token Count API is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
