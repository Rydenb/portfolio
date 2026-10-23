---
layout: post
codemirror: true
title: Ryden Bercovitch Retrospective
description: My retrospective on personal growth and work habits, what I learned from the MCQ, and how our team (Ryden and Aarav) improved while building the San Diego Rescue Mission website, login page, and backend connection.
permalink: /retrospective
author: Ryden Bercovitch
---

## Personal Growth & Ground Zero (Work Habits Included)

I grew a lot this sprint, and the biggest lesson was that doing things fast isn't the same as doing them right.

* **Learned how a full-stack pipeline actually works.** I connected our frontend login page to our Flask backend, so data typed on the site gets saved in the SQLite database and sent back. I can demo it on localhost.
* **Learned to work within the class system.** At first we used ai to generate the frontend and it used its own colors instead of the teacher's SASS. We switched every color to the original template palette, so the site follows the system instead of fighting it.
* **Learned to prompt AI within requirements and to review what it does.** Giving AI clear rules (use the teacher's SASS, don't commit or push) got much better results, and checking every change with `git diff` before committing keeps mistakes off the live site.
* **Work habits I'm fixing:** smaller commits with clear messages (not "debugging"), and keeping issues and the Kanban updated while I work, not after.

## MCQ Retrospective

I rushed the practice test and didn't read through almost half of the questions. I spent under 10 seconds on 29 of the 66 questions, so even the ones I got right don't really show what I know. My score was 50/66 (76%). My strongest areas were Algorithms & Programming (87%) and Networks (100%), and my weakest was **Data (50%)**, especially binary numbers, compression, and reading graphs. Nine of my 16 Data questions were ones I rushed, so that's where slowing down matters most. I'm redoing the rushed questions at 1–2 minutes each and writing out why each answer is right, starting with binary and data analysis.

## Team Improvements

As a team, Aarav and I got better at communicating and splitting work. Early on we both claimed the same issues (the resource finder and donation calculator), so we sorted it out and updated GitHub: Aarav took the Get Help Now finder, the donation calculator, and the accessibility audit, and I took volunteer signup, accounts and roles, and the donation needs board. I set up our GitHub organization, repos, and GitHub Pages deployment, then built the login page and connected it to our Flask backend. When we hit problems, like the site going blank and the colors not matching the teacher's SASS, we tracked down what caused them and fixed them within the repo's workflow instead of starting over.

---

# Sprint 1–2 Self-Evaluation

**Change** compares each score to my Week 4 Ground 0 self-evaluation (↑ up, ↓ down, = same).

## Technical Evaluation

### Tools & Development Environment

| ID | Area | Self Rank | Change | Peer | Teacher |
|---|---|:---:|:---:|:---:|:---:|
| T01 | Development Environment | 3 | = | | |
| T02 | VS Code | 3 | = | | |
| T03 | Git / GitHub | **4** | ↑ | | |
| T04 | Portfolio / GitHub Pages | 3 | = | | |

**Summary:** Git is where I grew the most. I set up our team's GitHub organization with frontend and backend repos, merged pull requests, and merged the class templates back into our project as an upstream with `--allow-unrelated-histories`, building before committing. I also learned `git stash` to set work aside safely, and `claude --continue` to recover after closing my terminal mid-task. I still run into Pages issues sometimes. For example, I learned that Jekyll skips posts without a date in the filename.

### Development & Creation

| ID | Area | Self Rank | Change | Peer | Teacher |
|---|---|:---:|:---:|:---:|:---:|
| T05 | Tools & Equipment Hacks | 3 | = | | |
| T06 | Portfolio / Blogging Hacks | 2 | = | | |
| T07 | Theme / Style / Layout | 2 | = | | |
| T08 | JavaScript / Coding Challenges | **1** | ↓ | | |
| T09 | AI / Live Code Orchestration | **3** | ↑ | | |

