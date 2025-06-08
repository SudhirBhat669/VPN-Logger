import tkinter as tk
from tkinter import messagebox, filedialog
import socket
import requests
from datetime import datetime
import threading
import csv
import matplotlib.pyplot as plt
from collections import Counter

LOG_FILE = "vpn_log.txt"
REFRESH_INTERVAL = 5 * 60 * 1000  # 5 minutes in milliseconds

def get_ip_info():
    try:
        external_ip = requests.get("https://api.ipify.org").text
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return external_ip, local_ip
    except Exception as e:
        return None, None

def log_ip(external_ip, local_ip):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} | External IP: {external_ip} | Local IP: {local_ip}\n")

def read_log():
    try:
        with open(LOG_FILE, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No log entries yet."

def parse_log():
    """Parse the log file and return a list of (timestamp, external_ip) tuples."""
    data = []
    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(" | ")
                if len(parts) == 3:
                    timestamp_str = parts[0]
                    ext_ip_part = parts[1]
                    # Extract external IP
                    ext_ip = ext_ip_part.replace("External IP: ", "")
                    data.append((timestamp_str, ext_ip))
    except FileNotFoundError:
        pass
    return data

def update_status():
    ext_ip, loc_ip = get_ip_info()
    if ext_ip and loc_ip:
        status = f"External IP: {ext_ip}\nLocal IP: {loc_ip}"
        log_ip(ext_ip, loc_ip)
    else:
        status = "Error: Could not retrieve IP information."
    status_text.set(status)
    # Update history box
    history_text.config(state=tk.NORMAL)
    history_text.delete("1.0", tk.END)
    history_text.insert(tk.END, read_log())
    history_text.config(state=tk.DISABLED)
    # Schedule next update
    root.after(REFRESH_INTERVAL, update_status)

def clear_log():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear the log?"):
        with open(LOG_FILE, "w") as f:
            f.write("")
        history_text.config(state=tk.NORMAL)
        history_text.delete("1.0", tk.END)
        history_text.insert(tk.END, "Log cleared.")
        history_text.config(state=tk.DISABLED)

def export_csv():
    data = parse_log()
    if not data:
        messagebox.showinfo("Export CSV", "No log data to export.")
        return
    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv")],
        title="Save log as CSV"
    )
    if file_path:
        with open(file_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Timestamp", "External IP"])
            writer.writerows(data)
        messagebox.showinfo("Export CSV", f"Log exported successfully to:\n{file_path}")

def plot_ip_changes():
    data = parse_log()
    if not data:
        messagebox.showinfo("Plot IP Changes", "No log data to plot.")
        return

    # Count frequency of each external IP and plot over time
    timestamps, ips = zip(*data)
    ip_counts = Counter(ips)

    plt.figure(figsize=(10, 5))
    plt.bar(ip_counts.keys(), ip_counts.values(), color='skyblue')
    plt.title("Frequency of External IPs over Time")
    plt.xlabel("External IP")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# GUI setup
root = tk.Tk()
root.title("VPN Logger")
root.geometry("600x500")

status_text = tk.StringVar()

tk.Label(root, text="Current IP Status:", font=("Arial", 14, "bold")).pack(pady=(10, 0))
status_label = tk.Label(root, textvariable=status_text, font=("Arial", 12), justify="left")
status_label.pack(pady=(0, 10))

btn_frame = tk.Frame(root)
btn_frame.pack()

refresh_btn = tk.Button(btn_frame, text="Refresh & Log Now", command=update_status)
refresh_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(btn_frame, text="Clear Log", command=clear_log)
clear_btn.grid(row=0, column=1, padx=10)

export_btn = tk.Button(btn_frame, text="Export Log to CSV", command=export_csv)
export_btn.grid(row=0, column=2, padx=10)

plot_btn = tk.Button(btn_frame, text="Plot IP Changes", command=plot_ip_changes)
plot_btn.grid(row=0, column=3, padx=10)

tk.Label(root, text="IP Log History:", font=("Arial", 14, "bold")).pack(pady=(10, 0))
history_text = tk.Text(root, height=15, width=70)
history_text.pack(pady=(0, 10))
history_text.insert(tk.END, read_log())
history_text.config(state=tk.DISABLED)

# Start initial update + schedule automatic refresh
update_status()

root.mainloop()
