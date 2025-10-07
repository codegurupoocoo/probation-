
# onboard-tushar — AveoEarth Onboarding Assignment

This repository contains the complete submission for the AveoEarth onboarding assignment by **Tushar Singh**.

## 📁 Folder Structure

```

onboard-tushar/
├── task1/                 # Email Automation Agent + Dashboard
│   ├── backend/
│   ├── frontend/
│   ├── docker-compose.yml
│   ├── .env.example
│   └── sample_recipients.xlsx
├── task2/                 # Blockchain & Cryptocurrency Strategy Proposal
│   ├── Task2_Blockchain_Strategy.pdf
│   ├── README.md
│   └── diagrams/
└── submission_tushar.pdf  # Main submission PDF with demo links and screenshots

````

---

## 1️⃣ Task 1 — Email Automation + Tracking Dashboard

### Features
- Upload XLSX/CSV recipient list.
- Send templated HTML emails with image + CTA button.
- Track email opens using 1x1 pixel tracking.
- Track CTA clicks using redirect URLs.
- Automatically send reminders for users who opened but did not click within 3 days.
- Dashboard with metrics, trends, recipient table, and CSV export.

### Tech Stack
- **Frontend:** Next.js, React, Tailwind CSS
- **Backend:** FastAPI, Celery, Redis, PostgreSQL
- **Email Provider:** SendGrid (or simulated for testing)
- **Deployment:** Docker + docker-compose

### Local Setup

1. Copy `.env.example` to `.env` and fill in keys (SendGrid optional for simulation):

```powershell
cp .env.example .env
````

2. Start Docker containers:

```powershell
docker compose up --build
```

3. Open apps:

* Frontend: [http://localhost:3000](http://localhost:3000)
* Backend API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

4. Upload `sample_recipients.xlsx`, start campaign, and view dashboard.

---

## 2️⃣ Task 2 — Blockchain & Cryptocurrency Strategy Proposal

* **PDF:** `task2/Task2_Blockchain_Strategy.pdf`
* Focuses on:

  * Blockchain-based Carbon Credit program (transparent, verifiable, no double-spending)
  * Aveo Coin (ICO) with Proof-of-Stake for minimal carbon footprint
  * Roadmap for ICO launch and ecosystem utility
* **Diagrams:** Placeholder files in `task2/diagrams/`

---

## 3️⃣ Task 3 — Next.js + FastAPI Technical Notes

* Cheat-sheet covering:

  * Next.js: SSR, SSG, ISR, API routes, image optimization, deployment
  * FastAPI: async endpoints, dependency injection, JWT auth, background tasks, WebSockets, pytest
* Demo integrated in Task 1 frontend + backend.

---

## 🎥 Demo Video

[Click here to view demo video](https://drive.google.com/file/d/1--ey5Dn5DPLJpvZHPNFCWtdFnEcaWh0w/view?usp=sharing)


---

## 📄 Submission PDF

* `submission_tushar.pdf` contains:

  * Executive summary
  * Dashboard screenshots
  * Event tracking logs
  * Task 2 proposal reference
  * Demo video link

---

## 📧 Contact

Tushar Singh — [tusharsingh1616@gmail.com](mailto:tusharsingh1616@gmail.com)

---

```

---

I can also **fill in the `<INSERT_DEMO_LINK_HERE>` for you** if you give me your YouTube/Drive demo link.  

Do you want me to do that now?
```
