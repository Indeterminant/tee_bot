import discord
from discord.ext import commands
import asyncio
import random
import math
from discord.utils import get

bot = commands.Bot(command_prefix='t_', case_insensitive=True)

bot.remove_command('help')

TOKEN = 'NzAzNDMyMDE5NTIyMjI0MTY5.Xs3DfQ.a_0AdPf1-tiupw2A5vC-zMJ6AXc'

helpinfo = """```Prefix: t_```
 My commands are `case insensitive`, and they also work in DMs.
 
 **💻 Commands:**
 > `help`
 > `hello`
 > `4minos`
 > `5minos`
 > `ppt 5minos`
 > `SRS`
 > `lookup`

 **🔍 t_lookup openers/setups:**
 > `perfect clear`
 > `DT cannon`
 > `TKI`
 > `albatross`
 > `pelican`
 > *more openers planned..*

 **🛠️ Utility/Misc:**
 > `math` or `calc` (basic operators, trigonometry, etc.)
 > `hex`
 > `RGB` (planned)
 > `invite`

 **📓 List commands: [to be restored]**
 > `references`
 > `terms`
 > `tools`
 > `customize`
 > `credits` or `citations`
 > `music` (planned)

 **👾 Fun commands:**
 > `tothestars`
 > `spin`
 > `F`
 > `unimpressed`
 > `say`
 > *easter egg autoreplies...*
 
 **📌 Planned/in development:**
 `remindme`
 `lookup` (refactored code)
 `boxes`
 `ping`
 `joke`
 `dictionary` (japanese terms)
 
 *Disclaimer: Note that the information in the list commands are not supposed to be exhaustive. They merely function as a quick compilation for convenience.*
 """

calcHELPfield1 = """
 > Addition: `t_add`
 > Subtraction: `t_sub`
 > Multiplication: `t_mul`
 > Division: `t_div`
 > Exponent/root: `t_exp`
 > Modulus: `t_mod`"""

calcHELPfield2 = """
 > Sine: `t_sin`
 > Cosine: `t_cos`
 > Tangent: `t_tan`
 > Cotangent: `t_cot`
 > Secant:`t_sec`
 > Cosecant: `t_csc`"""
 
calcHELPfield3 = """
 > Permutation: `t_permu`
 > Combination: `t_combi`
 > Factorial: `t_factorial`
 > Degrees to **Radians**: `t_rad`
 > Radians to **Degrees**: `t_deg`"""
 
calcHELP = """
 `t_add 1 1`
 `t_exp 4 0.5`
 `t_sin 30`
 `t_tan 45`
 
 For now, I can only work with two numbers for the basic arithmetic operations per command.
 The default input units for the trigonometry operations are **degrees.**
  
 **Warning: Please don't give me ridiculously large numbers to work with, especially for the exponent command. I have once passed out because Kiede told me to calculate 26178238173721 to the power of 1287361873452378487234. She needs to understand that I am not a graphing calculator, and I doubt that even a quantum computer can handle that.**
 """

reference = """This list will be frequently updated.

 **T-spin tutorials:**
 https://www.youtube.com/watch?v=FI39WJqTLvA&t=5s (T-spin guide)
 https://www.youtube.com/watch?v=yqyulht3wfM (T-spin guide)
 https://www.youtube.com/watch?v=Rvtc9rww-7c (T-spin guide)
 https://www.youtube.com/watch?v=YzrvmlZRuzI (T-spin openers)
 https://tetris.wiki/T-Spin_Guide (T-spin setups)
 https://www.youtube.com/watch?v=LRs9Lny_J7E&t=147s (T-spin Triples)
 
 **Perfect Clear tutorials:**
 https://www.youtube.com/watch?v=CFvQCo4veSA
 https://www.youtube.com/watch?v=SB2zUUQx7A0
 https://www.youtube.com/watch?v=XHwQ742aSeI

 **Combo tutorials:**
 https://www.youtube.com/watch?v=HBVuKR1MgFE (4wide)
 https://www.youtube.com/watch?v=CbMU5WkIhFg&t=685s (2wide, 3wide, 4wide)

 **Other spin tutorials:**
 https://www.youtube.com/watch?v=bIBgNrrbaS4 (Chopin's Spin Guide)
 https://www.youtube.com/watch?v=Ry8NJXrHjlU&t=1117s (All-Spin)
 https://www.youtube.com/watch?v=gDPD8gLg8fw&t=1s (PPT Big Bang)

 **Helpful articles:**
 https://steamcommunity.com/sharedfiles/filedetails/?id=1318514920 (Guide to Advanced Tetris)
 https://harddrop.com/wiki/Opener (Openers)
 https://harddrop.com/wiki/Pentomino (Pentominos)
 """

