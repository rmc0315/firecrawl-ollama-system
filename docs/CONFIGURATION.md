# ⚙️ Configuration Guide

Complete guide to configuring and customizing the Universal Firecrawl + Ollama Integration System.

## 🚀 Quick Configuration

### First-Time Setup
The system creates configuration automatically, but you can customize everything:

1. **Run the system**: `python universal_firecrawl_ollama.py`
2. **Enter API key** when prompted (saved automatically)
3. **Access Configuration**: Main Menu → Option 6 → Configuration Settings
4. **Customize as needed** using the interactive menu

### Configuration Menu Overview
```
⚙️ Configuration Settings:
1. 🔑 Update Firecrawl API Key
2. 📁 Change Reports Directory  
3. 💾 Set Default Save Format
4. 🔄 Reset Configuration
5. 📄 View Full Configuration
6. ⬅️ Back to Main Menu
```

---

## 📁 Configuration Files

### Primary Configuration: `config.py`
**Location**: Same directory as the main script  
**Purpose**: Stores all user settings and API keys  
**Auto-created**: Yes, on first run

**Example Configuration**:
```python
# Universal Firecrawl + Ollama Configuration
import os

# Firecrawl Configuration
FIRECRAWL_API_KEY = "fc-your-api-key-here"

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

# Advanced Settings
PROCESSING_TIMEOUT = 300  # seconds
MAX_CONTENT_LENGTH = 10000  # characters
ENABLE_DEBUG_LOGGING = False
```

### Template Configuration: `config_example.py`
**Location**: Same directory as the main script  
**Purpose**: Reference template for manual configuration  
**Auto-created**: Yes, by setup scripts

---

## 🔑 API Key Management

### Automatic API Key Storage
```python
# System automatically saves API key on first use
# No manual configuration needed for most users
```

### Manual API Key Configuration

#### **Method 1: Environment Variable (Recommended)**
```bash
# Windows (Command Prompt)
set FIRECRAWL_API_KEY=fc-your-api-key-here

# Windows (PowerShell)
$env:FIRECRAWL_API_KEY="fc-your-api-key-here"

# macOS/Linux (Bash/Zsh)
export FIRECRAWL_API_KEY="fc-your-api-key-here"

# Make permanent by adding to:
# Windows: System Environment Variables
# macOS: ~/.zshrc or ~/.bash_profile  
# Linux: ~/.bashrc or ~/.profile
```

#### **Method 2: Configuration File**
```python
# Edit config.py directly
FIRECRAWL_API_KEY = "fc-your-api-key-here"
```

#### **Method 3: Interactive Update**
```
1. Run system: python universal_firecrawl_ollama.py
2. Main Menu → Option 6 (Configuration Settings)  
3. Option 1 (Update Firecrawl API Key)
4. Enter new key
```

### API Key Security
```python
# ✅ Good practices:
# - Use environment variables for shared systems
# - Keep config.py in .gitignore  
# - Don't share config.py files
# - Regenerate keys if compromised

# ❌ Avoid:
# - Hardcoding keys in scripts
# - Sharing keys in chat/email
# - Using same key across multiple projects
```

---

## 🤖 Ollama Configuration

### Connection Settings

#### **Default Configuration**
```python
# Default Ollama host (works for most users)
OLLAMA_HOST = "http://localhost:11434"
```

#### **Custom Ollama Host**
```python
# If Ollama runs on different port
OLLAMA_HOST = "http://localhost:8080"

# If Ollama runs on different machine
OLLAMA_HOST = "http://192.168.1.100:11434"

# If using Docker
OLLAMA_HOST = "http://ollama-container:11434"
```

#### **Environment Variable Override**
```bash
# Set custom host without editing config
export OLLAMA_HOST="http://custom-host:11434"
```

### Model Preferences

#### **Automatic Detection (Default)**
```python
# System automatically detects and categorizes models
# No configuration needed - works with any models you have
```

