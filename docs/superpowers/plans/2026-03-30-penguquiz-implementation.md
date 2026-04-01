# PenguQuiz Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a local browser-based classroom quiz game (PenguQuiz) with a spinning wheel, team competition, patient scenario questions, admin panel, and penguin theme — all in two standalone HTML files.

**Architecture:** Two standalone HTML files (`index.html` for the game, `admin.html` for admin panel), each fully self-contained with inline CSS and JavaScript. All data persisted via `localStorage`. No external dependencies, no internet required.

**Tech Stack:** HTML5, CSS3, Vanilla JavaScript, Web Audio API (for sounds), Canvas API (for spinning wheel), localStorage (for data persistence).

---

## File Structure

| File | Responsibility |
|---|---|
| `index.html` | Complete game: welcome screen, wheel, question flow, scoreboard, finale |
| `admin.html` | Admin panel: manage questions, students, settings |

---

### Task 1: Data Layer & Default Content

**Files:**
- Create: `index.html` (skeleton + data layer only)

- [ ] **Step 1: Create index.html skeleton with data initialization**

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PenguQuiz 🐧</title>
  <style>
    /* styles added in Task 2 */
  </style>
</head>
<body>
<script>
// ============================================================
// DATA LAYER
// ============================================================
const DEFAULT_STUDENTS = [
  "Alida Kamwa","Ana Galeas","Angele Yvana","Anica Mahler","Arnaud Ntoutou",
  "Atakan Senol","Axinia Erhardt","Bella Chiwaza","Besarta Peci","Cedrick Kana",
  "Charnelle Noume","Christian Wanne","Danielle Maguim","Diura Rustamova",
  "Elvisa Krasniqi","Emilia Kempf","Evrard Berlo","Gina Kacanja",
  "Göksu Yildiz","Gyulben Radosla","Hilary Kenfack","Irina Arendt",
  "Julia Buchmiller","Khusrav Abidov","Laure Miyague","Lea Schäfer",
  "Lian Schnell","Lidiia Holovko","Loubna Diazal","Manuela Nzambo",
  "Maria Carmela","Marie Asley","Mustafa Kömür","Müjde Akbulut",
  "Nadine Benz","Natalie Bloos","Nazife Nur","Olga Jäger",
  "Ottilia Okel","Patricia Damaschke","Petronella Toevs","Sally Tambeline",
  "Sandra Paule","Soline Wokam","Sophia-Theresia","Stephane Talmi",
  "Stéphane Weya","Suzan Kansiray","Vishalini Mohanraj","Yusuf Dernek"
];

