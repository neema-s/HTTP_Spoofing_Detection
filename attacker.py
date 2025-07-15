import socket
import ssl

# Create SSL context and load the server's certificate
context = ssl.create_default_context(cafile="cert.pem")

# Wrap the socket with SSL
conn = context.wrap_socket(
    socket.socket(socket.AF_INET),
    server_hostname='server_hostname'
)

try:
    # Connect to the attacker server (replace IP and port as necessary)
    conn.connect(('attacker_ip', 443))

    # SSL context already performs hostname verification automatically
    print("Certificate matched successfully!")

    # Send and receive data
    original_domain = input("Enter domain to visit: ")
    conn.send(original_domain.encode())

    # Receiving spoofed domain
    spoofed_domain = conn.recv(1024).decode()
    print("Received domain:", spoofed_domain)

    # Detection logic for spoofing
    if any(ord(c) > 127 for c in spoofed_domain):
        print("Spoofing detected: Non-ASCII characters.")
    elif spoofed_domain != original_domain:
        print(f"Domain changed from {original_domain} to {spoofed_domain}")
        user_input = input("Proceed? (yes/no): ")
        if user_input.lower() != "yes":
            print("Spoofing blocked by user.")
        else:
            print("Proceeding...")
    else:
        print("Domain unchanged. Safe to proceed.")

except ssl.CertificateError as e:
    print(f"Certificate verification failed: {e}")
except Exception as e:
    print(f"Connection failed: {e}")
finally:
    conn.close()
