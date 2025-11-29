#!/usr/bin/env python3
"""
HTMLドキュメントのindexページを自動生成するスクリプト
docs/フォルダ内のHTMLファイルを検索し、index.htmlを生成します
日本語ファイル名は自動的にリネームします
"""

import os
import re
import unicodedata
from datetime import datetime
from pathlib import Path

DOCS_DIR = "docs"
OUTPUT_FILE = "index.html"
BASE_URL = "https://tamkai.github.io/MetaCreativeDocs/"

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

def generate_index():
    """index.htmlを生成"""
    docs_path = Path(DOCS_DIR)

    # 日本語ファイル名をリネーム
    if docs_path.exists():
        rename_japanese_files(docs_path)

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
            full_url = BASE_URL + doc['path']
            docs_html += f'''        <li class="doc-item">
            <a href="{doc['path']}" class="doc-link">
                <span class="doc-title">{doc['title']}</span>
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

    <div id="toast" class="toast">リンクをコピーしました</div>

    <script>
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
    </script>
</body>
</html>
'''

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Generated {OUTPUT_FILE} with {len(html_files)} documents")

if __name__ == "__main__":
    generate_index()
