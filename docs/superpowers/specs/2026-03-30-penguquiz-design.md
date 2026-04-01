# PenguQuiz — Design Specification
**Datum:** 2026-03-30
**Erstellt von:** Mustafa Kömür
**Zielgruppe:** Pflegefachkraft Ausbildung, 3. Lehrjahr (50 Schüler)

---

## 1. Überblick

PenguQuiz ist ein lokales, browserbasiertes Klassenquizspiel mit Penguinmaskottchen. Der Lehrer steuert das Spiel von einem Gerät. Zwei Schüler werden per Glücksrad ausgewählt und treten gegeneinander an — Rotes Team vs. Blaues Team. Fragen sind Patientenszenarien (Pflegefachkraft 3. Lehrjahr, 100% korrekte medizinische Inhalte, vollständig auf Deutsch).

---

## 2. Dateistruktur

```
Fach_Pflege_Game/
├── index.html       ← Hauptspiel (alles inline: HTML + CSS + JS)
├── admin.html       ← Admin-Panel (passwortgeschützt)
└── docs/
    └── superpowers/
        └── specs/
            └── 2026-03-30-penguquiz-design.md
```

Keine externen Abhängigkeiten. Keine Internetverbindung erforderlich. Sounds werden per Web Audio API generiert (kein mp3 nötig).

---

## 3. Datenspeicherung

Alle Daten werden im `localStorage` des Browsers gespeichert:
- `penguquiz_students` — Schülerliste (Array von Namen)
- `penguquiz_questions` — Fragenliste (Array von Objekten)
- `penguquiz_scores` — Aktueller Spielstand
- `penguquiz_used` — Bereits ausgewählte Schüler (damit keine Wiederholung)
- `penguquiz_settings` — Einstellungen (Passwort, Timer, Motivationssätze)

---

## 4. Schülerliste (50 Personen)

1. Alida Kamwa, 2. Ana Galeas, 3. Angele Yvana, 4. Anica Mahler, 5. Arnaud Ntoutou,
6. Atakan Senol, 7. Axinia Erhardt, 8. Bella Chiwaza, 9. Besarta Peci, 10. Cedrick Kana,
11. Charnelle Noume, 12. Christian Wanne, 13. Danielle Maguim, 14. Diura Rustamova,
15. Elvisa Krasniqi, 16. Emilia Kempf, 17. Evrard Berlo, 18. Gina Kacanja,
19. Göksu Yildiz, 20. Gyulben Radosla, 21. Hilary Kenfack, 22. Irina Arendt,
23. Julia Buchmiller, 24. Khusrav Abidov, 25. Laure Miyague, 26. Lea Schäfer,
27. Lian Schnell, 28. Lidiia Holovko, 29. Loubna Diazal, 30. Manuela Nzambo,
31. Maria Carmela, 32. Marie Asley, 33. Mustafa Kömür, 34. Müjde Akbulut,
35. Nadine Benz, 36. Natalie Bloos, 37. Nazife Nur, 38. Olga Jäger,
39. Ottilia Okel, 40. Patricia Damaschke, 41. Petronella Toevs, 42. Sally Tambeline,
43. Sandra Paule, 44. Soline Wokam, 45. Sophia-Theresia, 46. Stephane Talmi,
47. Stéphane Weya, 48. Suzan Kansiray, 49. Vishalini Mohanraj, 50. Yusuf Dernek

---

## 5. Spielablauf (Screen-by-Screen)

### Screen 1 — Willkommen & Regeln
- Großes Pinguin-Maskottchen zentriert
- Spieltitel: **"PenguQuiz 🐧"** (sehr große Schrift)
- Regeln in großer Schrift (von hinten lesbar, min. 28px):
  - Das Rad dreht sich → 2 Schüler werden ausgewählt
  - Rotes Team antwortet zuerst, dann Blaues Team
  - Richtig: +1 Punkt | Falsch: -1 Punkt
  - Zeit: 60 Sekunden pro Frage
- Button: **"Spiel starten"**

### Screen 2 — Glücksrad
- Großes, buntes Rad mit allen verbleibenden Namen als Segmente
- Lehrer drückt **"Drehen!"**
- Rad dreht sich mit Sound + Animation
- Anzeige: **"Jetzt aus dem ROTEN Team:"** → Name wird hervorgehoben, wandert nach links
- Rad dreht sich automatisch erneut
- Anzeige: **"Jetzt aus dem BLAUEN Team:"** → Name wird hervorgehoben

### Screen 3 — Bühnenaufruf
- Großer Text: **"Bitte kommt nach vorne: [Roter Name] & [Blauer Name]"**
- 5-Sekunden-Countdown
- Automatischer Übergang zum Fragebildschirm