#### **Custom Model Preferences**
```python
# Override automatic recommendations
PREFERRED_MODELS = {
    'fast': 'your-preferred-fast-model',
    'reasoning': 'your-preferred-reasoning-model',
    'coding': 'your-preferred-coding-model', 
    'comprehensive': 'your-preferred-comprehensive-model'
}

# Example with specific models:
PREFERRED_MODELS = {
    'fast': 'llama3.2:latest',
    'reasoning': 'qwen3:8b',
    'coding': 'codellama:13b',
    'comprehensive': 'mixtral:8x7b'
}
```

#### **Custom Model Categories**
```python
# Add custom categorization for your models
CUSTOM_MODEL_CATEGORIES = {
    'my-custom-model': 'reasoning',
    'fine-tuned-model': 'coding',
    'specialized-model': 'comprehensive'
}
```

---

## 📊 Report Configuration

### Output Directory

#### **Default Directory**
```python
REPORTS_DIR = 'firecrawl_reports'  # Created in script directory
```

#### **Custom Directory**
```python
# Relative path
REPORTS_DIR = 'my_analysis_reports'

# Absolute path  
REPORTS_DIR = '/home/user/Documents/reports'

# Windows absolute path
REPORTS_DIR = 'C:\\Users\\Username\\Documents\\Reports'

# Organize by date
REPORTS_DIR = 'reports/2024'
```

#### **Environment-Based Directory**
```python
import os
from datetime import datetime

# Different directories per user
REPORTS_DIR = f"reports/{os.getenv('USER', 'default_user')}"

# Date-based organization
REPORTS_DIR = f"reports/{datetime.now().strftime('%Y-%m')}"

# Project-based organization  
PROJECT_NAME = os.getenv('PROJECT_NAME', 'general')
REPORTS_DIR = f"reports/{PROJECT_NAME}"
```

### Default Save Format

#### **Available Formats**
```python
# Choose default format for all reports
DEFAULT_SAVE_FORMAT = 'html'         # Professional web reports
DEFAULT_SAVE_FORMAT = 'html_charts'  # Interactive reports with charts  
DEFAULT_SAVE_FORMAT = 'pdf'          # Print-ready documents
DEFAULT_SAVE_FORMAT = 'txt'          # Simple text format
DEFAULT_SAVE_FORMAT = 'csv'          # Data analysis format
DEFAULT_SAVE_FORMAT = 'json'         # Machine-readable format
```

#### **Format Selection Strategy**
```python
# For presentations
DEFAULT_SAVE_FORMAT = 'html_charts'

# For data analysis
DEFAULT_SAVE_FORMAT = 'csv'

# For documentation
DEFAULT_SAVE_FORMAT = 'pdf'

# For quick sharing
DEFAULT_SAVE_FORMAT = 'txt'

# For API integration
DEFAULT_SAVE_FORMAT = 'json'
```

### Report Customization

#### **File Naming**
```python
# Custom filename patterns (advanced)
REPORT_FILENAME_PATTERN = "{analysis_type}_{domain}_{timestamp}"

# Include model name in filename
INCLUDE_MODEL_IN_FILENAME = True

# Date format in filenames
TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"  # Default: 20241219_143022
TIMESTAMP_FORMAT = "%Y-%m-%d"       # Alternative: 2024-12-19
```

#### **Content Limits**
```python
# Maximum content length to analyze (characters)
MAX_CONTENT_LENGTH = 10000  # Default
MAX_CONTENT_LENGTH = 5000   # For faster processing
MAX_CONTENT_LENGTH = 20000  # For detailed analysis

# Timeout for processing (seconds)
PROCESSING_TIMEOUT = 300    # Default (5 minutes)
PROCESSING_TIMEOUT = 600    # Longer timeout for complex sites
PROCESSING_TIMEOUT = 120    # Shorter timeout for simple analysis
```

---

## 🔧 Advanced Configuration

### Performance Settings

#### **Memory Management**
```python
# Ollama memory settings
OLLAMA_MAX_LOADED_MODELS = 1  # Keep only one model in memory
OLLAMA_MEMORY_LIMIT = "8GB"   # Limit Ollama RAM usage (if supported)

# Content processing limits
CHUNK_SIZE = 1000             # Text chunk size for processing
CHUNK_OVERLAP = 200           # Overlap between chunks
MAX_CHUNKS_PER_ANALYSIS = 10  # Limit processing for large sites
```

