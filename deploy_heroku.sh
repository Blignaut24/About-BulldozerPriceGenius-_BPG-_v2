#!/bin/bash

# BulldozerPriceGenius Heroku Deployment Script
# Comprehensive deployment preparation and execution

echo "🚀 BulldozerPriceGenius Heroku Deployment"
echo "=========================================="

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Step 1: Pre-deployment checks
echo ""
echo "📋 Step 1: Pre-deployment Checks"
echo "--------------------------------"

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null; then
    print_error "Heroku CLI is not installed"
    echo "Please install it from: https://devcenter.heroku.com/articles/heroku-cli"
    exit 1
fi
print_status "Heroku CLI is installed"

# Check if user is logged in to Heroku
if ! heroku auth:whoami &> /dev/null; then
    print_error "Please log in to Heroku first: heroku login"
    exit 1
fi
print_status "Logged in to Heroku as: $(heroku auth:whoami)"

# Check if git is initialized
if [ ! -d ".git" ]; then
    print_error "Git repository not initialized"
    echo "Please run: git init && git add . && git commit -m 'Initial commit'"
    exit 1
fi
print_status "Git repository is initialized"

# Step 2: Verify deployment files
echo ""
echo "📋 Step 2: Deployment Files Verification"
echo "----------------------------------------"

# Check required files
required_files=("Procfile" "requirements.txt" ".python-version" "setup.sh" "app.py")
for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        print_status "$file exists"
    else
        print_error "$file is missing"
        exit 1
    fi
done

# Check .slugignore
if [ -f ".slugignore" ]; then
    print_status ".slugignore exists (optimizes deployment size)"
else
    print_warning ".slugignore not found (deployment may be larger)"
fi

# Step 3: Get app name
echo ""
echo "📋 Step 3: Heroku App Configuration"
echo "-----------------------------------"

read -p "Enter your Heroku app name (or press Enter to create new): " APP_NAME

if [ -z "$APP_NAME" ]; then
    echo "Creating new Heroku app..."
    APP_NAME=$(heroku create --json | python3 -c "import sys, json; print(json.load(sys.stdin)['name'])")
    print_status "Created new app: $APP_NAME"
else
    # Check if app exists
    if heroku apps:info --app "$APP_NAME" &> /dev/null; then
        print_status "App '$APP_NAME' exists"
    else
        print_error "App '$APP_NAME' does not exist"
        echo "Please create it first: heroku create $APP_NAME"
        exit 1
    fi
fi

# Step 4: Configure environment variables
echo ""
echo "📋 Step 4: Environment Variables Setup"
echo "--------------------------------------"

# Set Google Drive Model ID (must be provided as environment variable)
if [ -z "$GOOGLE_DRIVE_MODEL_ID" ]; then
    print_error "GOOGLE_DRIVE_MODEL_ID environment variable not set"
    echo "Please set it before running this script:"
    echo "export GOOGLE_DRIVE_MODEL_ID=your_file_id_here"
    exit 1
fi
print_info "Setting GOOGLE_DRIVE_MODEL_ID environment variable..."
heroku config:set GOOGLE_DRIVE_MODEL_ID="$GOOGLE_DRIVE_MODEL_ID" --app "$APP_NAME"

if [ $? -eq 0 ]; then
    print_status "Environment variable set successfully"
else
    print_error "Failed to set environment variable"
    exit 1
fi

# Step 5: Set dyno type recommendation
echo ""
echo "📋 Step 5: Dyno Configuration"
echo "-----------------------------"

print_info "Recommended dyno type: Standard-1X (512MB RAM) or higher"
print_info "The 561MB ML model requires sufficient memory"
print_warning "Free dynos (512MB) may experience memory issues"

read -p "Set dyno type to Standard-1X? (y/n): " SET_DYNO
if [[ $SET_DYNO =~ ^[Yy]$ ]]; then
    heroku ps:type Standard-1X --app "$APP_NAME"
    print_status "Dyno type set to Standard-1X"
fi

# Step 6: Deploy to Heroku
echo ""
echo "📋 Step 6: Deployment"
echo "--------------------"

print_info "Committing latest changes..."
git add .
git commit -m "Prepare for Heroku deployment - $(date)"

print_info "Deploying to Heroku..."
git push heroku main

if [ $? -eq 0 ]; then
    print_status "Deployment successful!"
else
    print_error "Deployment failed"
    echo "Check the logs: heroku logs --tail --app $APP_NAME"
    exit 1
fi

# Step 7: Post-deployment verification
echo ""
echo "📋 Step 7: Post-deployment Verification"
echo "---------------------------------------"

print_info "Opening app in browser..."
heroku open --app "$APP_NAME"

print_info "Checking app status..."
heroku ps --app "$APP_NAME"

echo ""
echo "🎉 Deployment Complete!"
echo "======================"
print_status "App URL: https://$APP_NAME.herokuapp.com"
print_status "App Name: $APP_NAME"
print_status "Model File ID: $FILE_ID"

echo ""
echo "📋 Next Steps:"
echo "- Test all 8 test scenarios on the deployed app"
echo "- Monitor logs: heroku logs --tail --app $APP_NAME"
echo "- Check app metrics: heroku addons:create papertrail --app $APP_NAME"

echo ""
print_warning "Important Notes:"
echo "- First load may take 30-60 seconds (model download)"
echo "- Subsequent loads will be faster (model cached)"
echo "- Monitor memory usage with Standard-1X dyno"
