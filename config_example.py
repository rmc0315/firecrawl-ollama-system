# Universal Firecrawl + Ollama Configuration
# Copy this to config.py and customize as needed

import os

# Firecrawl Configuration
FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY', 'your-api-key-here')

# Ollama Configuration  
OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'http://localhost:11434')

# Report Settings
REPORTS_DIR = 'firecrawl_reports'
DEFAULT_SAVE_FORMAT = 'html'  # txt, csv, html, pdf, json, html_charts

# Model Preferences (optional - system will auto-detect)
PREFERRED_MODELS = {
    'fast': 'llama3.2',
    'reasoning': 'qwen3', 
    'coding': 'qwen2.5-coder',
    'comprehensive': 'phi4'
}
