#!/usr/bin/env python3
"""
Full import script to pull all 4,836+ posts from tarothappy.com into Jekyll _posts
"""
import os
import sys
import json
import re
import time
import html
import urllib.request
import urllib.error
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
from markdownify import markdownify as md

WORKSPACE_DIR = "/home/reecewilliams8/dev work/repos/tarot"
POSTS_DIR = os.path.join(WORKSPACE_DIR, "_posts")
CARTOMANCY_IMG_DIR = os.path.join(WORKSPACE_DIR, "assets", "images", "cartomancy")
TAROT_IMG_DIR = os.path.join(WORKSPACE_DIR, "assets", "images", "tarot")
os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(TAROT_IMG_DIR, exist_ok=True)

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'

def get_json(url):
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode('utf-8'))
        except Exception as e:
            time.sleep(1.5 * (attempt + 1))
            if attempt == 3:
                raise e

def get_categories():
    print("Fetching categories...")
    url = "https://tarothappy.com/wp-json/wp/v2/categories?per_page=100"
    data = get_json(url)
    return {c['id']: c['slug'] for c in data}

def clean_title(title_rendered):
    t = html.unescape(title_rendered or "")
    t = t.replace('"', '\\"').replace('\n', ' ').strip()
    return t

def extract_first_paragraph(soup):
    for p in soup.find_all('p'):
        text = p.get_text().strip()
        if text and len(text) > 30:
            clean = html.unescape(text).replace('"', '\\"').replace('\n', ' ')
            return clean[:280]
    return ""

def download_image_if_needed(img_url, dest_dir):
    filename = img_url.split('/')[-1]
    # strip resize query / dimensions if present
    clean_name = re.sub(r'-\d+x\d+(\.[a-zA-Z]+)$', r'\1', filename)
    local_target = os.path.join(dest_dir, clean_name)
    if os.path.exists(local_target) and os.path.getsize(local_target) > 0:
        return f"assets/images/tarot/{clean_name}"
    
    # Attempt download of full resolution (clean_name) or fallback to img_url
    download_url = img_url
    if clean_name != filename:
        download_url = img_url.replace(filename, clean_name)
        
    try:
        req = urllib.request.Request(download_url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read()
            with open(local_target, 'wb') as f:
                f.write(content)
            return f"assets/images/tarot/{clean_name}"
    except Exception:
        # Fallback to direct original img_url
        try:
            req = urllib.request.Request(img_url, headers={'User-Agent': USER_AGENT})
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read()
                with open(local_target, 'wb') as f:
                    f.write(content)
                return f"assets/images/tarot/{clean_name}"
        except Exception:
            return img_url

def find_featured_image(soup):
    img = soup.find('img')
    if img and img.get('src'):
        src = img['src']
        filename = src.split('/')[-1]
        clean_name = re.sub(r'-\d+x\d+(\.[a-zA-Z]+)$', r'\1', filename)
        
        # 1. Local cartomancy check
        if os.path.exists(os.path.join(CARTOMANCY_IMG_DIR, clean_name)):
            return f"assets/images/cartomancy/{clean_name}", img
        if os.path.exists(os.path.join(CARTOMANCY_IMG_DIR, filename)):
            return f"assets/images/cartomancy/{filename}", img
            
        # 2. Local tarot check
        if os.path.exists(os.path.join(TAROT_IMG_DIR, clean_name)):
            return f"assets/images/tarot/{clean_name}", img
            
        # 3. If remote WP uploads, download or keep reference
        if "tarothappy.com/wp-content/uploads" in src:
            local_rel = download_image_if_needed(src, TAROT_IMG_DIR)
            return local_rel, img
            
        return src, img
    return None, None

def html_to_markdown(html_content, remove_first_img=True):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    if remove_first_img:
        first_img = soup.find('img')
        if first_img:
            parent = first_img.parent
            first_img.decompose()
            if parent and parent.name in ['figure', 'p'] and not parent.get_text().strip() and not parent.find_all('img'):
                parent.decompose()
                
    text = md(str(soup), heading_style="ATX", bullets="-")
    text = re.sub(r'\n{3,}', '\n\n', text).strip()
    return text

def process_single_post(p, cats_map):
    post_id = p['id']
    date_str = p.get('date', '2023-01-01T00:00:00')
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
    except Exception:
        date_obj = datetime(2023, 1, 1, 0, 0, 0)
        
    date_prefix = date_obj.strftime("%Y-%m-%d")
    date_frontmatter = date_obj.strftime("%Y-%m-%d %H:%M:%S +0000")
    
    slug = p.get('slug') or f"post-{post_id}"
    title = clean_title(p['title'].get('rendered', slug))
    cat_slugs = [cats_map.get(cid, "uncategorised") for cid in p.get('categories', [])]
    
    content_html = p.get('content', {}).get('rendered', '')
    soup = BeautifulSoup(content_html, 'html.parser')
    first_para = extract_first_paragraph(soup)
    image_path, _ = find_featured_image(soup)
    markdown_body = html_to_markdown(content_html, remove_first_img=bool(image_path))
    
    filename = f"{date_prefix}-{slug}.md"
    filepath = os.path.join(POSTS_DIR, filename)
    
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
    return filename

def fetch_and_save_page(page_num, cats_map):
    url = f"https://tarothappy.com/wp-json/wp/v2/posts?per_page=100&page={page_num}"
    try:
        posts = get_json(url)
    except urllib.error.HTTPError as e:
        if e.code == 400: # Beyond total pages
            return []
        raise e
        
    saved = []
    for p in posts:
        try:
            fn = process_single_post(p, cats_map)
            saved.append(fn)
        except Exception as e:
            print(f"Error processing post {p.get('id')}: {e}")
    return saved

def main():
    cats_map = get_categories()
    
    # Determine total pages
    head_req = urllib.request.Request("https://tarothappy.com/wp-json/wp/v2/posts?per_page=100&page=1", headers={'User-Agent': USER_AGENT})
    with urllib.request.urlopen(head_req, timeout=20) as resp:
        total_posts = int(resp.headers.get('X-WP-Total', 4836))
        total_pages = int(resp.headers.get('X-WP-TotalPages', 49))
        
    print(f"Total posts to import: {total_posts} across {total_pages} pages.")
    start_time = time.time()
    
    completed_posts = 0
    # Use ThreadPoolExecutor to fetch batches concurrently
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_to_page = {executor.submit(fetch_and_save_page, p, cats_map): p for p in range(1, total_pages + 1)}
        for future in as_completed(future_to_page):
            page_num = future_to_page[future]
            try:
                saved = future.result()
                completed_posts += len(saved)
                elapsed = time.time() - start_time
                rate = completed_posts / max(elapsed, 0.1)
                print(f"[Page {page_num:02d}/{total_pages}] +{len(saved)} posts saved | Total: {completed_posts}/{total_posts} ({rate:.1f} posts/s)")
            except Exception as e:
                print(f"[Page {page_num:02d}] Failed: {e}")
                
    total_time = time.time() - start_time
    print(f"\n==================================================")
    print(f"Finished import: {completed_posts} posts saved in {total_time:.1f}s.")
    print(f"Posts directory: {POSTS_DIR}")
    print(f"==================================================")

if __name__ == "__main__":
    main()

