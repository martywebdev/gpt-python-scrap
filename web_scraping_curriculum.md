# 🕸️ Python Web Scraping Curriculum

## Step 1: Fundamentals (Static Pages)
**Goal**: Learn to fetch and parse HTML from static pages.
- Tools: `requests`, `BeautifulSoup`, `lxml`
- Practice Site: [Quotes to Scrape](https://quotes.toscrape.com)
- Exercise:
  - Scrape all quotes and authors.
  - Extract tags for each quote.
  - Save results to CSV.

---

## Step 2: Handle Authentication (Login Required)
**Goal**: Log into a site and scrape protected pages.
- Tools: `requests.Session`
- Practice Site: [Quotes Login](https://quotes.toscrape.com/login)
- Exercise:
  - Log in with credentials.
  - Scrape quotes available only after login.
  - Maintain session cookies across requests.

---

## Step 3: Scrape Dynamic Content (JavaScript Sites)
**Goal**: Learn to extract data from JS-rendered pages.
- Tools: `Selenium`, `Playwright`
- Practice Site: [Quotes JS](https://quotes.toscrape.com/js)
- Exercise:
  - Render page fully.
  - Extract quotes as before.
  - Compare HTML before and after JS execution.

---

## Step 4: Work with APIs
**Goal**: Detect and use hidden APIs instead of scraping HTML.
- Tools: `requests`
- Practice: Use DevTools (Network tab) to find JSON endpoints.
- Exercise:
  - Identify API calls from Quotes site.
  - Fetch and parse JSON directly.

---

## Step 5: Anti-Bot / Cloudflare Protection
**Goal**: Understand techniques for scraping protected sites.
- Tools: Playwright, proxies, CAPTCHA solvers.
- Strategy:
  - Rotate headers, user-agents, and IPs.
  - Slow down requests.
  - Prefer APIs where possible.
- ⚠️ Use demo/test sites only for practice.

---

## Step 6: Store & Use Data
**Goal**: Save scraped data in useful formats.
- Tools: `pandas`, `sqlite3`
- Exercise:
  - Store quotes in CSV.
  - Insert into SQLite database.
  - Query data for authors/keywords.

---

## 📍 Learning Path
1. **Static scraping** → quotes/books demo sites.
2. **Login sessions** → scrape behind auth.
3. **Dynamic scraping** → handle JS-rendered content.
4. **API sniffing** → use hidden JSON endpoints.
5. **Anti-bot basics** → understand Cloudflare & protections.
6. **Data storage** → save & query scraped results.

---

## ✅ Practice Sites (Safe & Legal)
- **Static**: [https://quotes.toscrape.com](https://quotes.toscrape.com)
- **Pagination**: [https://books.toscrape.com](https://books.toscrape.com)
- **Login**: [https://quotes.toscrape.com/login](https://quotes.toscrape.com/login)
- **Dynamic (JS)**: [https://quotes.toscrape.com/js](https://quotes.toscrape.com/js)

