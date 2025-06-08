# VPN-Logger
# 🔐 VPN Setup Logger with IP Monitoring Dashboard
![Image](https://github.com/user-attachments/assets/3cc39407-ffff-4bb4-9aff-487a5e078069)
![Image](https://github.com/user-attachments/assets/0ab54016-ba49-4ab3-9680-2b0501cc8e76)

## 🎯 Objective
To set up and use a free VPN, monitor external and local IP address changes, and log the results using a Python-based GUI dashboard. This project demonstrates how VPN encryption works, how to verify VPN usage, and how to analyze changes in connection using visual tools.

## 📸 Screenshots
## VPN Client Connected
![Image](https://github.com/user-attachments/assets/a5e14e4c-4d62-4555-ba1b-4301f5742860)

## Changed IP Location
![Image](https://github.com/user-attachments/assets/06a4c4c7-427d-4c24-b046-356c72b846aa)

## VPN Disconnected and IP Reverted
![Image](https://github.com/user-attachments/assets/87b6a9ca-0503-48e5-b8bf-6e6406e19d26)

## Speed Test
![Image](https://github.com/user-attachments/assets/4de41a2f-fdd8-4ce7-afb9-5ccaa163cfb5)
![Image](https://github.com/user-attachments/assets/f960674b-55f0-4999-aba0-08b51e5dc44c)

## ✅ Outcome
- Successfully set up and tested a VPN connection.
- Verified IP address changes when connected/disconnected from the VPN.
- Logged external and local IPs over time.
- Plotted IP variation frequency for audit and monitoring purposes.

## 📌 Key Concepts
- VPN (Virtual Private Network)  
- IP Address Logging
- Tunneling Protocols
- Encryption and Privacy  
- GUI Programming with Tkinter  
- IP Tracking and Log Visualization  
- CSV Export & Data Analytics 

## 🛠 How It Was Done
1. Choose a VPN Provider 
   - Selected a reputable free VPN (like ProtonVPN or Windscribe).
   - Installed the VPN client and created an account.

2. GUI Tool Setup  
   - Created a Python GUI using Tkinter to track local and external IPs.
   - Fetched public IP using requests.get("https://api.ipify.org").

3. Log Management  
   - Logged IPs and timestamps into a csv file (vpn_log.csv).
   - Enabled real-time and manual refresh for IP logging.

4. Data Analysis Tools  
   - Added CSV export functionality for the logs.
   - Used matplotlib and collections.Counter to visualize IP change frequency.

5. Automation  
   - Automatic refresh every 5 minutes to capture IP changes periodically.
   - Manual logging option via "Refresh & Log Now" button.

## 📷 Deliverables
- VPN Setup Screenshot: Screenshot after connecting to VPN.
- Dashboard Screenshot: Tkinter GUI showing logged IPs.
- IP Change Visualization: Bar plot showing frequency of external IPs.

🔍 VPN Setup Instructions (Using Windscribe)
- Sign up at: https://windscribe.com/
- Download & install the Windscribe desktop app.
- Login and connect to a server (closest region recommended).
- Run the Python script above.
- Use "README.md" to verify IP change from your ISP.
- Visit https://whatismyipaddress.com manually to cross-verify.
- Disconnect from VPN and compare again.
- Observe how the ML model detects region/IP anomalies.

## ✅ Benefits of Using a VPN
- Hides IP address and location.
- Encrypts internet traffic (Wi-Fi protection).
- Bypasses geo-restrictions and censorship.
- Protects privacy on public Wi-Fi.

## ⚠️ Limitations of VPN
- May reduce internet speed.
- Some free VPNs log user data or show ads.
- Does not protect against phishing or malware.
- Certain websites block VPN traffic.

## 💬 Interview Questions 
1. What is a VPN and why is it used?
2. What does IP address reveal about a user?
3. How did you detect external IP in this project?
4. What's the difference between local and external IP?
5. Why do we compare external IPs before and after VPN?
6. How is the IP log stored?
8. How do you confirm traffic is encrypted?
9. How do you know VPN is working?
10. What are limitations of VPNs?
11. What is tunneling in VPNs?
 
## 🧠 Summary
This project demonstrates practical VPN usage, validation through IP logging, and monitoring network security visually. By capturing, storing, exporting, and plotting IP changes, we bridge the gap between VPN theory and hands-on verification using Python. It showcases how encryption, privacy, and analytics converge to empower users to control their online presence securely.
