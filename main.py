import discord
from discord.ext import commands

TOKEN = ""
intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)
client.remove_command('help')

############ Config ###############

yetkiliID = 964405394552291356
botkanal = 964405396821409858
yes = "<a:yes:973246120094478417>"
no = "<a:red:973245670456688670>"

####################################

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Resul 😍"))
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content == f"<@{client.user.id}>":
        embed=discord.Embed(description=f"Prefixim \"**{client.command_prefix}**\" <@{message.author.id}>", color=0xff0000)
        await message.channel.send(embed=embed)
    await client.process_commands(message)

@client.command('rol')
async def role(ctx, user : discord.Member = None, *, role : discord.Role = None):
    if ctx.message.channel.id == botkanal:
        test = discord.utils.get(ctx.guild.roles, id=yetkiliID)
        if test in ctx.author.roles:
            if user != None:
                if role != None:
                    if role.position > ctx.author.top_role.position:
                        embed=discord.Embed(description=f"Bu Yetkiyi Veremezsin. <@{ctx.message.author.id}>", color=0xff0000)
                        await ctx.message.add_reaction(emoji=no)
                        return await ctx.send(embed=embed) 
                    if role in user.roles:
                        await user.remove_roles(role)
                        embed=discord.Embed(description=f"{user.mention} kişisinden <@&{role.id}> rolü alındı. <@{ctx.message.author.id}>", color=0xff0000)
                        await ctx.message.add_reaction(emoji=yes)
                        await ctx.send(embed=embed)
                    else:
                        await user.add_roles(role)
                        await ctx.message.add_reaction(emoji=yes)
                        embed=discord.Embed(description=f"{user.mention} kişisine <@&{role.id}> rolü verildi. <@{ctx.message.author.id}>", color=0xff0000)
                        await ctx.send(embed=embed)
                else:
                    embed=discord.Embed(description=f"Rol etiketlemen lazm. <@{ctx.message.author.id}>", color=0xff0000)
                    await ctx.message.add_reaction(emoji=no)
                    await ctx.send(embed=embed)
            else:
                embed=discord.Embed(description=f"Birisini etiketlemen gerekiyor. <@{ctx.message.author.id}>", color=0xff0000)
                await ctx.message.add_reaction(emoji=no)
                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description=f"Bu komutu kullana bilmek için <@&{test.id}> rolüne sahip olman gerekiyor. <@{ctx.message.author.id}>", color=0xff0000)
            await ctx.message.add_reaction(emoji=no)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(description=f"Bu komutu bu kanalda kullanamazsın. <@{ctx.message.author.id}>", color=0xff0000)
        await ctx.message.add_reaction(emoji=no)
        await ctx.send(embed=embed)

@client.command('ban')
@commands.has_any_role("Head Admin","Director", "Management", "Founder", "Co Founder", "Project Leader")
async def ban (ctx, member:discord.Member=None, *, reason =None):
    test = discord.utils.get(ctx.guild.roles, id=yetkiliID)
    if test in ctx.author.roles:
        if member != None:
            if member.top_role.position > ctx.author.top_role.position:
                embed=discord.Embed(description=f"Bu Kisiyi Banlamaya Yetkin Yok. <@{ctx.message.author.id}>", color=0xff0000)
                await ctx.message.add_reaction(emoji=no)
                return await ctx.send(embed=embed) 
            else:
                if member == None or member == ctx.message.author:
                    embed=discord.Embed(description=f"Kendini Banlaymazsın! <@{ctx.message.author.id}>", color=0xff0000)
                    await ctx.message.add_reaction(emoji=no)
                    await ctx.send(embed=embed)
                    return
                if reason == None:
                    reason = f"Sebep Yok. - {ctx.message.author}"
                embed1=discord.Embed(description=f"**{ctx.guild.name}** sunucusundan banlandın! Sebep: {reason}", color=0xff0000)
                await member.send(embed=embed1)
                await ctx.guild.ban(member, reason=reason)
                embed=discord.Embed(description=f"{member} kişisi <@{ctx.message.author.id}> tarafından banlandı! Sebep: {reason}", color=0xff0000)
                await ctx.message.add_reaction(emoji=yes)
                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description=f"Birisini etiketlemen gerekiyor. <@{ctx.message.author.id}>", color=0xff0000)
            await ctx.message.add_reaction(emoji=no)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(description=f"Bu komutu kullana bilmek için <@&{test.id}> rolüne sahip olman gerekiyor. <@{ctx.message.author.id}>", color=0xff0000)
        await ctx.message.add_reaction(emoji=no)
        await ctx.send(embed=embed)

@client.command('unban')
@commands.has_any_role("Head Admin","Director", "Management", "Founder", "Co Founder", "Project Leader")
async def ban (ctx, id : int=None):
    test = discord.utils.get(ctx.guild.roles, id=yetkiliID)
    if test in ctx.author.roles:
        if id != None:
            user = await client.fetch_user(id)
            try:
                await ctx.guild.unban(user)
            except Exception:
                embed=discord.Embed(description=f"{user} kişisinin banı yok. <@{ctx.message.author.id}>", color=0xff0000)
                await ctx.message.add_reaction(emoji=no)
                await ctx.send(embed=embed)
                return
            embed=discord.Embed(description=f"{user} kişisinin banı <@{ctx.message.author.id}> tarafından banı açıldı!", color=0xff0000)
            await ctx.message.add_reaction(emoji=yes)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description=f"Banlı Birisinin IDsini yazman gerekiyor. <@{ctx.message.author.id}>", color=0xff0000)
            await ctx.message.add_reaction(emoji=no)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(description=f"Bu komutu kullana bilmek için <@&{test.id}> rolüne sahip olman gerekiyor. <@{ctx.message.author.id}>", color=0xff0000)
        await ctx.message.add_reaction(emoji=no)
        await ctx.send(embed=embed)

@client.command(name='sil')
async def help(ctx, arg : int = 10):
    test = discord.utils.get(ctx.guild.roles, id=yetkiliID)
    if test in ctx.author.roles:
        await ctx.channel.purge(limit=arg)     
        embed=discord.Embed(description=f"**{arg}** mesaj silindi. <@{ctx.message.author.id}>", color=0xff0000)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(description=f"Bu komutu kullana bilmek için <@&{test.id}> rolüne sahip olman gerekiyor. <@{ctx.message.author.id}>", color=0xff0000)
        await ctx.message.add_reaction(emoji=no)
        await ctx.send(embed=embed)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingAnyRole):
        em = discord.Embed(description=f"Yetkin Yok! <@{ctx.message.author.id}>", color=discord.Colour.random())
        await ctx.send(embed=em)
        await ctx.message.add_reaction(emoji=no)
    elif isinstance(error, discord.ext.commands.errors.MemberNotFound):
        em = discord.Embed(description=f"Kullanıcı Bulunamadı! <@{ctx.message.author.id}>", color=discord.Colour.random())
        await ctx.send(embed=em)
        await ctx.message.add_reaction(emoji=no)


client.run(TOKEN)
