# Microsoft Forms Template: Process & Call Log

Use this template to build a Microsoft Form where users:
1. Select their name,
2. Select one or more processes,
3. Enter total counts per selected process,
4. Enter call details (only if they had calls).

---

## Form Title
**Daily Process and Call Tracker**

## Form Description
Please submit your daily process counts. If you handled any calls, provide call details in the final section.

---

## Section 1: Employee Details

### Q1. Employee Name
- **Type:** Choice (Drop-down)
- **Required:** Yes
- **Options (example):**
  - Alice Johnson
  - Bob Smith
  - Charlie Lee
  - Diana Patel
  - Ethan Brown

> Tip: Keep "Drop-down" enabled so the list stays clean.

---

## Section 2: Process Selection

### Q2. Which process(es) did you work on today?
- **Type:** Choice
- **Allow multiple answers:** Yes
- **Required:** Yes
- **Options (example):**
  - Onboarding
  - Verification
  - Claims
  - Billing
  - Escalations

---

## Section 3: Process Counts

> Microsoft Forms cannot create fully dynamic repeated fields based on multiple selections. Use fixed numeric fields and instruct users to fill only selected processes.

### Q3. Onboarding Count
- **Type:** Text
- **Restrictions:** Number
- **Required:** No

### Q4. Verification Count
- **Type:** Text
- **Restrictions:** Number
- **Required:** No

### Q5. Claims Count
- **Type:** Text
- **Restrictions:** Number
- **Required:** No

### Q6. Billing Count
- **Type:** Text
- **Restrictions:** Number
- **Required:** No

### Q7. Escalations Count
- **Type:** Text
- **Restrictions:** Number
- **Required:** No

### Q8. Total Count (All Processes)
- **Type:** Text
- **Restrictions:** Number
- **Required:** Yes

---

## Section 4: Call Details

### Q9. Did you handle any calls today?
- **Type:** Choice
- **Required:** Yes
- **Options:**
  - Yes
  - No

### Branching from Q9
- If **Yes** → Go to call details questions (Q10–Q13)
- If **No** → Go to Submit

### Q10. Number of Calls Handled
- **Type:** Text
- **Restrictions:** Number
- **Required:** Yes (when Q9 = Yes)

### Q11. Total Call Duration (minutes)
- **Type:** Text
- **Restrictions:** Number
- **Required:** Yes (when Q9 = Yes)

### Q12. Call Types Handled
- **Type:** Choice
- **Allow multiple answers:** Yes
- **Required:** No
- **Options (example):**
  - Inbound
  - Outbound
  - Follow-up
  - Escalation Call

### Q13. Call Notes / Details
- **Type:** Long answer text
- **Required:** No
- **Prompt example:** Mention key customer issue, resolution, and any follow-up needed.

---

## Recommended Validation Rules

- For all count and duration fields, set **Number** restrictions.
- In form description, add this instruction:
  - "Fill process counts only for the processes you selected in Question 2."
- Optionally make `Total Count` checked later in Excel/Power Automate against process subtotals.

---

## Optional Enhancement (Power Automate)

After submission, create a flow to:
1. Store responses in Excel/SharePoint,
2. Calculate per-user productivity,
3. Flag mismatches where `Total Count` ≠ sum of individual process counts,
4. Send daily summary to team lead.