#### **Network Settings**
```python
# Request timeouts
FIRECRAWL_TIMEOUT = 60        # Firecrawl API timeout (seconds)
OLLAMA_TIMEOUT = 300          # Ollama response timeout (seconds)

# Retry settings
MAX_RETRIES = 3               # Number of retry attempts
RETRY_DELAY = 2               # Delay between retries (seconds)

# Rate limiting
REQUESTS_PER_MINUTE = 10      # Limit API requests
```

### Debug and Logging

#### **Enable Debug Mode**
```python
# Enhanced logging and error details
ENABLE_DEBUG_LOGGING = True
DEBUG_LOG_FILE = 'debug.log'
LOG_LEVEL = 'INFO'  # DEBUG, INFO, WARNING, ERROR

# Save raw scraped content for debugging
SAVE_RAW_CONTENT = True
RAW_CONTENT_DIR = 'debug/raw_content'
```

#### **Verbose Output**
```python
# Show detailed processing steps
VERBOSE_MODE = True

# Display processing statistics
SHOW_PERFORMANCE_STATS = True

# Log all API requests/responses
LOG_API_CALLS = True
```

### Security Settings

#### **Data Privacy**
```python
# Don't save sensitive content
EXCLUDE_PERSONAL_DATA = True

# Mask API keys in logs
MASK_API_KEYS_IN_LOGS = True

# Secure temporary file handling
SECURE_TEMP_FILES = True
TEMP_FILE_DIR = '/tmp/firecrawl_secure'
```

#### **Content Filtering**
```python
# Skip certain content types
SKIP_LOGIN_PAGES = True
SKIP_ERROR_PAGES = True
MIN_CONTENT_LENGTH = 100      # Skip pages with minimal content

# Content restrictions
ALLOWED_DOMAINS = []          # Empty = allow all
BLOCKED_DOMAINS = ['spam.com', 'malware.site']
```

---

## 🎨 UI and Experience Settings

### Interface Customization

#### **Display Options**
```python
# Customize console output
SHOW_EMOJIS = True            # Disable for plain terminals
COLORED_OUTPUT = True         # Disable for plain terminals  
PROGRESS_BARS = True          # Show progress indicators

# Menu behavior
AUTO_SAVE_REPORTS = False     # Skip save prompt
CONFIRM_DESTRUCTIVE_ACTIONS = True  # Confirm resets/deletions
```

#### **Language and Localization**
```python
# Date formats
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"    # International
DATE_FORMAT = "%m/%d/%Y %I:%M %p"    # US format

# Number formats
USE_METRIC_UNITS = True       # MB, GB vs MiB, GiB
DECIMAL_PLACES = 2            # Precision for statistics
```

### User Experience

#### **Workflow Optimization**  
```python
# Remember user preferences
REMEMBER_LAST_MODEL = True
REMEMBER_LAST_FORMAT = True
REMEMBER_LAST_TASK_TYPE = True

# Quick actions
ENABLE_KEYBOARD_SHORTCUTS = True
QUICK_ANALYSIS_MODE = False   # Skip confirmations for power users
```

---

## 🌐 Environment-Specific Configuration

### Development Environment
```python
# config_dev.py
FIRECRAWL_API_KEY = "fc-dev-key"
REPORTS_DIR = 'dev_reports'
ENABLE_DEBUG_LOGGING = True
OLLAMA_HOST = "http://localhost:11434"
DEFAULT_SAVE_FORMAT = 'json'  # For testing
```

### Production Environment
```python
# config_prod.py  
FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY')
REPORTS_DIR = '/var/reports'
ENABLE_DEBUG_LOGGING = False
PROCESSING_TIMEOUT = 600
DEFAULT_SAVE_FORMAT = 'html_charts'
```