terms = """This list of terms will be updated.

 APM - Attack Per Minute
 PPS -  Pieces Per Second
 DAS - Delayed Auto Shift
 ARR - Auto Repeat Rate 
 TSS - T-spin Single
 TSD - T-spin Double
 TST - T-spin Triple
 B2B - Back-to-Back
 SRS - Super/Standard Rotation System
 """

tools = """This list of tools will be updated.
 
 **Solution Finders/Analyzers**
 https://github.com/knewjade/solution-finder (Perfect Clear/T-spins/Combo Finders)
 https://harddrop.com/forums/index.php?showtopic=7588 (Perfect Clear solution finder)

 **Training:**
 https://tetresse.harddrop.com (Finesse)
 https://four.lol/mid-game/finesse/#content (article for referencing finesse rules)
 https://harddrop.com/fumen/ (Custom maps and piece sequences)
 https://harddrop.com/forums/index.php?showtopic=4469 (Fumen tool help guide)
 https://harddrop.com/forums/index.php?showtopic=5292 (MisaMino, T-spin AI)
 https://jstris.jezevec10.com (Cheese Race/downstacking, Survival, Multiplayer, etc.)
 https://tetralegends.app (Combo Challenge, Survival, etc.)
 https://tetr.io (Multiplayer, custom game modes, etc.)
 https://asc.winternebs.com (Custom pieces and rotation systems, multiplayer, etc.)

 **Misc. tools... Why not?**
 https://123apps.com (File converter with no file size limit :D)
 https://htmlcolorcodes.com (Generating colors from hex code and RGB online)
 """

citations = """Credits to the websites below for information on openers, setups, and terminology.

 **Hard Drop Wiki**
 https://harddrop.com/wiki/Tetris_Wiki
 
 **Four**
 https://harddrop.com/wiki/Tetris_Wiki

 **atwiki.jp**
 https://w.atwiki.jp/tetrismaps/
 """

custom = """This list of resources will be updated.
 
 **Jstris:**
 https://docs.google.com/spreadsheets/d/1xO8DTORacMmSJAQicpJscob7WUkOVuaNH0wzkR_X194/htmlview# (Jstris Customization Database, includes skins, themes, backgrounds, etc.)
 https://chrome.google.com/webstore/detail/jstris-companion/hcfobmlocggcombmbgpncmbknnggjlkf?hl=en (Jstris Companion extension for Google Chrome)
 https://addons.mozilla.org/en-US/firefox/addon/jstris-companion/ (Jstris Companion extension for Firefox)
 https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=en (TamperMonkey extension for Google Chrome, used for Jstris theme scripts)
 
 **Tetr.io:**
 https://addons.mozilla.org/en-CA/firefox/addon/tetrio-plus/?src=search (Tetr.io+ extension for Firefox)
 """

advice = """We hope that this advice can help at least one person and make a positive difference in their lives.
 
 **1. Take care of your phycical health.**
 You cannot work if you do not have the best health. 
 If you're feeling exhsausted and rusty from quarantine, take a 5 to 10-minute walk outside and catch some fresh air and sunlight. And don't forget to wear a mask.
 If you are unable to go outside or prefer not to, you can exercise at home. Remember to get up and stretch every 30 minutes to 1 hour, and take a walk to the patio.
 Don't forget to stay hydrated and eat your meals, but don't beat yourself if you skipped a meal. It's normal to have a small appetite if you are exhausted.
 """

