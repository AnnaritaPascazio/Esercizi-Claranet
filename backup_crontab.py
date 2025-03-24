#!/usr/bin/env python3

def get_crontab_command():
    """Returns the crontab command for weekly backups"""
    return "0 0 * * 0 tar czf - /home/user | ssh user@192.168.1.100 'cat > /backup/home_user_$(date +\\%Y\\%m\\%d).tar.gz'"

if __name__ == "__main__":
    print("\nCrontab command to execute every Sunday at midnight:")
    print(get_crontab_command())
    print("\nTo use this command:")
    print("1. Make sure SSH keys are set up:")
    print("   $ ssh-keygen -t ed25519")
    print("   $ ssh-copy-id user@192.168.1.100")
    print("\n2. Create backup directory on remote server:")
    print("   $ ssh user@192.168.1.100 'mkdir -p /backup'")
    print("\n3. Add to crontab:")
    print("   $ crontab -e")
    print("   (paste the command above)")
