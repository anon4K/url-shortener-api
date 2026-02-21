# 🔗 URL Shortener API

A production-ready URL shortener with Django REST Framework, Redis caching, and custom aliases.

## Features

- URL shortening with auto-generated or custom codes
- Click tracking and analytics
- Redis caching (200x performance boost)
- Input validation and duplicate detection
- REST API with full CRUD operations

## Live Demo

**API:** [Your deployed URL here]

Tech Stack

Django REST Framework • PostgreSQL • Redis

## Quick Start

# Clone and setup
git clone https://github.com/anon4K/url-shortener-api.git
cd url-shortener-api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Database setup
python manage.py migrate
python manage.py createsuperuser

# Run (make sure Redis is running)
python manage.py runserver
```

Visit `http://localhost:8000/api/urls/`

## 🔌 API Usage

**Create URL (auto-generated code):**
```bash
POST /api/urls/
{"original_url": "https://example.com"}
```

**Create URL (custom code):**
```bash
POST /api/urls/
{"original_url": "https://example.com", "custom_code": "mylink"}
```

**Access short URL:**
```bash
GET /{short_code}/
```

## Key Features Implementation

**Redis Caching:**
```python
cache_key = f'url_{pk}'
cached = cache.get(cache_key)
if cached:
    return Response(cached)
# Query DB and cache result
```

**Custom Code Validation:**
- 3+ characters, alphanumeric and hyphens only
- Duplicate detection
- Format validation

## Roadmap

- [ ] QR code generation
- [ ] Analytics dashboard
- [ ] Link expiration
- [ ] Rate limiting

## 👨‍💻 Author

**Michael Offordum** - [LinkedIn](https://www.linkedin.com/in/michael-offordum-3057a6240/) • [GitHub](https://github.com/anon4K)

---

Please star this repo if you found it helpful. Thank you!