tetriminos = "<:t_mino:720464385663041617> <:o_mino:720464422765723658> <:i_mino:720464385881145404> <:j_mino:720464385893597185> <:l_mino:720464386095054898> <:s_mino:720464438888497172> <:z_mino:720464385897660476>"

tetriminosdesc = """```These are all of the tetriminos, as their colors are according to the Tetris Guideline.```"""

pentominos1 = "<:0a_5mino:721173360226205796> <:0b_5mino:721173360100507699> <:0c_5mino:721173360306028594> <:0d_5mino:721173360327000094> <:0e_5mino:721173360331194439><:0f_5mino:721173360284794920>"

pentominos2 = "<:1a_5mino:721173360368681031> <:1b_5mino:721173360306028664> <:2a_5mino:721173360322674778> <:2b_5mino:721173360167485471> <:3a_5mino:721173360033398826> <:3b_5mino:721173360347709450>"

pentominos3 = "<:4a_5mino:721173360377200640> <:4b_5mino:721173360280600625> <:5a_5mino:721173360297640017> <:5b_5mino:721173360289120307> <:6a_5mino:721173360372875324> <:6b_5mino:721173359962095638>"

pentominosdesc = """```These are all of the pentomino combinations, including their reflections.
 Note that there are no standard colors nor rotation systems for pentominos.```
 """

pptpentominos = "<:t_5mino_ppt:720789886575181854> <:o_5mino_ppt:720789886130585671> <:i_5mino_ppt:720789886579245126> <:j_5mino_ppt:720789886268866682> <:l_5mino_ppt:720789886575050966> <:s_5mino_ppt:720789886545952788> <:z_5mino_ppt:720789886763794492>"

pptpentominosdesc = """```These are the pentominos that appear in Party Mode from Puyo Puyo Tetris. Each tetrimino is transformed into a pentomino.
 The colors and the rotations that appear in these emotes reference how they appear in-game.
 Note that these are not all of the pentomino formations.```
 """

plans = """The openers/strategies that Kiede plans to learn. Kiede, please stop procrastinating.
 https://harddrop.com/wiki/Imperial_cross
 https://harddrop.com/wiki/C-Spin
 https://harddrop.com/wiki/BT_Cannon
 https://harddrop.com/wiki/MKO_Stacking
 https://harddrop.com/wiki/Hachispin
 https://four.lol/openers/mr-tspin
 https://four.lol/perfect-clears/grace-system
 """


#DEBUGNOTE: DO NOT MAKE MESSAGES CAPITAL!!

###=================TEEBOT'S OLD CODE======================###

@bot.event
async def on_message(message):
 #message.content = message.content.lower()
 if message.author == bot.user:
  return
#AUTOREPLIES
#disable autoreply
 #if message.content.startswith('t_toggle autoreply') and autoreply == True:
  #autoreply = not autoreply
  #msg = 'Hello {0.author.mention}'.format(message)
  #await message.channel.send('```Autoreplies have been enabled.```')
 #if autoreply == False:
  #msg = 'Hello {0.author.mention}'.format(message)
  #await message.channel.send('```Autoreplies have been disabled.')
#aaaaaaa
 if message.content.startswith('aaa'):#and autoreply == True:
  msg = 'Hello {0.author.mention}'.format(message)
  await message.channel.send('End my suffering...')
#4wide
 if (message.content.startswith('t_4wide?') or message.content.startswith('t_fourwide?')):# and autoreply == True:
  msg = 'Hello {0.author.mention}'.format(message)
  await message.channel.send("No. It's time to stop. Please take a moment to reflect on your morality as to why you have came to the decision to fourwide.")
#no
 if (message.content.startswith('no ') or message.content.startswith('no.')) and message.author.id != 415159851837161472:
  await message.channel.send("It's time to stop.")
  if "decapitate" and "no." in message.content and message.author.id == 415159851837161472: 
    await message.channel.send("Haha No.")
#not now Tee
 if message.content.startswith('not now tee'):# and autoreply == True:
  msg = 'Hello {0.author.mention}'.format(message)
  await message.channel.send("NO YOU!!!")
