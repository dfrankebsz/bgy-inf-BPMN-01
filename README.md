# Version UE2 V3

**Neu:** Die draw.io-Werkstatt nutzt ausschließlich lokalen Diagrammvergleich mit Musterlösungen. Es werden keine Diagramme hochgeladen. Bearbeitbare `.drawio`-Vorlagen können dort, wo vorhanden, direkt an der jeweiligen Aufgabe heruntergeladen werden. Vorhandene Schülerkonten und Fortschritte bleiben beim Ersetzen des Projekts erhalten (bei gleichem Netlify-Projekt).

# BPMN-Labor · Informatik UE 2 – Netlify-Projekt

**Stand:** 24.11.2026  
**Schulart:** Berufliches Gymnasium, Klasse 11  
**Technik:** statische HTML/CSS/JavaScript-Oberfläche, Netlify Functions, Netlify Blobs, PDFKit. **Kein Supabase, keine SQL-Datenbank, keine allgemeine AUTH-Schlüsselvariable.**

## 1. Einrichtung in GitHub und Netlify

1. Entpacken Sie die ZIP-Datei. Laden Sie **den Inhalt des Ordners**, nicht die ZIP-Datei selbst, in das Hauptverzeichnis eines **neuen** GitHub-Repositories hoch. Insbesondere müssen `package.json`, `netlify.toml`, `app.js`, `course-data.js`, `index.html`, der Ordner `netlify/functions/` und `assets/` im Repository liegen.
2. Öffnen Sie Netlify → **Add new project** → **Import an existing project** und verbinden Sie Ihr GitHub-Repository.
3. Die Einstellungen werden aus `netlify.toml` geladen: **Build command** `npm run build`, **Publish directory** `dist`, **Functions** `netlify/functions`.
4. Unter **Site configuration → Environment variables** legen Sie die Variable **`TEACHER_ACCESS_CODE`** an. Wählen Sie einen zufälligen geheimen Code mit **mindestens 12 Zeichen** (längere zufällige Codes sind empfehlenswert) und erlauben Sie Zugriff zur Laufzeit der Functions. **Tragen Sie den Wert nicht in GitHub oder in Quelldateien ein.** Anschließend deployen Sie die Seite erneut.
5. Öffnen Sie die Netlify-Seite. Wählen Sie **Registrieren**, geben Sie eine **Klasse**, einen **Nickname** und ein selbstgewähltes **Passwort** mit mindestens 8 Zeichen ein. Lehrkräfte wählen zusätzlich **Lehrkraft** und geben den oben in Netlify hinterlegten Code ein. Konten bleiben an ihre angegebene Klasse gebunden. Jede Lehrkraft sieht nur Lernende derselben Klasse.
6. **Gastmodus:** Der Lernkurs ist ohne Konto nutzbar. Antwortdaten liegen dann nur im Browser-Speicher des betreffenden Geräts. Bei Anmeldung lässt sich vorhandener Gastfortschritt nach Bestätigung übernehmen.

**Hinweis zu vorhandenen UE-1-Kursen:** Der UE-2-Kurs besitzt **separate** Netlify-Blob-Stores mit eigenen Konten, Passwörtern und Fortschritten. Wenn Sie ihn als eigenes Netlify-Projekt deployen, beeinflusst er UE 1 nicht. Für dieselben Nicknames sind Konten pro Lernkurs erneut anzulegen. Eine Zusammenlegung in ein gemeinsames Portal ist später möglich, gehört aber nicht zu diesem Paket.

### Empfehlenswerte Netlify-Einstellungen

- HTTPS aktivieren (Netlify stellt HTTPS bereit).
- Für Lehrerkonten starke Passwörter und einen vertraulich behandelten Code verwenden.
- Bei schulischer Nutzung zunächst in einer Testklasse prüfen; die Lizenz-, Datenschutz- und Aufbewahrungsvorgaben Ihrer Schule beachten.
- Das Paket verlangt keinen externen KI-Dienst und übermittelt keine Freitextantworten an ein Sprachmodell.
- Der Unterrichtsrechner sollte draw.io/diagrams.net installiert haben; die URL ist nur als optionaler Web-Zugang verlinkt.

## 2. Kursstruktur

| Kapitel | Reguläre Aufgaben | Inhalte |
|---|---:|---|
| Warum BPMN? | 4 | Begriff, Entstehung, Berufsbezug |
| Ereignisse und Tätigkeiten | 6 | Start, Endereignis, Task |
| Sequenzfluss | 7 | Reihenfolge, Verbindungen, draw.io |
| XOR-Entscheidungen | 8 | Verzweigung, Bedingungen, Zusammenführung |
| draw.io-Werkstatt | 11 | Nachbauen, Fehlerkorrektur, eigenes Diagramm |
| Zusätzlich | 4 Bonusaufgaben | Anspruchsvollere Übertragungen |
| Abschlusstest | 10 Aufgaben | Kompetenzen prüfen |

