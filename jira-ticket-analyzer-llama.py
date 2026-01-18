import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

# Jira config
JIRA_DOMAIN = "https://jnvtestworkspace.atlassian.net"
TICKET_KEY = "TW-1"
JIRA_API_URL = f"{JIRA_DOMAIN}/rest/api/3/issue/{TICKET_KEY}"

# Fetch Jira ticket description
def fetch_jira_ticket_description():
    response = requests.get(
        JIRA_API_URL,
        auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
        headers={"Accept": "application/json"},
    )
    if response.status_code == 200:
        data = response.json()
        description = data["fields"].get("description")
        if isinstance(description, dict):
            # Jira Cloud often uses Atlassian Document Format (ADF), so extract plain text recursively
            return extract_plain_text_from_adf(description)
        return description or ""
    else:
        raise Exception(f"Failed to fetch ticket: {response.status_code} {response.text}")

# Helper function to extract plain text from ADF format
def extract_plain_text_from_adf(adf_node):
    text = ""
    if isinstance(adf_node, dict):
        if adf_node.get("type") == "text":
            return adf_node.get("text", "")
        for child in adf_node.get("content", []):
            text += extract_plain_text_from_adf(child)
    elif isinstance(adf_node, list):
        for item in adf_node:
            text += extract_plain_text_from_adf(item)
    return text

# Summarize ticket text using Ollama
def summarize_ticket_text(ticket_text):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",
        "prompt": (
            "You are an expert customer support agent. "
            "Summarize the following Jira ticket description into one clear sentence:\n\n"
            f"{ticket_text}"
        ),
        "stream": False
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()
    return data.get("response", "").strip()

# Main function
def main():
    if not JIRA_EMAIL or not JIRA_API_TOKEN:
        print("Please set environment variables: JIRA_EMAIL, JIRA_API_TOKEN")
        return

    try:
        print(f"Fetching ticket {TICKET_KEY} description from Jira...")
        ticket_description = fetch_jira_ticket_description()
        print("Ticket description fetched:")
        print(ticket_description[:300] + "..." if len(ticket_description) > 300 else ticket_description)

        print("Summarizing ticket with Ollama...")
        summary = summarize_ticket_text(ticket_description)
        print("Summary:")
        print(summary)

        with open("ticket_summary.txt", "w", encoding="utf-8") as f:
            f.write(summary)

        print("Summary saved to ticket_summary.txt")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
