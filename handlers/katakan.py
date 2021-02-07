from aiogram import types, md


async def katakansebenarnya(message: types.Message):
    await message.reply(md.text(
        md.bold('Salam Kenal dari AeroBot 🤖\n\n'),
        md.text('AeroBot dikembangkan untuk membantu kebutuhan dasar dalam chat Telegram BBTA3 🛰\n\n',),
        md.text('Memang saat ini fungsi AeroBot masih sedikit dan berharap pengembang dengan ikhlas meluangkan '
                'waktunya yang berharga untuk meningkatkan fungsi AeroBot 🤲🏽')
    ))


async def siapapembuat(message: types.Message):
    await message.reply(md.text(
        md.text('Baik, Baik, AeroBot dibuat oleh perekayas yang bermarkas di'), md.bold('AEROTRONIKA\n\n'),
        md.text('Untuk selangkapnya dapat melirik'),
        md.italic('Source Code'),
        md.link('AeroBot', 'https://github.com/bbta3-bppt/aerobot')
    ))
