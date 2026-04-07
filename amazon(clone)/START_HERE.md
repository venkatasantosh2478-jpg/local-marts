# 🚀 START YOUR AMAZON CLONE - 3 EASY WAYS

## ✨ CHOOSE YOUR METHOD:

---

## **METHOD 1: Windows Users (Easiest!) ⭐**

### Double-click one of these files:

📁 `START.bat` ← **RECOMMENDED** (Auto-installs everything)
```
This will:
✓ Check Python installed
✓ Install packages
✓ Create database
✓ Start server
✓ Open browser (manual step)
```

OR

📁 `RUN.bat` (Quick start if already setup)

---

## **METHOD 2: Command Line (All Platforms)**

```bash
# Step 1: Open Terminal/PowerShell in amazon(clone) folder

# Step 2: Install packages (first time only)
pip install -r requirements.txt

# Step 3: Run the app
python start.py
```

---

## **METHOD 3: Mac/Linux**

```bash
# Step 1: Open Terminal in amazon(clone) folder

# Step 2: Install packages (first time only)  
pip install -r requirements.txt

# Step 3: Run the app
python3 start.py

# OR use the shell script
bash start.sh
```

---

## 🌐 THEN OPEN YOUR BROWSER:

Go to: **http://localhost:5000**

---

## 🔐 LOGIN CREDENTIALS:

| Account | Username | Password |
|---------|----------|----------|
| Admin | `admin` | `admin123` |
| User | `testuser` | `test123` |

---

## 🆘 IF FIRST TIME SETUP:

Run this **once** to create sample data:
```bash
python seed.py
```

---

## ⚡ QUICK HELP

| Problem | Solution |
|---------|----------|
| Python not found | Download from https://www.python.org |
| Package errors | Run: `pip install -r requirements.txt` |
| Port already in use | Close other terminals OR use port 5001 |
| Database issues | Delete `app/amazon_clone.db` and run `python seed.py` |

---

## ✅ THAT'S IT!

Your Amazon Clone is running! 🎉
