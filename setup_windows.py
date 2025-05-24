#!/usr/bin/env python3
"""
Windows-compatible setup script for Universal Firecrawl + Ollama System
Handles encoding issues and provides fallbacks
"""

import subprocess
import sys
import os
import platform

def safe_print(text):
    """Print text safely on Windows with emoji fallbacks"""
    try:
        print(text)
    except UnicodeEncodeError:
        # Fallback without emojis for Windows
        safe_text = text.encode('ascii', 'ignore').decode('ascii')
        print(safe_text)

def run_command(command, description):
    """Run command with nice output"""
    safe_print(f"Installing {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            safe_print(f"✓ {description} completed")
            return True
        else:
            safe_print(f"✗ {description} failed: {result.stderr}")
            return False
    except Exception as e:
        safe_print(f"✗ {description} failed: {e}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        safe_print(f"✗ Python 3.8+ required. You have {version.major}.{version.minor}")
        return False
    safe_print(f"✓ Python {version.major}.{version.minor} - Compatible")
    return True

def install_dependencies():
    """Install required packages"""
    safe_print("\nInstalling Dependencies...")
    
    packages = [
        "firecrawl-py>=0.0.8",
        "ollama>=0.1.7", 
        "requests>=2.31.0",
        "reportlab>=4.0.4",
        "Pillow>=10.0.0"
    ]
    
    success_count = 0
    for package in packages:
        if run_command(f"pip install {package}", package):
            success_count += 1
        else:
            safe_print(f"Warning: Failed to install {package}, but continuing...")
    
    safe_print(f"Installed {success_count}/{len(packages)} packages successfully")
    return success_count > 0

def check_ollama():
    """Check if Ollama is installed and running"""
    safe_print("\nChecking Ollama...")
    
    # Check if ollama command exists
    if not run_command("ollama --version", "Ollama installation check"):
        safe_print("\n✗ Ollama not found!")
        safe_print("Install Ollama:")
        
        if platform.system() == "Windows":
            safe_print("  1. Download from: https://ollama.com/download/windows")
            safe_print("  2. Run the installer")
        elif platform.system() == "Darwin":  # macOS
            safe_print("  1. Download from: https://ollama.com/download/mac")
            safe_print("  2. Or use Homebrew: brew install ollama")
        else:  # Linux
            safe_print("  1. Run: curl -fsSL https://ollama.com/install.sh | sh")
            safe_print("  2. Or download from: https://ollama.com/download/linux")
        
        return False
    
    # Check if Ollama server is running
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            safe_print("✓ Ollama server is running")
            
            # Check for models
            models = response.json().get('models', [])
            if models:
                safe_print(f"✓ Found {len(models)} installed models")
                for model in models[:3]:  # Show first 3
                    safe_print(f"  • {model['name']}")
                if len(models) > 3:
                    safe_print(f"  ... and {len(models) - 3} more")
            else:
                safe_print("Warning: No models installed")
                safe_print("Install a model: ollama pull llama3.2")
            
            return True
        else:
            safe_print("✗ Ollama server not responding")
            return False
            
    except Exception as e:
        safe_print("✗ Ollama server not running")
        safe_print("Start Ollama: ollama serve")
        return False

def setup_firecrawl():
    """Help user setup Firecrawl"""
    safe_print("\nFirecrawl Setup...")
    
    api_key = os.getenv('FIRECRAWL_API_KEY')
    if api_key:
        safe_print("✓ FIRECRAWL_API_KEY environment variable found")
        return True
    
    safe_print("Firecrawl API Key needed:")
    safe_print("  1. Visit: https://firecrawl.dev")
    safe_print("  2. Sign up for free account")
    safe_print("  3. Get your API key")
    safe_print("  4. Set environment variable: FIRECRAWL_API_KEY")
    safe_print("\nOr enter it when prompted by the application")
    
    return True

def create_files():
    """Create configuration and launcher files"""
    safe_print("\nCreating configuration files...")
    
    # Create config example
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
    
    try:
        with open('config_example.py', 'w', encoding='utf-8') as f:
            f.write(config_content)
        safe_print("✓ Created config_example.py")
    except Exception as e:
        safe_print(f"✗ Failed to create config file: {e}")
    
    # Create platform-specific launchers
    current_platform = platform.system()
    safe_print(f"\nCreating launchers for {current_platform}...")
    
    # Windows launchers
    if current_platform == "Windows":
        # Batch file launcher
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
        try:
            with open('launch.bat', 'w', encoding='utf-8') as f:
                f.write(launcher_content)
            safe_print("✓ Created launch.bat (double-click to run)")
        except Exception as e:
            safe_print(f"✗ Failed to create launch.bat: {e}")
        
        # PowerShell launcher
        ps_launcher = """Write-Host "Starting Universal Firecrawl + Ollama System..." -ForegroundColor Green
Write-Host ""

# Try to detect and activate virtual environment
if (Test-Path "venv\\Scripts\\Activate.ps1") {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & .\\venv\\Scripts\\Activate.ps1
} elseif (Test-Path ".venv\\Scripts\\Activate.ps1") {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & .\\.venv\\Scripts\\Activate.ps1
} elseif (Test-Path "..\\venv\\Scripts\\Activate.ps1") {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & ..\\venv\\Scripts\\Activate.ps1
} else {
    Write-Host "Warning: No virtual environment found, using system Python" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Running Universal Firecrawl + Ollama System..." -ForegroundColor Green
Write-Host ""

python universal_firecrawl_ollama.py

Write-Host ""
Write-Host "System finished." -ForegroundColor Green
Read-Host "Press Enter to exit"
"""
        try:
            with open('launch.ps1', 'w', encoding='utf-8') as f:
                f.write(ps_launcher)
            safe_print("✓ Created launch.ps1 (PowerShell alternative)")
        except Exception as e:
            safe_print(f"Warning: Could not create launch.ps1: {e}")
    
    # Unix launchers (Linux/Mac)
    elif current_platform in ["Linux", "Darwin"]:
        launcher_content = """#!/bin/bash
echo "Starting Universal Firecrawl + Ollama System..."
echo

# Try to detect and activate virtual environment
if [ -f "venv/bin/activate" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
elif [ -f ".venv/bin/activate" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
elif [ -f "../venv/bin/activate" ]; then
    echo "Activating virtual environment..."
    source ../venv/bin/activate
else
    echo "Warning: No virtual environment found, using system Python"
fi

echo
echo "Running Universal Firecrawl + Ollama System..."
echo

python3 universal_firecrawl_ollama.py

echo
echo "System finished."
read -p "Press Enter to exit..."
"""
        try:
            with open('launch.sh', 'w', encoding='utf-8') as f:
                f.write(launcher_content)
            os.chmod('launch.sh', 0o755)  # Make executable
            
            platform_name = "macOS" if current_platform == "Darwin" else "Linux"
            safe_print(f"✓ Created launch.sh ({platform_name} launcher)")
            safe_print("  Run with: ./launch.sh")
        except Exception as e:
            safe_print(f"Warning: Could not create launch.sh: {e}")
    
    else:
        safe_print(f"Unknown platform: {current_platform}, skipping launcher creation")

def main():
    """Main setup function"""
    safe_print("=" * 50)
    safe_print("UNIVERSAL FIRECRAWL + OLLAMA SETUP")
    safe_print("=" * 50)
    safe_print("\nThis script will help you set up the system on ANY computer!")
    
    # Check Python version
    if not check_python_version():
        input("\nPress Enter to exit...")
        return
    
    # Install dependencies
    if not install_dependencies():
        safe_print("✗ Dependency installation failed")
        input("\nPress Enter to exit...")
        return
    
    # Check Ollama
    ollama_ok = check_ollama()
    
    # Setup Firecrawl
    firecrawl_ok = setup_firecrawl()
    
    # Create config and launcher
    create_files()
    
    # Summary
    safe_print("\n" + "="*60)
    safe_print("SETUP SUMMARY")
    safe_print("="*60)
    safe_print("✓ Python: Compatible")
    safe_print("✓ Dependencies: Installed")
    safe_print(f"{'✓' if ollama_ok else '✗'} Ollama: {'Ready' if ollama_ok else 'Needs setup'}")
    safe_print(f"{'✓' if firecrawl_ok else '!'} Firecrawl: {'Ready' if firecrawl_ok else 'API key needed'}")
    safe_print("✓ Config: config_example.py created")
    safe_print("✓ Launcher: Scripts created")
    
    if ollama_ok and firecrawl_ok:
        safe_print("\nSETUP COMPLETE!")
        safe_print("Run the system:")
        if platform.system() == "Windows":
            safe_print("  • Double-click launch.bat")
        safe_print("  • Or run: python universal_firecrawl_ollama.py")
    else:
        safe_print("\nSETUP NEEDS ATTENTION:")
        if not ollama_ok:
            safe_print("  • Install and start Ollama")
            safe_print("  • Install at least one model: ollama pull llama3.2")
        if not firecrawl_ok:
            safe_print("  • Get Firecrawl API key from https://firecrawl.dev")
        
        safe_print("\nRun setup again after fixing issues")
    
    safe_print("\nDocumentation:")
    safe_print("  • Ollama: https://ollama.com")
    safe_print("  • Firecrawl: https://firecrawl.dev")
    safe_print("  • This project: See README.md")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        safe_print("\n\nSetup cancelled")
    except Exception as e:
        safe_print(f"\nSetup failed: {e}")
        safe_print("Please report this issue")
        input("\nPress Enter to exit...")