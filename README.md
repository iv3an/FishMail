# FishMail

```text
F I S H M A I L
Inspect the email. Understand the warning signs.
```

A beginner Python CLI project by **iwan**, built to start my journey in cybersecurity and learn phishing email analysis one feature at a time.

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

These folders are preparation for later lessons, not implemented features. We will add Python modules only when we build the corresponding feature.

## Build roadmap

- [x] Create the banner and menu.
- [x] Ask the user for an email file path.
- [ ] Validate that the path points to an `.eml` file.
- [ ] Parse a local email and display From, Reply-To, and Subject.
- [ ] Extract body text and links without opening links.
- [ ] Explain suspicious wording and sender/reply domain differences.
- [ ] Add tests using fictional emails.
- [ ] Save an analysis report.
- [ ] Add optional Gmail sign-in and read-only message retrieval.
- [ ] Let the user choose a date range for Gmail messages.
- [ ] Add optional VirusTotal reputation lookups with clear limitations.
- [ ] Explore optional AI explanations after the basic analysis works.

Marking spam or managing sender filters is a possible later extension requiring separate permissions and explicit user confirmation. It is not part of the initial version.

## Learning goals

Practice functions, conditions, loops, file paths, exception handling, email parsing, and eventually API requests and authentication. Build each part in small steps so I can understand and explain the code.

## Email data and API keys

Use fictional messages while learning. Real emails, reports, OAuth credentials, tokens, and API keys should stay out of the repository. The `.gitignore` includes common private-file patterns; it does not remove files already tracked by Git.

Future external integrations may send email content, URLs, or other indicators to a provider. That behavior should be explicit and optional. Keep credentials outside Python source files.

## Inspiration

Inspired by [PhishSentinel](https://github.com/cyb2rS2c/PhishSentinel) and its Gmail phishing-analysis workflow. FishMail is my own learning project, built step by step rather than a copy of its implementation.