#BASIC COMMANDS
#t_kiede's plans
 if message.content.startswith("t_kiede's plans"):
  plansE = discord.Embed(title="Kiede's Plans",description=plans,color=int('66CCFF',16))
  plansE.set_thumbnail(url="https://cdn.discordapp.com/attachments/720463647654019127/721583168347701248/steeckerrr.png")
  plansE.set_footer(text="Kiede was here")
  await message.channel.send(embed=plansE)
#MEME COMMANDS HAHAHA
#contains "bad spin"
 if "bad spin" in message.content:
  msg = 'Hello {0.author.mention}'.format(message)
  await message.channel.send(":(")
#contains "tee"
 #if "tee" in message.content:
  #msg = 'Hello {0.author.mention}'.format(message)
  #await message.channel.send("You called?")
#f
 if message.content.startswith('t_f'):
  msg = 'Hello {0.author.mention}'.format(message)
  await message.channel.send(":regional_indicator_f:")
#roll
 if message.content.startswith('roll'):
  msg = 'Hello {0.author.mention}'.format(message)
  await message.channel.send('My advice is no. Please save your stones, because I know that gacha is a scam.')
#[BASIC TEXT COMMANDS]
#LIST COMMANDS
#reference
 if message.content.startswith('t_reference'):
  referenceE = discord.Embed(title='Helpful video tutorials and articles',description=reference,color=int('D303Fc',16))
  referenceE.set_thumbnail(url="https://cdn.discordapp.com/attachments/720463647654019127/721587339826036806/steecker_2.png")
  await message.channel.send(embed=referenceE)
#terms
 if message.content.startswith('t_terms'):
  termsE = discord.Embed(title='Common Abbreviations',description=terms,color=int('D303FC',16))
  await message.channel.send(embed=termsE)
#tools
 if message.content.startswith('t_tools'):
  toolsE = discord.Embed(title='Tools to use for practicing',description=tools,color=int('D303FC',16))
  await message.channel.send(embed=toolsE)
#customize
 if message.content.startswith('t_customize'):
  customE = discord.Embed(title='Resources for customizing your tetr.io or Jstris bot',description=custom,color=int('D303FC',16))
  await message.channel.send(embed=customE)
#citations or credits
 if message.content.startswith('t_citations') or message.content.startswith('t_credits'):
  citationsE = discord.Embed(title='Referenced Sources',description=citations,color=int('D303FC',16))
  citationsE.set_thumbnail(url="https://cdn.discordapp.com/attachments/720463647654019127/721587339826036806/steecker_2.png")
  await message.channel.send(embed=citationsE)
#advice
 if message.content.startswith('t_advice'):
  adviceE = discord.Embed(title='Some life advice from Tee and the Kiedev',description=advice,color=int('24BAFF',16))
  adviceE.set_thumbnail(url="https://cdn.discordapp.com/attachments/720463647654019127/721587339826036806/steecker_2.png")
  await message.channel.send(embed=adviceE)
#4minos
 if message.content.startswith('t_4minos'):
  msg = 'Hello {0.author.mention}'.format(message)
  await message.channel.send(tetriminos)
  await message.channel.send(tetriminosdesc)
  await message.add_reaction("<:t_mino:720464385663041617>")
  await message.add_reaction("<:o_mino:720464422765723658>")
  await message.add_reaction("<:i_mino:720464385881145404>")
  await message.add_reaction("<:j_mino:720464385893597185>")
  await message.add_reaction("<:l_mino:720464386095054898>")
  await message.add_reaction("<:s_mino:720464438888497172>")
  await message.add_reaction("<:z_mino:720464385897660476>")
#5minos
 if message.content.startswith('t_5minos'):
  msg = 'Hello {0.author.mention}'.format(message)
  await message.channel.send(pentominos1)
  await message.channel.send(pentominos2)
  await message.channel.send(pentominos3)
  await message.channel.send(pentominosdesc)
