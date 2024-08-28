from transformers import GPTNeoForCausalLM, GPT2Tokenizer

# Carga el tokenizador y el modelo
tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")

# Configura el token de padding si no está configurado
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

def get_ai_response(prompt):
    # Tokeniza el texto de entrada
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    
    # Genera la máscara de atención manualmente
    attention_mask = (inputs['input_ids'] != tokenizer.pad_token_id).long()

    # Genera la respuesta usando el modelo con ajustes en los parámetros
    outputs = model.generate(
        inputs['input_ids'],
        attention_mask=attention_mask,
        max_length=300,  # Longitud de respuesta
        num_return_sequences=1,
        pad_token_id=tokenizer.pad_token_id,
        do_sample=True,  # Usa muestreo
        temperature=0.3,  # Menor variabilidad
        top_k=30,        # Reduce opciones
        top_p=0.85,      # Probabilidad acumulada
        no_repeat_ngram_size=2,  # Evita repeticiones
        eos_token_id=tokenizer.eos_token_id
    )
    
    # Decodifica la respuesta generada
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response
