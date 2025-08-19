#!/bin/bash

# Heroku Environment Setup Script for BulldozerPriceGenius
# This script sets up the necessary environment variables for external model storage

echo "🚀 Setting up Heroku environment for BulldozerPriceGenius..."

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null; then
    echo "❌ Heroku CLI is not installed. Please install it first:"
    echo "   https://devcenter.heroku.com/articles/heroku-cli"
    exit 1
fi

# Check if user is logged in to Heroku
if ! heroku auth:whoami &> /dev/null; then
    echo "❌ Please log in to Heroku first:"
    echo "   heroku login"
    exit 1
fi

# Get the app name
read -p "Enter your Heroku app name: " APP_NAME

if [ -z "$APP_NAME" ]; then
    echo "❌ App name cannot be empty"
    exit 1
fi

# Get the Google Drive file ID
echo ""
echo "📁 Google Drive Model Configuration"
echo "Please provide your Google Drive file ID for the ML model."
echo "This should be extracted from your Google Drive share link."
echo ""
echo "Example: If your link is:"
echo "https://drive.google.com/file/d/1ABC123DEF456GHI789JKL/view?usp=sharing"
echo "Then your file ID is: 1ABC123DEF456GHI789JKL"
echo ""

read -p "Enter your Google Drive file ID: " FILE_ID

if [ -z "$FILE_ID" ]; then
    echo "❌ File ID cannot be empty"
    exit 1
fi

# Set the environment variable
echo "🔧 Setting GOOGLE_DRIVE_MODEL_ID environment variable..."
heroku config:set GOOGLE_DRIVE_MODEL_ID="$FILE_ID" --app "$APP_NAME"

if [ $? -eq 0 ]; then
    echo "✅ Environment variable set successfully!"
    echo ""
    echo "📋 Configuration Summary:"
    echo "   App Name: $APP_NAME"
    echo "   Google Drive File ID: $FILE_ID"
    echo "   Direct Download URL: https://drive.google.com/uc?export=download&id=$FILE_ID"
    echo ""
    echo "🚀 Your app is now configured for external model storage!"
    echo "   You can deploy with: git push heroku main"
else
    echo "❌ Failed to set environment variable"
    exit 1
fi