#ppt 5minos
 if message.content.startswith('t_ppt 5minos'):
  msg = 'Hello {0.author.mention}'.format(message)
  await message.channel.send(pptpentominos)
  await message.channel.send(pptpentominosdesc)
  await message.add_reaction("<:t_5mino_ppt:720789886575181854>")
  await message.add_reaction("<:o_5mino_ppt:720789886130585671>")
  await message.add_reaction("<:i_5mino_ppt:720789886579245126>")
  await message.add_reaction("<:j_5mino_ppt:720789886268866682>")
  await message.add_reaction("<:l_5mino_ppt:720789886575050966>")
  await message.add_reaction("<:s_5mino_ppt:720789886545952788>")
  await message.add_reaction("<:z_5mino_ppt:720789886763794492>")
#[image commands/misc]
#srs
 if message.content.startswith('t_srs'):
  srsE = discord.Embed()
  srsE.set_image(url="https://cdn.discordapp.com/attachments/715061925406572606/720085751412424744/SRS.png")
  await message.channel.send(embed=srsE)
#tothestars
 if message.content.startswith('t_tothestars'):
  tothestarsE = discord.Embed(color=int('FF00FF',16))
  tothestarsE.set_image(url="https://cdn.discordapp.com/attachments/715061925406572606/718600013755842601/tothestars.png")
  await message.channel.send(embed=tothestarsE)
#ineverbackdown
 if message.content.startswith('t_ineverbackdown'):
  ineverbackdownE = discord.Embed(color=int('FF00FF',16))
  ineverbackdownE.set_image(url="https://cdn.discordapp.com/attachments/720463647654019127/735220816286974072/i_never_back_down.png")
  await message.channel.send(embed=ineverbackdownE)
#galatea
 if message.content.startswith('acheo this is for you') or message.content.startswith('this is for you acheo'):
  galatea = discord.Embed()
  galatea.set_image(url="https://cdn.discordapp.com/attachments/715057463933534323/723058443623202926/galatea.png")
  await message.channel.send(embed=galatea)
#patri
 if message.content.startswith('pi this is for you') or message.content.startswith('this is for you pi'):
  patri = discord.Embed()
  patri.set_image(url=" https://puyonexus.com/mediawiki/images/9/9e/Img202704_l.png")
  await message.channel.send(embed=patri)
#unimpressed
 if message.content.startswith('t_unimpressed'):
  unimpressedE = discord.Embed()
  unimpressedE.set_image(url="https://cdn.discordapp.com/attachments/720463647654019127/720505034307010660/716901248565248001.png")
  await message.channel.send(embed=unimpressedE)
#spin
 if message.content.startswith('t_spin'):
  spinGIF = discord.Embed(color=int('FF00FF',16))
  spinGIF.set_image(url="https://media.discordapp.net/attachments/703430258699010108/719987301807292527/spin.gif")
  await message.channel.send(embed=spinGIF)
#[LOOKUP COMMANDS]
#lookup albatross
 if message.content.startswith('t_lookup albatross'):
  albatross1E = discord.Embed(title='Albatross',color=int('FF00FF',16))
  albatross1E.set_image(url="https://cdn.discordapp.com/attachments/720463647654019127/723256681219227678/albatross1.png")
  albatrossMSG = albatross1E
  albatross2E = discord.Embed(color=int('FF00FF',16))
  albatross2E.set_image(url="https://cdn.discordapp.com/attachments/720463647654019127/723256483902652427/albatross2.png")
  await message.channel.send(embed=albatross1E)
  #await albatrossMSG.add_reaction("1️⃣")
#lookup pelican
 if message.content.startswith('t_lookup pelican'):
  pelican1E = discord.Embed(title='Pelican',color=int('FF00FF',16))
  pelican1E.set_image(url="https://cdn.discordapp.com/attachments/720463647654019127/723253126479610026/pelican1.png")
  pelican2E = discord.Embed(color=int('FF00FF',16))
  pelican2E.set_image(url="https://cdn.discordapp.com/attachments/720463647654019127/723253128891203614/pelican2.png")
  await message.channel.send(embed=pelican1E)
  await message.channel.send(embed=pelican2E)
#lookup perfect clear
 if message.content.startswith('t_lookup perfect clear'):
  perfectclearE = discord.Embed(title='Perfect Clear',color=int('FFFF00',16))
  perfectclearE.set_image(url="https://cdn.discordapp.com/attachments/715061925406572606/718835139853156362/pc.png")
  await message.channel.send(embed=perfectclearE)
