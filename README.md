# Prompt Size Override Extension for Stable Diffusion WebUI

この拡張機能は、プロンプト文字列に埋め込まれた設定を使用して、生成される画像の幅と高さを上書きします。UI上の幅と高さの設定は変更されず、画像生成時にのみ適用されます。

## 機能

*   **プロンプトからの設定抽出**: プロンプト内のコメント行（`#`で始まる行）からJSON形式の設定を抽出します。
    *   例: `a beautiful landscape #{"width":1024,"height":768}#`
*   **画像サイズの自動調整**: 抽出された`width`と`height`の値に基づいて、生成画像のサイズを自動的に調整します。
*   **Hires. fix対応**: Hires. fixが有効な場合、`hr_resize_x`、`hr_resize_y`、`hr_upscale_to_x`、`hr_upscale_to_y`などのHires. fix関連のパラメータもプロンプトから設定できます。
    *   例:
    > #comment line ... #{"width":512,"height":512,"hr_resize_x":1024,"hr_resize_y":1024}#
    >
    > a cat
*   **UIからの有効/無効切り替え**: WebUIの「Settings」タブにある「Prompt Size Override」セクションから、この拡張機能の機能を簡単に有効/無効にできます。

## 使用方法

1.  Stable Diffusion WebUIを起動します。
2.  「Settings」タブに移動し、「Prompt Size Override」セクションを見つけます。
3.  「Enable Prompt Size Override」チェックボックスをオンにして、機能を有効にします。
4.  「txt2img」または「img2img」タブに移動します。
5.  プロンプト入力欄のコメント行に、生成したい画像の説明と、埋め込み設定をJSON形式で追加します。設定は`#`で囲んでください。
    *   例:
    > #{"width":1280,"height":720}#
    >
    > a futuristic city at night
6.  通常通り画像を生成します。指定した幅と高さで画像が生成されます。

## 注意事項

*   プロンプト内の埋め込み設定は、UI上の幅と高さの設定よりも優先されます。
*   埋め込み設定は、JSON形式で正しく記述されている必要があります。不正な形式の場合、設定は無視されます。
*   Hires. fixのパラメータを設定する場合、`enable_hr`がTrueである必要があります。
