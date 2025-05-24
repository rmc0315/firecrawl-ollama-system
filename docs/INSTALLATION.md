# 🚀 Installation Guide

Complete installation instructions for the Universal Firecrawl + Ollama Integration System.

## 📋 Prerequisites

### System Requirements
- **Python 3.8+** (Python 3.9+ recommended)
- **4GB+ RAM** (for running AI models)
- **Internet connection** (for web scraping)
- **2GB+ free disk space** (for models and reports)

### Required Services
- **[Ollama](https://ollama.com)** - Local AI runtime
- **[Firecrawl API Key](https://firecrawl.dev)** - Web scraping service (free tier available)

---

## 🎯 Quick Start (Recommended)

### Option 1: Automated Setup
```bash
# Clone the repository
git clone https://github.com/rmc0315/firecrawl-ollama-system.git
cd firecrawl-ollama-system

# Run automated setup
python setup.py
```

### Option 2: Windows Users
```cmd
# Clone the repository
git clone https://github.com/rmc0315/firecrawl-ollama-system.git
cd firecrawl-ollama-system

# Run Windows-optimized setup
python setup_windows.py
```

The setup script will:
- ✅ Check Python compatibility
- ✅ Install all dependencies
- ✅ Verify Ollama installation
- ✅ Test Firecrawl connection
- ✅ Create launcher scripts
- ✅ Set up configuration files

---

## 🔧 Manual Installation

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Install Ollama

#### Windows
1. Download from [ollama.com/download/windows](https://ollama.com/download/windows)
2. Run the installer
3. Open Command Prompt and run: `ollama serve`

#### macOS
```bash
# Option 1: Download installer
# Visit: https://ollama.com/download/mac

# Option 2: Homebrew
brew install ollama
```

#### Linux
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Step 3: Install AI Models
```bash
# Install recommended models
ollama pull llama3.2        # Fast analysis (2GB)
ollama pull qwen3           # Deep reasoning (5GB)
ollama pull qwen2.5-coder   # Structured data (4.7GB)
ollama pull phi4            # Comprehensive analysis (9GB)

# Or start with just one model
ollama pull llama3.2
```

### Step 4: Get Firecrawl API Key
1. Visit [firecrawl.dev](https://firecrawl.dev)
2. Sign up for free account
3. Get your API key from the dashboard
4. The system will prompt you to enter it on first run

### Step 5: Run the System
```bash
python universal_firecrawl_ollama.py
```

---

## 🖥️ Platform-Specific Instructions

### Windows Setup

#### Using PowerShell
```powershell
# Enable script execution (if needed)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Clone and setup
git clone https://github.com/rmc0315/firecrawl-ollama-system.git
cd firecrawl-ollama-system
python setup_windows.py

# Launch the system
.\launch.bat
# or
.\launch.ps1
```

#### Using Command Prompt
```cmd
git clone https://github.com/rmc0315/firecrawl-ollama-system.git
cd firecrawl-ollama-system
python setup_windows.py

# Launch the system
launch.bat
```

### macOS/Linux Setup

```bash
# Clone repository
git clone https://github.com/rmc0315/firecrawl-ollama-system.git
cd firecrawl-ollama-system

# Run setup
python3 setup.py

# Make launcher executable and run
chmod +x launch.sh
./launch.sh
```

---

## 🐳 Docker Installation (Coming Soon)

```bash
# Pull the image
docker pull firecrawl-ollama-system:latest

# Run with GPU support
docker run --gpus all -it firecrawl-ollama-system

# Run CPU-only
docker run -it firecrawl-ollama-system
```

---

## ⚙️ Configuration

### Environment Variables (Optional)
```bash
# Set API key to skip prompts
export FIRECRAWL_API_KEY="fc-your-api-key-here"

# Custom Ollama host
export OLLAMA_HOST="http://localhost:11434"
```

### Windows Environment Variables
```cmd
# Command Prompt
set FIRECRAWL_API_KEY=fc-your-api-key-here

# PowerShell
$env:FIRECRAWL_API_KEY="fc-your-api-key-here"
```

### Configuration File
The system creates `config.py` automatically, or you can create it manually:

```python
# config.py
FIRECRAWL_API_KEY = "fc-your-api-key-here"
OLLAMA_HOST = "http://localhost:11434"
REPORTS_DIR = "firecrawl_reports"
DEFAULT_SAVE_FORMAT = "html"
```

---

## 🧪 Testing Installation

### Quick Test
```bash
# Test Ollama
ollama list

# Test Python packages
python -c "import firecrawl, ollama; print('✅ Dependencies OK')"

# Run system test
python universal_firecrawl_ollama.py
```

### Comprehensive Test
1. Run the system: `python universal_firecrawl_ollama.py`
2. Choose option 1 (Single Website Analysis)
3. Enter URL: `https://example.com`
4. Enter task: `What is this website about?`
5. Select any available model
6. Verify analysis completes and offers to save report

---

## 🚨 Troubleshooting

### Common Issues

#### "No module named 'firecrawl'"
```bash
# Ensure you're in the right virtual environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate.bat  # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

#### "Ollama connection failed"
```bash
# Start Ollama service
ollama serve

# Check if running
curl http://localhost:11434/api/tags
```

#### "No models detected"
```bash
# Install at least one model
ollama pull llama3.2

# Check installed models
ollama list
```

#### "Permission denied" (Linux/Mac)
```bash
# Make scripts executable
chmod +x launch.sh
chmod +x setup.py
```

### Getting Help
- 📖 Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- 🐛 Report issues on [GitHub](https://github.com/rmc0315/firecrawl-ollama-system/issues)
- 💬 Join our [Discord community](https://discord.gg/your-server)

---

## 🎯 What's Next?

After installation:
1. **Run your first analysis** - Try option 1 with a simple website
2. **Explore model comparison** - See how different AI models analyze the same content
3. **Generate reports** - Try different export formats
4. **Configure settings** - Use option 6 to customize your setup
5. **Join the community** - Share your results and get help

**Ready to analyze the web with local AI? Let's go!** 🚀