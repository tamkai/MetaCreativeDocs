# Session Handover - 2026-02-24 22:00

## Summary
MetaCreativeDocs GitHub Pagesサイトをゼロから再構築した。旧HTML 40個をアーカイブし、「アトリエの朝」デザインシステムで新しいサイト骨格（ランディング・About・管理画面）+ HTML原本管理体制 + catalog.jsonメタデータ管理を構築。

## What We Accomplished
- **RadioWebからhtml-samples/を移管**: 全HTMLファイルをMetaCreativeDocs/html-originals/に移動し、新命名規則（`{R|T|V}_{YYYYMMDD}_{slug}_{s|r}.html`）でリネーム。RadioWeb側のhtml-samples/は削除済み
- **スキル出力先を変更**: `metacre-html-standard.md` と `metacre-html-rich.md` の出力先を `~/product/MetaCreativeDocs/html-originals/{standard|rich}/` に変更（場所: `/Users/tamkai/product/MetaCreativeToolkit/skills/`）
- **旧サイトをアーカイブ**: docs/内の40 HTML + 旧ツール類を `_archive/` に退避（.gitignoreに追加済み）
- **新サイト骨格を構築**:
  - `docs/index.html` — ブランドランディングページ（コピー改善が次の課題）
  - `docs/about.html` — RadioWebのabout_MetacreDocs.htmlを移植（3 View切替あり）
  - `docs/admin.html` — PW保護の管理画面（catalog.jsonから一覧表示、フィルタ・URLコピー機能）
  - `docs/assets/css/tokens.css` — アトリエの朝デザイントークン
  - `docs/assets/css/site.css` — サイト共通CSS
- **catalog.json作成**: 6件のサンプルドキュメントでメタデータ管理（type, tags, formats, protected）
- **deploy.yml作成**: docs/とcatalog.json変更時にGitHub Pagesへ自動デプロイ
- **コミット完了**: `c8cd62c` — まだpushしていない

## Key Decisions
| Decision | Rationale |
|----------|-----------|
| まっさらスタート（旧URL互換不要） | 旧サイトは運用停止済み、URLの互換性を気にする必要なし |
| フラット配置 + catalog.jsonでメタデータ管理 | フォルダ分けよりメンテナンスしやすく、管理画面でフィルタ可能 |
| 2段階パイプライン（原本→サイト版） | スキル出力はスタンドアロン（人に渡せる）、サイト版は共通CSS参照（一括更新可能） |
| docs/d/ にStandard、docs/showcase/ にRich | Richは自己完結型HTMLをそのまま配置、Standardはサイト統合版 |
| GitHub Pages維持（Vercel不要） | 現時点では静的配信で十分、将来的にサービス化するタイミングで検討 |
| ファイル命名: `{R\|T\|V}_{YYYYMMDD}_{slug}_{s\|r}.html` | タイプ・日付・内容が一目でわかり、ソート可能 |
| admin.htmlのPW保護はJSベースの仮実装 | 本格運用時はStatiCryptに移行予定 |
| アトリエの朝デザインシステムに統一 | RadioWebと同じデザイン言語でブランド統一 |

## Current State
- ブランチ: `main`、リモートより1コミット先行（未push）
- サイト骨格は完成、ローカルで動作確認済み（`python3 -m http.server --directory docs`）
- admin.htmlのPWは `password`（SHA-256ハッシュ、仮）
- `docs/d/` と `docs/showcase/` は空（実コンテンツ未配置）
- ランディングページのコピーは機能説明型 → ユーザーが「痛みから入るべき」とフィードバック済み

## Key Files Modified
- `docs/index.html` — ブランドランディング（コピー要改善）
- `docs/about.html` — メタクリドキュメント説明ページ（3 View切替、RadioWebから移植）
- `docs/admin.html` — PW保護の管理画面（catalog.json連携）
- `docs/assets/css/tokens.css` — アトリエの朝デザイントークン（rich-boilerplate.htmlから抽出）
- `docs/assets/css/site.css` — サイト共通スタイル（ヘッダー、カード、タグ等）
- `catalog.json` — ドキュメントメタデータ（6件登録済み、docs/にもコピーあり）
- `DESIGN_LANGUAGE.md` — RadioWebからコピーしたデザインシステム仕様
- `.github/workflows/deploy.yml` — GitHub Pages自動デプロイ
- `.gitignore` — `_archive/` 追加
- `html-originals/standard/` — Standard版原本4件
- `html-originals/rich/` — Rich版原本7件
- `/Users/tamkai/product/MetaCreativeToolkit/skills/metacre-html-standard.md` — 出力先パス変更
- `/Users/tamkai/product/MetaCreativeToolkit/skills/metacre-html-rich.md` — 出力先パス変更

## Lessons Learned
- **ローカルサーバーのディレクトリ指定が重要**: `python3 -m http.server --directory docs` としないとパスが合わない
- **catalog.jsonのパス**: admin.htmlからは `catalog.json` で参照（deploy.ymlでdocs/にコピーされる）。最初 `../catalog.json` で404になった
- **nohupでサーバー維持**: `nohup python3 -m http.server 8080 --directory docs > /dev/null 2>&1 &` で安定
- **スキルファイルの場所**: `~/.claude/commands/` ではなく `/Users/tamkai/product/MetaCreativeToolkit/skills/` にある

## Next Steps
- [ ] **ランディングページのコピー改善**（最優先）: `/research` で調査してから、痛みから入るアプローチに書き直し。「こういうことはありませんか？」→ 議事録が眠ってる、AI要約は二度と読まれない、対話のニュアンスが消える → メタクリドキュメントが解決する、の流れ
- [ ] `integrate-html.py` 作成: html-originals/の自己完結型HTML → docs/d/のサイト統合版に変換するツール
- [ ] `standard.css` 作成: Standard版ドキュメントの共通CSS
- [ ] `docs/d/` にStandard版コンテンツを配置
- [ ] `docs/showcase/` にRich版コンテンツを配置
- [ ] admin.htmlのパスワードを本番用に変更
- [ ] git push してGitHub Pagesデプロイを確認
- [ ] 将来: StatiCryptによる本格PW保護

## Blockers / Open Questions
- ランディングページのコピーは「マーケティングプロに相談したい」とユーザーが言及。`/research` でリサーチしてからコピーを書くアプローチを提案済み
- `integrate-html.py` の具体的な変換ロジック（何をどう置き換えるか）は未定義。原本のスタンドアロンCSSを共通CSS参照に置き換える処理が必要

## User Preferences Noted
- **日本語で会話**する
- ランディングは**機能説明からではなく、痛みから入る**（「こういうことはありませんか？」アプローチ）
- 具体的な痛みの例: 「2時間の議論のあと、議事録が箇条書き3行」「AI要約はきれいだけど二度と開かない」「あの時の熱量はどこに行った？」
- ユーザーは「コミュニケーションの記録をもったいない使い方している」と感じてもらうのが目標
- **過剰な提案は不要** — 聞かれたことをやる、シンプルに
- プランファイルは `.claude/plans/serialized-orbiting-quill.md` にある（全体設計の参照用）
