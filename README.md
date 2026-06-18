# AI Agent Sample

業務メモをAIで整理するサンプルアプリです。

このリポジトリでは、LLMを使った業務支援アプリを題材に、AI活用アプリの基本構成、プロンプト管理、LLMクライアントの抽象化、レスポンス構造化、テストしやすい設計を段階的に整備しています。

現時点では外部LLM APIは呼び出さず、モックLLMクライアントを使って、外部APIキーなしで動作確認・テストできる構成にしています。

## このリポジトリについて

このリポジトリは、AIエージェントやRAGアプリの前段階として、LLMを使った業務支援アプリの基本設計を整理することを目的としています。

サンプルアプリでは、入力された業務メモを以下の項目に整理します。

* 要約
* 決定事項
* TODO
* リスク
* 次に確認すべきこと

単にLLM APIを呼び出すだけでなく、以下のような実務で重要になりやすい観点を意識しています。

* LLM APIへの依存をアプリケーションロジックから分離する
* プロンプト生成処理を分離して管理する
* LLMレスポンスを構造化データとして扱う
* 外部APIに依存せずテストできるようにする
* CLIでコアロジックを手元で確認できるようにする
* CIとカバレッジで品質確認を自動化する

## このリポジトリで示したいこと

このリポジトリでは、以下を示すことを意識しています。

* AIを使った業務支援アプリの基本構成
* Pydanticモデルによる入出力定義
* LLMクライアントの抽象化
* モックLLMクライアントによるテストしやすい設計
* プロンプト生成処理の分離
* LLMレスポンスのJSON構造化
* CLIによるローカル動作確認
* pytestによる自動テスト
* RuffによるLintとフォーマット
* pytest-covによるカバレッジ確認
* GitHub ActionsによるCI
* Issue、Pull Request、自己レビューコメントを使った開発運用

## 主な機能

* 業務メモ入力モデル
* 業務メモ整理結果モデル
* LLMクライアントインターフェース
* モックLLMクライアント
* 業務メモ整理用プロンプト生成
* LLMレスポンスJSONパーサー
* CLI実行機能
* Lint、テスト、カバレッジ確認
* CIでのHTMLカバレッジレポート保存

## 技術スタック

* Python
* Pydantic
* pytest
* pytest-cov
* Ruff
* GitHub Actions
* uv

## ディレクトリ構成

```text
ai-agent-sample/
├── app/
│   ├── llm/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── mock.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── note.py
│   ├── parsers/
│   │   ├── __init__.py
│   │   └── note_response_parser.py
│   ├── prompts/
│   │   ├── __init__.py
│   │   └── note_prompt.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── note_organizer.py
│   ├── __init__.py
│   ├── cli.py
│   └── main.py
├── tests/
│   ├── test_cli.py
│   ├── test_llm_client.py
│   ├── test_main.py
│   ├── test_note_organizer.py
│   ├── test_note_prompt.py
│   └── test_note_response_parser.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

## セットアップ

依存関係をインストールします。

```bash
uv sync
```

## CLIでの実行

CLIから業務メモ整理ロジックを実行できます。

現時点では外部LLM APIは呼び出さず、モックLLMクライアントを使って固定のJSONレスポンスを返します。

```bash
uv run python -m app.cli "金曜日までに資料を確認する。レビュー時間が不足する可能性がある。"
```

出力例：

```text
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

現時点では、以下の流れで業務メモを整理します。

```text
業務メモ入力
↓
Pydanticモデルで入力を検証
↓
プロンプト生成
↓
LLMクライアント経由でレスポンス取得
↓
JSON文字列をPydanticモデルに変換
↓
CLIで整理結果を表示
```

## LLMクライアントの抽象化

LLM呼び出し部分は `app/llm/` に分離しています。

アプリケーションロジックが特定の外部LLM APIに直接依存しないように、LLMクライアントのインターフェースを定義しています。

現時点では、外部APIを呼び出さずに固定レスポンスを返す `MockLLMClient` を使っています。

