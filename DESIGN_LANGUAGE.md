# MetaCreative Design Language

## North Star: 「アトリエの朝」

朝の光が差し込むアトリエ。清潔で集中できる空間。道具は整頓されているが、使い込まれた温かみがある。キャンバスに向かおうとする静かな高揚感。

- **光が支配する**: ベージュ/ホワイトの背景が全体の80%以上を占める
- **色は道具のように点在する**: セージ、サーモン、ゴールドは小さな面積で効果的に使う
- **やさしいが甘くない**: 有機的・人間的だが、知的な緊張感がある
- **サイバー/ネオン/モノトーンは使わない**: AI時代だからこそ人間の手触り

---

## Color System

### Core Colors

#### Sage（セージ）— Primary「アトリエの植物」

| Token | Hex | RGB | 用途 |
|-------|-----|-----|------|
| `sage-50` | `#F4F6F2` | 244, 246, 242 | 大面積の背景、カード背景 |
| `sage-100` | `#E2E8DD` | 226, 232, 221 | セカンダリ背景、ホバー |
| `sage-200` | `#C5D1BC` | 197, 209, 188 | ボーダー、ディバイダー |
| `sage-400` | `#8B9A7D` | 139, 154, 125 | アイコン、バッジ、小面積のアクセント |
| `sage-600` | `#5E6E52` | 94, 110, 82 | テキスト強調、アクティブ状態 |

#### Rose（サーモン/ローズ）— Secondary「朝焼けの差し色」

| Token | Hex | RGB | 用途 |
|-------|-----|-----|------|
| `rose-50` | `#FDF5F3` | 253, 245, 243 | 背景アクセント、ハイライト |
| `rose-100` | `#F8E4DF` | 248, 228, 223 | カード背景、ホバー |
| `rose-200` | `#F0C4BB` | 240, 196, 187 | ボーダー |
| `rose-400` | `#E8A598` | 232, 165, 152 | アイコン、バッジ |
| `rose-600` | `#D88B7A` | 216, 139, 122 | テキスト強調 |

#### Gold（ゴールド）— Tertiary「道具の真鍮」

| Token | Hex | RGB | 用途 |
|-------|-----|-----|------|
| `gold-50` | `#FDF9EE` | 253, 249, 238 | 背景 |
| `gold-100` | `#F7EDCC` | 247, 237, 204 | ハイライト、マーカー |
| `gold-200` | `#EEDEA5` | 238, 222, 165 | ボーダー |
| `gold-400` | `#C4A057` | 196, 160, 87 | ボタン、CTA |
| `gold-600` | `#9A7B3A` | 154, 123, 58 | テキスト強調 |

#### Red（レッド）— Accent「絵の具の赤」

| Token | Hex | RGB | 用途 |
|-------|-----|-----|------|
| `red-50` | `#FEF2F1` | 254, 242, 241 | エラー背景 |
| `red-100` | `#FDDBD8` | 253, 219, 216 | 通知背景 |
| `red-200` | `#F5AFA7` | 245, 175, 167 | ボーダー |
| `red-400` | `#E74C3C` | 231, 76, 60 | CTA、重要マーク |
| `red-600` | `#C0392B` | 192, 57, 43 | エラーテキスト |

### Extended Colors（UIバリエーション用）

#### Blue（ブルー）— 「窓からの空」

| Token | Hex | RGB |
|-------|-----|-----|
| `blue-50` | `#F0F5FA` | 240, 245, 250 |
| `blue-100` | `#D6E4F0` | 214, 228, 240 |
| `blue-400` | `#5B8DB8` | 91, 141, 184 |
| `blue-600` | `#3A6B91` | 58, 107, 145 |

#### Purple（パープル）— 「朝のラベンダー」

| Token | Hex | RGB |
|-------|-----|-----|
| `purple-50` | `#F5F2F8` | 245, 242, 248 |
| `purple-100` | `#E4DCF0` | 228, 220, 240 |
| `purple-400` | `#8B7AAD` | 139, 122, 173 |
| `purple-600` | `#6B5A8E` | 107, 90, 142 |

### Neutrals

