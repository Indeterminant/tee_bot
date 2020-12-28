import discord
from discord.ext import commands
import asyncio
import random
import math
from discord.utils import get

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


###===========[BASIC COMMANDS]==============###
#hello
@bot.command()
async def hello(ctx):
  await ctx.send('Hello! I am Tee, the Tetris King and captain of the Starship Tetra.')

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
