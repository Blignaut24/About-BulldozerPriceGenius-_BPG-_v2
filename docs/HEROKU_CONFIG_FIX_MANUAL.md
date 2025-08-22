# Manual Heroku Configuration Fix

## 🎯 **Problem**: Model Configuration Required Error

The error occurs because the `GOOGLE_DRIVE_MODEL_ID` environment variable is not set in your Heroku app.

## 🔧 **Solution: Set Environment Variable**

### **Method 1: Using Heroku CLI (Recommended)**

```bash
# Set the environment variable
heroku config:set GOOGLE_DRIVE_MODEL_ID="1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp" --app your-app-name

# Verify it's set
heroku config:get GOOGLE_DRIVE_MODEL_ID --app your-app-name

# Restart the app
heroku restart --app your-app-name
```

### **Method 2: Using Heroku Dashboard (Web Interface)**

1. **Go to Heroku Dashboard**: https://dashboard.heroku.com
2. **Select your BulldozerPriceGenius app**
3. **Click the "Settings" tab**
4. **Scroll down to "Config Vars" section**
5. **Click "Reveal Config Vars"**
6. **Add new config var**:
   - **KEY**: `GOOGLE_DRIVE_MODEL_ID`
   - **VALUE**: `1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp`
7. **Click "Add"**
8. **Restart your app**:
   - Go to "More" menu (top right)
   - Click "Restart all dynos"

## 🔍 **Verification Steps**

### **1. Check Environment Variable is Set**

**Via CLI:**
```bash
heroku config --app your-app-name
```

**Expected Output:**
```
GOOGLE_DRIVE_MODEL_ID: 1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp
```

**Via Dashboard:**
- Go to Settings → Config Vars
- You should see `GOOGLE_DRIVE_MODEL_ID` listed

### **2. Test the Application**

1. **Open your app**: `heroku open --app your-app-name`
2. **Navigate to Interactive Prediction page**
3. **Look for these messages**:
   - ✅ `🌐 Loading ML model from external storage...`
   - ✅ `🔄 Downloading ML model from Google Drive...`
   - ✅ `📥 Downloading model file (561MB)...`
   - ✅ `✅ Model loaded successfully in X seconds!`

### **3. Monitor Logs**

```bash
heroku logs --tail --app your-app-name
```

**Expected Log Messages:**
```
🌐 Loading ML model from external storage...
📋 Configuration:
   File ID: 1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp
🔄 Downloading ML model from Google Drive...
✅ External ML Model loaded successfully!
```

## 🚨 **Troubleshooting**

### **Issue 1: Environment Variable Not Found**

**Symptoms:**
- Still seeing "Model Configuration Required" error
- `heroku config` doesn't show `GOOGLE_DRIVE_MODEL_ID`

**Solutions:**
1. Double-check the app name is correct
2. Ensure you have access to the Heroku app
3. Try setting via Dashboard instead of CLI
4. Wait 1-2 minutes after setting before testing

### **Issue 2: App Not Restarting**

**Symptoms:**
- Environment variable is set but error persists
- Old cached configuration still active

**Solutions:**
```bash
# Force restart all dynos
heroku restart --app your-app-name

# Or restart specific dyno type
heroku ps:restart web --app your-app-name

# Check dyno status
heroku ps --app your-app-name
```

### **Issue 3: Permission Denied**

**Symptoms:**
- "You do not have access to the app" error

**Solutions:**
1. Verify you're logged into the correct Heroku account
2. Check if you're a collaborator on the app
3. Contact the app owner to add you as a collaborator

### **Issue 4: Model Download Fails**

**Symptoms:**
- Environment variable is set correctly
- Still getting download errors

**Solutions:**
1. Check Google Drive file is still accessible
2. Verify file ID is correct: `1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp`
3. Test direct download URL: https://drive.google.com/uc?export=download&id=1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp

## ✅ **Success Indicators**

Your fix is successful when you see:

1. **✅ Environment variable set**: `heroku config` shows `GOOGLE_DRIVE_MODEL_ID`
2. **✅ App restarts cleanly**: No errors in `heroku logs`
3. **✅ Model loads**: Progress bar appears and completes
4. **✅ Predictions work**: Can make bulldozer price predictions
5. **✅ No error messages**: "Model Configuration Required" error is gone

## 📞 **Still Need Help?**

If the issue persists:

1. **Check logs**: `heroku logs --tail --app your-app-name`
2. **Verify app name**: `heroku apps` (lists all your apps)
3. **Test locally**: `streamlit run app.py` (should work with `.streamlit/secrets.toml`)
4. **Check file access**: Visit the Google Drive URL directly

## 🎉 **Expected Final Result**

After fixing the configuration, your app should:
- Load the 561MB model from Google Drive on first access (30-60 seconds)
- Cache the model for instant subsequent predictions
- Display progress during model download
- Work identically to the local version
- No longer show configuration errors

---

**The fix is complete when you can successfully make bulldozer price predictions without any configuration errors!**
