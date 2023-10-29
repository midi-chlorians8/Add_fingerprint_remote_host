import argparse
import subprocess
import sys

def check_sshpass_installed():
    try:
        subprocess.run(["sshpass", "-V"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        print("Debug: sshpass not found.")
        return False

def install_sshpass():
    print("Debug: Attempting to install sshpass.")
    try:
        platform = sys.platform
        if platform == "darwin":  # macOS
            subprocess.run(["brew", "install", "sshpass"], check=True)
        elif platform == "linux":  # Ubuntu/Linux
            subprocess.run(["sudo", "apt-get", "install", "sshpass", "-y"], check=True)
        else:
            print(f"Unsupported platform: {platform}")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install sshpass: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="SSH automation script.")
    parser.add_argument("-i", "--ip", nargs="+", help="List of IP addresses", required=True)
    parser.add_argument("-p", "--password", help="Password for SSH", required=True)
    parser.add_argument("-u", "--user", help="Username for SSH", required=True)

    args = parser.parse_args()
    print(f"Received arguments: IPs - {args.ip}, Password - {args.password}, User - {args.user}")

    if not check_sshpass_installed():
        install_sshpass()

    for ip in args.ip:
        command = ["sshpass", "-p", args.password, "ssh-copy-id", f"{args.user}@{ip}"]
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
            print(f"Executing: {' '.join(command)} - SUCCESS")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Executing: {' '.join(command)} - FAULT")
            print(e.stderr)

if __name__ == "__main__":
    main()
