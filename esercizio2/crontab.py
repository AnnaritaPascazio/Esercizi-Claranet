#!/usr/bin/env python3

def print_crontab_solution():
    """
    Prints the complete solution for setting up automated backups using crontab
    """
    crontab_string = "0 0 * * 0 tar czf - /home/user | ssh user@192.168.1.100 'cat > /backup/home_user_$(date +\\%Y\\%m\\%d).tar.gz'"
    
    solution = f"""
Esercizio 2 - Soluzione:

1. Stringa crontab:
{crontab_string}

Spiegazione della stringa crontab:
- 0 0 * * 0     : Esegue ogni domenica a mezzanotte
- tar czf -     : Crea un archivio compresso
  - c : create (crea nuovo archivio)
  - z : gzip (comprime con gzip)
  - f : file (specifica il file di output)
  - - : output su stdout invece che su file
- |             : Pipe, passa l'output al comando successivo
- ssh user@192.168.1.100 : Connessione SSH al server remoto
- 'cat > /backup/...' : Salva lo stream in un file sul server remoto
- $(date +\\%Y\\%m\\%d) : Aggiunge la data al nome del file

2. Configurazione necessaria per l'autenticazione SSH:

a) Generare le chiavi SSH sul server locale:
   $ ssh-keygen -t ed25519 -C "backup@local"
   Questo creerà:
   - ~/.ssh/id_ed25519 (chiave privata)
   - ~/.ssh/id_ed25519.pub (chiave pubblica)

b) Copiare la chiave pubblica sul server remoto:
   $ ssh-copy-id user@192.168.1.100
   Questo aggiungerà la chiave a ~/.ssh/authorized_keys sul server remoto

c) Verificare l'accesso SSH senza password:
   $ ssh user@192.168.1.100 echo "Test connection"

d) Creare la directory di backup sul server remoto:
   $ ssh user@192.168.1.100 'mkdir -p /backup'

e) Impostare i permessi corretti:
   Sul server locale:
   $ chmod 600 ~/.ssh/id_ed25519
   $ chmod 644 ~/.ssh/id_ed25519.pub
   
   Sul server remoto:
   $ chmod 700 ~/.ssh
   $ chmod 600 ~/.ssh/authorized_keys

3. Installazione del cronjob:
   $ crontab -e
   (Incollare la stringa crontab mostrata sopra)

Note di sicurezza:
- L'autenticazione basata su chiavi SSH è più sicura di quella basata su password
- I permessi restrittivi sui file delle chiavi sono essenziali per la sicurezza
- Il backup viene trasferito attraverso una connessione SSH crittografata
- Ogni backup ha un nome univoco con la data, facilitando la gestione delle versioni
"""
    print(solution)

if __name__ == "__main__":
    print_crontab_solution()