### Testing Environment
```python
# config_test.py
FIRECRAWL_API_KEY = "fc-test-key"
REPORTS_DIR = 'test_reports'
MAX_CONTENT_LENGTH = 1000     # Faster testing
PROCESSING_TIMEOUT = 60
SAVE_RAW_CONTENT = True       # For test verification
```

---

## 🔧 Configuration Management

### Using Multiple Configurations

#### **Environment-Based Loading**
```python
# Load different configs based on environment
import os

ENV = os.getenv('APP_ENV', 'development')

if ENV == 'production':
    from config_prod import *
elif ENV == 'testing':
    from config_test import *
else:
    from config_dev import *
```

#### **Command Line Override**
```bash
# Set environment before running
APP_ENV=production python universal_firecrawl_ollama.py

# Override specific settings
REPORTS_DIR=/tmp/reports python universal_firecrawl_ollama.py
```

### Configuration Validation

#### **Automatic Validation**
```python
# System automatically validates:
# - API key format (starts with 'fc-')
# - Directory permissions (writable)
# - Ollama connectivity
# - Model availability
```

#### **Manual Validation**
```python
# Test configuration without running full system
python -c "
import config
print('API Key:', config.FIRECRAWL_API_KEY[:8] + '...')
print('Reports Dir:', config.REPORTS_DIR)
print('Default Format:', config.DEFAULT_SAVE_FORMAT)
"
```

### Configuration Backup and Restore

#### **Backup Configuration**
```bash
# Backup current config
cp config.py config_backup_$(date +%Y%m%d).py

# Backup entire reports directory
tar -czf reports_backup_$(date +%Y%m%d).tar.gz firecrawl_reports/
```

#### **Restore Configuration**
```bash
# Restore from backup
cp config_backup_20241219.py config.py

# Reset to defaults (use Configuration Menu)
# Option 6 → Option 4 → Reset Configuration
```

---

## 📋 Configuration Templates

### Basic User Template
```python
# config.py - Basic Configuration
import os

# Required Settings
FIRECRAWL_API_KEY = "fc-your-key-here"
OLLAMA_HOST = "http://localhost:11434"

# Basic Customization
REPORTS_DIR = 'my_reports'
DEFAULT_SAVE_FORMAT = 'html'
```

### Power User Template  
```python
# config.py - Advanced Configuration
import os
from datetime import datetime

# API Configuration
FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY')
OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'http://localhost:11434')

# Dynamic Reports Directory
PROJECT = os.getenv('PROJECT_NAME', 'general')
REPORTS_DIR = f'reports/{PROJECT}/{datetime.now().strftime("%Y-%m")}'

# Performance Optimization
DEFAULT_SAVE_FORMAT = 'html_charts'
MAX_CONTENT_LENGTH = 15000
PROCESSING_TIMEOUT = 450

# Model Preferences
PREFERRED_MODELS = {
    'fast': 'llama3.2:latest',
    'reasoning': 'qwen3:latest', 
    'coding': 'qwen2.5-coder:latest',
    'comprehensive': 'phi4:latest'
}

# Advanced Features
ENABLE_DEBUG_LOGGING = True
VERBOSE_MODE = True
SAVE_RAW_CONTENT = False
```

### Enterprise Template
```python
# config.py - Enterprise Configuration
import os
import logging

# Security and Compliance
FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY')
MASK_API_KEYS_IN_LOGS = True
SECURE_TEMP_FILES = True

# Centralized Storage
REPORTS_DIR = os.getenv('REPORTS_BASE_DIR', '/shared/reports')
ARCHIVE_OLD_REPORTS = True
ARCHIVE_AFTER_DAYS = 90

# Performance and Reliability
PROCESSING_TIMEOUT = 900
MAX_RETRIES = 5
RETRY_DELAY = 5

# Audit and Logging
ENABLE_DEBUG_LOGGING = True
LOG_LEVEL = 'INFO'
DEBUG_LOG_FILE = f'/var/log/firecrawl-ollama/{os.getenv("USER")}.log'

# Content Restrictions
MIN_CONTENT_LENGTH = 500
BLOCKED_DOMAINS = ['internal.corp.com', 'confidential.example.com']
```

