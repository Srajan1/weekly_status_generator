#!/bin/sh

# Start the Ollama server in the background
ollama serve &

# Give the server a moment to start
sleep 2

# Only pull the model if it's not already pulled
if ! ollama list | grep -q 'phi3.*3.8b'; then
  echo "Pulling model phi3:3.8b..."
  ollama pull phi3:3.8b
else
  echo "Model phi3:3.8b already exists. Skipping pull."
fi

# Wait for Ollama server to stay alive
wait
