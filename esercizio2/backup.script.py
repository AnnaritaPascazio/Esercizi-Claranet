import os
import sys
import paramiko
import tarfile
import tempfile
from datetime import datetime

def create_backup(source_dir, remote_host, remote_user, remote_path):
    """ Create a backup and send it to remote server via SSH """
    ssh = None
    sftp = None
    
    try:
        print(f"Connecting to {remote_host}...")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(remote_host, username=remote_user, key_filename=os.path.expanduser("~/.ssh/id_ed25519"))

        sftp = ssh.open_sftp()
        timestamp = datetime.now().strftime('%Y%m%d')
        backup_filename = f'home_user_{timestamp}.tar.gz'
        remote_file_path = os.path.join(remote_path, backup_filename)

        print(f"Creating backup of {source_dir}")
        print(f"Will be sent to: {remote_host}:{remote_file_path}")

        with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
            tar_path = tmpfile.name

        with tarfile.open(tar_path, mode='w:gz') as tar:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    if os.path.exists(file_path) and os.access(file_path, os.R_OK):
                        arcname = os.path.relpath(file_path, source_dir)
                        tar.add(file_path, arcname=arcname)
        try:
            sftp.stat(remote_path)
        except FileNotFoundError:
            sftp.mkdir(remote_path)

        sftp.put(tar_path, remote_file_path)
        print(f"Backup successfully uploaded to {remote_host}:{remote_file_path}")

        os.remove(tar_path)

    except paramiko.SSHException as e:
        print(f"SSH Error: {e}")
        sys.exit(1)
    except TimeoutError as e:
        print(f"Timeout Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Backup failed: {e}")
        sys.exit(1)
    finally:
        if sftp is not None:
            sftp.close()
        if ssh is not None:
            ssh.close()

def main():
    SOURCE_DIR = os.path.expanduser("~")
    REMOTE_HOST = "192.168.1.100"
    REMOTE_USER = "user"
    REMOTE_BACKUP_PATH = "/backup"

    if not os.path.isdir(SOURCE_DIR):
        print(f"Error: Source directory '{SOURCE_DIR}' does not exist")
        sys.exit(1)

    create_backup(SOURCE_DIR, REMOTE_HOST, REMOTE_USER, REMOTE_BACKUP_PATH)

if __name__ == "__main__":
    main()
