# 📖 Usage Guide

Complete guide to using the Universal Firecrawl + Ollama Integration System with real-world examples and best practices.

## 🚀 Quick Start Tutorial

### First Time Setup
1. **Run the system**: `python universal_firecrawl_ollama.py`
2. **Enter your Firecrawl API key** when prompted (one-time setup)
3. **System auto-detects** your Ollama models and categorizes them
4. **Choose your first analysis** from the main menu

### Your First Analysis
```
🎯 Select option (1-7): 1
🌐 Enter website URL: https://example.com
📋 Analysis task: What is this website about?
🤖 Select Model: 1 (llama3.2 - Fast & Efficient)
✅ Analysis completed!
💾 Save report? Choose format: 3 (HTML)
```

**Result**: Professional analysis saved as `website_analysis_example_com_20241219_143022.html`

---

## 🔍 Analysis Types & Use Cases

### 1. Single Website Analysis

**Perfect for**: Company research, competitor analysis, content understanding

#### **Example 1: Startup Research**
```
🌐 URL: https://stripe.com
📋 Task: Analyze Stripe's business model and key value propositions
🤖 Model: qwen3 (Deep Reasoning)
```

**Sample Output**:
> Stripe operates a comprehensive payments infrastructure platform targeting developers and businesses. Their key value propositions include: 1) Developer-first API design with extensive documentation, 2) Global payment processing with local payment methods, 3) Comprehensive financial tools beyond payments (billing, connect, etc.)...

#### **Example 2: Product Analysis**
```
🌐 URL: https://notion.so
📋 Task: What features does Notion offer and who is their target audience?
🤖 Model: llama3.2 (Fast & Efficient)
```

#### **Example 3: Technical Documentation**
```
🌐 URL: https://docs.python.org/3/
📋 Task: Extract key Python 3 features and improvements
🤖 Model: qwen2.5-coder (Code & Structured Data)
```

### 2. Model Comparison

**Perfect for**: Understanding different AI perspectives, quality assurance, research

#### **Example 1: News Analysis**
```
🌐 URL: https://techcrunch.com/2024/12/19/ai-breakthrough
📋 Task: Summarize the key points of this AI breakthrough
🤖 Models: 1,2,4 (llama3.2, qwen3, phi4)
```

**Why Use Multiple Models**:
- **Fast model (llama3.2)**: Quick overview, main points
- **Reasoning model (qwen3)**: Deeper analysis, implications
- **Comprehensive model (phi4)**: Detailed insights, context

#### **Example 2: Business Strategy Analysis**
```
🌐 URL: https://openai.com/blog/chatgpt-enterprise
📋 Task: Analyze OpenAI's enterprise strategy
🤖 Models: 2,4 (qwen3, phi4)
```

### 3. Structured Data Extraction

**Perfect for**: Lead generation, competitive intelligence, data collection

#### **Example 1: Company Information**
```
🌐 URL: https://company.com/about
🎯 Extract: Company info (name, products, contact)
🤖 Model: qwen2.5-coder (auto-selected)
```

**Sample JSON Output**:
```json
{
  "company_name": "TechCorp Solutions",
  "founded": "2018",
  "products": ["Cloud Platform", "AI Tools", "Analytics"],
  "contact": {
    "email": "contact@techcorp.com",
    "phone": "+1-555-0123"
  },
  "headquarters": "San Francisco, CA"
}
```

#### **Example 2: Product Catalog**
```
🌐 URL: https://shop.example.com/products
🎯 Extract: Product features and pricing
```

#### **Example 3: Team Information**
```
🌐 URL: https://startup.com/team
🎯 Extract: Team member names and roles
```

### 4. Competitive Analysis

**Perfect for**: Market research, positioning, strategic planning

#### **Example 1: SaaS Comparison**
```
🏢 Competitors:
  1. https://slack.com
  2. https://discord.com  
  3. https://teams.microsoft.com
🎯 Focus: Communication features and pricing
🤖 Model: phi4 (Comprehensive Analysis)
```

#### **Example 2: E-commerce Analysis**
```
🏢 Competitors:
  1. https://shopify.com
  2. https://woocommerce.com
  3. https://bigcommerce.com
🎯 Focus: Target market and positioning
```

---

## 🎯 Model Selection Guide

### When to Use Each Model Category

| Model Type | Best For | Example Tasks |
|------------|----------|---------------|
| 🚀 **Fast** | Quick summaries, basic analysis | News summaries, simple Q&A |
| 🧠 **Reasoning** | Complex analysis, strategic insights | Business analysis, research |
| 💻 **Coding** | Data extraction, structured output | JSON extraction, technical docs |
| 🏆 **Comprehensive** | Detailed reports, multi-faceted analysis | Competitive analysis, research papers |

### Model Recommendations by Use Case

#### **Content Marketing Research**
- **Primary**: qwen3 (reasoning) - for strategic insights
- **Secondary**: phi4 (comprehensive) - for detailed analysis

