#  Lab 5 – Static Code Analysis  
### Issues Identified and Fixes Applied  
**File analyzed:** `inventory_system.py` (before) → `cleaned_inventory_system.py` (after)

---

| **Issue** | **Tool** | **Type** | **Line(s)** | **Description** | **Fix Approach** | **Status (Old → New)** |
|------------|-----------|-----------|---------------|------------------|------------------|------------------|
| Missing module docstring | Pylint | Convention | 1 | No description or purpose provided at top of file | Added module-level docstring at the beginning of the file | Fixed |
| Non-PEP8 function names (`addItem`, `removeItem`, etc.) | Pylint / Flake8 | Style | 11, 27, 44, 48, 62, 71, 77 | Function names didn’t follow snake_case convention | Renamed to `add_item`, `remove_item`, `get_qty`, etc. | Fixed |
| Logging using f-string interpolation | Pylint | Maintainability | 16–42 | Used f-strings in logging instead of lazy “%” formatting | Replaced with parameterized logging (`logging.info("%s", msg)`) | Fixed |
| No encoding specified in file open() | Bandit / Pylint | Security | 52, 65 | File opened without explicit encoding (unsafe default) | Added `encoding="utf-8"` in all `open()` calls | Fixed |
| Broad exception caught (`except Exception`) | Pylint / Bandit | Security | 68 | Used overly broad `except` block | Replaced with specific `except OSError as error` | Fixed |
| Mutable default argument (`logs=[]`) | Pylint | Bug | 11 | Default list reused across function calls | Changed to `logs=None` and initialized inside function | Fixed |
| Missing function docstrings | Pylint | Documentation | Multiple | Functions lacked docstrings explaining purpose | Added concise PEP 257-compliant docstrings for all functions | Fixed |
| Lines exceeding 79 characters | Flake8 / Pylint | Style | 6, 16, 19, 36, etc. | Several lines exceeded PEP 8 recommended length | Broke or wrapped long lines to improve readability | Partially fixed (few >79 remain) |
| Using `global` statement | Pylint | Convention | 63 | Accessed global variable `stock_data` | Retained (necessary for functionality) but documented clearly | Acceptable |
| Missing blank lines between functions | Flake8 | Style | Multiple | Functions not separated by 2 blank lines | Reformatted file with proper spacing | Fixed |

---

### Summary of Improvements

| **Tool** | **Old Score / Findings** | **New Score / Findings** | **Result** |
|-----------|---------------------------|---------------------------|-------------|
| **Pylint** | 7.08 / 10 | 9.86 / 10 | ↑ Major improvement in readability, structure, and safety |
| **Bandit** | No issues | No issues | Code remains secure and compliant |
| **Flake8** | 14 style violations | 6 minor (E501 line length) | Most formatting issues resolved |

---

###  Key Observations
- Improved **readability** through consistent naming and proper docstrings.  
- Enhanced **security** by adding file encodings and specific exception handling.  
- Increased **maintainability** through cleaner logging and removal of bad practices.  
- Pylint score improved from **7.08 → 9.86**, exceeding the lab target of 8.0+.  
- Bandit confirmed **zero security vulnerabilities** in both old and cleaned versions.  

---

**Prepared by:** _SIRI S ARADHYA[PES1UG23CS906]_  
**Date:** _27 October 2025_  
**Lab:** Static Code Analysis – Pylint, Bandit, and Flake8  
