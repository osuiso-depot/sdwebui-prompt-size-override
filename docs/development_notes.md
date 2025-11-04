# Prompt Size Override Extension - 開発メモ

## 目的
プロンプトで生成される画像の、幅と高さをプロンプト文字列の「埋め込み設定」によって変更する。
UI上の幅・高さ設定を、「埋め込み設定」によって上書きする機能。
ただし、UI上の表示や実際の設定は上書きされず、そのプロンプトの生成時のみ適用される。

## 機能
1. 処理するプロンプトに、コメント行「#」を利用した「埋め込み設定」を処理する。
2. 「埋め込み設定」は連想配列であり、例えば「{"width":1024,"height":1024}」というフォーマット。
3. widthは生成画像の幅、heightは高さである。

## 検討事項
*   **Custom-script vs Extension**: Extensionで実装する。
    *   UI上のトグルボタンで簡単に切り替え可能。
    *   他のユーザースクリプトと併用可能。
*   **プロンプト解析**:
    *   `modules/prompt_parser.py`の既存機能は利用せず、正規表現とJSONパースで独自に実装する。
    *   プロンプトの埋め込み設定のフォーマットは `#{"width":1024,"height":1024}#` のような形式を想定。
*   **画像生成パラメータの変更**:
    *   `modules/processing.py`の`StableDiffusionProcessing`クラスの`width`と`height`属性を上書きする。
    *   Hires. fix関連のパラメータ（`hr_resize_x`, `hr_resize_y`, `hr_upscale_to_x`, `hr_upscale_to_y`）も変更対象とするか検討。
*   **UI要素の追加**:
    *   Extension内の個別機能（幅・高さの上書き）の有効/無効を切り替えるトグルボタンをWebUIの拡張機能用の設定項目に配置する。
    *   参考ファイル: `extensions\sd-dynamic-prompts\sd_dynamic_prompts\settings.py`
*   **コールバック**:
    *   `modules/script_callbacks.py`の`on_before_process`または`on_before_process_batch`を利用して、画像生成前にパラメータを変更する。

## TODOリスト
- [x] Extensionのディレクトリ構造と`metadata.ini`の作成
- [x] `modules/processing.py`を読み込み、画像生成パラメータ（幅、高さ）の具体的な属性を特定する
- [x] プロンプトから「埋め込み設定」を抽出するロジックを実装する (正規表現とJSONパースを使用)
- [x] 抽出した設定を画像生成パラメータに適用するロジックを実装する
- [x] UIにトグルボタンを追加し、Extensionの有効/無効を切り替える機能を実装する (WebUIの拡張機能設定に配置)
- [x] 他のユーザースクリプトとの併用を考慮した設計を行う
- [x] テストコードを作成し、機能が正しく動作することを確認する
