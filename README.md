<!-- =============================== -->
#  P.E.S. University  
## Department of Computer Science and Engineering  
### Software Engineering Laboratory  
### **Lab 5 – Static Code Analysis Report**
<!-- =============================== -->

---

###  Student Information
**Name:** [SIRI S ARADHYA]  
**SRN:** [PES1UG23CS906]  
**Section:** [L]  
**Date:** 27 October 2025  
**Course Title:** Software Engineering Lab  
**Lab Topic:** Static Code Analysis using Pylint, Bandit, and Flake8  

---

##  Objective
To identify and fix coding, style, and security issues in `inventory_system.py` using Python static analysis tools, and to improve the code’s Pylint score above 8.0.

---

## Tools Used
- **Pylint** – Detects logical errors and poor coding practices  
- **Bandit** – Identifies potential security vulnerabilities in Python code  
- **Flake8** – Ensures compliance with PEP 8 coding and formatting standards  

---

##  Summary of Work Done
Static analysis tools were used to examine and refactor the given Python program `inventory_system.py`.  
Common issues such as missing docstrings, inconsistent naming conventions, unsafe logging, and missing file encoding specifications were detected and corrected.  

The refactored version now:
- Follows **PEP 8** standards  
- Uses **UTF-8 encoding** for all file operations  
- Includes **docstrings** and **consistent naming**  
- Handles exceptions securely and logs operations properly  

After applying fixes:
- The **Pylint score improved from 7.08 → 9.86**  
- **Bandit** detected **no security vulnerabilities**  
- **Flake8** reported only minor line-length warnings  

---

##  Final Results

| Tool | Old Result | New Result | Improvement |
|------|-------------|-------------|--------------|
| **Pylint** | 7.08 / 10 | **9.86 / 10** |  Major improvement in readability and safety |
| **Bandit** | No issues | No issues |  Secure and compliant |
| **Flake8** | 14 style violations | 6 minor (E501) |  Most style issues resolved |

---

##  Key Fixes Applied
- Added **module and function docstrings**  
- Renamed functions to **snake_case** (PEP 8 compliant)  
- Removed **mutable default arguments** (`logs=[] → None`)  
- Added **UTF-8 encoding** in `open()` calls  
- Replaced **bare exceptions** with specific `OSError`  
- Implemented **parameterized logging** instead of f-strings  
- Improved code formatting and spacing for clarity  

---

##  Deliverables Submitted
1. `cleaned_inventory_system.py` – Final refactored and PEP 8–compliant code  
2. `issues_fixes_table.md` – Detailed record of identified issues and applied fixes  
3. `reflection.md` – Reflection on findings and learning outcomes  
4. `README.md` – Summary of workflow and results  

---

##  Commands Used
```bash
# Analyze original code
pylint inventory_system.py > pylint_report_old.txt
flake8 inventory_system.py > flake8_report_old.txt
bandit -r inventory_system.py > bandit_report_old.txt

# Analyze cleaned version
pylint cleaned_inventory_system.py > pylint_report_new.txt
flake8 cleaned_inventory_system.py > flake8_report_new.txt
bandit -r cleaned_inventory_system.py > bandit_report_new.txt
