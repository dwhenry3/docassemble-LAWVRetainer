import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LAWVRetainer',
      version='2.0.2',
      description=('A docassemble extension to utilizing a multi-part interview to create either a 1) Legal, 2) Spanish, 3) FAST, or 4) BHA retainer'),
      long_description='\r\n# LAWV Retainer Agreement Interview\r\n\r\nA **Docassemble** interview developed by **Legal Aid of West Virginia** to allow advocates to generate, sign, email, and receive signed retainer agreements from clients. This tool streamlines the process for English, Spanish, FAST, and BHA retainer workflows while ensuring compliance with Legal Aid protocols.\r\n\r\nThe interview guides advocates and clients through entering required information, reviewing the applicable retainer terms, signing electronically, and automatically distributing completed documents.\r\n\r\n---\r\n\r\n## Purpose\r\n\r\nThis tool assists advocates in creating a complete and compliant **retainer agreement** for Legal Aid of West Virginia clients. It supports multiple program types, sends copies to all required parties, and facilitates digital signatures for both the advocate and the client.\r\n\r\n---\r\n\r\n## Features\r\n\r\n### User-Facing Features\r\n\r\n- Advocate selects whether signing personally or preparing for another staff member  \r\n- Guided entry of advocate, alternate advocate, client, and custodian (if applicable)  \r\n- Client citizenship screening with Non‑Citizen Status Questionnaire prompt  \r\n- Program‑specific retainer paths:\r\n  - **English Legal Retainer**\r\n  - **Spanish Legal Retainer**\r\n  - **FAST Advocate Retainer**\r\n  - **BHA Advocate Retainer**\r\n- Limited and extended scope options for English/Spanish legal retainers  \r\n- FAST and BHA service‑level checklists  \r\n- Client and advocate digital signatures  \r\n- Automatic email delivery of signed forms  \r\n- Ability for client to reject terms, generating notification back to LAWV  \r\n\r\n### Technical Features\r\n\r\n- Uses **docassemble.LAWVCommon** for styling and shared utility functions  \r\n- Multi‑party signature workflow (advocate → client)  \r\n- Dynamic generation of the correct retainer PDF based on program type  \r\n- Conditional logic managing:\r\n  - Citizenship rules  \r\n  - Custodian behavior  \r\n  - Co‑representation disclosures  \r\n  - Opt‑out of “Use of Information” terms  \r\n- Automatic notification emails using Docassemble templates  \r\n- Separate email handling when the retainer is prepared on behalf of another advocate  \r\n\r\n---\r\n\r\n## File Information\r\n\r\nThis repository includes the primary Docassemble interview file:\r\n\r\n- `retainer.yml` — Full interview logic, screens, validations, signature workflow, and document assembly configuration.\r\n\r\nThe YAML references several templates that must be included in the Docassemble package:\r\n\r\n- `lawv_retainer.pdf`  \r\n- `lawv_retainer_spanish.pdf`  \r\n- `fast.pdf`  \r\n- `bha.pdf`  \r\n- Optional sample PDFs:  \r\n  - `fast_sample.pdf`  \r\n  - `bha_sample.pdf`  \r\n  - `lawv_retainer_sample.pdf`  \r\n  - `lawv_retainer_spanish_sample.pdf`  \r\n- `non_citizen_status_worksheet.pdf`\r\n\r\n---\r\n\r\n## Logic Overview\r\n\r\nThe interview performs the following key actions:\r\n\r\n1. Determines whether the advocate is signing personally or preparing the retainer for someone else  \r\n2. Collects advocate, alternate advocate (if applicable), and client information  \r\n3. Screens client for citizenship and presents the mandatory non‑citizen questionnaire when needed  \r\n4. Prompts for retainer type:\r\n   - English or Spanish Legal Retainer  \r\n   - FAST Retainer  \r\n   - BHA Retainer  \r\n5. For legal retainers:\r\n   - Captures scope: limited or extended  \r\n   - Provides detailed checklists or fields depending on scope  \r\n6. For FAST and BHA:\r\n   - Guides selection of service levels  \r\n   - Handles custodian rules for minors or protected persons  \r\n7. Reviews and displays applicable terms, including required LAWV disclosures  \r\n8. Captures advocate signature (typed or digital)  \r\n9. Sends notification email to the client for their signature  \r\n10. Validates client identity via birthdate challenge  \r\n11. Presents the client with their portion of the retainer and signature options  \r\n12. Sends completed documents to both client and advocate(s)  \r\n13. Handles rejection pathways and notifies LAWV if terms are declined  \r\n\r\n---\r\n\r\n## Output\r\n\r\nDepending on the type of retainer selected, the interview generates and emails:\r\n\r\n- A completed PDF retainer agreement  \r\n- English and/or Spanish versions (for legal retainers)  \r\n- FAST or BHA program‑specific PDF retainers  \r\n- Copies automatically sent to the advocate, alternate advocate (if applicable), and the client  \r\n\r\nAll personal information is purged once the interview is complete.\r\n\r\n---\r\n\r\n## Contact\r\n\r\nCreated by **Dane W. Henry, Esq.** for **Legal Aid of West Virginia**.\r\n\r\nMore information about Legal Aid of West Virginia:  \r\nhttps://legalaidwv.org/\r\n',
      long_description_content_type='text/markdown',
      author='Dane Henry, Esq.',
      author_email='dhenry@lawv.net',
      license='MIT',
      url='https://docassemble.org',
      packages=find_namespace_packages(),
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LAWVRetainer/', package='docassemble.LAWVRetainer'),
     )
