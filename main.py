# si tu regarde ça c'est que tu veux participer au projet du bot (je suppose)
# toute les infos sont dans la README
# j'ai choisi python car c'est un langage acessible,et facile a utiliser
# version actuelle : 0.5
# j'ai jugé préférable de vous indiquer les section ou j'ai utlisé l'ia (gemini 3.5 flash)
# c'est un peu le bordel hésitez pas a faire une PULL REQUEST pour améliorer tt ça
# --DRID11--
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from typing import Optional
from discord import app_commands
from discord.ui import Button, View






load_dotenv()



bot = commands.Bot(command_prefix="/",intents=discord.Intents.all())
@bot.event
async def on_ready():
    print("hello world :DDDDDDDD")
      
    try:
       
       synced = await bot.tree.sync()
       print(f"syncro: {len(synced)}")

    except Exception as e :
         print("e")

@bot.tree.command(name="info", description="montre des informations a propos du bot ")
async def info(interaction:discord.interactions):
    embed= discord.Embed(
        title= 'info a propos du bot',
        description= 'bot qui fait tout car c\'est le goat ',
        color= discord.Color.purple())
    embed.add_field(name= 'version et changelog' , value=' v1, le bot devien goated ')
    embed.add_field(name="merci a",value="nicolas qui a tryhard le astrodico et la recherche des astres")
    embed.set_thumbnail(url='https://ici.exploratv.ca/upload/cms/IMAGES_2021/10-photos-espace-Pilier-creation.jpg')

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="questionsuggest", description="suggere une question a votre admin pref : anakine ")
async def info(interaction:discord.interactions,question:str):
    embed= discord.Embed(
        title= 'question suggérée',
        description= question,
        color= discord.Color.purple())
    

    await interaction.response.send_message(embed=embed)
    membre = await bot.fetch_user(1371065476746051624)

    if membre:
     await membre.send(f"on a suggéré une question: {question}")
@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id == 318312854816161792:
        return
    if payload.user_id == bot.user.id:
        return

    reaction_id = 1543939220962549822
    guild = bot.get_guild(payload.guild_id)
    member = await guild.fetch_member(payload.user_id)
    

    if not any(role.id == reaction_id for role in member.roles):
        role = guild.get_role(reaction_id)
        embed = discord.Embed(
            title=f'bravo a toi',
            description="bien joué tu as mis une réaction tu peux des maintenant en mettre partout",
            color=discord.Color.purple()
        )
        embed.set_thumbnail(url='https://www.gstatic.com/android/keyboard/emojikitchen/20231113/u1f947/u1f947_u1f3c6.png?fbx')
        #utilisation de l'ia dans le code si dessous afin de m'aider c'est la seule fois du programme
        try:
             await member.send(embed=embed)
        except discord.Forbidden:
             pass  
        # fin de section avec utilisation de l'ia
        await member.add_roles(role)
         
         
@bot.event
async def on_voice_state_update(member, before, after):
    voc_id=1544008288348147794
    radio_id=1544741067050713168
    role = member.guild.get_role(voc_id)

    role2 = member.guild.get_role(radio_id)

    if after.channel and after.channel.id == 1537416470458540082 and before.channel != after.channel:
        await member.add_roles(role2)

    if before.channel and before.channel.id == 1537416470458540082  and before.channel != after.channel:
        await member.remove_roles(role2)

    if before.channel is None and after.channel is not None:
         if not any(role.id == voc_id for role in member.roles): 
            embed = discord.Embed(
                          title=f'bravo a toi',
                          description="bien joué tu as rejoint un vocal tu peux des maintenant t\'exprimer avec ta voix",
                          color=discord.Color.purple()
                      )
            embed.set_thumbnail(url='https://www.gstatic.com/android/keyboard/emojikitchen/20231113/u1f947/u1f947_u1f3c6.png?fbx')
            await member.send(embed=embed)
            await member.add_roles(role)
              
@bot.tree.command(name="claim", description="recupère ta récompense")
@app_commands.choices(recompense=[
    app_commands.Choice ( name= "le dernier",value="le dernier")
    
    
])
async def succes(interaction: discord.Interaction,recompense:app_commands.Choice[str]):
    verif_ID = 1542855451996323840
    first_id = 1543292454784991343
    question_id=1543515726080380968
    iwantshowu_id=1543517610329505864
    react_id=1543939220962549822
    voc_id=1544008288348147794
    final_id=1544011693598707753
    membre= interaction.user
    role = membre.guild.get_role(final_id)
    if recompense.name == 'le dernier':
     if any(role.id == verif_ID for role in membre.roles):
           if any(role.id == first_id for role in membre.roles):
                 if any(role.id == question_id for role in membre.roles):
                       if any(role.id == iwantshowu_id for role in membre.roles):
                             if any(role.id == react_id for role in membre.roles):
                                   if any(role.id == voc_id for role in membre.roles):
                                         if not any(role.id == final_id for role in membre.roles):
                                               embed = discord.Embed(
                                                       title=f'bravo je pense que ce n\'était pas de tout repos {membre.display_name}',
                                                       description='tu as obtenu le succès : "grand final" bien joué  tu as maintenant toutes les permissions écrites ',
                                                       color=discord.Color.yellow())
                                               await membre.send(embed=embed)
                                               await membre.add_roles(role)
                                         else: await membre.send('tu as deja cette recompense ')
                                   else:await membre.send('succès manquant commande incomplete ')
                             else:await membre.send('succès manquant commande incomplete ')
                       else:await membre.send('succès manquant commande incomplete ')
                 else:await membre.send('succès manquant commande incomplete ')
           else:await membre.send('succès manquant commande incomplete ')
    else:await membre.send('succès manquant commande incomplete ')
                                   
                                                   
                                               
                                         

                      
         
@bot.event
async def on_message(message):
    ROLEfirst_ID = 1543292454784991343
    ROLEquestion_ID= 1543515726080380968
    ROLEimage_ID= 1543517610329505864
    general_id = 1537171333236924499
    question_id = 1539590329177481330
    
    auteurmsg = message.author

    if message.author == bot.user:
        return
          
          
    if message.channel.id == general_id:
        if not any(role.id == ROLEfirst_ID for role in auteurmsg.roles):
            role = message.guild.get_role(ROLEfirst_ID)
            
            embed = discord.Embed(
                title=f'bravo a {message.author}',
                description="bien joué tu as mis ton 1er message tu gagnes la permission de creer des fils",
                color=discord.Color.purple()
            )
            embed.set_thumbnail(url='https://www.gstatic.com/android/keyboard/emojikitchen/20231113/u1f947/u1f947_u1f3c6.png?fbx')
            await message.channel.send(embed=embed)
            await auteurmsg.add_roles(role)
    if message.channel.id == question_id:
            if not any(role.id == ROLEquestion_ID for role in auteurmsg.roles):
                role = message.guild.get_role(ROLEquestion_ID)
                embed = discord.Embed(
                    title=f'bravo a {message.author}',
                    description="bien joué tu as répondu a la question tu peux des maintenant mettre des images",
                    color=discord.Color.purple()
                )
                embed.set_thumbnail(url='https://www.gstatic.com/android/keyboard/emojikitchen/20231113/u1f947/u1f947_u1f3c6.png?fbx')
                await message.channel.send(embed=embed)
                await auteurmsg.add_roles(role)
    if message.attachments:
                if not any(role.id == ROLEimage_ID for role in auteurmsg.roles):
                    role = message.guild.get_role(ROLEimage_ID)
                    embed = discord.Embed(
                        title=f'bravo a {message.author}',
                        description="bien joué tu as mis une image tu peux des maintenant mettre des gifs ",
                        color=discord.Color.purple()
                    )
                    embed.set_thumbnail(url='https://www.gstatic.com/android/keyboard/emojikitchen/20231113/u1f947/u1f947_u1f3c6.png?fbx')
                    await message.channel.send(embed=embed)
                    await auteurmsg.add_roles(role)
    

    await bot.process_commands(message)

@bot.tree.command(name="lockchannel", description="empeche un role d'écrire dans ce salon")
@app_commands.checks.has_permissions(administrator= True) 
async def lockchannel(interaction: discord.Interaction, salon: discord.TextChannel):
    role = salon.guild.get_role(1543292454784991343)
    await salon.set_permissions(role, send_messages=False)
    await interaction.response.send_message(f"on ne peut plus écrire dans {salon.mention} !", ephemeral=True)

@bot.tree.command(name="unlockchannel", description="empeche un role d'écrire dans ce salon")
@app_commands.checks.has_permissions(administrator= True) 
async def lockchannel(interaction: discord.Interaction, salon: discord.TextChannel):
    role = salon.guild.get_role(1543292454784991343)
    await salon.set_permissions(role, send_messages=True)
    await interaction.response.send_message(f"on peut écrire dans {salon.mention} !", ephemeral=True)
@bot.tree.command(name="acceptreglement", description="accepte le reglement")
async def accept(interaction: discord.Interaction):
    buttonaccept = Button(label='j\'ai lu et j\'accepte le reglement', style=discord.ButtonStyle.green)
    role_id = 1542855451996323840

    async def button_callback(interaction):
        member = interaction.user
        role = interaction.guild.get_role(role_id)

        if any(r.id == role_id for r in member.roles):
            await interaction.response.send_message("Tu as deja accepté le reglement !", ephemeral=True)
        else:
            await member.add_roles(role)
            await interaction.response.send_message("Le règlement a été accepté !", ephemeral=True)
            await interaction.user.send("tu as accepté le reglement fait ```/succès``` pour voir tes succès")

    buttonaccept.callback = button_callback

    view = View()
    view.add_item(buttonaccept)

    embed = discord.Embed(
        title='accepte le reglement',
        description="quand tu auras cliqué sur le bouton ci dessous tu auras alors accepté le reglement tu pourras alors parler pourras alors être sanctioné en cas de non respect des regles ci dessus",
        color=discord.Color.blue()
    )

    await interaction.response.send_message(embed=embed, view=view)

@bot.tree.command(name="succès", description="regarde tes succès")
async def succes(interaction: discord.Interaction,membre:discord.Member):
    verif_ID = 1542855451996323840
    first_id = 1543292454784991343
    question_id=1543515726080380968
    iwantshowu_id=1543517610329505864
    react_id=1543939220962549822
    voc_id=1544008288348147794
    final_id=1544011693598707753
    okay ='​✅​'
    no='❌'


    embed = discord.Embed(
        title=f'voici la liste des succès de {membre.display_name}',
        color=discord.Color.dark_blue()
    )
    if any(role.id == verif_ID for role in membre.roles):
        embed.add_field(name="reglement accepté", value=f"{okay} tu as déja ce succès")
    else:
        embed.add_field(name="reglement accepté", value=f"{no} tu n'as pas ce succès")

    if any(role.id == first_id for role in membre.roles):
        embed.add_field(name="premier message", value=f"{okay} tu as déja ce succès")
    else:
        embed.add_field(name="premier message", value=f"{no} tu n'as pas ce succès")
    if any(role.id == question_id for role in membre.roles):
            embed.add_field(name="réponse a la question", value=f"{okay} tu as déja ce succès")
    else:
            embed.add_field(name="réponse a la question", value=f"{no} tu n'as pas ce succès")
    if any(role.id == iwantshowu_id for role in membre.roles):
                embed.add_field(name="je veux te montrer quelque chose", value=f"{okay} tu as déja ce succès")
    else:
                embed.add_field(name="je veux te montrer quelque chose", value=f"{no} tu n'as pas ce succès")
    if any(role.id == react_id for role in membre.roles):
                embed.add_field(name="action, réaction", value=f"{okay} tu as déja ce succès")
    else:
                embed.add_field(name="action, réaction", value=f"{no} tu n'as pas ce succès")
    if any(role.id == voc_id for role in membre.roles):
                embed.add_field(name="j'ai des cordes vocales", value=f"{okay} tu as déja ce succès")
    else:
                embed.add_field(name="j'ai des cordes vocales", value=f"{no} tu n'as pas ce succès")
    if any(role.id == final_id for role in membre.roles):
                embed.add_field(name="grand final", value=f"{okay} tu as déja ce succès")
    else:
                embed.add_field(name="grand final (besoin de faire /claim pour le recuperer avec comme récompense : le dernier)", value=f"{no} tu n'as pas ce succès")

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="succeshint", description="reçois un indice sur comment obtenir un succès")
@app_commands.choices(succes=[
    app_commands.Choice ( name= "accept reglement",value="accept reglement"),
    app_commands.Choice ( name= "premier message",value="premier message"), 
    app_commands.Choice ( name= "réponse a la question",value="réponse a la question"),
    app_commands.Choice ( name= "je veux te montrer quelque chose",value="je veux te montrer quelque chose"),
    app_commands.Choice ( name= "action,reaction",value="action,réaction"),
    app_commands.Choice ( name= "grand final",value="grand final"),
    app_commands.Choice ( name= "j'ai des cordes vocales",value="j'ai des cordes vocales")
    
])
async def succes(interaction: discord.Interaction,succes:app_commands.Choice[str]):
    


    embed = discord.Embed(
        title=f'voici un indice sur le succès {succes.name}  :',
        color=discord.Color.dark_blue()
    )
    if succes.name== 'accept reglement':
     embed.add_field(name="reglement accepté",value=f"il faut que tu accepte notre supperbe reglement ")
    elif succes.name== 'premier message':
        embed.add_field(name="premier message",value=f"envoyer un message c'est pas si compliqué ")
    elif succes.name== 'réponse a la question':
            embed.add_field(name="réponse a la question",value=f"il faudrait répondre a une question ")
    elif succes.name== 'je veux te montrer quelque chose':
                embed.add_field(name="je veux te montrer quelque chose",value=f"pour montrer il faudrait une image ou un dessin non ?")
    elif succes.name== 'action,reaction':
                    embed.add_field(name="action,reaction",value=f"le deuxieme mot t'indique peut être comment l'obtenir")
    elif succes.name== 'grand final':
                        embed.add_field(name="grand final",value=f"pour finir quelque chose c'est qu'il faut avoir tout fait non ?")
    elif succes.name== "j'ai des cordes vocales":
                            embed.add_field(name="j'ai des cordes vocales",value=f"si tu as des cordes vocales c'est qu'il faut les utiliser")
    else:
     embed.add_field(name="erreur",value=f"tu n'as pas mis de succes ")

    await interaction.response.send_message(embed=embed)
        
    membre = await bot.fetch_user(1371065476746051624)

    if membre:
     await membre.send(f"erreur succès non rentré dans la commande succèshint")
     await membre.send(f"erreur succès non rentré dans la commande succèshint")
     await membre.send(f"erreur succès non rentré dans la commande succèshint")



    

@bot.tree.command(name="embedcreate", description="[admins]crée un embed customisé") 
@app_commands.checks.has_permissions(administrator= True)    
async def embedcreate(interaction:discord.interactions,title:str,description:Optional[str],image:Optional[str],author:Optional[str],date:Optional[str],iconeenbas:Optional[str],miniature:Optional[str]):
    embed= discord.Embed(
        title= title,
        description= description,
        color= discord.Color.dark_blue())
    embed.set_thumbnail(url=miniature)
    embed.set_image(url= image)
    embed.set_author(name= author)
    embed.set_footer(text=date,icon_url=iconeenbas)
    await interaction.response.send_message(embed=embed)

