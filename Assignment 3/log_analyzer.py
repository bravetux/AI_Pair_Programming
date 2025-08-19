# log_analyzer.py

import sys
import csv
import os
from collections import Counter
import kagglehub

def analyze_log(log_file_path):
    """
    Reads a server log file and counts the number of requests per IP address.

    This function assumes a common log format where the IP address is the
    first element on each line.

    Args:
        log_file_path (str): The path to the log file.

    Returns:
        collections.Counter: An object containing IP addresses as keys and
                             their request counts as values. Returns None on error.
    """
    try:
        # Open the log file for reading
        with open(log_file_path, 'r') as f:
            # Use a generator expression for memory-efficient processing
            # The generator expression reads each line of the log file
            # and extracts the first element (IP address) from each line.
            # The if statement filters out empty lines.
            ip_addresses = (line.split()[0] for line in f if line.strip())
            # Return a Counter object that counts the occurrences of each IP address
            return Counter(ip_addresses)
    except FileNotFoundError:
        # If the log file is not found, print an error message and return None
        print(f"❌ Error: The file '{log_file_path}' was not found.")
        return None
    except IndexError:
        # If a line in the log file appears to be malformed, print an error message and return None
        print(f"❌ Error: A line in the log file appears to be malformed. Halting.")
        return None
    except Exception as e:
        # If any other unexpected error occurs, print an error message and return None
        print(f"An unexpected error occurred: {e}")
        return None 

def save_results_to_csv(ip_counts, output_file_path, top_n=5):
    """
    Identifies the top N IPs and saves the full count to a CSV file.

    Args:
        ip_counts (collections.Counter): The Counter object of IP counts.
        output_file_path (str): The path for the output CSV file.
        top_n (int): The number of top IPs to identify and print.
    """
    if not ip_counts:
        print("No IP data to process.")
        return

    try:
        # Get the top N most common IP addresses for printing
        top_ips = ip_counts.most_common(top_n)
        print(f"\n🏆 Top {top_n} IP Addresses by Request Count:")
        for ip, count in top_ips:
            print(f"- {ip}: {count} requests")

        # Save all IP counts to the CSV file, sorted by count
        with open(output_file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Write the header
            csv_writer.writerow(['IP_Address', 'Request_Count'])
            # Write all the data, sorted from most common to least
            csv_writer.writerows(ip_counts.most_common())

        print(f"\n✅ Successfully saved all IP counts to '{output_file_path}'.")

    except IOError as e:
        print(f"❌ Error: Could not write to file '{output_file_path}'. Reason: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during file writing: {e}")



def download_access_log_dataset():
    """
    Downloads the latest version of the web server access logs dataset using kagglehub.
    Returns the path to the dataset directory.
    """
    dataset_path = kagglehub.dataset_download("eliasdabbas/web-server-access-logs")
    print("Path to dataset files:", dataset_path)
    return dataset_path


def main():
    """
    Main function to download dataset, analyze log, and save results.
    """
    dataset_path = download_access_log_dataset()
    log_file = os.path.join(dataset_path, "access.log")
    if not os.path.exists(log_file):
        print(f"❌ Error: Could not find 'access.log' in the downloaded dataset at {dataset_path}.")
        sys.exit(1)

    # Always write output.csv to the output folder
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "output.csv")

    print(f"Analyzing log file: '{log_file}'...")
    all_ip_counts = analyze_log(log_file)

    if all_ip_counts:
        save_results_to_csv(all_ip_counts, output_file, top_n=5)


if __name__ == "__main__":
    main()