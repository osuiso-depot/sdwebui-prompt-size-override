import gradio as gr
import modules.scripts as scripts
import re
import json

from modules import script_callbacks, shared

def on_ui_settings():
    section = ("prompt_size_override", "Prompt Size Override")
    shared.opts.add_option(
        key="prompt_size_override_enabled",
        info=shared.OptionInfo(
            True,
            label="Enable Prompt Size Override",
            section=section,
        ),
    )

script_callbacks.on_ui_settings(on_ui_settings)

class PromptSizeOverrideScript(scripts.Script):
    def title(self):
        return "Prompt Size Override"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        # UI要素は設定タブに移動したため、ここでは何も返さない
        return []

    def process(self, p):
        if not shared.opts.prompt_size_override_enabled:
            return

        # プロンプトから埋め込み設定を抽出する正規表現
        # 例: #{"width":1024,"height":1024}#
        match = re.search(r'#(\{.*\})#', p.prompt)
        if match:
            try:
                settings_str = match.group(1)
                settings = json.loads(settings_str)

                if "negative" in settings:
                    # p.negative_prompt を更新
                    p.negative_prompt = p.negative_prompt + ", " + settings["negative"]

                    # p.all_negative_prompts の各要素も更新
                    if p.all_negative_prompts:
                        p.all_negative_prompts = [np + ", " + settings["negative"] for np in p.all_negative_prompts]
                    else:
                        # もし p.all_negative_prompts がまだ初期化されていない場合（稀なケース）
                        # p.negative_prompt の値で初期化する
                        p.all_negative_prompts = [p.negative_prompt] * p.batch_size * p.n_iter

                if "width" in settings:
                    p.width = settings["width"]
                if "height" in settings:
                    p.height = settings["height"]

                # Hires. fixのパラメータも変更する場合
                if p.enable_hr:
                    if "hr_resize_x" in settings:
                        p.hr_resize_x = settings["hr_resize_x"]
                    if "hr_resize_y" in settings:
                        p.hr_resize_y = settings["hr_resize_y"]
                    if "hr_upscale_to_x" in settings:
                        p.hr_upscale_to_x = settings["hr_upscale_to_x"]
                    if "hr_upscale_to_y" in settings:
                        p.hr_upscale_to_y = settings["hr_upscale_to_y"]

                # 抽出した設定をプロンプトから削除
                p.prompt = re.sub(r'#(\{.*\})#', '', p.prompt).strip()

            except json.JSONDecodeError:
                print("Prompt Size Override: Invalid JSON in prompt settings.")
            except Exception as e:
                print(f"Prompt Size Override: An error occurred: {e}")
