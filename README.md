# 🌐🔍 DNS Record Fetcher & Zone Transfer Auditor 🚀

**Description:**
Python tool 🐍 for fetching DNS records (A, AAAA, CNAME, MX, TXT, NS, SRV) and auditing zone transfers 🛡️ to detect security gaps 🔐. Ideal for network admins and cybersecurity pros 👨‍💻👩‍💻. Results are displayed clearly and saved as a CSV 📊 for easy analysis. Secure your DNS configurations with this handy tool!

## 📋 Features

- Fetches DNS records:
  - `A`
  - `AAAA`
  - `CNAME`
  - `MX`
  - `TXT`
  - `NS`
  - `SRV`
- Attempts zone transfers to identify potential security misconfigurations.
- Outputs results in a tabular format and saves them to a CSV file.

## 🛠️ Installation

1. Clone the repository:
```
git clone https://github.com/WildWestCyberSecurity/Comprehensive-DNS-Record-Fetcher-Zone-Transfer-Auditor-.git
```

2. Navigate to the project directory:
```
cd Comprehensive-DNS-Record-Fetcher-Zone-Transfer-Auditor-
```

3. Install the required Python packages:
```
pip install -r requirements.txt
```

## 🚀 Usage

1. Create a `domains.txt` file in the project directory with a list of domains, one per line.

2. Run the script:
```
python dns_fetcher.py -d domains.txt
```

3. The DNS records will be displayed in the terminal and saved to `dns_records.csv`.

## 📝 Example

Here’s how to structure your `domains.txt` file:
```
example.com
anotherdomain.com
```

When you run the script, it will fetch the DNS records for these domains and attempt zone transfers if applicable.

## ⚠️ Security Note

Performing zone transfers without authorization can be considered intrusive and potentially malicious. Always ensure you have permission to perform zone transfers on the target domains.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Contributing

Feel free to submit issues or pull requests if you’d like to contribute to the project. Contributions are always welcome!

---

Thank you for checking out the DNS Record Fetcher & Zone Transfer Auditor! If you find this tool helpful, please consider giving the repository a ⭐.