In den 36 regulären Aufgaben beträgt das Verhältnis AFB I / II / III = 9 / 18 / 9. Die Angaben zum Anforderungsbereich stehen nur direkt an der jeweiligen Aufgabe, nicht als Prozentwerte im Kurs.

Alle Kapitel enthalten die wesentlichen fachlichen Erklärungen und Musterlösungen. Die Videos des GBTEC-Tutorials sind mit **Start- und Endzeitpunkten** verlinkt. Das verlinkte Tutorial wird nicht kopiert oder lokal gespeichert. Für den Videoserver gelten dessen eigene Nutzungs- und Datenschutzbedingungen.

### Videos

Quelle: GBTEC Group, „Einfache Modellierung in BPMN 2.0 – Schulung“, https://www.youtube.com/watch?v=xmls25KO7V8 (veröffentlicht 03.12.2020). Die Ausschnitte stammen aus den Zeitangaben des vom Nutzer bereitgestellten Transkripts:

- BPMN-Überblick 00:05–00:48
- Ereignisse 00:54–01:47
- Tätigkeiten 02:29–02:56
- Gateways/XOR 03:19–03:47
- Sequenzflüsse 04:42–05:05

Die Video-Schaltflächen öffnen einen eingebetteten YouTube-Player, der über URL-Parameter nur den jeweiligen Bereich abspielen soll. Falls ein Schulnetz dies blockiert, kann das vollständige Video geöffnet und zum genannten Abschnitt navigiert werden.

### Bilder und draw.io-Dateien

Unter `assets/diagramme/` liegen `*.svg` und `*.png` als Ansichten sowie `*.drawio` als **editierbare Quelldiagramme**. Die Aufgaben- und Lösungsbilder sind bewusst getrennt. Für die freie Modellierung können auch andere **fachlich gleichwertige** Lösungen korrekt sein. Die Bilder sind didaktische Originaldiagramme zu einem **fiktiven Unternehmen**.

## 3. Wie wird bewertet?

- Single Choice, Multiple Choice, Wahr/Falsch, Kategorien, Paare, Sortierung und Symbol-Dropplätze werden **deterministisch** mit den Lösungsschlüsseln in `course-data.js` verglichen. Drag-and-Drop erhält Alternativen per Auswahlliste für Touchgeräte und Tastatur.
- **Freitext** und **draw.io-Modellierungen** werden **nicht automatisch bewertet**. Die Lernenden schreiben ihre Begründung, lassen sich nach einer Sicherheitsabfrage die Musterlösung anzeigen und setzen ihre Selbsteinschätzung selbst. Die Lehrkraft sieht den entsprechenden Fortschritt als Selbstbewertung.
- **draw.io-Aufgaben:** Lernende erstellen oder bearbeiten ihre Diagramme lokal in draw.io und speichern die `.drawio`-Datei auf dem eigenen Rechner. Wo eine bearbeitbare Vorlage vorgesehen ist, gibt es direkt in der Aufgabe einen Download-Button. Nach einer Rückfrage wird die Musterlösung sichtbar. Anschließend vergleichen Lernende ihre Zeichnung selbst mit den Kriterien und markieren die Aufgabe als gelöst oder als zu überarbeiten. **Es gibt keinen Datei-Upload.** Eine schriftliche Anmerkung ist freiwillig; die Selbsteinschätzung kann auch ohne Text erfolgen. Das PDF dokumentiert die Selbsteinschätzung und gegebenenfalls eine Anmerkung, **nicht** die lokale Diagrammdatei.
- Wenn der gesamte Fortschritt am gleichen Tag von mehreren Geräten gleichzeitig bearbeitet wird, können die letzten Änderungen einander überschreiben. Deshalb jeweils nur ein Gerät zur gleichen Zeit benutzen und den Speichervorgang abschließen lassen.
- XP werden für korrekte oder von Lernenden als korrekt selbstbewertete Leistungen vergeben. Der XP-Shop ist ausschließlich eine Lernmotivation, keine Leistungsnote.

## 4. Login, Datenschutz, Lehrerrechte