| Token | Hex | RGB | 用途 |
|-------|-----|-----|------|
| `base` | `#F5F0E8` | 245, 240, 232 | ページ背景（ベージュ） |
| `surface` | `#FAF8F5` | 250, 248, 245 | カード、パネル |
| `white` | `#FDFCFA` | 253, 252, 250 | テキストオンダーク |
| `text-primary` | `#2C3330` | 44, 51, 48 | 本文テキスト |
| `text-secondary` | `#6B6560` | 107, 101, 96 | 補助テキスト |
| `text-muted` | `#9E9690` | 158, 150, 144 | プレースホルダー |
| `border` | `#E5DFD6` | 229, 223, 214 | 標準ボーダー |

### カラー運用ルール

1. **面積と明度の原則**: 面積が大きいほど明るいトーン（50-100）を使う。濃いトーン（400-600）は点のように使う
2. **背景の階層**: `base` → `surface` → `[color]-50` の3段階で奥行きを作る
3. **テキストカラー**: 本文は必ず `text-primary`。色テキストは `[color]-600` のみ（400は面積が小さい要素専用）
4. **セージの重さ問題の回避**: `sage-400` 以上を背景に使わない。背景には `sage-50` or `sage-100` まで

---

## Typography

### フォントスタック

| Role | Font | Weights | 用途 |
|------|------|---------|------|
| **本文** | Noto Sans JP | 400, 500, 700 | 記事本文、UI、説明テキスト |
| **見出し・引用** | Noto Serif JP | 400, 500, 700 | 章タイトル、引用、導の文 |
| **英文** | Inter | 400, 500, 600, 700 | 英文コピー、ラベル、ナビ |
| **サイト（既存）** | M PLUS Rounded 1c | 400, 500, 700, 800 | サイトUI（既存を維持） |

### タイプスケール

| Token | Size | Line Height | Weight | 用途 |
|-------|------|-------------|--------|------|
| `display` | 2.5rem (40px) | 1.3 | Serif 700 | ページタイトル |
| `h1` | 2rem (32px) | 1.4 | Serif 700 | 章タイトル |
| `h2` | 1.5rem (24px) | 1.4 | Serif 500 | セクション見出し |
| `h3` | 1.25rem (20px) | 1.5 | Sans 700 | サブセクション |
| `body` | 1rem (16px) | 1.9 | Sans 400 | 本文 |
| `body-sm` | 0.875rem (14px) | 1.7 | Sans 400 | 補助テキスト |
| `caption` | 0.75rem (12px) | 1.5 | Sans 500 | ラベル、注釈 |
| `label` | 0.8125rem (13px) | 1.4 | Inter 600 | UIラベル、バッジ |

### タイポグラフィ運用ルール

1. **見出しはセリフ、本文はサンセリフ**: 知的な緊張感と読みやすさの両立
2. **行間は広め**: 本文 `line-height: 1.9` で呼吸できる余白を確保
3. **ウェイトは3段階まで**: Regular(400), Medium(500), Bold(700)。900は使わない
4. **文字サイズの最小は12px**: 可読性を保証

---

## Spacing

### 基本グリッド: 4px

| Token | Value | 用途 |
|-------|-------|------|
| `space-1` | 4px | 最小間隔 |
| `space-2` | 8px | アイコンとテキスト間 |
| `space-3` | 12px | フォーム要素内パディング |
| `space-4` | 16px | コンポーネント内パディング |
| `space-6` | 24px | セクション内マージン |
| `space-8` | 32px | カード間マージン |
| `space-12` | 48px | セクション間マージン |
| `space-16` | 64px | 大セクション間 |
| `space-24` | 96px | ページ内の大きな区切り |

### コンテンツ幅

| Token | Value | 用途 |
|-------|-------|------|
| `content-narrow` | 640px | 読み物コンテンツ（メタクリドキュメント） |
| `content-standard` | 800px | 標準コンテンツ |
| `content-wide` | 1080px | サイトレイアウト |

---

## Border Radius

| Token | Value | 用途 |
|-------|-------|------|
| `radius-sm` | 4px | 小さな要素、バッジ |
| `radius-md` | 8px | ボタン、入力 |
| `radius-lg` | 12px | カード |
| `radius-xl` | 16px | モーダル、大きなパネル |
| `radius-full` | 9999px | アバター、ピル |

---

## Shadow

| Token | Value | 用途 |
|-------|-------|------|
| `shadow-sm` | `0 1px 2px rgba(44, 51, 48, 0.05)` | カードのデフォルト |
| `shadow-md` | `0 4px 12px rgba(44, 51, 48, 0.08)` | ホバー時 |
| `shadow-lg` | `0 8px 24px rgba(44, 51, 48, 0.12)` | モーダル |