#lookup dt cannon
 if message.content.startswith('t_lookup dt cannon'):
  dt1E = discord.Embed(title='DT Cannon',color=int('FF00FF',16))
  dt1E.set_image(url="https://cdn.discordapp.com/attachments/720463647654019127/723251871942443008/DT1.png")
  dt2E = discord.Embed(color=int('FF00FF',16))
  dt2E.set_image(url="https://cdn.discordapp.com/attachments/720463647654019127/723251868100460614/DT2.png")
  await message.channel.send(embed=dt1E)
  await message.channel.send(embed=dt2E)
#lookup bt cannon
 if message.content.startswith('t_lookup bt cannon'):
  bt1E = discord.Embed(title='BT Cannon',color=int('FF00FF',16))
  bt1E.set_image(url="https://cdn.discordapp.com/attachments/720463647654019127/723251871942443008/DT1.png")
  bt2E = discord.Embed(color=int('FF00FF',16))
  bt2E.set_image(url="https://cdn.discordapp.com/attachments/720463647654019127/723251868100460614/DT2.png")
  await message.channel.send(embed=bt1E)
  await message.channel.send(embed=bt2E)
#lookup TKI
 elif message.content.startswith('t_lookup tki'):
  tkiE = discord.Embed(title='TKI',color=int('FF00FF',16))
  tkiE.set_image(url="https://cdn.discordapp.com/attachments/715061925406572606/720078756978622524/TKI.png")
  await message.channel.send(embed=tkiE)
 await bot.process_commands(message)


###===========[BASIC COMMANDS]==============###
#hello
@bot.command()
async def hello(ctx):
  await ctx.send('Hello! I am Tee, the Tetris King and captain of the Starship Tetra.')

@bot.command(aliases=["info"])
#t_help
async def help(ctx):
  helpE = discord.Embed(title='Help',description=helpinfo,color=int('FF00FF',16))
  helpE.set_thumbnail(url="https://cdn.discordapp.com/attachments/720463647654019127/721583168347701248/steeckerrr.png")
  helpE.set_footer(text="Created by Indeterminant/Kiede.")
  await ctx.send(embed=helpE)

#t_hug
@bot.command()
async def hug(ctx):
  if ctx.author.id == 328255863473307648:
    await ctx.send("Heey..! Kiede... !! *hugs* <:teebloosh:717110673653497929>")
  else:
    await ctx.send("*Hugs you*")

#t_hold
@bot.command()
async def hold(ctx, tee: str):
 if tee == '<@!703432019522224169>':
  await ctx.send("*Holds you*")

#GREETING NEW MEMBER
#@bot.event
#async def on_member_join(member):
    #channel = get(member.guild.channels, name="general")
    #await bot.send_message(channel,f"""{member.mention} Welcome to K-FC.""") 

###===========[UTILITY COMMANDS]==============###

#idea: refactor embed color hex code with variables...if possible :D

#t_calc. math commands help.
@bot.command(aliases=["math"])
async def calc(ctx):
  calcE = discord.Embed(title='🔢 Help for the calculator commands.', color=int('819BF5',16))
  calcE.add_field(name = 'Arithmetics', value = calcHELPfield1, inline=True)
  calcE.add_field(name = 'Trigonometry', value = calcHELPfield2, inline=True)
  calcE.add_field(name = 'Misc.', value = calcHELPfield3, inline=False)
  calcE.add_field(name = 'Examples:', value = calcHELP, inline=False)
  calcE.set_thumbnail(url="https://cdn.discordapp.com/attachments/720463647654019127/721583168347701248/steeckerrr.png")
  await ctx.send(embed=calcE)

#t_add. addition.
@bot.command()
async def add(ctx, left: float, right: float):
  addEXP = f"{left}" + " + " + f"{right}"
  addOUTPUT = left + right
  addRESULTS = f"""**Expression: **```{addEXP}```
  **Output:** ```{addOUTPUT}```"""
  addE = discord.Embed(title='📐 Calculation results',description=addRESULTS,color=int('819BF5',16))
  await ctx.send(embed = addE)

