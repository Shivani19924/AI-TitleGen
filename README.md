Model Overview

This backend uses a pre-trained text-to-text Transformer model from Hugging Face, specifically:

🧩 Model Used: t5-small (Text-to-Text Transfer Transformer)

It’s a sequence-to-sequence (Seq2Seq) model designed by Google, trained to convert an input text (paragraph) into another text output (title) by learning contextual understanding of words and phrases.

⚙️ How It Works (Simplified Flow)

Input:
The user sends a paragraph (story description, article, etc.) to the FastAPI endpoint /generate-title.

Tokenization:
The text is tokenized by the T5Tokenizer, converting words into numerical tokens that the model understands.

Model Inference:
The tokens are passed to the T5 model (T5ForConditionalGeneration), which uses its encoder-decoder Transformer architecture to generate a concise, contextually relevant title.

Decoding:
The output token IDs are decoded back into readable text — this becomes your generated story title.

Response:
The generated title is sent as a JSON response to the user.

🧩 Architecture Summary
User Input (Paragraph)
        │
        ▼
 FastAPI Endpoint (/generate-title)
        │
        ▼
 Tokenization (T5Tokenizer)
        │
        ▼
 Model Inference (T5ForConditionalGeneration)
        │
        ▼
 Title Generated (Decoded Text)
        │
        ▼
JSON Response → {"generated_title": "The Hidden Forest of Echoes"}
