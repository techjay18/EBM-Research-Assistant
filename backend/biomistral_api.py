from gradio_client import Client

client = Client("jaydesai18/ebm-biomistral")

def call_llm(prompt):
    response = client.predict(
        prompt=prompt,
        api_name="/generate"
    )
    # The model echoes the full prompt — strip everything before the generated answer

    cleaned_response = response.split("Final answer:")[-1].strip()
    return cleaned_response
