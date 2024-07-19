from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load summarization pipeline
summarizer = pipeline("summarization")

class TextRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    summary: str

@app.post("/summarize", response_model=SummaryResponse)
def summarize_text(request: TextRequest):
    if len(request.text.strip()) == 0:
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    # Perform summarization
    summary = summarizer(request.text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    
    return SummaryResponse(summary=summary)

# Example route to check if the API is running
@app.get("/")
def read_root():
    return {"message": "Summarization API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
