# 🔧 Troubleshooting Guide

Complete solutions for common issues with the Universal Firecrawl + Ollama Integration System.

## 🚨 Quick Fixes for Common Issues

### System Won't Start
```bash
# Error: "No module named 'firecrawl'"
pip install -r requirements.txt

# Error: "Command 'python' not found"
python3 universal_firecrawl_ollama.py

# Error: "Permission denied"
chmod +x universal_firecrawl_ollama.py
```

### Can't Connect to Services
```bash
# Ollama not responding
ollama serve

# Firecrawl API issues
# Check your API key in Configuration Settings (option 6)
```

---

## 🔥 Ollama Issues

### Problem: "❌ Could not connect to Ollama"

#### **Symptoms**:
- System can't detect Ollama
- Error: "Connection refused" or "No response from Ollama"
- Models not detected

#### **Solutions**:

**1. Check if Ollama is Running**
```bash
# Check Ollama status
curl http://localhost:11434/api/tags

# If no response, start Ollama
ollama serve
```

**2. Verify Ollama Installation**
```bash
# Check Ollama version
ollama --version

# If command not found, reinstall Ollama:
# Windows: Download from https://ollama.com/download/windows
# macOS: brew install ollama
# Linux: curl -fsSL https://ollama.com/install.sh | sh
```

**3. Check Ollama Port**
```bash
# Default port is 11434
netstat -an | grep 11434

# If using different port, set environment variable:
export OLLAMA_HOST="http://localhost:YOUR_PORT"
```

**4. Firewall Issues**
```bash
# Windows: Allow Ollama through Windows Firewall
# macOS: System Preferences → Security & Privacy → Firewall
# Linux: Check iptables/ufw rules
```

### Problem: "❌ No models detected"

#### **Symptoms**:
- Ollama connects but no models found
- Empty model list
- "No working models" error

#### **Solutions**:

**1. Install Models**
```bash
# Check what models you have
ollama list

# If empty, install recommended models
ollama pull llama3.2        # Fast model (2GB)
ollama pull qwen3           # Reasoning model (5GB)
ollama pull qwen2.5-coder   # Coding model (4.7GB)
ollama pull phi4            # Comprehensive model (9GB)

# Start with smallest model if storage is limited
ollama pull llama3.2
```

**2. Verify Model Installation**
```bash
# List installed models
ollama list

# Test a model manually
ollama run llama3.2 "Hello world"
```

**3. Model Compatibility Issues**
```bash
# Some models might be corrupted, reinstall
ollama rm problematic-model
ollama pull problematic-model

# Clear Ollama cache (if needed)
# Windows: %USERPROFILE%\.ollama
# macOS: ~/.ollama
# Linux: ~/.ollama
```

### Problem: "✗ Chat test failed with [model]"

#### **Symptoms**:
- Model detected but won't respond
- Timeout errors during model testing
- "Model is required" error

#### **Solutions**:

**1. Model Name Issues**
```bash
# Use exact model names from ollama list
ollama list

# Common naming variations:
# ✓ llama3.2:latest or llama3.2
# ✓ qwen3:latest or qwen3
# ✗ llama3.2-latest (incorrect format)
```

**2. Resource Issues**
```bash
# Check system resources
# RAM usage: Task Manager (Windows) / Activity Monitor (macOS) / htop (Linux)
# Close other applications if RAM is low

# For large models (13B+), you need:
# - 16GB+ RAM for decent performance
# - Consider using smaller models instead
```

**3. Model Corruption**
```bash
# Re-download corrupted model
ollama rm [model-name]
ollama pull [model-name]
```

---

## 🔥 Firecrawl Issues

### Problem: "❌ Firecrawl connection failed"

#### **Symptoms**:
- Can't connect to Firecrawl API
- "Request Timeout" errors
- "API key" errors

#### **Solutions**:

**1. API Key Issues**
```bash
# Check your API key
# Go to Configuration Settings (option 6) → Update Firecrawl API Key
# Or set environment variable:
export FIRECRAWL_API_KEY="fc-your-actual-key-here"

# Verify key format: should start with "fc-"
# Get new key from: https://firecrawl.dev
```

**2. Network/Connectivity Issues**
```bash
# Test internet connection
ping firecrawl.dev

# Check if corporate firewall is blocking
curl https://api.firecrawl.dev/v1/

# Try different network (mobile hotspot) to isolate issue
```

**3. Account/Credit Issues**
```bash
# Check your Firecrawl dashboard:
# - Account status
# - API usage/limits
# - Available credits
# Visit: https://firecrawl.dev/dashboard
```

### Problem: "Request Timeout" during scraping

