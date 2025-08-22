# BulldozerPriceGenius - Heroku Deployment Guide

## 🔒 Security-First Deployment Guide

This guide provides step-by-step instructions for securely deploying the BulldozerPriceGenius application to Heroku with comprehensive security measures.

## 📋 Prerequisites

- Heroku CLI installed and configured
- Git repository with the application code
- Heroku account with appropriate permissions
- Python 3.12+ environment

## 🛡️ Security Checklist (CRITICAL)

Before deployment, verify these security measures are in place:

### ✅ Sensitive Files Protection
- [ ] `.gitignore` excludes: `env.py`, `kaggle.json`, `cloudinary_python.txt`
- [ ] `.slugignore` excludes: `*.env`, `.env*`, `secrets.toml`, `*.key`, `*.pem`
- [ ] No hardcoded API keys, passwords, or credentials in source code
- [ ] No database connection strings or authentication tokens exposed

### ✅ Configuration Files Verified
- [ ] `requirements.txt` contains only production dependencies
- [ ] `Procfile` configured for Streamlit with proper port binding
- [ ] `setup.sh` creates secure Streamlit configuration
- [ ] `.slugignore` optimized to reduce slug size and exclude sensitive files

## 📁 Required Files for Deployment

### 1. requirements.txt
```
# BulldozerPriceGenius - Heroku Deployment Requirements
# SECURITY: This file contains only production dependencies for Heroku deployment

# Core Streamlit and web framework
streamlit>=1.18.0,<2.0.0
altair>=4.2.0,<5.0.0

# Data science and machine learning (core dependencies)
numpy>=1.21.0,<3.0.0
pandas>=1.3.0,<3.0.0
scikit-learn>=1.0.0,<2.0.0
joblib>=1.0.0,<2.0.0

# Visualization
matplotlib>=3.5.0,<4.0.0
seaborn>=0.11.0,<1.0.0

# Essential utilities only
tqdm>=4.60.0,<5.0.0
```

### 2. Procfile
```
web: sh setup.sh && streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

### 3. setup.sh
```bash
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"\"\n\
\n\
[server]\n\
headless = true\n\
enableCORS = false\n\
enableXsrfProtection = false\n\
port = \$PORT\n\
\n\
[theme]\n\
primaryColor = \"#FF6B6B\"\n\
backgroundColor = \"#FFFFFF\"\n\
secondaryBackgroundColor = \"#F0F2F6\"\n\
textColor = \"#262730\"\n\
" > ~/.streamlit/config.toml
```

## 🚀 Deployment Steps

### Step 1: Prepare Local Environment
```bash
# Activate the myenv virtual environment
source myenv/Scripts/activate  # Windows Git Bash
# or
myenv\Scripts\activate.bat      # Windows CMD

# Verify Python and dependencies
python --version
pip list | grep streamlit
```

### Step 2: Security Verification
```bash
# Check for sensitive files (should return empty)
find . -name "*.env" -o -name "secrets.toml" -o -name "kaggle.json"

# Verify .gitignore and .slugignore are properly configured
cat .gitignore
cat .slugignore
```

### Step 3: Test Application Locally
```bash
# Test core dependencies
python -c "import streamlit as st; import pandas as pd; import numpy as np; print('Dependencies OK')"

# Test application imports
python -c "import app; print('App imports successfully')"
```

### Step 4: Heroku Setup
```bash
# Login to Heroku
heroku login

# Create new Heroku app (replace 'your-app-name' with desired name)
heroku create your-bulldozer-price-genius-app

# Set Python runtime (optional - Heroku auto-detects)
echo "python-3.12.8" > runtime.txt
```

### Step 5: Deploy to Heroku
```bash
# Add files to git
git add .
git commit -m "Prepare for Heroku deployment with security measures"

# Deploy to Heroku
git push heroku main

# Monitor deployment logs
heroku logs --tail
```

### Step 6: Post-Deployment Verification
```bash
# Open the deployed application
heroku open

# Check application status
heroku ps:scale web=1
heroku ps

# Monitor logs for any issues
heroku logs --tail
```

## 🔧 Environment Configuration

### Heroku Environment Variables
If your application requires environment variables, set them securely:

```bash
# Example (only if needed - current app doesn't require these)
heroku config:set ENVIRONMENT=production
heroku config:set DEBUG=false

# View current config
heroku config
```

### Buildpack Configuration
Heroku automatically detects Python applications. If needed:

```bash
# Set Python buildpack explicitly
heroku buildpacks:set heroku/python
```

## 📊 Application Structure

The deployed application includes:
- **Main App**: `app.py` - Entry point
- **Pages**: `app_pages/` - Multi-page application structure
- **Models**: `src/models/` - ML models (only essential files included)
- **Static Assets**: `static/` - Images and resources (optimized)

## 🚨 Security Best Practices

### What's Protected:
- ✅ No sensitive credentials in source code
- ✅ Virtual environments excluded from deployment
- ✅ Development files excluded via .slugignore
- ✅ Large data files excluded to reduce slug size
- ✅ Test files and documentation excluded

### What's Included:
- ✅ Essential ML models only
- ✅ Production dependencies only
- ✅ Optimized static assets
- ✅ Core application files

## 🔍 Troubleshooting

### Common Issues:

1. **Slug Size Too Large**
   - Check `.slugignore` is properly configured
   - Ensure large data files are excluded
   - Verify virtual environments are excluded

2. **Application Won't Start**
   - Check `heroku logs --tail` for errors
   - Verify `Procfile` syntax
   - Ensure all dependencies are in `requirements.txt`

3. **Import Errors**
   - Verify all required packages are in `requirements.txt`
   - Check for missing dependencies
   - Ensure Python version compatibility

4. **Port Binding Issues**
   - Verify `Procfile` uses `$PORT` environment variable
   - Check `setup.sh` configuration

### Useful Commands:
```bash
# Restart application
heroku restart

# Scale dynos
heroku ps:scale web=1

# Access bash shell
heroku run bash

# View application info
heroku info
```

## 📞 Support

For deployment issues:
1. Check Heroku logs: `heroku logs --tail`
2. Verify security checklist above
3. Ensure all configuration files are properly formatted
4. Test locally before deploying

## 🔄 Updates and Maintenance

To update the deployed application:
```bash
# Make changes locally
git add .
git commit -m "Update application"

# Deploy updates
git push heroku main

# Monitor deployment
heroku logs --tail
```

---

**⚠️ SECURITY REMINDER**: Never commit sensitive information to your repository. Always verify the security checklist before deployment.
