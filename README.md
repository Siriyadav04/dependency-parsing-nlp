# Dependency Parsing for Low-Resource Languages

Fine-tuned style dependency parsing system using Stanza NLP with Django-based web integration for English and Hindi language analysis.

---

# Table of Contents

- Overview
- Features
- Project Structure
- Working Methodology
- Example Outputs
- Installation
- Usage
- Django Integration Details
- Tech Stack
- Future Scope
- Conclusion

---

# Overview

This project focuses on dependency parsing for low-resource language processing using the Stanza NLP library and Django web integration.

Dependency Parsing is an important Natural Language Processing (NLP) task used to identify grammatical relationships between words in a sentence. The system determines relations such as subject, object, auxiliary verb, modifiers, and root structure.

The project combines NLP processing, backend development, and web integration to create a real-time multilingual dependency parsing system.

The application supports both English and Hindi sentence parsing through an interactive Django web interface.

---

# Features

- English dependency parsing
- Hindi dependency parsing
- Real-time dependency relation extraction
- Django-based web interface
- Dependency tree visualization
- Language selection support
- Token-level grammatical analysis
- Interactive browser-based parsing

---

# Project Structure

```text
dependency-parsing-nlp/
│
├── nlp_lab/
│   ├── templates/
│   │   └── home.html
│   │
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── apps.py
│
├── nlp_modules/
│   ├── dependency.py
│   ├── evaluation.py
│   └── __init__.py
│
├── nlp_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── db.sqlite3
└── test_stanza.py

---

# Working Methodology

## Step 1 — User Input

The user enters a sentence in the Django web interface and selects the preferred language.

Supported Languages:
- English
- Hindi

---

## Step 2 — Backend Processing

The sentence is sent from Django views to the NLP processing module.

Main backend files:
- `views.py`
- `dependency.py`

---

## Step 3 — NLP Pipeline Execution

The Stanza NLP pipeline processes the sentence using:
- Tokenization
- POS Tagging
- Dependency Parsing

Example:

```python
nlp = stanza.Pipeline(lang='en')
doc = nlp(text)
```python
```

---

## Step 4 — Dependency Extraction

Dependency relations are extracted word-by-word.

Example relations:
- nsubj → nominal subject
- obj → object
- aux → auxiliary verb
- root → root word

---

## Step 5 — Result Visualization

The dependency output and dependency tree structure are displayed on the webpage.

---

# Example Outputs

## English Example

Input:

```text
Although it was raining heavily, Siri went to college because she had an exam.
```

Sample Dependency Relations:

| Word | Relation | Head |
|---|---|---|
| Siri | nsubj | went |
| went | root | ROOT |
| college | obl | went |
| had | advcl | went |
| exam | obj | had |

Dependency Tree:

```text
went [ROOT]
├── Siri [nsubj]
├── college [obl]
├── raining [advcl]
│   └── Although [mark]
└── had [advcl]
    ├── she [nsubj]
    └── exam [obj]
```

---

## Hindi Example

Input:

```text
राम आम खाता है।
```

Sample Dependency Relations:

| Word | Relation | Head |
|---|---|---|
| राम | nsubj | खाता |
| आम | obj | खाता |
| खाता | root | ROOT |
| है | aux | खाता |

Dependency Tree:

```text
खाता [ROOT]
├── राम [nsubj]
├── आम [obj]
└── है [aux]
```

---

# Installation

## Prerequisites

- Python 3.10+
- Django
- Stanza NLP
- VS Code

---

## Clone Repository

```bash
git clone https://github.com/your-username/dependency-parsing-nlp.git
cd dependency-parsing-nlp
```

---

## Install Dependencies

```bash
pip install django
pip install stanza
```

---

## Download Stanza Models

```python
import stanza

stanza.download('en')
stanza.download('hi')
```

---

# Usage

## Run the Django Server

```bash
python manage.py runserver
```

---

## Open Browser

```text
http://127.0.0.1:8000/
```

---

## Parse Sentences

1. Enter sentence
2. Select language
3. Click Parse Sentence
4. View dependency relations and dependency tree

---

# Django Integration Details

## Main Django Components

| File | Purpose |
|---|---|
| views.py | Handles user requests |
| urls.py | URL routing |
| home.html | Frontend interface |
| dependency.py | NLP processing logic |

---

## Backend Workflow

```text
User Input
   ↓
Django View
   ↓
Stanza NLP Pipeline
   ↓
Dependency Extraction
   ↓
Result Display
```

---

# Tech Stack

| Layer | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | Django |
| NLP Library | Stanza NLP |
| Frontend | HTML/CSS |
| Database | SQLite |
| IDE | VS Code |

---

# Future Scope

- Support for additional Indian languages
- Improved dependency tree visualization
- Advanced multilingual parsing
- Integration with speech-to-text systems
- Enhanced frontend visualization

---

# Conclusion

This project successfully demonstrates dependency parsing for English and Hindi using Stanza NLP integrated with Django.

The system performs grammatical dependency analysis in real time and displays dependency relations through a user-friendly web interface.

The project highlights the application of NLP techniques for multilingual and low-resource language processing.
