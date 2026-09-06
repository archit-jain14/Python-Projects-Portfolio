# 🔒 CLI Password Strength & Data Leak Checker

A lightweight Python command-line utility designed to evaluate password security and verify whether a credential has appeared in known data breaches.

This tool utilizes the **HaveIBeenPwned API** using a privacy-focused **k-Anonymity** model, ensuring that raw passwords or full hashes are never transmitted over the internet.

---

## ✨ Features

* **Complexity Analysis:** Uses Regular Expressions (`re`) to test for essential complexity criteria (length, uppercase, lowercase, numbers, and special characters).
* **Privacy-Preserving Leak Check:** Computes local SHA-1 hashes and sends only the first 5 characters to the API.
* **Hash Verification:** Local comparison against returned hash tails to detect exact breach counts.
* **Rich Terminal UI:** Clear status warnings, criteria checklists, and visual breach alerts powered by `rich`.

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.x
* **Libraries:**
  * `requests` (for HTTP API interaction)
  * `rich` (for CLI visual formatting)
  * `hashlib` (built-in SHA-1 hash computation)
  * `re` (built-in regex validation)

---

## 🚀 How It Works (Security & Privacy)

1. The script takes user input and checks it against 5 password strength rules locally.
2. It generates a **SHA-1 hash** of the entered password (e.g., `5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8`).
3. It splits the hash:
   * **Prefix (First 5 chars):** `5BAA6` -> Sent to `api.pwnedpasswords.com`
   * **Suffix (Remaining chars):** `1E4C9B93F3F0682250B6CF8331B7EE68FD8` -> Kept local
4. The API returns thousands of hash suffixes that share the same prefix.
5. The script matches the suffix locally to see if it exists in data breaches.

---

## 💻 How to Run Locally

1. **Navigate to the project folder:**
   ```bash
   cd 01-CLI-and-Utilities/05-Password-Checker
