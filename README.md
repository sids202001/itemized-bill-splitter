# Itemized Bill & Expense Splitter

> A zero-dependency, client-side web application engineered to solve group dining expense division through fair, proportional tax and tip attribution rather than crude flat splits.

---

## ⚡ The Problem
Splitting a shared bill after dining out or sharing household expenses always creates friction:
* **Unfair Flat Splits:** Standard apps divide total tax and tip equally. A person who orders a $12 salad ends up paying the same $10 tip as someone who ordered a $60 steak and cocktails.
* **Manual Math Headaches:** Calculating itemized percentages on a napkin or phone calculator is tedious and prone to rounding errors.

**Itemized Bill & Expense Splitter** eliminates this with a mathematically fair, consumption-weighted proportional algorithm.

---

## 🛠️ How It Works & Key Capabilities

### 1. Fair Proportional Fee Attribution
Instead of an equal split, extra fees (sales tax, tips, delivery fees) are distributed relative to each person's actual consumption:
Taxes and gratuities scale linearly with each person's individual item total.

### 2. Four Flexible Split Modes
* **Equal Split:** Checkbox toggle to quickly share an item across any subset of people.
* **Exact Dollar ($):** Assign exact amounts with a one-click *"Fill Remaining"* balance solver.
* **Percent (%):** Custom percentage allocation with real-time 100% sum-validation guards.
* **Weighted Shares (x:y):** Ratio-based division for unequal consumption tiers.

### 3. Floating-Point Cent Parity
Eliminates JavaScript IEEE-754 precision drift using integer-cent rounding reconciliation so the sum of individual balances perfectly matches the master invoice total.

### 4. Zero-Dependency, Offline-First Architecture
Built as a single standalone client combining pure **Vanilla ES6+** and **Tailwind CSS via CDN**. Loads in under 50ms, works completely offline, requires zero node_modules or build tools, and guarantees 100% client-side privacy.

### 5. One-Click Social & Data Export
* **Copy for WhatsApp / SMS:** Formats an itemized breakdown with per-person subtotals and balances ready to paste into group chats.
* **Download CSV:** Exports the complete digital receipt audit log as a spreadsheet.

---

## 🚀 Getting Started

### Web Application (Interactive)
Simply open `index.html` in any web browser on your phone, tablet, or desktop. No server or setup required!

### Python CLI Version
Run the companion command-line script:
```bash
python3 bill_splitter.py
```

---

## 🧰 Tech Stack
* **Frontend:** Vanilla JavaScript (ES6+), HTML5 Canvas/DOM
* **Styling:** Tailwind CSS (CDN), Custom Glassmorphic Dark UI
* **Icons:** Phosphor Icons
* **CLI:** Python 3
