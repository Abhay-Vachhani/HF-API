from gradio_client import Client

client = Client("abhayv28/MISTRAL-0.3-7B")
result = client.predict(
		prompt="Hello!!",
		system_prompt=None,
		api_name="/generate"
)
print(result)