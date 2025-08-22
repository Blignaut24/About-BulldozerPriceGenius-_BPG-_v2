# Google Drive Model Storage Setup Instructions

## 📤 Step 1: Upload Model to Google Drive

1. **Navigate to Google Drive**: Go to https://drive.google.com
2. **Upload the Model File**:
   - Click "New" → "File upload"
   - Select `src/models/randomforest_regressor_best_RMSLE.pkl` (561MB)
   - Wait for upload to complete (may take 5-10 minutes)

## 🔗 Step 2: Generate Shareable Link

1. **Right-click on the uploaded file** in Google Drive
2. **Select "Share"**
3. **Change permissions**:
   - Click "Restricted" → "Anyone with the link"
   - Set permission to "Viewer"
4. **Copy the share link** (will look like):
   ```
   https://drive.google.com/file/d/1ABC123DEF456GHI789JKL/view?usp=sharing
   ```

## 🔄 Step 3: Convert to Direct Download Link

**Original Google Drive link format**:
```
https://drive.google.com/file/d/FILE_ID/view?usp=sharing
```

**Convert to direct download format**:
```
https://drive.google.com/uc?export=download&id=FILE_ID
```

**Example**:
- Original: `https://drive.google.com/file/d/1ABC123DEF456GHI789JKL/view?usp=sharing`
- Direct: `https://drive.google.com/uc?export=download&id=1ABC123DEF456GHI789JKL`

## 📝 Step 4: Extract File ID

From your Google Drive share link, extract the FILE_ID:
```
https://drive.google.com/file/d/[FILE_ID]/view?usp=sharing
                                 ↑
                            This is your FILE_ID
```

## ⚙️ Step 5: Configure Application

Once you have the FILE_ID, you'll use it in the application configuration.

**Example FILE_ID**: `1ABC123DEF456GHI789JKL`
**Direct Download URL**: `https://drive.google.com/uc?export=download&id=1ABC123DEF456GHI789JKL`

## 🔒 Security Notes

- The Google Drive link will be public but not easily discoverable
- No authentication credentials are stored in the code
- The model file itself contains no sensitive information
- Consider using environment variables for the FILE_ID in production

## ✅ Verification

Test your direct download link by:
1. Opening it in a browser (should start downloading the .pkl file)
2. Verifying the downloaded file size matches the original (561MB)
3. Ensuring the file can be loaded with pickle

## 📋 Next Steps

After completing this setup:
1. Note down your FILE_ID
2. Proceed with the code implementation
3. Test the application locally before deploying to Heroku

---

**⚠️ Important**: Keep your FILE_ID secure and consider using environment variables for production deployment.
