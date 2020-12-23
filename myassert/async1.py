import asyncio


async def hello():
    print("hello")
    await asyncio.sleep(1)
    print("world")


if __name__ == "__main__":
    asyncio.run(hello())
