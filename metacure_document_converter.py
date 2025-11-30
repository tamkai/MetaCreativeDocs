import re
from typing import List, Tuple
from html import escape
import os
import argparse
from weasyprint import HTML

# --- 設定とデザイン定義 ---

# 話者名と対応するCSSクラスのマッピング (随時追加/修正可能)
SPEAKER_MAP = {
    "タムラカイ": "tamkai",
    "タムカイ": "tamkai",
    "小林": "tamkai", # ファシリテーターは一旦タムカイさんと同じブルー系に分類
    "黒田": "tamkai", # その他の話者も一旦ブルー系に分類
    "大里": "osato",
    "大里P": "osato",
    "Opi": "opi",
    # 今後のドキュメントで話者が増えた場合はここに追加
}

# 章の絵文字マッピング (ドキュメントの内容に合わせて変更)
# キーは章のタイトルを簡易的に識別するための文字列
CHAPTER_EMOJIS_MAP = {
    "現場からの変革": "💥",
    "パーパスカービング": "👩‍🌾",
    "トップを動かす": "🪜",
    "失敗と覚悟": "🛡️",
    "組織を超えたつながり": "🤝",
    "パーパス浸透ではなく": "💡",
}

CSS_STYLE = """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        @page {
            margin: 15mm;
        }

        body {
            font-family: "Noto Sans CJK JP", "Hiragino Sans", "Hiragino Kaku Gothic ProN", "Yu Gothic", "Meiryo", sans-serif;
            line-height: 1.8;
            color: #2d2d2d;
            background-color: #f5f3f0; /* ベース背景色: ウォームグレー */
            padding: 0;
            font-size: 15px;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #ffffff; /* コンテンツ背景: 白 */
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
        }

        /* --- 見出しのスタイル --- */
        h1 { font-size: 2.2em; font-weight: 700; color: #1a1a1a; margin-bottom: 0.5em; line-height: 1.3; text-align: center; }

        h2 {
            font-size: 1.6em; font-weight: 600; color: #2d2d2d; margin-top: 2.5em; margin-bottom: 1em;
            padding-bottom: 0.3em; border-bottom: 2px solid #d4cfc7;
        }

        h3 {
            font-size: 1.3em; font-weight: 600; color: #3a3a3a; margin-top: 2em; margin-bottom: 0.8em;
            display: inline-block; background: linear-gradient(transparent 60%, #ffd97d 60%);
            padding: 0 0.3em; line-height: 1.5; box-decoration-break: clone; -webkit-box-decoration-break: clone;
        }
        
        /* --- 地の文/段落 --- */
        p { margin-bottom: 1.2em; color: #3a3a3a; }
        hr { border: none; border-top: 1px solid #e0dbd3; margin: 2em 0; }
        strong { font-weight: 600; color: #2d2d2d; }

        /* --- 会話引用文のスタイル --- */
        .dialogue { border-left: 4px solid; padding: 1.2em 1.5em; margin: 1.5em 0; border-radius: 6px; font-size: 0.98em; }

        .dialogue.osato { background: linear-gradient(135deg, #fdf6e9 0%, #f7ebd4 100%); border-left-color: #d4a574; }
        .dialogue.osato .dialogue-speaker { color: #a87c3f; }

        .dialogue.tamkai { background: linear-gradient(135deg, #f0f4f7 0%, #e3ebf0 100%); border-left-color: #7b9aad; }
        .dialogue.tamkai .dialogue-speaker { color: #5a7485; }

        .dialogue.opi { background: linear-gradient(135deg, #f2f7f0 0%, #e5f0e3 100%); border-left-color: #8ba882; }
        .dialogue.opi .dialogue-speaker { color: #5d7a57; }

        .dialogue-speaker { font-weight: 600; margin-bottom: 0.3em; line-height: 1.2; }
        .dialogue-text { color: #3a3a3a; line-height: 1.7; margin-bottom: 0; }

        /* --- 注釈のスタイル --- */
        .annotation { background-color: #faf9f7; border: 1px solid #e5e1db; border-radius: 8px; padding: 1.5em; margin: 2em 0; font-size: 0.92em; }
        .annotation-title { font-weight: 700; color: #5a5a5a; margin-bottom: 0.8em; font-size: 1.05em; display: flex; align-items: center; }
        .annotation-title::before { content: "📚"; margin-right: 0.5em; font-size: 1.1em; }
        .annotation-content { color: #4a4a4a; line-height: 1.7; }
        .annotation-content p { margin-bottom: 0.8em; }
        .annotation-content p:last-child { margin-bottom: 0; }
        
        /* --- 目次のスタイル --- */
        .table-of-contents { background-color: #faf9f7; border: 1px solid #e5e1db; border-radius: 8px; padding: 2em; margin: 2.5em 0; }
        .table-of-contents h2 { font-size: 1.4em; margin-top: 0; margin-bottom: 1em; border-bottom: none; }
        .table-of-contents ol { list-style: none; margin-left: 0; counter-reset: chapter; }
        .table-of-contents li { counter-increment: chapter; margin-bottom: 0.8em; font-size: 1.05em; }
        .table-of-contents li::before { content: "第" counter(chapter) "章"; font-weight: 600; color: #8b6f47; margin-right: 1em; }
        .table-of-contents a { color: #3a3a3a; text-decoration: none; transition: color 0.2s; }
        .table-of-contents a:hover { color: #8b6f47; }

        /* --- 章の画像 (絵文字) --- */
        .chapter-image {
            width: 150px; height: 150px; margin: 1.5em auto; display: block; border-radius: 8px;
            background: linear-gradient(135deg, #d4cfc7 0%, #e8e3db 100%); 
            display: flex; align-items: center; justify-content: center; font-size: 3em; color: #2d2d2d;
        }

        /* --- タイトルページ装飾 --- */
        .title-page { padding: 8em 2em 6em 2em; text-align: center; }
        .title-ornament { font-size: 3em; margin: 0.5em 0; color: #d4a574; }
        .title-page h1 { border-bottom: 3px solid #d4cfc7; padding-bottom: 0.5em; display: inline-block; }
        .subtitle { font-size: 1.1em; color: #6b6b6b; margin-top: 1em; font-weight: 500; }
        
        /* --- PDF専用スタイル (@media print) --- */
        @media print {
            body, .container { background-color: white; box-shadow: none; }
            .title-page { page-break-after: always; }
            .table-of-contents { page-break-before: always; }
            h2 { page-break-before: always; }
            #introduction { page-break-before: auto; }
            .annotation, .dialogue { page-break-inside: avoid; }
        }
"""

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        {css_style}
    </style>
