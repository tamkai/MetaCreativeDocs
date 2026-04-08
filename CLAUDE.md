# MetaCreativeDocs

メタクリドキュメントのHTML成果物を管理するリポジトリ。

## フォルダ構成
- `html-originals/standard/` — Standard HTML（メタクリドキュメントの1:1構造変換）
- `html-originals/rich/` — Rich HTML（圧縮・再構成したイマーシブ版）

## 命名規則
- Standard: `{タイプ}_{YYYYMMDD}_{スラッグ}_s.html`
- Rich: `{タイプ}_{YYYYMMDD}_{スラッグ}_r.html`
- タイプ: `R_` = ラジオ, `T_` = トランスクリプト（実対話）, `V_` = 架空対話（リサーチ）

## 変換ワークフロー
- ソースの .md は Obsidian Vault に格納されている
- Standard 変換: `/metacre-html-standard` スキルを使用
- Rich 変換: `/metacre-html-rich` スキルを使用
- CSS/JS のテンプレートは MetaCreativeToolkit 側で管理

## 関連プロジェクト
- MetaCreativeToolkit — テンプレート・デザインシステム・スキル定義
- MetaCreativeRadioWeb — ラジオWebサイト（HTMLの公開先）
