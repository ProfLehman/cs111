# PROJECT-03 – Web Page Presenting Data and Results

**CS 111 – Introduction to Computer Science**

**75 Points**

**Due: Tuesday, November 24th (day before Thanksgiving Break)**

## Overview

Create and publish a website that presents the data, analysis, charts, and conclusions from your semester data project. You will use the data and results from Project 02 to build a website using HTML, CSS, and Chart.js.

Your website must be published using GitHub Pages and accessible through a public URL.

## Project Requirements

### 1. Website Content and Organization (25 points)

Create a website with at least **four HTML pages**:

- **Home Page (`index.html`) – 5 points:** Introduce your project, explain the purpose of your survey or data collection, and describe the questions you wanted to investigate.
- **Data and Analysis (`analysis.html`) – 8 points:** Explain how you collected your data, how many responses you received, and how you analyzed the data using Excel. Include a link to download your public-use data as a `.csv` file. This must be a cleaned-up copy of your data with names, email addresses, and other identifying information removed.
- **Charts (`charts.html`) – 6 points:** Display three charts using Chart.js, representing at least two different chart types. Charts should be based on the data and analysis from Project 02 and include descriptive titles and labels.
- **Results and Conclusions (`results.html`) – 6 points:** Summarize your findings, explain what you learned from the data, and discuss any limitations or interesting observations.

You may reuse and adapt written material, calculations, and results from Project 02.

### 2. HTML and Navigation (10 points)

- Use HTML to organize content with headings, paragraphs, lists, and links as appropriate.
- Include a navigation menu on every page with working links to the other pages.
- Use descriptive page titles and meaningful headings.
- Ensure all links work correctly.

### 3. CSS Formatting (10 points)

- Create one external CSS file (`style.css`) used by all four HTML pages.
- Use at least **five different CSS properties** to format your website.
- Apply consistent formatting across all pages.
- Make the website readable and visually organized.

Examples of CSS properties include `background-color`, `color`, `font-family`, `font-size`, `margin`, `padding`, `border`, and `text-align`.

### 4. Charts Using Chart.js (20 points)

- Implement **three charts** using the Chart.js JavaScript library.
- Use at least **two different types of charts** (for example, bar, pie, line, or doughnut).
- Charts must display actual results from Project 02.
- Include appropriate chart titles, labels, and legends where applicable.
- Manually enter the chart data into your JavaScript code using values calculated in Project 02. You are not required to read data directly from the CSV file.
- All three charts must display correctly when the website is opened through GitHub Pages.


**Chart.js Library:** You do not need to download or upload the Chart.js library. Reference it using a Content Delivery Network (CDN) by including the following line in your `charts.html` file:

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```
Place this line before your JavaScript code that creates the charts. You may write your chart code directly in `charts.html` using `<script>` tags.


### 5. GitHub Publishing and Submission (10 points)

- Upload all HTML, CSS, JavaScript (if separate), and public-use CSV files to a GitHub repository.
- Publish the website using GitHub Pages.
- Verify that all four pages, navigation links, charts, and CSV download work correctly.
- Submit the **public GitHub Pages URL** through Moodle.

## Grading Summary

| Category                         | Points |
| -------------------------------- | ------ |
| Website Content and Organization | 25     |
| HTML and Navigation              | 10     |
| CSS Formatting                   | 10     |
| Chart.js Charts                  | 20     |
| GitHub Publishing and Submission | 10     |
| **Total**                        | **75** |

## Additional Notes

- You may use AI tools to assist with HTML, CSS, JavaScript, and debugging. You must understand the code you submit and be able to explain how your website works.
- You are not required to collect new data or perform additional Excel calculations.
- You may reuse the three charts and results from Project 02, but the charts must be implemented using Chart.js rather than simply displaying images of Excel charts.
- The CSV file must be suitable for public sharing. Remove identifying information about respondents and review any free-text responses for potentially identifying details before publishing.
- Elaborate website designs and advanced JavaScript programming are not required. The primary goal is to communicate your data and findings clearly.


## Suggested Project File Structure

Organize your website files in a single folder as shown below.

```text
project03/
│
├── index.html       # Home page
├── analysis.html    # Data collection and analysis
├── charts.html      # Three Chart.js charts
├── results.html     # Results and conclusions
├── style.css        # Shared CSS stylesheet
├── data.csv         # Public-use CSV (identifying information removed)
```

**Notes:**
- All four HTML pages must use the same `style.css` file.
- The `charts.js` file is optional. JavaScript code may be included directly in `charts.html`.
- The `data.csv` file must be available for download from `analysis.html`.
- Your GitHub repository may contain additional files if needed.

-- end --