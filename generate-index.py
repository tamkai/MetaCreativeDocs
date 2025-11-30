#!/usr/bin/env python3
"""
HTMLドキュメントのindexページを自動生成するスクリプト
docs/フォルダ内のHTMLファイルを検索し、index.htmlを生成します
日本語ファイル名は自動的にリネームします
"""

import os
import re
import json
import unicodedata
from datetime import datetime
from pathlib import Path

DOCS_DIR = "docs"
OUTPUT_FILE = "index.html"
BASE_URL = "https://tamkai.github.io/MetaCreativeDocs/"
IGNORE_FILE = ".docsignore"
TAGS_FILE = "tags.json"

def sanitize_filename(filename):
    """日本語や特殊文字を含むファイル名をASCII安全な名前に変換"""
    stem = Path(filename).stem
    ext = Path(filename).suffix

    # ASCII文字のみかチェック
    try:
        stem.encode('ascii')
        return None  # リネーム不要
    except UnicodeEncodeError:
        pass

    # 日本語をローマ字風のハッシュに変換
    # シンプルにタイムスタンプベースの名前を生成
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    safe_name = f"doc-{timestamp}{ext}"
    return safe_name

def rename_japanese_files(docs_path):
    """日本語ファイル名をリネーム"""
    renamed = []
    for html_file in list(docs_path.glob("*.html")):
        new_name = sanitize_filename(html_file.name)
        if new_name:
            new_path = html_file.parent / new_name
            # 重複回避
            counter = 1
            while new_path.exists():
                stem = Path(new_name).stem
                ext = Path(new_name).suffix
                new_path = html_file.parent / f"{stem}-{counter}{ext}"
                counter += 1

            html_file.rename(new_path)
            renamed.append((html_file.name, new_path.name))
            print(f"Renamed: {html_file.name} -> {new_path.name}")
    return renamed

