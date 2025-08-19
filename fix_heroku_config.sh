#!/bin/bash

# Fix Heroku Configuration Script for BulldozerPriceGenius
# Sets the Google Drive model file ID environment variable

echo "🔧 Fixing Heroku Configuration for BulldozerPriceGenius"
echo "=" * 60

# Your Google Drive file ID
FILE_ID="1mSIR9TnJvP4zpVHlrsMGm11WS-DWyyTp"

echo "📋 Configuration Details:"
echo "   Google Drive File ID: $FILE_ID"
echo "   Environment Variable: GOOGLE_DRIVE_MODEL_ID"
echo ""

# Check if Heroku CLI is available
if ! command -v heroku &> /dev/null; then
    echo "❌ Heroku CLI is not installed."
    echo "   Please install it from: https://devcenter.heroku.com/articles/heroku-cli"
    echo ""
    echo "📋 Manual Setup Instructions:"
    echo "   1. Go to your Heroku Dashboard: https://dashboard.heroku.com"
    echo "   2. Select your BulldozerPriceGenius app"
    echo "   3. Go to Settings tab"
    echo "   4. Click 'Reveal Config Vars'"
    echo "   5. Add new config var:"
    echo "      KEY: GOOGLE_DRIVE_MODEL_ID"
    echo "      VALUE: $FILE_ID"
    echo "   6. Click 'Add'"
    echo "   7. Restart your app from the 'More' menu"
    exit 1
fi

# Check if user is logged in
if ! heroku auth:whoami &> /dev/null; then
    echo "❌ Not logged in to Heroku."
    echo "   Please run: heroku login"
    exit 1
fi

# Get app name
echo "🔍 Detecting Heroku app..."

# Try to get app name from git remote
APP_NAME=""
if git remote get-url heroku &> /dev/null; then
    HEROKU_URL=$(git remote get-url heroku)
    APP_NAME=$(basename "$HEROKU_URL" .git)
    echo "✅ Detected app from git remote: $APP_NAME"
else
    echo "⚠️  Could not detect app from git remote."
    read -p "Enter your Heroku app name: " APP_NAME
fi

if [ -z "$APP_NAME" ]; then
    echo "❌ App name is required"
    exit 1
fi

echo ""
echo "🔧 Setting environment variable for app: $APP_NAME"

# Set the environment variable
heroku config:set GOOGLE_DRIVE_MODEL_ID="$FILE_ID" --app "$APP_NAME"

if [ $? -eq 0 ]; then
    echo "✅ Environment variable set successfully!"
    
    echo ""
    echo "🔍 Verifying configuration..."
    heroku config:get GOOGLE_DRIVE_MODEL_ID --app "$APP_NAME"
    
    echo ""
    echo "📋 Current configuration:"
    heroku config --app "$APP_NAME"
    
    echo ""
    echo "🔄 Restarting app to apply changes..."
    heroku restart --app "$APP_NAME"
    
    echo ""
    echo "✅ Configuration fix completed!"
    echo ""
    echo "📋 Next Steps:"
    echo "   1. Wait 30-60 seconds for app to restart"
    echo "   2. Open your app: heroku open --app $APP_NAME"
    echo "   3. Navigate to the Interactive Prediction page"
    echo "   4. You should see: '🌐 Loading ML model from external storage...'"
    echo "   5. Monitor logs: heroku logs --tail --app $APP_NAME"
    
else
    echo "❌ Failed to set environment variable"
    echo "   Please try manual setup via Heroku Dashboard"
    exit 1
fi
