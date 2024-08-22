from langchain.callbacks.base import BaseCallbackHandler
from pyboxen import boxen


def boxen_print(*args, **kwargs):
    print(boxen(*args, **kwargs))


def get_messege_color(message_type):
    if message_type == 'system':
        return "yellow"
    if message_type == "human":
        return "green"

    if message_type == "ai":
        return "blue"

    if message_type == "ai_function_call":
        return "cyan"

    if message_type == "function":
        return "purple"

    return "white"


class ChatModelStartHandler(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
        print("\n\n\n\n=========== Sending Messages ===========\n\n")

        for message in messages[0]:

            message_type = message.type
            content = message.content

            if "function_call" in message.additional_kwargs:
                message_type = message_type + "_function_call"
                call = message.additional_kwargs["function_call"]
                content = f"Running tool {call['name']} "
                content = content + f"with args {call['arguments']}"

            color = get_messege_color(message_type=message_type)

            boxen_print(content, title=message.type, color=color)
