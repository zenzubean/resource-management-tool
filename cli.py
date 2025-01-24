import sys
from resource_manager import fetch_resources
from report_generator import generate_report

def main():
    print("Resource Management Tool")
    print("1. View Resources")
    print("2. Generate Report")
    choice = input("Enter your choice: ")

    if choice == "1":
        resources = fetch_resources()
        if resources:
            for r in resources:
                print(f"Name: {r['fields']['Name']}, Role: {r['fields']['Role']}, Availability: {r['fields']['Availability']}")
    elif choice == "2":
        generate_report()
        print("Report created successfully.")