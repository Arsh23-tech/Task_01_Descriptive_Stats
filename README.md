# Descriptive Analysis of Facebook Political Ads (2024)

## Project Overview
This project performs a comprehensive descriptive analysis of a dataset containing Facebook political advertisements related to the 2024 U.S. presidential election. The goal is to explore patterns in campaign messaging, topic focus, audience engagement strategies, and the tone of political discourse.

The analysis is conducted using both:
- Pure Python (manual statistical computation)
- Pandas (efficient data analysis)

Additionally, visualizations are created to highlight key insights.

---

## Dataset Description
The dataset consists of **246,745 political advertisements** with **40 features**, including:

- Ad metadata (ID, page, timestamps)
- Estimated impressions and spending
- Message types (advocacy, issue, attack, image)
- Policy topics (economy, health, immigration, etc.)
- Call-to-action indicators (fundraising, voting, engagement)
- Incivility indicators

---

## Project Structure
descriptive_stats_project/

data/
fb_ads_president_scored_anon.csv

pure_python_stats.py
pandas_stats.py
visualizations.py

output/
message_type_distribution.png
top_topics.png
incivility_rate.png

README.md
FINDINGS.md
COMPARISON.md

---

## How to Run the Project

### Step 1: Install dependencies

pip install pandas matplotlib

### Step 2: Run scripts in order

python pure_python_stats.py
python pandas_stats.py
python visualizations.py


---

## Visualizations

### Message Type Distribution
![Message Types](Output/message_type_distribution.png)

### Top Political Topics
![Topics](Output/top_topics.png)

### Incivility in Ads
![Incivility](Output/incivility_rate.png)

---

## Key Insights

- Political campaigns heavily rely on **advocacy and call-to-action messaging**
- **Economic and healthcare issues** dominate campaign narratives
- Social media ads are widely used for **fundraising and voter mobilization**
- A significant portion of ads contain **incivil or polarizing language**

---

## Pure Python vs Pandas

| Aspect | Pure Python | Pandas |
|------|------|------|
| Implementation | Manual | Automated |
| Complexity | High | Low |
| Speed | Slower | Faster |
| Transparency | High | Abstracted |

Using pure Python provided a deeper understanding of statistical computations, while Pandas significantly improved efficiency and scalability.

---

## Conclusion

This project demonstrates how descriptive statistics and exploratory data analysis can be used to understand political communication strategies. The findings highlight the role of social media in modern campaigns, particularly in persuasion, mobilization, and fundraising.

---

## Author
Arsh Chandrakar  
M.S. Information Systems (Data Science), Syracuse University
