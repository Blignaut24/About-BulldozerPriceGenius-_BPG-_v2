#!/bin/bash

# BulldozerPriceGenius Heroku Deployment Script
# This script helps deploy the application to Heroku with proper error checking

echo "🚀 BulldozerPriceGenius Heroku Deployment Script"
echo "================================================"

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null; then
    echo "❌ Heroku CLI is not installed. Please install it first."
    echo "   Visit: https://devcenter.heroku.com/articles/heroku-cli"
    exit 1
fi

# Check if user is logged in to Heroku
if ! heroku auth:whoami &> /dev/null; then
    echo "❌ Not logged in to Heroku. Please run 'heroku login' first."
    exit 1
fi

echo "✅ Heroku CLI is installed and you are logged in."

# Get app name
read -p "Enter your Heroku app name: " APP_NAME

if [ -z "$APP_NAME" ]; then
    echo "❌ App name cannot be empty."
    exit 1
fi

echo "📋 Checking app status..."
if heroku apps:info --app $APP_NAME &> /dev/null; then
    echo "✅ App '$APP_NAME' exists."
else
    echo "❌ App '$APP_NAME' does not exist. Please create it first:"
    echo "   heroku create $APP_NAME"
    exit 1
fi

# Pre-deployment checks
echo "🔍 Running pre-deployment checks..."

# Check if all required files exist
REQUIRED_FILES=("app.py" "requirements.txt" "Procfile" "setup.sh" "runtime.txt")
for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file exists"
    else
        echo "❌ $file is missing"
        exit 1
    fi
done

# Check if git repo is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not initialized. Please run 'git init' first."
    exit 1
fi

# Check if there are uncommitted changes
if ! git diff-index --quiet HEAD --; then
    echo "⚠️  You have uncommitted changes. Committing them now..."
    git add .
    git commit -m "fix: prepare for Heroku deployment with error handling and optimizations"
fi

# Set Heroku remote if not exists
if ! git remote get-url heroku &> /dev/null; then
    echo "🔗 Adding Heroku remote..."
    heroku git:remote --app $APP_NAME
fi

# Deploy to Heroku
echo "🚀 Deploying to Heroku..."
git push heroku main

# Check deployment status
echo "📊 Checking deployment status..."
sleep 5

# Show logs
echo "📋 Recent logs:"
heroku logs --lines 50 --app $APP_NAME

# Check if app is running
echo "🔍 Checking dyno status..."
heroku ps --app $APP_NAME

# Test the app
echo "🧪 Testing the deployed app..."
APP_URL="https://$APP_NAME.herokuapp.com"
echo "App URL: $APP_URL"

# Check if app responds
if curl -s --head $APP_URL | head -n 1 | grep -q "200 OK"; then
    echo "✅ App is responding successfully!"
    echo "🎉 Deployment completed successfully!"
    echo "📱 You can access your app at: $APP_URL"
else
    echo "❌ App is not responding. Checking logs for errors..."
    heroku logs --lines 100 --app $APP_NAME
    echo ""
    echo "🔧 Common fixes to try:"
    echo "1. Check the logs above for specific error messages"
    echo "2. Verify all dependencies are compatible with Heroku"
    echo "3. Ensure the app binds to the correct port (\$PORT)"
    echo "4. Check for memory limit issues"
    echo ""
    echo "📞 For detailed troubleshooting, run:"
    echo "   heroku logs --tail --app $APP_NAME"
fi

echo ""
echo "🛠️  Useful Heroku commands:"
echo "   heroku logs --tail --app $APP_NAME    # View real-time logs"
echo "   heroku restart --app $APP_NAME        # Restart the app"
echo "   heroku ps --app $APP_NAME             # Check dyno status"
echo "   heroku config --app $APP_NAME         # View config variables"