---

## Components（メタクリドキュメント用）

### 対話ブロック（Dialogue）

スピーカーごとに色分け:

| Speaker | Background | Border (left 4px) | Label Color |
|---------|-----------|-------------------|-------------|
| Tamkai | `sage-50` | `sage-400` | `sage-600` |
| Opi | `blue-50` | `blue-400` | `blue-600` |
| Osato | `gold-50` | `gold-400` | `gold-600` |

- スピーカー名: `label` サイズ、各色の600、`Inter 600` or `Noto Sans JP 700`
- 発言テキスト: `body`、`text-primary`
- ブロック間: `space-4`
- パディング: `space-4` 〜 `space-6`
- 角丸: `radius-md`

### 導の文（Guide Text）

- 背景: なし（本文と同じ流れ）
- テキスト: `Noto Sans JP 500`、`text-secondary`
- 行間: 2
- 枠やボーダーで囲まない。ウェイトと色の違いで本文と区別

### 註釈ブロック（Annotation）

- 背景: `gold-50`
- ボーダー: `gold-100` の1px
- 左ボーダー: `gold-400` の4px（Composition内では `gold-200` の3px）
- タイトル: `h3`、`gold-600`
- テキスト: `body-sm`、`text-secondary`
- パディング: `space-4` 〜 `space-6`
- 角丸: `radius-md`（Composition内では右のみ `radius-sm`）

### 引用ブロック（Quote / Highlight）

- 背景: `rose-50`（Composition内では背景なし）
- 左ボーダー: `rose-400` の4px（Composition内では `rose-200` の3px）
- テキスト: `Noto Serif JP 400 italic`、`text-primary`
- 引用符: `rose-200`、2rem
- パディング: `space-4` 〜 `space-6`

### 目次（Table of Contents）

- 背景: `surface`
- ボーダー: `border` の1px
- リンク: `text-secondary` → hover `sage-600`
- 現在地: `sage-400` のドット + `text-primary`
- パディング: `space-6`
- 角丸: `radius-lg`

### ボタン

| Variant | Background | Text | Border |
|---------|-----------|------|--------|
| Primary | `sage-400` | `white` | none |
| Primary Hover | `sage-600` | `white` | none |
| Secondary | transparent | `sage-600` | `sage-200` 1px |
| CTA | `gold-400` | `white` | none |
| Danger | `red-400` | `white` | none |

- パディング: `space-3` `space-6`
- 角丸: `radius-md`
- フォント: `label`

---

## Animation & Transition

### サイトUI共通

