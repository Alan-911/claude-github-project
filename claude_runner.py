import os
import anthropic

# Get your API key from environment variables
api_key = os.getenv("CLAUDE_API_KEY")
client = anthropic.Client(api_key=api_key)

prompt = "Write a short, funny story about AI in space."

response = client.completions.create(
    model="claude-3",
    prompt=prompt,
    max_tokens_to_sample=300
)

# Print output to GitHub Actions log
print(response.completion)
