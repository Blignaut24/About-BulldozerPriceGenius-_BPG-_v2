# 🚨 **Heroku Deployment Diagnostic Guide**
## BulldozerPriceGenius Application Error Resolution

---

## 🔍 **Step 1: Retrieve Heroku Logs**

### **📋 Commands to Run:**

```bash
# 1. Get your Heroku app name (if you don't know it)
heroku apps

# 2. View real-time logs (run this in a separate terminal and keep it open)
heroku logs --tail --app your-app-name

# 3. View recent log history (500 lines)
heroku logs --lines 500 --app your-app-name

# 4. View specific log types
heroku logs --source app --app your-app-name
heroku logs --source heroku --app your-app-name

# 5. Check dyno status
heroku ps --app your-app-name

# 6. Check config variables
heroku config --app your-app-name
```

### **🔍 What to Look For in Logs:**

1. **Import Errors**: `ModuleNotFoundError`, `ImportError`
2. **Memory Issues**: `R14 (Memory quota exceeded)`, `R15 (Memory quota vastly exceeded)`
3. **Timeout Issues**: `R10 (Boot timeout)`, `H12 (Request timeout)`
4. **Port Binding Issues**: `Error R10 (Boot timeout) -> Web process failed to bind to $PORT`
5. **File Path Issues**: `FileNotFoundError`, `No such file or directory`
6. **Dependency Issues**: Package version conflicts, missing dependencies

---

## 🔧 **Step 2: Common Issues and Fixes**

### **✅ Issue 1: Memory Limit Exceeded**
**Symptoms**: `R14`, `R15` errors, app crashes during model loading

**Fix**: Update `external_model_loader_v3_optimized.py` to use memory-efficient loading:

```python
# Add to the model loader class
def _load_model_memory_efficient(self, model_path: str):
    """Load model with memory optimization for Heroku"""
    import gc
    
    # Clear memory before loading
    gc.collect()
    
    # Load with memory mapping if possible
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    except MemoryError:
        # Fallback: try loading in chunks or use joblib
        import joblib
        return joblib.load(model_path, mmap_mode='r')
```

### **✅ Issue 2: Port Binding Error**
**Symptoms**: `Web process failed to bind to $PORT`

**Current Procfile**: ✅ Already correct
```
web: sh setup.sh && streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true --server.enableCORS=false --server.enableXsrfProtection=false
```

### **✅ Issue 3: Import/Dependency Issues**
**Symptoms**: `ModuleNotFoundError`, package conflicts

**Check**: Verify all imports in main files work:
```bash
# Test locally first
python -c "import streamlit, numpy, pandas, scikit-learn, joblib, matplotlib, seaborn"
```

### **✅ Issue 4: File Path Issues**
**Symptoms**: `FileNotFoundError` for model files

**Fix**: Ensure all paths are relative and case-sensitive:
```python
# In external_model_loader_v3_optimized.py
self.preprocessing_path = "src/models/preprocessing_components.pkl"  # ✅ Relative path
```

### **✅ Issue 5: Streamlit Configuration Issues**
**Current setup.sh**: ✅ Looks correct, but may need updates

---

## 🛠️ **Step 3: Immediate Fixes to Try**

### **🔧 Fix 1: Update Streamlit Configuration**
Create/update `.streamlit/config.toml`:

```toml
[server]
port = 8501
headless = true
enableCORS = false
enableXsrfProtection = false
maxUploadSize = 200

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#FF6B35"
backgroundColor = "#1e1e1e"
secondaryBackgroundColor = "#2d2d2d"
textColor = "#ffffff"

[runner]
magicEnabled = false
```

### **🔧 Fix 2: Add Runtime Specification**
Create `runtime.txt`:
```
python-3.11.9
```

### **🔧 Fix 3: Update Requirements for Heroku Compatibility**
Check if any packages need version updates:

```txt
# Critical: Ensure numpy compatibility
numpy>=1.21.0,<2.0.0
pandas>=1.3.0,<3.0.0
scikit-learn>=1.0.0,<2.0.0
streamlit>=1.28.0,<2.0.0
```

### **🔧 Fix 4: Add Error Handling to App Startup**
Update `app.py` with error handling:

```python
import streamlit as st
import sys
import traceback

try:
    from app_pages.multipage import MultiPage
    # ... rest of imports
except ImportError as e:
    st.error(f"Import Error: {e}")
    st.error("Please check that all dependencies are installed correctly.")
    st.stop()

try:
    # Create an instance of the app
    app = MultiPage(app_name="BulldozerPriceGenius(BPG)")
    # ... rest of app setup
    app.run()
except Exception as e:
    st.error(f"Application Error: {e}")
    st.error("Full traceback:")
    st.code(traceback.format_exc())
```

---

## 🧪 **Step 4: Testing and Deployment**

### **📋 Local Testing First:**
```bash
# 1. Test locally with Heroku-like environment
pip install -r requirements.txt
streamlit run app.py --server.port=8501 --server.address=0.0.0.0 --server.headless=true

# 2. Test specific imports
python -c "from app_pages.four_interactive_prediction import interactive_prediction_body"
```

### **🚀 Deploy to Heroku:**
```bash
# 1. Commit changes
git add .
git commit -m "fix: resolve Heroku deployment issues"

# 2. Deploy
git push heroku main

# 3. Monitor logs during deployment
heroku logs --tail --app your-app-name

# 4. Check dyno status
heroku ps --app your-app-name

# 5. Restart if needed
heroku restart --app your-app-name
```

---

## 🔍 **Step 5: Advanced Diagnostics**

### **📊 Check Resource Usage:**
```bash
# Check dyno metrics
heroku logs --dyno web.1 --app your-app-name

# Check for memory issues
heroku logs --app your-app-name | grep -E "R14|R15|Memory"

# Check for timeout issues  
heroku logs --app your-app-name | grep -E "R10|H12|timeout"
```

### **🔧 Emergency Fixes:**

**If model loading fails**, add this to `external_model_loader_v3_optimized.py`:
```python
def get_fallback_model(self):
    """Provide a simple fallback model if main model fails to load"""
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.preprocessing import StandardScaler
    
    # Create a minimal model for basic functionality
    model = RandomForestRegressor(n_estimators=10, random_state=42)
    scaler = StandardScaler()
    
    return model, {'scaler': scaler}
```

---

## 📞 **Next Steps**

1. **Run the log commands above** and share the output
2. **Look for specific error patterns** mentioned in this guide
3. **Apply the relevant fixes** based on the errors found
4. **Test locally first** before deploying to Heroku
5. **Monitor deployment logs** during the fix deployment

**Most Common Issues:**
- Memory limit exceeded during model loading
- Import errors due to dependency conflicts
- File path issues with model files
- Streamlit configuration problems

Share the Heroku logs output, and I'll provide specific fixes for your exact error! 🚀
