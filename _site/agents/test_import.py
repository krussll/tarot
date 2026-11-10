#!/usr/bin/env python3
"""
Test script to import 10 posts from tarothappy.com into Jekyll _posts
"""
import os
import sys
import json
import re
import urllib.request
import html
from datetime import datetime
from bs4 import BeautifulSoup
from markdownify import markdownify as md

WORKSPACE_DIR = "/home/reecewilliams8/dev work/repos/tarot"
POSTS_DIR = os.path.join(WORKSPACE_DIR, "_posts")
CARTOMANCY_IMG_DIR = os.path.join(WORKSPACE_DIR, "assets", "images", "cartomancy")

# Fetch categories lookup
def get_categories():
    url = "https://tarothappy.com/wp-json/wp/v2/categories?per_page=100"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    return {c['id']: c['slug'] for c in data}

def clean_title(title_rendered):
    t = html.unescape(title_rendered)
    # If title has long pipes, e.g. "Drawing X and Y Together | What Do They Mean... | A Complete Guide"
    # Keep the full title or clean it appropriately
    return t.replace('"', '\\"')

def extract_first_paragraph(soup):
    for p in soup.find_all('p'):
        text = p.get_text().strip()
        if text and len(text) > 30:
            return text.replace('"', '\\"')
    return ""

def find_featured_image(soup, post):
    # Check if there is an image inside the post content
    img = soup.find('img')
    if img and img.get('src'):
        src = img['src']
        filename = src.split('/')[-1]
        # Clean off resizing dimensions like -1024x576
        clean_name = re.sub(r'-\d+x\d+(\.[a-zA-Z]+)$', r'\1', filename)
        
        # Check if clean_name exists in local cartomancy dir
        local_path = os.path.join(CARTOMANCY_IMG_DIR, clean_name)
        if os.path.exists(local_path):
            return f"assets/images/cartomancy/{clean_name}", img
        # Also check with exact filename
        if os.path.exists(os.path.join(CARTOMANCY_IMG_DIR, filename)):
            return f"assets/images/cartomancy/{filename}", img
            
        return src, img
    return None, None

def html_to_markdown(html_content, remove_first_img=True):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove the first main image if it will be used as featured image in Jekyll layout
    if remove_first_img:
        first_img = soup.find('img')
        if first_img:
            # If inside figure or p, remove parent if empty
            parent = first_img.parent
            first_img.decompose()
            if parent and parent.name in ['figure', 'p'] and not parent.get_text().strip() and not parent.find_all('img'):
                parent.decompose()
                
    # Convert remaining html to clean markdown
    text = md(str(soup), heading_style="ATX", bullets="-")
    # Clean up excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text).strip()
    return text

def run_test(count=10):
    cats_map = get_categories()
    url = f"https://tarothappy.com/wp-json/wp/v2/posts?per_page={count}"
    print(f"Fetching {count} posts from {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    posts = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    
    os.makedirs(POSTS_DIR, exist_ok=True)
    created_files = []
    
    for p in posts:
        post_id = p['id']
        date_str = p['date'] # e.g. "2023-08-16T09:01:32"
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
        date_prefix = date_obj.strftime("%Y-%m-%d")
        date_frontmatter = date_obj.strftime("%Y-%m-%d %H:%M:%S +0000")
        
        slug = p['slug']
        title = clean_title(p['title']['rendered'])
        
        # Categories
        cat_slugs = [cats_map.get(cid, "uncategorised") for cid in p.get('categories', [])]
        
        soup = BeautifulSoup(p['content']['rendered'], 'html.parser')
        first_para = extract_first_paragraph(soup)
        image_path, img_elem = find_featured_image(soup, p)
        
        # Convert content
        markdown_body = html_to_markdown(p['content']['rendered'], remove_first_img=bool(image_path))
        
        filename = f"{date_prefix}-{slug}.md"
        filepath = os.path.join(POSTS_DIR, filename)
        
        # Construct YAML Frontmatter
        frontmatter = [
            "---",
            "layout: post",
            f'title: "{title}"',
            f"date: {date_frontmatter}",
            f'slug: "{slug}"',
            f"author: reece",
        ]
        
        if image_path:
            frontmatter.append(f'image: "{image_path}"')
        if first_para:
            frontmatter.append(f'first_paragraph: "{first_para}"')
        if cat_slugs:
            cats_formatted = ", ".join(cat_slugs)
            frontmatter.append(f"categories: [ {cats_formatted} ]")
            
        frontmatter.extend([
            "comments: false",
            "---",
            "",
            markdown_body,
            ""
        ])
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(frontmatter))
            
        created_files.append(filename)
        print(f"Created: {filename} (Image: {image_path})")
        
    print(f"\nSuccessfully imported {len(created_files)} test posts.")
    return created_files

if __name__ == "__main__":
    run_test(10)
