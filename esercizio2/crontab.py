#!/usr/bin/env python3

def print_crontab_solution():
    """
    Stampa la soluzione per configurare backup automatici usando crontab
    """

    crontab_string = "0 0 * * 0 tar czf - /home/user | ssh user@192.168.1.100 'cat > /backup/home_user_$(date +\\%Y\\%m\\%d).tar.gz'"

    solution = f"""
Fare il backup dei propri file è fondamentale, ma ricordarsi di farlo manualmente è spesso un problema. 
Gli script che abbiamo qui servono proprio a risolvere questo, creando un sistema automatico che salva i dati senza bisogno di intervento umano.
Per gestire l'autenticazione sul server remoto senza dover inserire la password ogni volta, è consigliabile configurare l'autenticazione SSH basata su chiave pubblica.

Ci sono tre parti principali:
1️⃣ Generazione del Comando Crontab per il Backup
Il primo script stampa a schermo il comando da inserire in crontab per avviare un backup automatico ogni domenica a mezzanotte.
💾 Il comando usa tar per comprimere la cartella /home/user e la invia a un server remoto.
🔑 Perché funzioni senza chiedere password, bisogna configurare l’accesso SSH con chiavi.
📌 Lo script fornisce anche i comandi per generare la chiave (ssh-keygen) e copiarla sul server (ssh-copy-id).
In breve, questo script aiuta a impostare il backup in pochi minuti, senza dover ricordare nulla ogni settimana.

Stringa crontab:
{crontab_string}

Spiegazione della stringa crontab:
- 0 0 * * 0: Ogni domenica a mezzanotte
- tar czf -: Crea un archivio compresso
- ssh user@192.168.1.100: Connessione SSH al server remoto
- 'cat > /backup/...': Salva il backup sul server remoto
- $(date +\\%Y\\%m\\%d): Nome file con la data

2️⃣ Creazione e Trasferimento Automatico del Backup via SSH
Il secondo script fa tutto da solo:
✅ Crea un archivio .tar.gz della cartella dell’utente.
✅ Controlla se la destinazione sul server remoto esiste, altrimenti la crea.
✅ Trasferisce il file tramite SFTP usando la libreria Paramiko.
✅ Cancella il file temporaneo dopo l’upload per non sprecare spazio.
Se qualcosa va storto, lo script intercetta gli errori (ad esempio, se la connessione SSH non funziona) e avvisa l’utente.
🔍 Questo è perfetto per chi vuole un backup automatico senza nemmeno dover aprire crontab: basta eseguire lo script e lui fa tutto.

3️⃣ Guida Dettagliata alla Configurazione
   - Generazione chiavi SSH:
     $ ssh-keygen -t ed25519 -C "backup@local"
   - Copia chiave pubblica sul server remoto:
     $ ssh-copy-id user@192.168.1.100
   - Verifica accesso SSH senza password:
     $ ssh user@192.168.1.100 echo "Test connection"
   - Crea la directory di backup:
     $ ssh user@192.168.1.100 'mkdir -p /backup'
   - Imposta i permessi corretti:
     Sul server locale:
     $ chmod 600 ~/.ssh/id_ed25519
     $ chmod 644 ~/.ssh/id_ed25519.pub
     Sul server remoto:
     $ chmod 700 ~/.ssh
     $ chmod 600 ~/.ssh/authorized_keys

Nota finale:
La configurazione SSH con chiavi permette un accesso sicuro senza dover digitare la password ogni volta, e il cronjob assicura che i backup vengano eseguiti in modo completamente automatico e sicuro.

"""
    print(solution)

if __name__ == "__main__":
    print_crontab_solution()


