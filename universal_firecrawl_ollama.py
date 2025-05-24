#!/usr/bin/env python3
"""
Universal Firecrawl + Ollama Integration System
Automatically detects and works with any user's Ollama setup
"""

from firecrawl import FirecrawlApp
from ollama import Client
import json
import time
import os
from datetime import datetime
import csv
import base64
import sys

class OllamaModelManager:
    """Dynamically manage available Ollama models"""
    
    def __init__(self, ollama_client):
        self.client = ollama_client
        self.available_models = []
        self.model_info = {}
        self.refresh_models()
    
    def refresh_models(self):
        """Get fresh list of available models"""
        try:
            response = self.client.list()
            self.available_models = []
            self.model_info = {}
            
            if hasattr(response, 'models') and response.models:
                for model in response.models:
                    if hasattr(model, 'model'):
                        model_name = model.model
                        self.available_models.append(model_name)
                        
                        # Extract model info
                        info = {
                            'name': model_name,
                            'size': getattr(model, 'size', 0),
                            'modified': getattr(model, 'modified_at', None),
                            'family': None,
                            'parameters': None
                        }
                        
                        # Try to get additional details
                        if hasattr(model, 'details'):
                            details = model.details
                            info['family'] = getattr(details, 'family', None)
                            info['parameters'] = getattr(details, 'parameter_size', None)
                        
                        self.model_info[model_name] = info
            
            print(f"🤖 Detected {len(self.available_models)} Ollama models")
            return True
            
        except Exception as e:
            print(f"❌ Error getting models: {e}")
            return False
    
    def test_model(self, model_name):
        """Test if a specific model works"""
        try:
            response = self.client.chat(
                model=model_name,
                messages=[{"role": "user", "content": "Hi"}],
                options={"num_predict": 3}
            )
            return True
        except Exception:
            return False
    
    def get_working_models(self):
        """Get list of models that actually work"""
        working_models = []
        
        print("🔧 Testing models for compatibility...")
        for model in self.available_models:
            print(f"  Testing {model}...", end=" ")
            if self.test_model(model):
                working_models.append(model)
                print("✅")
            else:
                print("❌")
        
        return working_models
    
    def categorize_models(self, working_models):
        """Categorize models by their likely use case"""
        categories = {
            'fast': [],
            'reasoning': [],
            'coding': [],
            'comprehensive': [],
            'embedding': [],
            'vision': [],
            'general': []
        }
        
        for model in working_models:
            model_lower = model.lower()
            info = self.model_info.get(model, {})
            
            # Categorize based on name patterns
            if any(x in model_lower for x in ['embed', 'embedding']):
                categories['embedding'].append(model)
            elif any(x in model_lower for x in ['vision', 'llava', 'visual', 'vl']):
                categories['vision'].append(model)
            elif any(x in model_lower for x in ['code', 'coder', 'programming']):
                categories['coding'].append(model)
            elif any(x in model_lower for x in ['qwen', 'deepseek', 'reasoning']):
                categories['reasoning'].append(model)
            elif any(x in model_lower for x in ['phi4', 'phi-4', 'claude', 'gpt-4']):
                categories['comprehensive'].append(model)
            elif any(x in model_lower for x in ['3.2', '1b', '3b', 'small']):
                categories['fast'].append(model)
            else:
                categories['general'].append(model)
        
        return categories

