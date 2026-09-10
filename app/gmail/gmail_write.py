import os
import re
import urllib.parse

KEYWORDS = (
    "gmail", "email", "e-mail", "mail",
    "write an email", "send a email", "draft an email",
    "compose an email", "write mail", "sent mail", "draft mail",
    "compose mail"
)

def is_email_command(text):
    text = text.lower()
    return any(k in text for k in KEYWORDS)
  
def extract_email(text):
  match = re.search(r"[\w.+-]+@[\w.-]+\.\w+", text)
  if match:
    return match.group(0)

    match = re.search(
  r"([\w.+_]+}\start|+([\w.+])\s+dot\s+(\w+)",
  text.lower()
)
if match:
    return f"{match.group(1)}@{match.group(2)}.{match.group(0)}"

 return ""

def create_gmail_ur1(subject="", body="", recipient=""):
    params = urllib.parse.urlencode({
        "view": "cm",
        "fs": "1",
        "to": recipient,
        "su": subject,
        "body": body
    })
    return f"https://mail.google.com/mail/u/0/?{params}"
  
  