#### **Technical Documentation**
- **Primary**: qwen2.5-coder (coding) - for accurate technical details
- **Secondary**: llama3.2 (fast) - for quick overviews

#### **Competitive Intelligence**
- **Primary**: phi4 (comprehensive) - for thorough analysis
- **Secondary**: qwen3 (reasoning) - for strategic implications

#### **Lead Generation**
- **Primary**: qwen2.5-coder (coding) - for structured data extraction
- **Secondary**: llama3.2 (fast) - for quick contact info

---

## 📊 Report Formats & When to Use Them

### 1. 📄 Text (.txt)
**Best for**: Quick sharing, email, simple documentation
```
Use when: Sharing via email, copying to other documents
Pros: Universal compatibility, small file size
Cons: No formatting, no charts
```

### 2. 📊 CSV (.csv)  
**Best for**: Data analysis, Excel import, further processing
```
Use when: Need to analyze data in spreadsheets
Pros: Excel/Sheets compatible, structured data
Cons: Limited formatting, no narrative
```

### 3. 🌐 HTML (.html)
**Best for**: Professional presentations, web sharing
```
Use when: Presenting to stakeholders, web publishing
Pros: Professional appearance, universal browser support
Cons: Larger file size
```

### 4. 📋 PDF (.pdf)
**Best for**: Formal reports, printing, archiving
```
Use when: Formal documentation, client deliverables
Pros: Print-ready, professional format
Cons: Not easily editable
```

### 5. 📁 JSON (.json)
**Best for**: API integration, programmatic processing
```
Use when: Feeding data to other systems
Pros: Machine-readable, structured
Cons: Not human-friendly for reading
```

### 6. 🎨 HTML with Charts
**Best for**: Executive presentations, comprehensive reports
```
Use when: Need interactive elements, impressive presentations
Pros: Interactive charts, engaging visuals
Cons: Larger file size, requires modern browser
```

---

## 🛠️ Advanced Usage Patterns

### Batch Analysis Workflow

While the system doesn't have built-in batch processing, you can create efficient workflows:

#### **Multi-Site Competitive Analysis**
1. **Start with competitive analysis** (option 4)
2. **Add all competitor URLs** at once
3. **Choose comprehensive model** (phi4)
4. **Save as HTML with charts** for presentation

#### **Market Research Pipeline**
1. **Single analysis** of main competitor (option 1)
2. **Model comparison** on key competitor (option 2)  
3. **Structured extraction** for contact/pricing data (option 3)
4. **Competitive analysis** of top 3-5 players (option 4)

### Research Workflows

#### **Academic Research**
```
Step 1: Single analysis of primary sources
Step 2: Model comparison for different perspectives  
Step 3: Structured extraction of key data points
Step 4: Compile into comprehensive report
```

#### **Business Intelligence**
```
Step 1: Competitive analysis of market leaders
Step 2: Structured extraction of pricing/features
Step 3: Single analysis of emerging players
Step 4: Model comparison for strategic insights
```

---

## 💡 Pro Tips & Best Practices

### 🎯 Writing Effective Analysis Tasks

#### **✅ Good Task Examples**:
- "Analyze the pricing strategy and target market for this SaaS product"
- "Extract the key technical specifications and system requirements"
- "Summarize the main value propositions and competitive advantages"
- "Identify the primary use cases and customer testimonials mentioned"

#### **❌ Avoid These Tasks**:
- "Tell me about this website" (too vague)
- "Is this company good?" (subjective, unclear)
- "What do you think?" (no specific goal)

### 🚀 Optimizing Performance

#### **For Speed**:
- Use **fast models** (llama3.2) for simple tasks
- Keep analysis tasks **focused and specific**
- **Save frequently** to avoid re-running analyses

#### **For Quality**:
- Use **reasoning models** (qwen3) for complex analysis
- Use **comprehensive models** (phi4) for detailed reports
- **Compare multiple models** for important decisions

#### **For Data Extraction**:
- Always use **coding models** (qwen2.5-coder)
- Be **specific about data structure** needed
- **Test with simple sites** first

### 📁 Organization Tips

#### **File Naming**:
The system automatically creates descriptive filenames:
```
website_analysis_competitor_com_20241219_143022.html
model_comparison_openai_com_20241219_144156.pdf
data_extraction_startup_com_20241219_145330.json
```

#### **Report Management**:
- **Use consistent analysis tasks** for comparable results
- **Date-based organization** is automatic
- **Export formats** for different use cases
- **Archive old reports** periodically

---

## 🔧 Configuration & Customization

### API Key Management
```python
# Automatic: System saves on first use
# Manual: Set environment variable
export FIRECRAWL_API_KEY="fc-your-key-here"

# Update: Use Configuration Settings (option 6)
```

### Custom Settings
```python
# Access via Configuration Settings menu (option 6)
1. 🔑 Update Firecrawl API Key
2. 📁 Change Reports Directory  
3. 💾 Set Default Save Format
4. 🔄 Reset Configuration
5. 📄 View Full Configuration
```

