# AI Agent Sample

業務メモをAIで整理するサンプルアプリです。

このリポジトリでは、LLM APIを使った業務支援アプリを題材に、AI活用アプリの基本構成、プロンプト設計、LLMクライアントの抽象化、テストしやすい設計を段階的に整備していきます。

## このリポジトリで示したいこと

- AIを使った業務支援アプリの基本構成
- プロンプトをコードから分離して管理する設計
- LLM APIへの依存を分離する設計
- モックを使って外部APIに依存せずテストする方法
- Streamlitなどを使った簡易UI
- README、Issue、Pull Requestを使った開発運用

## 想定するアプリ

入力された業務メモをもとに、以下の内容を整理します。

- 要約
- 決定事項
- TODO
- リスク
- 次に確認すべきこと

## セットアップ

```bash
uv sync
```

## テスト

```bash
uv run pytest
```

## Lint

```bash
uv run ruff check . --fix
uv run ruff format .
uv run ruff check .
```

## CI

このリポジトリでは、GitHub Actionsを使ってPull Request作成時およびmainブランチへのpush時に、Lintとテストを自動実行します。

実行しているチェックは以下です。

```bash
uv run ruff check .
uv run pytest
```

これにより、コード変更時に最低限の品質確認を自動化しています。


## CLIでの実行

CLIから業務メモ整理ロジックを実行できます。

現時点では外部LLM APIは呼び出さず、モックLLMクライアントを使って固定レスポンスを返します。

```bash
uv run python -m app.cli "金曜日までに資料を確認する。レビュー時間が不足する可能性がある。"
```

出力例：

```bash
Input:
金曜日までに資料を確認する。レビュー時間が不足する可能性がある。

Summary:
入力された業務メモを整理した要約です。

Decisions:
- 現時点ではモックの決定事項です。

TODO:
- 資料を確認する

Risks:
- レビュー時間が不足する可能性があります。

Next Actions:
- レビュー日程を確認する
```

## 現在の実装範囲

現時点では、モックLLMクライアントが返すJSON文字列を `OrganizedNote` に変換する処理を実装しています。

LLMレスポンスは以下の項目を持つJSON形式を想定しています。

```json
{
  "summary": "要約",
  "decisions": ["決定事項"],
  "todos": ["TODO"],
  "risks": ["リスク"],
  "next_actions": ["次に確認すべきこと"]
}
```

JSON文字列の解析処理は app/parsers/ に分離しています。
これにより、LLMレスポンスの形式チェックとアプリケーション内部モデルへの変換を独立してテストできるようにしています。



プロンプト生成処理は `app/prompts/` に分離しています。
これにより、業務ロジックとプロンプト設計を分けて管理できるようにしています。

LLM呼び出し部分は `app/llm/` に分離し、アプリケーションロジックが特定の外部LLM APIに直接依存しない構成にしています。

現時点では外部LLM APIは呼び出していません。
モックLLMクライアントを使い、外部APIキーなしでテストできる構成にしています。

## 今後の予定

- LLMレスポンスの構造化
- テストカバレッジの確認
- READMEの整理
- Streamlit UIの追加
- 外部LLM API連携
