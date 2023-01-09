from revChatGPT import __main__
import asyncio

bot = __main__.configure()


async def run():

    mesage = "Hello, how are you"

    ans = bot.get_responce_to_rasa(mesage)
    ans_aft = await ans
    print(ans_aft)


if __name__ == "__main__":
    asyncio.run(run())