### Screen 4 — Frage (Rotes Team zuerst)
- Oben: **"🔴 [Name], du bist dran!"**
- Rechts oben: 60-Sekunden-Countdown (rote Farbe)
- Mitte: Patientenszenario (große Schrift)
- Button: **"Ich bin bereit!"** → Frage erscheint, Timer startet
- 4 Antwortbuttons (A / B / C / D)
- Nach Antwort oder Zeitablauf → Screen 5

### Screen 5 — Ergebnis
- **Richtig:** "Herzlichen Glückwunsch! +1 Punkt 🎉" (grün, Tink-Sound)
- **Falsch:** "Leider falsch! -1 Punkt 😅" + zufälliger Motivationssatz (rot, Dunk-Sound)
- Motivationssätze (zufällig):
  - "Nicht aufgeben, du schaffst das!"
  - "Beim nächsten Mal klappt es!"
  - "Fehler sind der Weg zum Erfolg!"
  - "Du gibst immer dein Bestes!"
  - "Kopf hoch, weiter geht's!"
- Rechts: Live-Scoreboard wird aktualisiert
- Danach: gleicher Ablauf für Blaues Team (Screen 4 → 5)

### Screen 6 — Nächste Runde
- Nach beiden Antworten: Lehrer drückt erneut **"Drehen!"**
- Bereits ausgewählte Namen erscheinen NICHT mehr im Rad
- Ablauf wiederholt sich bis alle Schüler dran waren

### Screen 7 — Finale
- Animation: **"Punkte werden berechnet..."**
- Text: **"Seid ihr aufgeregt? 😄"** (3 Sekunden)
- Konfetti-Animation
- Kazanan takım büyük yazıyla: **"Das ROTE / BLAUE Team gewinnt! 🏆"**
- Gewinnerliste erscheint von oben nach unten (alle Mitglieder des Siegerteams)

---

## 6. Punktestand (Live-Scoreboard)

- Rechte Seite des Bildschirms, immer sichtbar ab Screen 4
- Zeigt: 🔴 Rotes Team: X Punkte | 🔵 Blaues Team: X Punkte
- Aktualisiert sich nach jeder Antwort mit Animation

---

## 7. Sounds (Web Audio API — kein externes File)

| Ereignis | Sound |
|---|---|
| Rad dreht sich | Rauschen / Ticker-Sound |
| Richtige Antwort | Heller "Tink"-Ton |
| Falsche Antwort | Tiefer "Dunk"-Ton |
| Countdown läuft | Leise Hintergrundmusik |
| Gewinner | Fanfare / Jubel-Ton |

---

## 8. Admin-Panel (admin.html)

**Zugang:** Passwortgeschützt (Standard: `admin123`)

**Registerkarte 1 — Fragen:**
- Liste aller Fragen
- Neue Frage hinzufügen: Szenario + 4 Antworten + korrekte Antwort markieren
- Frage bearbeiten / löschen

**Registerkarte 2 — Schüler:**
- Schülerliste anzeigen
- Namen hinzufügen / bearbeiten / löschen

**Registerkarte 3 — Einstellungen:**
- Passwort ändern
- Timer-Dauer ändern (Standard: 60 Sek.)
- Motivationssätze bearbeiten

---

## 9. Design & Theme

- **Hintergrund:** Dunkles Marineblau (`#0a1628`)
- **Schriftfarbe:** Weiß & Gelb
- **Teamfarben:** Rot (`#e74c3c`) & Blau (`#3498db`)
- **Font:** Groß, fett — min. 28px für Spielinhalt, 20px für Nebentexte
- **Pinguin-Maskottchen:** SVG-Pinguin, animiert auf Willkommensscreen und Ergebnisscreen
- **Rad:** Bunte Segmente, goldener Zeiger, flüssige CSS-Animation
- **Footer (alle Seiten):** `"Diese Seite wurde von Mustafa Kömür erstellt 🐧"`

---

## 10. Fragen (30 Patientenszenarien — Pflegefachkraft 3. Lehrjahr)

Alle Fragen sind medizinisch korrekt, auf Deutsch, Niveau 3. Lehrjahr Pflegefachkraft.

### Beispielstruktur:
```json
{
  "szenario": "Herr Müller, 72 Jahre, klagt über plötzlich einsetzende...",
  "antworten": ["A) ...", "B) ...", "C) ...", "D) ..."],
  "korrekt": "A"
}
```

*(Vollständige 30 Fragen werden beim Erstellen des index.html eingebettet)*

---

## 11. Technische Anforderungen

- Reines HTML5 + CSS3 + Vanilla JavaScript
- Keine externen Libraries, kein Internet nötig
- Läuft auf: Chrome, Firefox, Edge, Safari (Desktop & Tablet)
- Responsive für Beamer/Projektor (1920×1080 optimiert)
- localStorage für alle persistenten Daten

---

## 12. Footer

Alle Seiten: `"Diese Seite wurde von Mustafa Kömür erstellt 🐧"`
