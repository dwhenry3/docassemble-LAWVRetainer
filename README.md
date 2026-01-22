
# LAWV Retainer Agreement Interview

A **Docassemble** interview developed by **Legal Aid of West Virginia** to allow advocates to generate, sign, email, and receive signed retainer agreements from clients. This tool streamlines the process for English, Spanish, FAST, and BHA retainer workflows while ensuring compliance with Legal Aid protocols.

The interview guides advocates and clients through entering required information, reviewing the applicable retainer terms, signing electronically, and automatically distributing completed documents.

---

## Purpose

This tool assists advocates in creating a complete and compliant **retainer agreement** for Legal Aid of West Virginia clients. It supports multiple program types, sends copies to all required parties, and facilitates digital signatures for both the advocate and the client.

---

## Features

### User-Facing Features

- Advocate selects whether signing personally or preparing for another staff member  
- Guided entry of advocate, alternate advocate, client, and custodian (if applicable)  
- Client citizenship screening with Non‑Citizen Status Questionnaire prompt  
- Program‑specific retainer paths:
  - **English Legal Retainer**
  - **Spanish Legal Retainer**
  - **FAST Advocate Retainer**
  - **BHA Advocate Retainer**
- Limited and extended scope options for English/Spanish legal retainers  
- FAST and BHA service‑level checklists  
- Client and advocate digital signatures  
- Automatic email delivery of signed forms  
- Ability for client to reject terms, generating notification back to LAWV  

### Technical Features

- Uses **docassemble.LAWVCommon** for styling and shared utility functions  
- Multi‑party signature workflow (advocate → client)  
- Dynamic generation of the correct retainer PDF based on program type  
- Conditional logic managing:
  - Citizenship rules  
  - Custodian behavior  
  - Co‑representation disclosures  
  - Opt‑out of “Use of Information” terms  
- Automatic notification emails using Docassemble templates  
- Separate email handling when the retainer is prepared on behalf of another advocate  

---

## File Information

This repository includes the primary Docassemble interview file:

- `retainer.yml` — Full interview logic, screens, validations, signature workflow, and document assembly configuration.

The YAML references several templates that must be included in the Docassemble package:

- `lawv_retainer.pdf`  
- `lawv_retainer_spanish.pdf`  
- `fast.pdf`  
- `bha.pdf`  
- Optional sample PDFs:  
  - `fast_sample.pdf`  
  - `bha_sample.pdf`  
  - `lawv_retainer_sample.pdf`  
  - `lawv_retainer_spanish_sample.pdf`  
- `non_citizen_status_worksheet.pdf`

---

## Logic Overview

The interview performs the following key actions:

1. Determines whether the advocate is signing personally or preparing the retainer for someone else  
2. Collects advocate, alternate advocate (if applicable), and client information  
3. Screens client for citizenship and presents the mandatory non‑citizen questionnaire when needed  
4. Prompts for retainer type:
   - English or Spanish Legal Retainer  
   - FAST Retainer  
   - BHA Retainer  
5. For legal retainers:
   - Captures scope: limited or extended  
   - Provides detailed checklists or fields depending on scope  
6. For FAST and BHA:
   - Guides selection of service levels  
   - Handles custodian rules for minors or protected persons  
7. Reviews and displays applicable terms, including required LAWV disclosures  
8. Captures advocate signature (typed or digital)  
9. Sends notification email to the client for their signature  
10. Validates client identity via birthdate challenge  
11. Presents the client with their portion of the retainer and signature options  
12. Sends completed documents to both client and advocate(s)  
13. Handles rejection pathways and notifies LAWV if terms are declined  

---

## Output

Depending on the type of retainer selected, the interview generates and emails:

- A completed PDF retainer agreement  
- English and/or Spanish versions (for legal retainers)  
- FAST or BHA program‑specific PDF retainers  
- Copies automatically sent to the advocate, alternate advocate (if applicable), and the client  

All personal information is purged once the interview is complete.

---

## Contact

Created by **Dane W. Henry, Esq.** for **Legal Aid of West Virginia**.

More information about Legal Aid of West Virginia:  
https://legalaidwv.org/
