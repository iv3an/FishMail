
from email import policy
from email.parser import BytesParser
from pathlib import Path


def analyze_email(email_path):

    email_file = Path(email_path) #turns text to path
    if not email_file.is_file():
        print("[!] Email file not found. Check the path and try again.")
        return 

    if email_file.suffix.lower() != ".eml":  
        print("[!] Unsupported file type. Please select an .eml email.")
        return

    with email_file.open("rb") as file:
        message = BytesParser(policy=policy.default).parse(file)

    print("From:", message.get("From", "(Missing sender)"))
    print("Subject:", message.get("Subject", "(No subject)"))

    input("\nPress Enter to return to the menu...")

   