- Schüler-Anmeldung: **Klasse + Nickname + Passwort** (kein Klartextpasswort in der Datenbank; scrypt mit individuellem Salt).
- Lehrer-Anmeldung: derselbe Ablauf, zusätzlich Netlify-Variable `TEACHER_ACCESS_CODE` beim Registrieren.
- 30-Tage-Sitzung mit HttpOnly-, Secure- und SameSite-Cookie (bei HTTPS).
- Netlify Blobs: separate Speicherbereiche für Konten, Sitzungen und Fortschritte; Login und Teacher-Aktionen ausschließlich über Netlify Functions.
- Lehrer sehen für ihre Klasse Nickname, gelöste Aufgaben, Testergebnisse, XP, Selbstcheck und Änderungszeitpunkt. Sie können Klassenfortschritte löschen, einzelne Fortschritte zurücksetzen, Nutzer entfernen und ein vorläufiges Passwort erzeugen. Die Weitergabe des vorläufigen Passworts erfolgt **außerhalb** des Kurses.
- Auf einen Lehrerzugang kann nicht ohne Kenntnis des Lehrercodes registriert werden. **Den Code niemals veröffentlichen.**
- Der Lehrerzugang besitzt absichtlich keinen Volltext-Zugriff auf private Freitext-Eingaben. Für inhaltliche Kontrolle können Schüler ihre Portfolio-PDFs vorlegen.
- **Netlify Blobs ist ein Key-Value-Speicher und keine relationale Transaktionsdatenbank.** Für kleinere Kursgruppen geeignet; bei sehr vielen parallelen Nutzern sind weitere Last- und Sicherheitsprüfungen nötig.
- Datenschutzfreigabe vor dem realen Schuleinsatz: insbesondere Auftragsverarbeitung, Datenschutzhinweise, Speicherfristen und Löschverfahren mit der Schule klären.

## 5. Portfolio als PDF

Über **Übersicht → Antwort-Portfolio** oder am Testende wird ein PDF aus **allen begonnenen Aufgaben**, eingegebenen Texten, Auswahlen, Selbsteinschätzungen und dem Status der Diagramm-Selbstkontrollen erzeugt. Bei draw.io-Aufgaben erscheint die Selbsteinschätzung und gegebenenfalls eine freiwillige schriftliche Anmerkung; die nur lokal gespeicherte Zeichnung selbst wird nicht im PDF abgebildet. Bei angemeldeten Nutzern wird zuerst versucht, den Stand zu synchronisieren. Die Verarbeitung erfolgt serverseitig durch `pdfkit` in einer Netlify Function. Im Gastmodus wird die aktuelle Browserkopie übertragen, ohne dass ein Benutzerkonto entsteht.

## 6. Entwicklerprüfung

Voraussetzung: Node.js >= 22.13.

```bash
npm install
npm run check
npm test
npm run build
npm run dev
```

In der Erstellungssitzung wurden die Inhaltsprüfung und die automatisierten Logik-/API-Tests ausgeführt. Die End-to-End-Prüfung mit einem tatsächlichen Netlify-Deployment, Cloud-Blobs und PDFKit war in der Erstellungssitzung wegen eingeschränktem Paket-/Browserzugriff **nicht vollständig möglich**; führen Sie die folgenden Prüfungen nach dem ersten Deployment durch:

1. Registrieren Sie Lehrkraft und Testschüler derselben Klasse; testen Sie ein Konto in einer zweiten Klasse.
2. Lösen Sie eine Multiple-Choice-Aufgabe und eine Symbol-Drop-Aufgabe und melden Sie sich auf einem zweiten Gerät mit denselben Zugangsdaten an.
3. Laden Sie zu einer draw.io-Aufgabe ein kleines PNG hoch, sichern Sie den Fortschritt und prüfen Sie, ob es nach dem erneuten Login sichtbar bleibt.
4. Laden Sie das PDF-Portfolio und prüfen Sie die enthaltene Zeichnung, Aufgabe und schriftliche Begründung.
5. Prüfen Sie, ob die Lehreransicht den Fortschritt korrekt zeigt, danach einen gezielten Passwortreset und das Löschen eines Testkontos.
6. Testen Sie die Darstellung auf Windows, Android und Apple-Geräten. Bei Touchbedienung benutzen Sie für die Symbolpositionen bei Bedarf die Auswahllisten.

## 7. Quellen und redaktioneller Hinweis

- Nutzerbereitgestellter Lehrplanauszug Informatik, BGY Sachsen 2026, Lernbereich 2: Informatische Modellierung und Projektmanagement.
- Nutzerbereitgestelltes Videotranskript des GBTEC-Tutorials, Kapitel Einführung, Ereignisse, Aktivitäten, Gateways und Verbinder.
- Object Management Group (OMG), BPMN 2.0.2: https://www.omg.org/spec/BPMN/2.0.2/
- diagrams.net: https://www.diagrams.net/
- Netlify-Blobs-Dokumentation: https://docs.netlify.com/build/data-and-storage/netlify-blobs/

**Der Kurs setzt die fachspezifische Vertiefung der UE 2 um und vermittelt noch keine Pools/Lanes, AND-Gateways oder Schleifen.** Diese sind nur in der Legende als Ausblick aufgeführt. Die spätere Vernetzung mit Wirtschaftslehre/Recht bleibt erhalten.

Die fachliche Endprüfung und die Datenschutzfreigabe erfolgen durch die für den Unterricht verantwortliche Lehrkraft. Der KI-Nachweis steht im Footer der Website.
