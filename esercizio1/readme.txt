Analizzare una directory per identificare i file eseguibili è utile per capire quali linguaggi di scripting vengono utilizzati. 
Questo script automatizza tutto il processo, classificando i file in base all’interprete definito nella loro shebang.

Ci sono tre parti principali:
1️⃣ Identificazione dei file eseguibili
Lo script esamina i file in una directory e determina se sono eseguibili. Su Windows, controlla le estensioni (.exe, .bat, .py, ecc.); su Linux/macOS, verifica i permessi di esecuzione.

2️⃣ Estrazione della Shebang
Se un file è eseguibile, lo script legge la prima riga per identificare l’interprete. Se trova una shebang valida, registra l’interprete; altrimenti, ignora il file.

3️⃣ Classificazione e report dei risultati
Alla fine, lo script ordina i risultati per numero di file eseguibili e, in caso di parità, per nome dell’interprete. 

Viene poi stampato un report con il conteggio dei file per ogni interprete trovato.
In breve, questo script è un modo veloce per analizzare una directory e ottenere un resoconto dettagliato dei linguaggi di scripting utilizzati. 
Funziona su Windows, Linux e macOS, esplorando anche le sottodirectory.