**Summary:** I'm moving the home page to a hub built from YAML data with OCS grammar classes. My AI orchestration improved a lot. I write prompts with clear rules, have the AI show its plan first, and review the diff before committing.

### Technical Awareness & Communication

| ID | Area | Self Rank | Change | Peer | Teacher |
|---|---|:---:|:---:|:---:|:---:|
| T10 | Tech / Cyber Growth | 3 | = | | |
| T11 | Learning Through Mistakes | **4** | ↑ | | |
| T12 | Tech / Cyber Talk | 2 | = | | |

**Summary:** My biggest mistake was letting AI move all of our page text and data into the backend, which made the live site go blank without Flask running. I traced it back through the git history, figured out which commits caused it, and fixed it. I also came away with a clear rule: page text and fixed data stay in the frontend, and only shared or private data (users, roles, sign-ups) goes in the backend.

## Professional Evaluation

### Core Behaviors

| ID | Area | Self Rank | Change | Peer | Teacher |
|---|---|:---:|:---:|:---:|:---:|
| P01 | Attendance / Tardy | 4 | = | | |
| P02 | Work Habits | **2** | ↓ | | |
| P03 | Integrity | **2** | ↓ | | |

**Summary:** My attendance is still strong. I lowered work habits because I committed AI changes without reviewing them, used vague commit messages like "debugging", and rushed the practice MCQ. For integrity, I haven't been 100% sure on everything my bot code is doing.

### Collaboration

| ID | Area | Self Rank | Change | Peer | Teacher |
|---|---|:---:|:---:|:---:|:---:|
| P04 | Communication | 2 | = | | |
| P05 | Help Seeking | 3 | = | | |
| P06 | Mentoring / Advocacy | 2 | = | | |

**Summary:** Aarav and I both claimed the same issues at first, which showed we weren't communicating enough. We sorted it out and updated the GitHub assignments, and now each of us owns three issues.

### Professional Skills

| ID | Area | Self Rank | Change | Peer | Teacher |
|---|---|:---:|:---:|:---:|:---:|
| P07 | Timeliness | 2 | = | | |
| P08 | Persistence | 3 | = | | |
| P09 | Organization | 2 | = | | |
| P10 | Engagement | **2** | ↓ | | |

**Summary:** I kept going through a lot of broken builds, merge conflicts, and backend errors. I lowered engagement because I didn't actually read almost half the MCQ questions. That's not real effort, and it means my score doesn't show what I know.

## Retrospective Question
**What can I do now as a developer that I could not do at the beginning of this sprint?**
I can connect a frontend to a backend: a login form sends JSON to a Flask API, which checks and saves it in SQLite and sends a session back. I can also manage a real team repo: an organization, branches, pull requests, stashing, and merging an upstream template into our project.

## Strongest Technical Evidence
- **The technical evidence I am most proud of:** The working login page connected to our Flask backend (PR #13). Signing up on the site creates a new row in the SQLite `users` table.
- **The biggest technical problem I solved:** The live site went blank because page text had been moved into the backend. I found the cause in the git history and fixed the frontend/backend split.
- **The technical skill I most need to improve:** JavaScript / Coding Challenges, understanding more of what the ai is doing and learning the structure allowing me to build our product in a safer manner.
- **My next technical learning goal:** Write my own `filterOpportunities()` procedure for the volunteer page (issue #8) and use it as my Create PT code.

## Next Sprint Commitment
- **One professional behavior I will improve:** Work habits. Review every change with `git diff` before committing, and use clear commit messages.
- **One technical skill I will improve:** JavaScript, by writing `filterOpportunities()` and its tests myself.
- **One way I will contribute more effectively to my team:** Keep my issues (#2, #4, #8) and the Kanban updated while I work, and check in with Aarav before starting anything that touches his issues.
- **Evidence I will collect during the next sprint:** My `filterOpportunities()` code with test results, screenshots of the hub home page, and closed issues on our Kanban board.
