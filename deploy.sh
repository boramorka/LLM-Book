#!/bin/bash

echo "🚀 Building multilingual site for GitHub Pages deployment..."

# Clean previous builds
rm -rf site

# Build main landing page
echo "📄 Building main landing page..."
mkdocs build

# Build English version in subdirectory
echo "🇺🇸 Building English version..."
mkdocs build -f mkdocs-en.yml

# Build Russian version in subdirectory  
echo "🇷🇺 Building Russian version..."
mkdocs build -f mkdocs-ru.yml

# Verify structure
echo "📁 Site structure:"
find site -type f -name "index.html" | head -10

echo "✅ Build complete! Site ready in ./site/"
echo ""
echo "🌐 Local testing URLs:"
echo "   Main: file://$(pwd)/site/index.html"
echo "   English: file://$(pwd)/site/en/index.html" 
echo "   Russian: file://$(pwd)/site/ru/index.html"
echo ""
echo "📤 To deploy to GitHub Pages:"
echo "   git add site/"
echo "   git commit -m 'Deploy multilingual site'"
echo "   git subtree push --prefix site origin gh-pages"