const DEFAULT_QUESTIONS = [
  {
    szenario: "Ein 68-jähriger Patient klagt über plötzlich einsetzende, einseitige Gesichtsschwäche, hängenden Mundwinkel und Sprachstörungen. Was ist die wahrscheinlichste Diagnose?",
    antworten: ["A) Hypoglykämie", "B) Schlaganfall (Apoplex)", "C) Migräne", "D) Epileptischer Anfall"],
    korrekt: "B"
  },
  {
    szenario: "Eine 75-jährige Patientin zeigt Verwirrtheit, Desorientiertheit und hat Fieber von 38,9°C. Der Urin ist trüb und riecht unangenehm. Was ist die wahrscheinlichste Ursache?",
    antworten: ["A) Demenz-Exazerbation", "B) Harnwegsinfekt (HWI)", "C) Pneumonie", "D) Hypertensive Krise"],
    korrekt: "B"
  },
  {
    szenario: "Herr Schmidt, 80 Jahre, ist seit dem Sturz vor 3 Tagen bettlägerig. Welche Pflegemaßnahme hat höchste Priorität zur Dekubitusprophylaxe?",
    antworten: ["A) Tägliche Ganzkörperwaschung", "B) Regelmäßige Umlagerung alle 2 Stunden", "C) Erhöhte Kalorienzufuhr", "D) Physiotherapie täglich"],
    korrekt: "B"
  },
  {
    szenario: "Eine Patientin mit Diabetes mellitus Typ 2 klagt über Schwitzen, Zittern, Herzrasen und Verwirrtheit. Blutzucker: 2,8 mmol/l. Was ist die Erstmaßnahme?",
    antworten: ["A) Insulin geben", "B) Notarzt rufen und abwarten", "C) Sofort schnell resorbierbare Kohlenhydrate geben", "D) Blutdruck messen"],
    korrekt: "C"
  },
  {
    szenario: "Bei einem 70-jährigen Patienten mit COPD beträgt die Sauerstoffsättigung 88%. Der Arzt verordnet O2-Gabe. Welcher SpO2-Zielwert ist bei COPD-Patienten angemessen?",
    antworten: ["A) 98–100%", "B) 88–92%", "C) 94–96%", "D) 80–85%"],
    korrekt: "B"
  },
  {
    szenario: "Frau Bauer, 65 Jahre, hat eine Herzinsuffizienz NYHA III. Sie klagt über Gewichtszunahme von 2 kg innerhalb von 2 Tagen und Knöchelödeme. Was ist zu tun?",
    antworten: ["A) Flüssigkeitszufuhr erhöhen", "B) Arzt informieren — Gewichtszunahme ist Zeichen einer Dekompensation", "C) Kompressionsstrümpfe anlegen und abwarten", "D) Bettruhe anordnen ohne Arztinformation"],
    korrekt: "B"
  },
  {
    szenario: "Ein Patient erhält Heparin-Therapie. Welcher Laborwert muss regelmäßig kontrolliert werden?",
    antworten: ["A) Blutzucker (BZ)", "B) Kreatinin", "C) aPTT (aktivierte partielle Thromboplastinzeit)", "D) TSH"],
    korrekt: "C"
  },
  {
    szenario: "Eine 82-jährige Bewohnerin mit Alzheimer-Demenz verweigert das Frühstück und ist agitiert. Was ist der erste Schritt?",
    antworten: ["A) Nahrung per Sonde verabreichen", "B) Ruhige, zugewandte Kommunikation, Ursache der Agitation erforschen", "C) Arzt sofort für Sedierung anrufen", "D) Frühstück zwangsweise verabreichen"],
    korrekt: "B"
  },
  {
    szenario: "Welches Zeichen ist ein typisches Frühzeichen eines Druckulkus (Dekubitus Grad I)?",
    antworten: ["A) Offene Wunde mit Nekrose", "B) Nicht wegdrückbare Rötung der intakten Haut", "C) Tiefe Gewebeschädigung mit Knochenbeteiligung", "D) Blasenbildung auf der Haut"],
    korrekt: "B"
  },
  {
    szenario: "Ein Patient mit tiefer Beinvenenthrombose (TVT) klagt über plötzliche Atemnot, Brustschmerzen und Husten. Was ist die gefürchtete Komplikation?",
    antworten: ["A) Herzinfarkt", "B) Lungenembolie", "C) Pneumonie", "D) Pleuraerguss"],
    korrekt: "B"
  },
  {
    szenario: "Frau Müller, 78 Jahre, nimmt Marcumar (Phenprocoumon). Welcher Laborwert kontrolliert die Wirkung?",
    antworten: ["A) INR / Quick-Wert", "B) Hämoglobin", "C) Leukozyten", "D) Kreatinin"],
    korrekt: "A"
  },
  {
    szenario: "Ein bewusstloser Patient atmet nicht. Was ist die korrekte Reihenfolge der Basisreanimation nach ERC-Leitlinie?",
    antworten: ["A) Atemwege freimachen → Beatmung → Herzdruckmassage", "B) Notruf → 30 Herzdruckmassagen → 2 Beatmungen (30:2)", "C) Beatmung → Herzdruckmassage → Notruf", "D) Puls prüfen → Herzdruckmassage → Beatmung"],
    korrekt: "B"
  },
  {
    szenario: "Welches Symptom ist charakteristisch für eine hypertensive Krise (RR > 180/120 mmHg)?",
    antworten: ["A) Bradykardie und Hypotonie", "B) Starke Kopfschmerzen, Sehstörungen, Schwindel", "C) Hypothermie und Bewusstlosigkeit", "D) Blutzuckeranstieg über 300 mg/dl"],
    korrekt: "B"
  },
  {
    szenario: "Ein Patient nach Hüft-TEP soll mobilisiert werden. Was muss bei der Lagerung unbedingt vermieden werden?",
    antworten: ["A) Streckung des Hüftgelenks", "B) Adduktion und Innenrotation der operierten Hüfte", "C) Sitzen auf erhöhtem Stuhl", "D) Gehen mit Gehstützen"],
    korrekt: "B"
  },
  {
    szenario: "Welche Pflege-Intervention gehört zur Sturzprophylaxe bei einem älteren Patienten?",
    antworten: ["A) Bettgitter hochstellen und Patienten zur Ruhe zwingen", "B) Rutschfeste Schuhe, ausreichend Beleuchtung, Klingelanlage in Reichweite", "C) Schlafmittel abends geben damit Patient schläft", "D) Mobilisation komplett vermeiden"],
    korrekt: "B"
  },
  {
    szenario: "Ein Patient mit Niereninsuffizienz hat folgende Laborwerte: Kreatinin 4,2 mg/dl, Kalium 6,1 mmol/l. Was ist die gefährlichste Komplikation der Hyperkaliämie?",
    antworten: ["A) Muskelkrämpfe", "B) Herzrhythmusstörungen bis zum Herzstillstand", "C) Hypertonie", "D) Polyurie"],
    korrekt: "B"
  },
  {
    szenario: "Frau Klein, 70 Jahre, kommt nach einer Gastrektomie (Magenentfernung). Welcher Vitaminmangel tritt langfristig zwingend auf?",
    antworten: ["A) Vitamin C-Mangel", "B) Vitamin D-Mangel", "C) Vitamin B12-Mangel (da Intrinsic Factor fehlt)", "D) Folsäure-Mangel"],
    korrekt: "C"
  },
  {
    szenario: "Welches ist ein typisches Zeichen einer Aspiration bei einem Patienten mit Dysphagie?",
    antworten: ["A) Gewichtszunahme", "B) Husten während oder nach dem Essen, brodelnde Atemgeräusche", "C) Verstopfung", "D) Bradykardie"],
    korrekt: "B"
  },
  {
    szenario: "Ein Patient mit Parkinson-Erkrankung erhält L-Dopa. Was ist eine häufige Nebenwirkung dieser Medikation?",
    antworten: ["A) Hypertonie", "B) Orthostatische Hypotonie (Schwindel beim Aufstehen)", "C) Bradykardie", "D) Gewichtszunahme"],
    korrekt: "B"
  },
  {
    szenario: "Herr Fischer, 55 Jahre, hat einen akuten Myokardinfarkt. Welches Symptom ist typisch?",
    antworten: ["A) Kolikartige Bauchschmerzen", "B) Vernichtungsschmerz in der Brust, ausstrahlend in linken Arm und Kiefer", "C) Fieber über 40°C", "D) Plötzliche Sehverschlechterung"],
    korrekt: "B"
  },
  {
    szenario: "Was bedeutet die Abkürzung 'NRS' im Pflegekontext?",
    antworten: ["A) Nutritional Risk Screening — Instrument zur Erfassung von Mangelernährungsrisiko", "B) Neurologisches Risiko Screening", "C) Notfall-Reaktions-Schema", "D) Nacht-Ruhe-Sicherung"],
    korrekt: "A"
  },
  {
    szenario: "Eine Patientin mit Hypothyreose erhält L-Thyroxin. Wann soll das Medikament eingenommen werden?",
    antworten: ["A) Abends mit dem Abendessen", "B) Morgens nüchtern, 30 Minuten vor dem Frühstück", "C) Zu jeder Mahlzeit", "D) Nur bei Bedarf"],
    korrekt: "B"
  },
  {
    szenario: "Welches Pflegeproblem hat bei einem Patienten mit akutem Herzinfarkt auf der Intensivstation höchste Priorität?",
    antworten: ["A) Ernährungsdefizit", "B") Beeinträchtigte Gewebeperfusion und lebensbedrohliche Herzrhythmusstörungen", "C) Schlafstörungen", "D) Kommunikationsdefizit"],
    korrekt: "B"
  },
  {
    szenario: "Ein Patient hat eine Wunde mit gelblichem, fibrinösem Belag. In welche Wundheilungsphase befindet sich die Wunde?",
    antworten: ["A) Proliferationsphase", "B) Reinigungsphase (Exsudationsphase)", "C) Epithelisierungsphase", "D) Hämostasephase"],
    korrekt: "B"
  },
  {
    szenario: "Frau Weber, 88 Jahre, ist immobil und inkontinent. Welche Maßnahme verhindert am wirksamsten einen Inkontinenz-assoziierten Dermatitis?",
    antworten: ["A) Nur einmal täglich waschen", "B) Haut nach jeder Ausscheidung reinigen, trocknen und mit Barrierecreme schützen", "C) Wundauflage auf die gesamte Gesäßfläche", "D) Dauerkatheter immer legen"],
    korrekt: "B"
  },
  {
    szenario: "Welcher Glasgow Coma Scale (GCS) Wert zeigt eine schwere Bewusstseinsstörung an?",
    antworten: ["A) GCS 15", "B) GCS 12", "C) GCS 8 oder weniger", "D) GCS 10"],
    korrekt: "C"
  },
  {
    szenario: "Ein Patient nach Schlaganfall hat eine Hemiparese rechts. Auf welcher Seite soll die Pflegefachkraft beim Transfer stehen?",
    antworten: ["A) Auf der gesunden (linken) Seite", "B) Hinter dem Patienten", "C) Auf der betroffenen (rechten) Seite", "D) Egal, beide Seiten sind gleichwertig"],
    korrekt: "C"
  },
  {
    szenario: "Was ist das Hauptziel der palliativen Pflege?",
    antworten: ["A) Heilung der Grunderkrankung", "B) Lebensverlängerung durch aggressive Therapie", "C) Bestmögliche Lebensqualität und Symptomkontrolle bei unheilbarer Erkrankung", "D) Vorbereitung auf chirurgische Eingriffe"],
    korrekt: "C"
  },
  {
    szenario: "Ein Patient erhält eine intravenöse Infusion. Die Einstichstelle ist gerötet, geschwollen und der Patient klagt über Schmerzen. Was ist zu tun?",
    antworten: ["A) Infusionsrate reduzieren und weiter beobachten", "B) Infusion sofort stoppen, Venenverweilkanüle entfernen, Arzt informieren", "C) Warme Kompresse anlegen und weiterinfundieren", "D) Analgetikum geben und abwarten"],
    korrekt: "B"
  },
  {
    szenario: "Welche Maßnahme ist bei der Pflege eines Patienten mit MRSA zwingend erforderlich?",
    antworten: ["A) Normales Händewaschen reicht aus", "B) Kontaktisolation: Schutzkleidung (Kittel, Handschuhe, Maske), Einzelzimmer, hygienische Händedesinfektion", "C) Patient muss im Krankenhaus bleiben bis MRSA weg ist", "D) Antibiotikaprophylaxe für alle Pflegenden"],
    korrekt: "B"
  }
];

const DEFAULT_SETTINGS = {
  password: "admin123",
  timerSeconds: 60,
  motivationMessages: [
    "Nicht aufgeben, du schaffst das!",
    "Beim nächsten Mal klappt es bestimmt!",
    "Fehler sind der Weg zum Erfolg!",
    "Du gibst immer dein Bestes!",
    "Kopf hoch, weiter geht's!",
    "Das war knapp, aber du lernst daraus!",
    "Bleib stark, du bist auf dem richtigen Weg!"
  ]
};

function initData() {
  if (!localStorage.getItem('penguquiz_students')) {
    localStorage.setItem('penguquiz_students', JSON.stringify(DEFAULT_STUDENTS));
  }
  if (!localStorage.getItem('penguquiz_questions')) {
    localStorage.setItem('penguquiz_questions', JSON.stringify(DEFAULT_QUESTIONS));
  }
  if (!localStorage.getItem('penguquiz_settings')) {
    localStorage.setItem('penguquiz_settings', JSON.stringify(DEFAULT_SETTINGS));
  }
}

