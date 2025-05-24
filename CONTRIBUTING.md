# 🤝 Contributing Guide

Thank you for your interest in contributing to the Universal Firecrawl + Ollama Integration System! This project thrives thanks to contributions from the community.

## 🌟 Ways to Contribute

We welcome all types of contributions, whether you're a developer, writer, designer, or just an enthusiastic user!

### 🐛 **Bug Reports & Issues**
- Found a bug? [Report it here](../../issues/new?template=bug_report.md)
- System not working as expected? Let us know!
- Unclear documentation? That's a bug too!

### ✨ **Feature Requests**
- Have an idea for improvement? [Share it here](../../issues/new?template=feature_request.md)
- Want a new analysis type or export format?
- Need integration with another tool?

### 💻 **Code Contributions**
- Bug fixes and improvements
- New features and analysis types
- Performance optimizations
- Platform-specific enhancements

### 📚 **Documentation**
- Improve existing documentation
- Add new examples and tutorials
- Create video guides or blog posts
- Translate documentation

### 🧪 **Testing & Quality Assurance**
- Test on different platforms
- Try with various Ollama models
- Verify installation instructions
- Performance testing and benchmarking

### 🎨 **Design & UX**
- Improve CLI interface design
- Create better report templates
- Design logos and graphics
- Enhance user experience

---

## 🚀 Getting Started

### Prerequisites for Development

#### **System Requirements**
- **Python 3.8+** (Python 3.9+ recommended)
- **Git** for version control
- **Ollama** with at least one model installed
- **Firecrawl API key** (free tier available)

#### **Development Tools**
```bash
# Recommended tools
pip install black flake8 pytest  # Code formatting and testing
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Fork and Clone

#### **1. Fork the Repository**
- Click the "Fork" button on the [main repository page](../../)
- This creates your own copy of the project

#### **2. Clone Your Fork**
```bash
git clone https://github.com/YOUR-USERNAME/firecrawl-ollama-system.git
cd firecrawl-ollama-system
```

#### **3. Set Up Remote**
```bash
# Add the original repository as "upstream"
git remote add upstream https://github.com/ORIGINAL-OWNER/firecrawl-ollama-system.git

# Verify remotes
git remote -v
# Should show both "origin" (your fork) and "upstream" (original)
```

### Development Setup

#### **1. Create Virtual Environment**
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate.bat
# macOS/Linux:
source venv/bin/activate
```

#### **2. Install Dependencies**
```bash
# Install all dependencies including development tools
pip install -r requirements.txt
pip install black flake8 pytest  # Development tools

# Or install in development mode
pip install -e .
```

#### **3. Set Up Configuration**
```bash
# Copy example configuration
cp config_example.py config.py

# Add your Firecrawl API key
# Edit config.py or set environment variable:
export FIRECRAWL_API_KEY="fc-your-key-here"
```

#### **4. Test Your Setup**
```bash
# Run the system to make sure everything works
python universal_firecrawl_ollama.py

# Run tests (if available)
pytest tests/
```

---

## 🔧 Development Workflow

### Before Making Changes

#### **1. Create a Branch**
```bash
# Update your main branch
git checkout main
git pull upstream main

# Create a new branch for your changes
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-number-description
```

#### **2. Branch Naming Conventions**
```bash
# Features
git checkout -b feature/batch-processing
git checkout -b feature/export-powerpoint

# Bug fixes
git checkout -b bugfix/123-ollama-connection-issue
git checkout -b bugfix/report-generation-error

# Documentation
git checkout -b docs/update-installation-guide
git checkout -b docs/add-usage-examples

# Improvements
git checkout -b improve/performance-optimization
git checkout -b improve/ui-enhancements
```

### Making Changes

#### **1. Code Style**
We follow Python best practices and use automated formatting:

```bash
# Format code with Black
black universal_firecrawl_ollama.py

# Check code style with flake8
flake8 universal_firecrawl_ollama.py

# Fix common issues
black . && flake8 .
```

#### **2. Code Quality Guidelines**
```python
# ✅ Good practices:
def analyze_website(url: str, task: str) -> dict:
    """
    Analyze a website with clear documentation.
    
    Args:
        url: Website URL to analyze
        task: Analysis task description
        
    Returns:
        Dictionary containing analysis results
    """
    # Clear, descriptive variable names
    scraped_content = scrape_website(url)
    analysis_result = process_with_ai(scraped_content, task)
    
    return {
        'url': url,
        'task': task,
        'analysis': analysis_result,
        'timestamp': datetime.now().isoformat()
    }

# ❌ Avoid:
def analyze(u, t):  # Unclear function name and parameters
    c = scrape(u)   # Unclear variable names
    return c        # No type hints or documentation
```

