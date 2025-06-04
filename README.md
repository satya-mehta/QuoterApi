# QuoterAPI

QuoterAPI is a lightweight, fast, and searchable REST API for quotes built using Flask.  
It supports filtering by tags, quote length, authors, and more — making it perfect for your apps, websites, or just daily inspiration.

🔗 **Live Demo:**  
[![Test API](https://img.shields.io/badge/Launch%20API-quoterapi.onrender.com-blue?logo=flask)](https://quoterapi.onrender.com/quotes/random)

---

## 🚀 Base URL

```
https://quoterapi.onrender.com
```

---

## 📚 Endpoints

### 1. `GET /quotes/random`

Returns one or more random quotes.

#### 🔸 Query Parameters

| Parameter   | Type   | Description                                                |
|-------------|--------|------------------------------------------------------------|
| `tags`      | string | Filter by one or more tags (comma-separated).              |
| `maxlength` | int    | Only include quotes with this max length.                  |
| `limit`     | int    | Number of quotes to return (default = 1).                  |

#### 🔹 Example Queries

- **One random quote:**  
  [`/quotes/random (try)`](https://quoterapi.onrender.com/quotes/random)

- **Quote tagged 'war':**  
  [`/quotes/random?tags=war (try)`](https://quoterapi.onrender.com/quotes/random?tags=war)

- **Multiple tags:**  
  [`/quotes/random?tags=freedom,war (try)`](https://quoterapi.onrender.com/quotes/random?tags=freedom,war)

- **Quote with max 80 chars:**  
  [`/quotes/random?maxlength=80 (try)`](https://quoterapi.onrender.com/quotes/random?maxlength=80)

- **Top 5 short inspirational quotes:**  
  [`/quotes/random?tags=inspirational&maxlength=100&limit=5 (try)`](https://quoterapi.onrender.com/quotes/random?tags=inspirational&maxlength=100&limit=5)

---

### 2. `GET /api/search`

Search for quotes by author or single tag.

#### 🔸 Query Parameters

| Parameter | Type   | Description                             |
|-----------|--------|-----------------------------------------|
| `author`  | string | Filter quotes by author's name          |
| `tag`     | string | Filter quotes by a single tag           |

#### 🔹 Example Queries

- [`/api/search?author=orwell (try)`](https://quoterapi.onrender.com/api/search?author=orwell)  
- [`/api/search?tag=inspirational (try)`](https://quoterapi.onrender.com/api/search?tag=inspirational)  
- [`/api/search?author=george&tag=war (try)`](https://quoterapi.onrender.com/api/search?author=george&tag=war)

Returns up to 10 matching quotes.

---

### 3. `GET /api/quote/<index>`

Returns a quote by its index number.

- Example:  
  [`/api/quote/100 (try)`](https://quoterapi.onrender.com/api/quote/100)

---

## 🧠 Features

- 🔎 Search quotes by **tags**
- ✍️ Filter by **author**
- 📏 Quote **length filtering** with `maxlength`
- 🎯 Get **multiple** quotes at once using `limit`
- 💾 Built on a dataset of over **2500 curated quotes**
- 🚀 Hosted on **Render**

---

## 🔧 Tech Stack

- Python 3
- Flask
- Render (deployment)

---

## 📂 Dataset Format

Each quote in the dataset follows this structure:

```json
{
  "index": 92,
  "quote": "War is peace",
  "author": "George Orwell",
  "tags": ["freedom;ignorance;inspirational;war"],
  "likes": 6103
}
```

> Internally parsed to allow filtering by individual tags.

---

## 📬 Contact

Made with ❤️ by [Satya Mehta]

---