function getStudents() { return JSON.parse(localStorage.getItem('penguquiz_students')); }
function getQuestions() { return JSON.parse(localStorage.getItem('penguquiz_questions')); }
function getSettings() { return JSON.parse(localStorage.getItem('penguquiz_settings')); }

initData();
</script>
</body>
</html>
```

- [ ] **Step 2: Verify data loads correctly**

Open `index.html` in browser, open DevTools Console, run:
```js
console.log(JSON.parse(localStorage.getItem('penguquiz_students')).length); // → 50
console.log(JSON.parse(localStorage.getItem('penguquiz_questions')).length); // → 30
```
Expected: 50 and 30

- [ ] **Step 3: Commit**
```bash
git init
git add index.html
git commit -m "feat: add data layer with 50 students and 30 questions"
```

---

### Task 2: Global Styles & Theme

**Files:**
- Modify: `index.html` — fill in the `<style>` block

- [ ] **Step 1: Add global CSS inside the `<style>` tag**

Replace `/* styles added in Task 2 */` with:

```css
* { margin: 0; padding: 0; box-sizing: border-box; }

:root {
  --bg: #0a1628;
  --bg2: #0f2040;
  --card: #162035;
  --red: #e74c3c;
  --blue: #3498db;
  --gold: #f1c40f;
  --green: #2ecc71;
  --white: #ffffff;
  --gray: #8899aa;
  --font-xl: clamp(2rem, 5vw, 4rem);
  --font-lg: clamp(1.4rem, 3vw, 2.4rem);
  --font-md: clamp(1.1rem, 2.2vw, 1.8rem);
  --font-sm: clamp(0.9rem, 1.5vw, 1.3rem);
}

body {
  background: var(--bg);
  color: var(--white);
  font-family: 'Segoe UI', Arial, sans-serif;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.screen {
  display: none;
  flex: 1;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  min-height: 100vh;
  animation: fadeIn 0.4s ease;
}
.screen.active { display: flex; }

@keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

.btn {
  background: var(--gold);
  color: var(--bg);
  border: none;
  padding: 1rem 2.5rem;
  font-size: var(--font-md);
  font-weight: 800;
  border-radius: 50px;
  cursor: pointer;
  transition: transform 0.15s, box-shadow 0.15s;
  box-shadow: 0 4px 20px rgba(241,196,15,0.4);
}
.btn:hover { transform: scale(1.05); box-shadow: 0 6px 28px rgba(241,196,15,0.6); }
.btn:active { transform: scale(0.97); }
.btn.red { background: var(--red); color: white; box-shadow: 0 4px 20px rgba(231,76,60,0.4); }
.btn.blue { background: var(--blue); color: white; box-shadow: 0 4px 20px rgba(52,152,219,0.4); }
.btn.green { background: var(--green); color: white; box-shadow: 0 4px 20px rgba(46,204,113,0.4); }

.penguin-svg { width: 120px; height: 120px; }
.penguin-lg { width: 200px; height: 200px; }

.tag-red { color: var(--red); font-weight: 800; }
.tag-blue { color: var(--blue); font-weight: 800; }

.scoreboard {
  position: fixed;
  right: 1.5rem;
  top: 50%;
  transform: translateY(-50%);
  background: var(--card);
  border-radius: 16px;
  padding: 1.2rem 1.8rem;
  text-align: center;
  border: 2px solid var(--gold);
  min-width: 140px;
  z-index: 100;
}
.scoreboard h3 { font-size: var(--font-sm); color: var(--gold); margin-bottom: 0.8rem; }
.score-red { font-size: var(--font-lg); color: var(--red); font-weight: 900; }
.score-blue { font-size: var(--font-lg); color: var(--blue); font-weight: 900; margin-top: 0.5rem; }
.score-label { font-size: 0.9rem; color: var(--gray); }

footer {
  text-align: center;
  padding: 0.8rem;
  color: var(--gray);
  font-size: 0.85rem;
  background: var(--bg2);
}

/* Timer */
.timer-ring { position: relative; width: 90px; height: 90px; }
.timer-text { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); font-size: 1.8rem; font-weight: 900; }
.timer-urgent { color: var(--red); animation: pulse 0.5s infinite alternate; }
@keyframes pulse { from { transform: translate(-50%,-50%) scale(1); } to { transform: translate(-50%,-50%) scale(1.15); } }

