import json
import os
from datetime import datetime, timedelta
from fastapi import HTTPException


# Upload CVEs from file
def load_cve_data():
    if not os.path.exists("./exploits.json"):
        raise HTTPException(status_code=404, detail="File not found")

    with open("./exploits.json", "r") as file:
        return json.load(file)


# Filter CVE
# changed days to 10, because 5 is not enough to see the output
def get_recent_cve(cve_data, days: int = 10, limit: int = 40):
    five_days_ago = datetime.now() - timedelta(days=days)
    recent_cve = []

    for cve in cve_data['vulnerabilities']:
        cve_date = datetime.strptime(cve['dateAdded'], "%Y-%m-%d")
        if cve_date >= five_days_ago:
            recent_cve.append(cve)
        if len(recent_cve) >= limit:
            break

    return recent_cve


def get_new_cve(cve_data, limit: int = 10):
    return sorted(cve_data['vulnerabilities'], key=lambda x: x['dateAdded'], reverse=True)[:limit]


def get_known_ransomware_cve(cve_data):
    return [
        cve for cve in cve_data['vulnerabilities'] if cve.get('knownRansomwareCampaignUse') == 'Known'
    ]
