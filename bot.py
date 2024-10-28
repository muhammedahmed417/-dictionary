import discord
import random
import asyncio


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$guess'):
            await message.channel.send('Merhaba! Lütfen 1 ile 10 arasinda rakam giriniz')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Özür dileriz! Fakat cevabinizin gelmesi cok uzun sürdü ütfen yeniden deneyin{answer}.')

            if int(guess.content) == answer:
                await message.channel.send('Aferin! Dogru bildin ')
            else:
                await message.channel.send(f'Oops. Cevap bu degil lütfen yeniden deneyin bu arada cevap {answer}du.')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('')

