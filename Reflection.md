#  Lab 5 – Reflection on Static Code Analysis

**File analyzed:** `inventory_system.py` → `cleaned_inventory_system.py`  
**Tools used:** Pylint, Bandit, and Flake8  
**Date:** 27 October 2025  
**Author:** SIRI S ARADHYA[PES1UG23CS906]

---

##  1. Which issues were easiest and hardest to fix?

The easiest issues to fix were the **naming conventions** and **missing docstrings**.  
Renaming functions to `snake_case` and adding proper documentation instantly improved readability and removed multiple Pylint/Flake8 warnings.

The hardest issue was understanding **Bandit’s recommendations** and **the “global” statement warning**.  
While Pylint discouraged using `global`, it was required for modifying `stock_data` within functions, so it was left intentionally with proper documentation.

---

##  2. Did any static analysis tools report false positives?

Yes — the `global-statement (W0603)` warning from Pylint can be considered a **false positive** in this context because using `global stock_data` was necessary to modify the shared inventory dictionary.  
Apart from that, all warnings were valid and useful for improving the code.

---

##  3. How would you integrate static analysis tools in real development?

In a real-world software workflow:
- **Pylint**, **Bandit**, and **Flake8** can be integrated into **GitHub Actions** or **CI/CD pipelines**.  
- They can automatically analyze each pull request and reject merges if the score falls below a set threshold (e.g., Pylint < 8.0).  
- Developers can also add **pre-commit hooks** that run these tools before code is committed, ensuring quality from the start.

This ensures consistent style, better security, and fewer runtime bugs.

---

##  4. What improvements were observed after applying the fixes?

| **Aspect** | **Before (Old File)** | **After (Cleaned File)** |
|-------------|------------------------|---------------------------|
| **Pylint Score** | 7.08 / 10 | **9.86 / 10** |
| **Bandit Issues** | 0 (no issues) | 0 (no issues) |
| **Flake8 Violations** | 14 | 6 minor (E501 only) |
| **Readability** | Inconsistent and undocumented | Fully documented and PEP 8 compliant |
| **Logging** | Used f-strings (unsafe practice) | Parameterized, secure logging |
| **Security** | Bare `except:` and no encoding | Specific exception + UTF-8 encoding |

Overall, the cleaned version is **more maintainable, secure, and professional**.

---

##  5. Summary Reflection

Performing static analysis helped me clearly see the **value of automated code review**.  
It taught me how even small style and logging improvements can greatly increase readability and maintainability.  
After applying the fixes, the code now follows PEP 8 standards, is free of high-risk security warnings, and has a consistent structure suitable for production.

---

**Final Pylint Score:**  **9.86 / 10**  
**Final Verdict:** Code quality significantly improved — meets all lab requirements.
