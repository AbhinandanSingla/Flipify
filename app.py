import chainlit as cl
from chainlit import make_async
from chainlit.input_widget import Slider, Select, Switch

from model import agent_executor


@cl.author_rename
def rename(orig_author: str):
    rename_dict = {"LLMChain": "Albert Einstein", "Chatbot": "Flipify"}
    return rename_dict.get(orig_author, orig_author)


def my_sync_function(message):
    res = agent_executor.run(message)
    return res


@cl.on_chat_start
async def start():
    content = "Hii, I am Flipify. Your personal AI"
    infos = cl.user_session.get("user_infos")
    await cl.Avatar(
        name="Deepu Singla",
        url="https://cdn-icons-png.flaticon.com/512/9313/9313209.png",
        content="Deepu Singla"
    ).send()
    await cl.Avatar(
        name="Flipify",
        url="https://logos-world.net/wp-content/uploads/2020/11/Flipkart-Emblem.png",
    ).send()
    settings = await cl.ChatSettings(
        [
            Select(
                id="Model",
                label="OpenAI - Model",
                values=["gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-4", "gpt-4-32k"],
                initial_index=0,
            ),
            Switch(id="Streaming", label="OpenAI - Stream Tokens", initial=True),
            Slider(
                id="Temperature",
                label="OpenAI - Temperature",
                initial=1,
                min=0,
                max=2,
                step=0.1,
            ),
            Slider(
                id="SAI_Steps",
                label="Stability AI - Steps",
                initial=30,
                min=10,
                max=150,
                step=1,
                description="Amount of inference steps performed on image generation.",
            ),
            Slider(
                id="SAI_Cfg_Scale",
                label="Stability AI - Cfg_Scale",
                initial=7,
                min=1,
                max=35,
                step=0.1,
                description="Influences how strongly your generation is guided to match your prompt.",
            ),
            Slider(
                id="SAI_Width",
                label="Stability AI - Image Width",
                initial=512,
                min=256,
                max=2048,
                step=64,
                tooltip="Measured in pixels",
            ),
            Slider(
                id="SAI_Height",
                label="Stability AI - Image Height",
                initial=512,
                min=256,
                max=2048,
                step=64,
                tooltip="Measured in pixels",
            ),
        ]
    ).send()

    # #
    # await cl.Message(
    #     content=content,
    # ).send()


@cl.on_settings_update
async def setup_agent(settings):
    print("on_settings_update", settings)


@cl.on_message
async def main(message: str):
    async_function = make_async(my_sync_function)
    result = await async_function(message)
    print(result)
    await cl.Message(content=result).send()
