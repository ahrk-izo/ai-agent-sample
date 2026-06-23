# AI Agent Sample

業務メモをAIで整理するサンプルアプリです。

このリポジトリでは、LLMを使った業務支援アプリを題材に、AI活用アプリの基本構成、プロンプト管理、LLMクライアントの抽象化、レスポンス構造化、テストしやすい設計を段階的に整備しています。

現時点では外部LLM APIは呼び出さず、モックLLMクライアントを使って、外部APIキーなしで動作確認・テストできる構成にしています。

## このリポジトリについて

このリポジトリは、AIエージェントやRAGアプリの前段階として、LLMを使った業務支援アプリの基本設計を整理することを目的としています。

サンプルアプリでは、入力された業務メモを以下の項目に整理します。

- 要約
- 決定事項
- TODO
- リスク
- 次に確認すべきこと

単にLLM APIを呼び出すだけでなく、以下のような実務で重要になりやすい観点を意識しています。

- LLM APIへの依存をアプリケーションロジックから分離する
- プロンプト生成処理を分離して管理する
- LLMレスポンスを構造化データとして扱う
- 外部APIに依存せずテストできるようにする
- CLIでコアロジックを手元で確認できるようにする
- CIとカバレッジで品質確認を自動化する

## このリポジトリで示したいこと

このリポジトリでは、以下を示すことを意識しています。

- AIを使った業務支援アプリの基本構成
- Pydanticモデルによる入出力定義
- LLMクライアントの抽象化
- モックLLMクライアントによるテストしやすい設計
- プロンプト生成処理の分離
- LLMレスポンスのJSON構造化
- CLIによるローカル動作確認
- pytestによる自動テスト
- RuffによるLintとフォーマット
- pytest-covによるカバレッジ確認
- GitHub ActionsによるCI
- Issue、Pull Request、自己レビューコメントを使った開発運用

## 主な機能

- 業務メモ入力モデル
- 業務メモ整理結果モデル
- LLMクライアントインターフェース
- モックLLMクライアント
- 業務メモ整理用プロンプト生成
- LLMレスポンスJSONパーサー
- CLI実行機能
- Lint、テスト、カバレッジ確認
- CIでのHTMLカバレッジレポート保存
- Streamlitによる簡易UI
- DockerによるStreamlit UI起動

## 技術スタック

- Python
- Pydantic
- pytest
- pytest-cov
- Ruff
- GitHub Actions
- uv
- Streamlit
- OpenAI SDK
- Docker
- Docker Compose

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
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── streamlit_app.py
│   │   └── streamlit_view_model.py
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
├── .dockerignore
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── .python-version
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── uv.lock
└── README.md
```

## セットアップ

依存関係をインストールします。

```bash
uv sync
```


## OpenAI API連携

デフォルトでは `MockLLMClient` を使用します。

OpenAI APIを使う場合は、`OPENAI_API_KEY` を環境変数として設定し、`LLM_PROVIDER=openai` を指定します。

```bash
export OPENAI_API_KEY="your_api_key_here"
LLM_PROVIDER=openai uv run python -m app.cli "金曜日までに資料を確認する。レビュー時間が不足する可能性がある。"
```

モデルを変更する場合は、`OPENAI_MODEL` を指定します。

```bash
OPENAI_MODEL=gpt-4.1-mini LLM_PROVIDER=openai uv run python -m app.cli "金曜日までに資料を確認する。レビュー時間が不足する可能性がある。"
```

`OPENAI_API_KEY` が未設定の場合は、OpenAI APIを呼び出さず、`MockLLMClient` を使用します。

CIでは外部OpenAI APIを呼び出しません。
そのため、APIキーなしでもテストとCIが実行できる構成にしています。

OpenAI APIを利用するには、OpenAI Platform側でBilling設定が必要です。
`OPENAI_API_KEY` を設定していても、API利用枠やクレジットが不足している場合は `insufficient_quota` エラーになることがあります。
その場合は、OpenAI PlatformのBilling画面で支払い方法やクレジット残高を確認してください。

## CLIでの実行

CLIから業務メモ整理ロジックを実行できます。

デフォルトでは、外部LLM APIを呼び出さず、モックLLMクライアントを使って固定のJSONレスポンスを返します。

```bash
uv run python -m app.cli "金曜日までに資料を確認する。レビュー時間が不足する可能性がある。"
```

OpenAI APIを使う場合は、`OPENAI_API_KEY` を設定し、`LLM_PROVIDER=openai` または `--provider openai` を指定します。

```bash
LLM_PROVIDER=openai uv run python -m app.cli "金曜日までに資料を確認する。レビュー時間が不足する可能性がある。"
```

または、以下のように指定できます。

```bash
uv run python -m app.cli --provider openai "金曜日までに資料を確認する。レビュー時間が不足する可能性がある。"
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

## Streamlit UIでの実行