class FirecrawlOllamaSystem:
    """Main system class"""
    
    def __init__(self):
        self.app = None
        self.ollama_client = None
        self.model_manager = None
        self.working_models = []
        self.model_categories = {}
        
        # Create reports directory
        self.reports_dir = "firecrawl_reports"
        if not os.path.exists(self.reports_dir):
            os.makedirs(self.reports_dir)
    
    def setup_firecrawl(self):
        """Setup Firecrawl with user's API key - auto-save/load from config"""
        print("🔥 Setting up Firecrawl...")
        
        # Check multiple sources for API key
        api_key = None
        
        # 1. Check environment variable first
        api_key = os.getenv('FIRECRAWL_API_KEY')
        if api_key:
            print("✅ Using API key from environment variable")
        
        # 2. Check config.py file
        if not api_key:
            try:
                if os.path.exists('config.py'):
                    import importlib.util
                    spec = importlib.util.spec_from_file_location("config", "config.py")
                    config = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(config)
                    
                    if hasattr(config, 'FIRECRAWL_API_KEY') and config.FIRECRAWL_API_KEY != 'your-api-key-here':
                        api_key = config.FIRECRAWL_API_KEY
                        print("✅ Using API key from config.py")
            except Exception as e:
                print(f"⚠️ Could not load config.py: {e}")
        
        # 3. Prompt user if no key found
        if not api_key:
            print("\n🔑 Firecrawl API Key Setup:")
            print("You can get a free API key at: https://firecrawl.dev")
            print("This will be saved so you only need to enter it once.")
            
            api_key = input("\nEnter your Firecrawl API key: ").strip()
            
            if not api_key:
                print("❌ API key required to continue")
                return False
            
            # Save the API key to config.py
            self.save_api_key_to_config(api_key)
        
        # Test the API key
        try:
            self.app = FirecrawlApp(api_key=api_key)
            
            # Test the connection with multiple URLs
            test_urls = ["https://example.com", "https://httpbin.org/html"]
            
            for test_url in test_urls:
                try:
                    result = self.app.scrape_url(test_url, formats=['markdown'])
                    print("✅ Firecrawl connected successfully")
                    return True
                except:
                    continue
            
            print("❌ Firecrawl connection failed - check your API key")
            # If connection fails, prompt for new key
            return self.retry_api_key_setup()
            
        except Exception as e:
            print(f"❌ Firecrawl setup failed: {e}")
            return self.retry_api_key_setup()
    
    def save_api_key_to_config(self, api_key):
        """Save API key to config.py file"""
        try:
            config_content = f'''# Universal Firecrawl + Ollama Configuration
import os

# Firecrawl Configuration
FIRECRAWL_API_KEY = "{api_key}"

# Ollama Configuration  
OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'http://localhost:11434')

# Report Settings
REPORTS_DIR = 'firecrawl_reports'
DEFAULT_SAVE_FORMAT = 'html'  # txt, csv, html, pdf, json, html_charts

# Model Preferences (optional - system will auto-detect)
PREFERRED_MODELS = {{
    'fast': 'llama3.2',
    'reasoning': 'qwen3', 
    'coding': 'qwen2.5-coder',
    'comprehensive': 'phi4'
}}
'''
            
            with open('config.py', 'w', encoding='utf-8') as f:
                f.write(config_content)
            
            print("✅ API key saved to config.py")
            
        except Exception as e:
            print(f"⚠️ Could not save config file: {e}")
    
    def retry_api_key_setup(self):
        """Allow user to retry with a different API key"""
        print("\n🔄 API key may be invalid or connection failed.")
        retry = input("Try with a different API key? (y/n): ").lower().startswith('y')
        
        if retry:
            print("\n🔑 Enter new Firecrawl API key:")
            new_key = input("API key: ").strip()
            
            if new_key:
                self.save_api_key_to_config(new_key)
                # Recursively try setup again
                return self.setup_firecrawl()
        
        return False
    
    def setup_ollama(self):
        """Setup Ollama connection"""
        print("🤖 Setting up Ollama...")
        
        # Try different common Ollama endpoints
        endpoints = [
            "http://localhost:11434",
            "http://127.0.0.1:11434", 
            "http://0.0.0.0:11434"
        ]
        
        ollama_host = os.getenv('OLLAMA_HOST', endpoints[0])
        
        for endpoint in [ollama_host] + endpoints:
            try:
                print(f"  Trying {endpoint}...")
                self.ollama_client = Client(host=endpoint)
                
                # Test connection
                models_response = self.ollama_client.list()
                print(f"✅ Connected to Ollama at {endpoint}")
                
                # Setup model manager
                self.model_manager = OllamaModelManager(self.ollama_client)
                self.working_models = self.model_manager.get_working_models()
                
                if not self.working_models:
                    print("❌ No working models found")
                    print("💡 Try: ollama pull llama3.2")
                    return False
                
                self.model_categories = self.model_manager.categorize_models(self.working_models)
                return True
                
            except Exception as e:
                print(f"  ❌ Failed: {str(e)[:50]}...")
                continue
        
        print("❌ Could not connect to Ollama")
        print("💡 Make sure Ollama is running: ollama serve")
        return False
    
    def display_available_models(self):
        """Show user their available models with categories"""
        print(f"\n🤖 Your Available Models ({len(self.working_models)} total):")
        print("=" * 60)
        
        category_icons = {
            'fast': '🚀',
            'reasoning': '🧠', 
            'coding': '💻',
            'comprehensive': '🏆',
            'embedding': '🔍',
            'vision': '👁️',
            'general': '⚡'
        }
        
        category_descriptions = {
            'fast': 'Fast & Efficient',
            'reasoning': 'Deep Reasoning',
            'coding': 'Code & Structured Data',
            'comprehensive': 'Comprehensive Analysis',
            'embedding': 'Text Embeddings',
            'vision': 'Vision & Multimodal',
            'general': 'General Purpose'
        }
        
        for category, models in self.model_categories.items():
            if models:
                icon = category_icons.get(category, '🤖')
                desc = category_descriptions.get(category, category.title())
                print(f"\n{icon} {desc}:")
                
                for model in models:
                    info = self.model_manager.model_info.get(model, {})
                    size_mb = info.get('size', 0) / (1024 * 1024) if info.get('size') else 0
                    size_str = f" ({size_mb:.1f}MB)" if size_mb > 0 else ""
                    params = info.get('parameters', '')
                    param_str = f" - {params}" if params else ""
                    
                    print(f"  • {model}{size_str}{param_str}")
    
    def select_model_dynamically(self, preferred_category=None):
        """Let user select from their available models"""
        
        if preferred_category and preferred_category in self.model_categories:
            relevant_models = self.model_categories[preferred_category]
            if not relevant_models:
                relevant_models = self.working_models
        else:
            relevant_models = self.working_models
        
        if len(relevant_models) == 1:
            print(f"🤖 Using your only available model: {relevant_models[0]}")
            return relevant_models[0]
        
        print(f"\n🤖 Select Model:")
        for i, model in enumerate(relevant_models, 1):
            info = self.model_manager.model_info.get(model, {})
            size_mb = info.get('size', 0) / (1024 * 1024) if info.get('size') else 0
            size_str = f" ({size_mb:.1f}MB)" if size_mb > 0 else ""
            
            # Add category hint
            model_category = None
            for cat, models in self.model_categories.items():
                if model in models:
                    model_category = cat
                    break
            
            category_hint = f" - {model_category}" if model_category else ""
            print(f"{i}. {model}{size_str}{category_hint}")
        
        while True:
            try:
                choice = int(input(f"\nSelect model (1-{len(relevant_models)}): "))
                if 1 <= choice <= len(relevant_models):
                    selected = relevant_models[choice - 1]
                    print(f"✅ Selected: {selected}")
                    return selected
                else:
                    print(f"Please enter a number between 1 and {len(relevant_models)}")
            except (ValueError, KeyboardInterrupt):
                print("Invalid input or cancelled")
                return None
    
    def get_recommended_models(self):
        """Get recommended models for different tasks"""
        recommendations = {}
        
        # Fast analysis
        if self.model_categories['fast']:
            recommendations['fast'] = self.model_categories['fast'][0]
        elif self.working_models:
            recommendations['fast'] = self.working_models[0]
        
        # Reasoning
        if self.model_categories['reasoning']:
            recommendations['reasoning'] = self.model_categories['reasoning'][0]
        elif self.model_categories['comprehensive']:
            recommendations['reasoning'] = self.model_categories['comprehensive'][0]
        else:
            recommendations['reasoning'] = self.working_models[0] if self.working_models else None
        
        # Coding
        if self.model_categories['coding']:
            recommendations['coding'] = self.model_categories['coding'][0]
        else:
            recommendations['coding'] = recommendations.get('reasoning', self.working_models[0] if self.working_models else None)
        
        # Comprehensive
        if self.model_categories['comprehensive']:
            recommendations['comprehensive'] = self.model_categories['comprehensive'][0]
        else:
            recommendations['comprehensive'] = recommendations.get('reasoning', self.working_models[0] if self.working_models else None)
        
        return recommendations

    def get_user_input(self, prompt, input_type="text"):
        """Get user input with validation"""
        while True:
            try:
                if input_type == "int":
                    return int(input(prompt))
                elif input_type == "url":
                    url = input(prompt).strip()
                    if not url.startswith(('http://', 'https://')):
                        url = 'https://' + url
                    return url
                elif input_type == "list":
                    items = input(prompt).strip().split(',')
                    return [item.strip() for item in items if item.strip()]
                else:
                    return input(prompt).strip()
            except ValueError as e:
                print(f"Invalid input. Please try again. ({e})")
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                return None

    def single_website_analysis(self):
        """Analyze a single website - now fully dynamic"""
        print("\n" + "="*60)
        print("🔍 SINGLE WEBSITE ANALYSIS")
        print("="*60)
        
        # Get URL from user
        url = self.get_user_input("🌐 Enter website URL: ", "url")
        if not url:
            return
        
        # Get analysis task
        print("\n📝 What would you like to analyze? Examples:")
        print("  • What is this company's main focus?")
        print("  • Summarize the key features of their product")
        print("  • What are their pricing options?")
        print("  • Who are their target customers?")
        
        task = self.get_user_input("\n📋 Analysis task: ")
        if not task:
            return
        
        # Select model dynamically
        model = self.select_model_dynamically('general')
        if not model:
            return
        
        # Perform analysis
        try:
            print(f"\n🔄 Scraping {url}...")
            scraped_data = self.app.scrape_url(url, formats=['markdown'])
            content = scraped_data.markdown
            
            if not content or len(content.strip()) < 50:
                print("⚠️ Warning: Very little content found")
                retry = input("Try a different URL? (y/n): ").lower().startswith('y')
                if retry:
                    return self.single_website_analysis()
                return
            
            # Limit content length
            original_length = len(content)
            if len(content) > 4000:
                content = content[:4000] + "\n\n[Content truncated for analysis...]"
            
            print(f"✅ Scraped {len(content)} characters")
            print(f"🤖 Processing with {model}...")
            
            start_time = time.time()
            response = self.ollama_client.chat(
                model=model,
                messages=[
                    {
                        "role": "system", 
                        "content": "You are an expert analyst. Provide clear, structured insights based on website content."
                    },
                    {
                        "role": "user", 
                        "content": f"Task: {task}\n\nWebsite Content:\n{content}"
                    }
                ],
                options={"temperature": 0.3}
            )
            end_time = time.time()
            
            # Prepare results
            results = {
                "url": url,
                "task": task,
                "model": model,
                "content_length": original_length,
                "processing_time": f"{end_time - start_time:.1f} seconds",
                "analysis": response['message']['content'],
                "timestamp": datetime.now().isoformat(),
                "system_info": {
                    "total_models_available": len(self.working_models),
                    "model_categories": list(self.model_categories.keys())
                }
            }
            
            # Display results
            print("\n" + "="*60)
            print("📊 ANALYSIS RESULTS")  
            print("="*60)
            print(f"🌐 Website: {url}")
            print(f"📋 Task: {task}")
            print(f"🤖 Model: {model}")
            print(f"⏱️ Processing Time: {results['processing_time']}")
            print("-"*60)
            print(response['message']['content'])
            print("="*60)
            
            # Save report (using the save functions from previous version)
            self.save_report(results, "website_analysis", url)
            
        except Exception as e:
            self.handle_error(e, "single_website_analysis")

    def model_comparison(self):
        """Compare different models - now fully dynamic"""
        print("\n" + "="*60)
        print("🏆 MODEL COMPARISON")
        print("="*60)
        
        if len(self.working_models) < 2:
            print(f"❌ Need at least 2 models for comparison. You have {len(self.working_models)}.")
            print("💡 Install more models with: ollama pull <model-name>")
            return
        
        # Get URL
        url = self.get_user_input("🌐 Enter website URL to analyze: ", "url")
        if not url:
            return
        
        # Get task
        task = self.get_user_input("📋 What should all models analyze? ")
        if not task:
            return
        
        # Let user select models to compare
        print(f"\n🤖 Select models to compare from your {len(self.working_models)} available models:")
        print("Enter numbers separated by commas (e.g., 1,2,4):")
        
        for i, model in enumerate(self.working_models, 1):
            info = self.model_manager.model_info.get(model, {})
            size_mb = info.get('size', 0) / (1024 * 1024) if info.get('size') else 0
            size_str = f" ({size_mb:.1f}MB)" if size_mb > 0 else ""
            print(f"{i}. {model}{size_str}")
        
        model_choices = self.get_user_input("\nModels to compare: ", "list")
        if not model_choices:
            return
        
        # Convert choices to model names
        selected_models = []
        for choice in model_choices:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(self.working_models):
                    selected_models.append(self.working_models[idx])
            except ValueError:
                continue
        
        if len(selected_models) < 2:
            print("❌ Need at least 2 valid models for comparison.")
            return
        
        print(f"✅ Comparing {len(selected_models)} models: {', '.join(selected_models)}")
        
        # Perform comparison
        try:
            print(f"\n🔄 Scraping {url}...")
            scraped_data = self.app.scrape_url(url, formats=['markdown'])
            content = scraped_data.markdown[:3500]  # Limit for comparison
            print(f"✅ Scraped {len(content)} characters")
            
            # Analyze with each model
            results = {
                "url": url,
                "task": task,
                "models_compared": selected_models,
                "timestamp": datetime.now().isoformat(),
                "system_info": {
                    "total_models_available": len(self.working_models),
                    "comparison_count": len(selected_models)
                }
            }
            
            processing_times = {}
            
            for model in selected_models:
                print(f"\n🤖 Processing with {model}...")
                
                start_time = time.time()
                response = self.ollama_client.chat(
                    model=model,
                    messages=[
                        {"role": "system", "content": "You are an expert analyst. Be concise but thorough."},
                        {"role": "user", "content": f"Task: {task}\n\nContent:\n{content}"}
                    ],
                    options={"temperature": 0.2}
                )
                end_time = time.time()
                
                results[f"{model}_analysis"] = response['message']['content']
                processing_times[model] = f"{end_time - start_time:.1f}s"
                print(f"✅ {model} completed ({processing_times[model]})")
            
            results["processing_times"] = processing_times
            
            # Display results
            print("\n" + "="*80)
            print("🏆 MODEL COMPARISON RESULTS")
            print("="*80)
            print(f"🌐 Website: {url}")
            print(f"📋 Task: {task}")
            print("="*80)
            
            for model in selected_models:
                analysis = results[f"{model}_analysis"]
                print(f"\n🤖 {model.upper()} ({processing_times[model]}):")
                print("-" * 50)
                print(analysis)
                print("-" * 50)
            
            # Save report
            self.save_report(results, "model_comparison", url)
            
        except Exception as e:
            self.handle_error(e, "model_comparison")

    def structured_extraction(self):
        """Extract structured data - dynamically selects best coding model"""
        print("\n" + "="*60)
        print("🏗️ STRUCTURED DATA EXTRACTION")
        print("="*60)
        
        # Get URL
        url = self.get_user_input("🌐 Enter website URL: ", "url")
        if not url:
            return
        
        # Get extraction schema
        print("\n📋 What data would you like to extract? Examples:")
        print("  • Company info (name, products, contact)")
        print("  • Product features and pricing")
        print("  • Team member names and roles")
        print("  • Article titles and summaries")
        
        data_type = self.get_user_input("\n🎯 What to extract: ")
        if not data_type:
            return
        
        # Select best model for structured data
        recommendations = self.get_recommended_models()
        coding_model = recommendations.get('coding', self.working_models[0])
        
        print(f"🤖 Using {coding_model} for structured extraction")
        
        # Rest of the structured extraction logic...
        # (Similar to previous version but with dynamic model selection)
        
        try:
            # Create schema
            print(f"\n🏗️ Creating extraction schema for: {data_type}")
            
            schema_prompt = f"""
            Create a JSON schema to extract {data_type} from website content.
            Make it practical and useful. Return only the schema description, not actual JSON.
            """
            
            schema_response = self.ollama_client.chat(
                model=coding_model,
                messages=[
                    {"role": "system", "content": "You are a data extraction expert. Create clear, practical JSON schemas."},
                    {"role": "user", "content": schema_prompt}
                ],
                options={"temperature": 0.1}
            )
            
            schema_description = schema_response['message']['content']
            print(f"✅ Schema created with {coding_model}")
            
            # Scrape and extract
            print(f"\n🔄 Scraping {url}...")
            scraped_data = self.app.scrape_url(url, formats=['markdown'])  
            content = scraped_data.markdown[:4000]
            print(f"✅ Scraped {len(content)} characters")
            
            print("🤖 Extracting structured data...")
            
            extraction_prompt = f"""
            Extract {data_type} from the website content below.
            Use this schema as a guide: {schema_description}
            
            Return valid JSON only, no extra text.
            
            Website Content:
            {content}
            """
            
            response = self.ollama_client.chat(
                model=coding_model,
                messages=[
                    {"role": "system", "content": "You are a data extraction expert. Always return valid JSON."},
                    {"role": "user", "content": extraction_prompt}
                ],
                options={"temperature": 0.1}
            )
            
            # Prepare results
            results = {
                "url": url,
                "data_type": data_type,
                "schema": schema_description,
                "extracted_data": response['message']['content'],
                "timestamp": datetime.now().isoformat(),
                "model": coding_model,
                "system_info": {
                    "recommended_model_used": True,
                    "model_category": "coding"
                }
            }
            
            print("\n" + "="*60)
            print("🏗️ EXTRACTED DATA")
            print("="*60)
            print(f"🌐 Website: {url}")
            print(f"🎯 Data Type: {data_type}")
            print(f"🤖 Model: {coding_model}")
            print("-"*60)
            print(response['message']['content'])
            print("="*60)
            
            # Save report
            self.save_report(results, "data_extraction", url)
            
        except Exception as e:
            self.handle_error(e, "structured_extraction")

    def handle_error(self, error, context):
        """Enhanced error handling"""
        error_msg = str(error)
        print(f"❌ Error in {context}: {error_msg}")
        
        if "timeout" in error_msg.lower():
            print("💡 Timeout - try a simpler/faster website")
        elif "api key" in error_msg.lower():
            print("💡 Check your Firecrawl API key")
        elif "model" in error_msg.lower():
            print("💡 Model issue - try refreshing models")
            self.model_manager.refresh_models()
        
        retry = input("\nTry again? (y/n): ").lower().startswith('y')
        if retry and context == "single_website_analysis":
            self.single_website_analysis()

    def manage_config(self):
        """Manage configuration settings"""
        print("\n" + "="*60)
        print("⚙️ CONFIGURATION MANAGEMENT")
        print("="*60)
        
        print("\n📋 Current Configuration:")
        
        # Show current API key status
        api_key = None
        if os.path.exists('config.py'):
            try:
                import importlib.util
                spec = importlib.util.spec_from_file_location("config", "config.py")
                config = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(config)
                
                if hasattr(config, 'FIRECRAWL_API_KEY'):
                    api_key = config.FIRECRAWL_API_KEY
                    if api_key != 'your-api-key-here':
                        print(f"🔑 Firecrawl API Key: {api_key[:8]}...{api_key[-4:]} (saved)")
                    else:
                        print("🔑 Firecrawl API Key: Not configured")
                
                if hasattr(config, 'REPORTS_DIR'):
                    print(f"📁 Reports Directory: {config.REPORTS_DIR}")
                
                if hasattr(config, 'DEFAULT_SAVE_FORMAT'):
                    print(f"💾 Default Save Format: {config.DEFAULT_SAVE_FORMAT}")
                    
            except Exception as e:
                print(f"⚠️ Error reading config: {e}")
        else:
            print("📄 No config.py file found")
        
        print("\n📋 Configuration Options:")
        print("1. 🔑 Update Firecrawl API Key")
        print("2. 📁 Change Reports Directory")
        print("3. 💾 Set Default Save Format")
        print("4. 🔄 Reset Configuration")
        print("5. 📄 View Full Configuration")
        print("6. ⬅️ Back to Main Menu")
        
        choice = self.get_user_input("\n⚙️ Select option (1-6): ", "int")
        
        if choice == 1:
            self.update_api_key()
        elif choice == 2:
            self.update_reports_dir()
        elif choice == 3:
            self.update_save_format()
        elif choice == 4:
            self.reset_configuration()
        elif choice == 5:
            self.view_full_config()
        elif choice == 6:
            return
        else:
            print("❌ Please select a number between 1 and 6.")
    
    def update_api_key(self):
        """Update the Firecrawl API key"""
        print("\n🔑 Update Firecrawl API Key")
        print("Get your API key from: https://firecrawl.dev")
        
        new_key = input("\nEnter new API key: ").strip()
        if new_key:
            self.save_api_key_to_config(new_key)
            print("✅ API key updated! Restart the application to use the new key.")
        else:
            print("❌ No key entered, keeping current configuration.")
    
    def update_reports_dir(self):
        """Update the reports directory"""
        print("\n📁 Update Reports Directory")
        print(f"Current directory: {self.reports_dir}")
        
        new_dir = input("\nEnter new reports directory name: ").strip()
        if new_dir:
            self.reports_dir = new_dir
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            self.update_config_setting('REPORTS_DIR', f"'{new_dir}'")
            print(f"✅ Reports directory updated to: {new_dir}")
        else:
            print("❌ No directory entered, keeping current configuration.")
    
    def update_save_format(self):
        """Update the default save format"""
        print("\n💾 Update Default Save Format")
        print("Available formats:")
        print("1. txt - Plain text")
        print("2. csv - Comma-separated values")
        print("3. html - Web page")
        print("4. pdf - PDF document") 
        print("5. json - JSON data")
        print("6. html_charts - HTML with charts")
        
        format_map = {
            1: 'txt', 2: 'csv', 3: 'html',
            4: 'pdf', 5: 'json', 6: 'html_charts'
        }
        
        choice = self.get_user_input("\nSelect format (1-6): ", "int")
        if choice in format_map:
            new_format = format_map[choice]
            self.update_config_setting('DEFAULT_SAVE_FORMAT', f"'{new_format}'")
            print(f"✅ Default save format updated to: {new_format}")
        else:
            print("❌ Invalid choice, keeping current configuration.")
    
    def reset_configuration(self):
        """Reset configuration to defaults"""
        print("\n🔄 Reset Configuration")
        confirm = input("This will reset all settings to defaults. Continue? (y/n): ").lower().startswith('y')
        
        if confirm:
            try:
                if os.path.exists('config.py'):
                    os.remove('config.py')
                print("✅ Configuration reset. You'll be prompted for settings on next startup.")
            except Exception as e:
                print(f"❌ Error resetting config: {e}")
        else:
            print("❌ Reset cancelled.")
    
    def view_full_config(self):
        """View the full configuration file"""
        print("\n📄 Full Configuration")
        print("-" * 60)
        
        if os.path.exists('config.py'):
            try:
                with open('config.py', 'r', encoding='utf-8') as f:
                    content = f.read()
                print(content)
            except Exception as e:
                print(f"❌ Error reading config file: {e}")
        else:
            print("No config.py file found.")
        
        print("-" * 60)
        input("Press Enter to continue...")
    
    def update_config_setting(self, setting_name, setting_value):
        """Update a specific setting in the config file"""
        try:
            if os.path.exists('config.py'):
                # Read current config
                with open('config.py', 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                # Update the specific setting
                updated = False
                for i, line in enumerate(lines):
                    if line.strip().startswith(f'{setting_name} ='):
                        lines[i] = f'{setting_name} = {setting_value}\n'
                        updated = True
                        break
                
                # If setting not found, add it
                if not updated:
                    lines.append(f'\n{setting_name} = {setting_value}\n')
                
                # Write back to file
                with open('config.py', 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                
                print(f"✅ Updated {setting_name} in config.py")
            else:
                print("❌ No config file found to update.")
                
        except Exception as e:
            print(f"❌ Error updating config: {e}")

    # Report saving functionality
    def save_report_options(self):
        """Ask user about report saving preferences"""
        print("\n💾 Save Report Options:")
        print("1. 📄 Text file (.txt)")
        print("2. 📊 CSV file (.csv)")
        print("3. 🌐 HTML file (.html)")
        print("4. 📋 PDF file (.pdf)")
        print("5. 📁 JSON file (.json)")
        print("6. 🎨 HTML with Charts (.html)")
        print("7. ❌ Don't save")
        
        choice = self.get_user_input("\nSelect save format (1-7): ", "int")
        
        if choice == 7 or not choice:
            return None
        
        format_map = {
            1: "txt", 2: "csv", 3: "html",
            4: "pdf", 5: "json", 6: "html_charts"
        }
        
        return format_map.get(choice, None)

    def save_report(self, data, analysis_type, url=None):
        """Save report in user's chosen format"""
        save_format = self.save_report_options()
        
        if not save_format:
            print("📋 Report not saved (user choice)")
            return
        
        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if url:
            clean_url = url.replace('https://', '').replace('http://', '').replace('/', '_').replace(':', '')[:30]
            filename = f"{self.reports_dir}/{analysis_type}_{clean_url}_{timestamp}"
        else:
            filename = f"{self.reports_dir}/{analysis_type}_{timestamp}"
        
        # Save in requested format
        if save_format == "json":
            self.save_as_json(data, f"{filename}.json")
        elif save_format == "txt":
            self.save_as_txt(data, f"{filename}.txt")
        elif save_format == "csv":
            self.save_as_csv(data, f"{filename}.csv")
        elif save_format == "html":
            self.save_as_html(data, f"{filename}.html", False)
        elif save_format == "html_charts":
            self.save_as_html(data, f"{filename}.html", True)
        elif save_format == "pdf":
            self.save_as_pdf(data, f"{filename}.pdf")
        
        print(f"📁 Report saved in: {self.reports_dir}/")

    def save_as_json(self, data, filename):
        """Save report as JSON file"""
        report_data = {
            "timestamp": datetime.now().isoformat(),
            "analysis_data": data,
            "generated_by": "Universal Firecrawl + Ollama System"
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ JSON report saved: {filename}")

    def save_as_txt(self, data, filename):
        """Save report as text file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("UNIVERSAL FIRECRAWL + OLLAMA ANALYSIS REPORT\n")
            f.write("="*80 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            if isinstance(data, dict):
                for key, value in data.items():
                    f.write(f"{key.upper().replace('_', ' ')}:\n")
                    f.write("-" * 40 + "\n")
                    f.write(f"{value}\n\n")
            else:
                f.write(str(data))
        
        print(f"✅ Text report saved: {filename}")

    def save_as_csv(self, data, filename):
        """Save report as CSV file"""
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Field", "Value"])
            
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            if isinstance(data, dict):
                for key, value in data.items():
                    writer.writerow([timestamp, key.replace('_', ' ').title(), str(value)[:1000]])
            else:
                writer.writerow([timestamp, "Analysis", str(data)[:1000]])
        
        print(f"✅ CSV report saved: {filename}")

    def save_as_html(self, data, filename, include_charts=False):
        """Save report as HTML file with optional charts"""
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Universal Firecrawl + Ollama Analysis Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; background-color: #f4f4f4; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
        .header {{ text-align: center; color: #333; border-bottom: 3px solid #007acc; padding-bottom: 20px; margin-bottom: 30px; }}
        .section {{ margin-bottom: 30px; padding: 20px; background: #f9f9f9; border-radius: 5px; border-left: 4px solid #007acc; }}
        .section h2 {{ color: #007acc; margin-top: 0; }}
        .metadata {{ background: #e7f3ff; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
        .analysis-content {{ background: white; padding: 20px; border-radius: 5px; white-space: pre-wrap; font-family: 'Courier New', monospace; border: 1px solid #ddd; }}
        .footer {{ text-align: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; color: #666; }}
    </style>"""
        
        if include_charts:
            html_content += '<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>'
        
        html_content += f"""
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔥 Universal Firecrawl + Ollama Analysis Report</h1>
            <p>Generated on {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}</p>
        </div>
        
        <div class="metadata">
            <h3>📊 Report Information</h3>
            <p><strong>Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p><strong>System:</strong> Universal Firecrawl + Ollama Integration</p>"""
        
        if isinstance(data, dict):
            if 'url' in data:
                html_content += f'<p><strong>Analyzed URL:</strong> <a href="{data["url"]}" target="_blank">{data["url"]}</a></p>'
            if 'model' in data:
                html_content += f'<p><strong>AI Model:</strong> {data["model"]}</p>'
        
        html_content += "</div>"
        
        # Add analysis sections
        if isinstance(data, dict):
            for key, value in data.items():
                if key not in ['url', 'model', 'timestamp']:
                    html_content += f"""
                    <div class="section">
                        <h2>{key.replace('_', ' ').title()}</h2>
                        <div class="analysis-content">{str(value)}</div>
                    </div>"""
        else:
            html_content += f"""
                <div class="section">
                    <h2>Analysis Results</h2>
                    <div class="analysis-content">{str(data)}</div>
                </div>"""
        
        html_content += """
            <div class="footer">
                <p>Report generated by <strong>Universal Firecrawl + Ollama Integration System</strong></p>
                <p>For more information, visit <a href="https://firecrawl.dev">Firecrawl</a> and <a href="https://ollama.com">Ollama</a></p>
            </div>
        </div>
    </body>
    </html>"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        chart_note = " with charts" if include_charts else ""
        print(f"✅ HTML report{chart_note} saved: {filename}")
        print(f"🌐 Open in browser: file://{os.path.abspath(filename)}")

    def save_as_pdf(self, data, filename):
        """Save report as PDF file with fallback"""
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            
            doc = SimpleDocTemplate(filename, pagesize=A4)
            styles = getSampleStyleSheet()
            story = []
            
            # Title
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                spaceAfter=30,
                alignment=1
            )
            story.append(Paragraph("Universal Firecrawl + Ollama Analysis Report", title_style))
            story.append(Spacer(1, 12))
            
            # Timestamp
            story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
            story.append(Spacer(1, 20))
            
            # Content
            if isinstance(data, dict):
                for key, value in data.items():
                    story.append(Paragraph(key.replace('_', ' ').title(), styles['Heading2']))
                    story.append(Spacer(1, 12))
                    
                    text_content = str(value)
                    paragraphs = text_content.split('\n\n')
                    for para in paragraphs:
                        if para.strip():
                            story.append(Paragraph(para.strip(), styles['Normal']))
                            story.append(Spacer(1, 12))
                    
                    story.append(Spacer(1, 20))
            else:
                story.append(Paragraph("Analysis Results", styles['Heading2']))
                story.append(Spacer(1, 12))
                story.append(Paragraph(str(data), styles['Normal']))
            
            doc.build(story)
            print(f"✅ PDF report saved: {filename}")
            
        except ImportError:
            print("❌ PDF generation requires 'reportlab' package.")
            print("💡 Install with: pip install reportlab")
            print("🔄 Saving as HTML instead...")
            
            html_filename = filename.replace('.pdf', '.html')
            self.save_as_html(data, html_filename)

    def main_menu(self):
        """Dynamic main menu"""
        while True:
            print("\n" + "🔥"*20)
            print("🚀 UNIVERSAL FIRECRAWL + OLLAMA SYSTEM")
            print("🔥"*20)
            print(f"🤖 {len(self.working_models)} models ready | 📁 Reports: {self.reports_dir}/")
            print("\n📋 Choose an option:")
            print("1. 🔍 Single Website Analysis")
            print("2. 🏆 Model Comparison")
            print("3. 🏗️ Structured Data Extraction")
            print("4. 🤖 View Your Models")
            print("5. 🔄 Refresh Model List")
            print("6. ⚙️ Configuration Settings")
            print("7. ❌ Exit")
            
            choice = self.get_user_input("\n🎯 Select option (1-7): ", "int")
            
            if choice == 1:
                self.single_website_analysis()
            elif choice == 2:
                self.model_comparison()
            elif choice == 3:
                self.structured_extraction()
            elif choice == 4:
                self.display_available_models()
            elif choice == 5:
                print("🔄 Refreshing model list...")
                self.model_manager.refresh_models()
                self.working_models = self.model_manager.get_working_models()
                self.model_categories = self.model_manager.categorize_models(self.working_models)
                print(f"✅ Found {len(self.working_models)} working models")
            elif choice == 6:
                self.manage_config()
            elif choice == 7:
                print("\n👋 Thanks for using the Universal Firecrawl + Ollama System!")
                break
            else:
                print("❌ Please select a number between 1 and 7.")
            
            # Continue option
            if choice in [1, 2, 3, 4, 5, 6]:
                continue_choice = input("\n❓ Run another operation? (y/n): ").lower()
                if not continue_choice.startswith('y'):
                    print("\n👋 Thanks for using the Universal Firecrawl + Ollama System!")
                    break

def main():
    """Main entry point"""
    print("🔥 Universal Firecrawl + Ollama Integration System")
    print("=" * 60)
    print("🎯 Automatically detects and works with YOUR setup!")
    print("=" * 60)
    
    system = FirecrawlOllamaSystem()
    
    # Setup Firecrawl
    if not system.setup_firecrawl():
        print("❌ Cannot continue without Firecrawl")
        return
    
    # Setup Ollama  
    if not system.setup_ollama():
        print("❌ Cannot continue without Ollama")
        return
    
    # Show user their setup
    system.display_available_models()
    
    print(f"\n🎉 System ready with {len(system.working_models)} working models!")
    print(f"📁 Reports will be saved to: {system.reports_dir}/")
    
    # Start main menu
    system.main_menu()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please report this issue with your system details.")