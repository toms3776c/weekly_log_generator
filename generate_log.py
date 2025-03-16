#!/usr/bin/env python3
from datetime import datetime, timedelta
import os
import argparse

def get_week_dates(target_date=None):
    """指定された日付（デフォルトは今日）を含む週の日付情報を取得"""
    if target_date is None:
        target_date = datetime.now()
    
    # 月曜日を取得（日本では月曜始まりが一般的）
    monday = target_date - timedelta(days=target_date.weekday())
    dates = {
        'week_start_date': monday.strftime('%Y/%m/%d'),
        'week_end_date': (monday + timedelta(days=6)).strftime('%Y/%m/%d'),
        'monday_date': monday.strftime('%Y/%m/%d'),
        'tuesday_date': (monday + timedelta(days=1)).strftime('%Y/%m/%d'),
        'wednesday_date': (monday + timedelta(days=2)).strftime('%Y/%m/%d'),
        'thursday_date': (monday + timedelta(days=3)).strftime('%Y/%m/%d'),
        'friday_date': (monday + timedelta(days=4)).strftime('%Y/%m/%d'),
    }
    return dates

def generate_weekly_log(template_path, output_dir, target_date=None):
    """週次作業ログを生成"""
    # テンプレートを読み込む
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # 日付情報を取得
    dates = get_week_dates(target_date)
    
    # テンプレートに日付を埋め込む
    log_content = template_content.format(**dates)
    
    # 出力ディレクトリが存在しない場合は作成
    os.makedirs(output_dir, exist_ok=True)
    
    # 出力ファイル名を生成（例: weekly_log_2025_02_24-2025_03_02.md）
    output_filename = f"weekly_log_{dates['week_start_date'].replace('/', '_')}-{dates['week_end_date'].replace('/', '_')}.md"
    output_path = os.path.join(output_dir, output_filename)
    
    # ファイルに書き出し
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(log_content)
    
    return output_path

def main():
    parser = argparse.ArgumentParser(description='週次作業ログジェネレーター')
    parser.add_argument('--date', help='対象週の日付（YYYY-MM-DD形式）。指定がない場合は今日の日付を使用。')
    parser.add_argument('--template', default='templates/template.md',
                      help='テンプレートファイルのパス（デフォルト: templates/template.md）')
    parser.add_argument('--output-dir', default='logs',
                      help='出力先ディレクトリ（デフォルト: logs）')
    
    args = parser.parse_args()
    
    # 日付の指定がある場合はパース
    target_date = None
    if args.date:
        target_date = datetime.strptime(args.date, '%Y-%m-%d')
    
    # スクリプトのディレクトリをベースにパスを解決
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, args.template)
    output_dir = os.path.join(script_dir, args.output_dir)
    
    # ログファイルを生成
    output_path = generate_weekly_log(template_path, output_dir, target_date)
    print(f'週次作業ログを生成しました: {output_path}')

if __name__ == '__main__':
    main()
