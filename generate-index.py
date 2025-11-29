#!/usr/bin/env python3
"""
HTMLドキュメントのindexページを自動生成するスクリプト
docs/フォルダ内のHTMLファイルを検索し、index.htmlを生成します
"""

import os
import re
from datetime import datetime
from pathlib import Path

DOCS_DIR = "docs"
OUTPUT_FILE = "index.html"

def get_html_title(filepath):
    """HTMLファイルからtitleタグの内容を取得"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
    except:
        pass
    return Path(filepath).stem

def get_file_date(filepath):
    """ファイルの更新日時を取得"""
    return datetime.fromtimestamp(os.path.getmtime(filepath))

def generate_index():
    """index.htmlを生成"""
    docs_path = Path(DOCS_DIR)

    # HTMLファイルを収集
    html_files = []
    if docs_path.exists():
        for html_file in docs_path.glob("*.html"):
            title = get_html_title(html_file)
            date = get_file_date(html_file)
            html_files.append({
                'path': str(html_file),
                'filename': html_file.name,
                'title': title,
                'date': date
            })

    # 日付の新しい順にソート
    html_files.sort(key=lambda x: x['date'], reverse=True)

    # ドキュメントリストのHTML生成
    if html_files:
        docs_html = ""
        for doc in html_files:
            date_str = doc['date'].strftime('%Y-%m-%d')
            docs_html += f'''        <li class="doc-item">
            <a href="{doc['path']}" class="doc-link">
                <span class="doc-title">{doc['title']}</span>
                <span class="doc-date">{date_str}</span>
            </a>
        </li>
'''
    else:
        docs_html = '        <li class="no-docs">ドキュメントはまだありません</li>\n'

    # index.html生成
    html_content = f'''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
                <h2>ドキュメント <span class="count">({len(html_files)}件)</span></h2>
                <ul>
{docs_html}                </ul>
            </section>
        </main>

        <footer>
            <p>最終更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
        </footer>
    </div>
</body>
</html>
'''

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Generated {OUTPUT_FILE} with {len(html_files)} documents")

if __name__ == "__main__":
    generate_index()