これにより、以下のメリットがあります。

* APIキーなしでテストできる
* CIで外部APIに依存しない
* OpenAI、Azure OpenAI、Claudeなどに後から差し替えやすい
* アプリケーションロジックとLLM呼び出し処理を分離できる

## プロンプト管理

業務メモ整理用のプロンプト生成処理は `app/prompts/` に分離しています。

プロンプトをサービスロジック内に直接書かず、専用モジュールで管理することで、以下を実現しやすくしています。

* プロンプトの改善
* 出力形式の調整
* プロンプトのテスト
* 業務ロジックとプロンプト設計の分離

## LLMレスポンスの構造化

LLMレスポンスは以下のJSON形式を想定しています。

```json
{
  "summary": "要約",
  "decisions": ["決定事項"],
  "todos": ["TODO"],
  "risks": ["リスク"],
  "next_actions": ["次に確認すべきこと"]
}
```

JSON文字列の解析処理は `app/parsers/` に分離しています。

これにより、LLMレスポンスの形式チェックとアプリケーション内部モデルへの変換を独立してテストできるようにしています。

不正なJSON形式や必須項目不足の場合は、エラーとして扱います。

## テスト・Lint・フォーマット

### テストの実行

```bash
uv run pytest
```

### Lintチェック

```bash
uv run ruff check .
```

### Lintの自動修正

```bash
uv run ruff check . --fix
```

### コードフォーマット

```bash
uv run ruff format .
```

### PR作成前の確認

PR作成前は、以下を実行します。

```bash
uv run ruff check . --fix
uv run ruff format .
uv run ruff check .
uv run pytest
```

## テストカバレッジ

pytest-covを使って、テストカバレッジを確認します。

```bash
uv run pytest --cov=app --cov-report=term-missing
```

`term-missing` を指定すると、テストされていない行を確認できます。

HTML形式で確認する場合は、以下を実行します。

```bash
uv run pytest --cov=app --cov-report=term-missing --cov-report=html --cov-fail-under=80
```

実行後、`htmlcov/index.html` をブラウザで開きます。

```bash
open htmlcov/index.html
```

CIでは最低カバレッジ率を80%に設定し、HTMLカバレッジレポートを `coverage-html` artifact として保存します。

## CI

このリポジトリでは、GitHub Actionsを使ってPull Request作成時およびmainブランチへのpush時に、Lint、テスト、カバレッジ確認を自動実行します。

実行しているチェックは以下です。

```bash
uv run ruff check .
uv run pytest --cov=app --cov-report=term-missing --cov-report=html --cov-fail-under=80
```

CIでは、HTMLカバレッジレポートを `coverage-html` artifact として保存します。

これにより、コード変更時に最低限の品質確認を自動化しています。

## 開発フロー

このリポジトリでは、実務を意識して以下の流れで開発を進めています。

```text
Issue作成
↓
featureブランチ作成
↓
実装
↓
Pull Request作成
↓
CI確認
↓
自己レビューコメント
↓
mainブランチへマージ
```

Pull Requestでは、1人開発でも確認内容を明記し、必要に応じて「自己レビュー済み」のコメントを残します。

## 今後の予定

今後は、必要に応じて以下のような拡張を検討します。

* Streamlit UIの追加
* 外部LLM API連携
* OpenAI / Azure OpenAI / Claude などのLLMクライアント実装
* APIキーや設定値の管理
* LLMレスポンス解析エラー時の扱い整理
* プロンプト改善
* RAG構成への拡張
* ファイル入力への対応
* READMEやサンプル利用手順の継続的な改善

## 備考

このリポジトリは、完成済みのAIアプリではなく、AI活用アプリを実務的な構成で段階的に整備していくためのサンプルです。

外部LLM API連携やStreamlit UIは今後追加予定です。
現時点では、外部APIに依存しない形で、LLMクライアント抽象化、プロンプト管理、レスポンス構造化、テスト、CIを確認できる構成にしています。
