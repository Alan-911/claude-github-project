import os
import anthropic

# Get your API key from environment variables
api_key = os.getenv("CLAUDE_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

prompt = "Write a short, funny story about AI in space."

response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=300,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Print output to GitHub Actions log
print(response.content[0].text)
