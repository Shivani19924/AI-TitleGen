from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class TitleGenerator:
    def __init__(self, model_name="google/flan-t5-base"):
        print("Loading model... please wait...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        print("Model loaded successfully.")

    def generate_title(self, paragraph: str):
        prompt = f"Generate a creative and contextually fitting title for this story: {paragraph}"
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=20,
            num_return_sequences=3,
            do_sample=True,
            temperature=0.8,
            top_p=0.9
        )
        titles = [self.tokenizer.decode(o, skip_special_tokens=True) for o in outputs]
        return titles
