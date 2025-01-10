
# File Renamer 
<img src="assets/logo.svg" alt="File Renamer Logo" width="50"/> 

**File Renamer** ist ein praktisches Python-Tool, das das Umbenennen von Dateien effizient und benutzerfreundlich gestaltet. Es bietet die Möglichkeit, Dateien nach spezifischen Konventionen umzubenennen, wie z. B.:

- Umwandlung von Groß- in Kleinbuchstaben.
- Ersetzen von Leerzeichen durch Unterstriche (`_`).
- Anpassung von Umlauten wie `ä`, `ö`, `ü` in `ae`, `oe`, `ue`.
- Ergänzen fehlender Dateiendungen basierend auf dem Dateityp.
- Korrektur falscher Dateiendungen.
- Automatisches Hinzufügen von Präfixen wie `img_` für Bilder oder `vid_` für Videos.

Das Tool wurde speziell für Benutzer entwickelt, die mit großen Mengen an Dateien arbeiten und diese schnell und effizient organisieren möchten.

# Gebrauchsanweisung

## Nutzung von File Renamer

1. **Verzeichnis auswählen:**
   - Klicke auf den Button **"Select Directory"**.
   - Wähle das Verzeichnis aus, in dem sich die Dateien befinden, die nach den festgelegten **Namenskonventionen** geprüft werden sollen:
     - **Namenskonventionen:** Regeln, die sicherstellen, dass Dateinamen einheitlich und übersichtlich sind:
       - **Kleinbuchstaben verwenden:** Vermeidung von Großbuchstaben für Konsistenz.
      - **Wörter mit Unterstrichen trennen:** `urlaub fotos 2023.jpg` → `urlaub_fotos_2023.jpg`.             Leerzeichen werden durch Unterstriche ersetzt, um Dateinamen serverfreundlich zu gestalten.
      - **CamelCase in Bindestriche umwandeln:** `UrlaubFotos2023.jpg` → `urlaub-fotos-2023.jpg`.          Dies sorgt für einheitliche und gut lesbare Dateinamen.

       - **Umlaute und Sonderzeichen ersetzen:** `ä` → `ae`, `ö` → `oe`, `ü` → `ue`, `ß` → `ss`.

2. **Dateien prüfen:**
   - Nachdem das Verzeichnis ausgewählt wurde, erscheinen die Dateien in einem Vorschaufenster.
   - Überprüfe die angezeigten Dateien und stelle sicher, dass sich die gewünschten Dateien im Verzeichnis befinden.

3. **Dateien umbenennen:**
   - Klicke auf den Button **"Start"**, um den Umbenennungsprozess zu starten.
   - Das Tool prüft alle Dateien im ausgewählten Verzeichnis und passt die Dateinamen nach den Konventionen an, wenn nötig.

4. **Ergebnis überprüfen:**
   - Die aktualisierten Dateinamen werden automatisch im Vorschaufenster angezeigt.
   - Eine Übersicht der Änderungen wird auch in der Konsole ausgegeben.

---

## Video-Demonstration

Sieh dir das folgende kurze Video an, um zu erfahren, wie du das Tool Schritt für Schritt nutzen kannst:

<video width="600" controls>
  <source src="assets/screencast.mp4" type="video/mp4">
  Dein Browser unterstützt dieses Video-Format nicht.
</video>

---

## Download

### Linux
Lade die ausführbare Datei für Linux herunter und führe sie aus:

- [Download fileRenamer für Linux](dist/fileRenamer)
- [Download fileRenamer.zip für Linux](assets/fileRenamer.zip)


## Hinweise

- **Unveränderte Dateien:** Dateien, die bereits den Konventionen entsprechen, werden nicht umbenannt.
- **Unterstützte Dateitypen:** Das Tool erkennt und korrigiert Endungen für Bilder (z. B. `.jpg`, `.png`), Videos (z. B. `.mp4`, `.mov`) und PDFs.

---

Dieses Tool wurde entwickelt, um den Umgang mit großen Mengen an Dateien effizienter und zeitsparender zu gestalten. Viel Erfolg beim Organisieren deiner Dateien! 😊

## Features

- **Benutzerfreundliche GUI:** Intuitive Oberfläche mit Dateivorschau und Verzeichnisauswahl.
- **Automatische Erkennung des Dateityps:** Nutzt den Dateiinhalt, um den MIME-Typ zu bestimmen.
- **Schnell und effizient:** Optimiert für die Verarbeitung vieler Dateien gleichzeitig.
- **Plattformübergreifend:** Funktioniert auf Windows, macOS und Linux.

## Installation

Um die Anwendung auszuführen, stelle sicher, dass Python installiert ist. Du kannst das Programm entweder direkt ausführen oder eine Standalone-Version herunterladen.

## Autor

Dieses Projekt wurde von **Martin Drus** entwickelt. Es wurde mit dem Ziel erstellt, Zeit zu sparen und Dateimanagement einfacher zu machen.