/* Answer buttons */
.answer-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; width: 100%; max-width: 800px; margin-top: 1.5rem; }
.answer-btn {
  background: var(--card);
  border: 2px solid var(--gray);
  color: var(--white);
  padding: 1.2rem;
  font-size: var(--font-sm);
  font-weight: 600;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s;
  text-align: left;
}
.answer-btn:hover { border-color: var(--gold); background: #1e3050; }
.answer-btn.correct { background: #1a5c30; border-color: var(--green); }
.answer-btn.wrong { background: #5c1a1a; border-color: var(--red); }

/* Confetti */
.confetti-piece {
  position: fixed;
  width: 10px;
  height: 10px;
  border-radius: 2px;
  animation: confettiFall linear forwards;
  z-index: 999;
}
@keyframes confettiFall {
  0% { transform: translateY(-10px) rotate(0deg); opacity: 1; }
  100% { transform: translateY(110vh) rotate(720deg); opacity: 0; }
}
```

- [ ] **Step 2: Add the penguin SVG function and footer to the script**

Add before `initData()` call:

```js
function penguinSVG(size='normal') {
  const cls = size === 'large' ? 'penguin-lg' : 'penguin-svg';
  return `<svg class="${cls}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <ellipse cx="50" cy="62" rx="28" ry="32" fill="#1a1a2e"/>
    <ellipse cx="50" cy="65" rx="18" ry="22" fill="white"/>
    <circle cx="50" cy="28" r="22" fill="#1a1a2e"/>
    <circle cx="43" cy="24" r="5" fill="white"/>
    <circle cx="57" cy="24" r="5" fill="white"/>
    <circle cx="44" cy="25" r="3" fill="#1a1a2e"/>
    <circle cx="58" cy="25" r="3" fill="#1a1a2e"/>
    <ellipse cx="50" cy="33" rx="5" ry="3" fill="#f1c40f"/>
    <ellipse cx="30" cy="60" rx="8" ry="18" fill="#1a1a2e" transform="rotate(15,30,60)"/>
    <ellipse cx="70" cy="60" rx="8" ry="18" fill="#1a1a2e" transform="rotate(-15,70,60)"/>
    <ellipse cx="40" cy="90" rx="8" ry="5" fill="#f1c40f"/>
    <ellipse cx="60" cy="90" rx="8" ry="5" fill="#f1c40f"/>
  </svg>`;
}

document.addEventListener('DOMContentLoaded', () => {
  document.body.insertAdjacentHTML('beforeend',
    `<footer>Diese Seite wurde von Mustafa Kömür erstellt 🐧</footer>`);
});
```

- [ ] **Step 3: Verify styles load**

Open in browser — page should show dark navy background, no errors in console.

- [ ] **Step 4: Commit**
```bash
git add index.html
git commit -m "feat: add global theme styles and penguin SVG"
```

---

### Task 3: Screen Manager & Welcome Screen

**Files:**
- Modify: `index.html` — add HTML screens + screen navigation

- [ ] **Step 1: Add screen HTML inside `<body>` before `<script>`**

```html
<!-- SCREEN 1: Welcome -->
<div id="screen-welcome" class="screen active">
  <div id="penguin-welcome"></div>
  <h1 style="font-size:var(--font-xl);margin:1rem 0;text-shadow:0 0 30px rgba(241,196,15,0.5)">PenguQuiz 🐧</h1>
  <div style="background:var(--card);border-radius:20px;padding:2rem 3rem;max-width:700px;width:100%;margin:1rem 0;border:1px solid var(--gold)">
    <h2 style="font-size:var(--font-lg);color:var(--gold);margin-bottom:1.5rem;text-align:center">Spielregeln</h2>
    <ul style="font-size:var(--font-md);line-height:2.2;list-style:none;">
      <li>🎡 Das Rad dreht sich → 2 Schüler werden ausgewählt</li>
      <li>🔴 Rotes Team antwortet zuerst</li>
      <li>🔵 Blaues Team antwortet danach</li>
      <li>✅ Richtige Antwort: <strong style="color:var(--green)">+1 Punkt</strong></li>
      <li>❌ Falsche Antwort: <strong style="color:var(--red)">−1 Punkt</strong></li>
      <li>⏱️ Zeit pro Frage: <strong style="color:var(--gold)">60 Sekunden</strong></li>
    </ul>
  </div>
  <button class="btn" onclick="showScreen('screen-wheel')">Spiel starten 🚀</button>
</div>

<!-- SCREEN 2: Wheel -->
<div id="screen-wheel" class="screen">
  <h2 style="font-size:var(--font-lg);margin-bottom:1rem">🎡 Glücksrad</h2>
  <div style="position:relative;display:inline-block">
    <canvas id="wheel-canvas" width="500" height="500"></canvas>
    <div id="wheel-pointer" style="position:absolute;top:-10px;left:50%;transform:translateX(-50%);font-size:3rem">▼</div>
  </div>
  <div id="wheel-announcement" style="font-size:var(--font-lg);margin:1.5rem 0;min-height:3rem;text-align:center"></div>
  <button id="btn-spin" class="btn" onclick="spinWheel()">Drehen! 🎯</button>
</div>

<!-- SCREEN 3: Stage Call -->
<div id="screen-stage" class="screen">
  <div id="stage-penguin"></div>
  <h1 id="stage-title" style="font-size:var(--font-xl);text-align:center;margin:1rem 0"></h1>
  <div id="stage-countdown" style="font-size:var(--font-xl);color:var(--gold);font-weight:900"></div>
</div>

<!-- SCREEN 4: Question -->
<div id="screen-question" class="screen" style="align-items:flex-start;padding:2rem 6rem 2rem 2rem">
  <div style="display:flex;align-items:center;gap:1rem;margin-bottom:1rem;width:100%">
    <div id="q-team-badge" style="padding:0.5rem 1.5rem;border-radius:50px;font-size:var(--font-md);font-weight:900"></div>
    <div id="q-player-name" style="font-size:var(--font-lg);font-weight:800"></div>
    <div style="margin-left:auto">
      <svg id="timer-svg" width="90" height="90">
        <circle cx="45" cy="45" r="38" fill="none" stroke="#162035" stroke-width="8"/>
        <circle id="timer-arc" cx="45" cy="45" r="38" fill="none" stroke="#f1c40f" stroke-width="8"
          stroke-dasharray="239" stroke-dashoffset="0" stroke-linecap="round"
          transform="rotate(-90 45 45)"/>
      </svg>
      <div id="timer-text" class="timer-text" style="position:relative;top:-65px;left:0;text-align:center"></div>
    </div>
  </div>
  <div id="q-scenario" style="font-size:var(--font-md);background:var(--card);border-radius:16px;padding:1.5rem;width:100%;max-width:900px;line-height:1.7;margin-bottom:1rem;border-left:5px solid var(--gold)"></div>
  <div id="q-ready-area" style="width:100%;max-width:900px">
    <button class="btn" onclick="startQuestion()">Ich bin bereit! ✋</button>
  </div>
  <div id="q-answers" class="answer-grid" style="display:none;max-width:900px"></div>
</div>

<!-- SCREEN 5: Result -->
<div id="screen-result" class="screen">
  <div id="result-penguin"></div>
  <div id="result-icon" style="font-size:6rem"></div>
  <h2 id="result-title" style="font-size:var(--font-xl);margin:0.5rem 0"></h2>
  <div id="result-points" style="font-size:var(--font-lg);font-weight:900;margin-bottom:1rem"></div>
  <div id="result-motivation" style="font-size:var(--font-md);color:var(--gray);font-style:italic;max-width:500px;text-align:center"></div>
  <button id="btn-result-next" class="btn" style="margin-top:2rem" onclick="resultNext()">Weiter ➡️</button>
</div>

<!-- SCREEN 6: Final -->
<div id="screen-final" class="screen">
  <div id="final-content" style="text-align:center"></div>
</div>

<!-- Live Scoreboard (hidden until game starts) -->
<div id="scoreboard" class="scoreboard" style="display:none">
  <h3>PUNKTE</h3>
  <div class="score-red" id="score-red-val">0</div>
  <div class="score-label">🔴 Rot</div>
  <div class="score-blue" id="score-blue-val">0</div>
  <div class="score-label">🔵 Blau</div>
</div>
```

- [ ] **Step 2: Add screen navigation function to script**

Add after `initData()` call:

```js
function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
}

// Init penguin on welcome
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('penguin-welcome').innerHTML = penguinSVG('large');
  document.getElementById('stage-penguin').innerHTML = penguinSVG('large');
  document.getElementById('result-penguin').innerHTML = penguinSVG();
});
```

- [ ] **Step 3: Verify welcome screen renders**

Open browser → should see navy background, penguin, rules, "Spiel starten" button.

- [ ] **Step 4: Commit**
```bash
git add index.html
git commit -m "feat: add all screens and screen navigation"
```

---

### Task 4: Spinning Wheel

**Files:**
- Modify: `index.html` — add wheel drawing and spin logic

- [ ] **Step 1: Add wheel state variables to script**

Add after `initData()`:

```js
// WHEEL STATE
let wheelStudents = [];       // remaining students (not yet picked)
let usedStudents = [];        // already used this session
let currentRed = null;
let currentBlue = null;
let wheelSpinning = false;
let wheelAngle = 0;
let wheelPhase = 0; // 0=pick red, 1=pick blue
let wheelColors = [
  '#e74c3c','#3498db','#2ecc71','#f39c12','#9b59b6',
  '#1abc9c','#e67e22','#e91e63','#00bcd4','#8bc34a'
];

