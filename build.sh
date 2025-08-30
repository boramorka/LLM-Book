#!/bin/bash

echo "Building all language versions..."

# Build main landing page
echo "Building main landing page..."
mkdocs build

# Build English version
echo "Building English version..."
mkdocs build -f mkdocs-en.yml

# Build Russian version
echo "Building Russian version..."
mkdocs build -f mkdocs-ru.yml

echo "All versions built successfully!"
echo "Main site: site/index.html"
echo "English: site/en/index.html"
echo "Russian: site/ru/index.html"
