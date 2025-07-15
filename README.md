# SSL Spoofing Detection & Homograph Attack Simulation

This project demonstrates how **SSL/TLS certificate validation** can be **bypassed** if trust is misused, and how **Unicode-based homograph attacks** can spoof domain names to trick users. It includes two components:

- `attacker.py`: Simulates an attacker server with a valid-looking certificate and sends spoofed domain names.
- `sniffer.py`: Simulates a client that connects via SSL and detects if the returned domain is spoofed using homograph techniques.

---

## Disclaimer

This project is intended **strictly for educational and research purposes only**. Do **not** use this to conduct unauthorized spoofing or intercept SSL connections in production systems.

---

## SSL Trust Exploit Demonstration

In this simulation, SSL is **bypassed** by trusting a malicious certificate:

- A self-signed SSL certificate (`cert.pem`, `key.pem`) is generated and **used by the attacker server**.
- The **same certificate is hardcoded as trusted** in the client (`sniffer.py`) using `ssl.create_default_context(cafile="cert.pem")`.
- As a result, the attacker’s SSL connection is considered “valid” — even though it shouldn't be in a real-world scenario.

This simulates what can happen when:

- Users manually trust a malicious certificate.
- Malware injects malicious root certificates into the system/browser.
- Developers hardcode trusted certificates without proper verification.

> **Key Insight**: SSL alone is not foolproof if the trust model is compromised.

---

##  Homograph Attack Background

Homograph attacks exploit visually similar characters from non-Latin scripts to spoof legitimate domains.

### Examples:

| Legitimate Domain | Spoofed Domain          | Trick Used                         |
|-------------------|-------------------------|------------------------------------|
| `google.com`      | `gоogle.com`            | Cyrillic `о` (U+043E)              |
| `apple.com`       | `аpple.com`             | Cyrillic `а` (U+0430)              |
| `paypal.com`      | `раyраl.com`            | Cyrillic `р`, `а`                  |
| `github.com`      | `gitһub.com`            | Cyrillic `һ` (U+04BB)              |

These are **visually identical** to users but resolve to different DNS entries.

---

##  Detection Logic in `sniffer.py`

- **SSL Certificate Validation** (simulated trust bypass)
- **Spoofing Checks**:
  - Flags domains with Unicode characters (`ord(c) > 127`)
  - Compares received domain with original
  - Prompts user if a change is detected

---

## 🛠 How to Run

1. **Generate Certificate** 
2. **Start attacker server first : python attacker.py**
3. **Start the sniffer client : python sniffer.py**

