# Build Instructions

## Overview

This project has separate configurations for different languages:
- `mkdocs.yml` - Main landing page
- `mkdocs-en.yml` - English version
- `mkdocs-ru.yml` - Russian version

## Building

### Build All Versions
```bash
./build.sh
```

### Build Individual Versions
```bash
# Main landing page
mkdocs build

# English version
mkdocs build -f mkdocs-en.yml

# Russian version
mkdocs build -f mkdocs-ru.yml
```

## Development Servers

### Serve Individual Languages
```bash
# Russian version (localhost:8001)
./serve-ru.sh

# English version (localhost:8002)
./serve-en.sh

# Main page (localhost:8000)
mkdocs serve
```

## Site Structure

After building, the site structure will be:
```
site/
├── index.html          # Main landing page
├── en/                 # English version
│   ├── index.html
│   ├── CHAPTER-1/
│   ├── CHAPTER-2/
│   └── CHAPTER-3/
├── ru/                 # Russian version
│   ├── index.html
│   ├── CHAPTER-1/
│   ├── CHAPTER-2/
│   └── CHAPTER-3/
└── assets/            # Shared assets
```

## Language Navigation

Each language version has its own:
- Navigation structure (in the respective language)
- Content files (from `docs/en/` or `docs/ru/`)
- Search functionality
- Language switcher in the header