</head>
<body>
    <div class="container">
        <div class="title-page">
            <div class="title-ornament">✦</div>
            <h1>{main_title}</h1>
            <p class="subtitle"><strong>{sub_title}</strong></p>
            <p class="subtitle" style="margin-top: 2em; font-size: 0.9em; color: #8b8b8b;">{metadata}</p>
            <div class="title-ornament">✦</div>
        </div>

        {content_html}
        
        <div class="final-message">
            <p><strong>編集：哲学的編集者（Claude）</strong></p>
            <p style="margin: 0.5em 0;">このドキュメントは自動生成されたものです。</p>
        </div>
    </div>
</body>
</html>
"""

# --- マークダウンパースロジック ---

def get_speaker_class(speaker: str) -> str:
    """話者名から対応するCSSクラスを取得する"""
    for key, class_name in SPEAKER_MAP.items():
        if key in speaker:
            return class_name
    return "tamkai" # デフォルト

def get_chapter_emoji(title: str) -> str:
    """章のタイトルから対応する絵文字を取得する"""
    for key, emoji in CHAPTER_EMOJIS_MAP.items():
        if key in title:
            return emoji
    return ""

def markdown_to_html_custom(md_content: str, metadata: dict) -> str:
    """カスタムマークダウンをHTMLに変換し、目次を生成する"""
    
    # メタデータ抽出 (最初の # から --- の間)
    
    # 連続する複数の空白行を単一の空白行に置換
    md_content = re.sub(r'\n\s*\n', '\n\n', md_content)
    
    lines = md_content.split('\n')
    
    html_lines = []
    toc_entries = []
    
    chapter_count = 0
    in_annotation = False
    annotation_content = []

    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # 1. 注釈ブロックの処理
        if stripped_line == "---":
            # 注釈終了
            if in_annotation:
                content_text = "\n".join(annotation_content)
                
                # 注釈タイトルを抽出
                title_match = re.search(r'\*\*【(.+?)】\*\*', content_text, re.DOTALL)
                title = title_match.group(1).strip() if title_match else "注釈"
                
                # 注釈内容を抽出 (タイトル行以降)
                content_body = re.sub(r'\*\*【.+?】\*\*\n*', '', content_text, 1).strip()
                content_paragraphs = "".join([f"<p>{escape(p.strip())}</p>" for p in content_body.split('\n\n') if p.strip()])
                
                html_lines.append(f"""
