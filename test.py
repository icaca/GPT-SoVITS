import gradio as gr
import time

with gr.Blocks(title="GPT-SoVITS WebUI", analytics_enabled=False) as app:
    gr.Markdown(
        value=
        "本软件以MIT协议开源, 作者不对软件具备任何控制力, 使用软件者、传播软件导出的声音者自负全责. <br>如不认可该条款, 则不能使用或引用软件包内任何代码和文件. 详见根目录<b>LICENSE</b>."
    )

a, b, c = app.queue().launch(
    server_name="0.0.0.0",
    inbrowser=True,
    share=True,
    server_port=5001,
    prevent_thread_lock=True,
    # analytics_enabled=True,
    # max_threads=1,
    # concurrency_count=1,
    quiet=False,
)
print("准备请求远程地址")
print(a, b, c)
while True:
    time.sleep(0.1)