Streamlitを使って、ブラウザ上から業務メモ整理ロジックを確認できます。

```bash
PYTHONPATH=. uv run streamlit run app/ui/streamlit_app.py
```

起動後、ブラウザで業務メモを入力し、「整理する」ボタンを押すと、以下の項目に分けて整理結果を表示します。

- Summary
- Decisions
- TODO
- Risks
- Next Actions

UI上で `mock` / `openai` を選択できます。

`openai` を選択する場合は、事前に `OPENAI_API_KEY` を設定してください。
`OPENAI_API_KEY` が未設定の場合は、OpenAI APIを呼び出さず、MockLLMClientを使用します。

```bash
export OPENAI_API_KEY="your_api_key_here"
PYTHONPATH=. LLM_PROVIDER=openai uv run streamlit run app/ui/streamlit_app.py
```


## Dockerでの実行

Dockerを使って、ローカルのPython環境に依存せずStreamlit UIを起動できます。

デフォルトでは `MockLLMClient` を使用します。


```bash
docker compose up --build
```

起動後、ブラウザで以下にアクセスします。

```text
http://localhost:8501
```

終了する場合は、別ターミナルで以下を実行します。

```bash
docker compose down
```

OpenAI APIを使う場合は、`OPENAI_API_KEY` と `LLM_PROVIDER=openai` を指定します。

```bash
OPENAI_API_KEY="your_api_key_here" LLM_PROVIDER=openai docker compose up --build
```

モデルを指定する場合は、`OPENAI_MODEL` を指定します。

```bash
OPENAI_API_KEY="your_api_key_here" LLM_PROVIDER=openai OPENAI_MODEL=gpt-4.1-mini docker compose up --build
```

`OPENAI_API_KEY` が未設定の場合は、OpenAI APIを呼び出さず、MockLLMClientを使用します。


## 開発時の確認コマンド

通常のPR作成前は、以下を確認します。

```bash
uv run ruff check . --fix
uv run ruff format .
uv run ruff check .
uv run pytest
uv run pytest --cov=app --cov-report=term-missing --cov-report=html --cov-fail-under=80
uv run python -m app.cli "金曜日までに資料を確認する。レビュー時間が不足する可能性がある。"
```

Streamlit UIを変更した場合は、手動で画面起動も確認します。

```bash
PYTHONPATH=. uv run streamlit run app/ui/streamlit_app.py
```

OpenAI API連携を変更した場合のみ、APIキーを設定したうえで任意で実行確認します。

```bash
export OPENAI_API_KEY="your_api_key_here"
LLM_PROVIDER=openai uv run python -m app.cli "金曜日までに資料を確認する。レビュー時間が不足する可能性がある。"
```

OpenAI APIの実行確認は、APIキー、Billing設定、利用枠に依存するため、CIの必須チェックには含めません。


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

- APIキーなしでテストできる
- CIで外部APIに依存しない
- OpenAI、Azure OpenAI、Claudeなどに後から差し替えやすい
- アプリケーションロジックとLLM呼び出し処理を分離できる

## プロンプト管理

業務メモ整理用のプロンプト生成処理は `app/prompts/` に分離しています。

プロンプトをサービスロジック内に直接書かず、専用モジュールで管理することで、以下を実現しやすくしています。

- プロンプトの改善
- 出力形式の調整
- プロンプトのテスト
- 業務ロジックとプロンプト設計の分離

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

Streamlitの画面描画を行う `app/ui/streamlit_app.py` は、手動確認を前提とし、カバレッジ対象から除外しています。
UIから呼び出す業務ロジックは `app/ui/streamlit_view_model.py` に分離し、pytestでテストできるようにしています。


## CI

このリポジトリでは、GitHub Actionsを使ってPull Request作成時およびmainブランチへのpush時に、Lint、テスト、カバレッジ確認を自動実行します。

実行しているチェックは以下です。

```bash
uv run ruff check .
uv run pytest --cov=app --cov-report=term-missing --cov-report=html --cov-fail-under=80
```

CIでは、HTMLカバレッジレポートを `coverage-html` artifact として保存します。

これにより、コード変更時に最低限の品質確認を自動化しています。

DockerはStreamlit UIをローカル環境に依存せず起動するために用意しています。

現時点では、CI上でDockerを使ったテスト実行は行っていません。  
CIでは引き続き、GitHub Actions上でRuff、pytest、カバレッジ確認を実行します。


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

- Streamlit UIの改善
- 外部LLM API連携
- OpenAI / Azure OpenAI / Claude などのLLMクライアント実装


## 備考

このリポジトリは、完成済みのAIアプリではなく、AI活用アプリを実務的な構成で段階的に整備していくためのサンプルです。

外部LLM API連携やStreamlit UIは今後追加予定です。
現時点では、外部APIに依存しない形で、LLMクライアント抽象化、プロンプト管理、レスポンス構造化、テスト、CIを確認できる構成にしています。