| Token | Value | 用途 |
|-------|-------|------|
| `duration-fast` | 150ms | ホバー、フォーカス |
| `duration-normal` | 250ms | 状態変化 |
| `duration-slow` | 400ms | パネル開閉 |
| `easing-default` | `cubic-bezier(0.4, 0, 0.2, 1)` | 標準 |
| `easing-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | バウンス |

### サイトUIルール
- アニメーションは控えめに。「アトリエの朝」は静かな空間
- ページ読み込み時のフェードインは `duration-slow`、`easing-default`
- ホバーエフェクトは `duration-fast` のみ

### Rich HTML アニメーション（Ep.19 正式仕様）

PCとモバイルで異なるアニメーション方式を使用する。実装リファレンス: `rich-ep19-travel.html`

#### PC版（1024px以上）: 時間ベース・ワンショット

IntersectionObserver でビューポート 70% 到達時にトリガー。一度表示された要素はそのまま維持。

| 要素 | 初期 transform | duration | easing |
|------|---------------|----------|--------|
| デフォルト `.reveal` | `translateY(40px)` | **0.85s** | `ease-out` |
| `.chapter-header` | `scale(0.85) translateY(30px)` | 0.95s | `ease-out` |
| `.section-divider` | `scaleX(0.3)` | 0.75s | `ease-out` |
| `.concept-diagram` / `.contrast-diagram` | `scale(0.9)` | 0.85s | `ease-out` |
| `.takeaway-card` | `scale(0.9) translateY(20px)` | 0.75s | `ease-out` |
| `.annotation` | `translateY(30px)` | **1.3s** | `cubic-bezier(0.25, 0.1, 0.25, 1)` |
| `.dialogue-item`（奇数） | `translateX(-60px)` | 0.8s | `ease-out` |
| `.dialogue-item`（偶数） | `translateX(60px)` | 0.8s | `ease-out` |

**breathing delay（一呼吸の遅延）**:
- 導の文 → 対話ブロック最初の発言: **0.2s**
- 対話ブロック → 次の導の文: **0.18s**
- ダイアログスタガー: `index × 80ms`（最大 300ms）

#### モバイル版: CSS scroll-driven animation（Spotlight）

`animation-timeline: view()` でスクロール連動。コンテンツの可読性をスクロール位置で制御。

| パラメータ | モバイル | PC（フォールバック参考） |
|-----------|---------|---------------------|
| 可読ゾーン | 30%-70% | 25%-75% |
| 最小 opacity | 0.2 | 0.35 |
| 最大 blur | 1px | 0.5px |
| translateY（入場時） | 6px | 4px |

#### アニメーション設計原則
- **PC版**: 「ダイナミックだが一度きり」
- **モバイル版**: 「効いているけど気づかない」
- Atmosphere Shift: `background-color 0.8s` で背景色を滑らかに遷移
- アノテーションはクリック展開のみ（自動展開はしない）

---

## Dark Pattern: 「書斎の夜」

夜の書斎。読書灯がひとつ点いている。革張りの椅子、木の机、積み上げられた本。静かで深い集中の時間。

- **暗さは温かい**: 真っ黒（#000）は使わない。木や革を思わせるウォームダーク
- **色は灯りに照らされる**: ライトテーマの色相を維持し、明度を落として彩度をやや上げる
- **テキストは紙の色**: 真っ白（#FFF）ではなくクリーム〜アイボリーで目に優しく
- **コントラストは控えめに**: 読書灯の柔らかい光。ギラつかない

### Dark Neutrals

| Token | Light | Dark | Dark RGB | 用途 |
|-------|-------|------|----------|------|
| `base` | `#F5F0E8` | `#1C1A17` | 28, 26, 23 | ページ背景（深い木の色） |
| `surface` | `#FAF8F5` | `#252320` | 37, 35, 32 | カード、パネル（やや浮いた面） |
| `surface-raised` | — | `#2E2B27` | 46, 43, 39 | ホバー、モーダル（さらに浮いた面） |
| `white` | `#FDFCFA` | `#E8E4DC` | 232, 228, 220 | テキストオンダーク → オンライト |
| `text-primary` | `#2C3330` | `#E2DDD5` | 226, 221, 213 | 本文テキスト（古紙のクリーム色） |
| `text-secondary` | `#6B6560` | `#A09890` | 160, 152, 144 | 補助テキスト |
| `text-muted` | `#9E9690` | `#6B6360` | 107, 99, 96 | プレースホルダー |
| `border` | `#E5DFD6` | `#3A3630` | 58, 54, 48 | 標準ボーダー（うっすら見える程度） |

### Dark Core Colors

#### Sage — Dark「暗がりの植物」

| Token | Light | Dark | Dark RGB |
|-------|-------|------|----------|
| `sage-50` | `#F4F6F2` | `#1E221C` | 30, 34, 28 |
| `sage-100` | `#E2E8DD` | `#2A302A` | 42, 48, 42 |
| `sage-200` | `#C5D1BC` | `#3D4A38` | 61, 74, 56 |
| `sage-400` | `#8B9A7D` | `#708A62` | 112, 138, 98 |
| `sage-600` | `#5E6E52` | `#A8BF9A` | 168, 191, 154 |

#### Rose — Dark「読書灯のローズ」

| Token | Light | Dark | Dark RGB |
|-------|-------|------|----------|
| `rose-50` | `#FDF5F3` | `#241C1A` | 36, 28, 26 |
| `rose-100` | `#F8E4DF` | `#332422` | 51, 36, 34 |
| `rose-200` | `#F0C4BB` | `#5A3A34` | 90, 58, 52 |
| `rose-400` | `#E8A598` | `#B87A72` | 184, 122, 114 |
| `rose-600` | `#D88B7A` | `#E8A598` | 232, 165, 152 |

#### Gold — Dark「真鍮のランプ」

| Token | Light | Dark | Dark RGB |
|-------|-------|------|----------|
| `gold-50` | `#FDF9EE` | `#22201A` | 34, 32, 26 |
| `gold-100` | `#F7EDCC` | `#302A1E` | 48, 42, 30 |
| `gold-200` | `#EEDEA5` | `#504020` | 80, 64, 32 |
| `gold-400` | `#C4A057` | `#B89040` | 184, 144, 64 |
| `gold-600` | `#9A7B3A` | `#E0C070` | 224, 192, 112 |

