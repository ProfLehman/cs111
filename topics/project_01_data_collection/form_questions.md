# Microsoft Forms — Designing Good Data Collection Questions

Microsoft Forms can be used to collect several different types of data. Choosing the right question type will make your data easier to summarize, graph, and analyze later.

---

## Microsoft Forms Question Types

| Question Type          | Description                                        | Example                                             |
| ---------------------- | -------------------------------------------------- | --------------------------------------------------- |
| **Choice**             | Select one or more predefined choices              | What is your class year?                            |
| **Text**               | Enter a short or long response                     | How many hours do you sleep each night?             |
| **Rating**             | Select a rating using numbers or stars             | Rate your satisfaction with campus dining.          |
| **Date**               | Select a calendar date                             | When did you last attend a campus event?            |
| **Ranking**            | Put several choices in order                       | Rank these activities from most to least preferred. |
| **Likert**             | Respond to several statements using the same scale | Strongly Disagree to Strongly Agree                 |
| **File Upload**        | Upload a file as part of the response              | Upload a photograph or document.                    |
| **Net Promoter Score** | Give a 0–10 recommendation rating                  | How likely are you to recommend this service?       |

**Section** can also be used to organize a longer form into groups of questions.

---

## Most Useful Types for Our Data Project

For most CS 111 projects, you will primarily use:

* **Choice** — useful for categorical data
* **Text with a number restriction** — useful for numerical data
* **Rating** — useful for ratings and scales

Other question types can be used when they make sense for your project.

---

## Choice Questions — One Answer or Multiple Answers?

Microsoft Forms **Choice** questions can allow either:

* **One answer** — displayed as **radio buttons**
* **Multiple answers** — displayed as **checkboxes**

### Radio Buttons — Choose One

Use radio buttons when the respondent should select **one category**.

Example:

**What is your current class year?**

* ○ First-year
* ○ Sophomore
* ○ Junior
* ○ Senior
* ○ Other

Each respondent should belong to only one category.

Another example:

**What is your primary method of transportation to campus?**

* ○ Drive myself
* ○ Ride with someone else
* ○ Walk
* ○ Bicycle
* ○ Other

The word **primary** indicates that only one response should be selected.

---

### Checkboxes — Select All That Apply

Use checkboxes when more than one answer may legitimately apply.

Example:

**Which streaming services do you currently use? Select all that apply.**

* ☐ Netflix
* ☐ Hulu
* ☐ Disney+
* ☐ Max
* ☐ Prime Video
* ☐ Other

A respondent may select several answers.

---

### Match the Question to the Response Type

**Bad:**

**What is your favorite streaming service? Select all that apply.**

"Favorite" suggests one answer, while "select all that apply" allows several.

**Better:**

**What is your favorite streaming service?**

→ Use **radio buttons**

or

**Which streaming services do you currently use? Select all that apply.**

→ Use **checkboxes**

---

### Think About the Data

Radio-button questions usually produce simpler data:

```text
Sophomore
```

Checkbox questions may produce several values for one respondent:

```text
Netflix; Disney+; Prime Video
```

Multiple-answer questions can be useful, but they are somewhat more complicated to analyze.

> **Use radio buttons when one response answers the question. Use checkboxes only when respondents genuinely need to select multiple answers.**

---

# Designing Good Questions

A good question should:

* Collect data that is useful for your project.
* Clearly tell respondents what information to provide.
* Use an appropriate Microsoft Forms question type.
* Produce responses that will be easy to analyze.
* Avoid collecting unnecessary personal information.

Before adding a question, ask:

> **What will I do with this variable when I analyze my data?**

---

## Example 1 — Collect Numerical Data

### Bad Question

**How much do you sleep?**

Possible answers:

* `a lot`
* `not enough`
* `7-8`
* `about seven hours`

### Better Question

**On average, how many hours of sleep do you get per night?**

* Type: **Text**
* Restriction: **Number**

Example response:

`7.5`

### Why is this better?

The responses will contain consistent numerical values that can be:

* Averaged
* Graphed
* Compared with another variable

---

## Example 2 — Clearly Specify Units

### Bad Question

**How much do you exercise each week?**

Possible responses:

* `3`
* `a little`
* `2 hours`
* `five days`

What does `3` mean?

### Better Question

**Approximately how many minutes do you exercise during a typical week?**

* Type: **Text**
* Restriction: **Number**

Example:

`150`

### Key Idea

Always make the **unit of measurement** clear.

---

## Example 3 — Collect Categorical Data

### Bad Question

**What year are you?**

* Type: Text

Possible responses:

* `Freshman`
* `freshman`
* `First year`
* `1st year`
* `2029`

### Better Question

**What is your current class year?**

* First-year

* Sophomore

* Junior

* Senior

* Other

* Type: **Choice**

### Why is this better?

Everyone selects from the same categories, making the data easier to count and graph.

---

