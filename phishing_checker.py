
import re
from urllib.parse import urlparse

def inspect_url(raw_url):
    """Check visible URL text for selected warning signs."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url
    parsed = urlparse(candidate)
    host = (parsed.hostname or "").lower()

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings


def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    while True:
        raw_url = input(
            "\nEnter a sample URL to inspect (or type 'quit' to exit): "
        )

        if raw_url.strip().lower() == "quit":
            print("Thank you for using the checker!")
            break

        findings = inspect_url(raw_url)

        print("\nResult:")
        for item in findings:
            print("- " + item)

        if findings == [
            "No listed warning signs found. This does NOT prove safety."
        ]:
            print("Summary: No listed warning signs found.")
        elif findings == ["No URL entered."]:
            print("Summary: Please enter a URL.")
        elif findings == ["Could not identify a hostname."]:
            print("Summary: Please check the URL format.")
        else:
            print("Summary: Review carefully; warning signs were found.")

        print("Never enter passwords from unexpected links.")

if __name__ == "__main__":
    main()

