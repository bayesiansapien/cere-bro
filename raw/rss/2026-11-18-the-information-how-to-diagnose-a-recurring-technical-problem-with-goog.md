---
source: farmer/rss
feed: the-information
farmed: 2026-11-19T05:43:16.598167+00:00
title: "How to Diagnose a Recurring Technical Problem with Google Gemini"
url: https://www.theinformation.com/articles/diagnose-recurring-technical-problem-google-gemini
published: 2026-11-18
author: The Information Partnerships
---

# How to Diagnose a Recurring Technical Problem with Google Gemini

<p>Persistent IT problems can drain employee productivity and strain help desk teams.</p>

<p>And while a  one-off technology problem often amounts to little more than a nuisance, recurring problems often have a real impact on the business. Imagine, for instance, that you run IT support for your company, and employees keep reporting that their VPN connections are dropping, locking remote workers out of company systems. Even with your IT team helping one user after another, the tickets keep piling up, and the underlying issue remains unaddressed.</p>

<p>Google Gemini can help IT teams sort through this information, spot patterns, and identify the root of the problem to help the organization get back to business.</p>

<p><strong>Step 1: Define the Problem</strong></p>

<p>First, you’ll want to use Gemini to cut through the chaos of helpdesk logs to better understand the frequency of the issue and create a consolidated dataset for further analysis. Take a screenshot of the error message that your users are getting, and export data from recent support tickets into a Google Sheet. Then, ask Gemini to compare the ticket data against the error message.</p>

<p>Try this prompt:</p>

<p><em>You are a Level 2 debugging specialist. Analyze the attached error screenshot to identify the exact error code or message. Using this key, review the attached support tickets from the last 60 days and find all tickets that contain the identical error message. Output the results as a table.</em></p>

<p><strong>Step 2: Hunt for Root Cause</strong></p>

<p>From a dataset of 500 help tickets, Gemini might identify two dozen or so dropped VPN connections, providing a table that identifies the ticket number, date, and location of each. This narrower dataset will make it easier to find out what the tickets have in common (and, therefore, what might be causing the problem).</p>

<p>Your ticket export should already include each employee’s operating system, VPN client version, and location. To see what the affected employees have in common, prompt Gemini again:</p>

<p><em>You are a technical data analyst. Analyze the consolidated ticket data to identify statistically significant correlations between the ‘VPN connection dropping’ issue and the following attributes: operating system, VPN client version, and user geolocation. Format the findings as a ranked list, stating the calculated confidence level for each correlation.</em></p>

<p>The results of this step can be extremely revealing. For example, Gemini might note that only macOS users running a particular client version are experiencing the problem.</p>

<p><strong>Step 3: Identify the Solution</strong></p>

<p><br />The good news is that your helpdesk team has already solved users’ VPN problem multiple times. However, it’s likely this is the first time anyone has looked at all of these tickets together, since they were previously scattered among tickets for various one-off problems. Therefore, it’s highly possible no one in the organization knows the most common fix, even if your helpdesk has already applied that solution over and over again.</p>

<p>In your Gemini chat, type:</p>

<p><em>From the ‘Resolution Notes’ field of all closed tickets in the consolidated data, extract and rank the top 5 most successful, non-escalated troubleshooting actions that resolved the ‘VPN connection dropping’ issue. Output the steps as a numbered list, including the calculated frequency/success rate for each step.</em></p>

<p>Gemini will identify which fixes have been tried and list their success rates. For example, Gemini might note that every resolved ticket required the user to install a new client version and clear the macOS DNS cache.</p>

<p><strong>Step 4: Create a Playbook</strong></p>

<p>Now that you know how often VPN connections are dropping, what is causing the problem, and how it has been fixed in the past, you can give your frontline technicians a clear, repeatable playbook for handling the issue. This will ensure that the problem gets fixed quickly, without unnecessary escalation to senior engineers.</p>

<p>Gemini can quickly draft a playbook with desired content, length, and tone. Try this prompt:</p>

<p><em>You are a Level 2 technical writer. Draft an updated, internal-facing knowledge base article titled ‘Resolving recurring VPN drops: root cause analysis and Tier 1 triage.’ Structure the article with two main sections: ‘Summary of root cause’ and ‘Tier 1 troubleshooting steps.’ The tone must be concise and instructional, explicitly targeting Level 1 helpdesk technicians.</em></p>

<p>The playbook will give your technicians exactly the information they’ll need when the issue pops up again in the future. And a problem that previously robbed teams of hours of productive time each month will instead be resolved in minutes.</p>
