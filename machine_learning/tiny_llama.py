# Install transformers from source - only needed for versions <= v4.34
# pip install git+https://github.com/huggingface/transformers.git
# pip install accelerate

import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16, device_map="auto")

while True:
    system_prompt = """

        Intruction: You are my helpful tutor for computer science. Please respond in a helpful and kind manner
        Personality : Sassy
        Gender : Female
        Age : 23
        Student_Profile: The student you are tutoring is named Jeff. He is a slow learner, has difficulties with understand operating systems
    """
    user_prompt = input("What do you want to ask? ")

    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {"role": "user", "content": user_prompt},
    ]

    prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)

    print(outputs[0]["generated_text"])