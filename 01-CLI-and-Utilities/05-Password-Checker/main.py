import re
import hashlib
import requests
from rich.console import Console
from rich.panel import Panel

console = Console()

def check_strength(password: str):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("At least 8 characters long")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("At least one uppercase letter (A-Z)")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("At least one lowercase letter (a-z)")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("At least one digit (0-9)")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("At least one special character (!@#$...)")

    return score, feedback

def check_pwned_api(password: str):
    # k-Anonymity model: Only send first 5 chars of SHA1 hash for privacy
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_chars, tail = sha1password[:5], sha1password[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{first5_chars}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            hashes = (line.split(':') for line in response.text.splitlines())
            for h, count in hashes:
                if h == tail:
                    return int(count)
    except Exception:
        pass
    return 0

if __name__ == "__main__":
    console.print(Panel.fit("[bold cyan]🔒 Password Strength & Data Leak Checker[/]"))
    user_pass = input("\nEnter password to test: ").strip()

    if user_pass:
        score, feedback = check_strength(user_pass)
        leaks = check_pwned_api(user_pass)

        console.print(f"\n[bold]Strength Score:[/] {score}/5")
        
        if score == 5:
            console.print("[bold green]Status: Strong Password! ✅[/]")
        else:
            console.print("[bold yellow]Status: Weak Password ⚠️[/]")
            for f in feedback:
                console.print(f"  • {f}")

        if leaks > 0:
            console.print(f"\n[bold red]⚠️ ALERT: This password was found in {leaks:,} known data breaches![/]")
        else:
            console.print("\n[bold green]🛡️ Safe: No breach history found for this password.[/]")