#t_sub. subtraction.
@bot.command()
async def sub(ctx, left: float, right: float):
  subEXP = f"{left}" + " - " + f"{right}"
  subOUTPUT = left - right
  subRESULTS = f"""**Expression: **```{subEXP}```
  **Output:** ```{subOUTPUT}```"""
  subE = discord.Embed(title='📐 Calculation results',description=subRESULTS,color=int('819BF5',16))
  await ctx.send(embed = subE)

#t_mul. multiplication.
@bot.command()
async def mul(ctx, left: float, right: float):
  mulEXP = f"{left}" + " × " + f"{right}"
  mulOUTPUT = left * right
  mulRESULTS = f"""**Expression: **```{mulEXP}```
  **Output:** ```{mulOUTPUT}```"""
  mulE = discord.Embed(title='📐 Calculation results',description=mulRESULTS,color=int('819BF5',16))
  await ctx.send(embed = mulE)

#t_div. division.
@bot.command()
async def div(ctx, left: float, right: float):
  divEXP = f"{left}" + " ÷ " + f"{right}"
  divOUTPUT = left / right
  if right == 0:
   divOUTPUT = """haha no         *tposes*"""
  divRESULTS = f"""**Expression: **```{divEXP}```
  **Output:** ```{divOUTPUT}```"""
  divE = discord.Embed(title='📐 Calculation results',description=divRESULTS,color=int('819BF5',16))
  await ctx.send(embed = divE)

#t_exp. exponents. might want to work on this more about roots and exponents.
@bot.command()
async def exp(ctx, left: float, right: float):
  expEXP = f"{left}" + " ^ " + f"{right}"
  expOUTPUT = left ** right
  expRESULTS = f"""**Expression: **```{expEXP}```
  **Output:** ```{expOUTPUT}```"""
  expE = discord.Embed(title='📐 Calculation results',description=expRESULTS,color=int('819BF5',16))
  await ctx.send(embed = expE)

#t_mod. modulus.
@bot.command()
async def mod(ctx, left: float, right: float):
  modEXP = f"{left}" + " mod " + f"{right}"
  modOUTPUT = left % right
  modRESULTS = f"""**Expression: **```{modEXP}```
  **Output:** ```{modOUTPUT}```"""
  modE = discord.Embed(title='📐 Calculation results',description=modRESULTS,color=int('819BF5',16))
  await ctx.send(embed = modE)

###TRIG COMMANDS
#t_sin
@bot.command()
async def sin(ctx, x: float):
  sinEXP_deg = f"sin({x})"
  sinEXP_rad = f"sin({math.radians(x)})"
  sinOUTPUT = math.sin(math.radians(x))
  sinOUTPUT_rounded = round(sinOUTPUT, 7)
  sinRESULTS = f"""**Expression: **```{sinEXP_deg} in degrees```
  ```{sinEXP_rad} in radians```
  **Output:** ```{sinOUTPUT_rounded}```"""
  sinE = discord.Embed(title='📐 Calculation results',description=sinRESULTS,color=int('819BF5',16))
  await ctx.send(embed = sinE)

#t_cos
@bot.command()
async def cos(ctx, x: float):
  cosEXP_deg = f"cos({x})"
  cosEXP_rad = f"cos({math.radians(x)})"
  cosOUTPUT = math.cos(math.radians(x))
  cosOUTPUT_rounded = round(cosOUTPUT, 7)
  cosRESULTS = f"""**Expression: **```{cosEXP_deg} in degrees```
  ```{cosEXP_rad} in radians```
  **Output:** ```{cosOUTPUT_rounded}```"""
  cosE = discord.Embed(title='📐 Calculation results',description=cosRESULTS,color=int('819BF5',16))
  await ctx.send(embed = cosE)

#t_tan
@bot.command()
async def tan(ctx, x: float):
  tanEXP_deg = f"tan({x})"
  tanEXP_rad = f"tan({math.radians(x)})"
  tanOUTPUT = math.tan(math.radians(x))
  tanOUTPUT_rounded = round(tanOUTPUT, 7)
  tanRESULTS = f"""**Expression: **```{tanEXP_deg} in degrees```
  ```{tanEXP_rad} in radians```
  **Output:** ```{tanOUTPUT_rounded}```"""
  tanE = discord.Embed(title='📐 Calculation results',description=tanRESULTS,color=int('819BF5',16))
  await ctx.send(embed = tanE)

