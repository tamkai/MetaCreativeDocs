# Session Handover - 2026-03-30 09:00

## Summary
`metacre-chapter-infographic` スキルの完成と実運用。3つのスタイルで実験した結果「アイソメ＋日本語キーワードラベル」をデフォルトに決定。`--hero` オプション追加、モバイル対応CSS修正、Ep18での実運用テストまで完了。

## What We Accomplished

### スキル完成
- `metacre-chapter-infographic` スキルを設計・実装・反復改善
- 3スタイル実験: アイソメ(1:1) → グラレコ(4:3) → **アイソメ＋ラベル(4:3)** をデフォルトに決定
- `--hero` オプション追加: タイトル下16:9ヒーロー画像も自動生成・挿入
- デフォルトアスペクト比を4:3に、画像サイズを1536px（実際は約1200px）に設定
- CSSの80px/64px上書き問題を正規表現で自動修正するよう対応
- モバイルでの画像はみ出し問題を `max-width: min(560px, 100%)` で修正

### 実運用テスト
- 「書籍が組織に根を下ろすとき」で3スタイル比較版を生成・デプロイ
- 「Ep18 ノイズ」でスキルの汎用性を確認（ヒーロー1枚＋チャプター6枚、1コマンドで完了）

### ショーケース管理
- 新規HTML多数追加（podcast, 育成feedback/kansei, 書籍）
- テキスト修正（エアカバー、ディベロップメント）
- admin.htmlにインフォグラフィック版のリンクも追加済み

### メモリ記録
- `feedback_infographic_style.md` — インフォグラフィックは「アイソメイラスト＋キーワード」、説明文不要

## Key Decisions
| Decision | Rationale |
|----------|-----------|
| アイソメ＋ラベルをデフォルトスタイルに | グラレコはチャプター間でスタイルがずれやすい。アイソメは統一感があり、キーワードラベルで内容もアンカーできる |
| 説明文ではなくキーワードのみ | 詳細テキストが後に続くドキュメント構造なので、画像は視覚的な地図・要約に徹すべき |
| 4:3をデフォルトに | 1:1は縦に長すぎ、4:3が横長で読みやすくコンテンツ幅に収まる |
| 画像1536px | 再利用（印刷・SNS等）を考慮。Gemini出力は実際1200px程度 |
| 元HTMLを変更せず別ファイル出力 | インフォグラフィック版はオプションの二段階変換 |
| Gemini 3.1 Flash API | 1K画像で$0.067/枚。1ドキュメント変換あたり約$0.47（約70円） |

## Current State
- mainブランチに全てコミット・プッシュ済み、未コミットの変更なし
- スキルは完成・実用可能な状態
- 実験用の3バリエーション（infographic, graphrec, isolabel）がshowcaseに残っている

## Key Files Modified

### スキル（~/.claude/skills/metacre-chapter-infographic/）
- `skill.md` — スキル定義（`--hero` オプション記載）
- `scripts/generate_chapter_infographics.py` — メインスクリプト（hero生成、CSS自動修正、min()対応）
- `styles/metacre-isometric-labeled.txt` — デフォルトスタイル（**これが正解**）
- `styles/metacre-isometric.txt` — アイソメのみ（テキストなし）
- `styles/metacre-graphicrecording.txt` — グラレコ風

### ショーケース（docs/d/showcase/）
- `T_20260326_shoseki-soshiki-ni-ne_isolabel_s.html` — 書籍アイソメ＋ラベル版（推奨）
- `R_20260126_ep18-noise_infographic_s.html` — Ep18インフォグラフィック版
- `img/isolabel/` — 書籍の画像（hero + ch1-5）
- `img/ep18/` — Ep18の画像（hero + ch1-6）
- `admin.html` — 全記事リスト更新済み

## Lessons Learned
- `.chapter-image` の元CSS（80px）とモバイル用CSS（64px）が後から追加したinfographic CSSを上書きする → スクリプト内で正規表現で元CSSを書き換える方式で根本解決
- `max-width: 560px` だけではモバイルではみ出す → `min(560px, 100%)` が正解
- GitHub Pagesのキャッシュ → `?v=N` パラメータで回避
- Gemini Flashは「テキストなし」指示を守らないことがある → ユーザーはむしろキーワードラベル入りを歓迎
- グラレコスタイルはチャプター間の視覚的統一感が弱い → アイソメの方が安定
- Gemini 3.1 Flash画像生成は無料ではない: 1K画像$0.067/枚

## Next Steps
- [ ] 他のStandard版HTMLにインフォグラフィック版を適用（ユーザーの指示に応じて）
- [ ] 実験用3バリエーション（infographic, graphrec）をshowcaseから整理するか検討
- [ ] スタイルプロンプトの微調整（チャプター間の一貫性をさらに向上させたい場合）

## Blockers / Open Questions
- Gemini Flash生成解像度が1200px程度で1536pxに届かないケースがある
- プレビュー期間終了後の料金変動の可能性

## User Preferences Noted
- インフォグラフィックは「情報量の多いアイソメイラスト＋キーワード」。説明文は不要（詳細テキストが後に続くから）
- ショーケースHTML追加時はadmin.htmlも必ず更新する
- インフォグラフィック版は二段階変換の位置づけ（全ドキュメントに適用するわけではない、ここぞという時に使う）
- テキストラベルは許容・歓迎（むしろキーワードがあった方がいい）
- スタイル未指定時はアイソメ＋ラベルをデフォルト使用でOK
