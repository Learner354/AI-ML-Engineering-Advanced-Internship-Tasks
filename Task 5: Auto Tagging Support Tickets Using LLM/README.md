#  Auto Tagging Support Tickets Using LLMs

##  Problem Statement

In customer support systems, manually tagging support tickets by category (e.g., Billing, Technical, Account) is time-consuming and inconsistent. Automating this process helps route issues faster, improve response time, and enable better analytics.

---

##  Objective

The objective of this project is to **automatically classify (tag) support tickets into categories** using a Large Language Model (LLM) with:

- **Zero-shot** prompting
- **Few-shot** prompting (with examples)

No model training was required, allowing for quick setup and high-quality results using state-of-the-art LLM inference.

---

## 🗂️ Dataset

A small sample dataset was created with 5–10 synthetic support ticket examples covering categories like:

- `Billing`
- `Technical`
- `Account`
- `Service`
- `Upgrade`

Each ticket is a short sentence describing a customer's issue.

---

##  Methodology

### Zero-Shot Classification

- Used GPT-4 via the OpenAI API with a prompt that lists candidate tags.
- The model is asked to select the **top 3 most relevant tags** for each ticket.

### Few-Shot Classification

- Added a few labeled examples to the prompt (few-shot learning).
- Improves accuracy by giving the model context on how to tag.

---

## Technology Stack

- Python 3
- OpenAI GPT-4 (`openai` SDK with custom base URL)
- Pandas for data manipulation

---

## 📈 Output Example

| Ticket                                           | Zero-Shot Tags             | Few-Shot Tags              |
|--------------------------------------------------|-----------------------------|-----------------------------|
| My internet is down since morning.              | Technical, Service, Account | Technical, Service, Account |
| I want to change my billing address.            | Billing, Account, Service   | Billing, Account, Service   |

---

## Summary

This project demonstrates a **quick and effective LLM-based solution** for automating ticket tagging using both zero-shot and few-shot learning techniques. It avoids model training entirely, relying on prompt engineering to deliver intelligent multi-label classification in seconds.

---

## Skills Applied

- Prompt Engineering
- LLM Text Classification
- Zero-shot and Few-shot Learning
- Multi-class Prediction and Ranking