function resetWheelSession() {
  wheelStudents = getStudents().filter(s => !usedStudents.includes(s));
  wheelAngle = 0;
  wheelPhase = 0;
  currentRed = null;
  currentBlue = null;
  document.getElementById('wheel-announcement').textContent = '';
  document.getElementById('btn-spin').disabled = false;
  drawWheel();
}
```

- [ ] **Step 2: Add drawWheel function**

```js
function drawWheel() {
  const canvas = document.getElementById('wheel-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const cx = 250, cy = 250, r = 230;
  const students = wheelStudents.length > 0 ? wheelStudents : ['Keine Schüler'];
  const sliceAngle = (2 * Math.PI) / students.length;

  ctx.clearRect(0, 0, 500, 500);

  students.forEach((name, i) => {
    const start = wheelAngle + i * sliceAngle;
    const end = start + sliceAngle;
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.arc(cx, cy, r, start, end);
    ctx.closePath();
    ctx.fillStyle = wheelColors[i % wheelColors.length];
    ctx.fill();
    ctx.strokeStyle = '#0a1628';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Text
    ctx.save();
    ctx.translate(cx, cy);
    ctx.rotate(start + sliceAngle / 2);
    ctx.textAlign = 'right';
    ctx.fillStyle = 'white';
    ctx.font = `bold ${Math.max(10, Math.min(16, 200/students.length))}px Segoe UI`;
    ctx.shadowColor = 'rgba(0,0,0,0.8)';
    ctx.shadowBlur = 4;
    ctx.fillText(name, r - 10, 5);
    ctx.restore();
  });

  // Center circle
  ctx.beginPath();
  ctx.arc(cx, cy, 30, 0, 2*Math.PI);
  ctx.fillStyle = '#0a1628';
  ctx.fill();
  ctx.strokeStyle = '#f1c40f';
  ctx.lineWidth = 3;
  ctx.stroke();
}
```

- [ ] **Step 3: Add spinWheel function**

```js
function spinWheel() {
  if (wheelSpinning || wheelStudents.length === 0) return;
  wheelSpinning = true;
  document.getElementById('btn-spin').disabled = true;
  document.getElementById('wheel-announcement').textContent = '';

  playSound('spin');

  const totalRotation = (Math.PI * 2 * (5 + Math.random() * 5)); // 5-10 full rotations
  const duration = 4000;
  const start = performance.now();
  const startAngle = wheelAngle;

  function animate(now) {
    const elapsed = now - start;
    const t = Math.min(elapsed / duration, 1);
    const ease = 1 - Math.pow(1 - t, 4); // ease-out quartic
    wheelAngle = startAngle + totalRotation * ease;
    drawWheel();

    if (t < 1) {
      requestAnimationFrame(animate);
    } else {
      wheelSpinning = false;
      resolveWheelResult();
    }
  }
  requestAnimationFrame(animate);
}

function resolveWheelResult() {
  // Pointer is at top (angle = -PI/2 from center)
  // Find which segment is at the top
  const students = wheelStudents;
  const sliceAngle = (2 * Math.PI) / students.length;
  // Normalize angle
  let a = ((-wheelAngle % (2*Math.PI)) + 2*Math.PI) % (2*Math.PI);
  const idx = Math.floor(a / sliceAngle) % students.length;
  const selected = students[idx];

  if (wheelPhase === 0) {
    currentRed = selected;
    wheelStudents = wheelStudents.filter(s => s !== selected);
    usedStudents.push(selected);
    const ann = document.getElementById('wheel-announcement');
    ann.innerHTML = `Jetzt aus dem <span class="tag-red">ROTEN Team</span>: <strong style="font-size:1.4em">${selected}</strong>`;
    wheelPhase = 1;
    // Auto-spin after 1.5s for blue
    setTimeout(() => {
      if (wheelStudents.length > 0) spinWheel();
    }, 1500);
  } else {
    currentBlue = selected;
    wheelStudents = wheelStudents.filter(s => s !== selected);
    usedStudents.push(selected);
    const ann = document.getElementById('wheel-announcement');
    ann.innerHTML = `<span class="tag-red">🔴 ${currentRed}</span> &nbsp;vs&nbsp; <span class="tag-blue">🔵 ${currentBlue}</span>`;
    wheelPhase = 2;
    document.getElementById('btn-spin').textContent = 'Bühne frei! 🎤';
    document.getElementById('btn-spin').disabled = false;
    document.getElementById('btn-spin').onclick = goToStage;
  }
}
```

- [ ] **Step 4: Init wheel on screen show**

Add to `DOMContentLoaded`:
```js
document.querySelector('[onclick="showScreen(\'screen-wheel\')"]').addEventListener('click', () => {
  resetWheelSession();
});
```

- [ ] **Step 5: Verify wheel spins and selects 2 names**

Open browser → Spiel starten → Drehen → wheel should spin, announce red name, auto-spin again, announce blue name.

- [ ] **Step 6: Commit**
```bash
git add index.html
git commit -m "feat: add spinning wheel with auto red/blue selection"
```

---

### Task 5: Stage Call, Question & Timer

**Files:**
- Modify: `index.html` — stage screen, question display, 60s timer

- [ ] **Step 1: Add goToStage and stage countdown**

```js
function goToStage() {
  document.getElementById('stage-title').innerHTML =
    `Bitte kommt nach vorne:<br><span class="tag-red">🔴 ${currentRed}</span> &amp; <span class="tag-blue">🔵 ${currentBlue}</span>`;
  showScreen('screen-stage');
  document.getElementById('scoreboard').style.display = 'block';

  let count = 5;
  document.getElementById('stage-countdown').textContent = count;
  const interval = setInterval(() => {
    count--;
    if (count > 0) {
      document.getElementById('stage-countdown').textContent = count;
    } else {
      clearInterval(interval);
      startTurn('red');
    }
  }, 1000);
}
```

- [ ] **Step 2: Add game state and startTurn**

```js
// GAME STATE
let scores = { red: 0, blue: 0 };
let currentTurn = 'red'; // 'red' or 'blue'
let currentQuestion = null;
let timerInterval = null;
let timerSeconds = 60;
let questionAnswered = false;

function getRandomQuestion() {
  const questions = getQuestions();
  return questions[Math.floor(Math.random() * questions.length)];
}

function startTurn(team) {
  currentTurn = team;
  currentQuestion = getRandomQuestion();
  questionAnswered = false;

  const name = team === 'red' ? currentRed : currentBlue;
  const color = team === 'red' ? 'var(--red)' : 'var(--blue)';
  const label = team === 'red' ? '🔴 ROTES TEAM' : '🔵 BLAUES TEAM';

  const badge = document.getElementById('q-team-badge');
  badge.textContent = label;
  badge.style.background = color;
  badge.style.color = 'white';

  document.getElementById('q-player-name').textContent = name;
  document.getElementById('q-scenario').textContent = currentQuestion.szenario;
  document.getElementById('q-ready-area').style.display = 'block';
  document.getElementById('q-answers').style.display = 'none';
  document.getElementById('timer-text').textContent = '';
  document.getElementById('timer-arc').style.strokeDashoffset = '0';

  showScreen('screen-question');
}

function startQuestion() {
  document.getElementById('q-ready-area').style.display = 'none';
  const answersDiv = document.getElementById('q-answers');
  answersDiv.style.display = 'grid';
  answersDiv.innerHTML = currentQuestion.antworten.map((a, i) => {
    const letter = ['A','B','C','D'][i];
    return `<button class="answer-btn" onclick="submitAnswer('${letter}')">${a}</button>`;
  }).join('');

  // Start timer
  timerSeconds = getSettings().timerSeconds;
  updateTimerDisplay(timerSeconds);
  timerInterval = setInterval(() => {
    timerSeconds--;
    updateTimerDisplay(timerSeconds);
    if (timerSeconds <= 0) {
      clearInterval(timerInterval);
      submitAnswer(null); // time out
    }
  }, 1000);
}

function updateTimerDisplay(secs) {
  const total = getSettings().timerSeconds;
  const frac = secs / total;
  const circ = 239;
  document.getElementById('timer-arc').style.strokeDashoffset = circ * (1 - frac);
  document.getElementById('timer-arc').style.stroke = secs <= 10 ? '#e74c3c' : '#f1c40f';
  const el = document.getElementById('timer-text');
  el.textContent = secs;
  el.style.color = secs <= 10 ? '#e74c3c' : 'white';
  if (secs <= 10) el.classList.add('timer-urgent'); else el.classList.remove('timer-urgent');
}
```

- [ ] **Step 3: Add submitAnswer**

```js
function submitAnswer(letter) {
  if (questionAnswered) return;
  questionAnswered = true;
  clearInterval(timerInterval);

  // Disable all answer buttons
  document.querySelectorAll('.answer-btn').forEach((btn, i) => {
    const l = ['A','B','C','D'][i];
    btn.disabled = true;
    if (l === currentQuestion.korrekt) btn.classList.add('correct');
    else if (l === letter) btn.classList.add('wrong');
  });

  const correct = letter === currentQuestion.korrekt;

  setTimeout(() => showResult(correct), 800);
}

function showResult(correct) {
  const name = currentTurn === 'red' ? currentRed : currentBlue;

  if (correct) {
    scores[currentTurn]++;
    document.getElementById('result-icon').textContent = '🎉';
    document.getElementById('result-title').innerHTML = `<span style="color:var(--green)">Herzlichen Glückwunsch!</span>`;
    document.getElementById('result-points').innerHTML = `<span style="color:var(--green)">+1 Punkt für ${name}</span>`;
    document.getElementById('result-motivation').textContent = '';
    playSound('correct');
  } else {
    scores[currentTurn]--;
    const msgs = getSettings().motivationMessages;
    const msg = msgs[Math.floor(Math.random() * msgs.length)];
    document.getElementById('result-icon').textContent = '😅';
    document.getElementById('result-title').innerHTML = `<span style="color:var(--red)">Leider falsch!</span>`;
    document.getElementById('result-points').innerHTML = `<span style="color:var(--red)">−1 Punkt für ${name}</span>`;
    document.getElementById('result-motivation').textContent = msg;
    playSound('wrong');
  }

  updateScoreboard();
  document.getElementById('btn-result-next').dataset.next = currentTurn === 'red' ? 'blue' : 'done';
  showScreen('screen-result');
}

function resultNext() {
  const next = document.getElementById('btn-result-next').dataset.next;
  if (next === 'blue') {
    startTurn('blue');
  } else {
    // Both done — check if more students remain
    if (usedStudents.length < getStudents().length - 1) {
      // Reset wheel for next round (keep scores, keep usedStudents)
      wheelStudents = getStudents().filter(s => !usedStudents.includes(s));
      wheelPhase = 0;
      currentRed = null;
      currentBlue = null;
      document.getElementById('btn-spin').textContent = 'Drehen! 🎯';
      document.getElementById('btn-spin').onclick = spinWheel;
      document.getElementById('wheel-announcement').textContent = '';
      drawWheel();
      document.getElementById('scoreboard').style.display = 'block';
      showScreen('screen-wheel');
    } else {
      showFinal();
    }
  }
}

function updateScoreboard() {
  document.getElementById('score-red-val').textContent = scores.red;
  document.getElementById('score-blue-val').textContent = scores.blue;
}
```

- [ ] **Step 4: Verify question flow**

Open browser → Spiel starten → Drehen (×2) → Bühne frei → countdown → Kırmızı turn → Ich bin bereit → answer → result → Blau turn → result → back to wheel.

- [ ] **Step 5: Commit**
```bash
git add index.html
git commit -m "feat: add question flow, timer, scoring, and result screens"
```

---

### Task 6: Final Screen & Confetti

**Files:**
- Modify: `index.html` — finale with winner reveal and confetti

- [ ] **Step 1: Add showFinal and confetti**

```js
function showFinal() {
  document.getElementById('scoreboard').style.display = 'none';
  showScreen('screen-final');

  const content = document.getElementById('final-content');
  content.innerHTML = `<h2 style="font-size:var(--font-xl);color:var(--gold)">Punkte werden berechnet... ⚙️</h2>`;

  setTimeout(() => {
    content.innerHTML = `<h2 style="font-size:var(--font-xl)">Seid ihr aufgeregt? 😄</h2>`;
  }, 2000);

  setTimeout(() => {
    const winner = scores.red > scores.blue ? 'red' : scores.blue > scores.red ? 'blue' : 'draw';
    launchConfetti();
    playSound('fanfare');

    let html = '';
    if (winner === 'draw') {
      html = `<h1 style="font-size:var(--font-xl);color:var(--gold)">🤝 Unentschieden!</h1>
              <p style="font-size:var(--font-md);margin-top:1rem">Beide Teams: ${scores.red} Punkte</p>`;
    } else {
      const wColor = winner === 'red' ? 'var(--red)' : 'var(--blue)';
      const wLabel = winner === 'red' ? '🔴 ROTES TEAM' : '🔵 BLAUES TEAM';
      const wScore = winner === 'red' ? scores.red : scores.blue;
      html = `<h1 style="font-size:var(--font-xl);color:${wColor}">${wLabel} GEWINNT! 🏆</h1>
              <p style="font-size:var(--font-lg);color:${wColor};font-weight:900;margin:0.5rem 0">${wScore} Punkte</p>
              <p style="font-size:var(--font-md);color:var(--gray);margin-bottom:1.5rem">vs. ${winner==='red'?scores.blue:scores.red} Punkte</p>`;
    }
    html += `<button class="btn" onclick="resetGame()" style="margin-top:1.5rem">Neues Spiel 🔄</button>`;
    content.innerHTML = html;
  }, 4500);
}

function launchConfetti() {
  const colors = ['#e74c3c','#3498db','#f1c40f','#2ecc71','#9b59b6','#e67e22'];
  for (let i = 0; i < 120; i++) {
    setTimeout(() => {
      const el = document.createElement('div');
      el.className = 'confetti-piece';
      el.style.left = Math.random() * 100 + 'vw';
      el.style.background = colors[Math.floor(Math.random() * colors.length)];
      el.style.animationDuration = (2 + Math.random() * 3) + 's';
      el.style.animationDelay = '0s';
      el.style.borderRadius = Math.random() > 0.5 ? '50%' : '2px';
      document.body.appendChild(el);
      setTimeout(() => el.remove(), 5000);
    }, Math.random() * 2000);
  }
}

function resetGame() {
  scores = { red: 0, blue: 0 };
  usedStudents = [];
  updateScoreboard();
  document.getElementById('scoreboard').style.display = 'none';
  resetWheelSession();
  showScreen('screen-welcome');
}
```

- [ ] **Step 2: Verify final screen**

Play through a round to the end → final screen should show calculating → excitement → winner with confetti.

- [ ] **Step 3: Commit**
```bash
git add index.html
git commit -m "feat: add final screen with winner reveal and confetti"
```

---

### Task 7: Web Audio Sounds

**Files:**
- Modify: `index.html` — add playSound() using Web Audio API

- [ ] **Step 1: Add sound engine**

Add to script (before `initData()`):

```js
const AudioCtx = window.AudioContext || window.webkitAudioContext;
let audioCtx = null;

function getAudioCtx() {
  if (!audioCtx) audioCtx = new AudioCtx();
  return audioCtx;
}

function playSound(type) {
  try {
    const ctx = getAudioCtx();
    const now = ctx.currentTime;

    if (type === 'spin') {
      // Rapid ticking
      for (let i = 0; i < 30; i++) {
        const o = ctx.createOscillator();
        const g = ctx.createGain();
        o.connect(g); g.connect(ctx.destination);
        o.frequency.value = 800 + Math.random() * 400;
        o.type = 'square';
        g.gain.setValueAtTime(0.08, now + i * 0.13);
        g.gain.exponentialRampToValueAtTime(0.001, now + i * 0.13 + 0.1);
        o.start(now + i * 0.13);
        o.stop(now + i * 0.13 + 0.1);
      }
    } else if (type === 'correct') {
      // Bright ascending ding
      [523, 659, 784, 1047].forEach((freq, i) => {
        const o = ctx.createOscillator();
        const g = ctx.createGain();
        o.connect(g); g.connect(ctx.destination);
        o.frequency.value = freq;
        o.type = 'sine';
        g.gain.setValueAtTime(0.3, now + i * 0.12);
        g.gain.exponentialRampToValueAtTime(0.001, now + i * 0.12 + 0.4);
        o.start(now + i * 0.12);
        o.stop(now + i * 0.12 + 0.4);
      });
    } else if (type === 'wrong') {
      // Low dunk
      [200, 150].forEach((freq, i) => {
        const o = ctx.createOscillator();
        const g = ctx.createGain();
        o.connect(g); g.connect(ctx.destination);
        o.frequency.value = freq;
        o.type = 'sawtooth';
        g.gain.setValueAtTime(0.3, now + i * 0.2);
        g.gain.exponentialRampToValueAtTime(0.001, now + i * 0.2 + 0.4);
        o.start(now + i * 0.2);
        o.stop(now + i * 0.2 + 0.5);
      });
    } else if (type === 'fanfare') {
      // Victory fanfare
      const melody = [523,523,523,415,523,0,659,0,784];
      melody.forEach((freq, i) => {
        if (!freq) return;
        const o = ctx.createOscillator();
        const g = ctx.createGain();
        o.connect(g); g.connect(ctx.destination);
        o.frequency.value = freq;
        o.type = 'square';
        g.gain.setValueAtTime(0.2, now + i * 0.18);
        g.gain.exponentialRampToValueAtTime(0.001, now + i * 0.18 + 0.3);
        o.start(now + i * 0.18);
        o.stop(now + i * 0.18 + 0.3);
      });
    }
  } catch(e) { /* silent fail */ }
}
```

- [ ] **Step 2: Verify sounds**

Test each trigger — spin button, correct answer, wrong answer, and let the game reach finale.

- [ ] **Step 3: Commit**
```bash
git add index.html
git commit -m "feat: add web audio sounds for spin, correct, wrong, fanfare"
```

---

### Task 8: Admin Panel (admin.html)

**Files:**
- Create: `admin.html`

- [ ] **Step 1: Create admin.html**

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PenguQuiz Admin 🐧</title>
  <style>
    * { margin:0; padding:0; box-sizing:border-box; }
    body { background:#0a1628; color:white; font-family:'Segoe UI',Arial,sans-serif; min-height:100vh; }
    .login-screen { display:flex; flex-direction:column; align-items:center; justify-content:center; min-height:100vh; gap:1rem; }
    .login-screen h1 { font-size:2.5rem; color:#f1c40f; }
    input[type=password], input[type=text], textarea {
      background:#162035; border:2px solid #8899aa; color:white; padding:0.8rem 1rem;
      border-radius:8px; font-size:1rem; width:100%; outline:none;
      font-family:'Segoe UI',Arial,sans-serif;
    }
    input:focus, textarea:focus { border-color:#f1c40f; }
    .btn { background:#f1c40f; color:#0a1628; border:none; padding:0.8rem 2rem; font-size:1rem;
           font-weight:800; border-radius:50px; cursor:pointer; transition:transform 0.15s; }
    .btn:hover { transform:scale(1.04); }
    .btn.danger { background:#e74c3c; color:white; }
    .btn.success { background:#2ecc71; color:white; }
    .btn.sm { padding:0.4rem 1rem; font-size:0.85rem; }
    .admin-layout { display:none; flex-direction:column; min-height:100vh; }
    .admin-layout.active { display:flex; }
    .topbar { background:#0f2040; padding:1rem 2rem; display:flex; align-items:center; gap:1rem; border-bottom:2px solid #f1c40f; }
    .topbar h1 { font-size:1.5rem; color:#f1c40f; flex:1; }
    .tabs { display:flex; gap:0.5rem; }
    .tab { background:#162035; border:2px solid #8899aa; color:white; padding:0.6rem 1.5rem;
           border-radius:8px; cursor:pointer; font-size:1rem; font-weight:600; transition:all 0.2s; }
    .tab.active { background:#f1c40f; color:#0a1628; border-color:#f1c40f; }
    .content { flex:1; padding:2rem; }
    .panel { display:none; }
    .panel.active { display:block; }
    .card { background:#162035; border-radius:12px; padding:1.5rem; margin-bottom:1rem; border:1px solid #1e3050; }
    .card h3 { color:#f1c40f; margin-bottom:1rem; font-size:1.1rem; }
    .question-item { background:#0f2040; border-radius:8px; padding:1rem; margin-bottom:0.8rem; border-left:4px solid #f1c40f; }
    .question-item p { font-size:0.9rem; color:#ccc; margin-bottom:0.5rem; }
    .question-item .answers { font-size:0.85rem; color:#8899aa; }
    .question-item .correct-mark { color:#2ecc71; font-weight:bold; }
    .student-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(180px,1fr)); gap:0.5rem; }
    .student-chip { background:#0f2040; border-radius:8px; padding:0.5rem 1rem; display:flex; justify-content:space-between; align-items:center; }
    .del-btn { background:none; border:none; color:#e74c3c; cursor:pointer; font-size:1.2rem; padding:0 0.3rem; }
    .form-row { display:grid; grid-template-columns:1fr 1fr; gap:0.8rem; margin-bottom:0.8rem; }
    label { font-size:0.85rem; color:#8899aa; display:block; margin-bottom:0.3rem; }
    .correct-radio { display:flex; gap:1rem; margin:0.5rem 0; }
    .correct-radio label { color:white; cursor:pointer; display:flex; align-items:center; gap:0.3rem; font-size:1rem; }
    .msg { padding:0.8rem 1rem; border-radius:8px; margin-top:0.5rem; font-weight:600; }
    .msg.ok { background:#1a5c30; color:#2ecc71; }
    .msg.err { background:#5c1a1a; color:#e74c3c; }
    footer { text-align:center; padding:0.8rem; color:#8899aa; font-size:0.85rem; background:#0f2040; }
  </style>
</head>
<body>

<!-- LOGIN -->
<div class="login-screen" id="login-screen">
  <h1>🐧 PenguQuiz Admin</h1>
  <div style="width:300px;display:flex;flex-direction:column;gap:0.8rem">
    <input type="password" id="pw-input" placeholder="Passwort eingeben..." onkeydown="if(event.key==='Enter')doLogin()">
    <button class="btn" onclick="doLogin()">Anmelden</button>
    <div id="login-err" style="color:#e74c3c;text-align:center;min-height:1.2rem"></div>
  </div>
</div>

<!-- ADMIN LAYOUT -->
<div class="admin-layout" id="admin-layout">
  <div class="topbar">
    <h1>🐧 PenguQuiz Admin</h1>
    <div class="tabs">
      <button class="tab active" onclick="switchTab('questions')">Fragen</button>
      <button class="tab" onclick="switchTab('students')">Schüler</button>
      <button class="tab" onclick="switchTab('settings')">Einstellungen</button>
    </div>
    <button class="btn sm danger" onclick="doLogout()">Abmelden</button>
  </div>
  <div class="content">

    <!-- QUESTIONS PANEL -->
    <div class="panel active" id="panel-questions">
      <div class="card">
        <h3>➕ Neue Frage hinzufügen</h3>
        <label>Szenario / Frage</label>
        <textarea id="new-scenario" rows="3" placeholder="Patientenszenario eingeben..."></textarea>
        <div class="form-row" style="margin-top:0.8rem">
          <div><label>Antwort A</label><input type="text" id="new-a" placeholder="Antwort A"></div>
          <div><label>Antwort B</label><input type="text" id="new-b" placeholder="Antwort B"></div>
          <div><label>Antwort C</label><input type="text" id="new-c" placeholder="Antwort C"></div>
          <div><label>Antwort D</label><input type="text" id="new-d" placeholder="Antwort D"></div>
        </div>
        <label>Richtige Antwort</label>
        <div class="correct-radio">
          <label><input type="radio" name="correct" value="A" checked> A</label>
          <label><input type="radio" name="correct" value="B"> B</label>
          <label><input type="radio" name="correct" value="C"> C</label>
          <label><input type="radio" name="correct" value="D"> D</label>
        </div>
        <button class="btn success" onclick="addQuestion()">Frage speichern</button>
        <div id="q-msg"></div>
      </div>
      <div id="questions-list"></div>
    </div>

    <!-- STUDENTS PANEL -->
    <div class="panel" id="panel-students">
      <div class="card">
        <h3>➕ Schüler hinzufügen</h3>
        <div style="display:flex;gap:0.8rem">
          <input type="text" id="new-student" placeholder="Name eingeben...">
          <button class="btn success" onclick="addStudent()">Hinzufügen</button>
        </div>
        <div id="s-msg"></div>
      </div>
      <div class="card">
        <h3>👥 Schülerliste (<span id="student-count">0</span> Personen)</h3>
        <div class="student-grid" id="student-grid"></div>
      </div>
    </div>

    <!-- SETTINGS PANEL -->
    <div class="panel" id="panel-settings">
      <div class="card">
        <h3>⏱️ Timer</h3>
        <label>Sekunden pro Frage</label>
        <input type="number" id="set-timer" min="10" max="300" value="60" style="width:120px">
      </div>
      <div class="card">
        <h3>💬 Motivationssätze (einer pro Zeile)</h3>
        <textarea id="set-motiv" rows="8"></textarea>
      </div>
      <div class="card">
        <h3>🔒 Passwort ändern</h3>
        <div style="display:flex;gap:0.8rem;max-width:400px">
          <input type="password" id="set-pw" placeholder="Neues Passwort">
          <input type="password" id="set-pw2" placeholder="Wiederholen">
        </div>
      </div>
      <button class="btn" onclick="saveSettings()" style="margin-top:1rem">Einstellungen speichern</button>
      <div id="set-msg"></div>
    </div>
  </div>
  <footer>Diese Seite wurde von Mustafa Kömür erstellt 🐧</footer>
</div>

<script>
function getStudents() { return JSON.parse(localStorage.getItem('penguquiz_students') || '[]'); }
function getQuestions() { return JSON.parse(localStorage.getItem('penguquiz_questions') || '[]'); }
function getSettings() { return JSON.parse(localStorage.getItem('penguquiz_settings') || '{"password":"admin123","timerSeconds":60,"motivationMessages":[]}'); }
function saveStudents(d) { localStorage.setItem('penguquiz_students', JSON.stringify(d)); }
function saveQuestions(d) { localStorage.setItem('penguquiz_questions', JSON.stringify(d)); }
function saveSettingsData(d) { localStorage.setItem('penguquiz_settings', JSON.stringify(d)); }

function doLogin() {
  const pw = document.getElementById('pw-input').value;
  const settings = getSettings();
  if (pw === settings.password) {
    document.getElementById('login-screen').style.display = 'none';
    document.getElementById('admin-layout').classList.add('active');
    renderAll();
  } else {
    document.getElementById('login-err').textContent = 'Falsches Passwort!';
  }
}

function doLogout() {
  document.getElementById('login-screen').style.display = 'flex';
  document.getElementById('admin-layout').classList.remove('active');
  document.getElementById('pw-input').value = '';
  document.getElementById('login-err').textContent = '';
}

function switchTab(tab) {
  document.querySelectorAll('.tab').forEach((t,i) => {
    t.classList.toggle('active', ['questions','students','settings'][i] === tab);
  });
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  document.getElementById('panel-' + tab).classList.add('active');
  renderAll();
}

function renderAll() { renderQuestions(); renderStudents(); renderSettings(); }

function renderQuestions() {
  const list = document.getElementById('questions-list');
  const qs = getQuestions();
  list.innerHTML = qs.map((q, i) => `
    <div class="question-item">
      <p><strong>${i+1}.</strong> ${q.szenario}</p>
      <div class="answers">
        ${q.antworten.map((a,j) => {
          const l = ['A','B','C','D'][j];
          return `<span ${l===q.korrekt?'class="correct-mark"':''}>${a}${l===q.korrekt?' ✓':''}</span>`;
        }).join(' &nbsp;|&nbsp; ')}
      </div>
      <button class="btn danger sm" onclick="deleteQuestion(${i})" style="margin-top:0.5rem">Löschen</button>
    </div>
  `).join('');
}

function addQuestion() {
  const s = document.getElementById('new-scenario').value.trim();
  const a = document.getElementById('new-a').value.trim();
  const b = document.getElementById('new-b').value.trim();
  const c = document.getElementById('new-c').value.trim();
  const d = document.getElementById('new-d').value.trim();
  const correct = document.querySelector('input[name="correct"]:checked').value;
  if (!s||!a||!b||!c||!d) { showMsg('q-msg','Alle Felder ausfüllen!','err'); return; }
  const qs = getQuestions();
  qs.push({ szenario: s, antworten: [`A) ${a}`,`B) ${b}`,`C) ${c}`,`D) ${d}`], korrekt: correct });
  saveQuestions(qs);
  ['new-scenario','new-a','new-b','new-c','new-d'].forEach(id => document.getElementById(id).value='');
  showMsg('q-msg','Frage gespeichert! ✅','ok');
  renderQuestions();
}

function deleteQuestion(i) {
  if (!confirm('Frage löschen?')) return;
  const qs = getQuestions();
  qs.splice(i,1);
  saveQuestions(qs);
  renderQuestions();
}

function renderStudents() {
  const students = getStudents();
  document.getElementById('student-count').textContent = students.length;
  document.getElementById('student-grid').innerHTML = students.map((s,i) =>
    `<div class="student-chip"><span>${s}</span><button class="del-btn" onclick="deleteStudent(${i})">×</button></div>`
  ).join('');
}

function addStudent() {
  const name = document.getElementById('new-student').value.trim();
  if (!name) return;
  const students = getStudents();
  students.push(name);
  saveStudents(students);
  document.getElementById('new-student').value = '';
  showMsg('s-msg','Schüler hinzugefügt! ✅','ok');
  renderStudents();
}

function deleteStudent(i) {
  if (!confirm('Schüler entfernen?')) return;
  const students = getStudents();
  students.splice(i,1);
  saveStudents(students);
  renderStudents();
}

function renderSettings() {
  const s = getSettings();
  document.getElementById('set-timer').value = s.timerSeconds;
  document.getElementById('set-motiv').value = s.motivationMessages.join('\n');
}

function saveSettings() {
  const s = getSettings();
  const newPw = document.getElementById('set-pw').value;
  const newPw2 = document.getElementById('set-pw2').value;
  if (newPw) {
    if (newPw !== newPw2) { showMsg('set-msg','Passwörter stimmen nicht überein!','err'); return; }
    s.password = newPw;
  }
  s.timerSeconds = parseInt(document.getElementById('set-timer').value) || 60;
  s.motivationMessages = document.getElementById('set-motiv').value.split('\n').filter(l=>l.trim());
  saveSettingsData(s);
  showMsg('set-msg','Gespeichert! ✅','ok');
}

function showMsg(id, text, type) {
  const el = document.getElementById(id);
  el.className = 'msg ' + type;
  el.textContent = text;
  setTimeout(() => el.textContent = '', 3000);
}
</script>
</body>
</html>
```