#### Red — Dark「炉の赤」

| Token | Light | Dark | Dark RGB |
|-------|-------|------|----------|
| `red-50` | `#FEF2F1` | `#261816` | 38, 24, 22 |
| `red-100` | `#FDDBD8` | `#3A2220` | 58, 34, 32 |
| `red-400` | `#E74C3C` | `#D04838` | 208, 72, 56 |
| `red-600` | `#C0392B` | `#F07060` | 240, 112, 96 |

### Dark Extended Colors

#### Blue — Dark「月明かり」

| Token | Light | Dark | Dark RGB |
|-------|-------|------|----------|
| `blue-50` | `#F0F5FA` | `#181E24` | 24, 30, 36 |
| `blue-100` | `#D6E4F0` | `#1E2C38` | 30, 44, 56 |
| `blue-400` | `#5B8DB8` | `#5588B0` | 85, 136, 176 |
| `blue-600` | `#3A6B91` | `#88BDE0` | 136, 189, 224 |

#### Purple — Dark「夜のラベンダー」

| Token | Light | Dark | Dark RGB |
|-------|-------|------|----------|
| `purple-50` | `#F5F2F8` | `#1E1A22` | 30, 26, 34 |
| `purple-100` | `#E4DCF0` | `#282030` | 40, 32, 48 |
| `purple-400` | `#8B7AAD` | `#8070A5` | 128, 112, 165 |
| `purple-600` | `#6B5A8E` | `#B8A0D8` | 184, 160, 216 |

### Dark Shadow

| Token | Light | Dark |
|-------|-------|------|
| `shadow-sm` | `0 1px 2px rgba(44,51,48,0.05)` | `0 1px 3px rgba(0,0,0,0.3)` |
| `shadow-md` | `0 4px 12px rgba(44,51,48,0.08)` | `0 4px 12px rgba(0,0,0,0.4)` |
| `shadow-lg` | `0 8px 24px rgba(44,51,48,0.12)` | `0 8px 24px rgba(0,0,0,0.5)` |

### Dark カラー運用ルール

1. **明度反転の原則**: ライトで50-100（薄い色）だった背景は、ダークでも50-100トークンを使う（値が暗い色に反転済み）
2. **アクセント色は明るくなる**: 400-600トークンはダークモードでやや明度を上げ、暗い背景上で視認性を確保
3. **背景の階層**: `base` → `surface` → `surface-raised` → `[color]-50` の4段階
4. **グラデーション禁止**: ダークモードでグラデーションは汚く見えやすい。ソリッドカラーのみ
5. **ボーダーは控えめに**: `border` は背景との差がわずかでいい。存在を主張しない

### 実装方法

```css
/* ライトテーマ（デフォルト） */
:root {
  --base: #F5F0E8;
  --surface: #FAF8F5;
  /* ... */
}

/* ダークテーマ */
[data-theme="dark"] {
  --base: #1C1A17;
  --surface: #252320;
  --surface-raised: #2E2B27;
  /* ... */
}
```

- `data-theme` 属性で切り替え（メタクリスペース既存方式と統一）
- `prefers-color-scheme` メディアクエリでのOS連動もサポート
- フラッシュ防止のため、`<head>` 内でインラインスクリプトによる即時適用

---

## Tone of Voice

### コピーの言葉遣い
- **一人称**: 「私たち」ではなく「メタクリ」または主語なし
- **語尾**: 「〜です・ます」ベース。堅すぎず砕けすぎず
- **カタカナ語**: 必要なら使うが、日本語で言えるなら日本語で
- **問いかけ**: メタクリドキュメントでは読者への問いかけを積極的に使う

### UIテキスト
- **ボタン**: 簡潔（「聴く」「読む」「もっと見る」）
- **エラー**: 具体的で親切（「接続できませんでした。もう一度お試しください」）
- **空状態**: 前向き（「まだエピソードがありません」→「最初のエピソードを追加しましょう」）

---

## 適用ガイド

### プロダクト別の適用