#### **3. Testing Your Changes**
```bash
# Test basic functionality
python universal_firecrawl_ollama.py

# Test specific features you modified
# Try different analysis types, models, export formats

# Test on different platforms if possible
# Windows, macOS, Linux

# Test with different Ollama models
# Small models (llama3.2) and large models (phi4)
```

### Commit Guidelines

#### **1. Commit Message Format**
```bash
# Format: type(scope): description
# 
# Types:
feat:     New feature
fix:      Bug fix
docs:     Documentation changes
style:    Code style changes (formatting, etc)
refactor: Code refactoring
test:     Adding or updating tests
chore:    Maintenance tasks

# Examples:
git commit -m "feat(analysis): add batch processing support"
git commit -m "fix(ollama): resolve connection timeout issues"
git commit -m "docs(usage): add model comparison examples"
git commit -m "style(reports): improve HTML report formatting"
```

#### **2. Good Commit Messages**
```bash
# ✅ Good commits:
git commit -m "feat(export): add PowerPoint export format"
git commit -m "fix(config): handle missing API key gracefully"
git commit -m "docs(install): update Windows installation steps"
git commit -m "improve(performance): optimize large content processing"

# ❌ Poor commits:
git commit -m "fixed stuff"
git commit -m "changes"
git commit -m "update"
```

---

## 📋 Contribution Types

### 🐛 Bug Fixes

#### **Before You Start**
1. **Check existing issues** - Make sure the bug isn't already reported
2. **Reproduce the issue** - Confirm you can recreate the problem
3. **Document the bug** - Note system info, steps to reproduce, expected vs actual behavior

#### **Bug Fix Process**
```bash
# 1. Create branch
git checkout -b bugfix/123-ollama-connection-timeout

# 2. Fix the issue
# Edit the relevant files

# 3. Test thoroughly
python universal_firecrawl_ollama.py
# Try to reproduce the original bug - it should be fixed
# Test other functionality to ensure no regressions

# 4. Commit and push
git add .
git commit -m "fix(ollama): resolve connection timeout by increasing retry limit"
git push origin bugfix/123-ollama-connection-timeout
```

### ✨ New Features

#### **Feature Development Process**
1. **Discuss first** - Open an issue or discussion to talk about your idea
2. **Plan the implementation** - Think about how it fits with existing code
3. **Start small** - Build a minimal working version first
4. **Get feedback early** - Share work-in-progress for input

#### **Example: Adding New Export Format**
```python
# 1. Add the new format option
def save_report_options(self):
    print("6. 📄 Word document (.docx)")  # Add new option
    
# 2. Implement the export function
def save_as_docx(self, data, filename):
    """Save report as Word document"""
    # Implementation here
    
# 3. Integrate with existing code
elif save_format == "docx":
    self.save_as_docx(data, f"{filename}.docx")
    
# 4. Update documentation
# Add to README.md, USAGE.md, etc.
```

### 📚 Documentation Contributions

#### **Types of Documentation Needed**
- **Installation guides** for specific platforms
- **Usage examples** for different industries/use cases
- **Video tutorials** and walkthroughs
- **Blog posts** about interesting analyses
- **API documentation** for advanced usage

#### **Documentation Standards**
```markdown
# ✅ Good documentation:
## Clear Section Headers

Step-by-step instructions:
1. **First step** - Clear action item
2. **Second step** - With expected results
3. **Third step** - Including troubleshooting

```bash
# Code examples with comments
python setup.py  # This installs dependencies
```

**Expected output:**
```
✅ Dependencies installed successfully
```

# ❌ Poor documentation:
do the thing
run stuff
it should work
```

### 🧪 Testing Contributions

#### **Areas That Need Testing**
- **Platform testing** - Windows, macOS, Linux
- **Model compatibility** - Different Ollama models
- **Performance testing** - Large websites, multiple analyses
- **Edge cases** - Network issues, malformed content, etc.

#### **How to Contribute Testing**
1. **Try different scenarios** that others might not have tested
2. **Document what you tested** and the results
3. **Report any issues** you find
4. **Share successful configurations** that work well

---

## 🎯 Priority Areas for Contributions

### 🔥 High Priority (Most Needed)

#### **1. Platform Compatibility**
- **Windows** - Better batch file handling, encoding issues
- **macOS** - ARM/Intel compatibility, permission issues  
- **Linux** - Different distributions, dependency management

#### **2. Model Support**
- **New model compatibility** - Test with latest Ollama models
- **Model optimization** - Performance tuning for different models
- **Custom model categories** - Better auto-categorization

#### **3. Export Formats**
- **Microsoft Office** - Word, PowerPoint, Excel exports
- **Enhanced HTML** - Better charts, interactive elements
- **Email integration** - Send reports directly via email