- [ ] **Step 2: Verify admin panel**

Open `admin.html` → login with `admin123` → add a question → check it appears → delete it → change a student → save settings.

- [ ] **Step 3: Commit**
```bash
git add admin.html
git commit -m "feat: add admin panel with questions, students, and settings management"
```

---

### Task 9: Polish & Cross-Device Testing

**Files:**
- Modify: `index.html` — fix any layout issues, ensure readability on projector

- [ ] **Step 1: Add responsive projector fixes**

Add to CSS:
```css
@media (min-width: 1400px) {
  :root {
    --font-xl: 4.5rem;
    --font-lg: 3rem;
    --font-md: 2rem;
    --font-sm: 1.5rem;
  }
}
@media (max-width: 768px) {
  .answer-grid { grid-template-columns: 1fr; }
  .scoreboard { position:static; transform:none; margin:1rem; }
  #screen-question { padding: 1rem; }
}
```

- [ ] **Step 2: Add "Zum Spiel" link in admin**

In `admin.html` topbar, add after the tabs:
```html
<a href="index.html" class="btn sm" style="text-decoration:none">🎮 Zum Spiel</a>
```

- [ ] **Step 3: Test on multiple browsers**

Open both files in Chrome and Firefox. Verify:
- Wheel spins and selects names correctly
- Timer counts down with visual arc
- Sounds play (may need first click to unlock AudioContext)
- Confetti appears on finale
- Admin panel saves and loads data correctly

