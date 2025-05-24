# 🔥 Universal Firecrawl + Ollama Integration System

> **A powerful, completely local AI-powered web scraping and analysis system that automatically adapts to ANY user's setup.**

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-production--ready-brightgreen.svg)]()
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()

**🎯 No hard-coded models • 🔒 100% local AI processing • 📊 Professional reports • ⚡ One-click setup**

<div align="center">

![Demo](screenshots/demo.gif)
*Automatically detects your models and creates professional analysis reports*

[📥 **Quick Start**](#-quick-start) • [📖 **Documentation**](docs/) • [🐛 **Issues**](../../issues) • [💬 **Discussions**](../../discussions)

</div>

---

## ✨ What Makes This Special?

### 🎯 **Universal Compatibility**
- **Automatically detects** your installed Ollama models
- **Works with ANY setup** - no configuration needed
- **Intelligent categorization** - Fast, Reasoning, Coding, Comprehensive models
- **Dynamic recommendations** based on task requirements

### 🔍 **Powerful Analysis**
- **Single Website Analysis** - Deep insights from any website
- **Model Comparison** - See how different AI models analyze the same content  
- **Structured Data Extraction** - Extract clean JSON from websites
- **Competitive Analysis** - Multi-competitor analysis with summaries

### 📊 **Professional Reports**
- **6 Export Formats**: TXT, CSV, HTML, PDF, JSON, Interactive HTML with Charts
- **Auto-generated filenames** with timestamps
- **Publication-ready** formatting and styling
- **One-click sharing** - open HTML reports in any browser

### 🔒 **Privacy & Control**
- **100% local AI processing** (only web scraping uses external API)
- **Your models, your data, your control**
- **No ongoing costs** for AI analysis
- **Secure API key storage**

---

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)
```bash
git clone https://github.com/rmc0315/firecrawl-ollama-system.git
cd firecrawl-ollama-system
python setup.py
```

### Option 2: Windows Users
```cmd
git clone https://github.com/rmc0315/firecrawl-ollama-system.git
cd firecrawl-ollama-system
python setup_windows.py
```

### Option 3: One-Line Install
```bash
curl -sSL https://raw.githubusercontent.com/rmc0315/firecrawl-ollama-system/main/install.sh | bash
```

**That's it!** The setup handles everything automatically:
- ✅ Installs dependencies
- ✅ Detects your Ollama models  
- ✅ Creates launcher scripts
- ✅ Tests connections
- ✅ Guides you through API key setup

---

## 🎬 See It In Action

<table>
<tr>
<td width="50%">

**🔍 Model Detection**
```
🤖 Your Available Models (5 total):
🚀 Fast & Efficient:
  • llama3.2:latest (1925MB) - 3.2B
🧠 Deep Reasoning:  
  • qwen3:latest (4983MB) - 8.2B
💻 Code & Structured Data:
  • qwen2.5-coder:latest (4466MB) - 7.6B
🏆 Comprehensive Analysis:
  • phi4:latest (8633MB) - 14.7B
```

</td>
<td width="50%">

**📊 Smart Analysis**
```
🌐 Website: https://competitor.com
📋 Task: Analyze pricing strategy  
🤖 Model: qwen3 (selected for reasoning)
⏱️ Processing Time: 3.2 seconds

💾 Save Report Options:
1. 📄 Text  2. 📊 CSV  3. 🌐 HTML
4. 📋 PDF  5. 📁 JSON  6. 🎨 Charts
```

</td>
</tr>
</table>

---

## 🎯 Perfect For

<table>
<tr>
<td align="center" width="20%">
<img src="https://img.icons8.com/color/96/000000/research.png" width="64"><br>
<b>Researchers</b><br>
<small>Analyze competitors<br>and market trends</small>
</td>
<td align="center" width="20%">
<img src="https://img.icons8.com/color/96/000000/code.png" width="64"><br>
<b>Developers</b><br>
<small>Extract structured<br>data from websites</small>
</td>
<td align="center" width="20%">
<img src="https://img.icons8.com/color/96/000000/business.png" width="64"><br>
<b>Businesses</b><br>
<small>Monitor competition<br>and industry changes</small>
</td>
<td align="center" width="20%">
<img src="https://img.icons8.com/color/96/000000/student-male.png" width="64"><br>
<b>Students</b><br>
<small>Research projects<br>and data analysis</small>
</td>
<td align="center" width="20%">
<img src="https://img.icons8.com/color/96/000000/privacy.png" width="64"><br>
<b>Privacy-Conscious</b><br>
<small>Local AI processing<br>keeps data private</small>
</td>
</tr>
</table>

---

## 🤖 Model Compatibility

**Works with ANY Ollama model!** Automatically tested and categorized:

| Category | Examples | Best For |
|----------|----------|----------|
| 🚀 **Fast** | llama3.2, phi3, gemma2-2b | Quick analysis, summaries |
| 🧠 **Reasoning** | qwen3, deepseek, claude-3 | Complex analysis, research |
| 💻 **Coding** | qwen2.5-coder, codellama | Data extraction, JSON parsing |
| 🏆 **Comprehensive** | phi4, llama3-70b, mixtral | Detailed reports, comparisons |
| 👁️ **Vision** | llava, bakllava | Image analysis (coming soon) |

**Don't have models?** The setup suggests the best ones for your use case!

---

## 📊 Report Examples

<div align="center">