#### **Symptoms**:
- Scraping starts but times out
- Works with some sites but not others
- Intermittent failures

#### **Solutions**:

**1. Try Different Websites**
```bash
# Test with simple sites first:
# ✓ https://example.com
# ✓ https://httpbin.org/html
# ✓ https://jsonplaceholder.typicode.com

# Avoid initially:
# ✗ Very large/complex sites
# ✗ Sites with heavy JavaScript
# ✗ Sites requiring authentication
```

**2. Network Optimization**
```bash
# Use wired connection instead of WiFi
# Close bandwidth-heavy applications
# Try during off-peak hours
# Consider VPN if regional issues
```

**3. Site-Specific Issues**
```bash
# Some sites block automated requests
# Try different pages on the same site
# Check if site has robots.txt restrictions
# Look for API alternatives for the data you need
```

---

## 🐍 Python & Installation Issues

### Problem: "No module named 'firecrawl'" or similar import errors

#### **Symptoms**:
- ImportError when starting the system
- "Module not found" errors
- Script starts but crashes immediately

#### **Solutions**:

**1. Virtual Environment Issues**
```bash
# Make sure you're in the right virtual environment
# Windows:
venv\Scripts\activate.bat

# macOS/Linux:
source venv/bin/activate

# Verify you're in venv (should see (venv) in prompt)
# Then reinstall dependencies:
pip install -r requirements.txt
```

**2. Python Path Issues**
```bash
# Check Python version
python --version  # Should be 3.8+

# If using python3:
python3 universal_firecrawl_ollama.py

# Check pip is installing to right location:
pip show firecrawl-py
```

**3. Permission Issues**
```bash
# Install with user flag if permission denied:
pip install --user -r requirements.txt

# Or use sudo (Linux/macOS):
sudo pip install -r requirements.txt
```

### Problem: "Python version compatibility"

#### **Symptoms**:
- "Python 3.8+ required" error
- Syntax errors in modern Python code
- Feature not supported in your Python version

#### **Solutions**:

**1. Upgrade Python**
```bash
# Check current version
python --version

# Windows: Download from python.org
# macOS: brew install python@3.11
# Linux: sudo apt update && sudo apt install python3.11
```

**2. Use Multiple Python Versions**
```bash
# Use specific Python version
python3.11 universal_firecrawl_ollama.py

# Create virtual environment with specific version
python3.11 -m venv venv
```

---

## 🖥️ Platform-Specific Issues

### Windows Issues

#### **Problem: "batch file not working"**
```cmd
REM Error: 'python' is not recognized
REM Solution: Use full path or add Python to PATH

REM Edit launch.bat to use:
python.exe universal_firecrawl_ollama.py
REM or:
py universal_firecrawl_ollama.py
```

#### **Problem: PowerShell execution policy**
```powershell
# Error: "cannot be loaded because running scripts is disabled"
# Solution: Change execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then run:
.\launch.ps1
```

#### **Problem: Encoding issues with emojis**
```cmd
REM If you see weird characters instead of emojis:
REM 1. Use Windows Terminal (better Unicode support)
REM 2. Or run: chcp 65001 before starting
REM 3. Set PYTHONIOENCODING=utf-8
```

### macOS Issues

#### **Problem: "Permission denied" on launch.sh**
```bash
# Make script executable
chmod +x launch.sh

# Then run:
./launch.sh
```

#### **Problem: "Command not found: python"**
```bash
# macOS uses python3 by default
python3 universal_firecrawl_ollama.py

# Or create alias in ~/.zshrc:
echo "alias python=python3" >> ~/.zshrc
source ~/.zshrc
```

### Linux Issues

#### **Problem: Missing system dependencies**
```bash
# Ubuntu/Debian:
sudo apt update
sudo apt install python3-pip python3-venv python3-dev

# CentOS/RHEL:
sudo yum install python3-pip python3-venv python3-devel

# Arch:
sudo pacman -S python-pip python-virtualenv
```

---

## 📊 Report Generation Issues

### Problem: "PDF generation failed"

#### **Symptoms**:
- PDF option available but files not created
- "reportlab not found" error
- Empty or corrupted PDF files

#### **Solutions**:

**1. Install PDF Dependencies**
```bash
# Install required packages
pip install reportlab Pillow

# If still fails, try system package:
# Ubuntu: sudo apt install python3-reportlab
# macOS: brew install python-tk
```

**2. Fallback to HTML**
```bash
# System automatically falls back to HTML
# HTML reports can be printed to PDF from browser:
# Browser → Print → Save as PDF
```

### Problem: "Charts not displaying in HTML reports"

#### **Symptoms**:
- HTML report opens but charts are blank
- JavaScript errors in browser console
- Charts show loading spinner indefinitely

