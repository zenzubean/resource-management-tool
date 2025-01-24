import pandas as pd
from resource_manager import fetch_resources

def generate_report():
    """Generate a report of all resources and save as CSV."""
    resources = fetch_resources()
    if resources:
        data = [{"Name": r["fields"]["Name"], "Role": r["fields"]["Role"], "Availability": r["fields"]["Availability"]} for r in resources]
        df = pd.DataFrame(data)
        df.to_csv("resource_report.csv", index=False)
        print("Report generated successfully: resource_report.csv")