| Format | Use Case | Preview |
|--------|----------|---------|
| **📄 TXT** | Simple sharing | `Clean, readable text format` |
| **📊 CSV** | Data analysis | `Import into Excel/Sheets` |
| **🌐 HTML** | Professional presentation | [View Sample](examples/sample_report.html) |
| **📋 PDF** | Print/archive | [Download Sample](examples/sample_report.pdf) |
| **📁 JSON** | API integration | `Machine-readable structured data` |
| **🎨 Charts** | Interactive analysis | [Interactive Demo](examples/charts_demo.html) |

</div>

---

## 🛠️ Installation & Requirements

### Prerequisites
- **Python 3.8+** (Python 3.9+ recommended)
- **4GB+ RAM** (for AI models)
- **[Ollama](https://ollama.com)** - Local AI runtime
- **[Firecrawl API](https://firecrawl.dev)** - Web scraping (free tier)

### Supported Platforms
- ✅ **Windows 10/11** (with enhanced batch files)
- ✅ **macOS** (Intel & Apple Silicon)
- ✅ **Linux** (Ubuntu, Debian, CentOS, etc.)

### Dependencies
All automatically installed by setup:
```
firecrawl-py>=0.0.8    # Web scraping
ollama>=0.1.7          # AI model interface  
requests>=2.31.0       # HTTP requests
reportlab>=4.0.4       # PDF generation
Pillow>=10.0.0         # Image processing
```

**📖 Detailed Instructions**: [INSTALLATION.md](docs/INSTALLATION.md)

---

## 📖 Documentation

| Document | Description |
|----------|-------------|
| [📥 **Installation Guide**](docs/INSTALLATION.md) | Complete setup instructions for all platforms |
| [🎯 **Usage Examples**](docs/USAGE.md) | Step-by-step tutorials and real-world examples |
| [🔧 **Troubleshooting**](docs/TROUBLESHOOTING.md) | Common issues and solutions |
| [⚙️ **Configuration**](docs/CONFIGURATION.md) | Advanced settings and customization |
| [🤝 **Contributing**](CONTRIBUTING.md) | How to contribute to the project |
| [📋 **Changelog**](CHANGELOG.md) | Version history and updates |

---

## 🎮 Usage Examples

### Basic Website Analysis
```python  
🌐 Enter website URL: https://techcrunch.com
📋 Analysis task: Summarize today's top tech news
🤖 Select Model: qwen3 (Deep Reasoning)
⚡ Processing... ✅ Complete!
💾 Save as: HTML with Charts
```

### Model Comparison
```python
🌐 URL: https://openai.com  
📋 Task: What are their main products?
🤖 Models: llama3.2, qwen3, phi4
📊 Result: Side-by-side analysis showing different perspectives
```

### Competitive Analysis  
```python
🏢 Competitors: openai.com, anthropic.com, google.ai
🎯 Focus: AI safety approaches
📈 Output: Comprehensive comparison report with insights
```

---

## 🌟 Community & Support

<div align="center">

[![GitHub Issues](https://img.shields.io/github/issues/rmc0315/firecrawl-ollama-system)](../../issues)
[![GitHub Discussions](https://img.shields.io/github/discussions/rmc0315/firecrawl-ollama-system)](../../discussions)  
[![GitHub Stars](https://img.shields.io/github/stars/rmc0315/firecrawl-ollama-system)](../../stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/rmc0315/firecrawl-ollama-system)](../../forks)

</div>

### 💬 Get Help
- **🐛 Bug Reports**: [Create an Issue](../../issues/new?template=bug_report.md)
- **💡 Feature Requests**: [Share Your Ideas](../../issues/new?template=feature_request.md)
- **❓ Questions**: [GitHub Discussions](../../discussions)
- **📖 Documentation**: [Wiki Pages](../../wiki)

### 🤝 Contributing
We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- 🐛 Bug fixes and improvements
- ✨ New features and analysis types  
- 📚 Documentation and examples
- 🧪 Testing and quality assurance

---

## 🎉 What's Coming Next?

### v1.1.0 - Enhanced Features
- 🔄 **Batch Processing** - Analyze multiple URLs simultaneously
- 🌐 **Web UI** - Optional browser-based interface
- 📅 **Scheduled Analysis** - Automated monitoring
- 🔌 **API Mode** - Use as library in other projects

### v1.2.0 - Enterprise Features
- 🐳 **Docker Support** - Containerized deployment
- 👥 **Team Collaboration** - Shared reports and settings
- ☁️ **Cloud Integration** - Save to AWS, GCS, Azure
- 📊 **Advanced Analytics** - Trend analysis and insights

**Want to influence the roadmap?** [Join the discussion!](../../discussions)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**TL;DR**: ✅ Commercial use ✅ Modification ✅ Distribution ✅ Private use

---

## 🙏 Acknowledgments

- **[Ollama](https://ollama.com)** - Amazing local AI runtime that makes this possible
- **[Firecrawl](https://firecrawl.dev)** - Excellent web scraping service with clean APIs  
- **Community Contributors** - Thank you for feedback, bug reports, and improvements!
- **Open Source AI** - Built on the shoulders of giants in the AI community

---

<div align="center">

**⭐ If this project helps you, please give it a star! ⭐**

**Built with ❤️ for the open source and local AI community**

[⬆️ **Back to Top**](#-universal-firecrawl--ollama-integration-system)

</div>