#### **Solutions**:

**1. Browser Compatibility**
```bash
# Use modern browser:
# ✓ Chrome 80+, Firefox 75+, Safari 13+, Edge 80+
# ✗ Internet Explorer (not supported)

# Enable JavaScript in browser
# Disable ad blockers that might block Chart.js CDN
```

**2. Network Issues**
```bash
# Charts require internet connection for Chart.js library
# If offline, charts won't load (but text content will)
# Consider saving as plain HTML for offline use
```

### Problem: "Report files not found"

#### **Symptoms**:
- System says report saved but file doesn't exist
- "Permission denied" when saving
- Reports saved to unexpected location

#### **Solutions**:

**1. Check Reports Directory**
```bash
# Default location: ./firecrawl_reports/
# Check if directory exists and is writable
ls -la firecrawl_reports/

# Check current working directory
pwd
```

**2. Permission Issues**
```bash
# Fix permissions:
chmod 755 firecrawl_reports/

# Or change reports directory in Configuration Settings
```

---

## 🚀 Performance Issues

### Problem: "System running very slowly"

#### **Symptoms**:
- Long delays between responses
- High CPU/RAM usage
- System becomes unresponsive

#### **Solutions**:

**1. Resource Management**
```bash
# Close other applications
# Use Task Manager/Activity Monitor to check resource usage

# Switch to smaller models:
# Instead of phi4 (9GB) → use llama3.2 (2GB)
# Check available RAM: should have 2x model size free
```

**2. Model Selection**
```bash
# Use appropriate models for tasks:
# Quick summaries → llama3.2 (fast)
# Complex analysis → qwen3 (reasoning)
# Don't use phi4 for simple tasks
```

### Problem: "Ollama using too much RAM"

#### **Symptoms**:
- System RAM usage at 90%+
- Other applications crashing
- Computer becomes slow

#### **Solutions**:

**1. Model Size Management**
```bash
# Check model sizes:
ollama list

# Remove large models you don't use:
ollama rm large-model-name

# Use smaller alternatives:
# phi4 (9GB) → qwen3 (5GB) → llama3 (4.7GB) → llama3.2 (2GB)
```

**2. Ollama Configuration**
```bash
# Limit Ollama memory usage (if supported in your version)
# Set OLLAMA_MAX_LOADED_MODELS=1 to keep only one model in memory
```

---

## 🔧 Configuration Issues

### Problem: "Configuration not saving"

#### **Symptoms**:
- API key asked for every time
- Settings don't persist between sessions
- config.py not created

#### **Solutions**:

**1. File Permissions**
```bash
# Check if current directory is writable
touch test_file && rm test_file

# If permission denied, run from writable directory:
cd ~/Documents/firecrawl-ollama-system/
python universal_firecrawl_ollama.py
```

**2. Configuration File Issues**
```bash
# Check if config.py exists
ls -la config.py

# If corrupted, reset configuration:
# Go to Configuration Settings → Reset Configuration
# Or manually delete: rm config.py
```

### Problem: "Environment variables not working"

#### **Symptoms**:
- Set FIRECRAWL_API_KEY but still prompted
- OLLAMA_HOST not recognized
- Environment variables ignored

#### **Solutions**:

**1. Verify Environment Variables**
```bash
# Check if variables are set:
echo $FIRECRAWL_API_KEY
echo $OLLAMA_HOST

# Windows:
echo %FIRECRAWL_API_KEY%
echo %OLLAMA_HOST%
```

**2. Set Variables Correctly**
```bash
# Bash/Zsh:
export FIRECRAWL_API_KEY="fc-your-key"
export OLLAMA_HOST="http://localhost:11434"

# Windows CMD:
set FIRECRAWL_API_KEY=fc-your-key

# Windows PowerShell:
$env:FIRECRAWL_API_KEY="fc-your-key"
```

---

## 🌐 Network & Connectivity Issues

### Problem: "Connection timeouts"

#### **Symptoms**:
- Random connection failures
- "Request timed out" errors
- Works sometimes, fails others

#### **Solutions**:

**1. Network Stability**
```bash
# Test basic connectivity:
ping google.com
ping firecrawl.dev

# Check DNS resolution:
nslookup firecrawl.dev

# Try different DNS servers:
# 8.8.8.8 (Google)
# 1.1.1.1 (Cloudflare)
```

**2. Corporate/Firewall Issues**
```bash
# Check if corporate firewall blocks API calls
# Try from personal network/mobile hotspot
# Contact IT department about Firecrawl API access
# Ports needed: 443 (HTTPS), 11434 (Ollama)
```

### Problem: "Proxy configuration"

