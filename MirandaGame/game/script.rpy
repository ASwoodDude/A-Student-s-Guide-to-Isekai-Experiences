


# Characters
# Sorta in order of appearance

default affection = [0,0,0,0,0,0,0,0,0,0]
default player_name = ""

# Melody (MC)
define m = Character("Melody", image="mc",color="#F17AA2")

# unknown standin
define u = Character("???")

# Fairy
define f = Character("Fairy",image="fairy")

# Tarran
define t = Character("Tarran",image="tarran",color="#FFF176")

# Kylie
define k = Character("Kylie",image="kylie",color="#F28B20")

# Noah
define n = Character("Noah",image="noah",color ="#5D96C4")

# Leslie
define le = Character("Leslie",image="leslie",color="#63B367")

# Lorenzo
define lo = Character("Lorenzo",image="lorenzo",color="#BD70CA")



# Music
define audio.ordinary_day = "audio/Music/reflected-light USE FOR ORDINARY DAY.mp3"
define audio.library_ambient = "audio/Music/ambient-classical USE FOR LIBRARY.mp3"
define audio.home_menu = "audio/Music/home menu twinkle.mp3"
define audio.fantastical_day = "audio/Music/acoustic-guitars.mp3"
define audio.bad_end = "audio/Music/Bad End.mp3"
define audio.castle_theme = "audio/Music/Phenai theme castle march.mp3"
define audio.kitchen = "audio/Music/kitchen music.mp3"
define audio.pasture = "audio/Music/pasture music medieval abbey.mp3"

# Themes
define audio.mc_theme = "audio/Music/ProtagonistTheme.mp3"
define audio.lorenzo_theme = "audio/Music/Lorenzo Theme.mp3"
define audio.tarran_theme = "audio/Music/Tarran's Lullaby.mp3"
define audio.leslie_theme = "audio/Music/Leslies Theme.mp3"
define audio.kylie_theme = "audio/Music/Kylies Theme.mp3"
define audio.tarran_theme = "audio/Music/Tarrans Lullaby.mp3"
define audio.noah_theme = "audio/Music/Noahs Theme.mp3"


# Sounds
define audio.footsteps = "Sound Effects/footsteps.mp3"
define audio.clicking = "Sound Effects/mouse clicking.mp3"
define audio.sheep_short = "Sound Effects/single sheep bleat.mp3"
define audio.sheep_long = "Sound Effects/Sheep long for loop.mp3"
define audio.explosion = "Sound Effects/explosion.mp3"
define audio.birds = "Sound Effects/Bird chirp long for loop.mp3"
define audio.sparkle = "Sound Effects/fairy twinkle.mp3"
define audio.crash = "Sound Effects/crash.mp3"
define audio.menuclicking = "Sound Effects/menu button clicking.mp3"
#define audio.pages = ""


# Placeholders
image bgp = "images/Placeholder Assets/Background Placeholder.jpg"
image cgp = "images/Placeholder Assets/CG Placeholder.jpg"

# Sprites
image fairy sprite = Image("images/Sprites/fairy sprite.png",oversample=16,ypos=.2)
image leslie sprite = Image("images/Sprites/leslie sprite.png",oversample=4)
image kylie sprite = Image("images/Sprites/kylie sprite.png",oversample=4)
image lorenzo sprite = Image("images/Sprites/lorenzo sprite.png",oversample=4)
image noah sprite = Image("images/Sprites/noah sprite.png",oversample=4)
image tarran sprite = Image("images/Sprites/tarran sprite.png",oversample=4)
image noah modern = Image("images/Sprites/noah modern.png",oversample=4)
# Backgrounds

# CGs
image cg painting = Image("images/CGs/lesliespainting.jpg")
image cg storybook = Image("images/CGs/storybook.jpg")
image cg unmasked = Image("images/CGs/lorenzo unmasked.jpg")

image white = "#ffffff"
image red = "#ff0000"

# Transitions
define flash = Fade(0.5, 0, 0.5, color="#FFFFFF")
define blood = Fade(0.5, 0, 0.5, color="#FF0000")

#transform

# Fairy Positions
transform fairycenter:
    xalign .5
    yalign .6

transform fairycenterleft:
    xalign .35
    yalign .6

transform fairycenterright:
    xalign .65
    yalign .6

# kitchen positions

transform kitcenterleft:
    xalign .25
    yalign 1.3
    zoom 1

transform kitcenterright:
    xalign .55
    yalign 1.3
    zoom 1

# General Positions

transform center:
    xalign .5
    yalign 1.3