ASTRES = {
    "m81": {
        "alias": ["galaxie de bode", "ngc 3031"],
        "titre": "M81",
        "description": "M81 (NGC 3031), aussi surnommée la galaxie de Bode, est une galaxie spirale rapprochée située à environ 12 millions d'al, selon des mesures non basées sur le décalage vers le rouge, dans la constellation de la Grande Ourse La classe de luminosité de M81. M81 est une galaxie LINER, c'est-à-dire une galaxie dont le noyau présente un spectre d'émission caractérisé par de larges raies d'atomes faiblement ionisés. De plus, elle est aussi une galaxie active de type Seyfert .Selon la base de données NASA/IPAC, la vitesse de M81 par rapport au fond diffus cosmologique est de 43 ± 6 km/s.trou noir supermassif au centre de M81 serait comprise entre 8,4 et 41 millions de M ⊙ (masse solaire /astrodefinition pour en savoir plus)",
        "champs": [
            ("découverte de M81", 'M81 a été découverte par l\'astronome allemand Johann Elert Bode en 1774, qui a aussi découvert la même nuit M82 (NGC 3034). On donne d\'ailleurs le nom de galaxies de Bode à ces deux galaxies. M81 a été redécouverte indépendamment par l\'astronome français Pierre Méchain en aout 1780 qui le signala à son ami Charles Messier. Messier a observé M81 le 9 février 1781. D\'autres astronomes ont aussi observé et enregistré M81, Johann Gottfried Koehler en 1779 et John Herschel en 1831', True),
            ('annecdotes sur M81:', 'M81 est une galaxie ou les novas(/astrodefinition) sont fréquentes on a aussi compté a ce jour une seule supernova dans cette galxie (date de rédaction:2026),M81 est très proche de M82, les deux galaxies n’étant séparées que d’environ 150 000 années-lumière. Cette proximité n’est pas seulement apparente : elles ont subi une interaction gravitationnelle importante. Un passage rapproché de M81 a notamment perturbé M82 et contribué à déclencher l’intense activité de formation d’étoiles qui caractérise aujourd’hui la galaxie du Cigare. Les deux galaxies font partie du même groupe de galaxies, avec notamment NGC 3077, et leurs interactions ont également déformé leurs structures et influencé la répartition du gaz.', True),
            ('comment l\'observer', 'l\'image ci dessous te montre sa position', False),
        ],
        "thumbnail": 'https://thumb.wikimedia.org/wikipedia/commons/thumb/9/99/NGC_3031_SDSS_%28M81%29.jpg/960px-NGC_3031_SDSS_%28M81%29.jpg?utm_source=fr.wikipedia.org&utm_campaign=parser&utm_content=thumbnail',
        "image": 'https://www.stelvision.com/astro/wp-content/uploads/2021/06/M81_M82_0.jpg',
        "footer": 'l\'image permettant la localisation provien du site de stellvision merci a eux'
    },
    "m1": {
        "alias": ["nébuleuse du crabe", "ngc 1952"],
        "titre": "M1",
        "description": "M1 (NGC 1952), aussi surnommée la nébuleuse du Crabe, est un rémanent de supernova et une nébuleuse de vent de pulsar située à environ 6 200 années-lumière de la Terre, dans la constellation du Taureau. Elle se trouve dans le bras de Persée de la Voie lactée. D'un diamètre d'environ 10 années-lumière, elle est en expansion à une vitesse d'environ 1 500 km/s. En son centre se trouve le pulsar du Crabe (PSR B0531+21), une étoile à neutrons qui tourne sur elle même environ 30 fois par seconde. La nébuleuse est principalement constituée des restes de l'étoile qui a explosé en supernova, avec notamment de l'hydrogène, de l'hélium, du carbone, de l'oxygène, de l'azote, du fer, du néon et du soufre. Son rayonnement est observable sur une très large gamme de longueurs d'onde, des ondes radio jusqu'aux rayons gamma.",
        "champs": [
            ("découverte de M1", 'La nébuleuse du Crabe a été observée pour la première fois en 1731 par l\'astronome britannique John Bevis. Charles Messier l\'a ensuite observée en 1758 alors qu\'il cherchait la comète de Halley. En constatant qu\'il ne s\'agissait pas de la comète recherchée, Messier décida de commencer un catalogue d\'objets nébuleux afin d\'éviter de les confondre avec des comètes. La nébuleuse du Crabe devint ainsi le premier objet de son catalogue, sous la désignation M1. Son nom de « nébuleuse du Crabe » vient d\'un dessin réalisé dans les années 1840 par William Parsons, troisième comte de Rosse, dont la forme lui évoquait un crabe.', True),
            ('annecdote sur M1:', 'M1 est particulièrement célèbre car elle est directement associée à la supernova SN 1054, observée par des astronomes chinois, japonais et arabes en 1054. Cette supernova était si brillante qu\'elle a été visible en plein jour pendant environ 23 jours et est restée observable à l\'œil nu pendant près de deux ans. La nébuleuse du Crabe est le premier objet astronomique dont le lien avec une explosion de supernova historique a pu être établi.', True),
        ],
        "thumbnail": 'https://cdn.discordapp.com/attachments/1545471786496426118/1545775931203788811/Crab_Nebula.jpg?ex=6a9d5f85&is=6a9c0e05&hm=41724e4c989c7fc7d26de61060ffa2a7fa050016f9b6f5f0971e61d743e337fd&',
        "image": 'https://www.astroshop.de/CMS/images/text/category/Id%201270%20Messier_1.jpg',
        "footer": 'l\'image de localisation provient de astroshop merci a eux'
    },
    "m2": {
        "alias": ["ngc 7089"],
        "titre": "M2",
        "description": "M2 (NGC 7089) est un amas globulaire situé à environ 37 500 années-lumière de la Terre, dans la constellation du Verseau. Il appartient à la Voie lactée et est âgé d'environ 11,78 milliards d'années. Sa masse est estimée à environ 104 000 masses solaires. Avec un diamètre apparent de 16 minutes d'arc, sa taille réelle est d'environ 175 années-lumière. M2 est classé dans la classe II de concentration de Shapley-Sawyer, ce qui signifie qu'il possède une forte concentration d'étoiles vers son centre. Il est également pauvre en éléments lourds, avec une métallicité bien inférieure à celle du Soleil.",
        "champs": [
            ("découverte de M2", 'M2 a été découvert par l\'astronome italien Giovanni Domenico Maraldi le 11 septembre 1746, alors qu\'il recherchait la comète de Chéseaux. Il observa un objet rond, brillant en son centre, qu\'il prit d\'abord pour une comète. Exactement 14 ans plus tard, le 11 septembre 1760, Charles Messier redécouvrit indépendamment l\'objet et le décrivit comme une nébuleuse sans étoiles. William Herschel fut ensuite le premier à résoudre ses étoiles et à comprendre sa véritable nature d\'amas globulaire. M2 fut plus tard inscrit dans le New General Catalogue sous la désignation NGC 7089.', True),
            ('annecdote sur M2:', 'M2 est entouré d\'une immense enveloppe stellaire diffuse et possède une longue queue de marée composée de débris d\'étoiles, s\'étendant sur environ 45° dans le ciel. On pense alors que M2 pourrait être le vestige d\'une ancienne galaxie naine capturée par la Voie lactée.', True),
        ],
        "thumbnail": 'https://cdn.discordapp.com/attachments/1545471786496426118/1545778297114206229/Messier2_-_HST_-_Potw1913a.jpg?ex=6a9d61b9&is=6a9c1039&hm=4be4d63cf7fe0a821d2ead44c1a4b018c33057bd0f4eaaef8e73b4929d5887f2&',
        "image": 'https://upload.wikimedia.org/wikipedia/commons/9/92/NGC_7089_Stellarium.jpg?utm_source=fr.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail_unscaled',
        "footer": 'l\'image de localisation provient du logiciel stellarium merci a eux'
    },
    "m3": {
            "alias": ["NGC 5272"],
            "titre": "M3",
            "description": "M3 (NGC 5272) est un amas globulaire situé à environ 33 300 années-lumière de la Terre, dans la constellation des Chiens de chasse. Il appartient à la Voie lactée et est âgé d'environ 11,4 milliards d'années. Avec une masse estimée à environ 957 000 masses solaires et un diamètre d'environ 174 années-lumière, M3 est l'un des amas globulaires les plus massifs et les plus brillants connus. Il contient environ un demi-million d'étoiles et possède une magnitude apparente de 6,3, le plaçant juste au-dessus de la limite théorique de visibilité à l'œil nu.",
            "champs": [
                ("découverte de M3", 'M3 a été découvert par l\'astronome français Charles Messier le 3 mai 1764. Il s\'agit du premier objet de son catalogue qu\'il a lui-même découvert. À l\'époque, Messier le décrit comme une nébuleuse, sans savoir qu\'il s\'agissait d\'un amas composé de centaines de milliers d\'étoiles. En 1784, William Herschel fut le premier à décrire la composition de M3 en étoiles et à reconnaître sa véritable nature d\'amas globulaire.', True),
                ('annecdotes sur M3:', 'M3 est particulièrement remarquable par son nombre exceptionnel d\'étoiles variables. On en connaît aujourd\'hui 274, dont au moins 170 sont des étoiles de type RR Lyrae. Cela en fait l\'amas globulaire connu qui possède la plus grande population d\'étoiles variables.M3 contient également un nombre important d\'étoiles bleues traînardes. Ces étoiles sont plus chaudes, plus bleues et plus lumineuses que les autres étoiles de l\'amas, ce qui est étonnant dans un amas globulaire principalement constitué de très vieilles étoiles. Leur formation, probablement liée à des interactions entre étoiles ou à des fusions, reste un sujet de recherche', True),
            ],
            "thumbnail": 'https://cdn.discordapp.com/attachments/1545471786496426118/1545780640648003625/Messier3_-_HST_-_Potw1914a.jpg?ex=6a9d63e7&is=6a9c1267&hm=761e1939a30972ebb01ee6e2a613875110af17750d2cc183012814e040f1788e&',
            "image": 'https://upload.wikimedia.org/wikipedia/commons/1/17/M3map.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail_unscaled&_=20090410155347',
            "footer": 'l\'image de localisation provient de wikipédia merci a eux'
        },
    "m4": {
                    "alias": ["NGC 6121"],
                    "titre": "M4",
                    "description": "M4 (ou NGC 6121) est un amas globulaire situé dans la constellation du Scorpion, à environ 7 200 années-lumière du Soleil. Avec une masse d'environ 195 000 fois celle du Soleil et un âge estimé à 12,54 milliards d'années, M4 fait partie des amas globulaires les plus proches de nous et les plus anciens de notre environnement galactique. Il possède une magnitude apparente de 5,4, ce qui le rend visible avec des jumelles dans de bonnes conditions, et s'étend sur environ 36 minutes d'arc dans le ciel.",
                    "champs": [
                        ("découverte de M4", "M4 a été découvert en 1746 par l'astronome suisse Jean Philippe Loys de Cheseaux. À l'époque, les amas globulaires étaient encore considérés comme des objets nébuleux dont la véritable nature restait inconnue. Ce n'est que plus tard que les astronomes ont pu comprendre qu'il s'agissait d'immenses regroupements d'étoiles liés par la gravitation. M4 est aujourd'hui connu sous la désignation NGC 6121 et orbite autour du centre de la Voie lactée.", True),
                        ('annecdotes sur M4:', "M4 abrite une planète extrêmement ancienne, appelée PSR B1620-26 b. Découverte en 2003 grâce au télescope spatial Hubble, elle possède une masse estimée à environ 2,5 fois celle de Jupiter et serait âgée d'environ 13 milliards d'années. Elle est particulièrement surprenante car elle orbite autour d'un système composé d'une naine blanche et d'un pulsar. Elle s'est donc formée lorsque l'Univers était encore très jeune, près de trois fois avant la formation du Système solaire.En 2023, l'étude des mouvements d'étoiles au cœur de l'amas a conduit à proposer l'existence d'un objet invisible d'environ 800 masses solaires. Il pourrait s'agir d'un trou noir de masse intermédiaire, beaucoup plus massif que les trous noirs stellaires mais beaucoup moins que les trous noirs supermassifs, car celui-ci est si compact qu'aucune autre hypothèse ne peut supporter la nature de cet objet. Cette interprétation reste cependant à confirmer, car la nature exacte de cet objet n'est pas encore établie. ", True),
                    ],
                    "thumbnail": 'https://cdn.discordapp.com/attachments/1545471786496426118/1545782281535492146/241129.jpg?ex=6a9e0e2f&is=6a9cbcaf&hm=fe1ecd708363fa2bcaa35bd2d54d645b44e33f6cc76dcf968db04ef233719352&',
                    "image": 'http://www.waloszek.de/astro_dso/M4_1600m.jpg',
                    "footer": 'l\'image de localisation provient de waloszek merci a eux'
                },
    "m5": {
                                    "alias": ["NGC 6121"],
                                    "titre": "M5",
                                    "description": "M5 (ou NGC 5904) est un amas globulaire situé dans la constellation du Serpent, à environ 24 500 années-lumière du Soleil. Avec un diamètre d'environ 164 années-lumière et un âge estimé à 10,62 milliards d'années, M5 est un immense regroupement d'étoiles très ancien. Il possède une magnitude apparente de 5,7, ce qui le rend observable avec des jumelles dans de bonnes conditions, et il orbite autour du centre de la Voie lactée.",
                                    "champs": [
                                        ("découverte de M5", "M5 a été découvert le 5 mai 1702 par l'astronome allemand Gottfried Kirch. À cette époque, sa nature d'amas globulaire n'était pas encore comprise : il apparaissait simplement comme une tache nébuleuse dans les instruments astronomiques. Il a ensuite été catalogué sous le nom de NGC 5904, qui est aujourd'hui sa désignation officielle.", True),
                                        ('annecdotes sur M5:', "M5 est particulièrement intéressant pour les astronomes car il est relativement riche en étoiles variables. Ces étoiles dont la luminosité change au cours du temps permettent notamment d'étudier les propriétés et la distance des amas globulaires. M5 possède également une importante population d'étoiles bleues traînardes (blue stragglers), des étoiles qui paraissent plus jeunes, plus chaudes et plus bleues que les autres étoiles de leur amas. Leur formation est encore étudiée aujourd'hui.", True),
                                    ],
                                    "thumbnail": 'https://cdn.discordapp.com/attachments/1545471786496426118/1545803554718224394/Messier_5_-_HST.jpg?ex=6a9e21ff&is=6a9cd07f&hm=d7b9dfe29c634b0ccb6cc97b4806627c5dabc5f67c0de1c4b363573275b234ae&',
                                    "image": 'http://www.waloszek.de/astro_dso/M5_2_1800.jpg',
                                    "footer": 'l\'image de localisation provient de waloszek merci a eux'
                                },
    "m6": {
             "alias": ["NGC 6405","amas du papillon"],
             "titre": "M6",
             "description": "M6 (ou NGC 6405, aussi appelé amas du Papillon) est un amas ouvert situé dans la constellation du Scorpion, à environ 1 490 années-lumière du Soleil. Il mesure environ 10,5 années-lumière de diamètre et son âge est estimé à environ 76 millions d'années (soit à peine à peine environ 1,7 % de l'âge du Soleil). Avec une magnitude apparente de 4,2, M6 est suffisamment lumineux pour être aperçu à l'œil nu sous un ciel très sombre et facilement observable avec de petites jumelles. Il contient plusieurs dizaines d'étoiles considérées comme membres confirmés de l'amas.",
             "champs": [
                ("découverte de M6", "M6 a été observé pour la première fois par l'astronome italien Giovanni Battista Hodierna, avant 1674, mais la date exacte de sa découverte est inconnue. L'astronome suisse Jean Philippe Loys de Cheseaux le redécouvrit vers 1745-1746 et fut l'un des premiers à reconnaître qu'il s'agissait d'un véritable amas d'étoiles. Nicolas-Louis de Lacaille l'intégra ensuite à son catalogue en 1751-1752, avant que Charles Messier ne l'ajoute à son célèbre catalogue en 1764, sous la désignation M6.", True),
                ('annecdotes sur M6:', "M6 est surnommé l'amas du Papillon en raison de la disposition de ses étoiles, qui évoque la silhouette d'un papillon. Avec une magnitude de 4,2, il est l'un des objets de Messier les plus faciles à observer : sous un ciel suffisamment sombre, il peut même être aperçu sans instrument. L'une des étoiles les plus remarquables de M6 est BM Scorpii, une supergéante jaune ou orange et une étoile variable. Sa luminosité change au cours du temps, avec une magnitude apparente variant approximativement de 5,25 à 6,46. Elle est également l'une des étoiles les plus brillantes de l'amas et contribue fortement à son apparence caractéristique. ", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545804865517920356/NGC_6405_DSS.jpg?ex=6a9e2337&is=6a9cd1b7&hm=42205b9f2c3159b22b76a5941e6fe724649d3a20b4f9723fcc4f3ab4bf3f5228&",
             "image": 'http://www.waloszek.de/astro_dso/M6_M7_1800.jpg',
             "footer": 'l\'image de localisation provient de waloszek merci a eux'
                                },
    "m7": {
             "alias": ["NGC 6475","amas de ptolémée"],
             "titre": "M7",
             "description": "M7 (ou NGC 6475), aussi appelé amas de Ptolémée, est un amas ouvert situé dans la constellation du Scorpion, à environ 890 années-lumière du Soleil. Il mesure environ 20,1 années-lumière de diamètre et son âge est estimé à environ 465 millions d'années selon les données récentes de Gaia. Avec une magnitude apparente de 3,3, M7 est facilement observable à l'œil nu sous un ciel suffisamment sombre. Il possède une masse d'environ 791 masses solaires et compte plusieurs dizaines à plus d'une centaine d'étoiles selon les méthodes de comptage utilisées.",
             "champs": [
                ("découverte de M7", "M7 est l'un des objets astronomiques les plus anciens à avoir été décrit : il fut observé par l'astronome grec Claude Ptolémée vers 138 apr. J.-C., d'où son surnom d'amas de Ptolémée. Il fut ensuite observé par plusieurs astronomes, notamment Abd al-Rahman al-Soufi, Ulugh Beg, Giovanni Battista Hodierna et Edmond Halley. Charles Messier l'observa le 23 mai 1764, la même nuit que M6, et l'intégra à son célèbre catalogue sous la désignation M7. Il fut ensuite étudié par plusieurs astronomes, dont William Herschel et John Herschel, avant d'être intégré au New General Catalogue sous la désignation NGC 6475.", True),
                ('annecdotes sur M7:', "M7 est l'un des amas ouverts les plus brillants du catalogue de Messier. Avec une magnitude apparente de 3,3, il est suffisamment lumineux pour être observé à l'œil nu. Sa grande taille apparente, d'environ 75 à 80 minutes d'arc, le rend particulièrement spectaculaire dans le ciel du Scorpion.Son âge est estimé à environ 465 millions d'années selon une étude récente basée sur les données du satellite Gaia. Cependant, d'autres estimations donnent un âge d'environ 140 millions d'années, ce qui montre que l'âge exact de M7 reste discuté. Même avec l'estimation la plus élevée, ses étoiles sont beaucoup plus jeunes que le Soleil, âgé d'environ 4,6 milliards d'années. ", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545806297918603314/The_star_cluster_Messier_7.jpg?ex=6a9e248d&is=6a9cd30d&hm=66d0b09697e88ebb4eb24a7bcac0fe1f89c8ff071c3dbb08217b477b4842f3d6&",
             "image": 'https://dq0hsqwjhea1.cloudfront.net/M6-M7-locator_Generic-V2.jpg',
             "footer": 'l\'image de localisation provient de skyandtelescope merci a eux'
                                },
    "m8": {
             "alias": ["NGC 6523","nébuleuse de la lagune"],
             "titre": "M8",
             "description": "M8 (ou NGC 6523) aussi appelée nébuleuse de la Lagune ou nébuleuse du Lagon, est une nébuleuse en émission située dans la constellation du Sagittaire, à environ 4 080 années-lumière de la Terre. Il s'agit d'un immense nuage interstellaire composé principalement d'hydrogène et de poussières, dans lequel se forment de nombreuses étoiles jeunes. Elle mesure environ 45 × 30 minutes d'arc dans le ciel, ce qui correspond à une taille réelle d'environ 54 années-lumière dans sa plus grande dimension. Avec une magnitude apparente d'environ 6,0, elle peut être visible à l'œil nu sous un ciel très sombre et dans de bonnes conditions.",
             "champs": [
                ("découverte de M8", "La nébuleuse de la Lagune a été découverte par l'astronome italien Giovanni Battista Hodierna avant 1654. Elle fut ensuite observée en 1680 par John Flamsteed, qui la décrivit également comme une nébuleuse. En 1746, Jean Philippe Loys de Cheseaux parvint à distinguer certaines étoiles à l'intérieur de la nébuleuse et la classifia alors comme un amas stellaire. Guillaume Le Gentil l'observa à son tour en 1747, puis Nicolas-Louis de Lacaille la catalogua en 1751-1752 sous la désignation Lacaille III.13. Le 23 mai 1764, Charles Messier l'ajouta à son catalogue sous le numéro M8. Le nom de « nébuleuse de la Lagune » fut finalement donné en 1890 par l'astronome britannique Agnes Mary Clerke.", True),
                ('annecdotes sur M8:', "M8 est une véritable pouponnière stellaire. Elle contient l'amas ouvert NGC 6530, composé d'étoiles très jeunes et très chaudes de types spectraux O et B, âgées d'environ 2 millions d'années. Ces étoiles se sont donc formées très récemment à l'échelle cosmique à partir du gaz de la nébuleuse.La nébuleuse est illuminée notamment par 9 Sagittarii, un système binaire constitué de deux géantes bleues extrêmement lumineuses. Elles brillent respectivement à environ 316 000 et 562 000 fois la luminosité du Soleil ! Leur rayonnement ultraviolet ionise le gaz environnant, ce qui fait briller la nébuleuse. ", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545809044965687296/Lagoon_Nebula_ESO.jpg?ex=6a9e271c&is=6a9cd59c&hm=4e9387b41abd57325c110a8171ecc0e5553ece3ce05e91d20095ad2558f093a7&",
             "image": 'https://www.constellation-guide.com/wp-content/uploads/2014/03/Lagoon-Nebula-location.webp',
             "footer": 'l\'image de localisation provient de constellaton guide merci a eux'
                                },
    "m9": {
             "alias": ["NGC 6333"],
             "titre": "M9",
             "description": "M9 (ou NGC 6333) est un amas globulaire situé dans la constellation d'Ophiuchus âgé d'environ 12 milliards d'années, à environ 25 800 années-lumière de la Terre. Il appartient à la Voie lactée, possède un diamètre apparent d'environ 12 minutes d'arc et une masse d'environ 422 000 masse solaire. Avec une magnitude apparente de 7,72, M9 n'est pas visible à l'œil nu, mais peut être observé avec une petite lunette ou un télescope. Il s'agit d'un ensemble extrêmement dense de vieilles étoiles liées entre elles par la gravitation.",
             "champs": [
                ("découverte de M9", "M9 a été découvert par l'astronome français Charles Messier le 28 mai 1764. Messier l'observa alors qu'il recherchait des objets nébuleux qui pouvaient être confondus avec des comètes. Il le décrivit comme une nébuleuse sans étoiles visibles avec les instruments de l'époque. Ce n'est que plus tard, grâce à des télescopes plus puissants, que sa nature d'amas globulaire fut clairement établie.", True),
                ('annecdotes sur M9:', "M9 se trouve dans une région du ciel où la poussière interstellaire de la Voie lactée masque une partie de sa lumière. Malgré sa distance d'environ 25 800 années-lumière, il reste suffisamment lumineux pour être facilement repéré au télescope.Une particularité intéressante de M9 est sa forme légèrement aplatie : contrairement à certains amas globulaires presque parfaitement sphériques, M9 présente une certaine déformation. Cette caractéristique est notamment liée aux effets gravitationnels qu'il subit au cours de son déplacement autour du centre de la Voie lactée.Enfin, M9 appartient à la classe VIII dans la classification de concentration des amas globulaires de Harlow Shapley et Helen Sawyer Hogg. M9 se situe donc dans la partie relativement peu concentrée de cette classification.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545811086463344640/Messier_9_Hubble_WikiSky_wfpc2_patched.jpg?ex=6a9e2902&is=6a9cd782&hm=8da981f1bbf5de8769c31b44fe0a32662faa455962f0a92c9c02d56c64199bfd&",
             "image":"https://upload.wikimedia.org/wikipedia/commons/2/2b/M9map.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original ",
             "footer": 'l\'image de localisation provient de wikipédia merci a eux'
                                },
    "m10": {
             "alias": ["NGC 6254"],
             "titre": "M10",
             "description": "M10 (ou NGC 6254) est un amas globulaire situé dans la constellation d'Ophiuchus, à environ 14 400 années-lumière du Soleil. Il appartient à la Voie lactée, possède un diamètre d'environ 80 années-lumière et une masse estimée à environ 252 000 fois celle du Soleil. Avec une magnitude apparente de 6,6, M10 est suffisamment lumineux pour être facilement observable avec des jumelles, où il apparaît comme une petite tache laiteuse. Son âge est estimé à environ 11,4 milliards d'années.",
             "champs": [
                ("découverte de M10", "M10 a été découvert par l'astronome français Charles Messier le 29 mai 1764. Il l'inscrivit dans son catalogue en le décrivant comme une nébuleuse ronde sans étoiles visibles. En 1774, l'astronome allemand Johann Elert Bode le décrivit également comme une tache nébuleuse très pâle. Plus tard, William Herschel utilisa des instruments plus puissants qui lui permirent de résoudre l'amas en étoiles individuelles. Il le décrivit alors comme un « beau groupe d'étoiles extrêmement comprimées ». John Dreyer l'ajouta ensuite au New General Catalogue sous la désignation NGC 6254.", True),
                ('annecdotes sur M10:', "Malgré son âge, M10 possède une population importante de traînardes bleues. Ces étoiles semblent plus jeunes et plus chaudes que ce que leur âge devrait laisser attendre. Les observations du télescope spatial Hubble ont notamment montré leur présence dans la région centrale de l'amas. Certaines de ces étoiles se seraient formées il y a seulement 2 à 5 milliards d'années, bien après la formation de la majorité des étoiles de M10.M10 contient également de nombreuses étoiles variables. Des observations réalisées entre 1998 et 2015 ont permis d'en identifier environ 40, dont plusieurs types différents : étoiles RR Lyrae, céphéides de type II, étoiles SX Phoenicis pulsantes, étoiles binaires à contact et géantes rouges semi-régulières. ", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545812858611441795/Messier_10_Hubble_WikiSky.jpg?ex=6a9e2aa9&is=6a9cd929&hm=d3b684d60367f15f26dffdf54c06471e02fc3330bf9f07bb4c1cd7107540e924&",
             "image": 'https://upload.wikimedia.org/wikipedia/commons/6/65/Ophiuchus_IAU.svg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original',
             "footer": 'l\'image de localisation provient de wikipédia merci a eux'
                                },
    "m11": {
             "alias": ["NGC 6705","amas du canard sauvage"],
             "titre": "M11",
             "description": "M11 (ou NGC 6705, aussi appelé amas du Canard sauvage) est un amas ouvert situé dans la constellation de l'Écu de Sobieski, à environ 6 730 années-lumière du Soleil. Il mesure environ 21,5 années-lumière de diamètre et son âge est estimé entre 200 et 440 millions d'années selon les études. M11 reste donc un amas très jeune à l'échelle astronomique. À titre de comparaison, le Soleil est âgé d'environ 4,6 milliards d'années. Avec une magnitude apparente de 5,8, M11 est visible aux jumelles sous la forme d'une tache diffuse et peut révéler de nombreuses étoiles avec un télescope. Il contient plusieurs centaines d'étoiles.",
             "champs": [
                ("découverte de M11", "M11 a été découvert par l'astronome allemand Gottfried Kirch à l'observatoire de Berlin en 1681. Ses étoiles furent ensuite résolues par William Derham en 1733. Charles Messier l'intégra à son catalogue le 30 mai 1764. Au fil des années, l'amas fut observé par plusieurs astronomes, notamment Edmond Halley, Jean Philippe Loys de Cheseaux, Johann Elert Bode, Caroline Herschel et William Herschel. En 1835, l'astronome britannique William Henry Smyth lui donna son célèbre surnom d'amas des Canards sauvages, en raison de sa forme qui lui rappelait un groupe de canards en vol. Il fut ensuite catalogué sous le nom de NGC 6705 par John Dreyer.", True),
                ('annecdotes sur M11:', "M11 est un amas ouvert particulièrement dense. Sa concentration est si importante qu'avec un télescope, il peut facilement donner l'impression d'être un amas globulaire, alors qu'il s'agit bien d'un amas ouvert. M11 contient également un grand nombre d'étoiles variables. En 2007, 82 étoiles variables avaient été identifiées dans l'amas, appartenant à plusieurs catégories différentes, notamment des étoiles Delta Scuti, Gamma Doradus et plusieurs types d'étoiles binaires. Au moins une traînarde bleue (blue straggler) y a également été découverte. ", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545819739320754268/Eso1430a.jpg?ex=6a9ed9d1&is=6a9d8851&hm=ed35df4dce68e8701c6965dd0fb25e3151102055a5f8ea5c29325c9c5a9fd51a&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/03/Messier-11-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m12": {
                 "alias": ["NGC 6218"],
                 "titre": "M12",
                 "description": "M12 (ou NGC 6218) est un amas globulaire situé dans la constellation d'Ophiuchus, à environ 16 000 années-lumière du Soleil et 14 700 années-lumière du centre de la Voie lactée. Il mesure environ 16 minutes d'arc dans le ciel et possède une masse estimée à environ 217 000 fois celle du Soleil. Avec une magnitude apparente de 6,1, M12 est presque visible à l'œil nu et facilement observable avec des jumelles sous un ciel sombre. Il contient environ 200 000 étoiles et son âge est estimé à environ 12,7 milliards d'années.",
                 "champs": [
                    ("découverte de M12", "M12 a été découvert par l'astronome français Charles Messier le 30 mai 1764. Dans son carnet d'observation, Messier le décrivit comme une nébuleuse ronde ne contenant pas d'étoiles, dont le diamètre pouvait atteindre environ 3 minutes d'arc. L'amas fut ensuite observé par Johann Bode en 1774 et par John Herschel en 1825. En 1783, William Herschel fut le premier à parvenir à résoudre les étoiles de M12, révélant ainsi qu'il s'agissait bien d'un amas d'étoiles.", True),
                    ('annecdotes sur M12:', "M12 contient environ 200 000 étoiles. Les plus brillantes atteignent une magnitude d'environ 12, et le type spectral global de l'amas est estimé à F7. L'astronome Allan Sandage a également identifié 13 étoiles variables au sein de M12.La métallicité de M12 est comprise entre −1,14 et −1,37, ce qui signifie que sa concentration en fer représente environ 4,2 à 7,2 % de celle du Soleil. Cette faible métallicité est caractéristique des anciens amas globulaires et témoigne d'une époque où l'Univers contenait encore beaucoup moins d'éléments lourds. ", True),
                                        ],
                 "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545829922092875776/M12_Hubble.jpg?ex=6a9e3a8d&is=6a9ce90d&hm=a77052d1a2be1c37cc2cf6161db08fe1a0395e4514e7b6e7ad8c39d520dc4244&",
                 "image": 'https://www.messier-objects.com/wp-content/uploads/2015/03/Messier-12-location.png',
                 "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                    },
    "m13": {
                 "alias": ["NGC 6205","grand amas d'hercule"],
                 "titre": "M13",
                 "description": "M13 (ou NGC 6205, aussi appelé Grand Amas d'Hercule) est un amas globulaire situé dans la constellation d'Hercule, à environ 25 100 années-lumière du Soleil. Il mesure environ 145 années-lumière de diamètre et contient plus de 100 000 étoiles. Avec une magnitude apparente de 5,8, M13 peut être distingué à l'œil nu sous un ciel sombre et sans Lune brillante. Son âge est estimé à environ 11,65 milliards d'années et sa masse à 775 000 M ⊙(masses solaires).",
                 "champs": [
                    ("découverte de M13", "M13 a été découvert par l'astronome anglais Edmond Halley en 1714. Charles Messier l'ajouta ensuite à son catalogue le 1er juin 1764. À cette époque, l'amas apparaissait comme une tache nébuleuse, car les instruments ne permettaient pas encore de distinguer ses étoiles individuellement. Ce n'est qu'en 1799 que William Herschel parvint pour la première fois à résoudre les étoiles de M13.", True),
                    ('annecdotes sur M13:', "M13 est un amas particulièrement dense. Dans sa région centrale, la densité d'étoiles est environ 100 fois supérieure à celle de la région entourant le Système solaire. Les étoiles y sont tellement rapprochées qu'elles peuvent parfois entrer en collision, donnant naissance à des étoiles massives appelées traînardes bleues. Le télescope spatial Hubble en a notamment révélé de nombreuses au cœur de l'amas.M13 contient également au moins 64 étoiles variables. Les deux dernières, V63 et V64, ont été découvertes respectivement en 2021 et 2022 par Francisco Violat-Bordonau. L'une des étoiles les plus brillantes de M13 est V11, également désignée V1554 Herculis. Il s'agit d'une géante rouge et d'une étoile variable, dont la magnitude apparente est d'environ 11,95.M13 est aussi célèbre pour avoir été la cible d'un message radio destiné à d'éventuelles civilisations extraterrestres. Le 16 novembre 1974, le radiotélescope d'Arecibo a envoyé un message en direction du Grand Amas d'Hercule. Ce message, connu sous le nom de message d'Arecibo, contenait des informations codées sur l'humanité et la Terre. ", True),
                                        ],
                 "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545831681682968596/NGC_6205_SDSS2.jpg?ex=6a9e3c31&is=6a9ceab1&hm=521323b0ceede6c480055f075d2d64231190d6c8e4b246ab5cbec6119884660e&",
                 "image": 'https://www.universetoday.com/article_images/Messier-13-location-472x580.png',
                 "footer": 'l\'image de localisation provient de messier object merci a eux'
                                    },
    "m14": {
                 "alias": ["NGC 6402"],
                 "titre": "M14",
                 "description": "M14 (ou NGC 6402) est un amas globulaire situé dans la constellation d'Ophiuchus, à environ 30 300 années-lumière du Soleil. Il mesure environ 100 années-lumière de diamètre et contient environ 150 000 étoiles. Avec une magnitude apparente de 6,72, M14 est facilement observable avec des jumelles, mais reste invisible à l'œil nu. Son âge est estimé à environ 12,6 milliards d'années et sa masse  à 1 040 000  M ⊙(masse solaires).",
                 "champs": [
                    ("découverte de M14", "M14 a été découvert par l'astronome français Charles Messier le 1er juin 1764. L'amas fut ensuite étudié par différents astronomes, qui ont notamment permis de mieux déterminer ses caractéristiques physiques et sa composition.", True),
                    ('annecdotes sur M14:', "M14 contient environ 70 étoiles variables, dont plusieurs sont des étoiles W Virginis, une sous-classe des céphéides de type II. L'amas possède également un nombre important d'étoiles RR Lyrae, qui sont elles aussi des étoiles variables.Contrairement à de nombreux amas globulaires, M14 n'est pas parfaitement sphérique : son ellipticité de 0,11 montre qu'il est légèrement aplati. ", True),
                                        ],
                 "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545832651686940852/NGC_6402_PanS.jpg?ex=6a9e3d18&is=6a9ceb98&hm=cfb583c37356320c55ac8ff78f0552103919fd68dd3448b2491c9a0cdd4d9333&",
                 "image": 'https://www.messier-objects.com/wp-content/uploads/2015/03/Messier-14-location.png',
                 "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                    },
    "m15": {
                 "alias": ["NGC 7078"],
                 "titre": "M15",
                 "description": "M15 (ou NGC 7078) est un amas globulaire situé dans la constellation de Pégase, à environ 35 700 années-lumière du Soleil. Il mesure environ 187 années-lumière de diamètre et contient environ 150 000 étoiles. Avec une magnitude apparente d'environ 6,2, M15 est facilement observable avec de petites jumelles, où il apparaît comme une tache laiteuse. Son âge est estimé à environ 12,93 milliards d'années et sa masse à  1 190 000 M☉.",
                 "champs": [
                    ("découverte de M15", "M15 a été découvert par l'astronome italien Giovanni Domenico Maraldi le 7 septembre 1746, alors qu'il cherchait la comète de Chéseaux. Il remarqua une étoile nébuleuse assez brillante entre les étoiles Epsilon Pegasi et Beta Equulei.Charles Messier retrouva l'amas dans la nuit du 3 au 4 juin 1764 et l'ajouta à son catalogue. Il le décrivit comme une « nébuleuse ronde et sans étoiles, avec un centre brillant ». En 1783, William Herschel parvint finalement à résoudre ses étoiles et à découvrir la véritable nature de cette nébuleuse. M15 fut ensuite catalogué sous le nom de NGC 7078 par John Dreyer.", True),
                    ('annecdotes sur M15:', "M15 est un amas particulièrement dense. Il est peut-être même le plus dense des amas globulaires connus dans la Voie lactée. Son noyau a subi un phénomène appelé effondrement de cœur, qui a rendu sa région centrale extrêmement compacte. Le noyau ne mesure qu'environ 0,14 minute d'arc, tandis que la moitié de la masse de l'amas se trouve dans un rayon d'environ 10 années-lumière. Certains chercheurs pensent que le centre de M15 pourrait contenir un ou plusieurs trous noirs.L'amas contient environ 70 étoiles variables. Certaines sont des étoiles W Virginis, une sous-classe des céphéides de type II, et M15 possède également un nombre important d'étoiles RR Lyrae.Enfin, M15 se trouve à environ 4,1° au nord-ouest de l'étoile Enif (Epsilon Pegasi), ce qui permet de le localiser relativement facilement dans la constellation de Pégase. ", True),
                                        ],
                 "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545833485133029499/NGC_7078_SDSS9_Color.jpg?ex=6a9e3ddf&is=6a9cec5f&hm=fc68de8ebb99e73bba01febc1084c831f5b909215bc79c17646e3b3f6b9253bd&",
                 "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-15-location.png',
                 "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                    },
    "m16": {
                 "alias": ["NGC 6611"],
                 "titre": "M16",
                 "description": "M16 (ou NGC 6611) est un très jeune amas ouvert situé dans la constellation du Serpent, à environ 5 160 années-lumière du Soleil. Il mesure environ 15 années-lumière de diamètre et est âgé d'environ 5,5 millions d'années. Avec une magnitude apparente de 6,0, il est observable avec des jumelles, où l'on peut distinguer une dizaine de ses étoiles. M16 baigne dans la nébuleuse de l'Aigle (IC 4703), une région où de nouvelles étoiles se forment.",
                 "champs": [
                    ("découverte de M16", "M16 a été découvert par l'astronome suisse Jean Philippe Loys de Cheseaux en 1745. Charles Messier le redécouvrit le 3 juin 1764 et le décrivit comme un amas d'étoiles « mêlée d'une faible lumière », suggérant la présence d'une nébuleuse autour de l'amas.William et Caroline Herschel observèrent l'amas en 1783, sans noter la présence de la nébuleuse. L'amas fut ensuite catalogué sous la désignation NGC 6611 par John Dreyer, tandis que la nébuleuse reçut finalement la désignation IC 4703 en 1908.", True),
                    ('annecdotes sur M16:', "M16 est souvent associé à la spectaculaire nébuleuse de l'Aigle, qui l'entoure. Cette nébuleuse mesure environ 70 × 55 années-lumière et constitue une véritable pouponnière stellaire. Plusieurs de ses régions sont des lieux intenses de formation d'étoiles, notamment les célèbres Piliers de la création. Les images du télescope spatial Hubble prises en 1995 ont notamment révélé la nature de pouponnière stellaire de la nébuleuse de l'Aigle. En 2022, le télescope spatial James Webb l'a à son tour photographiée en infrarouge, révélant de nouveaux détails sur cette région.Il existe cependant une importante confusion entre M16 et la nébuleuse de l'Aigle. M16 désigne à proprement parler l'amas ouvert NGC 6611, tandis que la nébuleuse qui l'entoure est IC 4703. Certaines sources attribuent pourtant le nom M16 à l'ensemble, notamment parce que Messier avait observé l'amas accompagné d'une faible lumière nébuleuse. ", True),
                                        ],
                 "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545835026233426000/Eagle_Nebula_from_ESO.jpg?ex=6a9e3f4e&is=6a9cedce&hm=23f9d9dbb75311e80ba231c0214bc0b4c4d3e8d90b3eb7930e4cd20c28aeab97&",
                 "image": 'https://thumb.wikimedia.org/wikipedia/commons/thumb/2/2e/Serpens_Cauda_IAU.svg/960px-Serpens_Cauda_IAU.svg.png?utm_source=fr.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail',
                 "footer": 'l\'image de localisation provient de wikipedia merci a eux'
                                    },
    "m17": {
                 "alias": ["NGC 6618","nébuleuse oméga"],
                 "titre": "M17",
                 "description": "M17 (ou NGC 6618), aussi appelée nébuleuse Oméga, du Cygne, du Fer à Cheval ou le Homard, est une nébuleuse en émission située dans la constellation du Sagittaire, à environ 5 100 à 5 900 années-lumière du Soleil. Elle mesure environ 30 à 34 années-lumière dans sa plus grande dimension et contient environ 800 masses solaires de gaz. Avec une magnitude apparente de 6,0, M17 est tout juste visible à l'œil nu dans des conditions très favorables, mais elle est facilement repérable avec des jumelles.",
                 "champs": [
                    ("découverte de M17", "M17 a été découverte par l'astronome suisse Jean Philippe Loys de Cheseaux en 1745, mais sa découverte fut peu diffusée. Charles Messier la redécouvrit indépendamment le 3 juin 1764 et l'ajouta à son catalogue sous le numéro M17. Plus tard, John Herschel compara sa forme à la lettre grecque oméga (Ω) et à un fer à cheval, donnant naissance à plusieurs de ses surnoms. D'autres observateurs y voient également un cygne ou, dans l'hémisphère sud, un homard.", True),
                    ('annecdotes sur M17:', "M17 est une véritable pouponnière stellaire. La nébuleuse a connu au moins trois phases de formation d'étoiles. La première aurait produit environ 2 000 étoiles il y a entre 2 et 5 millions d'années, puis une deuxième phase aurait donné naissance à environ 12 000 étoiles. Une troisième phase est encore en cours dans les régions externes et concerne environ 1 000 étoiles.Une grande partie des étoiles formées lors de la deuxième phase est cachée derrière les gaz de la nébuleuse et est donc beaucoup plus facile à observer en infrarouge. Certaines étoiles massives de M17 sont particulièrement impressionnantes : plusieurs étoiles de type O possèdent entre 5 et 20 masses solaires, tandis que certaines étoiles détectées en infrarouge dépassent 60 masses solaires. ", True),
                                        ],
                 "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545836547595706459/The_star_formation_region_Messier_17.jpg?ex=6a9e40b9&is=6a9cef39&hm=7737bde19c95754cd80be44b10d736ec18f102793ff4aff31c7691f47e97d79f&",
                 "image": 'https://freestarcharts.com/images/Articles/Messier/Single/M17_Finder_Chart.png',
                 "footer": 'l\'image de localisation provient de freestarscharts merci a eux'
                                    },
    "m18": {
                 "alias": ["NGC 6613"],
                 "titre": "M18",
                 "description": "M18 (ou NGC 6613) est un très jeune amas ouvert situé dans la constellation du Sagittaire, à environ 5 090 années-lumière du Soleil. Il mesure environ 8,9 années-lumière de diamètre et son âge est estimé à environ 16,7 millions d'années. Avec une magnitude apparente de 6,9, M18 est observable avec de petites jumelles. L'amas contient environ 40 étoiles, dont plusieurs sont plus massives que le Soleil. Selon la classification de Robert Trumpler, il contient moins de 50 étoiles, avec une concentration moyenne et un large éventail de luminosités.",
                 "champs": [
                    ("découverte de M18", "M18 a été découvert par l'astronome français Charles Messier avant le 3 juin 1764, date à laquelle il l'ajouta à son catalogue. L'amas fut ensuite identifié sous la désignation NGC 6613. Sa position dans le Sagittaire le place également à proximité de M17, la nébuleuse Oméga.", True),
                    ('annecdotes sur M18:', "M18 contient plusieurs étoiles massives. Une étude de 2005 y avait identifié 29 étoiles de type B ainsi qu'une étoile de type Be, mais les données plus récentes de Gaia EDR3 indiquent seulement 8 étoiles de type B dont la distance est comparable à celle de l'amas. Trois supergéantes de type A ou plus froides sont également présentes. L'étoile la plus brillante de M18 est HD 168352, une étoile de type B2III dont la magnitude apparente est de 8,65.M18 se trouve dans une région particulièrement intéressante du Sagittaire : il est situé à seulement environ 53 minutes d'arc au sud-ouest de M17. Cette proximité permet de retrouver facilement les deux objets dans le ciel, même s'ils sont de natures différentes : M17 est une nébuleuse en émission, tandis que M18 est un amas ouvert. ", True),
                                        ],
                 "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545837434292412426/Eso1628a-crop.png?ex=6a9e418c&is=6a9cf00c&hm=bebd8d105906aeb458f75bbe11cb6c321dd3c4fa3e99805501c4fb595899b319&",
                 "image": 'https://www.universetoday.com/article_images/Messier-18-location-471x580.png',
                 "footer": 'l\'image de localisation provient de universe today merci a eux'
                                    },
    "m19": {
                 "alias": ["NGC 6273"],
                 "titre": "M19",
                 "description": "M19 (ou NGC 6273) est un amas globulaire situé dans la constellation d'Ophiuchus, à environ 28 000 années-lumière du Soleil et à seulement 5 220 années-lumière du centre de la Voie lactée. Il mesure environ 140 années-lumière de diamètre et possède une masse estimée à environ 1,1 million de fois celle du Soleil. Avec une magnitude apparente de 6,8, M19 est observable aux jumelles, où il apparaît comme une tache diffuse. Son âge est estimé à environ 11,9 milliards d'années.",
                 "champs": [
                    ("découverte de M19", "M19 a été découvert par l'astronome français Charles Messier le 5 juin 1764. L'amas fut ensuite étudié par différents astronomes afin de déterminer ses propriétés et sa composition. Il est aujourd'hui également catalogué sous la désignation NGC 6273.", True),
                    ('annecdotes sur M19:', "M19 est un amas globulaire particulièrement aplati, ce qui est inhabituel car la plupart des amas globulaires sont presque sphériques. Son excentricité de 0,27 en fait même l'un des amas globulaires connus présentant le plus fort degré d'aplatissement. Cette forme serait probablement liée aux forces de marée exercées par la Voie lactée, M19 étant relativement proche de son centre.Une étude publiée en 2015 a classé M19 parmi les « amas complexes de fer ». Sa métallicité présente une grande dispersion, avec des valeurs allant de −1,80 à 1,30, ce qui suggère que M19 contient au moins deux populations distinctes d'étoiles.M19 contient également plusieurs étoiles variables. Une étude de 1978 en avait identifié huit, dont trois étoiles RR Lyrae et quatre céphéides de type II, avec des périodes comprises entre 2,4 et 16,9 jours.", True),
                                        ],
                 "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545838547334991974/M19-Cluster.png?ex=6a9e4295&is=6a9cf115&hm=a3251892275d4221cca68f0a43c8efb4f836c521071f97727dfa6441fa9500f9&",
                 "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-19-location.png',
                 "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                    },
    "m20": {
                 "alias": ["NGC 6121","nébuleuse de la trifide"],
                 "titre": "M20",
                 "description": "M20 (ou NGC 6514), aussi appelée nébuleuse Trifide, est une région HII située dans la constellation du Sagittaire, à environ 3 960 années-lumière du Système solaire. Elle se trouve dans une région de formation stellaire du bras du Centaure de la Voie lactée. M20 contient un amas ouvert d'étoiles et compte environ 3 100 étoiles. Avec une magnitude apparente comprise entre 6,8 et 9,0, elle est surtout observable avec un télescope.",
                 "champs": [
                    ("découverte de M20", "M20 a été découverte par l'astronome français Charles Messier le 5 juin 1764, qui l'ajouta à son catalogue. Son nom de « nébuleuse Trifide » vient de son apparence caractéristique divisée en trois lobes par des bandes de nébuleuse sombre. Le nom courant est attribué à John Herschel. La partie sombre responsable de cet aspect a ensuite été cataloguée B 85 par l'astronome américain Edward Barnard. William Herschel lui attribua quant à lui quatre numéros différents dans son catalogue : H IV.41, H V.10, H V.11 et H V.12.", True),
                    ('annecdotes sur M20:', "M20 est particulièrement intéressante car elle combine plusieurs types de nébuleuses. Elle est principalement une nébuleuse en émission, mais ses régions externes forment également une nébuleuse par réflexion. Une nébuleuse obscure traverse la région brillante et forme les trois lobes caractéristiques qui lui donnent son nom. M20 est également une véritable pouponnière stellaire.Au cœur de M20 se trouve le système HD 164492, composé d'au moins trois étoiles, voire quatre. L'étoile principale, HD 164492A, est une étoile massive de type O7.5 III. C'est elle qui fournit le rayonnement nécessaire pour ioniser le gaz et faire briller la nébuleuse. Les composantes B et C sont de type B6 V, tandis qu'une quatrième composante pourrait être une étoile de type Be. ", True),
                                        ],
                 "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545841554793693255/Messier_20_Nebulosa_Trifida_en_LRGB.jpg?ex=6a9e4563&is=6a9cf3e3&hm=6702cac046642700f18d5c466d4e25740674c540b571285736bad2d78b3f7339&",
                 "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-20-location.png',
                 "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                    },
    "m21": {
             "alias": ["NGC 6531"],
             "titre": "M21",
             "description": "M21 (ou NGC 6531) est un très jeune amas ouvert situé dans la constellation du Sagittaire, à environ 3 900 années-lumière du Soleil. Il mesure environ 16,5 années-lumière de diamètre et son âge est estimé à seulement 12 millions d'années. Avec une magnitude apparente de 5,9, M21 est à la limite de la visibilité à l'œil nu, mais il est facilement observable avec de petites jumelles. Selon les estimations, il contient environ 70 étoiles, dont plusieurs étoiles de la séquence principale et des étoiles encore en pré-séquence principale.",
             "champs": [
                ("découverte de M21", "M21 a été découvert par l'astronome français Charles Messier le 5 juin 1764, le même jour où il observa M20, la nébuleuse Trifide. Messier remarqua d'ailleurs la proximité entre les deux objets et indiqua que les étoiles de M21 avaient une magnitude comprise entre 8 et 9. L'amas fut ensuite observé par Johann Elert Bode, William Herschel et John Herschel, qui l'inscrivit dans son catalogue sous la désignation GC 4367. En 1835, Charles Piazzi Smyth l'observa également. Enfin, John Dreyer le catalogua sous la désignation NGC 6531, en le décrivant comme un amas assez riche et peu comprimé.", True),
                ('annecdotes sur M21:', "Selon la classification de Robert Trumpler, M21 appartient à la classe I3m : il possède une forte concentration d'étoiles et celles-ci présentent un large intervalle de luminosités. Cette classification indique également que l'amas contient entre 50 et 100 étoiles.M21 est particulièrement intéressant à observer car il se trouve juste à côté de la nébuleuse Trifide (M20). Les deux objets sont séparés de seulement 0,4°, ce qui permet de les observer ensemble avec un télescope à grand champ. La nébuleuse de la Lagune (M8) se trouve également dans la même région, à environ 2° au sud de M21.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545875865454510100/image.png?ex=6aa05f97&is=6a9f0e17&hm=985a690c6e8b5dc61a4aa590e83ada91ecd022f991fab6ad88966a1637f48a42&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-21-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m22": {
             "alias": ["NGC 6656"],
             "titre": "M22",
             "description": "M22 (ou NGC 6656) est un amas globulaire situé dans la constellation du Sagittaire, à environ 10 450 années-lumière du Soleil, ce qui en fait l'un des plus proches de la Terre. Il possède une masse estimée à environ 644 000 fois celle du Soleil et son âge est estimé à environ 12,67 milliards d'années. Avec une magnitude apparente de 5,1, M22 est facilement visible à l'œil nu dans de bonnes conditions et fait partie des quatre amas globulaires les plus brillants du ciel. Son diamètre apparent atteint environ 32 minutes d'arc, légèrement supérieur à celui de la Lune.",
             "champs": [
                ("découverte de M22", "M22 a été découvert par l'astronome allemand Johann Abraham Ihle le 26 août 1665, alors qu'il tentait d'observer Saturne. L'amas fut ensuite observé par Edmond Halley en 1715 et Nicolas-Louis de Lacaille en 1752. Charles Messier l'ajouta à son catalogue le 5 juin 1764, en le décrivant encore comme une nébuleuse. Le 4 juillet 1783, William Herschel parvint à résoudre M22 en étoiles et confirma ainsi sa véritable nature d'amas globulaire.", True),
                ('annecdotes sur M22:', "M22 possède une population particulièrement riche en étoiles variables. Des études ont identifié de nombreuses variables appartenant à l'amas, des binaires à contact et des binaires à éclipses. L'amas contient également au moins deux pulsars millisecondes, dont l'un est un pulsar binaire.M22 pourrait également abriter plusieurs trous noirs. En 2012, des astronomes ont proposé que deux sources radio puissent correspondre à des trous noirs de 10 à 20 masses solaires. Selon cette étude, l'amas pourrait même contenir entre 5 et 100 trous noirs.M22 possède aussi une particularité extrêmement rare : une nébuleuse planétaire, appelée IRAS 18333−2357. Elle ne serait âgée que d'environ 6 000 ans et est illuminée par une étoile dont la température atteint environ 50 000 K. Il s'agit de l'une des seulement quatre nébuleuses planétaires connues dans un amas globulaire de la Voie lactée.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545879081478783057/M22HunterWilson.jpg?ex=6aa06296&is=6a9f1116&hm=21cef563620a51ee386ddf31677552a45d830440488a8ada4fe00daa11dc2344&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-22-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m23": {
             "alias": ["NGC 6494"],
             "titre": "M23",
             "description": "M23 (ou NGC 6494) est un amas ouvert situé dans la constellation du Sagittaire, à environ 2 390 années-lumière du Soleil. Il mesure environ 18,8 années-lumière de diamètre et son âge est estimé à environ 300 millions d'années. Avec une magnitude apparente de 5,5, M23 est facilement observable avec de petites jumelles. Selon les estimations, il contient entre 50 et 100 étoiles, voire environ 150 étoiles selon le catalogue Lynga.",
             "champs": [
                ("découverte de M23", "M23 a été découvert par l'astronome français Charles Messier le 20 juin 1764. Il le décrivit alors comme un amas d'environ 15 minutes d'arc de diamètre, dont les étoiles étaient très rapprochées. L'amas fut ensuite observé par Johann Elert Bode et Caroline Herschel en 1783, puis par William Herschel en 1784. John Herschel l'observa à plusieurs reprises entre 1826 et 1830 et le catalogua sous la désignation GC 4346. Enfin, John Dreyer l'intégra au New General Catalogue sous le nom NGC 6494.", True),
                ('annecdotes sur M23:', "Les différentes classifications de M23 donnent une idée de sa structure. Selon Robert Trumpler, il contient entre 50 et 100 étoiles, avec une concentration moyennement faible et des étoiles dont les luminosités sont assez proches. Le catalogue Lynga estime toutefois qu'il contient environ 150 étoiles et le classe différemment, comme un amas plus concentré et riche.Les données du satellite Gaia permettent d'identifier probablement 29 étoiles membres de M23 grâce à leur distance et à leur mouvement propre. Parmi les étoiles de l'amas, on trouve six étoiles de type B et aucune étoile de type O. M23 contient également au moins deux traînardes bleues, des étoiles qui paraissent plus jeunes et plus chaudes que ce que leur environnement stellaire laisse normalement attendre.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545879860730396682/M23_Open_Star_Cluster.png?ex=6aa10c0f&is=6a9fba8f&hm=77f7346ad63d6bc8e3e13f77d42aa2aa2d0932bef007e1a99496bc9304ce618c&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-23-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m24": {
             "alias": ["nuage du sagittaire"],
             "titre": "M24",
             "description": "M24 (aussi appelé nuage du Sagittaire) est un vaste nuage galactique situé dans la constellation du Sagittaire, à environ 10 000 années-lumière de la Terre. Contrairement à ce que son nom de catalogue pourrait laisser penser, M24 n'est pas un véritable amas d'étoiles : il s'agit d'une importante concentration d'étoiles et de gaz interstellaire située dans la Voie lactée. Il s'étend sur environ 600 années-lumière de large et présente une magnitude apparente de 4,6, ce qui le rend facilement visible à l'œil nu sous un ciel suffisamment sombre.",
             "champs": [
                ("découverte de M24", "M24 a été découvert par l'astronome français Charles Messier le 20 juin 1764. Il le décrivit comme une « large nébulosité dans laquelle se trouvent de nombreuses étoiles de différentes magnitudes ». Messier l'intégra ainsi à son catalogue, bien qu'il ne s'agisse pas réellement d'un objet individuel situé à une distance précise comme un amas ou une nébuleuse.", True),
                ('annecdotes sur M24:', "M24 est un objet assez particulier du catalogue de Messier : il ne correspond pas à un véritable objet céleste compact, mais à une fenêtre à travers les régions poussiéreuses de la Voie lactée, donnant l'impression d'une immense concentration d'étoiles. C'est pour cette raison qu'il est parfois considéré comme une erreur du catalogue de Messier, au même titre que M40 et M73.À l'intérieur de M24 se trouvent plusieurs véritables objets célestes. On y trouve notamment l'amas ouvert NGC 6603, parfois désigné à tort comme M24, ainsi que l'amas Markarian 38. Deux nébuleuses obscures, B92 et B93, se trouvent également dans cette région. Elles seraient situées au premier plan, dans le bras du Sagittaire-Carène, à environ 7 000 années-lumière.M24 possède une profondeur considérable : la région observée s'étend sur environ 10 000 à 16 000 années-lumière. Elle constitue surtout une concentration spectaculaire d'étoiles visibles depuis la Terre.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545880399119654942/Caustiche.jpg?ex=6aa10c90&is=6a9fbb10&hm=7aabda319bc9bb76f995a846f36a9d182328a0eb0323df941df4073e956d85d1&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-24-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m25": {
             "alias": ["ic 4725"],
             "titre": "M25",
             "description": "M25 (ou IC 4725) est un amas ouvert situé dans la constellation du Sagittaire, à environ 2 165 années-lumière du Système solaire. Il mesure environ 23 années-lumière de diamètre et possède une magnitude apparente de 4,6, ce qui le rend facilement visible à l'œil nu dans de bonnes conditions et très facile à observer avec de petites jumelles. Il contient au moins 86 étoiles. Son diamètre apparent atteint environ 40 minutes d'arc, soit une région du ciel plus grande que la pleine Lune.",
             "champs": [
                ("découverte de M25", "M25 a été découvert par l'astronome suisse Jean Philippe Loys de Cheseaux en 1745. Charles Messier l'inclut ensuite dans son catalogue en 1764. L'amas est également connu sous la désignation IC 4725.", True),
                ('annecdotes sur M25:', "M25 contient au moins 86 étoiles, parmi lesquelles se trouvent deux étoiles géantes de type G. Deux autres géantes de type M sont visibles dans la même région, mais elles ne font en réalité pas partie de l'amas : elles se trouvent simplement sur la même ligne de visée, donnant une impression de proximité.M25 abrite également une céphéide variable, appelée U Sagittarii. Découverte en 1956, cette étoile possède une période de variation de 6,74 jours. Les céphéides sont des étoiles dont la luminosité varie périodiquement. ", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545882069828243456/Messier-25-1024x1024.jpg?ex=6aa10e1e&is=6a9fbc9e&hm=42752f4339bca22171481521ac792f3f7abcce24d4a1f8eb8e319f8b4039e6c0&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-25-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m26": {
             "alias": ["NGC 6694"],
             "titre": "M26",
             "description": "M26 (ou NGC 6694) est un amas ouvert situé dans la constellation de l'Écu de Sobieski, à environ 5 460 années-lumière du Système solaire. Il mesure environ 11,9 années-lumière de diamètre, son âge est estimé à environ 100 millions d'années, avec une incertitude de +44/−31 millions d'années et possède une masse estimée à environ 1 208 masses solaires . Avec une magnitude apparente de 8,87, M26 n'est pas visible à l'œil nu, mais peut être observé avec des jumelles de 60 à 70 mm ou un petit télescope.",
             "champs": [
                ("découverte de M26", "M26 a été découvert par l'astronome français Charles Messier avant le 20 juin 1764. Messier nota qu'il n'était pas discernable dans une lunette de 3,5 pieds. L'amas fut ensuite observé par Johann Elert Bode et William Herschel. Bode le décrivit comme un amas accompagné d'une nébuleuse, tandis que Herschel le considéra comme un amas d'étoiles dispersées et peu riche. John Herschel l'observa le 27 mai 1835 et l'inscrivit dans son catalogue sous la désignation GC 4432. Enfin, John Dreyer le catalogua sous le nom NGC 6694.", True),
                ('annecdotes sur M26:', "M26 est un amas relativement compact, mais les estimations de son nombre d'étoiles varient fortement selon les sources. La classification de Trumpler le place entre I1m et II3m, tandis que les différentes estimations donnent entre 30 et 100 étoiles.M26 possède une particularité assez inhabituelle : une zone de faible densité stellaire d'environ 3,1 minutes d'arc autour de son centre. Cette sorte de « trou » pourrait toutefois ne pas être réel : selon James Cuffey, il pourrait être provoqué par de la matière interstellaire située entre nous et l'amas, qui masquerait certaines étoiles.L'amas contient également au moins une traînarde bleue (blue straggler), une étoile qui présente des caractéristiques semblant la rendre plus jeune et plus chaude que les autres étoiles de son environnement. ", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545884530827858000/Messier_26_Cluster.png?ex=6aa11069&is=6a9fbee9&hm=772db0803f03af5ec29c8814a6f6147dc1dabf4063533c35876418f45bdc66bb&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-26-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m27": {
             "alias": ["NGC 6853","nébuleuse de l'haltère"],
             "titre": "M27",
             "description": "M27 (ou NGC 6853), la nébuleuse de l'Haltère, est une nébuleuse planétaire située dans la constellation du Petit Renard, à environ 1 250 années-lumière du Système solaire. Elle mesure environ 2,43 années-lumière de diamètre pour sa partie principale, tandis que son faible halo s'étend jusqu'à environ 5,4 années-lumière. Avec une magnitude apparente de 7,4, M27 n'est pas visible à l'œil nu, mais peut être observée aux jumelles dans de bonnes conditions. Son âge est estimé entre 10 000 et 25 290 ans selon les études. Sa température varie d'environ 6 000 à 10 000 K, tandis que sa densité atteint environ 20 000 ions par cm³.",
             "champs": [
                ("découverte de M27", "M27 a été découverte par l'astronome français Charles Messier dans la nuit du 12 juillet 1764. Il la décrivit comme une nébuleuse ovale sans étoile. William Herschel étudia à son tour sa structure et émit dès 1784 l'hypothèse qu'elle pouvait provenir d'une double couche d'étoiles très étendue. Entre 1828 et 1830, John Herschel observa M27 à plusieurs reprises et la décrivit comme une nébuleuse en forme d'haltère, origine de son surnom. La classification définitive comme nébuleuse planétaire fut réalisée dans les années 1910. ", True),
                ('annecdotes sur M27:', "Sa forme est celle d'un ellipsoïde allongé, avec une région centrale brillante en forme d'haltère entourée d'une enveloppe beaucoup plus faible qui possède elle-même un halo qui porte l'étendue totale de la nébuleuse jusqu'à environ 15 minutes d'arc dans le ciel. Sa structure contient également des nœuds et des régions sombres et brillantes liées à la photo-ionisation.Au centre de M27 se trouve une naine blanche extrêmement chaude. Sa température de surface est estimée à environ 136 000 ± 10 000 K. Elle possède une magnitude apparente d'environ 14,09. M27 abrite également un système stellaire triple : deux étoiles compagnes ont été identifiées autour de la naine blanche, l'une de type K et l'autre de type M.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1545886838651101265/M27_-_Dumbbell_Nebula.jpg?ex=6aa1128f&is=6a9fc10f&hm=5d5287846f02e0a663d53ae950da37768012d218c5c2e7dfc4c8b2494565e713&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-27-location.webp',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m28": {
             "alias": ["NGC 6626"],
             "titre": "M28",
             "description": "M28 (ou NGC 6626) est un amas globulaire situé dans la constellation du Sagittaire, à environ 17 950 années-lumière du Soleil et 8 800 années-lumière du centre de la Voie lactée. Il mesure environ 13,8 minutes d'arc dans le ciel et possède une masse estimée à environ 551 000 fois celle du Soleil. Avec une magnitude apparente de 6,79, M28 est faiblement visible aux jumelles sous la forme d'une tache floue. Son âge est estimé à environ 12 milliards d'années.",
             "champs": [
                ("découverte de M28", "M28 a été découvert par l'astronome français Charles Messier le 27 juillet 1764, mais Messier le décrivit comme une nébuleuse sans étoiles. Les astronomes Johann Elert Bode et Johann Gottfried Koehler firent également cette erreur. En 1799, William Herschel fut le premier à comprendre qu'il s'agissait d'un amas riche en étoiles. À partir de 1826, John Herschel observa M28 à plusieurs reprises et le décrivit comme un amas très brillant et de plus en plus dense vers son centre. En 1836, William Henry Smyth l'observa également. Enfin, John Dreyer l'intégra au New General Catalogue sous la désignation NGC 6626.", True),
                ('annecdotes sur M28:', "M28 possède une importante population d'étoiles variables. En 2014, 22 étoiles variables de type RR Lyrae avaient été identifiées, ainsi que 10 autres étoiles variables. Certaines de ces étoiles possèdent des périodes très courtes, de seulement quelques dizaines de secondes.Mais la particularité la plus remarquable de M28 est probablement sa population de pulsars. Le PSR 1821−24, découvert en 1987, fut le premier pulsar découvert dans un amas globulaire. En 2022, on connaissait au total 14 pulsars dans M28, dont 13 pulsars millisecondes et un pulsar ayant une période de 79,83 millisecondes. Ces objets sont associés à des étoiles à neutrons.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546142014465249290/Nebulous_but_no_nebula_Messier_28.jpg?ex=6aa15776&is=6aa005f6&hm=0b257b37d73485cafd202f5f0dee8f07b3c25a9b12307a4fd03540d6cf693002&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-28-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m29": {
             "alias": ["NGC 6913"],
             "titre": "M29",
             "description": "M29 (ou NGC 6913) est un amas ouvert situé dans la constellation du Cygne, à environ 5 340 années-lumière du Système solaire. Il mesure environ 15,5 années-lumière de diamètre et son âge est estimé entre 4,5 et 12,9 millions d'années selon les études. Avec une magnitude apparente de 6,6, M29 est visible avec de petites jumelles. Sa masse est estimée à environ 903 masses solaires et les estimations modernes lui attribuent environ 170 étoiles.",
             "champs": [
                ("découverte de M29", "M29 a été découvert par l'astronome français Charles Messier en 1764, qui le décrivit comme un amas de sept ou huit petites étoiles situé près de Gamma Cygni. L'amas avait toutefois déjà été redécouvert par Johann Elert Bode en 1744 et par Caroline Herschel en 1783. Il fut ensuite observé par William Herschel, John Herschel et William Henry Smyth. John Herschel l'inscrivit dans son catalogue sous la désignation GC 4567, avant que John Dreyer ne le répertorie dans le New General Catalogue sous le nom NGC 6913.", True),
                ('annecdotes sur M29:', "M29 est un amas très jeune. Les différentes études donnent des âges allant de seulement 4,5 millions d'années jusqu'à 12,9 millions d'années, avec une estimation récente de 7,7 ± 0,7 millions d'années. Il s'est donc formé très récemment à l'échelle astronomique.Le nombre d'étoiles de M29 varie fortement selon les méthodes utilisées. La classification de Robert Trumpler lui attribue moins de 50 étoiles, tandis que le catalogue Lynga en estime environ 50 à 100. Les estimations modernes donnent cependant environ 170 étoiles.Dans le ciel, les huit étoiles les plus brillantes de la région forment une figure assez caractéristique : un quadrilatère, avec une extension vers le nord-ouest, surmonté d'un triangle. Cette configuration aide à reconnaître l'amas.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546142869260345566/M29s.jpg?ex=6aa15841&is=6aa006c1&hm=4d44d0119013981b41866cc08933648c5a5f5a8d18d546f7d63a8f97e20afc8f&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-29-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m30": {
             "alias": ["NGC 7099"],
             "titre": "M30",
             "description": "M30 (ou NGC 7099) est un amas globulaire situé dans la constellation du Capricorne, à environ 26 400 années-lumière du Soleil et 23 160 années-lumière du centre de la Voie lactée. Il mesure environ 92 années-lumière de diamètre et possède une masse estimée à environ 241 000 fois celle du Soleil. Avec une magnitude apparente d'environ 7,1, M30 est facilement observable avec de petites jumelles. Son âge est estimé à environ 12,93 milliards d'années.",
             "champs": [
                ("découverte de M30", "M30 a été découvert par l'astronome français Charles Messier le 3 septembre 1764. Il le décrivit comme une nébuleuse ronde et sans étoiles, située près de l'étoile 41 Capricorni. C'est William Herschel, vers 1784, qui révéla sa véritable nature en parvenant à résoudre ses étoiles. John Herschel observa ensuite M30 en 1830 et le décrivit comme un amas légèrement allongé, avec deux lignes d'étoiles s'étendant vers le nord. Enfin, John Dreyer l'intégra au New General Catalogue sous la désignation NGC 7099.", True),
                ('annecdotes sur M30:', "M30 a connu un phénomène appelé effondrement gravitationnel du cœur, qui a fortement concentré les étoiles dans sa région centrale, d'où son noyau très dense. Son noyau ne mesure qu'environ 0,12 minute d'arc, soit moins d'une année-lumière de diamètre. La moitié de la masse de l'amas se trouve dans un diamètre d'environ 17,4 années-lumière.M30 possède une population intéressante d'étoiles. Une étude a notamment identifié 1 218 étoiles de la séquence principale, 185 géantes rouges, 47 traînardes bleues, 41 étoiles de la branche horizontale et 78 sources bleues constituées notamment de naines blanches. M30 contient également 17 étoiles variables identifiées en 2014, 4 étoiles de type W Ursae Majoris, 2 SX Phoenicis, une variable éruptive, une binaire à éclipses et aussi deux pulsars millisecondes. Ils tournent extrêmement rapidement : l'un possède une période de seulement 11 millisecondes, tandis que l'autre a une période de 13 millisecondes et suit une orbite très elliptique.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546147851032072242/Messier_30_Hubble_WikiSky.jpg?ex=6aa15ce5&is=6aa00b65&hm=652ba9274956036b4b76bfcf2095f308f1d38690169aafc83851dd415faaa737&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-30-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m31": {
             "alias": ["NGC 224","galaxie d'andromède"],
             "titre": "M31",
             "description": "M31 (ou NGC 224), appelée galaxie d'Andromède, est une galaxie spirale située dans la constellation d'Andromède, à environ 2,54 millions d'années-lumière du Soleil. Elle mesure environ 220 000 années-lumière de diamètre et contiendrait environ 1 000 milliards d'étoiles. Avec une magnitude apparente de 3,4, M31 est l'une des rares galaxies visibles à l'œil nu depuis l'hémisphère nord avec un diamètre apparent est gigantesque : environ 3,18°, soit plus de six fois le diamètre apparent de la pleine Lune. Elle est également le plus grand membre du Groupe local de galaxies et la plus proche de la Voie lactée. Elle contient environ deux à cinq fois plus d'étoiles que notre galaxie. Une étude publiée en 2025 a proposé une masse totale d'environ 450 milliards de masses solaires.",
             "champs": [
                ("découverte de M31", "La première mention écrite connue de M31 remonte à 964, lorsque l'astronome perse Abd al-Rahman al-Soufi la décrit dans son Livre des étoiles fixes. La première observation au télescope est réalisée par Simon Marius en 1612. Elle est ensuite photographiée pour la première fois en 1887 par Isaac Roberts. Pendant longtemps, M31 est considérée comme une simple nébuleuse, appelée « grande nébuleuse d'Andromède ». Dans les années 1920, Edwin Hubble identifie des étoiles céphéides dans celle-ci. Grâce à la relation période-luminositén il a été démontré que M31 est en réalité une galaxie extérieure à la Voie lactée.", True),
                ('annecdotes sur M31:', "Son cœur possède une structure étonnante : il contient deux concentrations stellaires, appelées P1 et P2, séparées d'environ 4,9 années-lumière. P2 correspond au véritable centre de la galaxie et abrite M31*, un trou noir supermassif dont la masse est estimée à environ 140 millions de masses solaires selon une étude.M31 possède également une structure complexe de bras spiraux et d'anneaux de poussière. Un anneau situé à environ 33 000 années-lumière du centre concentre une grande partie de la poussière et du gaz de la galaxie. Un autre anneau, plus intérieur, serait lié à la collision de M32 avec Andromède il y a environ 210 millions d'années. M31 possède enfin une importante population de galaxies satellites : environ une vingtaine de galaxies naines orbiteraient autour d'elle. Parmi les plus connues figurent M32 et M110. Elle possède également environ 460 amas globulaires ; le plus massif, Mayall II (G1), contient plusieurs millions d'étoiles et est le plus brillant du Groupe local.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546150818946748548/M31_the_Andromeda_Galaxy_Killarney_Provincial_Park_Observatory.jpg?ex=6aa402a9&is=6aa2b129&hm=226fe51a0a8eb2882d138e9d8acf37db7dadae58c3e2ecc2ed354f9c2cf7819b&",
             "image": 'https://www.cosmodixi.fr/ciel/cartes/andromede.webp',
             "footer": 'l\'image de localisation provient de cosmodixi merci a eux'
                                },
    "m32": {
             "alias": ["NGC 221"],
             "titre": "M32",
             "description": "M32 (ou NGC 221) est une galaxie elliptique compacte de type cE2, située dans la constellation d'Andromède, à environ 2,5 millions d'années-lumière du Soleil. Elle est une galaxie satellite de la galaxie d'Andromède et appartient au Groupe local. Avec une longueur maximale d'environ 8 000 années-lumière, M32 est une galaxie de petite taille. Sa magnitude apparente est de 7,07. Son âge moyen est estimé à environ 6,8 milliards d'années au centre et 9,2 milliards d'années en périphérie, ce qui semble indiquer que la formation stellaire s'est progressivement déplacée du centre vers l'extérieur.",
             "champs": [
                ("découverte de M32", "M32 a été découverte par l'astronome français Guillaume Le Gentil. Elle est aujourd'hui également connue sous les désignations NGC 221, PGC 2555 et UGC 452. Sa nature de galaxie elliptique compacte de type cE2 a notamment été utilisée dans la classification morphologique de Gérard de Vaucouleurs.", True),
                ('annecdotes sur M32:', "M32 est une galaxie elliptique particulière car elle est très pauvre en gaz et en poussières interstellaires. Elle est principalement constituée d'étoiles naines jaunes et rouges âgées et n'a pas connu d'activité importante de formation d'étoiles depuis longtemps. Sa forme actuelle pourrait être liée à son interaction gravitationnelle avec Andromède. Selon une hypothèse, M32 aurait autrefois été une petite galaxie spirale qui aurait traversé le disque d'Andromède. Elle aurait alors perdu une grande partie de sa matière périphérique, ne conservant principalement que son bulbe galactique.M32 pourrait également abriter un trou noir supermassif en son centre. Une étude menée sur 76 galaxies estime sa masse à environ 2,5 millions de masses solaires.Enfin, M32 est particulièrement intéressante à observer en raison de sa proximité apparente avec la galaxie d'Andromède : elle apparaît devant celle-ci dans le ciel, ce qui permet de voir directement deux galaxies appartenant au même environnement galactique.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546151886367891556/NGC_0221_DSS.png?ex=6aa403a7&is=6aa2b227&hm=d2bab9e42b1cfb2fd6734a640fb2e512b87a44c247aa629bf764a9f9d2194651&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-32-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m33": {
             "alias": ["NGC 598","galaxie du triangle"],
             "titre": "M33",
             "description": "M33 (ou NGC 598, aussi appelée galaxie du Triangle) est une galaxie spirale de type SA(s)cd située dans la constellation du Triangle, à une distance estimée entre environ 2,38 et 3,14 millions d'années-lumière du Soleil. Elle appartient au Groupe local et pourrait être un satellite de la galaxie d'Andromède. Sa masse est estimée à environ 60 milliards de masses solaires, dont la matière noire représenterait près de 85 %. C'est alors la troisième galaxie la plus massive du Groupe local, après la galaxie d'Andromède et la Voie lactée. Son diamètre est estimé entre 50 000 et 60 000 années-lumière. Avec une magnitude apparente de 6,27, M33 peut être visible à l'œil nu lorsque les conditions d'observation sont excellentes.",
             "champs": [
                ("découverte de M33:", "M33 aurait probablement été découverte avant 1654 par l'astronome italien Giovanni Battista Hodierna, qui l'aurait peut-être confondue avec l'amas ouvert NGC 752. Elle fut redécouverte par Charles Messier le 25 août 1764, qui l'ajouta à son catalogue sous le numéro M33. John Charles Duncan en 1922 et Max Wolf en 1923 y détectèrent des étoiles variables dans la galaxie. Edwin Hubble étudia ensuite de nombreuses photographies et identifia 45 étoiles variables, dont 35 céphéides. Ces observations contribuèrent à démontrer que M33 était une galaxie extérieure à la Voie lactée.", True),
                ('annecdotes sur M33:', "M33 est une galaxie spirale particulière car elle ne possède pas de bulbe galactique visible autour de son noyau. Elle possède des bras spiraux ouverts et n'est officiellement pas considérée comme barrée ni comme une galaxie à anneau. Elle est une galaxie où la formation d'étoiles est très active. Environ 10 % de son gaz interstellaire se trouve sous forme moléculaire, notamment dans des nuages moléculaires géants qui constituent les sites de naissance des étoiles. Son taux de formation stellaire est estimé à environ 0,45 masse solaire par an, soit 4,6 fois plus élevé par unité de volume que celui d'Andromède. Son cœur contient une source de rayons X extrêmement puissante appelée M33 X-8. Avec une puissance d'environ 1,2 × 10³² W, elle constitue la source de rayons X la plus puissante du Groupe local. Elle serait associée à un trou noir d'au moins 10 masses solaires en orbite autour d'une étoile massive et non un trou noir supermassif.M33 possède plusieurs immenses régions H II, où de nouvelles étoiles se forment. La plus remarquable est NGC 604, qui s'étend sur près de 1 500 années-lumière. Il s'agit de la seconde région H II la plus lumineuse du Groupe local, avec une luminosité d'environ 45 millions de fois celle du Soleil. La galaxie contient également environ 54 amas globulaires confirmés, mais leur nombre réel pourrait dépasser 120. Elle abrite aussi un système particulièrement intéressant, M33 X-7, une binaire X contenant un trou noir d'environ 15,7 masses solaires. ", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546160648784711770/M33-Galaxie-du-Triangle-07-10-2023-Hamois.jpg?ex=6aa40bd0&is=6aa2ba50&hm=32180c37c8a384cf040575bc95d94991f7c54d1b175af9f5dcd53f479e2b385c&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-33-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m34": {
             "alias": ["NGC 1039"],
             "titre": "M34",
             "description": "M34 (ou NGC 1039) est un amas ouvert situé dans la constellation de Persée, à environ 1 630 années-lumière du Système solaire. Il mesure environ 12 années-lumière de diamètre et son âge est estimé à environ 177 millions d'années, ses étoiles se sont donc formées relativement récemment. Avec une magnitude apparente de 5,2, M34 est facilement observable avec de petites jumelles. Il contient environ une centaine d'étoiles, dont la plus brillante possède une magnitude apparente de 7,9.",
             "champs": [
                ("découverte de M34", "M34 a été découvert par l'astronome italien Giovanni Battista Hodierna, à une date inconnue mais certainement avant 1654, puisqu'il figurait dans son catalogue publié cette année-là. L'amas fut ensuite observé par Charles Messier le 25 août 1764, qui l'ajouta à son catalogue sous le numéro M34. Il fut finalement catalogué sous la désignation NGC 1039.", True),
                ('annecdotes sur M34:', "selon la classification de Robert Trumpler, M34 appartient à la classe II3m. Cela signifie qu'il contient entre 50 et 100 étoiles, que leur concentration est moyenne et que leurs luminosités couvrent un large intervalle. M34 possède un diamètre apparent d'environ 25 minutes d'arc. Malgré sa distance d'environ 1 630 années-lumière, cela correspond à un diamètre réel d'environ 12 années-lumière.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546164117998669874/NGC_1039_PanS.jpg?ex=6aa40f0c&is=6aa2bd8c&hm=2787d402af07ac7f08d4637dfe1326b13b58206a160d1d7dbd4ebc85c595f660&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-34-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m35": {
             "alias": ["NGC 2168"],
             "titre": "M35",
             "description": "M35 (ou NGC 2168) est un amas ouvert situé dans la constellation des Gémeaux, à environ 2 660 années-lumière du Système solaire. Il mesure environ 19,4 années-lumière de diamètre et son âge est estimé à environ 95,3 millions d'années. Avec une magnitude apparente de 5,1, M35 peut être visible à l'œil nu dans de très bonnes conditions. Il contient entre 50 et 100 étoiles selon la classification de Robert Trumpler.",
             "champs": [
                ("découverte de M35", "M35 a été découvert par l'astronome suisse Jean Philippe Loys de Cheseaux en 1745. Charles Messier l'observa ensuite le 30 août 1764 et l'ajouta à son catalogue sous le numéro M35.", True),
                ('annecdotes sur M35:', "Selon la classification de Robert Trumpler, il appartient à la classe III2m : sa concentration est moyennement faible et ses étoiles présentent un intervalle de luminosités moyen.M35 possède un diamètre apparent d'environ 25 minutes d'arc, ce qui correspond à une taille réelle d'environ 19,4 années-lumière. Sa centaine d'étoiles s'étend donc sur une région relativement vaste de la Voie lactée.M35 est également intéressant car il se trouve dans la même région du ciel que NGC 2158, un autre amas ouvert. Celui-ci est beaucoup plus dense, ancien et éloigné, à environ 16 500 années-lumière. Les deux amas peuvent ainsi être observés ensemble avec un télescope de faible puissance.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546191991262679170/Messier-35.jpg?ex=6aa42901&is=6aa2d781&hm=66dfd25c137d644d151a756d6f3cf7cf01fe8ac7b25544e334ce139c21230fcd&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-35-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m36": {
             "alias": ["NGC 1960"],
             "titre": "M36",
             "description": "M36 (ou NGC 1960) est un jeune amas ouvert situé dans la constellation du Cocher, à environ 4 300 années-lumière du Système solaire. Il mesure environ 12,5 années-lumière de diamètre et son âge est estimé à environ 29,4 millions d'années. Avec une magnitude apparente de 6,0, M36 est observable avec de petites jumelles. Selon la classification de Robert Trumpler, il contient entre 50 et 100 étoiles.",
             "champs": [
                ("découverte de M36", "M36 a été découvert par l'astronome sicilien Giovanni Battista Hodierna avant 1654. Il fut ensuite redécouvert indépendamment par Guillaume Le Gentil en 1749, puis par Charles Messier le 2 septembre 1764, qui l'intégra à son catalogue sous le numéro M36. L'amas est également catalogué sous la désignation NGC 1960.", True),
                ('annecdotes sur M36:', "Selon la classification de Robert Trumpler, M36 appartient à la classe II3m. Cela signifie que sa concentration d'étoiles est moyenne, que ses étoiles présentent un large intervalle de luminosités et qu'il contient entre 50 et 100 étoiles.M36 possède un diamètre apparent d'environ 10 minutes d'arc. Malgré sa distance d'environ 4 300 années-lumière, cela correspond à une taille réelle d'environ 12,5 années-lumière.Il fait partie d'une région du Cocher particulièrement riche en amas ouverts, aux côtés notamment de M37 et M38.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546192466221342830/M36a.jpg?ex=6aa42972&is=6aa2d7f2&hm=dc9a3601da28edd6081dc3db2422ec92cd5445d290f2016c7f981d1d0325a433&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-36-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m37": {
             "alias": ["NGC 2099"],
             "titre": "M37",
             "description": "M37 (ou NGC 2099) est un amas ouvert situé dans la constellation du Cocher, à environ 4 510 années-lumière du Système solaire. Il mesure environ 19,7 années-lumière de diamètre et son âge est estimé à environ 347 millions d'années. Avec une magnitude apparente de 5,6, M37 peut être visible à l'œil nu dans d'excellentes conditions. Il contient plus de 100 étoiles selon la classification de Robert Trumpler.",
             "champs": [
                ("découverte de M37", "M37 a été découvert par l'astronome sicilien Giovanni Battista Hodierna avant 1654. Charles Messier le découvrit indépendamment en 1764 et l'intégra à son catalogue. L'amas est également connu sous la désignation NGC 2099.", True),
                ('annecdotes sur M37:', "M37 est un amas relativement ancien pour un amas ouvert : son âge d'environ 347 millions d'années est nettement supérieur à celui de plusieurs autres amas ouverts du catalogue de Messier.Selon la classification de Robert Trumpler, M37 appartient à la classe II1r. Cela signifie qu'il possède une concentration moyenne, que ses étoiles présentent un faible intervalle de luminosités et qu'il contient plus de 100 étoiles.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546193002425491466/Messier-37.jpg?ex=6aa429f2&is=6aa2d872&hm=8069a358a86a6c05c1eaf38fe0690e507e97b5d53d090e0f3eb0478938175d20&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-37-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m38": {
             "alias": ["NGC 1912"],
             "titre": "M38",
             "description": "M38 (ou NGC 1912) est un amas ouvert situé dans la constellation du Cocher, à environ 3 480 années-lumière du Système solaire. Il mesure environ 15,2 années-lumière de diamètre et son âge est estimé à environ 290 millions d'années. Avec une magnitude apparente de 6,4, M38 est observable avec de petites jumelles. Selon la classification de Robert Trumpler, il contient entre 50 et 100 étoiles.",
             "champs": [
                ("découverte de M38", "M38 a été découvert par l'astronome sicilien Giovanni Battista Hodierna avant 1654. Il fut ensuite redécouvert indépendamment par Guillaume Le Gentil en 1749, puis par Charles Messier le 25 septembre 1764, qui l'intégra à son catalogue. L'amas est également connu sous la désignation NGC 1912.", True),
                ('annecdotes sur M38:', "Selon la classification de Robert Trumpler, M38 appartient à la classe III2m. Cela signifie que sa concentration d'étoiles est moyennement faible, que les étoiles présentent un intervalle moyen de luminosités et que l'amas contient entre 50 et 100 étoiles.M38 possède un diamètre apparent d'environ 15 minutes d'arc, ce qui correspond à une taille réelle d'environ 15,2 années-lumière.Enfin, avec une magnitude de 6,4, M38 est observable avec de petites jumelles. Il se trouve dans la même région du Cocher que M36 et M37, formant ainsi un trio d'amas ouverts particulièrement intéressant à observer. M38 est également entouré d'une importante région HII, c'est-à-dire une région de gaz ionisé où se produisent des phénomènes liés à la formation d'étoiles.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546193586335387869/d8a647_fcb487eccc2347e7b011458b763757fbmv2.avif?ex=6aa42a7d&is=6aa2d8fd&hm=806bf4a528ed40ca6c4937e4b6eb16c385db76290cc6e70367d5cb3c484964be&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/04/Messier-38-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m39": {
             "alias": ["NGC 7092"],
             "titre": "M39",
             "description": "M39 (ou NGC 7092) est un amas ouvert situé dans la constellation du Cygne, à environ 1 070 années-lumière du Système solaire. Il mesure environ 9,6 années-lumière de diamètre et son âge est estimé à environ 453 millions d'années, avec une incertitude importante. Avec une magnitude apparente de 4,6, M39 est tout juste visible à l'œil nu et facilement observable avec de petites jumelles. Les observations du satellite Gaia ont permis d'estimer qu'il contient environ 248 étoiles.",
             "champs": [
                ("découverte de M39", "M39 a été découvert par l'astronome français Charles Messier le 24 octobre 1764, qui le décrivit comme un amas très grand et très dispersé. Certaines sources attribuent sa découverte à Guillaume Le Gentil, mais cette identification est considérée comme très douteuse. L'amas fut ensuite observé par Johann Elert Bode, William Herschel, John Herschel et Charles Piazzi Smyth, avant d'être catalogué sous la désignation NGC 7092 par John Dreyer.", True),
                ('annecdotes sur M39:', "M39 est un amas particulièrement étendu et peu concentré. William Herschel avait même remarqué en 1788 qu'il était si grand et dispersé qu'il lui était difficile de déterminer précisément où l'amas commençait et où il finissait.Le nombre d'étoiles de M39 a longtemps été incertain. La classification de Robert Trumpler lui attribue moins de 50 étoiles, tandis que le catalogue Lynga en donne entre 50 et 100. Les mesures du satellite Gaia ont cependant permis d'identifier environ 248 étoiles appartenant à l'amas.M39 est relativement âgé pour un amas ouvert, avec un âge estimé à environ 453 millions d'années. L'incertitude reste toutefois importante, avec une estimation comprise approximativement entre 327 et 628 millions d'années.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546194079698780271/M39.jpg?ex=6aa42af3&is=6aa2d973&hm=2bab22689a00d9eaba39cf25a32964b8f231be68b8d74667ebfe034a67a5a6c2&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/05/Messier-39-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m40": {
             "alias": ["Winnecke 4","le pire objet messier"],
             "titre": "M40",
             "description": "M40 (ou Winnecke 4) est une double optique située dans la constellation de la Grande Ourse. Avec une magnitude apparente de 8,4, elle n'est pas visible à l'œil nu. Il s'agit de deux étoiles qui semblent proches dans le ciel, mais qui sont en réalité situées à des distances très différentes de la Terre.",
             "champs": [
                ("découverte de M40", "En cherchant une nébuleuse décrite par Johannes Hevelius, Charles Messier découvrit cette étoile double en 1764 et l'intégra à son catalogue sous le numéro M40, alors qu'il ne s'agissait pas d'une nébuleuse. En 1869, l'astronome allemand August Winnecke la classa indépendamment dans son catalogue d'étoiles doubles sous le nom Winnecke 4.", True),
                ('annecdotes sur M40:', "M40 est un objet assez particulier du catalogue de Messier : contrairement à la majorité des objets du catalogue, ce n'est ni une nébuleuse, ni un amas, ni une galaxie, mais simplement une double optique, c'est-à-dire deux étoiles qui paraissent proches uniquement parce qu'elles sont alignées dans la même direction depuis la Terre.Les mesures du satellite Gaia ont permis de montrer que les deux étoiles sont en réalité très éloignées l'une de l'autre. HD 238107, l'étoile la plus brillante, se trouve à environ 311 ± 1 parsecs, tandis que HD 238108 est à seulement 144,2 ± 0,3 parsecs. Elles ne forment donc pas un véritable système binaire.M40 illustre ainsi une particularité importante de l'observation astronomique : deux étoiles peuvent sembler voisines dans le ciel sans être physiquement liées. Leur proximité apparente est simplement due à leur alignement sur notre ligne de visée.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546194584348921856/Messier-40.jpg?ex=6aa42b6b&is=6aa2d9eb&hm=9409d784efd5f22861ebd942b9577263bbabea5752b70e4a646283ea221966a1&",
             "image": 'https://freestarcharts.com/images/Articles/Messier/Single/M40_Finder_Chart.png',
             "footer": 'l\'image de localisation provient de freestarscharts merci a eux'
                                },
    "m41": {
             "alias": ["NGC 2287"],
             "titre": "M41",
             "description": "M41 (ou NGC 2287) est un amas ouvert situé dans la constellation du Grand Chien, à environ 2 260 années-lumière du Système solaire. Il mesure environ 25,6 années-lumière de diamètre et son âge est estimé à environ 243 millions d'années. Avec une magnitude apparente de 4,5, M41 est facilement observable et se trouve presque exactement à 4° au sud de Sirius. Il contient entre 50 et 100 étoiles, dont plusieurs géantes rouges et des naines blanches.",
             "champs": [
                ("découverte de M41", "M41 aurait été observé dès 325 av. J.-C. par Aristote, ce qui en ferait l'un des objets du catalogue de Messier connus depuis l'Antiquité. L'astronome sicilien Giovanni Battista Hodierna fut ensuite le premier à le cataloguer, avant 1654. Ses travaux étant tombés dans l'oubli, l'amas fut redécouvert par John Flamsteed en 1702, puis par Guillaume Le Gentil en 1749. Charles Messier l'intégra finalement à son catalogue le 16 janvier 1765. John Herschel le catalogua ensuite sous la désignation GC 1454.", True),
                ('annecdotes sur M41:', "L'amas contient un peu moins de 100 étoiles, dont plusieurs géantes rouges. L'étoile la plus brillante est une géante de type spectral K3, avec une magnitude apparente de 6,9. M41 contient également des naines blanches, vestiges d'étoiles ayant déjà terminé leur évolution.M41 est particulièrement facile à localiser : il se trouve à seulement 4° au sud de Sirius, l'étoile la plus brillante du ciel nocturne. Cette proximité apparente en fait un repère pratique pour retrouver l'amas. Avec une magnitude de 4,5, M41 est un objet assez lumineux. Il peut être observé depuis les latitudes moyennes de l'hémisphère nord entre septembre et avril, tandis qu'il est observable toute l'année depuis les latitudes moyennes de l'hémisphère sud, avec toutefois des conditions moins favorables autour du solstice d'hiver austral.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546195340116627568/Messier-41.jpg?ex=6aaac3a0&is=6aa97220&hm=d4d7ea06ae5589819d6e0b7198c7ce92e91bc5aad1b5f6e365a43230e52d667f&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/05/Messier-41-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m42": {
             "alias": ["NGC 1976","nébuleuse d'orion"],
             "titre": "M42",
             "description": "M42 (ou NGC 1976, aussi appelée nébuleuse d'Orion) est une nébuleuse diffuse située dans la constellation d'Orion, dans le bras d'Orion de la Voie lactée, à environ 1 340 années-lumière du Système solaire. Elle mesure environ 25,3 années-lumière et possède une magnitude apparente de 3,7. Elle est à la fois une nébuleuse en émission et en réflexion et constitue une importante région de formation d'étoiles. Elle contient notamment l'amas du Trapèze, composé de nombreuses étoiles très jeunes et très chaudes.",
             "champs": [
                ("découverte de M42", "La nébuleuse d'Orion a été découverte le 24 novembre 1610 par l'astronome français Nicolas-Claude Fabri de Peiresc, qui fut apparemment le premier à remarquer son aspect diffus. Galilée avait cependant déjà détecté de petites étoiles dans cette région avec sa lunette astronomique. La nébuleuse est ensuite devenue M42 dans le catalogue de Charles Messier et est également connue sous les désignations NGC 1976, Sh2-281 et LBN 974.", True),
                ('annecdotes sur M42:', "M42 est l'une des nébuleuses les plus spectaculaires et les plus faciles à observer. Avec une magnitude de 3,7, elle est même la nébuleuse la plus intense visible à l'œil nu depuis l'hémisphère nord, lorsque le ciel est suffisamment sombre. Elle se trouve dans l'Épée d'Orion, juste sous les trois étoiles de la ceinture d'Orion, ce qui la rend particulièrement facile à repérer. Elle constitue la partie principale du beaucoup plus vaste nuage d'Orion, qui s'étend sur près de la moitié de la constellation et contient notamment la boucle de Barnard et la nébuleuse de la Tête de Cheval.M42 est une véritable pouponnière stellaire. Elle contient de nombreuses étoiles très jeunes et très chaudes, notamment celles de l'amas du Trapèze. Leur rayonnement ionise l'hydrogène environnant et fait briller la nébuleuse. L'âge indiqué pour la nébuleuse est d'environ 3 millions d'années et sa masse est estimée entre 700 et 2 100 masses solaires.M42 abrite également une immense bulle de gaz extrêmement ténue, dont la température atteint environ 2 millions de degrés Celsius. Un gaz aussi chaud émet principalement dans les rayons X plutôt que dans le visible. Cette bulle a notamment été découverte grâce au satellite XMM-Newton.Le télescope spatial James Webb a permis d'y réaliser des observations remarquables. En 2023, son instrument MIRI a détecté pour la première fois la molécule de méthylium dans un disque protoplanétaire autour d'une jeune étoile de la nébuleuse. En 2025, ALMA et James Webb ont également obtenu des images directes d'une exoplanète en formation autour de la protoétoile HOPS 315 située dans M42.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546196930017894411/Orion_Nebula_-_Hubble_2006_mosaic_18000.jpg?ex=6aaa1c5b&is=6aa8cadb&hm=e65a312e8f655fb147623a343ef3b3894d05d7925b87a1efadc2cf44e098ee64&",
             "image": 'https://freestarcharts.com/images/Articles/Messier/Single/M42_Finder_Chart.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m43": {
             "alias": ["NGC 1982","nébuleuse de marian"],
             "titre": "M43",
             "description": "M43 (ou NGC 1982, aussi appelée nébuleuse de Mairan) est une nébuleuse en émission située dans la constellation d'Orion, au nord de la nébuleuse d'Orion (M42), à environ 1 600 années-lumière du Système solaire. Elle mesure environ 20 × 15 minutes d'arc dans le ciel et possède une magnitude apparente de 9,0. M43 est éclairée par l'étoile NU Orionis (HD 37061) et contiendrait également un amas stellaire.",
             "champs": [
                ("découverte de M43", "M43 a été découverte en 1731 par l'astronome français Jean-Jacques Dortous de Mairan, qui remarqua une « nébulosité brillante entourant une étoile ». En 1769, Charles Messier lui attribua le numéro M43 dans son dessin de M42. William Herschel la catalogua ensuite indépendamment le 3 novembre 1783. Elle est également connue sous la désignation NGC 1982.", True),
                ('annecdotes sur M43:', "M43 est située juste au nord de M42, au cœur de la région d'Orion. Les deux nébuleuses apparaissent ainsi côte à côte dans les observations et les photographies, M43 étant une petite région distincte de la grande nébuleuse d'OrionM43 est une nébuleuse en émission : son gaz produit sa propre lumière. Elle est notamment éclairée par NU Orionis, une étoile de magnitude 7, qui se trouve au cœur de la nébuleuse. M43 contiendrait également un amas stellaire.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546200053507424366/Messier-43.jpg?ex=6aaa1f43&is=6aa8cdc3&hm=ebc1a3c001a09b7b9534a2beefd6a9aac3f9fa97c84b3ab9bf00f7dafac7c06e&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/05/Messier-43-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m44": {
             "alias": ["NGC 2632","amas de la crèche"],
             "titre": "M44",
             "description": "M44 (ou NGC 2632, aussi appelé amas de la Crèche, Praesepe ou la Ruche) est un amas ouvert situé dans la constellation du Cancer, à environ 594 années-lumière du Système solaire. Il mesure jusqu'à environ 12 années-lumière de diamètre pour une masse totale comprise entre 500 et 600 masses solaires et son âge est estimé à environ 730 millions d'années. Avec une magnitude apparente de 3,1, M44 est facilement visible à l'œil nu, mais ses étoiles individuelles ne peuvent pas être résolues sans instrument. Les études récentes estiment qu'il contient environ 1 000 étoiles.",
             "champs": [
                ("découverte de M44", "M44 est connu depuis l'Antiquité et aurait été observé pour la première fois par Eudoxe de Cnide entre 380 et 360 av. J.-C.. Le poète grec Aratos de Soles le décrivit en 260 av. J.-C. comme une « petite nuée », tandis qu'Hipparque l'appela le « Petit Nuage » ou « l'Étoile embrumée ». Il apparaît également dans l'Almageste de Claude Ptolémée. En 1609, Galilée observa M44 avec sa lunette et découvrit qu'il s'agissait d'un groupe de plus de 40 étoiles. Charles Messier l'ajouta finalement à son catalogue le 4 mars 1764.", True),
                ('annecdotes sur M44:', "Les Grecs et les Romains l'associaient à une crèche contenant deux ânes, représentés par Asellus Borealis et Asellus Australis. Dans l'astrologie chinoise, son apparence était également associée à un fantôme ou un démon à bord d'un chariot.Il contient : 68 % sont des naines rouges, 30 % sont des étoiles de types spectraux F, G et K semblables au Soleil, et 2 % sont des étoiles brillantes de type A. M44 possède également cinq étoiles géantes, onze naines blanches,  ainsi que très peu de naines brunes, probablement parce qu'une partie d'entre elles aurait été éjectée du halo par les effets de marée.M44 abrite aussi plusieurs exoplanètes. En 2012, deux planètes, Pr0201 b et Pr0211 b, ont été découvertes autour de deux étoiles différentes semblables au Soleil. Il s'agissait alors des premières planètes découvertes autour d'étoiles semblables au Soleil dans un amas ouvert. Ce sont deux Jupiters chauds. Une troisième planète, Pr0211c, a ensuite été découverte en 2016.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546565720559583314/M44-Star-Cluster.png?ex=6aaa2251&is=6aa8d0d1&hm=beebcf68112d7c74977b33e1d0a06c30e0f8293619203f0fc5f9af5a25412427&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/05/Messier-44-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m45": {
             "alias": ["amas des pléiades","pléiades"],
             "titre": "M45",
             "description": "M45 (ou amas des Pléiades) est un amas ouvert situé dans la constellation du Taureau, à environ 444 années-lumière du Système solaire. Il s'étend sur environ 2° dans le ciel et contient environ 3 000 étoiles, dont une douzaine sont visibles à l'œil nu, Les 9 étoiles les plus brillantes portent les noms des sept sœurs de la mythologie grecque et de leurs parents. Son âge est estimé à environ 100 millions d'années. Avec une magnitude apparente de 1,6, M45 est facilement visible à l'œil nu.",
             "champs": [
                ("découverte de M45", "Les Pléiades sont connues depuis l'Antiquité et étaient déjà utilisées par plusieurs civilisations pour établir leurs calendriers. Elles apparaissent notamment sur le disque céleste de Nebra, daté d'environ 1600 av. J.-C.. Dans la Grèce antique, elles étaient associées aux sept filles d'Atlas et de Pléioné. Charles Messier ajouta finalement l'amas à son catalogue en 1769.", True),
                ('annecdotes sur M45:', "M45 possède une place particulière dans l'histoire de l'astronomie car son apparition était utilisée depuis l'Antiquité pour marquer certaines périodes de l'année. En Mésopotamie, en Inde et dans le monde arabe, les Pléiades étaient notamment associées à différents calendriers et stations lunaires.L'amas est relativement jeune, avec un âge estimé à environ 100 millions d'années. Sa faible densité fait qu'il ne devrait cependant pas rester uni très longtemps : il pourrait se disperser dans environ 250 millions d'années.M45 est entouré d'un important nuage de poussière qui réfléchit la lumière des étoiles de l'amas. La partie la plus brillante de ce nuage, autour de Mérope, a été découverte en 1859 et est cataloguée sous le nom de NGC 1435. D'autres extensions sont visibles autour de Maïa, Alcyone, Électre, Célaéno et Taygète. Ce nuage n'est toutefois pas le reste du nuage originel ayant donné naissance aux Pléiades : l'amas aurait simplement croisé ce nuage sur son chemin.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546566817206763682/Pleiades_large.jpg?ex=6aaa2357&is=6aa8d1d7&hm=e1356a68b4695971a4c25ae360f2cddbe9a0360b8f394b469b6231a6bd9f568f&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/05/Messier-45-location.gif',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m46": {
             "alias": ["NGC 2437"],
             "titre": "M46",
             "description": "M46 (NGC 2437) est un amas ouvert situé dans la constellation de la Poupe. Il se trouve à environ 4 480 années-lumière de la Terre, mesure jusqu'à environ 26 années-lumière de diamètre et est âgé d'environ 245 millions d'années. Sa magnitude apparente est de 6,1 et il contient près de 600 étoiles.",
             "champs": [
                ("découverte de M46", "M46 a été découvert par l'astronome français Charles Messier le 19 février 1771, soit trois ans avant la création de son catalogue des objets d'aspect diffus.", True),
                ('annecdotes sur M46:', "M46 est proche de M47, situé à environ 1° à l'ouest. Les deux amas peuvent être observés simultanément avec une paire de jumelles.L'amas est classé III2m selon la classification de Trumpler : sa concentration est moyennement faible et ses étoiles présentent un intervalle moyen de magnitudes. Cette classification indique entre 50 et 100 étoiles, mais les observations montrent qu'il en contient en réalité près de 600.M46 présente un alignement particulièrement intéressant avec la nébuleuse planétaire NGC 2438, qui apparaît comme un cercle bleuté superposé aux étoiles de l'amas. Pourtant, elle ne fait pas partie de M46. Une étude publiée en 2008 a montré une différence d'environ 30 km/s entre leurs vitesses moyennes, prouvant qu'elles ne sont pas liées. NGC 2438 est en réalité située à environ 3 000 années-lumière et apparaît simplement dans la même direction que M46.M46 est donc un bel exemple de superposition apparente : deux objets peuvent sembler proches dans le ciel tout en étant séparés par plusieurs milliers d'années-lumière.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546567851484381264/M46-star-cluster.png?ex=6aaa244d&is=6aa8d2cd&hm=c21f3654d15b9d5782d0720bdb4d1542437422568f8617ebe2f17d6ee990fc47&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/05/Messier-46-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m47": {
             "alias": ["NGC 2422","ngc 2478"],
             "titre": "M47",
             "description": "M47 (NGC 2422 ou NGC 2478) est un amas ouvert situé dans la constellation de la Poupe. Il se trouve à environ 1 600 années-lumière de la Terre, mesure jusqu'à environ 12 années-lumière et est âgé d'environ 73 millions d'années. Sa magnitude apparente est de 4,4 et il contient environ 50 étoiles, principalement de brillantes étoiles bleues accompagnées de quelques géantes rouges.",
             "champs": [
                ("découverte de M47", "M47 a été découvert avant 1654 par l'astronome sicilien Giovanni Battista Hodierna, mais ses travaux tombèrent dans l'oubli pendant plusieurs siècles. Charles Messier observa indépendamment l'amas le 19 février 1771. Cependant, une erreur dans les coordonnées qu'il indiqua fit qu'aucun objet ne semblait correspondre à sa description. M47 fut alors considéré pendant longtemps comme un objet perdu ou inexistant. Ce n'est qu'en 1959 que l'astronome canadien T. F. Morris démontra que M47 correspondait en réalité à NGC 2422, en corrigeant l'erreur de coordonnées de Messier.", True),
                ('annecdotes sur M47:', "M47 est situé à seulement 1° à l'est de M46 sur la voûte céleste. Les deux amas peuvent donc être observés simultanément avec des jumelles, formant un joli couple d'amas ouverts.L'amas est relativement jeune, avec un âge estimé à 73 millions d'années. Il est principalement constitué d'étoiles bleues brillantes, mais quelques géantes rouges se distinguent également.Selon la classification de Trumpler, M47 est classé III2m : sa concentration est moyennement faible et ses étoiles présentent un intervalle moyen de magnitudes. Cette classification estime entre 50 et 100 étoiles, ce qui correspond approximativement au nombre d'étoiles généralement attribué à l'amas.M47 possède plusieurs désignations, notamment NGC 2422 et NGC 2478. Cette double désignation est liée à son histoire mouvementée dans les catalogues astronomiques.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546568386954133625/eso1441a.jpg?ex=6aaa24cd&is=6aa8d34d&hm=9f8e90ebebaea45a71ad92e94f1d0c9c114e7285fee437de12d7a0590350a782&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/05/Messier-47-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m48": {
             "alias": ["NGC 2548"],
             "titre": "M48",
             "description": "M48 (NGC 2548) est un amas ouvert situé dans la constellation de l'Hydre. Il se trouve à environ 2 510 années-lumière de la Terre, est âgé d'environ 361 millions d'années et possède une magnitude apparente de 5,8. Son noyau mesure environ 22 années-lumière, mais l'amas s'étend en réalité jusqu'à environ 39 années-lumière et compte environ 80 étoiles.",
             "champs": [
                ("découverte de M48", "M48 a été découvert par Charles Messier le 19 février 1771, mais Messier nota une position erronée dans ses observations. L'objet fut alors considéré comme inexistant ou perdu. Cette erreur fit que M48 fut redécouvert indépendamment par Johann Elert Bode avant 1782 et par Caroline Herschel le 3 août 1783. L'observation de Caroline fut publiée par son frère William Herschel en 1786 et devint ensuite la référence utilisée pour le catalogue NGC, sous le nom de NGC 2548. Ce n'est qu'en 1934 qu'Oswald Thomas identifia M48 à NGC 2548, identification retrouvée indépendamment par T. F. Morris en 1959.", True),
                ('annecdotes sur M48:', "La distance de M48 reste incertaine selon les sources : certaines l'estiment à 1 500 ou 2 000 années-lumière, tandis que WEBDA donne environ 2 510 années-lumière.L'étoile la plus lumineuse de M48 est une étoile de type spectral A2, de magnitude 8,8, dont la luminosité est environ 70 fois supérieure à celle du Soleil. L'amas contient également trois géantes jaunes de types spectraux G à K.M48 est classé I2m selon la classification de Trumpler : sa concentration est forte et ses étoiles présentent un intervalle moyen de magnitudes.M48 a donc lui aussi connu le même problème que M47 : à cause d'une erreur de coordonnées de Messier, son identité a été perdue pendant plus d'un siècle avant d'être finalement retrouvée.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546569447144296621/M48_Mazur.jpg?ex=6aaa25ca&is=6aa8d44a&hm=353b29e91d4c3755171da593d406038f43ecfa18fee3980c5d30d17501747a43&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/05/Messier-48-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m49": {
             "alias": ["NGC 4472"],
             "titre": "M49",
             "description": "M49 (NGC 4472) est une vaste galaxie elliptique située dans la constellation de la Vierge. Elle se trouve à environ 52 à 63 millions d’années-lumière selon la méthode utilisée et mesure environ 156 000 années-lumière de diamètre. Sa magnitude apparente est de 8,4. Elle contient environ 200 milliards d’étoiles et abrite un trou noir supermassif de plus de 500 millions de masses solaires.",
             "champs": [
                ("découverte de M49", "M49 a été découverte par Charles Messier le 19 février 1771. C’est la première galaxie de l’amas de la Vierge découverte et elle fut intégrée à son catalogue sous le numéro M49. Elle est également connue sous les désignations NGC 4472, PGC 41220 et UGC 7629.", True),
                ('annecdotes sur M49:', "M49 est une galaxie elliptique de type E2, dont la couleur globalement jaune témoigne d'une population principalement composée d'étoiles anciennes et relativement rouges. Sa dernière grande période de formation d’étoiles remonterait à environ 6 milliards d’années, avant même la naissance du Soleil. M49 possède un nombre exceptionnellement élevé d’amas globulaires : environ 6 000, voire 7 813 ± 830 selon une étude de 2008. À titre de comparaison, la Voie lactée en possède environ 150.Son centre abrite un trou noir supermassif dont la masse a été estimée à 565 millions de masses solaires grâce aux observations en rayons X du télescope spatial Chandra. Un candidat trou noir d’origine stellaire a également été identifié dans l’un de ses amas globulaires.Une supernova, SN 1969Q, a été découverte dans M49 le 1er mai 1969 par l’astronome amateur australien Robert Evans. Son type n’a cependant pas été déterminé.M49 est la galaxie la plus grosse et la plus brillante du groupe de M49, qui comprend 127 galaxies. Ce groupe appartient à l’amas de la Vierge, un immense ensemble qui compterait environ 1 300 galaxies, et peut-être plus de 2 000. L’amas de la Vierge fait lui-même partie du superamas de la Vierge, auquel appartient également le Groupe local.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546570304384409670/Messier_49-Rubin_Observatory.png?ex=6aaa2696&is=6aa8d516&hm=de8f34d53d9ee9a79ada2cbc9882c24f9c07cf06495b43dbe50ad45ff0b9e793&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/05/Messier-49-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                }, 
    "m50": {
             "alias": ["NGC 2323"],
             "titre": "M50",
             "description": "M50 (NGC 2323) est un jeune amas ouvert situé dans la constellation de la Licorne, à environ 929 parsecs (3 030 années-lumière) du Système solaire. Il présente une magnitude apparente de 5,9 et s’étend sur environ 15 minutes d’arc, ce qui correspond à une taille réelle maximale d’environ 13 années-lumière. Son âge est estimé à environ 125 millions d’années.",
             "champs": [
                ("découverte de M50", "M50 a probablement été découvert par l’astronome franco-italien Jean-Dominique Cassini avant 1711, selon le témoignage de son fils Jacques Cassini dans son ouvrage Éléments d’astronomie, publié en 1740. Charles Messier l’a ensuite découvert indépendamment le 5 avril 1772 et l’a intégré à son catalogue. L’amas est également connu sous la désignation NGC 2323.", True),
                ('annecdotes sur M50:', "M50 est classé II3m selon la classification des amas ouverts de Robert Trumpler. Cette classification indique que l’amas possède une concentration moyenne d’étoiles, représentée par le chiffre romain II, que ses étoiles présentent un grand intervalle de magnitudes, représenté par le chiffre 3, et qu’il contient entre 50 et 100 étoiles, représenté par la lettre m.Avec un âge d’environ 125 millions d’années, M50 est considéré comme un jeune amas ouvert. Ses étoiles sont encore liées au sein d’une même structure issue de leur formation commune, dans la Voie lactée.La découverte de M50 présente une particularité historique : bien que l’amas soit attribué à Jean-Dominique Cassini, sa découverte n’est connue que par le témoignage de son fils Jacques Cassini, qui indique qu’elle aurait eu lieu avant 1711. Messier l’a ainsi découvert indépendamment plus de soixante ans plus tard, en 1772.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546610302596939837/M50.jpg?ex=6aaa4bd6&is=6aa8fa56&hm=275f0e1f41062b97b61f31091002ac329aac5b10e3a2d158fda78f30c1e4c639&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/05/Messier-50-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m51": {
             "alias": ["NGC 5194"],
             "titre": "M51",
             "description": "M51 (NGC 5194), aussi surnommée la galaxie du Tourbillon, est une galaxie spirale située dans la constellation des Chiens de chasse, à une distance estimée à environ 25 millions d’années-lumière. Elle mesure environ 80 900 années-lumière de diamètre et possède deux grands bras spiraux particulièrement bien définis. M51 est en interaction gravitationnelle avec sa galaxie compagne NGC 5195, ce qui contribue probablement à la forme spectaculaire de ses bras spiraux et à l'augmentation de son activité de formation stellaire. Sa magnitude apparente est de 8,4, ce qui permet de l'observer avec un petit instrument sous un ciel sombre.",
             "champs": [
                ("découverte de M51", "M51 a été découverte par Charles Messier le 13 octobre 1773, puis ajoutée à son catalogue le 11 janvier 1774. La galaxie compagne NGC 5195 ne fut identifiée qu'en 1781 par Pierre Méchain, même si Messier pourrait déjà l'avoir observée sans la distinguer comme un objet séparé. En 1845, l'astronome irlandais William Parsons fut le premier à observer clairement la structure spirale de M51 grâce à son immense télescope de 1,8 mètre de diamètre. M51 devint ainsi la première « nébuleuse » connue présentant une structure spirale. Cette découverte conduisit ensuite les astronomes à parler de « nébuleuses spirales » pour désigner des objets similaires, avant que les travaux d'Edwin Hubble dans les années 1920 ne permettent de comprendre qu'il s'agissait en réalité de galaxies distinctes de la Voie lactée.", True),
                ('annecdotes sur M51:', "M51 et NGC 5195. Les deux galaxies ont connu au moins une ou plusieurs rencontres rapprochées, mais le déroulement exact de cette interaction reste encore discuté. Selon certains modèles, NGC 5195 aurait traversé le disque de M51 il y a plusieurs centaines de millions d'années, puis aurait effectué un autre passage plus récent.Cette interaction a également favorisé la formation d'étoiles dans M51, en particulier dans son bras spiral nord. Les deux galaxies sont entourées de vastes débris de marée, principalement constitués d'étoiles arrachées au cours de leurs interactions. Un immense panache diffus s'étend ainsi sur environ 140 000 années-lumière depuis le centre de M51.M51 possède également un trou noir supermassif en son centre. Les estimations de sa masse sont très différentes selon les méthodes utilisées, allant de quelques centaines de milliers à plusieurs millions de masses solaires. Les observations du télescope spatial Hubble ont notamment révélé une étonnante structure sombre en forme de « X » autour de sa position. Celle-ci pourrait être liée à des structures de poussière entourant le trou noir et son disque d'accrétion.Une observation particulièrement étonnante concerne l'étoile M51-DS1, une supergéante rouge qui semblait avoir disparu entre 2017 et 2019. Les astronomes avaient alors envisagé l'hypothèse rare d'une « supernova ratée », dans laquelle une étoile massive s'effondrerait directement en trou noir sans produire d'explosion lumineuse importante. L'étoile est cependant réapparue en 2021 : elle avait probablement subi une importante éruption de matière qui l'avait temporairement obscurcie.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546612219880415363/255_hour_collaboration_-_Whirlpool_Galaxy_with_Ionized_Hydrogen__Shelf__-_Flickr_-_William_Ostling.png?ex=6aaa4d9f&is=6aa8fc1f&hm=f71b934549c1742be195522b5c928dcc5eff9684e4d183455ef8f08a8b7de8e1&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/06/Messier-51-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m52": {
             "alias": ["NGC 7654"],
             "titre": "M52",
             "description": "M52, également désigné NGC 7654, est un amas ouvert situé dans la constellation de Cassiopée, à environ 5 400 années-lumière. Il mesure environ 23 années-lumière de diamètre et serait âgé de 120 ± 20 millions d’années, même si d'autres estimations donnent environ 58 millions d'années. Sa magnitude apparente est comprise entre 6,6 et 7,3, ce qui le rend invisible à l'œil nu. L'amas est classé I2r selon la classification de Trumpler, ce qui signifie qu'il possède une forte concentration d'étoiles, qu'il est riche en étoiles et que leurs magnitudes couvrent un intervalle moyen.",
             "champs": [
                ("découverte de M52", "M52 a été découvert par Charles Messier le 7 septembre 1774. Il fut ensuite observé par William Herschel le 29 août 1783, puis par son fils John Herschel le 9 octobre 1829. Il est aujourd'hui également répertorié sous la désignation NGC 7654.", True),
                ('annecdotes sur M52:', "M52 contient un grand nombre d'étoiles. Les données de Simbad recensent 1 088 entrées, mais certaines correspondent plusieurs fois aux mêmes étoiles. En ne conservant que les étoiles ayant une probabilité d'appartenance à l'amas d'au moins 90 %, on obtient environ 800 étoiles différentes. Les propriétés de l'amas, notamment sa distance et son mouvement propre, ont été déterminées à partir de 798 d'entre elles.M52 n'est pas visible à l'œil nu, mais peut être observé avec un petit télescope. Il est relativement isolé des étoiles brillantes, l'étoile brillante la plus proche étant Caph, située à environ 6,2°. Une fois M52 trouvé, deux autres objets intéressants se trouvent à proximité : les nébuleuses en émission NGC 7635, connue sous le nom de nébuleuse de la Bulle, et NGC 7538.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546616294214865006/M52_and_the_Bubble_Nebula_noao-m52r.jpg?ex=6aaa516b&is=6aa8ffeb&hm=27f26310eebf32e2e9b106de942bd5a8657937641bd2706176bc873ca23cc5d7&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/06/Messier-52-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m53": {
             "alias": ["NGC 5024"],
             "titre": "M53",
             "description": "M53, également désigné NGC 5024, est un amas globulaire situé dans la constellation de la Chevelure de Bérénice, à environ 58 000 années-lumière de la Terre. Il mesure environ 221 années-lumière de diamètre et contient une importante population stellaire. Âgé d'environ 12,67 milliards d'années et ayant une masse d'environ 826 000 masse solaires, il possède une très faible métallicité, ce qui en fait l'un des amas globulaires les plus pauvres en métaux de la Voie lactée. Sa magnitude apparente de 7,7 le rend invisible à l'œil nu, mais il peut être observé au télescope.",
             "champs": [
                ("découverte de M53", "M53 a été découvert par l'astronome allemand Johann Elert Bode le 3 février 1775. Charles Messier l'observa ensuite le 26 février 1777 et l'ajouta à son catalogue sous le numéro M53. William Herschel fut le premier à parvenir à résoudre les étoiles de l'amas, c'est-à-dire à les distinguer individuellement plutôt que de voir uniquement une tache lumineuse.", True),
                ('annecdotes sur M53:', "La majorité de ses géantes rouges semblent appartenir à une première génération d'étoiles, tandis que les étoiles de deuxième génération sont davantage concentrées vers le centre de l'amas. Sa composition stellaire présente ainsi des similitudes avec celle des étoiles du halo galactique.M53 possède une population particulièrement importante d'étoiles variables. On y connaît notamment 55 variables de type RR Lyrae, dont 34 présentent un comportement associé à l'effet Blazhko. Parmi elles, 23 sont de type RRc, ce qui constitue la plus grande population de ce type connue dans un amas globulaire de la Voie lactée. L'amas contient également au moins trois variables de type SX Phoenicis et une géante rouge semi-régulière.M53 présente des signes d'interactions gravitationnelles avec NGC 5053, un amas globulaire voisin beaucoup plus diffus. Des effets de marée sont visibles dans les régions périphériques de M53, notamment sous la forme de régions plus denses, d'ondulations et de queues de matière orientées selon son orbite. Un possible pont de marée et une enveloppe commune semblent même relier les deux amas, ce qui pourrait être la conséquence d'une interaction dynamique entre eux. Si cette interprétation est correcte, il s'agirait d'un événement particulièrement rare, car aucun autre système d'amas globulaires binaires n'est connu dans la Voie lactée.Enfin, M53 est également considéré comme un candidat pour appartenir au courant de marée de la galaxie naine du Sagittaire, ce qui pourrait fournir un indice supplémentaire sur son histoire et ses interactions gravitationnelles dans la Voie lactée.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546617658798112839/Messier53_-_SDSS_DR14_panorama.jpg?ex=6aaa52b0&is=6aa90130&hm=0a1787cffb4dae9da7fab2a39109ccd8843acb90431815543e24de436e6bd3b3&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/06/Messier-53-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },     
    "m54": {
             "alias": ["NGC 6121"],
             "titre": "M54",
             "description": "M54 (NGC 6715) est un amas globulaire situé dans la constellation du Sagittaire, à environ 86 450 années-lumière du Soleil et 61 650 années-lumière du centre de la Voie lactée. Il possède une masse d’environ 179 000 masses solaires, un âge estimé à 12,9 milliards d’années et une magnitude apparente de 7,6. M54 appartient à la galaxie naine du Sagittaire (SagDEG), ce qui en fait un amas globulaire extragalactique.",
             "champs": [
                ("découverte de M54", "M54 a été découvert par Charles Messier le 24 juillet 1788, qui le décrivit comme très faible depuis Paris. En 1784, William Herschel parvint à résoudre certaines étoiles des régions externes de l’amas, tandis que James Dunlop l’observa en 1827 sans parvenir à distinguer ses étoiles. C’est finalement John Herschel, après plusieurs observations entre 1834 et 1836, qui identifia clairement M54 comme un amas globulaire. Il fut ensuite catalogué sous la désignation NGC 6715 par John Dreyer.", True),
                ('annecdotes sur M54:', "M54 a longtemps été considéré comme un amas appartenant à la Voie lactée, car sa distance était alors estimée entre 50 000 et 65 000 années-lumière. Des observations réalisées en 1994 ont cependant montré qu’il se trouvait en réalité dans la galaxie naine du Sagittaire, faisant de M54 le premier amas globulaire extragalactique découvert. La galaxie naine du Sagittaire est progressivement attirée par la Voie lactée et devrait finir par fusionner avec elle. M54 possède de nombreuses étoiles variables. En 2016, 67 nouvelles étoiles variables ont été identifiées parmi celles appartenant à l’amas, en plus des 17 déjà connues. Elles comprennent notamment des RR Lyrae, des étoiles irrégulières à longue période, des semi-régulières, une W Virginis et une binaire à éclipses. Aucun pulsar n’avait été détecté dans M54 en 2023, mais un modèle basé sur les émissions de haute énergie estime qu’il pourrait contenir jusqu’à 25 pulsars milliseconde.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546622177678327808/Messier_54_HST.jpg?ex=6aaa56e6&is=6aa90566&hm=d2f36ee02753e587787c2e6a90f95595122ff40aab0d7d1c560b88d5938075f1&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/06/Messier-54-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                },
    "m55": {
             "alias": ["NGC 6809"],
             "titre": "M55",
             "description": "M55 (NGC 6809) est un amas globulaire situé dans la constellation du Sagittaire, à environ 17 600 années-lumière du Soleil et 12 720 années-lumière du centre de la Voie lactée. Il possède une masse d’environ 269 000 masses solaires, un diamètre réel d’environ 97 années-lumière et un âge estimé à 12,29 milliards d’années. Avec une magnitude apparente de 6,32, il est presque visible à l’œil nu et facilement observable aux jumelles ou avec un petit télescope.",
             "champs": [
                ("découverte de M55", "M55 a été découvert par l’astronome français Nicolas-Louis de Lacaille le 16 juin 1752, alors qu’il se trouvait en Afrique du Sud. Son apparence très peu concentrée pouvait cependant le faire prendre pour un simple amas d’étoiles, voire pour une nébuleuse : Johann Elert Bode le compara même à un noyau cométaire obscur. William Herschel parvint ensuite à résoudre ses étoiles entre 1783 et 1785, puis John Herschel l’observa en 1834 et le classa clairement comme un amas globulaire. ", True),
                ('annecdotes sur M55:', "M55 est un amas globulaire particulièrement déconcentré : sa classe de concentration Shapley-Sawyer est XI, l'une des classes indiquant la plus faible concentration vers le centre. Cela explique pourquoi plusieurs astronomes des XVIIIe et XIXe siècles ont décrit son aspect comme celui d’une large nébuleuse ou d’un amas peu concentré.M55 contient au moins 74 traînardes bleues (blue straggler stars) dans sa région centrale. Leur répartition sur le diagramme de Hertzsprung-Russell présente deux séquences distinctes, une particularité confirmée par des observations réalisées avec le télescope spatial Hubble ainsi qu’avec des télescopes terrestres.Une étude photométrique a également identifié 55 étoiles variables dans la région centrale de l’amas, dont 28 nouvelles et 13 binaires à éclipses. Parmi elles figurent notamment 35 étoiles de type SX Phoenicis, deux binaires à contact et une binaire semi-détachée. Deux traînardes rouges ont également été détectées.", True),
                                    ],
             "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546623076983378020/Messier_55_VISTA.jpg?ex=6ab3923c&is=6ab240bc&hm=6b0e66afc4fddc4f087fcb7396aa0e16867af8e3e23a3d035c3e8f62ed45b127&",
             "image": 'https://www.messier-objects.com/wp-content/uploads/2015/06/Messier-55-location.png',
             "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                }, 
    "m56": {
                 "alias": ["NGC 6779"],
                 "titre": "M56",
                 "description": "M56 (NGC 6779) est un amas globulaire situé dans la constellation de la Lyre, à environ 30 660 années-lumière du Soleil et à environ 30 010 années-lumière du centre de la Voie lactée. Il a une magnitude apparente de 8,27 donc invisible à l'œil nu, une taille apparente de 8,8 minutes d’arc et une masse d’environ 230 000 masses solaires. Son âge est estimé à environ 13,7 milliards d’années et sa métallicité est très faible, à environ 1 % de celle du Soleil.",
                 "champs": [
                    ("découverte de M56", "M56 a été découvert par Charles Messier le 23 janvier 1779, qui le décrivit comme une faible nébuleuse sans étoiles. Cette même nuit, Messier découvrit également la comète de 1779. Caroline Herschel observa ensuite M56 en 1783, puis William Herschel l'observa en 1807 et fut le premier à résoudre ses étoiles. John Herschel l'étudia à six reprises entre 1825 et 1829 et le décrivit comme un amas finement condensé, plus brillant vers le centre, composé d'étoiles de magnitude 12 à 14. Il fut ensuite catalogué comme NGC 6779 par John Dreyer.", True),
                    ('annecdotes sur M56:', "M56 est un amas globulaire relativement déconcentré vers son centre, ce qui lui vaut la classe X dans la classification de concentration de Shapley-Sawyer. Malgré son apparence peu concentrée, ses étoiles deviennent progressivement plus denses en allant vers le centre.Sept étoiles variables ont été détectées dans M56 : deux de type RR Lyrae, une de type RV Tauri, une de type BL Herculis, deux étoiles semi-régulières et une étoile variable pulsante dont le type n'a pas été identifié.Une possible source diffuse de rayons X a également été détectée dans son environnement. Sa position suggère qu'elle pourrait provenir du milieu interstellaire chauffé dans le sillage de l'amas, à la suite de l'interaction entre M56 et le halo gazeux qui l'entoure.", True),
                                        ],
                 "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546877669591752874/M56HunterWilson.jpg?ex=6ab3d698&is=6ab28518&hm=4f23ca57aa20150056987497784d949e42cc281453a982b1f5ffcc2c6e355b10&",
                 "image": 'https://www.messier-objects.com/wp-content/uploads/2015/06/Messier-56-location.png',
                 "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                    },
    "m57": {
                 "alias": ["NGC 6720"],
                 "titre": "M57",
                 "description": "M57 (NGC 6720), aussi appelée nébuleuse de la Lyre ou nébuleuse de l'Anneau, est une nébuleuse planétaire située dans la constellation de la Lyre, à environ 2 570 années-lumière de la Terre. Elle possède une magnitude apparente de 8,8, un diamètre apparent d'environ 3 minutes d'arc, une masse d'environ 0,61 masse solaire et une taille réelle d'environ 2,24 années-lumière. Son âge est difficile à déterminer et les estimations vont de quelques milliers d'années à plus de 20 000 ans selon les méthodes utilisées.",
                 "champs": [
                    ("découverte de M57", "M57 a été découverte par Charles Messier le 31 janvier 1779, alors qu'il recherchait la comète C/1779 A1 (Bode). Il remarqua une petite tache lumineuse à proximité de la trajectoire de la comète. Antoine Darquier de Pellepoix la découvrit indépendamment deux semaines plus tard et la compara à Jupiter, ce qui contribua à l'appellation persistante de « nébuleuse planétaire ». William Herschel l'observa ensuite à plusieurs reprises et participa à l'introduction de cette appellation, car les nébuleuses planétaires connues lui semblaient ressembler à Uranus. L'étoile centrale fut découverte en 1800 par Friedrich von Hahn, tandis que John Dreyer l'intégra ensuite au catalogue NGC sous la désignation NGC 6720.", True),
                    ('annecdotes sur M57:', "M57 est devenue un archétype des nébuleuses planétaires. Elle résulte de l'évolution finale d'une étoile similaire au Soleil : celle-ci a expulsé progressivement ses couches externes, qui forment aujourd'hui les structures gazeuses lumineuses autour de l'étoile centrale. Cette dernière est désormais une naine blanche, dont la taille est comparable à celle de la Terre. Sa température est estimée autour de 120 000 à 132 000 K, pour une luminosité d'environ 200 fois celle du Soleil. Sa masse est donnée entre 0,61 et 0,62 masse solaire par une étude, tandis qu'une autre estimation donne 1,537 masse solaire.La nébuleuse présente trois grandes structures : un vide central bleu-vert composé principalement d'oxygène doublement ionisé, un anneau rougeâtre due notamment aux émissions de l'hydrogène et de l'azote et un halo externe. L'anneau, qui constitue la partie la plus lumineuse, possède une forme elliptique et un aspect grumeleux avec des « touffes » et des « globules ». Le halo est beaucoup plus faible et présente des arcs concentriques ainsi que de nombreuses pointes radiales. Des observations récentes de 2026 ont également révélé une structure linéaire composée d'atomes de fer ionisés traversant la cavité centrale, dont l'origine reste incertaine.", True),
                                        ],
                 "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546880001029316618/Messier_57_-_The_Ring_Nebula_-_Flickr_-_gjdonatiello.jpg?ex=6ab3d8c3&is=6ab28743&hm=8bb015277d02649a38531e41481447edf5df07107c3159c8e394b941058617f2&",
                 "image": 'https://www.messier-objects.com/wp-content/uploads/2015/06/Messier-57-location.png',
                 "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                    },
    "m58": {
                 "alias": ["NGC 4579"],
                 "titre": "M58",
                 "description": "M58 (NGC 4579) est une galaxie spirale intermédiaire située dans la constellation de la Vierge, à environ 60 millions d’années-lumière. Elle mesure environ 133 000 années-lumière de diamètre et possède une magnitude apparente de 9,7. Sa vitesse radiale est de 1 517 ± 1 km/s. M58 est une galaxie active de type Seyfert 1.9 et est également classée comme galaxie LINER.",
                 "champs": [
                    ("découverte de M58", "M58 a été découverte par Charles Messier le 15 avril 1779, la même nuit que M88. Messier l'observa alors qu'il étudiait la comète C/1779 A1 (Bode) et la décrivit comme une très pâle nébuleuse, dont la faible lumière pouvait même disparaître lorsqu'il utilisait l'éclairage nécessaire au réticule de son télescope. Quelques jours auparavant, Johann Gottfried Koehler avait découvert M59 et M60, que Messier observa également cette même nuit.", True),
                    ('annecdotes sur M58:', "M58 présente une structure assez particulière : elle est décrite comme une galaxie spirale intermédiaire barrée, car une barre centrale est nettement visible sur certaines photographies. Dans les observations en infrarouge, son bulbe apparaît brillant et légèrement elliptique, traversé par une barre proéminente à partir de laquelle commencent les bras spiraux. M58 possède un trou noir supermassif en son centre. Une étude fondée sur la vitesse interne de la galaxie estime sa masse entre 43 et 230 millions de masses solaires.La galaxie se trouve dans l’amas de la Vierge qui compterait entre 1300 et 2 000 galaxies selon certaines estimations. Elle est notamment considérée comme membre du groupe de M87, qui comprend au moins 96 galaxies. Son déplacement dans le milieu intergalactique provoque une pression dynamique qui lui arrache une partie de ses gaz. Malgré cette perte de gaz, son taux de formation d'étoiles reste normal. Le télescope spatial Hubble a également révélé un disque de formation d'étoiles autour du noyau, dont le demi-grand axe mesure environ 555 années-lumière.Deux supernovas ont été observées dans M58. SN 1988A, découverte le 18 janvier 1988 par l'astronome amateur japonais Kaoru Ikeya et indépendamment par Robert Evans, était une supernova de type II. SN 1989M, découverte le 28 juin 1989 par G. N. Kimeridze, était quant à elle une supernova de type Ia.", True),
                                        ],
                 "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546883234955268166/M58s_visible.jpg?ex=6ab3dbc6&is=6ab28a46&hm=8f4c44de88b4aa316df6efb47dfc8f4f17ac26a30d424372f8bc997b8e78db22&",
                 "image": 'https://www.messier-objects.com/wp-content/uploads/2015/06/Messier-58-location.png',
                 "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                    },
    "m59": {
                 "alias": ["NGC 4621"],
                 "titre": "M59",
                 "description": "M59 (NGC 4621) est une galaxie elliptique située dans la constellation de la Vierge, à environ 52,2 millions d’années-lumière. Elle mesure environ 104 000 années-lumière de diamètre et possède une magnitude apparente de 9,6. Sa masse est estimée à environ 97 milliards de masses solaires. M59 appartient à l’amas de la Vierge et possède une galaxie naine ultracompacte compagne, M60-UCD1.",
                 "champs": [
                    ("découverte de M59", "M59 a été découverte le 11 avril 1779 par l’astronome allemand Johann Gottfried Koehler. Charles Messier l’observa seulement quatre jours plus tard et l’ajouta à son catalogue. M59 fait ainsi partie des galaxies de l’amas de la Vierge observées par Messier lors de cette période.", True),
                    ('annecdotes sur M59:', "Le noyau de M59 est une galaxie elliptique de type E5 possédant une structure inhabituelle : les observations de sa cinématique stellaire ont révélé un noyau contre-rotatif d’environ 196 années-lumière de diamètre, dont les étoiles tournent dans le sens opposé à celui d'une partie du reste de la galaxie. Le noyau contient également un disque plus bleu que le bulbe, dont une extension pourrait être la conséquence d’une ancienne fusion galactique suivie d’un sursaut de formation d’étoiles.Son centre possède un trou noir supermassif particulièrement massif. Une étude de 2008 l’estime à environ 270 millions de masses solaires, tandis qu’une autre étude publiée la même année donne une estimation plus élevée de 400 millions de masses solaires.Le télescope spatial Hubble a permis d’estimer que M59 possède environ 803 ± 355 amas globulaires, soit plusieurs centaines d’amas stellaires très anciens gravitant autour de la galaxie. M59 a également été le théâtre d’une supernova, SN 1939B, découverte le 19 mai 1939 par l’astrophysicien Fritz Zwicky. Le type de cette supernova n’a cependant pas été déterminé.", True),
                                        ],
                 "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546885320673329222/Messier59_-_HST_-_Potw1921a.jpg?ex=6ab3ddb8&is=6ab28c38&hm=5be5794ce084c21bfcb99d83b7b4b9c2749ba4bb67060f0dd0d1fa40ecbfb34f&",
                 "image": 'https://freestarcharts.com/images/Articles/Messier/Single/M59_Finder_Chart.png',
                 "footer": 'l\'image de localisation provient de freestarscharts merci a eux'
                                    },
    "m60": {
                 "alias": ["NGC 6121"],
                 "titre": "M60",
                 "description": "M60 (NGC 4649) est une galaxie elliptique située dans la constellation de la Vierge, à environ 54,5 millions d’années-lumière. Elle mesure environ 127 000 années-lumière de diamètre et possède une masse estimée à 250 milliards de masses solaires. Sa magnitude apparente est de 8,8. M60 abrite également un trou noir supermassif dont la masse est estimée entre 2,0 et 4,5 milliards de masses solaires. Les observations des amas globulaires indiquent qu’environ 72 ± 5 % de la masse de M60 serait constituée de matière noire.",
                 "champs": [
                    ("découverte de M60:", "M60 a été découverte le 11 avril 1779 par Johann Gottfried Koehler, qui l’observa la même nuit que M59 alors qu’il suivait une comète. Le lendemain, l’astronome italien Barnaba Oriani l’observa indépendamment, sans toutefois voir M59. Quatre jours plus tard, Charles Messier l’ajouta à son catalogue.", True),
                    ('annecdotes sur M60:', "M60 est l'une des grandes galaxies de l’amas de la Vierge. Elle forme, avec M58 et M59, une série de trois galaxies qui peuvent apparaître successivement dans le champ d’une lunette pointée vers cette région du ciel. À faible grossissement, M60 apparaît dans le même champ à seulement 25 minutes d'arc de M59.M60 possède un très grand nombre d’amas globulaires estimé à environ 4 745 ± 1 099 d’après une étude réalisée Hubble. En 2004, une supernova de type Ia, SN 2004W, a également été observée dans la galaxie, avec une magnitude de 18,8 au moment de sa découverte. En 2013, les astronomes ont découvert M60-UCD1, une galaxie naine ultracompacte en orbite autour de M60, considérée comme l’une des galaxies les plus denses de l’Univers proche.M60 est également associée à NGC 4647, une galaxie spirale qui semble se superposer à elle depuis notre point de vue. Leur interaction gravitationnelle a longtemps été débattue : aucune formation récente d’étoiles ne constitue une preuve évidente d’une interaction, mais des observations détaillées de Hubble suggèrent le début d’une interaction de marée entre les deux galaxies.", True),
                                        ],
                 "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546895060958978138/Arp116_Hubble.jpg?ex=6ab3e6ca&is=6ab2954a&hm=9830233a5fc42978debaa561ef4ddf578949e75ac858b41b945ed1cf337f97c8&",
                 "image": 'https://www.messier-objects.com/wp-content/uploads/2015/06/Messier-60-location.png',
                 "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                    },
    "m61": {
                     "alias": ["NGC 4303"],
                     "titre": "M61",
                     "description": "M61 (NGC 4303) est une galaxie spirale intermédiaire située dans la constellation de la Vierge, à environ 47,7 millions d’années-lumière. Vue presque de face, elle mesure environ 91 600 années-lumière de diamètre et possède une magnitude apparente de 9,7. M61 est une galaxie active de type Seyfert 2 et une galaxie à sursaut de formation d’étoiles. Elle abrite également un trou noir supermassif, dont la masse est estimée entre 600 000 et 16 millions de masses solaires selon les études.",
                     "champs": [
                        ("découverte de M61:", "M61 a été découverte le 5 mai 1779 par l’astronome italien Barnaba Oriani. Charles Messier l’a observée le même jour, mais l’a prise à deux reprises pour une comète avant de comprendre, six jours plus tard, qu’elle ne se déplaçait pas. Elle est alors devenue la 61e entrée de son catalogue. William Herschel l’observa ensuite en 1786, puis John Herschel à deux reprises en 1828 et 1851.", True),
                        ('annecdotes sur M61:', "M61 possède une structure spirale particulièrement complexe : ses deux bras partent d’une barre centrale peu lumineuse et forment un pseudo-anneau interne. Les bras sont irréguliers, avec de nombreux nœuds de formation d’étoiles, notamment dans le bras nord. Le télescope spatial Hubble a également permis de détecter autour du noyau un disque de formation d’étoiles d’environ 1 140 années-lumière de demi-grand axe. C'est une galaxie à sursaut de formation d’étoiles : les étoiles s'y forment à un rythme particulièrement élevé. Son activité ne se limite pas à la formation stellaire : une source de rayons X détectée au cœur de la galaxie indique également la présence probable d’un trou noir supermassif.M61 est particulièrement remarquable par le nombre de supernovas observées en son sein. Huit supernovas y ont été découvertes, la majorité étaient des supernovas de type II, tandis qu'une était de type Ia-pec. Certaines ont été découvertes par des astronomes amateurs ou par des observateurs utilisant des programmes automatisés.M61 fait partie de l’amas de la Vierge et est l’une de ses galaxies les plus vastes. Elle est également la principale galaxie du groupe de M61, qui comprend au moins 32 galaxies. Ce groupe fait partie de l’amas de la Vierge, lui-même situé au cœur du superamas de la Vierge, dont fait partie le Groupe local. M61 appartient ainsi à une immense structure regroupant des centaines, voire des milliers de galaxies.", True),
                                            ],
                     "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546918402226921615/vierge.jpg?ex=6ae76707&is=6ae61587&hm=daf6c8f6cb5806e2b4af0f5bacc2b232528c9f531787e9d19bf8e7314fd6ee72&",
                     "image": 'https://www.messier-objects.com/wp-content/uploads/2015/07/Messier-61-location.png',
                     "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                        },                                              
    "m62": {
                     "alias": ["NGC 6266"],
                     "titre": "M62",
                     "description": "M62 (NGC 6266) est un amas globulaire situé dans la constellation d’Ophiuchus, à environ 22 500 années-lumière du Soleil et seulement 5 550 années-lumière du centre de la Voie lactée. Il possède une magnitude apparente de 6,4, un diamètre apparent d’environ 15 minutes d’arc, une masse d’environ 1,22 million de masses solaires et un âge estimé à 11,78 milliards d’années.",
                     "champs": [
                        ("découverte de M62:", "M62 a été découvert par Charles Messier le 7 juin 1771. L’amas a ensuite été observé par plusieurs astronomes, mais Messier fut le premier à l’ajouter à son catalogue. Il est aujourd’hui également connu sous la désignation NGC 6266.", True),
                        ('annecdotes sur M62:', "M62 est assez inhabituel parmi les amas globulaires, car il n’est pas parfaitement sphérique. Il est déformé et étiré sur un côté, ce qui lui donne une apparence évoquant une comète, avec une tête brillante et une sorte de queue. Cette forme serait très probablement due aux forces de marée exercées par la Voie lactée, M62 étant l’un des amas globulaires les plus proches du centre galactique.L’amas est particulièrement riche en étoiles variables : une étude de 2010 en a identifié 245, dont 209 RR Lyrae, 4 céphéides de type II, 25 variables à longue période, une binaire à éclipses et six étoiles encore mal classifiées. M62 abrite également six pulsars millisecondes à éclipse, dont l’un semble recevoir un jet de gaz provenant de son étoile compagne. Environ 50 sources de rayons X ont été détectées à l’intérieur de son rayon de demi-masse, tandis que 57 traînardes bleues ont été identifiées près de son centre.La grande masse de M62 a conduit à des recherches un éventuel trou noir de masse intermédiaire. Une étude du mouvement des étoiles n’a pas jugé nécessaire d’en introduire un pour expliquer leurs trajectoires. Mais, une étude publiée en 2019, basée sur l’accélération des pulsars, a détecté une masse non lumineuse comprise entre 1 200 et 6 000 masses solaires qui pourrait être répartie entre plusieurs rémanents de supernovas ", True),
                                            ],
                     "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546920978746048642/Messier62_-_HST_-_Potw1915a.jpg?ex=6ae7696d&is=6ae617ed&hm=8a555ca1724a11f693c2c219d00d6d7a3f6a44b5947c43ad0ddc8ee428941649&",
                     "image": 'https://www.messier-objects.com/wp-content/uploads/2015/07/Messier-62-location.png',
                     "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                        },                                              
    "m63": {
                     "alias": ["NGC 5055"],
                     "titre": "M63",
                     "description": "M63 (NGC 5055) est une galaxie spirale située dans la constellation des Chiens de chasse, à environ 25,2 millions d’années-lumière de la Terre. Elle mesure environ 110 000 années-lumière de diamètre et présente une magnitude apparente de 8,6. Elle est classée SA(rs)bc / Sbc et possède une vitesse radiale d’environ 500 km/s.",
                     "champs": [
                        ("découverte de M63:", "M63 a été découverte par l’astronome français Pierre Méchain le 14 juin 1779. Charles Messier confirma son observation le même jour et l’intégra à son catalogue. La galaxie est parfois surnommée la galaxie du Tournesol. Sa structure spirale fut ensuite identifiée comme telle par Lord Rosse, qui la compta en 1850 parmi les premières nébuleuses spirales reconnues.", True),
                        ('annecdotes sur M63:',"La galaxie possède un noyau de type LINER, caractérisé par des raies d’émission provenant d’atomes faiblement ionisés, ainsi que de nombreuses régions H II, où se trouvent de l’hydrogène ionisé. M63 est également particulièrement lumineuse dans l’infrarouge : sa luminosité dans l’infrarouge lointain atteint environ 10,2 milliards de luminosités solaires, tandis que sa luminosité infrarouge totale est d’environ 12,3 milliards de luminosités solaires.M63 fait partie du groupe de M51, qui comprend au moins dix galaxies, dont M51, la galaxie du Tourbillon. Elle est également incluse dans des classifications plus larges du groupe de M101, qui rassemblerait plus de 80 galaxies. Les deux ensembles sont associés à l’amas de la Grande Ourse, lui-même situé dans le superamas de la Vierge.Une supernova de type Ia, nommée SN 1971I, a été découverte dans M63 le 24 mai 1971 par Jolly Clark. Les supernovas de type Ia sont particulièrement importantes en astronomie car elles peuvent servir d’objets de référence pour mesurer les distances à l’échelle cosmologique.", True),
                                            ],
                     "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546923257377067008/Messier-63.jpg?ex=6ae76b8d&is=6ae61a0d&hm=584763e5da817db861ddb5c5f337950fc5a69acdda66e042ddecab1b13ef6f08&",
                     "image": 'https://www.messier-objects.com/wp-content/uploads/2015/07/Messier-63-location.png',
                     "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                        },                                              
    "m64": {
                     "alias": ["NGC 4826"],
                     "titre": "M64",
                     "description": "M64 (NGC 4826) est une galaxie spirale située dans la constellation de la Chevelure de Bérénice, à environ 17,7 millions d’années-lumière de la Terre. Elle mesure environ 53 800 années-lumière de diamètre et présente une magnitude apparente de 8,5. Elle est notamment connue sous les noms de galaxie de l’Œil noir, galaxie de l’Œil poché ou Beauté endormie. Un trou noir supermassif se trouve au centre de M64 et on estime sa masse entre 18 et 42 millions de masses solaires.",
                     "champs": [
                        ("découverte de M64:", "M64 a été découverte par l’astronome britannique Edward Pigott le 23 mars 1779, puis indépendamment par Johann Elert Bode le 4 avril de la même année. Charles Messier la redécouvrit ensuite le 1er mars 1780 et l’ajouta à son catalogue. La découverte de Pigott ne fut toutefois reconnue par les historiens qu’en 2002, lorsque ses travaux furent retrouvés.", True),
                        ('annecdotes sur M64:', "M64 est particulièrement remarquable par ses deux disques de gaz et d’étoiles qui tournent en sens opposés. Le disque interne contient les importantes bandes de poussière visibles autour du centre, tandis que le disque externe présente une contre-rotation. Cette configuration pourrait être le résultat d’une fusion passée avec une petite galaxie riche en gaz orbitant en sens rétrograde, ou de l’accrétion progressive de gaz provenant du milieu intergalactique.La galaxie possède une activité particulière en son centre : elle est classée à la fois comme galaxie de Seyfert 2 et comme galaxie LINER. Elle contient également des régions d’hydrogène ionisé et une faible source d’émission radio. Malgré cela, son taux global de formation d’étoiles est faible et M64 est considérée comme une galaxie anémique.M64 serait relativement isolée, puisqu’elle pourrait être une galaxie du champ, c’est-à-dire une galaxie qui n’appartient pas à un groupe ou à un amas important. Elle est donc gravitationnellement plus isolée que de nombreuses autres galaxies du catalogue de Messier.", True),
                                            ],
                     "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546931037609795675/NGC_4826_-_HST.png?ex=6ae772cb&is=6ae6214b&hm=713df94c28d89c9946e1c35aceb639c79433433cc040a960d2217b68602a543a&",
                     "image": 'https://www.messier-objects.com/wp-content/uploads/2015/07/Messier-64-location.png',
                     "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                        },                                              
    "m65": {
                     "alias": ["NGC 3623"],
                     "titre": "M65",
                     "description": "M65 (NGC 3623) est une galaxie spirale située dans la constellation du Lion, à environ 39,9 millions d’années-lumière de la Terre. Elle mesure environ 113 000 années-lumière de diamètre et présente une magnitude apparente de 9,3. Sa classification varie selon les sources, mais elle est généralement décrite comme une galaxie spirale ordinaire ou intermédiaire. Un trou noir supermassif se trouve au centre de M65. Une estimation fondée sur la luminosité infrarouge proche de son bulbe lui attribue une masse d'environ 13 millions de masses solaires.",
                     "champs": [
                        ("découverte de M65:", "M65 a été découverte par Charles Messier le 1er mars 1780. Contrairement à plusieurs objets de son catalogue, Messier ne mentionne aucune découverte antérieure par son ami Pierre Méchain. L'attribution de la découverte à Méchain, encore présente dans certaines sources, provient en réalité d'une erreur de William Henry Smyth, qui l'avait également attribuée à Méchain pour M66 et M68.", True),
                        ('annecdotes sur M65:', "M65 fait partie du Triplet du Lion, avec M66 et NGC 3628. Ces trois galaxies appartiennent au groupe de NGC 3627, qui comprend également NGC 3593. Un autre classement regroupe ces quatre galaxies avec NGC 3596 et NGC 3666, faisant du Triplet du Lion un sous-groupe d'un ensemble de six galaxies.M65 a également été le théâtre d'une supernova de type II, appelée SN 2013am, découverte le 21 mars 2013 par l'astronome japonais Matsuo Sugano.", True),
                                            ],
                     "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546951781290876980/070601.jpg?ex=6ae6dd5d&is=6ae58bdd&hm=e093a2032ce109e910278ba449f237b1f90147de4ffbf71d6f2fe64f07923f8b&",
                     "image": 'https://www.messier-objects.com/wp-content/uploads/2015/07/Messier-65-and-66-location.png',
                     "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                        },                                              
    "m66": {
                     "alias": ["NGC 3627"],
                     "titre": "M66",
                     "description": "M66 (NGC 3627) est une galaxie spirale intermédiaire située dans la constellation du Lion, à environ 31,4 millions d’années-lumière de la Terre. Elle mesure environ 85 200 années-lumière de diamètre et possède une magnitude apparente de 8,9. Elle est également classée comme galaxie active de type Seyfert 2 et comme LINER. Son trou noir supermassif au centre possède une masse comprise entre 6,8 et 15 millions de masses solaires. Une autre estimation, fondée sur la luminosité infrarouge du bulbe, donne environ 13 millions de masses solaires.",
                     "champs": [
                        ("découverte de M66:", "M66 a été découverte par Charles Messier en 1780. Comme pour M65, aucune mention d'une découverte antérieure par Pierre Méchain n'apparaît dans les notes de Messier. L'attribution de sa découverte à Méchain vient d'une erreur de William Henry Smyth, reprise ensuite par d'autres sources.", True),
                        ('annecdotes sur M66:', "M66 est la galaxie la plus brillante du groupe de NGC 3627, qui comprend quatre galaxies : M66, M65, NGC 3628 et NGC 3593. M65, M66 et NGC 3628 forment le célèbre Triplet du Lion. Un classement plus large ajoute NGC 3596 et NGC 3666, faisant de cet ensemble un groupe de six galaxies.M66 est particulièrement intéressante pour ses supernovas : cinq ont été observées entre 1973 et 2018. Une a été particulièrement étudiée en 1989, sa luminosité ayant atteint une magnitude visuelle de 12,0 et son déclin ayant été inhabituellement lent. M66 a également subi une interaction gravitationnelle avec NGC 3628. Cette rencontre a profondément perturbé les deux galaxies et a notamment entraîné une concentration de matière stellaire et gazeuse dans le centre de NGC 3628, ainsi que l'arrachage d'une importante quantité d'hydrogène neutre provenant de ses bras spiraux. Ces interactions contribuent aux structures particulières observées dans le Triplet du Lion.",True)
                                            ],
                     "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1546953035169661000/Phot-33c-03-fullres.jpg?ex=6ae6de88&is=6ae58d08&hm=77cff0d0de8d22d0c14d2a5e5569337400d46c53afa8722b1c7d853d17208ca1&",
                     "image": 'https://www.messier-objects.com/wp-content/uploads/2015/07/Messier-65-and-66-location.png',
                     "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                        },                                              
    "m67": {
                     "alias": ["NGC 2682"],
                     "titre": "M67",
                     "description": "M67 (NGC 2682) est un amas ouvert situé dans la constellation du Cancer, à environ 2 960 années-lumière du Système solaire. Il mesure environ 22 années-lumière de diamètre et possède une magnitude apparente de 6,9. Son âge reste incertain : les estimations vont de 2,6 à 5 milliards d’années, tandis que sa masse est estimée entre 1 080 et 1 400 masses solaires. L’amas contient plus de 500 étoiles.",
                     "champs": [
                        ("découverte de M67:", "M67 a été découvert par l’astronome allemand Johann Gottfried Koehler en 1779. Johann Elert Bode aurait cependant observé l’amas peu avant cette date, sans parvenir à distinguer ses étoiles avec ses instruments. Charles Messier l’a ensuite ajouté à son catalogue le 6 avril 1780.", True),
                        ('annecdotes sur M67:', "M67 est un amas particulièrement intéressant pour étudier l’évolution stellaire. Ses étoiles sont presque toutes situées à la même distance et ont approximativement le même âge, tandis que la faible quantité de poussière qui nous sépare de l’amas permet de les observer relativement facilement. Il contient notamment plus d’une centaine d’étoiles semblables au Soleil et de nombreuses géantes rouges.La présence de nombreuses étoiles semblables au Soleil et l’âge de M67 ont conduit à l’hypothèse selon laquelle le Soleil pourrait y être né. Cependant, des simulations numériques montrent que cette hypothèse est très peu probable. Une étude réalisée avec le télescope spatial Kepler a par ailleurs montré que des étoiles de M67 âgées d’environ 4 milliards d’années ont une période de rotation d’environ 26 jours, proche des 27,28 jours du Soleil.Enfin, trois exoplanètes ont été découvertes dans M67 grâce à l’instrument HARPS. YBP 1194b et YBP 1514b sont deux Jupiters chauds, avec respectivement des masses d’environ 0,33 et 0,4 masse de Jupiter. La troisième, SAND 364b, orbite autour d’une géante rouge et possède une masse d’environ 1,5 masse de Jupiter. M67 fait ainsi partie des rares amas ouverts dans lesquels des exoplanètes ont été découvertes.",True)
                                            ],
                     "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1547284267783163934/M67-Star-Cluster.png?ex=6ae76a44&is=6ae618c4&hm=a0d710384902cf3664c5346c728059ffef782363b1e3a03559f362bbde02d9b2&",
                     "image": 'https://www.messier-objects.com/wp-content/uploads/2015/07/Messier-67-location.png',
                     "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                        },                                              
    "m68": {
                     "alias": ["NGC 4590"],
                     "titre": "M68",
                     "description": "M68 (NGC 4590) est un amas globulaire de classe X situé dans la constellation de l’Hydre, à environ 33 600 années-lumière du Système solaire. Il possède une magnitude apparente d’environ 7,3 à 7,96, un diamètre réel d’environ 106 années-lumière et une masse estimée à 2,23 × 10⁵ masses solaires. Son âge est estimé à environ 11,52 milliards d’années.",
                     "champs": [
                        ("découverte de M68:", "M68 a été découvert par l’astronome français Charles Messier le 9 avril 1780 et ajouté à son catalogue la même année.", True),
                        ('annecdotes sur M68:', "M68 se rapproche actuellement du Système solaire à environ 112 km/s. Son orbite autour de la Voie lactée est très excentrique, avec une excentricité de 0,5, ce qui l’éloigne jusqu’à environ 100 000 années-lumière du centre galactique.M68 pourrait être en train de se contracter vers son centre et présente des signes de rotation sur lui-même. Une hypothèse propose également qu’il pourrait être issu de la capture par la Voie lactée d’une petite galaxie satellite.En 2015, 50 étoiles variables avaient été identifiées dans M68, dont 28 découvertes par Harlow Shapley en 1919-1920. La majorité sont des RR Lyrae, tandis que six sont des étoiles variables de type SX Phoenicis, caractérisées par des variations rapides et de forte amplitude.", True),
                                            ],
                     "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1547284824350527559/Messier_68_Hubble_WikiSky.jpg?ex=6ae76ac9&is=6ae61949&hm=7711d136069f17a90efd23b4637bdafbc3d5d7e076e7f74fb8a8a2eafeb7eff2&",
                     "image": 'https://www.messier-objects.com/wp-content/uploads/2015/07/Messier-68-location.png',
                     "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                        },                                              
    "m69": {
                     "alias": ["NGC 6637"],
                     "titre": "M69",
                     "description": "M69 (NGC 6637) est un amas globulaire situé dans la constellation du Sagittaire, à environ 28 700 années-lumière du Soleil et à environ 5 550 années-lumière du centre de la Voie lactée. Il possède une magnitude apparente de 7,64, une masse d’environ 105 000 masses solaires et un âge estimé à 13,06 milliards d’années. Son diamètre réel est estimé à environ 59 années-lumière, ou jusqu’à 82 années-lumière sur les photographies à très longue exposition.",
                     "champs": [
                        ("découverte de M69:", "Charles Messier a découvert M69 le 31 août 1780, la même nuit que M70. Il recherchait alors un objet nébuleux catalogué par Nicolas-Louis de Lacaille sous la désignation Lac I.11, qu’il avait cherché sans succès en 1764. Messier pensa avoir retrouvé cet objet, mais M69 était en réalité beaucoup moins lumineux que celui observé par Lacaille.", True),
                        ('annecdotes sur M69:', "L’amas est presque parfaitement circulaire, avec une ellipticité de seulement 0,01. Son cœur, compact et brillant, mesure environ 3 minutes d’arc, tandis que sa concentration stellaire intermédiaire lui vaut la classe V de Shapley-Sawyer. Selon la manière de mesurer ses extensions, son diamètre réel est estimé entre 59 et 82 années-lumière.M69 est relativement riche en éléments lourds pour un amas globulaire du halo galactique. Les estimations de sa métallicité vont de −0,90 à −0,64 [Fe/H], ce qui correspond à une concentration en fer comprise entre 13 et 23 % de celle du Soleil. Son âge, estimé à environ 13,06 milliards d’années, montre toutefois qu’il s’agit d’un amas très ancien.", True),
                                            ],
                     "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1547285343735255192/Cosmic_riches.jpg?ex=6ae76b45&is=6ae619c5&hm=b258adeb642e6f2185c281e5ece9047ceea2055c0cb55b974e7a7f8b172a777b&",
                     "image": 'https://www.messier-objects.com/wp-content/uploads/2015/07/Messier-69-location.png',
                     "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                        },  
    "m70": {
                     "alias": ["NGC 6121"],
                     "titre": "M70",
                     "description": "M70 (NGC 6681) est un amas globulaire situé dans la constellation du Sagittaire, à environ 29 350 années-lumière de la Terre et 7 175 années-lumière du centre de la Voie lactée. Il possède une masse d’environ 179 000 masses solaires, un diamètre réel d’environ 68 années-lumière et un âge estimé à 12,8 milliards d’années. Sa magnitude apparente est de 7,87 et il appartient à la classe de concentration V.",
                     "champs": [
                        ("découverte de M70:", "M70 a été découvert par Charles Messier le 31 août 1780, la même nuit que M69. Messier le décrit alors comme une nébuleuse sans étoiles. William Herschel fut le premier à parvenir à résoudre ses étoiles, le 13 juillet 1784. L’amas fut ensuite observé à plusieurs reprises par John Herschel avant d’être intégré au General Catalogue of Nebulae and Clusters, puis au catalogue NGC sous la désignation NGC 6681. Une première photographie de M70 fut réalisée par Heber Doust Curtis et publiée en 1918.", True),
                        ('annecdotes sur M70:', "M70 est presque parfaitement sphérique, avec une ellipticité de seulement 0,01. Sa taille apparente de 8′ correspond à environ 68 années-lumière de diamètre réel. Sa vitesse radiale est d’environ 216,6 km/s selon les mesures de Gaia, ce qui signifie qu’il se déplace rapidement par rapport au Soleil.Son cœur est extrêmement dense et l’amas a subi un effondrement gravitationnel de son noyau au cours de son histoire. Ce phénomène concerne également plusieurs autres amas globulaires de la Voie lactée, notamment M15 et M30.M70 ne possède que deux étoiles variables connues, toutes deux de type RR Lyrae, et son centre abrite également deux traînardes bleues. Aucun pulsar n’y a été découvert, même si une étude de 2016 a identifié une source de rayonnement gamma pouvant potentiellement être associée à des pulsars millisecondes.", True),
                                            ],
                     "thumbnail": "https://cdn.discordapp.com/attachments/1545471786496426118/1547285940827987988/Messier70-HST-Potw1215a.jpg?ex=6ae76bd3&is=6ae61a53&hm=2c9b97e2d45dea7787fe4123b6928ce2f8f94071f87cba4e5453abba907b1ef4&",
                     "image": 'https://www.messier-objects.com/wp-content/uploads/2015/07/Messier-70-location.png',
                     "footer": 'l\'image de localisation provient de messier objects merci a eux'
                                        },                                              
                                                                    }


class Rechercheastre(discord.ui.Modal, title="Rechercher un astre"):
    nom_astre = discord.ui.TextInput(
        label="Nom de l'astre",
        placeholder="ex: si tu recherches m81 tu tomberas sur m81"
    )

    async def on_submit(self, interaction: discord.Interaction):
        recherche = self.nom_astre.value.lower().strip()

        astre_trouve = None
        for cle, infos in ASTRES.items():
            if recherche == cle or recherche in infos["alias"]:
                astre_trouve = infos
                break

        if astre_trouve is None:
            await interaction.response.send_message("Aucun résultat trouvé.", ephemeral=True)
            return

        embed = discord.Embed(
            title=astre_trouve["titre"],
            description=astre_trouve["description"],
            color=discord.Color.blue()
        )
        for nom_champ, valeur_champ, inline in astre_trouve["champs"]:
            embed.add_field(name=nom_champ, value=valeur_champ, inline=inline)

        embed.set_thumbnail(url=astre_trouve["thumbnail"])
        embed.set_image(url=astre_trouve["image"])
        embed.set_footer(text=astre_trouve["footer"])

        await interaction.response.send_message(embed=embed)


@bot.tree.command(name="astreinformation", description="obtiens des information sur un astre et sur comment l'observer")
async def astroobjet(interaction: discord.Interaction):

    buttonsearch = Button(label='commencer la recherche', emoji="🔭", style=discord.ButtonStyle.green)

    async def button_callback(interaction):
        await interaction.response.send_modal(Rechercheastre())

    buttonsearch.callback = button_callback

    view = View()
    view.add_item(buttonsearch)

    embed = discord.Embed(
        title='comment utiliser cette commande',
        description="pour commencer la recherche il faut cliquer sur le bouton ci dessous pour rechercher un astre il faut rentrer soit son nom (sans fautes svp et en français) ou alors son nom dans le catalogue (messier/ngc)",
        color=discord.Color.blue()
    )

    await interaction.response.send_message(embed=embed, view=view)

DEFINITIONS ={
    "nova": {
        "alias": ["novae"],
        "titre": "Nova",
        "description": "Une nova est une explosion thermonucléaire se produisant à la surface d'une naine blanche, dans un système binaire, lorsque celle-ci accumule suffisamment de matière (généralement de l'hydrogène) provenant de son étoile compagnon. Contrairement à une supernova, la naine blanche survit à l'explosion et le phénomène peut se reproduire plusieurs fois.",
        "champs": [
            ("différence avec une supernova", "Une nova n'entraîne pas la destruction de l'étoile, alors qu'une supernova marque la fin catastrophique d'une étoile massive ou d'une naine blanche.", True),
        ],
        "thumbnail": None,
        "image": None,
        "footer": None
    },
    "système binaire": {
        "alias": ["binaire",],
        "titre": "système binaire",
        "description": "Un **système binaire** est un système astronomique regroupant deux objets de l'espace (habituellement des étoiles, mais aussi des planètes, des galaxies, des astéroïdes ou des trous noirs) qui sont proches, et que leur interaction gravitationnelle fait orbiter autour d'un centre de masse commun nettement distinct de chacun d'eux. Dans le cas des étoiles binaires, cette exigence n'est pas forcément requise.",
        "champs": [
            ("dans la fiction","Les étoiles binaires et les systèmes d'étoiles sont abondants dans les films Star Wars et leurs produits dérivés, l'exemple le plus connu étant le système dans lequel est située la planète Tatooine.",True)
        ],
        "thumbnail": None,
        "image": 'https://upload.wikimedia.org/wikipedia/commons/6/6c/Pluto-Charon_System.gif?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original',
        "footer": None
    },


}




class Recherchedefinition(discord.ui.Modal, title="Rechercher une définition"):
    terme = discord.ui.TextInput(
        label="Terme à rechercher",
        placeholder="ex: nova, trou noir supermassif, supernova..."
    )

    async def on_submit(self, interaction: discord.Interaction):
        recherche = self.terme.value.lower().strip()

        definition_trouvee = None
        for cle, infos in DEFINITIONS.items():
            if recherche == cle or recherche in infos["alias"]:
                definition_trouvee = infos
                break

        if definition_trouvee is None:
            await interaction.response.send_message("Aucun résultat trouvé.", ephemeral=True)
            return

        embed = discord.Embed(
            title=definition_trouvee["titre"],
            description=definition_trouvee["description"],
            color=discord.Color.dark_blue()
        )
        for nom_champ, valeur_champ, inline in definition_trouvee["champs"]:
            embed.add_field(name=nom_champ, value=valeur_champ, inline=inline)

        if definition_trouvee["thumbnail"]:
            embed.set_thumbnail(url=definition_trouvee["thumbnail"])
        if definition_trouvee["image"]:
            embed.set_image(url=definition_trouvee["image"])
        if definition_trouvee["footer"]:
            embed.set_footer(text=definition_trouvee["footer"])

        await interaction.response.send_message(embed=embed)


@bot.tree.command(name="astrodictionnaire", description="obtiens la définition d'un terme d'astronomie")
async def astrodictionnaire(interaction: discord.Interaction):

    buttonsearch = Button(label='rechercher un terme', emoji="📖", style=discord.ButtonStyle.primary)

    async def button_callback(interaction):
        await interaction.response.send_modal(Recherchedefinition())

    buttonsearch.callback = button_callback

    view = View()
    view.add_item(buttonsearch)

    embed = discord.Embed(
        title='dictionnaire astronomique',
        description="clique sur le bouton ci-dessous pour rechercher la définition d'un terme d'astronomie (nova, supernova, trou noir supermassif...)",
        color=discord.Color.dark_blue()
    )

    await interaction.response.send_message(embed=embed, view=view)




    
    
if __name__ =="__main__"  : 
 bot.run(os.getenv('DISCORD_TOKEN'))