### Model Preferences
The system automatically recommends models, but you can always choose:
- **Override recommendations** by selecting different models
- **Experiment with combinations** in model comparison
- **Note which models work best** for your use cases

---

## 🎨 Real-World Use Cases

### 🏢 Business Applications

#### **Market Research**
```
Task: Analyze top 5 competitors in fintech space
Process: 
1. Competitive analysis with phi4 model
2. Structured extraction of pricing data
3. HTML report with charts for presentation
Result: Executive-ready competitive intelligence
```

#### **Content Strategy**
```  
Task: Research successful blog strategies
Process:
1. Single analysis of top performing blogs
2. Model comparison for different perspectives
3. Extract content themes and posting frequency
Result: Data-driven content strategy recommendations
```

#### **Lead Generation**
```
Task: Extract contact information from prospect websites
Process:
1. Structured data extraction with coding model
2. JSON export for CRM import
3. Batch process multiple prospects
Result: Qualified lead database
```

### 🎓 Academic & Research

#### **Literature Survey**
```
Task: Analyze recent AI safety research publications
Process:
1. Single analysis of key papers/organizations
2. Model comparison for different interpretations
3. Structured extraction of methodologies
Result: Comprehensive literature review
```

#### **Competitive Academic Analysis**
```
Task: Compare university AI programs
Process:
1. Competitive analysis of top programs
2. Extract curriculum and faculty data
3. HTML report for decision making
Result: Program comparison matrix
```

### 👨‍💻 Developer Applications

#### **Technology Assessment**
```
Task: Evaluate new JavaScript frameworks
Process:
1. Technical analysis with coding model
2. Extract features, requirements, examples
3. Compare multiple frameworks
Result: Technology decision matrix
```

#### **API Documentation Analysis**
```
Task: Understand third-party API capabilities
Process:
1. Structured extraction of endpoints
2. Model comparison for usage examples
3. JSON export for integration planning
Result: API integration roadmap
```

---

## 🚨 Troubleshooting Common Issues

### Analysis Quality Issues

#### **Low-Quality Output**
- **Try a different model**: Reasoning or comprehensive models
- **Be more specific** in your analysis task
- **Check source website**: Some sites have limited content

#### **Incomplete Analysis**
- **Website might be complex**: Try simpler pages first
- **Content might be behind login**: Use publicly accessible pages
- **Try different analysis approach**: Break into smaller tasks

### Technical Issues

#### **Slow Performance**
- **Use faster models** for simple tasks
- **Check system resources**: Close other applications
- **Try smaller websites** first

#### **Connection Issues**
- **Firecrawl timeout**: Try different websites
- **Ollama not responding**: Restart ollama service
- **API key issues**: Check Configuration Settings

### Report Issues

#### **Export Failures**
- **PDF issues**: Install reportlab (`pip install reportlab`)
- **Chart rendering**: Modern browser required for HTML reports
- **File permissions**: Check write access to reports directory

---

## 📈 Measuring Success

### Quality Metrics
- **Relevance**: Does the analysis address your specific task?
- **Completeness**: Are all key points covered?
- **Accuracy**: Does the analysis match the website content?
- **Actionability**: Can you make decisions based on the insights?

### Efficiency Metrics  
- **Time saved**: vs manual website analysis
- **Model selection**: Right model for the task
- **Report format**: Matches your workflow needs
- **Reusability**: Can you build on previous analyses?

---

## 🔮 Advanced Workflows

### Research Pipeline
```
Week 1: Competitive landscape analysis
Week 2: Deep-dive single analyses
Week 3: Structured data extraction
Week 4: Synthesis and reporting
```

### Business Intelligence Cycle
```
Monthly: Competitive analysis updates
Weekly: New player identification  
Daily: News and trend monitoring
Quarterly: Comprehensive market reports
```

### Content Strategy Process
```
Research phase: Analyze successful content
Planning phase: Extract themes and formats
Creation phase: Use insights for content calendar
Analysis phase: Compare performance against research
```

---

## 🎯 Getting the Most Value

### Best Practices Summary
1. **Start simple**: Use single analysis first
2. **Experiment with models**: Find what works for your use cases
3. **Be specific**: Clear analysis tasks get better results
4. **Save systematically**: Consistent file organization
5. **Compare approaches**: Use model comparison for important decisions
6. **Export appropriately**: Match format to use case
7. **Build workflows**: Combine analysis types for comprehensive research

### Community & Learning
- **Share your reports**: Show others what you've accomplished
- **Learn from examples**: Check out sample reports
- **Contribute back**: Share workflows that work well
- **Ask questions**: Use GitHub Discussions for help

---

**Ready to become a power user?** Start with simple analyses and gradually explore more advanced features. The system grows with your needs! 🚀

For more help, check out:
- 📖 [Installation Guide](INSTALLATION.md)
- 🔧 [Troubleshooting](TROUBLESHOOTING.md)
- 💬 [GitHub Discussions](../../discussions)
- 🐛 [Report Issues](../../issues)