# 🚀 Deployment Guide

## 📋 Overview

This multilingual MkDocs site has three deployment options:

## 🎯 Option 1: Manual Deployment (Recommended)

### Local Testing
```bash
# Test Russian version
mkdocs serve -f mkdocs-ru.yml -a localhost:8001

# Test English version  
mkdocs serve -f mkdocs-en.yml -a localhost:8002

# Test main landing page
mkdocs serve
```

### Build All Versions
```bash
./deploy.sh
```

### Deploy to GitHub Pages
```bash
./deploy-github.sh
```

## 🤖 Option 2: GitHub Actions (Automatic)

The `.github/workflows/deploy.yml` automatically builds and deploys on every push to main/master.

**Setup:**
1. Go to your repo → Settings → Pages
2. Set Source to "GitHub Actions"
3. Push to main branch
4. Site will be available at: `https://yourusername.github.io/repo-name/`

## 📁 Option 3: Manual GitHub Pages

If you prefer the classic `mkdocs gh-deploy`:

```bash
# Build all versions first
./deploy.sh

# Deploy using subtree
git add site/
git commit -m "Deploy documentation"
git subtree push --prefix site origin gh-pages
```

## 🌐 Site Structure

After deployment, your site will have:

```
https://yourdomain.com/
├── index.html          # Main landing page with language selection
├── en/                 # English version with full navigation
│   ├── index.html
│   ├── CHAPTER-1/
│   ├── CHAPTER-2/
│   └── CHAPTER-3/
├── ru/                 # Russian version with full navigation  
│   ├── index.html
│   ├── CHAPTER-1/
│   ├── CHAPTER-2/
│   └── CHAPTER-3/
└── assets/            # Shared assets
```

## ✅ What Works After Deployment

- ✅ Main page with language selection
- ✅ Full Russian navigation at `/ru/`
- ✅ Full English navigation at `/en/`
- ✅ Language switcher in each version
- ✅ Search functionality for each language
- ✅ Mobile-responsive design
- ✅ All Material theme features

## 🔧 Configuration Files

- `mkdocs.yml` - Main landing page
- `mkdocs-en.yml` - English version configuration
- `mkdocs-ru.yml` - Russian version configuration
- `deploy.sh` - Local build script
- `deploy-github.sh` - GitHub deployment script
- `.github/workflows/deploy.yml` - GitHub Actions workflow