def get_html_title(filepath):
    """HTMLファイルからtitleタグの内容を取得"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # titleタグから取得
            match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            if match:
                title = match.group(1).strip()
                if title:
                    return title
            # h1タグから取得（titleがない場合）
            match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
            if match:
                # HTMLタグを除去
                title = re.sub(r'<[^>]+>', '', match.group(1)).strip()
                if title:
                    return title
    except:
        pass
    return Path(filepath).stem

def get_file_date(filepath):
    """ファイルの更新日時を取得"""
    return datetime.fromtimestamp(os.path.getmtime(filepath))

def get_date_from_filename(filename):
    """ファイル名から日付を抽出（YYYYMMDD形式）"""
    match = re.match(r'^(\d{8})', filename)
    if match:
        try:
            return datetime.strptime(match.group(1), '%Y%m%d')
        except ValueError:
            pass
    return None

def get_sort_key_from_filename(filename):
    """ファイル名からソートキーを抽出（YYYYMMDD_NN形式）"""
    # 例: 20251128_02_xxx.html -> (20251128, 2)
    match = re.match(r'^(\d{8})(?:_(\d+))?', filename)
    if match:
        date_str = match.group(1)
        num = int(match.group(2)) if match.group(2) else 0
        return (date_str, num)
    return ('00000000', 0)

def load_ignore_list():
    """除外リストを読み込む"""
    ignore_list = set()
    if Path(IGNORE_FILE).exists():
        with open(IGNORE_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_list.add(line)
    return ignore_list

def load_tags():
    """タグ情報を読み込む"""
    if Path(TAGS_FILE).exists():
        with open(TAGS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def get_all_tags(tags_data):
    """全タグのリストを取得"""
    all_tags = set()
    for tags in tags_data.values():
        all_tags.update(tags)
    return sorted(all_tags)

def generate_index():
    """index.htmlを生成"""
    docs_path = Path(DOCS_DIR)

    # 除外リストを読み込む
    ignore_list = load_ignore_list()

    # タグ情報を読み込む
    tags_data = load_tags()
    all_tags = get_all_tags(tags_data)

    # 日本語ファイル名をリネーム
    if docs_path.exists():
        rename_japanese_files(docs_path)

    # HTMLファイルを収集
    html_files = []
    if docs_path.exists():
        for html_file in docs_path.glob("*.html"):
            # 除外リストに含まれるファイルはスキップ
            if html_file.name in ignore_list:
                print(f"Skipped (in ignore list): {html_file.name}")
                continue
            title = get_html_title(html_file)
            # ファイル名から日付を取得、なければ更新日時を使用
            filename_date = get_date_from_filename(html_file.name)
            date = filename_date if filename_date else get_file_date(html_file)
            sort_key = get_sort_key_from_filename(html_file.name)
            # タグを取得
            doc_tags = tags_data.get(html_file.name, [])
            html_files.append({
                'path': str(html_file),
                'filename': html_file.name,
                'title': title,
                'date': date,
                'sort_key': sort_key,
                'tags': doc_tags
            })

    # 日付の新しい順、同日は番号順にソート
    html_files.sort(key=lambda x: (x['sort_key'][0], x['sort_key'][1]), reverse=True)

    # ドキュメントリストのHTML生成
    if html_files:
        docs_html = ""
        for doc in html_files:
            date_str = doc['date'].strftime('%Y-%m-%d')
            full_url = BASE_URL + doc['path']
            sort_key = f"{doc['sort_key'][0]}_{doc['sort_key'][1]:02d}"
            tags_attr = ' '.join(doc['tags']) if doc['tags'] else ''
            tags_html = ''.join([f'<span class="tag">{tag}</span>' for tag in doc['tags']])
            docs_html += f'''        <li class="doc-item" data-sort-key="{sort_key}" data-tags="{tags_attr}">
            <a href="{doc['path']}" class="doc-link">
                <div class="doc-info">
                    <span class="doc-title">{doc['title']}</span>
                    <div class="doc-tags">{tags_html}</div>
                </div>
                <span class="doc-meta">
                    <span class="doc-date">{date_str}</span>
                    <button class="copy-btn" onclick="copyLink(event, '{full_url}')" title="リンクをコピー">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    </button>
                </span>
            </a>
        </li>
'''
    else:
        docs_html = '        <li class="no-docs">ドキュメントはまだありません</li>\n'

    # タグフィルターのHTML生成
    tags_filter_html = ''
    if all_tags:
        tags_filter_html = '<div class="tag-filter"><span class="filter-label">タグで絞り込み:</span><div class="tag-buttons">'
        tags_filter_html += '<button class="tag-btn active" data-tag="">すべて</button>'
        for tag in all_tags:
            tags_filter_html += f'<button class="tag-btn" data-tag="{tag}">{tag}</button>'
        tags_filter_html += '</div></div>'

    # index.html生成
    html_content = f'''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex, nofollow">
    <title>MetaCreative Docs</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>MetaCreative Docs</h1>
            <p class="subtitle">ドキュメント一覧</p>
        </header>

        <main>
            <section class="doc-list">
                <div class="list-header">
                    <h2>ドキュメント <span class="count" id="doc-count">({len(html_files)}件)</span></h2>
                    <button id="sort-toggle" class="sort-btn" onclick="toggleSort()" title="並び順を切り替え">
                        <span class="sort-label">新しい順</span>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
                    </button>
                </div>
                {tags_filter_html}
                <ul id="doc-list">
{docs_html}                </ul>
            </section>
        </main>

        <footer>
            <p>最終更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
        </footer>
    </div>

    <div id="toast" class="toast">リンクをコピーしました</div>

    <script>
    let isDescending = true;

    function copyLink(event, url) {{
        event.preventDefault();
        event.stopPropagation();

        navigator.clipboard.writeText(url).then(function() {{
            const toast = document.getElementById('toast');
            toast.classList.add('show');
            setTimeout(function() {{
                toast.classList.remove('show');
            }}, 2000);
        }}).catch(function(err) {{
            console.error('コピーに失敗しました:', err);
        }});
    }}

    function toggleSort() {{
        isDescending = !isDescending;
        const list = document.getElementById('doc-list');
        const items = Array.from(list.querySelectorAll('.doc-item'));
        const btn = document.getElementById('sort-toggle');
        const label = btn.querySelector('.sort-label');
        const svg = btn.querySelector('svg');

        items.sort((a, b) => {{
            const keyA = a.dataset.sortKey;
            const keyB = b.dataset.sortKey;
            return isDescending ? keyB.localeCompare(keyA) : keyA.localeCompare(keyB);
        }});

        items.forEach(item => list.appendChild(item));
        label.textContent = isDescending ? '新しい順' : '古い順';
        svg.style.transform = isDescending ? 'rotate(0deg)' : 'rotate(180deg)';
    }}

    // タグフィルター機能
    let currentTag = '';

    document.addEventListener('DOMContentLoaded', function() {{
        const tagButtons = document.querySelectorAll('.tag-btn');
        tagButtons.forEach(btn => {{
            btn.addEventListener('click', function() {{
                const tag = this.dataset.tag;
                filterByTag(tag);
                tagButtons.forEach(b => b.classList.remove('active'));
                this.classList.add('active');
            }});
        }});
    }});

    function filterByTag(tag) {{
        currentTag = tag;
        const items = document.querySelectorAll('.doc-item');
        let visibleCount = 0;

        items.forEach(item => {{
            const tags = item.dataset.tags || '';
            if (!tag || tags.split(' ').includes(tag)) {{
                item.style.display = '';
                visibleCount++;
            }} else {{
                item.style.display = 'none';
            }}
        }});

        document.getElementById('doc-count').textContent = `(${{visibleCount}}件)`;
    }}
    </script>
</body>
</html>
'''

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Generated {OUTPUT_FILE} with {len(html_files)} documents")

if __name__ == "__main__":
    generate_index()