#### **Symptoms**:
- Behind corporate proxy
- "Proxy authentication required"
- API calls blocked

#### **Solutions**:

**1. Configure Proxy**
```bash
# Set proxy environment variables:
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080

# With authentication:
export HTTP_PROXY=http://username:password@proxy.company.com:8080
```

**2. Bypass Proxy for Local Services**
```bash
# Don't proxy Ollama (local service):
export NO_PROXY=localhost,127.0.0.1
```

---

## 🆘 Getting Help

### Before Asking for Help

**1. Check Common Issues Above**
- Most problems have solutions listed here
- Try the suggested fixes first

**2. Gather Information**
```bash
# Collect system information:
python --version
ollama --version
pip list | grep -E "(firecrawl|ollama)"

# Check error messages:
# Copy the exact error message
# Note what you were trying to do when it failed
```

**3. Test Basic Functionality**
```bash
# Test Ollama independently:
ollama list
ollama run llama3.2 "Hello"

# Test Firecrawl (if you have curl):
curl -X POST "https://api.firecrawl.dev/v1/scrape" \
  -H "Authorization: Bearer fc-your-key" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

### Where to Get Help

**1. GitHub Issues** (Best for bugs)
- 🐛 [Report Bug](../../issues/new?template=bug_report.md)
- Include system info, error messages, steps to reproduce

**2. GitHub Discussions** (Best for questions)  
- 🙋 [Ask Question](../../discussions/new?category=q-a)
- 💡 [Share Ideas](../../discussions/new?category=ideas)

**3. Documentation**
- 📖 [Installation Guide](INSTALLATION.md)
- 📚 [Usage Examples](USAGE.md)
- 📋 [README](README.md)

### How to Write a Good Bug Report

**Include This Information**:
```markdown
**System Information:**
- OS: Windows 11 / macOS 14 / Ubuntu 22.04
- Python Version: 3.11.2
- Ollama Version: 0.1.17
- Models Installed: llama3.2, qwen3

**Error Message:**
[Copy exact error message here]

**Steps to Reproduce:**
1. Started system with `python universal_firecrawl_ollama.py`
2. Selected option 1 (Single Website Analysis)
3. Entered URL: https://example.com
4. Error occurred when selecting model

**Expected Behavior:**
Should show model selection menu

**Additional Context:**
[Any other relevant information]
```

---

## 🔍 Diagnostic Commands

### Quick System Check
```bash
# Run all diagnostic commands:

echo "=== Python Check ==="
python --version
python -c "import sys; print(sys.executable)"

echo "=== Ollama Check ==="
ollama --version
ollama list
curl -s http://localhost:11434/api/tags | head -20

echo "=== Python Packages ==="
pip list | grep -E "(firecrawl|ollama|requests|reportlab)"

echo "=== System Resources ==="
# Linux/macOS:
free -h  # RAM
df -h .  # Disk space

# Windows (PowerShell):
# Get-WmiObject -Class Win32_ComputerSystem | Select TotalPhysicalMemory
```

### Network Diagnostics
```bash
echo "=== Network Check ==="
ping -c 3 google.com
ping -c 3 firecrawl.dev
nslookup firecrawl.dev

echo "=== Ollama API Check ==="
curl -s http://localhost:11434/api/version
```

---

## 📈 Preventive Measures

### Regular Maintenance

**1. Keep Dependencies Updated**
```bash
# Monthly update check:
pip list --outdated
pip install --upgrade firecrawl-py ollama requests reportlab

# Update Ollama:
# Download latest from ollama.com
```

**2. Clean Up Old Reports**
```bash
# Archive old reports (older than 30 days)
find firecrawl_reports/ -name "*.html" -mtime +30 -exec mv {} archive/ \;
```

**3. Monitor System Resources**
```bash
# Check available disk space regularly
df -h .

# Monitor Ollama memory usage
# Use system monitor to check RAM usage
```

### Best Practices

**1. Start Small**
- Test with simple websites first
- Use smaller models initially
- Save frequently to avoid losing work

**2. Resource Management**
- Close unnecessary applications
- Monitor RAM usage with large models
- Use appropriate models for each task

**3. Backup Important Reports**
- Export important analyses in multiple formats
- Keep copies of valuable reports
- Document successful workflows

---

**Still Having Issues?** 

Don't hesitate to reach out! The community is here to help:
- 💬 [GitHub Discussions](../../discussions) for questions
- 🐛 [GitHub Issues](../../issues) for bugs
- 📖 Check our other [documentation](docs/) files

**Remember**: This is an open-source project, and we rely on community feedback to improve. Your bug reports and questions help make the system better for everyone! 🚀