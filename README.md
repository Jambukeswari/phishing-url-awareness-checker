
# Phishing URL Awareness Checker

## Overview
This is a simple Python command-line tool that checks visible URL text for selected phishing warning signs.

## Features
- Checks for an @ symbol.
- Checks whether the URL is longer than 100 characters.
- Detects an IP address used as the hostname.
- Checks for many hostname segments.
- Detects punycode-style hostnames.
- Warns when HTTP is used instead of HTTPS.

## Improvements
- Allows users to check multiple URLs without restarting the program.
- Displays a clear summary when warning signs are found.
- Provides helpful messages for empty or invalid URL input.

## Requirements
Python 3 is required. No additional packages are needed.

## How to Run
Run the following command in the project folder:

python phishing_checker.py

Enter a sample URL when prompted.

## Testing
Five sample URL test cases are documented in tests/test_samples.md.

## Screenshots
- screenshots/sample_run.jpeg
- screenshots/test_results.jpeg
- screenshots/improvements.jpeg

### Python Program Code
- screenshots/program_code1.jpeg
- screenshots/program_code2.jpeg
- screenshots/program_code3.jpeg
- screenshots/program_code4.jpeg

## Limitations
This tool checks URL text only. It does not open URLs, scan websites, or make internet requests. No warnings does not prove that a URL is safe.

## Ethical Use
Use this tool for learning and cybersecurity awareness. Never enter passwords on unexpected links.