### 🚀 Medium Priority (Would Be Great)

#### **4. User Experience**
- **Web interface** - Optional browser-based UI
- **Configuration wizard** - Guided first-time setup
- **Batch processing** - Analyze multiple URLs at once

#### **5. Advanced Features**
- **Scheduled analysis** - Cron-like functionality
- **API integration** - REST API for programmatic access  
- **Plugin system** - Extensible analysis types

### 💡 Nice to Have (Future Ideas)

#### **6. Enterprise Features**
- **Team collaboration** - Shared reports and settings
- **User management** - Multiple user accounts
- **Cloud storage** - Integration with AWS, GCS, etc.

---

## 📝 Pull Request Process

### Before Submitting

#### **1. Pre-Submission Checklist**
- [ ] **Code runs without errors** on your system
- [ ] **Follow code style guidelines** (run `black .` and `flake8 .`)
- [ ] **Test your changes** thoroughly
- [ ] **Update documentation** if needed
- [ ] **Write clear commit messages**
- [ ] **Branch is up to date** with main

#### **2. Update Your Branch**
```bash
# Get latest changes from main repository
git fetch upstream
git checkout main
git merge upstream/main

# Update your feature branch
git checkout your-feature-branch
git merge main
# or
git rebase main
```

### Submitting Your Pull Request

#### **1. Push Your Changes**
```bash
git push origin your-feature-branch
```

#### **2. Create Pull Request**
1. **Go to your fork** on GitHub
2. **Click "New Pull Request"**
3. **Choose branches**: `base: main` ← `compare: your-feature-branch`
4. **Fill out the template** (see below)

#### **3. Pull Request Template**
```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] 🐛 Bug fix (non-breaking change that fixes an issue)
- [ ] ✨ New feature (non-breaking change that adds functionality)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📚 Documentation update
- [ ] 🎨 Style/formatting changes
- [ ] ♻️ Code refactoring

## Testing
- [ ] Tested on Windows/macOS/Linux
- [ ] Tested with different Ollama models
- [ ] Tested different analysis types
- [ ] No regressions in existing functionality

## Screenshots (if applicable)
Add screenshots to help explain your changes.

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] Any dependent changes have been merged and published
```

### Review Process

#### **What to Expect**
1. **Automated checks** - Code style, basic functionality
2. **Maintainer review** - Code quality, design decisions
3. **Community feedback** - Other contributors may comment
4. **Revision requests** - You may need to make changes

#### **Responding to Feedback**
```bash
# Make requested changes
# Edit your files

# Commit changes
git add .
git commit -m "address review feedback: improve error handling"

# Push updates
git push origin your-feature-branch
# This automatically updates your PR
```

---

## 🏆 Recognition and Rewards

### Contributor Recognition

#### **Contributors Wall**
- All contributors are listed in our [CONTRIBUTORS.md](CONTRIBUTORS.md) file
- Significant contributions are highlighted in release notes
- Regular contributors may be invited to join the maintainer team

#### **Contribution Types Recognized**
- **Code contributions** - Features, bug fixes, improvements
- **Documentation** - Guides, examples, translations  
- **Testing** - Bug reports, compatibility testing
- **Community support** - Helping other users, answering questions
- **Design** - UI improvements, graphics, templates

### Becoming a Maintainer

#### **Path to Maintainership**
1. **Regular contributions** - Consistent, quality contributions over time
2. **Community involvement** - Help other users, participate in discussions
3. **Technical expertise** - Deep understanding of the codebase
4. **Reliability** - Dependable, responsive, professional communication

#### **Maintainer Responsibilities**
- **Review pull requests** from other contributors
- **Triage issues** and help users with problems
- **Release management** - Testing, versioning, release notes
- **Project direction** - Help guide the project's future

---

## 🌍 Community Guidelines

### Code of Conduct

#### **Our Pledge**
We are committed to making participation in this project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

#### **Our Standards**
**✅ Positive behavior includes:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**❌ Unacceptable behavior includes:**
- The use of sexualized language or imagery
- Trolling, insulting/derogatory comments, and personal attacks
- Public or private harassment
- Publishing others' private information without explicit permission
- Other conduct which could reasonably be considered inappropriate

### Communication Channels

#### **GitHub Discussions** 💬
- **General chat** - Casual conversation about the project
- **Q&A** - Ask questions, get help from the community
- **Ideas** - Share feature ideas and suggestions
- **Show and tell** - Share your analyses and use cases

#### **GitHub Issues** 🐛
- **Bug reports** - Found a problem? Report it here
- **Feature requests** - Ideas for new functionality
- **Questions** - Technical questions about usage

