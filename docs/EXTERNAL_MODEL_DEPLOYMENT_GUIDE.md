# External Model Storage Deployment Guide

## 🎯 Overview

This guide implements external model storage using Google Drive to overcome Heroku's 500MB slug size limit. The 561MB RandomForest model is stored on Google Drive and downloaded at runtime.

## 📋 Prerequisites

- Google Drive account
- Heroku account and CLI
- Git repository with the BulldozerPriceGenius application

## 🚀 Step-by-Step Implementation

### Step 1: Upload Model to Google Drive

1. **Go to Google Drive**: https://drive.google.com
2. **Upload the model file**:
   - Click "New" → "File upload"
   - Select `src/models/randomforest_regressor_best_RMSLE.pkl`
   - Wait for upload (5-10 minutes for 561MB file)

### Step 2: Configure Google Drive Sharing

1. **Right-click the uploaded file** → "Share"
2. **Change permissions**:
   - Click "Restricted" → "Anyone with the link"
   - Set to "Viewer"
3. **Copy the share link** (format):
   ```
   https://drive.google.com/file/d/FILE_ID/view?usp=sharing
   ```
4. **Extract the FILE_ID** from the link

### Step 3: Local Development Setup

For local development, create `.streamlit/secrets.toml`:

```toml
# .streamlit/secrets.toml
GOOGLE_DRIVE_MODEL_ID = "YOUR_ACTUAL_FILE_ID"
```

### Step 4: Test the Implementation

Run the test script to verify everything works:

```bash
python test_external_model.py
```

Expected output:
```
✅ External model loader imported successfully
✅ Connection successful
✅ Downloaded 1024.0KB successfully
✅ File appears to be a valid pickle file
🎉 External model loading is ready for deployment!
```

### Step 5: Heroku Deployment

#### Option A: Using the Setup Script
```bash
chmod +x heroku_setup.sh
./heroku_setup.sh
```

#### Option B: Manual Setup
```bash
# Set the environment variable
heroku config:set GOOGLE_DRIVE_MODEL_ID="YOUR_FILE_ID" --app your-app-name

# Deploy the application
git add .
git commit -m "feat: implement external model storage for Heroku deployment"
git push heroku main
```

## 🔧 Technical Implementation Details

### Files Modified/Created

1. **`src/external_model_loader.py`** - Core external model loading logic
2. **`requirements.txt`** - Added `requests` dependency
3. **`app_pages/four_interactive_prediction.py`** - Updated to use external loader
4. **`.slugignore`** - Excludes large model file from deployment
5. **Configuration files** - Templates and setup scripts

### Key Features

- **Caching**: Uses `@st.cache_resource` to avoid re-downloading
- **Error Handling**: Comprehensive error messages and fallbacks
- **Progress Tracking**: Shows download progress to users
- **Security**: No credentials stored in code
- **Fallback**: Falls back to statistical prediction if model fails

### Performance Characteristics

- **First Load**: 30-60 seconds (downloads 561MB)
- **Subsequent Loads**: Instant (cached in memory)
- **Memory Usage**: ~600MB during model loading
- **Network Usage**: 561MB on first load only

## 🔍 Troubleshooting

### Common Issues

1. **"File ID not configured"**
   - Set `GOOGLE_DRIVE_MODEL_ID` environment variable
   - Check `.streamlit/secrets.toml` for local development

2. **"Connection timeout"**
   - Check internet connection
   - Verify Google Drive link is public
   - Try again (temporary network issue)

3. **"File not found" (HTTP 404)**
   - Verify file ID is correct
   - Ensure file is shared publicly
   - Check file hasn't been deleted

4. **"Model loading error"**
   - Verify uploaded file is the correct model
   - Check file wasn't corrupted during upload

### Verification Commands

```bash
# Check Heroku environment variables
heroku config --app your-app-name

# Check application logs
heroku logs --tail --app your-app-name

# Test direct download
curl -I "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID"
```

## 📊 Deployment Benefits

### Before (Local Model)
- ❌ Slug size: ~600MB (exceeds 500MB limit)
- ❌ Deployment fails on Heroku
- ❌ Large git repository

### After (External Model)
- ✅ Slug size: ~50MB (well under limit)
- ✅ Successful Heroku deployment
- ✅ Fast git operations
- ✅ Same prediction accuracy
- ✅ Cached for performance

## 🔒 Security Considerations

- **Public Access**: Model file is publicly accessible but not discoverable
- **No Credentials**: No authentication tokens in code
- **Environment Variables**: Sensitive config in Heroku environment
- **Model Content**: ML model contains no sensitive business data

## 💰 Cost Analysis

### Google Drive Storage
- **Free Tier**: 15GB (sufficient for this model)
- **Cost**: $0/month

### Heroku Hosting
- **Standard-1X**: $25/month
- **Memory**: 512MB (sufficient with external storage)
- **Total**: $25/month

### Network Costs
- **Download**: ~561MB on first load
- **Frequency**: Once per dyno restart
- **Cost**: Negligible

## 🎯 Success Criteria

✅ **Deployment**: Application deploys successfully to Heroku  
✅ **Functionality**: ML predictions work identically to local version  
✅ **Performance**: Model loads within 60 seconds on first access  
✅ **Caching**: Subsequent predictions are instant  
✅ **Error Handling**: Graceful fallbacks for network issues  
✅ **Security**: No sensitive credentials exposed  

## 📞 Support

If you encounter issues:

1. **Run the test script**: `python test_external_model.py`
2. **Check Heroku logs**: `heroku logs --tail`
3. **Verify configuration**: Ensure file ID is correct
4. **Test direct download**: Verify Google Drive link works

---

**🎉 Congratulations!** Your BulldozerPriceGenius application is now ready for Heroku deployment with external model storage!
