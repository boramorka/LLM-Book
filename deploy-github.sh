#!/bin/bash

echo "🚀 Deploying to GitHub Pages..."

# Build all versions
./deploy.sh

# Deploy to GitHub Pages using subtree
echo "📤 Pushing to gh-pages branch..."
git add -A
git commit -m "Deploy multilingual documentation $(date)"

# Push the site directory to gh-pages branch
git subtree push --prefix site origin gh-pages

echo "✅ Deployment complete!"
echo "🌐 Your site will be available at: https://boramorka.github.io/LLM-book/"
