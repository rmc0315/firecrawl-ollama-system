#!/usr/bin/env python3
"""
Easy setup script for Universal Firecrawl + Ollama System
Automatically installs dependencies and guides users through setup
"""

import subprocess
import sys
import os
import platform

def run_command(command, description):
    """Run command with nice output"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed")
            return True
        else:
            print(f"❌ {description} failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ {description} failed: {e}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python 3.8+ required. You have {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor} - Compatible")
    return True

def install_dependencies():
    """Install required packages"""
    print("\n📦 Installing Dependencies...")
    
    packages = [
        "firecrawl-py>=0.0.8",
        "ollama>=0.1.7", 
        "requests>=2.31.0",
        "reportlab>=4.0.4",
        "Pillow>=10.0.0"
    ]
    
    for package in packages:
        if not run_command(f"pip install {package}", f"Installing {package}"):
            print(f"⚠️ Failed to install {package}, but continuing...")
    
    return True

def check_ollama():
    """Check if Ollama is installed and running"""
    print("\n🤖 Checking Ollama...")
    
    # Check if ollama command exists
    if not run_command("ollama --version", "Checking Ollama installation"):
        print("\n❌ Ollama not found!")
        print("💡 Install Ollama:")
        
        if platform.system() == "Windows":
            print("  1. Download from: https://ollama.com/download/windows")
            print("  2. Run the installer")
        elif platform.system() == "Darwin":  # macOS
            print("  1. Download from: https://ollama.com/download/mac")
            print("  2. Or use Homebrew: brew install ollama")
        else:  # Linux
            print("  1. Run: curl -fsSL https://ollama.com/install.sh | sh")
            print("  2. Or download from: https://ollama.com/download/linux")
        
        return False
    
    # Check if Ollama server is running
    import requests
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            print("✅ Ollama server is running")
            
            # Check for models
            models = response.json().get('models', [])
            if models:
                print(f"✅ Found {len(models)} installed models")
                for model in models[:3]:  # Show first 3
                    print(f"  • {model['name']}")
                if len(models) > 3:
                    print(f"  ... and {len(models) - 3} more")
            else:
                print("⚠️ No models installed")
                print("💡 Install a model: ollama pull llama3.2")
            
            return True
        else:
            print("❌ Ollama server not responding")
            return False
            
    except Exception:
        print("❌ Ollama server not running")
        print("💡 Start Ollama: ollama serve")
        return False

def setup_firecrawl():
    """Help user setup Firecrawl"""
    print("\n🔥 Firecrawl Setup...")
    
    api_key = os.getenv('FIRECRAWL_API_KEY')
    if api_key:
        print("✅ FIRECRAWL_API_KEY environment variable found")
        return True
    
    print("🔑 Firecrawl API Key needed:")
    print("  1. Visit: https://firecrawl.dev")
    print("  2. Sign up for free account")
    print("  3. Get your API key")
    print("  4. Set environment variable: FIRECRAWL_API_KEY")
    print("\n💡 Or enter it when prompted by the application")
    
    return True

def create_example_config():
    """Create example configuration file"""
    config_content = """# Universal Firecrawl + Ollama Configuration
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
"""
    
    with open('config_example.py', 'w', encoding='utf-8') as f:
        f.write(config_content)
    
    print("✅ Created config_example.py")

def create_launcher_script():
    """Create easy launcher script"""
    
    # Windows batch file
    if platform.system() == "Windows":
        launcher_content = """@echo off
echo Starting Universal Firecrawl + Ollama System...
echo.

REM Try to detect and activate virtual environment
if exist "venv\\Scripts\\activate.bat" (
    echo Activating virtual environment...
    call venv\\Scripts\\activate.bat
) else if exist ".venv\\Scripts\\activate.bat" (
    echo Activating virtual environment...
    call .venv\\Scripts\\activate.bat
) else if exist "..\\venv\\Scripts\\activate.bat" (
    echo Activating virtual environment...
    call ..\\venv\\Scripts\\activate.bat
) else (
    echo Warning: No virtual environment found, using system Python
)

echo.
echo Running Universal Firecrawl + Ollama System...
echo.

python universal_firecrawl_ollama.py

echo.
echo System finished.
pause
"""
        with open('launch.bat', 'w', encoding='utf-8') as f:
            f.write(launcher_content)
        print("✅ Created launch.bat with virtual environment support")
    
    # Unix shell script
    launcher_content = """#!/bin/bash
echo "Starting Universal Firecrawl + Ollama System..."
python3 universal_firecrawl_ollama.py
"""
    with open('launch.sh', 'w', encoding='utf-8') as f:
        f.write(launcher_content)
    
    # Make executable on Unix systems
    if platform.system() != "Windows":
        os.chmod('launch.sh', 0o755)
        print("✅ Created launch.sh")

def main():
    """Main setup function"""
    print("🔥" * 50)
    print("🚀 UNIVERSAL FIRECRAWL + OLLAMA SETUP")
    print("🔥" * 50)
    print("\nThis script will help you set up the system on ANY computer!")
    
    # Check Python version
    if not check_python_version():
        return
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Dependency installation failed")
        return
    
    # Check Ollama
    ollama_ok = check_ollama()
    
    # Setup Firecrawl
    firecrawl_ok = setup_firecrawl()
    
    # Create config and launcher
    create_example_config()
    create_launcher_script()
    
    # Summary
    print("\n" + "="*60)
    print("🎯 SETUP SUMMARY")
    print("="*60)
    print(f"✅ Python: Compatible")
    print(f"✅ Dependencies: Installed")
    print(f"{'✅' if ollama_ok else '❌'} Ollama: {'Ready' if ollama_ok else 'Needs setup'}")
    print(f"{'✅' if firecrawl_ok else '⚠️'} Firecrawl: {'Ready' if firecrawl_ok else 'API key needed'}")
    print(f"✅ Config: config_example.py created")
    print(f"✅ Launcher: Scripts created")
    
    if ollama_ok and firecrawl_ok:
        print("\n🎉 SETUP COMPLETE!")
        print("🚀 Run the system:")
        if platform.system() == "Windows":
            print("  • Double-click launch.bat")
        print("  • Or run: python universal_firecrawl_ollama.py")
    else:
        print("\n⚠️ SETUP NEEDS ATTENTION:")
        if not ollama_ok:
            print("  • Install and start Ollama")
            print("  • Install at least one model: ollama pull llama3.2")
        if not firecrawl_ok:
            print("  • Get Firecrawl API key from https://firecrawl.dev")
        
        print("\n🔄 Run setup again after fixing issues")
    
    print("\n📚 Documentation:")
    print("  • Ollama: https://ollama.com")
    print("  • Firecrawl: https://firecrawl.dev")
    print("  • This project: See README.md")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Setup cancelled")
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        print("Please report this issue")