<div class="annotation">
    <div class="annotation-title">{escape(title)}</div>
    <div class="annotation-content">
        {content_paragraphs}
    </div>
</div>
                """.strip())
                in_annotation = False
                annotation_content = []
                continue
            
            # 注釈開始 (次の行が **【タイトル】** の場合)
            if i + 1 < len(lines) and re.match(r'^\*\*【.+?】\*\*', lines[i+1].strip()):
                in_annotation = True
                continue
            
            # 通常の水平線
            if not in_annotation:
                html_lines.append("<hr>")
                continue
        
        if in_annotation:
            annotation_content.append(line)
            continue
            
        # 2. 見出しの処理
        if stripped_line.startswith('## '):
            title = stripped_line[3:].strip()
            anchor = title.replace(' ', '-').replace('：', '').replace('—', '').replace('——', '') # 簡易アンカー
            
            if 'はじめに' in title and chapter_count == 0:
                anchor = "introduction"
                html_lines.append(f'<h2 id="{anchor}">{escape(title)}</h2>')
            else:
                chapter_count += 1
                toc_entries.append((chapter_count, title, anchor))
                
                # HTML出力
                html_lines.append(f'<h2 id="chapter{chapter_count}">第{chapter_count}章:{escape(title)}</h2>')
                emoji = get_chapter_emoji(title)
                if emoji:
                    html_lines.append(f'<div class="chapter-image">{emoji}</div>')

        elif stripped_line.startswith('### '):
            title = stripped_line[4:].strip()
            html_lines.append(f'<h3>{escape(title)}</h3>')

        # 3. 会話引用文の処理
        elif re.match(r'^>\s\*\*(.+?)\*\*：「(.+?)」', stripped_line):
            dialogue_match = re.match(r'^>\s\*\*(.+?)\*\*：「(.+?)」', stripped_line)
            speaker = dialogue_match.group(1).strip()
            text = dialogue_match.group(2).strip()
            speaker_class = get_speaker_class(speaker)
            
            html_lines.append(f"""
<div class="dialogue {speaker_class}">
    <div class="dialogue-speaker">{escape(speaker)}</div>
    <p class="dialogue-text">「{escape(text)}」</p>
