from fastapi import FastAPI, Form
from model.text_model import TitleGenerator
from utils.metrics import distinct_n

app = FastAPI(title="AI Story Title Generator")
generator = TitleGenerator()

@app.post("/generate-title")
def generate(paragraph: str = Form(...)):
    titles = generator.generate_title(paragraph)
    score = distinct_n(titles, 3)
    chosen = titles[0]
    return {"titles": titles, "distinct_3": round(score, 3), "final_title": chosen}