- [ ] **Step 4: Final commit**
```bash
git add index.html admin.html
git commit -m "feat: responsive polish, projector layout, admin game link"
```

---

## Self-Review

**Spec coverage check:**
- ✅ Spinning wheel with auto red/blue selection → Task 4
- ✅ Stage call with 5s countdown → Task 5
- ✅ "Ich bin bereit!" button → Task 5
- ✅ 60s timer with visual arc → Task 5
- ✅ +1/-1 scoring → Task 5
- ✅ Motivational messages on wrong answer → Task 5
- ✅ Live scoreboard (right side) → Task 5
- ✅ Used students never repeat → Task 5 (usedStudents array)
- ✅ Final screen with winner reveal → Task 6
- ✅ Confetti animation → Task 6
- ✅ Web Audio sounds (spin, correct, wrong, fanfare) → Task 7
- ✅ Admin panel (questions, students, settings) → Task 8
- ✅ Password protection → Task 8
- ✅ localStorage persistence → Task 1
- ✅ 50 students hardcoded → Task 1
- ✅ 30 medically correct questions → Task 1
- ✅ Penguin theme, dark navy background → Task 2
- ✅ Footer "Diese Seite wurde von Mustafa Kömür erstellt 🐧" → Task 2
- ✅ Projector-friendly large fonts → Task 9
- ✅ Cross-device responsive → Task 9
