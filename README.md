# 週次作業ログジェネレーター

テンプレートから週次作業ログを生成するPythonスクリプトです。

## 使い方

1. 基本的な使い方（今週の作業ログを生成）:
```bash
python generate_log.py
```

2. 特定の週の作業ログを生成:
```bash
python generate_log.py --date 2025-02-24
```

3. カスタムテンプレートと出力先を指定:
```bash
python generate_log.py --template custom_template.md --output-dir custom_logs
```

4. 日付指定とサブフォルダへの出力:
```bash
python generate_log.py --date 2025-04-28 --output-dir 2025/04
```

## オプション

- `--date`: 対象週の日付（YYYY-MM-DD形式）。指定がない場合は今日の日付を使用。
- `--template`: テンプレートファイルのパス（デフォルト: templates/template.md）
- `--output-dir`: 出力先ディレクトリ（デフォルト: logs）

## テンプレートのカスタマイズ

`templates/template.md` を編集することで、生成される作業ログの形式をカスタマイズできます。
以下のプレースホルダーが使用可能です：

- `{week_start_date}`: 週の開始日（月曜日）
- `{week_end_date}`: 週の終了日（日曜日）
- `{monday_date}`: 月曜日の日付
- `{tuesday_date}`: 火曜日の日付
- `{wednesday_date}`: 水曜日の日付
- `{thursday_date}`: 木曜日の日付
- `{friday_date}`: 金曜日の日付
