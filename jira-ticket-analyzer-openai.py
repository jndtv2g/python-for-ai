import os
import requests
from requests.auth import HTTPBasicAuth
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

# Jira config
JIRA_DOMAIN = "https://jnvtestworkspace.atlassian.net"
TICKET_KEY = "TW-1"
JIRA_API_URL = f"{JIRA_DOMAIN}/rest/api/3/issue/{TICKET_KEY}"

# Your Jira credentials (replace with your actual email and API token or read from environment variables)
JIRA_EMAIL = os.getenv("JIRA_EMAIL")  # Set this in your environment variables
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")  # Set this in your environment variables

# OpenAI config
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Fetch Jira ticket description
def fetch_jira_ticket_description():
    response = requests.get(
        JIRA_API_URL,
        auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
        headers={"Accept": "application/json"},
    )
    if response.status_code == 200:
        data = response.json()
        # Description may be None or complex rich text; this gets plain text if possible
        description = data["fields"].get("description")
        if isinstance(description, dict):
            # Jira Cloud often uses Atlassian Document Format (ADF), so extract plain text recursively
            return extract_plain_text_from_adf(description)
        return description or ""
    else:
        raise Exception(f"Failed to fetch ticket: {response.status_code} {response.text}")

# Helper function to extract plain text from ADF format
def extract_plain_text_from_adf(adf_node):
    # Recursively extract plain text from Atlassian Document Format JSON
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

# Summarize ticket text using OpenAI
def summarize_ticket_text(ticket_text, client):
    prompt = (
        "You are an expert customer support agent. "
        "Summarize the following Jira ticket description into one clear sentence:\n\n"
        f"{ticket_text}"
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=60,
    )
    return response.choices[0].message.content.strip()

# Main function
def main():
    # Check for required environment variables
    if not JIRA_EMAIL or not JIRA_API_TOKEN or not OPENAI_API_KEY:
        print("Please set environment variables: JIRA_EMAIL, JIRA_API_TOKEN, OPENAI_API_KEY")
        return

    # Fetch ticket description and summarize
    try:
        print(f"Fetching ticket {TICKET_KEY} description from Jira...")
        ticket_description = fetch_jira_ticket_description()
        print("Ticket description fetched:")
        print(ticket_description[:300] + "..." if len(ticket_description) > 300 else ticket_description)

        client = OpenAI(api_key=OPENAI_API_KEY)

        print("Summarizing ticket with OpenAI...")
        summary = summarize_ticket_text(ticket_description, client)
        print("Summary:")
        print(summary)

        with open("ticket_summary.txt", "w", encoding="utf-8") as f:
            f.write(summary)

        print("Summary saved to ticket_summary.txt")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
