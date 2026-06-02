# URL Shortener

**Difficulty**: Medium  
**Skills**: HTTP APIs, JSON, random strings

## Spec

Build a CLI tool that wraps the [TinyURL](https://tinyurl.com) API (or similar) to shorten URLs.

### Features

```
python shorten.py https://example.com/very/long/url
# -> Shortened: https://tinyurl.com/abc123

python shorten.py --custom pyweek https://example.com/long
# -> Shortened: https://tinyurl.com/pyweek

python shorten.py --stats https://tinyurl.com/abc123
# -> Stats: 42 clicks
```

### Requirements

- Use `requests` library (install with `uv pip install requests`)
- Handle network errors gracefully
- Validate URLs before sending
- Save history to a JSON file so you can look up past shortened URLs
- Provide a `--list` flag to show all saved URLs

### Extension Ideas

- QR code generation (qrcode library)
- Bulk shorten from a file
- Self-hosted with FastAPI (stretch goal)
