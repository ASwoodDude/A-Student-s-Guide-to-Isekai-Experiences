# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Melody", image="mc")

# Music
define audio.ordinary_day = "audio/Music/reflected-light USE FOR ORDINARY DAY.mp3"
define audio.mc_waltz = "" # TODO

# Sounds
define audio.footsteps = "Sound Effects/footsteps-all.mp3"
define audio.clicking = "Sound Effects/mouse-click-153941.mp3"
define audio.sheep_short = "Sound Effects/single sheep bleat.mp3"
define audio.explosion = "Sound Effects/explosion-6801.mp3"

# Placeholders
image bgp = "images/Placeholder Assets/Background Placeholder.jpg"
image cgp = "images/Placeholder Assets/CG Placeholder.jpg"

#locations
    

# The game starts here.

label start:


    # TODO
    scene bgp

    play music ordinary_day

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.


    m "It is far too early to be awake right now."

    play sound footsteps

    m "I’m headed to the local university library to work on a research project."

    m "Looking back, I’m not sure what I expected when I applied to graduate Musicology programs, but I’m also not sure it was this."

    m "My bag is full of books, my head is full of fog, and I don’t really want to be awake at the moment, but we do what we need to do."

    # TODO
    # This shouldn't change anything, but putting it here for background change later
    # Background: Modern Library Inside
    scene bgp

    m "The equally sleepy librarian halfheartedly waves hello as I enter, and I wave back with as much of a smile as I can muster at 7AM."

    m "However, as I go to unpack my things at my usual desk, I realize that I forgot the charging cord for my laptop. And, unfortunately, it is completely dead."

    m "Heaving a sigh, I slide the laptop back into my bag and decide that instead of going all the way home and risking a parking dilemma when I return, I’ll work on one of the library computers for the day and save my research to the cloud for later."

    # TODO
    # This shouldn't change anything, but putting it here for background change later
    # Background: Modern computer, off
    scene bgp

    m "The library recently acquired new computers, finally upgrading from the old, 3:4 ratio clunky monitors with curved glass screens they’d had for twenty years. The old head of the library argued that the monitors still worked, so there was no need to replace them, but as soon as he retired, the new hire immediately started upgrading technology."

    # TODO
    # This shouldn't change anything, but putting it here for background change later
    # Background: Modern computer, off
    scene bgp

    m "It’s a relief to know that I’ll at least be working on updated technology today, but before I can click the icon to open a browser, something strange catches my eye."
    
    m "I squint, leaning in close to the screen to get a better look at what appears to be a storybook icon. There is no name or description under the small image, just a book with a red cover and gold pages."
    
    # TODO slashes
    # m /"What the heck is that…?"/ "I mutter under my breath."
    
    m "What the heck is that…?"

    m "I mutter under my breath."

    m "I have plenty of time, I think."
    
    m "Let’s find out."

    play sound clicking

    # TODO
    # This shouldn't change anything, but putting it here for background change later
    # Background: Modern computer, off
    scene bgp

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
        # play music m_waltz
        play music ordinary_day

        m "Well… I’m curious. It won’t take long. I’ll just take fifteen minutes and see what this is about, and then I’ll get back to my morning research."

        m "I click the ‘new game’ button."

        python:
            name = renpy.input("ENTER PLAYER NAME: ")

            name = name.strip()

        "WELCOME, \[PLAYER NAME\]"

        m "Wow, not great programming there, but okay. Fine."

        "YOU HAVE BEEN HIRED AS THE NEW CASTLE LIBRARIAN FOR THE KINGDOM OF PHENAI."

        "PHENAI HAS A RICH CULTURAL HISTORY AND A THRIVING ECONOMY DEPENDENT ON SHEPHERDS AND PRODUCTS DERIVED FROM SHEEP."

        m "Did… did that say sheep?"

        play sound sheep_short

        m "It did. Okay."

        "PLEASE CHOOSE YOUR UNIFORM AND REPORT TO THE CASTLE STEWARDESS FOR DETAILS ON YOUR FIRST ASSIGNMENT."

        # TODO
        # Fade background to white?
        # There's a saturation thing I saw
        # https://lemmasoft.renai.us/forums/viewtopic.php?t=8243

        # TODO 
        # Forward Slash
        # m /"What’s— What’s happening?"/
        m "What’s— What’s happening?"

        m "I close my eyes against the sudden bright flash, so bright it seems like it couldn’t possibly be coming from an ordinary computer screen, but it does no good. The bright white light burns through my eyelids and I scream in shock and pain, body crumpling as I curl away from the blast."

        play sound explosion

        m "I wonder if something in the library has exploded, if there’s something wrong with the lighting, or maybe if the world has just suddenly… ended."

        m "I guess in that case, at least I wouldn’t have to write my dissertation."

        m "Finally, after seconds or minutes of terror, I dare to crack my eyes open, but the sight is… not what I expected, to say the least."

        jump choice1_done

    label choice1_no:

        m "I'd rather not."

        m "Guess we'll just sit here."

        jump choice1_done

    label choice1_done:

        # ... the game continues here.
 

        jump chapter2

        # ... the game continues here.