#### **Best Practices for Communication**
- **Be specific** - Provide details, examples, screenshots
- **Be patient** - Maintainers and community members are volunteers
- **Be helpful** - Help others when you can
- **Search first** - Check if your question has been asked before

---

## 🛠️ Development Environment Setup

### Recommended IDE Setup

#### **Visual Studio Code**
```json
// .vscode/settings.json
{
    "python.defaultInterpreter": "./venv/bin/python",
    "python.formatting.provider": "black",
    "python.linting.flake8Enabled": true,
    "python.linting.enabled": true,
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true
    }
}
```

#### **Useful Extensions**
- **Python** - Python language support
- **Black Formatter** - Automatic code formatting
- **GitLens** - Enhanced Git integration
- **Python Docstring Generator** - Generate docstrings

### Development Tools

#### **Code Quality Tools**
```bash
# Install development dependencies
pip install black flake8 isort pytest mypy

# Format code
black .

# Check style
flake8 .

# Sort imports
isort .

# Type checking (optional)
mypy universal_firecrawl_ollama.py
```

#### **Git Hooks (Optional)**
```bash
# Set up pre-commit hooks to automatically format code
pip install pre-commit

# Create .pre-commit-config.yaml
cat > .pre-commit-config.yaml << EOF
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
EOF

# Install hooks
pre-commit install
```

---

## 🎓 Learning Resources

### For New Contributors

#### **Git and GitHub**
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)

#### **Python Development**
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/) - Excellent Python tutorials
- [Python Code Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/)

#### **Project-Specific Knowledge**
- [Ollama Documentation](https://ollama.com/docs)
- [Firecrawl API Documentation](https://docs.firecrawl.dev/)
- [Chart.js Documentation](https://www.chartjs.org/docs/) (for HTML reports)

### For Advanced Contributors

#### **AI and Language Models**
- [Hugging Face Course](https://huggingface.co/course/chapter1/1)
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction.html)
- [Ollama Model Library](https://ollama.com/library)

#### **Web Scraping**
- [Requests Documentation](https://docs.python-requests.org/)
- [BeautifulSoup Tutorial](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Web Scraping Best Practices](https://blog.apify.com/web-scraping-best-practices/)

---

## 📞 Getting Help

### Stuck? Here's How to Get Help

#### **1. Check Documentation First**
- [Installation Guide](INSTALLATION.md)
- [Usage Guide](USAGE.md)  
- [Troubleshooting Guide](TROUBLESHOOTING.md)
- [Configuration Guide](CONFIGURATION.md)

#### **2. Search Existing Issues**
- [Open Issues](../../issues) - Current problems being worked on
- [Closed Issues](../../issues?q=is%3Aissue+is%3Aclosed) - Previously solved problems

#### **3. Ask the Community**
- [GitHub Discussions](../../discussions) - Best place for questions
- Be specific about your problem, include error messages and system info

#### **4. Report Bugs**
- [Create New Issue](../../issues/new) - If you found a genuine bug
- Use the bug report template
- Include steps to reproduce the problem

### Contact Information

#### **Project Maintainers**
- Check the [CONTRIBUTORS.md](CONTRIBUTORS.md) file for current maintainers
- Maintainers are volunteers, please be patient with response times

#### **Response Time Expectations**
- **Bug reports**: Usually within 1-3 days
- **Feature requests**: Within a week for initial response
- **Pull requests**: 1-7 days depending on complexity
- **Questions**: Community usually responds within 24-48 hours

---

## 🎉 Thank You!

### Your Contributions Matter

Every contribution, no matter how small, helps make this project better for everyone. Whether you:
- 🐛 **Fix a typo** in documentation
- ✨ **Add a major feature**
- 🧪 **Test on a new platform**
- 💬 **Help another user** in discussions

**You're making a difference!**

### Recognition

Contributors are recognized in:
- **Release notes** for their contributions
- **CONTRIBUTORS.md** file with their GitHub profile
- **Special thanks** in project documentation

### Building Something Great Together

This project started as a solution to make local AI more accessible and powerful. With your help, we can:
- **Support more platforms and models**
- **Add advanced features** for power users
- **Improve documentation** for beginners
- **Build a welcoming community** where everyone can contribute

**Thank you for being part of this journey!** 🚀

---

## 📚 Quick Links

- 🏠 [Project Home](../../)
- 📖 [Documentation](docs/)
- 🐛 [Report Bug](../../issues/new?template=bug_report.md)
- ✨ [Feature Request](../../issues/new?template=feature_request.md)
- 💬 [Discussions](../../discussions)
- 🤝 [Contributors](CONTRIBUTORS.md)

**Happy Contributing!** 🎯