#t_cot
@bot.command()
async def cot(ctx, x: float):
  cotEXP_deg = f"cot({x})"
  cotEXP_rad = f"cot({math.radians(x)})"
  cotOUTPUT = 1 / math.tan(math.radians(x))
  cotOUTPUT_rounded = round(cotOUTPUT, 7)
  cotRESULTS = f"""**Expression: **```{cotEXP_deg} in degrees```
  ```{cotEXP_rad} in radians```
  **Output:** ```{cotOUTPUT_rounded}```"""
  cotE = discord.Embed(title='📐 Calculation results',description=cotRESULTS,color=int('819BF5',16))
  await ctx.send(embed = cotE)

#t_sec
@bot.command()
async def sec(ctx, x: float):
  secEXP_deg = f"sec({x})"
  secEXP_rad = f"sec({math.radians(x)})"
  secOUTPUT = 1 / math.cos(math.radians(x))
  secOUTPUT_rounded = round(secOUTPUT, 7)
  secRESULTS = f"""**Expression: **```{secEXP_deg} in degrees```
  ```{secEXP_rad} in radians```
  **Output:** ```{secOUTPUT_rounded}```"""
  secE = discord.Embed(title='📐 Calculation results',description=secRESULTS,color=int('819BF5',16))
  await ctx.send(embed = secE)

#t_csc
@bot.command()
async def csc(ctx, x: float):
  cscEXP_deg = f"csc({x})"
  cscEXP_rad = f"csc({math.radians(x)})"
  cscOUTPUT = 1 / math.sin(math.radians(x))
  cscOUTPUT_rounded = round(cscOUTPUT, 7)
  cscRESULTS = f"""**Expression: **```{cscEXP_deg} in degrees```
  ```{cscEXP_rad} in radians```
  **Output:** ```{cscOUTPUT_rounded}```"""
  cscE = discord.Embed(title='📐 Calculation results',description=cscRESULTS,color=int('819BF5',16))
  await ctx.send(embed = cscE)

#t_hex
@bot.command()
async def hex(ctx, hexcode: str):
  hexDESC = f"""HEX code: {hexcode}"""
  hexE = discord.Embed(title='Results',description=hexDESC,color=int(f'{hexcode}',16))
  hexE.set_footer(text="Color generated from hex code. Visit https://htmlcolorcodes.com for more utilities and fun information.")
  await ctx.send(embed=hexE)

#t_rgb
#@bot.command()
#async def rgb(ctx, r: int, g: int, b: int):
  #r_hex = hex(r)
  #g_hex = hex(g)
  #b_hex = hex(b)
  #RGBtoHEX = f"{r_hex}" + f"{g_hex}" + f"{b_hex}"
  #RGBdesc = f"""R: {r}
  #G: {g}
  #B: {b}
  #HEX code: {RGBtoHEX}"""
  #rgbE = discord.Embed(title='Results',color=int(f'{RGBtoHEX}',16))
  #rgbE.set_footer(text="Color generated from RGB. Visit https://htmlcolorcodes.com for more utilities and fun information.")
  #await ctx.send(embed=rgbE)

#t_invite. Tee sends you a link when you can invite him to a server that you moderate.
@bot.command()
async def invite(ctx):
  inviteDESC = """Use the link below to invite me into a server you own or moderate.
  https://discord.com/api/oauth2/authorize?client_id=703432019522224169&permissions=0&scope=bot"""
  await ctx.send(inviteDESC)

#Tee repeats your message.
@bot.command(aliases=["repeat"])
async def say(ctx, arg):
 await ctx.message.delete()
 await ctx.send(arg)

#autoreply = True

@bot.event
async def on_ready():
 await bot.change_presence(status=discord.Status.online,activity=discord.Game("Tetris || t_help"))
 print('Logged in as')
 print(bot.user.name)
 print(bot.user.id)
 print('------')

bot.run(TOKEN)