import openai
import config 

openai.api_key = config.OPENAI_API_KEY

def chatbot(message):
    if message:
        # Optional: Modify the prompt based on message or context
        prompt = "Answer the following question in a comprehensive and informative way:\n" + message

        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  # Or another suitable model
            prompt=prompt,
            max_tokens=150,  # Adjust as needed
            temperature=0.7,  # Adjust for desired response creativity
            n=1,
            stop=None,
        )
        return response.choices[0].text