---

## 🔍 Configuration Troubleshooting

### Common Configuration Issues

#### **Config File Not Found**
```bash
# Error: config.py doesn't exist
# Solution: Run system once to auto-create, or copy from config_example.py
cp config_example.py config.py
```

#### **Permission Errors**
```bash
# Error: Can't write to reports directory
# Solution: Check directory permissions
chmod 755 firecrawl_reports/
# Or change to writable directory in config
```

#### **Invalid API Key Format**
```python
# Error: API key validation failed
# Solution: Ensure key starts with 'fc-' and is complete
FIRECRAWL_API_KEY = "fc-complete-key-here"  # ✅ Correct
FIRECRAWL_API_KEY = "incomplete-key"        # ❌ Wrong
```

### Configuration Testing

#### **Test Configuration**
```bash
# Quick config test
python -c "
try:
    import config
    print('✅ Configuration loaded successfully')
    print(f'Reports Dir: {config.REPORTS_DIR}')
    print(f'API Key: {config.FIRECRAWL_API_KEY[:8]}...')
except Exception as e:
    print(f'❌ Configuration error: {e}')
"
```

#### **Validate Settings**
```python
# Add to config.py for self-validation
def validate_config():
    """Validate configuration settings"""
    import os
    
    # Check API key
    if not FIRECRAWL_API_KEY.startswith('fc-'):
        raise ValueError("Invalid Firecrawl API key format")
    
    # Check reports directory
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)
        print(f"Created reports directory: {REPORTS_DIR}")
    
    # Check Ollama connectivity
    import requests
    try:
        resp = requests.get(f"{OLLAMA_HOST}/api/version", timeout=5)
        print("✅ Ollama connection successful")
    except:
        print("⚠️ Ollama connection failed")

# Uncomment to run validation when config is imported
# validate_config()
```

---

## 🎯 Best Practices

### Configuration Management

#### **✅ Do This**:
- Keep `config.py` in `.gitignore`
- Use environment variables for sensitive data
- Document custom settings with comments
- Backup configuration before major changes
- Test configuration changes in development first

#### **❌ Avoid This**:
- Hardcoding API keys in shared code
- Storing credentials in version control
- Making changes directly in production
- Ignoring configuration validation errors

### Security Best Practices

#### **API Key Security**:
```python
# ✅ Good practices
FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY')  # Environment variable
FIRECRAWL_API_KEY = input("Enter API key: ")        # Runtime input

# ❌ Bad practices  
FIRECRAWL_API_KEY = "fc-1234567890abcdef"          # Hardcoded
# Never commit API keys to version control
```

#### **File Permissions**:
```bash
# Secure configuration file
chmod 600 config.py          # Owner read/write only
chmod 700 firecrawl_reports/ # Owner access only
```

### Performance Optimization

#### **Resource Management**:
```python
# Optimize for your system
if TOTAL_RAM_GB < 8:
    MAX_CONTENT_LENGTH = 5000
    PREFERRED_MODELS['comprehensive'] = 'llama3.2'  # Use smaller model
elif TOTAL_RAM_GB >= 16:
    MAX_CONTENT_LENGTH = 20000
    PROCESSING_TIMEOUT = 600
```

#### **Network Optimization**:
```python
# Adjust for your connection speed
if CONNECTION_SPEED == 'slow':
    FIRECRAWL_TIMEOUT = 120
    MAX_RETRIES = 5
elif CONNECTION_SPEED == 'fast':
    FIRECRAWL_TIMEOUT = 30
    MAX_RETRIES = 2
```

---

**Need Help with Configuration?**

- 🔧 [Troubleshooting Guide](TROUBLESHOOTING.md) for common issues
- 📖 [Usage Guide](USAGE.md) for practical examples
- 💬 [GitHub Discussions](../../discussions) for configuration questions
- 🐛 [GitHub Issues](../../issues) for configuration bugs

**Remember**: The system works great with default settings! Only customize if you have specific needs. 🚀