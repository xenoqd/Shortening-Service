# Shortening-Service

Shortening Service is a simple RESTful API that allows users to shorten long URLs

This API provides endpoints to create, retrieve, update and delete short URLs

Project based on <https://roadmap.sh/projects/url-shortening-service> challenge

## How to Run the Project

Requirements

- Python 3.8

- pip

- virtualenv

- Postgres

---

### 1. Clone the repository

```bash
git clone https://github.com/xenoqd/Caching-Proxy.git
cd Caching-Proxy
```

### 2. Create and activate a virtual environment

Windows

```bash
python -m venv venv
```

Linux / macOS

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run development server

```bash
fastapi dev main.py
```

## API Endpoints

Create Short URL

Endpoint: POST /shorten

Description: Create a new short URL for a given URL.

Request Body:

```json
{
  "url": "https://example.com/very/long/url"
}
```

Response:

```json
{
  "id": 1,
  "url": "https://example.com/very/long/url",
  "shortcode": "eFTDDC",
  "createdAt": "2026-01-17T07:01:38.181187",
  "updatedAt": null
}
```

---

Retrieve Original URL

Endpoint: GET /{shortcode}

Description: Retrieve the original URL using the shortcode.

Response:

```json
{
  "id": 7,
  "url": "https://example.com/very/long/url",
  "shortcode": "eFTDDC",
  "createdAt": "2026-01-17T07:01:38.181187",
  "updatedAt": null
}
```

---

Update Short URL

Endpoint: PUT /update/{shortcode}

Description: Update the original URL associated with a shortcode.

Request Body:

```json
{
  "url": "https://example.com/new-url"
}
```

Response:

```json
{
  "id": 1,
  "url": "https://example.com/new-url",
  "shortcode": "eFTDDC",
  "createdAt": "2026-01-17T07:01:38.181187",
  "updatedAt": "2026-01-17T07:17:49.773512"
}
```

---

Delete Short URL

Endpoint: DELETE /delete/{shortcode}

Description: Delete a short URL by its shortcode.

Response:

```json
{
  "message": "Short URL deleted successfully"
}
```

---

URL Statistics

Endpoint: GET /stats/{shortcode}

Description: Get statistics for a short URL and the number of times it has been accessed.

Response:

```json
{
  "id": 1,
  "url": "https://example.com/new-url",
  "shortcode": "eFTDDC",
  "createdAt": "2026-01-17T07:01:38.181187",
  "updatedAt": "2026-01-17T07:17:49.773512",
  "access_count": 0
}
```

---

URL Redirect

Endpoint: GET /{shortcode}

Description: Redirects the user to the original URL associated with the given shortcode. Each time the shortcode is accessed, the access count for that URL is incremented in Database.
