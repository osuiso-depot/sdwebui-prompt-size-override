# Prompt Size Override Extension for Stable Diffusion WebUI

この拡張機能は、プロンプト文字列に埋め込まれた設定を使用して、生成される画像の幅と高さを上書きします。UI上の幅と高さの設定は変更されず、画像生成時にのみ適用されます。

## 機能

*   **プロンプトからの設定抽出**: プロンプト内のコメント行（`#`で始まる行）からJSON形式の設定を抽出します。
    *   例: `a beautiful landscape #{"width":1024,"height":768}#`
*   **画像サイズの自動調整**: 抽出された`width`と`height`の値に基づいて、生成画像のサイズを自動的に調整します。
*   **Hires. fix対応**: Hires. fixが有効な場合、`hr_resize_x`、`hr_resize_y`、`hr_upscale_to_x`、`hr_upscale_to_y`などのHires. fix関連のパラメータもプロンプトから設定できます。
    *   例:
    > #comment line ... #{"width":512,"height":512,"hr_resize_x":1024,"hr_resize_y":1024}#
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
    > a futuristic city at night
6.  通常通り画像を生成します。指定した幅と高さで画像が生成されます。

## 注意事項

*   プロンプト内の埋め込み設定は、UI上の幅と高さの設定よりも優先されます。
*   埋め込み設定は、JSON形式で正しく記述されている必要があります。不正な形式の場合、設定は無視されます。
*   Hires. fixのパラメータを設定する場合、`enable_hr`がTrueである必要があります。

## ライセンス
The MIT License

Copyright (c) 2025 osuiso-depot

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

以下に定める条件に従い、本ソフトウェアおよび関連文書のファイル（以下「ソフトウェア」）の複製を取得するすべての人に対し、ソフトウェアを無制限に扱うことを無償で許可します。これには、ソフトウェアの複製を使用、複写、変更、結合、掲載、頒布、サブライセンス、および/または販売する権利、およびソフトウェアを提供する相手に同じことを許可する権利も無制限に含まれます。

上記の著作権表示および本許諾表示を、ソフトウェアのすべての複製または重要な部分に記載するものとします。

ソフトウェアは「現状のまま」で、明示であるか暗黙であるかを問わず、何らの保証もなく提供されます。ここでいう保証とは、商品性、特定の目的への適合性、および権利非侵害についての保証も含みますが、それに限定されるものではありません。 作者または著作権者は、契約行為、不法行為、またはそれ以外であろうと、ソフトウェアに起因または関連し、あるいはソフトウェアの使用またはその他の扱いによって生じる一切の請求、損害、その他の義務について何らの責任も負わないものとします。

----
※この雛形の取得元
英語（http://www.opensource.org/licenses/mit-license.php）
日本語（http://sourceforge.jp/projects/opensource/wiki/licenses%2FMIT_license）
