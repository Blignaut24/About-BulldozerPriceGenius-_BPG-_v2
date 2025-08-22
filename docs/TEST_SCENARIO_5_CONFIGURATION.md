# Test Scenario 5: Small Contractor Regional Market Configuration

## 🎯 **Test Purpose**
Tests regional market adjustments and smaller equipment pricing accuracy.

## 📋 **Required Configuration**

### **Basic Information**
- **Year Made:** 2003
- **Product Size:** Small
- **State:** Vermont

### **Detailed Specifications**
- **Model ID:** 3100
- **Enclosure:** OROPS
- **Base Model:** D5
- **Coupler System:** Manual
- **Tire Size:** **20.5R25** ← **FIXED: Now available in dropdown**
- **Hydraulics Flow:** Standard
- **Grouser Tracks:** Double
- **Hydraulics:** Standard (default)

### **Sale Information**
- **Sale Year:** 2007
- **Sale Day of Year:** 60

## ✅ **Verification Steps**

### **Step 1: Navigate to Interactive Prediction**
1. Open BulldozerPriceGenius application
2. Go to "Page 4: Interactive Prediction"

### **Step 2: Configure Basic Information**
1. Set **Year Made:** 2003
2. Select **Product Size:** Small
3. Select **State:** Vermont

### **Step 3: Configure Detailed Specifications**
1. Set **Model ID:** 3100
2. Select **Enclosure:** OROPS
3. Select **Base Model:** D5
4. Select **Coupler System:** Manual
5. **VERIFY:** Select **Tire Size:** 20.5R25 (should now be available)
6. Select **Hydraulics Flow:** Standard
7. Select **Grouser Tracks:** Double

### **Step 4: Configure Sale Information**
1. Set **Sale Year:** 2007
2. Set **Sale Day of Year:** 60

### **Step 5: Execute Prediction**
1. Click "🤖 Get ML Prediction"
2. Verify prediction completes successfully
3. Check that tire size "20.5R25" is properly processed

## 🔧 **Fix Applied**

### **Issue Resolved**
- **Problem:** "20.5R25" tire size was missing from dropdown options
- **Location:** `app_pages/four_interactive_prediction.py`
- **Fix:** Added "20.5R25" to both:
  1. Dropdown options list (line 405)
  2. Feature mappings dictionary (lines 1148-1151)

### **Changes Made**

**Before:**
```python
'Tire_Size': ['None or Unspecified', '16.9R24', '23.5', '26.5', '29.5', '35/65-33', '750/65R25']
```

**After:**
```python
'Tire_Size': ['None or Unspecified', '16.9R24', '20.5R25', '23.5', '26.5', '29.5', '35/65-33', '750/65R25']
```

**Feature Mapping Updated:**
```python
'Tire_Size': {
    'None or Unspecified': 0, '16.9R24': 1, '20.5R25': 2, '23.5': 3, 
    '26.5': 4, '29.5': 5, '35/65-33': 6, '750/65R25': 7
}
```

## ✅ **Expected Results**

### **Dropdown Verification**
- ✅ "20.5R25" appears in Tire Size dropdown
- ✅ "20.5R25" can be selected without errors
- ✅ Selection is properly encoded for ML model

### **Prediction Functionality**
- ✅ Test Scenario 5 configuration can be completed
- ✅ ML prediction processes tire size correctly
- ✅ No encoding errors or missing value warnings

### **Test Scenario 5 Readiness**
- ✅ All required configuration options now available
- ✅ Test can be executed as documented in TEST.md
- ✅ Regional market adjustments can be properly tested

## 🚀 **Next Steps**

1. **Execute Test Scenario 5** using the configuration above
2. **Document results** in TEST.md if successful
3. **Verify regional market adjustments** for Vermont small equipment
4. **Compare results** against expected criteria for small contractor equipment

**Test Scenario 5 is now ready for execution with the missing "20.5R25" tire size option available in the dropdown.**