transform centerright:
    xalign .65
    yalign 1.3

transform centerleft:
    xalign .35
    yalign 1.3

# Chapter 6, 4 person lineup

transform pos1:
    xalign .20
    yalign 1.3    

transform pos2:
    xalign .40
    yalign 1.3

transform pos3:
    xalign .60
    yalign 1.3

transform pos4:
    xalign .80
    yalign 1.3

# The game starts here.

label start:

    scene title cp1 with fade

    $ renpy.pause()

    scene bg library doors

    play music ordinary_day

    m "It is far too early to be awake right now."

    play sound footsteps

    m "I’m headed to the local university library to work on a research project."

    m "Looking back, I’m not sure what I expected when I applied to graduate Musicology programs, but I’m also not sure it was this."

    m "My bag is full of books, my head is full of fog, and I don’t really want to be awake at the moment, but we do what we need to do."

    m "The equally sleepy librarian halfheartedly waves hello as I enter, and I wave back with as much of a smile as I can muster at 7AM."

    m "However, as I go to unpack my things at my usual desk, I realize that I forgot the charging cord for my laptop. And, unfortunately, it is completely dead."

    m "Heaving a sigh, I slide the laptop back into my bag and decide that instead of going all the way home and risking a parking dilemma when I return, I’ll work on one of the library computers for the day and save my research to the cloud for later."

    scene bg computer

    m "The library recently acquired new computers, finally upgrading from the old, 3:4 ratio clunky monitors with curved glass screens they’d had for twenty years."

    m "The old head of the library argued that the monitors still worked, so there was no need to replace them, but as soon as he retired, the new hire immediately started upgrading technology."

    m "It’s a relief to know that I’ll at least be working on updated technology today, but before I can click the icon to open a browser, something strange catches my eye."
    
    m "I squint, leaning in close to the screen to get a better look at what appears to be a storybook icon. There is no name or description under the small image, just a book with a red cover and gold pages."
    
    m "\"What the heck is that…?\" I mutter under my breath."

    m "I have plenty of time, I think."
    
    m "Let’s find out."

    play sound clicking

    m "It’s… some kind of game, I guess?"

    m "I blink at the bright colors, glancing at the ‘new game’ button, but there is very little information. If I had to guess, it looks a bit like a visual novel, but I can’t be sure without playing."


    menu:

        "DO YOU WANT TO PLAY"

        "YES":
            jump choice1_yes

        "NO":
            jump choice1_no

    label choice1_yes:

        # TODO
        play music mc_theme

        m "Well… I’m curious. It won’t take long. I’ll just take fifteen minutes and see what this is about, and then I’ll get back to my morning research."

        m "I click the ‘new game’ button."

        python:
            name = renpy.input("ENTER PLAYER NAME: ")

            name = name.strip()

            player_name = name

        #"WELCOME, \[PLAYER NAME\]"

        "WELCOME, [[player_name]"

        m "Wow, not great programming there, but okay. Fine."

        "YOU HAVE BEEN HIRED AS THE NEW CASTLE LIBRARIAN FOR THE KINGDOM OF PHENAI."

        "PHENAI HAS A RICH CULTURAL HISTORY AND A THRIVING ECONOMY DEPENDENT ON SHEPHERDS AND PRODUCTS DERIVED FROM SHEEP."

        m "Did… did that say sheep?"

        play sound sheep_short

        m "It did. Okay."

        "PLEASE CHOOSE YOUR UNIFORM AND REPORT TO THE CASTLE STEWARDESS FOR DETAILS ON YOUR FIRST ASSIGNMENT."

        m "\"What’s— What’s happening?\""

        m "I close my eyes against the sudden bright flash, so bright it seems like it couldn’t possibly be coming from an ordinary computer screen, but it does no good." 
        
        m "The bright white light burns through my eyelids and I scream in shock and pain, body crumpling as I curl away from the blast."

        play sound explosion

        scene white with flash

        m "I wonder if something in the library has exploded, if there’s something wrong with the lighting, or maybe if the world has just suddenly… ended."

        m "I guess in that case, at least I wouldn’t have to write my dissertation."

        m "Finally, after seconds or minutes of terror, I dare to crack my eyes open, but the sight is… not what I expected, to say the least."

        jump choice1_done

    label choice1_no:

        m "I'd rather not."

        # Fade to white
        scene white with flash

        stop sound
        stop music

        jump chapter_1_ending

        # ... the game continues here.
        # Miranda said it should jump to one of the bad endings, need confirmation

    label choice1_done:

        stop music
        stop sound

        jump chapter2

        # ... the game continues here.