| プロダクト | Primary | Secondary | Extended | Typography |
|-----------|---------|-----------|----------|------------|
| **メタクリサイト** | Sage + Gold | Rose + Red | Blue | M PLUS Rounded 1c（既存維持）→ リニューアル時にNoto Sans JP |
| **メタクリドキュメント** | Sage | Rose, Gold | — | Noto Sans JP + Noto Serif JP |
| **メタクリスペース** | Sage | Rose | Blue, Purple | Noto Sans JP + Inter |
| **METACRI SCAN** | Sage + Rose | — | — | Inter + Noto Sans JP |

### 段階的な適用計画

1. **Phase 1**: メタクリドキュメント HTML（Type B/Type A）に適用
2. **Phase 2**: メタクリスペースのカラー調整
3. **Phase 3**: サイトリニューアル時に適用
4. **Phase 4**: METACRI SCAN に適用

---

## Hero Color Sets（Rich HTML用）

Rich HTML のヒーローセクションにおいて、エピソードごとのビジュアル差別化を実現するためのカラーセット定義。グロー（背景 radial-gradient）、フローティングシェイプの色・形状、テキストアクセントを連動させて「空気」を変える。

### 設計原則

- **外部アセット不要**: CSSの値を変えるだけで実現。画像や絵文字に頼らない
- **パレット内で収める**: DESIGN_LANGUAGE のカラーシステム内の色のみ使用
- **3レイヤー連動**: グロー・シェイプ・アクセントの色を統一して空気感を作る

### カラーセット一覧

#### Default（デフォルト）— gold + sage

現行の標準セット。汎用的に使える。

| レイヤー | 値 |
|---------|-----|
| グロー | `gold(0.3)` + `sage(0.25)` + `gold(0.15)` |
| シェイプ色 | `gold-400`, `sage-400` |
| シェイプ形状 | 円、45度回転四角、有機形 |
| hero-label | `gold-400` |
| .accent gradient | `sage-400 → gold-400` |
| hero-meta dot | `gold-400` |

#### Intellectual（知的・構造系）— blue + purple

組織論、フレームワーク、分析的なテーマに。

| レイヤー | 値 |
|---------|-----|
| グロー | `blue(0.3)` + `purple(0.25)` + `blue(0.15)` |
| シェイプ色 | `blue-400`, `purple-400` |
| シェイプ形状 | 円、六角形（clip-path）、角丸四角15度回転、小円 |
| hero-label | `blue-400` |
| .accent gradient | `blue-400 → purple-400` |
| hero-meta dot | `blue-400` |

#### Adventure（冒険・開放系）— gold + blue

旅、探索、外の世界との出会いがテーマに。

| レイヤー | 値 |
|---------|-----|
| グロー | `gold(0.3)` + `blue(0.25)` + `gold(0.15)` |
| シェイプ色 | `gold-400`, `blue-400` |
| シェイプ形状 | 円、楕円、ゆるいカーブ |
| hero-label | `gold-400` |
| .accent gradient | `gold-400 → blue-400` |
| hero-meta dot | `gold-400` |

#### Warmth（手触り・温かみ系）— sage + rose

手仕事、身体性、人間的な温かさがテーマに。

| レイヤー | 値 |
|---------|-----|
| グロー | `sage(0.3)` + `rose(0.25)` + `sage(0.15)` |
| シェイプ色 | `sage-400`, `rose-400` |
| シェイプ形状 | 円、有機形、波形 |
| hero-label | `sage-400` |
| .accent gradient | `sage-400 → rose-400` |
| hero-meta dot | `sage-400` |

### 運用ルール

1. **テーマからセットを選ぶ**: エピソードの主題に最も近いカテゴリを選択
2. **迷ったらDefault**: 複数のテーマが混在する場合は Default を使用
3. **新セットの追加**: 既存4セットで表現できないテーマが出た場合、Extended Colors（Blue, Purple）の範囲内で新セットを定義可
4. **本文には影響しない**: ヒーローセクションのみに適用。本文の対話ブロック・註釈・導の文の色は変えない

### 実装リファレンス

- **Default**: [rich-ep19-travel.html](html-samples/rich-ep19-travel.html), [rich-ep12-bricolage.html](html-samples/rich-ep12-bricolage.html)
- **Intellectual**: [rich-20251129-organizational-creativity.html](html-samples/rich-20251129-organizational-creativity.html)

---

**Version**: 1.1
**Created**: 2026-02-04
**Last Updated**: 2026-02-07（Hero Color Sets 追加）
**Author**: tamkai + Claude Code (Creative Director)
**North Star**: アトリエの朝
