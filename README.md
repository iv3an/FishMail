# FishMail

```text
███████╗██╗███████╗██╗  ██╗███╗   ███╗ █████╗ ██╗██╗
██╔════╝██║██╔════╝██║  ██║████╗ ████║██╔══██╗██║██║
█████╗  ██║███████╗███████║██╔████╔██║███████║██║██║
██╔══╝  ██║╚════██║██╔══██║██║╚██╔╝██║██╔══██║██║██║
██║     ██║███████║██║  ██║██║ ╚═╝ ██║██║  ██║██║███████╗
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  F I S H M A I L     /     EMAIL THREAT ANALYSIS     v0.1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

A beginner Python CLI project by **iwan**, built to start my journey in cybersecurity and learn phishing email analysis .

## Project status

**Work in progress — currently a terminal menu, not a working phishing detector.**

Working now:
- ASCII banner and repeating terminal menu.
- Analyze option that asks for an `.eml` path and displays it.
- About and Exit options, plus invalid menu choice handling.

The analysis module is currently empty. Gmail access, email parsing, reputation checks, and AI analysis are not implemented yet.

## The goal

Build a terminal tool that explains suspicious email indicators, beginning with local `.eml` files and eventually adding optional Gmail access and URL reputation checks.

The tool should show evidence for manual review. A keyword match, an authentication result, or a reputation lookup alone cannot prove whether an email is phishing.

## Run the current version

Use Python 3.10 or newer. No third-party packages are needed for the current menu.

```bash
git clone https://github.com/iv3an/pfish.git
cd pfish
python3 main.py
```

If you already have the repository, open a terminal in its folder and run `python3 main.py`. On Windows outside WSL, use `py main.py`.

## Project structure

```text
pfish/
├── main.py          # Banner, menu, and user input
├── analyser.py      # Future email parsing and analysis functions
├── integrations/    # Future Gmail and reputation service modules
├── samples/         # Fictional test emails and local practice files
├── tests/           # Future automated checks
├── reports/         # Local generated reports (contents ignored by Git)
├── README.md
└── .gitignore
```