## Example 4 — Avoid Overlapping Categories

### Bad Question

**How many hours per day do you use social media?**

* 0–1 hours
* 1–2 hours
* 2–3 hours
* 3+ hours

### Problem

Where should someone who uses social media exactly **2 hours** respond?

The categories overlap.

### Better Choice Version

**Approximately how many hours per day do you use social media?**

* Less than 1 hour
* 1 to less than 2 hours
* 2 to less than 3 hours
* 3 hours or more

### Even Better for This Project

Ask for the actual number:

**Approximately how many hours per day do you use social media?**

* Type: **Text**
* Restriction: **Number**

Example:

`2.5`

---

## Example 5 — Don't Turn Numbers into Categories Too Soon

### Not Ideal

**How many hours do you sleep each night?**

* Less than 5 hours
* 5–6 hours
* 7–8 hours
* More than 8 hours

This works, but some information is lost.

A student sleeping **7 hours** and a student sleeping **8 hours** are placed in the same category.

### Better

**On average, how many hours do you sleep each night?**

Example:

`7.5`

### Key Idea

When something can naturally be measured as a number, consider collecting the **actual numerical value**.

You can always create categories later.

---

## Example 6 — Use "Other" Appropriately

### Bad Question

**What is your primary way of getting to campus?**

* Car
* Other

### Better Question

**What is your primary way of getting to campus?**

* Drive myself
* Ride with someone else
* Walk
* Bicycle
* University transportation
* Other

### Key Idea

Include common or expected responses as regular categories.

Use **Other** for responses that you cannot reasonably anticipate.

---

## Example 7 — Avoid Unnecessary Free-Text Categories

### Bad Question

**What streaming service do you use most often?**

* Type: Text

Possible responses:

* `Netflix`
* `netflix`
* `NETFLIX`
* `Netflix and Hulu`
* `I mostly watch YouTube`

### Better Question

**Which streaming service do you use most often?**

* Netflix

* Hulu

* Disney+

* Max

* Prime Video

* YouTube

* Other

* I do not use a streaming service

* Type: **Choice**

### Key Idea

If you already know the likely categories, use **Choice** rather than Text.

---

## Example 8 — Avoid Leading Questions

### Bad Question

**Don't you think students who get enough sleep perform better academically?**

### Problem

The wording suggests the answer that the researcher expects.

### Better Approach

Collect the variables separately.

**On average, how many hours do you sleep each night?**

and

**Approximately how many hours per week do you spend studying outside of class?**

Then examine the data for possible relationships.

### Key Idea

Ask questions that collect the data.

Let the **data** help answer your research question.

---

## Example 9 — Don't Ask Two Questions at Once

### Bad Question

**How satisfied are you with campus food and housing?**

### Problem

A student might:

* Like campus housing
* Dislike campus food

One rating cannot accurately represent both opinions.

### Better

**How satisfied are you with campus dining?**

* Rating: 1–5

If housing is important to the project, ask it as a separate question:

**How satisfied are you with campus housing?**

* Rating: 1–5

### Key Idea

A question should normally measure **one thing at a time**.

---

## Example 10 — Avoid Unnecessary Personal Information

### Bad Questions

**What is your name?**

**What is your Huntington University email address?**

### Ask Yourself

Do you actually need this information to answer your project question?

For most CS 111 projects, the answer is **no**.

### Better

Do not ask for identifying information unless it is actually necessary.

Responses should normally be anonymous.

---

## Example 11 — Make Questions Relevant to the Project

Suppose your project question is:

> **Is there a relationship between sleep and caffeine consumption among college students?**

Useful questions might include:

1. **On average, how many hours do you sleep each night?**

   * Numerical

2. **How many caffeinated beverages do you drink on a typical day?**

   * Numerical

3. **What time do you usually go to bed on a weeknight?**

   * Choice

4. **What is your current class year?**

   * Choice

5. **How would you rate the quality of your sleep?**

   * Rating

---

## What About This Question?

**What is your favorite color?**

This is a perfectly reasonable survey question.

But...

> **How will favorite color help us investigate sleep and caffeine consumption?**

It probably will not.

### Key Idea

Do not add questions simply to make your form longer.

Every variable should have a reason for being included.

---

# Good Question Checklist

Before adding a question to your form, ask:

* Is this information useful for my project?
* Is the question clear?
* Are the units clear for numerical data?
* Am I using the best Microsoft Forms question type?
* Would predefined choices produce better data than a text response?
* Do my categories overlap?
* Am I asking only one thing?
* Is the wording neutral rather than leading?
* Am I collecting unnecessary personal information?
* Will I be able to analyze this variable later?

---

# Remember

Your goal is **not simply to create a survey**.

Your goal is to:

1. Identify something you want to investigate.
2. Decide what data you need.
3. Design questions that collect that data.
4. Collect consistent and usable responses.
5. Analyze those responses later using spreadsheets, web pages, and Python.
f
