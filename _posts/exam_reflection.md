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
* **Learned what belongs in the frontend vs. the backend.** At one point too much got moved into the backend and the live site went blank without Flask running. Now I keep page text and fixed data in the frontend, and only shared or private data (users, roles, sign-ups) in the backend.
* **Learned to work within the class system.** At first we used ai to generate the frontend and it used its own colors instead of the teacher's SASS. I switched every color to the original template palette, so the site follows the system instead of fighting it.
* **Learned to prompt AI within requirements and to review what it does.** Giving AI clear rules (use the teacher's SASS, don't commit or push) got much better results, and checking every change with `git diff` before committing keeps mistakes off the live site.
* **Work habits I'm fixing:** smaller commits with clear messages (not "debugging"), and keeping issues and the Kanban updated while I work, not after.

## MCQ Retrospective

I rushed the practice test. I spent under 10 seconds on 29 of the 66 questions, so even the ones I got right don't really show what I know. My score was 50/66 (76%). My strongest areas were Algorithms & Programming (87%) and Networks (100%), and my weakest was **Data (50%)**, especially binary numbers, compression, and reading graphs. Nine of my 16 Data questions were ones I rushed, so that's where slowing down matters most. I'm redoing the rushed questions at 1–2 minutes each and writing out why each answer is right, starting with binary and data analysis.

## Team Improvements

As a team, Aarav and I got better at communicating and splitting work. Early on we both claimed the same issues (the resource finder and donation calculator), so we sorted it out and updated GitHub: Aarav took the Get Help Now finder, the donation calculator, and the accessibility audit, and I took volunteer signup, accounts and roles, and the donation needs board. I set up our GitHub organization, repos, and GitHub Pages deployment, then built the login page and connected it to our Flask backend. When we hit problems, like the site going blank and the colors not matching the teacher's SASS, we tracked down what caused them and fixed them within the repo's workflow instead of starting over.
