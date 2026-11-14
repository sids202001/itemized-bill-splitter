# 🧾 Itemized Bill & Expense Splitter

<p align="left">
  <img src="https://img.shields.io/badge/Vanilla_ES6+-Pure_JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="Vanilla ES6+" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-Modern_UI-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS" />
  <img src="https://img.shields.io/badge/Offline--First-On--Demand_OCR-success?style=for-the-badge" alt="Offline-First" />
  <img src="https://img.shields.io/badge/WhatsApp-Instant_Export-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp" />
</p>

Splitting a shared bill after dining out or sharing apartment expenses with friends almost always turns into an awkward math headache. Standard expense-splitting apps either force everyone into a flat equal split—which is unfair when one person ordered an expensive entrée and cocktails while another just had a side salad—or they leave you scribbling on receipts with a phone calculator trying to figure out how to divide variable sales tax, tips, and service fees without shortchanging anyone. I built this web application to solve that exact friction with mathematical fairness and zero hassle.

The application breaks down bills item-by-item and gives users four flexible ways to divide each dish: split equally across a group, assign exact dollar amounts, set custom percentages, or allocate weighted shares. What makes the engine truly fair is its proportional fee distribution algorithm: instead of naively splitting taxes and tips evenly, it calculates each person's exact percentage of the pre-tax food and drink subtotal, dynamically scaling their share of the tax, gratuity, and delivery fees based strictly on what they actually consumed. Built with an offline-first architecture with on-demand client-side OCR (zero external dependencies until optional client-side OCR is loaded on demand) in pure Vanilla ES6+ and Tailwind CSS, the app loads in under 50ms on any phone or desktop browser with zero login, zero installations, and total client-side privacy. It automatically balances fractional penny rounding errors down to the cent, generates a real-time digital receipt audit log, and lets you export a pre-formatted itemized breakdown directly to WhatsApp or download a complete CSV report with a single tap.

<p align="left">
  <img src="https://img.shields.io/badge/Financial_Algorithms-Proportional_Fee_Distribution-blue?style=flat-square" alt="Financial Algorithms" />
  <img src="https://img.shields.io/badge/Precision-Cent_Rounding_Reconciliation-blueviolet?style=flat-square" alt="Cent Precision" />
  <img src="https://img.shields.io/badge/Architecture-100%25_Client--Side_Privacy-success?style=flat-square" alt="Privacy" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-Responsive_Glassmorphism-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white" alt="Tailwind CSS" />
  <img src="https://img.shields.io/badge/Export-WhatsApp_%7C_CSV_Download-25D366?style=flat-square&logo=whatsapp&logoColor=white" alt="Export" />
</p>