</div>
            """.strip())

        # 4. 通常の段落・リストの処理
        elif stripped_line and not stripped_line.startswith('#') and not stripped_line.startswith('>'):
            # 強調 (*や**で囲まれた部分) を<strong>タグに変換 (簡易)
            text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', stripped_line)
            text = re.sub(r'\*(.+?)\*', r'<strong>\1</strong>', text)
            
            if re.match(r'^[*-]\s', text): # リストアイテム
                html_lines.append(f"<ul><li>{text[2:].strip()}</li></ul>")
            elif re.match(r'^\d+\.\s', text): # 番号付きリストアイテム
                # ここではリストの開始/終了タグの制御が困難なため、簡易的な <p> として処理
                 html_lines.append(f"<p>{text}</p>")
            else:
                 html_lines.append(f"<p>{text}</p>")
    
    # 5. リストの修正 (簡易: 連続する <ul>/</ul> を削除)
    content_html = "\n".join(html_lines)
    content_html = re.sub(r'</ul>\s*<ul>', '', content_html)


    # 6. 目次HTMLの生成と挿入
    toc_html = """
        <div class="table-of-contents">
            <h2>目次</h2>
            <ol>
    """
    for count, title, anchor in toc_entries:
        display_title = re.sub(r'第\d+章:\s*', '', title)
        toc_html += f'<li><a href="#chapter{count}">{escape(display_title)}</a></li>\n'
    toc_html += """
            </ol>
        </div>
    """
    
    # 「はじめに」セクションの後に目次を挿入
    intro_end_index = content_html.find('</p>', content_html.find('id="introduction"'))
    if intro_end_index != -1:
        # 最初の hr の位置を探す (導入と目次の区切りとして)
        hr_index = content_html.find('<hr>', intro_end_index)
        
        if hr_index != -1:
             final_content_html = content_html[:hr_index] + "<hr>\n" + toc_html + content_html[hr_index:]
        else:
             final_content_html = content_html[:intro_end_index + 4] + "\n\n<hr>\n" + toc_html + content_html[intro_end_index + 4:]
    else:
        final_content_html = content_html


    return HTML_TEMPLATE.format(
        title=metadata['title'],
        css_style=CSS_STYLE,
        main_title=metadata['main_title'],
        sub_title=metadata['sub_title'],
        metadata=metadata['metadata'],
        content_html=final_content_html
    )

# --- メイン実行関数 ---

def main():
    parser = argparse.ArgumentParser(description="メタクリドキュメントをHTML/PDFに変換します。")
    parser.add_argument("input_file", help="入力マークダウンファイル (.md)")
    parser.add_argument("--output_html", default="output.html", help="出力HTMLファイル名")
    parser.add_argument("--output_pdf", default="output.pdf", help="出力PDFファイル名 (weasyprintが必要)")
    args = parser.parse_args()

    # メタデータ (必要に応じて外部から取得するか、MDファイルからパース)
    # ここでは、フジトラレポートのメタデータをハードコード (実際の利用時はMDからパース推奨)
    metadata = {
        'title': '現場からカルチャー変革は起こせるのか - フジトラの実践者が語る',
        'main_title': '現場からカルチャー変革は起こせるのか',
        'sub_title': '富士通「フジトラ」の実践者が語る、自分ごと化の本質',
        'metadata': '日付：2025年11月26日<br>登壇者：タムラカイ（株式会社AFFLATUS代表取締役）<br>主催：株式会社セルム パーパス経営・理念経営勉強会'
    }

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()

        full_html = markdown_to_html_custom(md_content, metadata)

        # 1. HTMLファイルを保存
        with open(args.output_html, 'w', encoding='utf-8') as f:
            f.write(full_html)
        print(f"✅ HTMLファイルが {args.output_html} に保存されました。")

        # 2. PDFファイルを生成
        try:
            # WeasyPrint を使用
            HTML(string=full_html).write_pdf(args.output_pdf)
            print(f"✅ PDFファイルが {args.output_pdf} に保存されました。")
        except Exception as e:
            print(f"⚠️ WeasyPrintでのPDF生成に失敗しました (WeasyPrintがインストールされていないか、他のエラー): {e}")
            print("HTMLファイルのみが生成されています。")

    except FileNotFoundError:
        print(f"❌ エラー: 入力ファイル {args.input_file} が見つかりません。")
    except Exception as e:
        print(f"❌ 予期せぬエラーが発生しました: {e}")

if __name__ == '__main__':
    # 実行例: python metacure_document_converter.py 20251126_report.md
    # main() # 知識登録時はコメントアウト