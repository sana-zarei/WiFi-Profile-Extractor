import subprocess

def get_wifi_profiles():
    """
    Retrieves a list of WiFi profiles stored on the system.
    Returns : List of WiFi profile names.
    """
    # Command to fetch WiFi profiles
    command = ['netsh', 'wlan', 'show', 'profiles']
    # Execute command and decode output
    output = subprocess.check_output(command).decode('utf-8', errors="backslashreplace")
    # Extract profiles from command output
    profiles_data = output.split('\n')
    profiles = [line.split(":")[1].strip() for line in profiles_data if "All User Profile" in line]
    return profiles

def get_wifi_passwords(profiles):
    """
    Retrieves passwords for the given WiFi profiles.
    Args : profiles: List of WiFi profile names.
    Returns : Dictionary with profile names as keys and their passwords as values.
    """
    passwords = {}
    for profile in profiles:
        # Command to fetch password for a specific WiFi profile
        command = ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']
        # Execute command and decode output
        output = subprocess.check_output(command).decode('utf-8', errors="backslashreplace")
        # Extract password from command output
        password_data = [line.split(":")[1].strip() for line in output.split('\n') if "Key Content" in line]
        password = password_data[0] if password_data else ""
        passwords[profile] = password
    return passwords

def main():
    """
    Main function to retrieve and print WiFi profiles and their passwords.
    """
    # Retrieve WiFi profiles
    profiles = get_wifi_profiles()
    # Retrieve passwords for these profiles
    passwords = get_wifi_passwords(profiles)
    # Print profiles and their passwords
    for profile, password in passwords.items():
        print("{:<30}| {:<}".format(profile, password))

if __name__ == "__main__":
    main()
