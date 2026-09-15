import random

banner=r"""

███████╗██╗███████╗██╗  ██╗███╗   ███╗ █████╗ ██╗██╗
██╔════╝██║██╔════╝██║  ██║████╗ ████║██╔══██╗██║██║
█████╗  ██║███████╗███████║██╔████╔██║███████║██║██║
██╔══╝  ██║╚════██║██╔══██║██║╚██╔╝██║██╔══██║██║██║
██║     ██║███████║██║  ██║██║ ╚═╝ ██║██║  ██║██║███████╗
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  F I S H M A I L     /     EMAIL THREAT ANALYSIS     v0.1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""





#main menu prints 
print(banner)
while True:

    print("""
        [1] Analyze an email
        [2] About
        [0] Exit
    """)
    choice=input('> ').strip()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    if choice == "1":
        email_path = input("\n[ FishMail ] Enter the path to your .eml file\n> ").strip()
        print(email_path)

    elif choice == "2":
        print("""
    ── ABOUT FISHMAIL ──
    Created by iwan.
    A simple project to start my journey in cybersecurity
    and learn Python through phishing email analysis.
         """)
        

    elif choice == "0":
        print("\n    [ Goodbye from FishMail — don't take the bait. ]\n")
        break

    else:
        print("Invalid option. Choose 1, 2, or 0.")



