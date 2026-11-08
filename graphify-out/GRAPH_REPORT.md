# Graph Report - Abdulloh_ustudy  (2026-11-08)

## Corpus Check
- Corpus is ~4,793 words - fits in a single context window. You may not need a graph.

## Summary
- 165 nodes · 201 edges · 16 communities (7 shown, 9 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 22 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Page App (Speakers, Branches)
- Courses App
- Compose Services
- Web Env Config
- Django Project Bootstrap
- Postgres Service
- DB Migrations
- App Configs
- Python Dependencies
- MCP Config

## God Nodes (most connected - your core abstractions)
1. `environment` - 12 edges
2. `Courses` - 11 edges
3. `Speakers` - 9 edges
4. `db` - 6 edges
5. `web` - 6 edges
6. `nginx` - 6 edges
7. `volumes` - 6 edges
8. `Branches` - 6 edges
9. `Base Navbar` - 6 edges
10. `services` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Speaker Upload Form` --shares_data_with--> `Speakers`  [AMBIGUOUS]
  templates/speakers/speakers.html → page/models.py
- `Base Navbar` --references--> `list_course()`  [EXTRACTED]
  templates/base.html → courses/views.py
- `Ayron (Ayran) Course Image` --shares_data_with--> `Courses`  [INFERRED]
  courses/images/ayron.webp → courses/models.py
- `Course Card Grid` --references--> `detail_course()`  [EXTRACTED]
  templates/course/course_list.html → courses/views.py
- `Base Footer` --references--> `about_us()`  [EXTRACTED]
  templates/base.html → page/views.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Model-backed list pages (grid of cards)** — templates_course_course_list, templates_speakers_list_speakers, templates_branches_branches [INFERRED 0.85]
- **Empty placeholder pages** — templates_home_home, templates_contacts_contacts, templates_news_news, templates_about_us_about_us [INFERRED 0.85]

## Communities (16 total, 9 thin omitted)

### Community 0 - "Page App (Speakers, Branches)"
Cohesion: 0.12
Nodes (17): SpeakersForm, Meta, Branches, Speakers, about_us(), contact_us(), home(), list_branches() (+9 more)

### Community 1 - "Courses App"
Cohesion: 0.15
Nodes (11): CourseForm, Meta, Ayron (Ayran) Course Image, Ayran yogurt drink in glass decanter, Courses, detail_course(), list_course(), Pillow 12.3.0 (+3 more)

### Community 2 - "Compose Services"
Cohesion: 0.11
Nodes (18): image, profiles, volumes, name, depends_on, image, ports, restart (+10 more)

### Community 3 - "Web Env Config"
Cohesion: 0.11
Nodes (19): condition, db, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS, DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT (+11 more)

### Community 5 - "Postgres Service"
Cohesion: 0.15
Nodes (13): environment, healthcheck, image, restart, volumes, POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_USER (+5 more)

### Community 6 - "DB Migrations"
Cohesion: 0.15
Nodes (6): Migration, Migration, Migration, Migration, Migration, Migration

### Community 9 - "Python Dependencies"
Cohesion: 0.29
Nodes (6): asgiref 3.12.1, Django 6.1.2, gunicorn 23.0.0, psycopg2-binary 2.9.13, python-dotenv 1.2.4, sqlparse 0.6.0

## Ambiguous Edges - Review These
- `Speakers` → `Speaker Upload Form`  [AMBIGUOUS]
  templates/speakers/speakers.html · relation: shares_data_with

## Knowledge Gaps
- **10 isolated node(s):** `Django 6.1.2`, `psycopg2-binary 2.9.13`, `python-dotenv 1.2.4`, `gunicorn 23.0.0`, `asgiref 3.12.1` (+5 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 86 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `services` connect `Compose Services` to `Web Env Config`, `Postgres Service`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `Courses` (e.g. with `CourseForm` and `Ayron (Ayran) Course Image`) actually correct?**
  _`Courses` has 6 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Django 6.1.2`, `psycopg2-binary 2.9.13`, `python-dotenv 1.2.4` to the rest of the system?**
  _10 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Page App (Speakers, Branches)` be split into smaller, more focused modules?**
  _Cohesion score 0.11827956989247312 - nodes in this community are weakly interconnected._
- **Why does `web` connect `Web Env Config` to `Compose Services`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Speakers` (e.g. with `SpeakersForm` and `list_speakers()`) actually correct?**
  _`Speakers` has 3 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `Speakers` and `Speaker Upload Form`?**
  _Edge tagged AMBIGUOUS (relation: shares_data_with) - confidence is low._