
label chapter2:

    #Chapter Title Background

    play music ordinary_day
    play audio birds

    m "I am riding in the back of a cart clattering down a cobblestone street, jostling around with unidentified bags that seem like grain."

    m "The city around me is bright and bustling. People dressed in European Renaissance-style clothing scatter this way and that, and a sour smell permeates my nose that I soon realize is coming from the horses pulling the cart."
    
    m "My arms and legs tingle with something like numbness, and I look down to see myself in unfamiliar clothing— the same clothing as the avatar I picked only moments ago. I poke at my arms and legs as the numbness fades, pinching and prodding."
    
    m "Maybe I fell asleep? Maybe something knocked me unconscious?"
    
    m "I scratch at my arm. A red line wells up. I do not wake up."
    
    m "I bite my lower lip. Hard. The iron taste of blood hits my tongue and I wince at the sting."
    
    m "I do not wake up."
    
    m "\"What the f—\""

    m "What the f—"    

    # driver
    u "\"Oh, good, you’re finally awake!\""
    
    m "I yelp with surprise and turn to the driver, who waves genially and offers me a smile."
    
    # driver
    "Driver" "\"We’re almost to the castle. The stewardess will meet you outside.\""
    
    m "I can’t help but think that maybe I’m dead. Maybe the library exploded and this is some strange version of an afterlife."
    
    m "I pull myself up to a more comfortable sitting position and look around me, noticing a canvas bag in my lap that I assume is mine."
    
    m "The strange thing about it, though, is that something inside the canvas bag is moving."

    # fairy
    u "\"Hey! Hey, you! Let me out!\" A small, muffled voice cries from inside the bag."
    
    m "I glance up at the driver, but he doesn’t seem to have heard, his eyes firmly on the road in front of us."
    
    m "Slowly and carefully, I undo the drawstring at the top of the bag."
    
    play sound sparkle
    stop audio
    
    m "A shower of pink and gold sparkles erupts from the bag as a tiny figure zooms out of the opening. I blink in surprise, scrunching up my nose at what appears to be a tiny… fairy?"
    
    #Sprite: Fairy full body
    show fairy sprite at right
    
    f "\"About time you let me out of there! It’s so stuffy.\" She says, brushing what appears to be glitter off her tiny body as she shakes out her arms and legs."
    
    m "\"Am… I dead?\""
    
    m "It’s the first thing that comes out of my mouth. I can’t help it."
    
    m "The fairy comes closer, all her annoyance draining as her eyebrows raise in concern."
    
    # TODO
    # Sprite: fairy zoom in
    
    f "\"Oh. Oh, no, though you’re not the first one to think that,\" she says. \"You found the game, didn’t you?\""
    
    m "\"The… game?\""
    
    f "\"The game at the library. You found it, right?\""
    
    m "\"Yes?\""
    
    m "At this point I’m feeling much more like crying than conversing, but it’s the closest to anything that’s made sense at all in the last several minutes, so I do my best to keep it together."
    
    f "\"You’re in the game now.\""
    
    m "I blink at the fairy very, very slowly."
    
    f "\"You hit start, you go into the game. That’s how it works. Now you’re the character you picked."
    
    m "\"That’s impossible.\""
    
    f "\"Would you rather be dead like you thought you were?\""
    
    m "I cross my arms over my chest grumpily."
    
    m "\"… No.\""

    f "\"Great. Step one, accomplished. You’re not dead, you’re just in a video game.\""

    # TODO
    # DIALOGUE CHOICE, NO EFFECT [What do you mean I’m in a game? / You’re out of your mind. / Clearly I am dreaming.]
    menu:
        "What do you mean I’m in a game?":
            jump choice_tutorial
        "You’re out of your mind.":
            jump choice_tutorial
        "Clearly I am dreaming.":
            jump choice_tutorial
    
    label choice_tutorial:

    m "\"WHAT WAS THAT?\""
    
    f "\"That was a choice box! You’re in a visual novel game, so you get to make choices about what to do. You’ll see them pop up on screen every now and then.\""
    
    m "\"Can everyone else see them, too?\" I wondered. That had to be weird for people casually walking around to see dialogue boxes pop up."
    
    f "\"Uh… no. That’s the thing. They sort of… don’t know they’re in a video game. They can’t see me, either.\""
    
    m "\"Are you telling me that I appear to be talking to myself right now?\""
    
    f "\"…Yes. Pretty much, yes.\""
    
    m "\"I… have been dropped into my own isekai webcomic.\" I flop back against the side of the carriage, eyes fixed hopelessly on the middle space."
    
    f "\"Congratulations?\""
    
    m "\"Not really. It doesn’t often end too well for the protagonists.\""
    
    f "\"… Maybe let’s not focus on that part.\""
    
    m "\"So what exactly would you suggest we focus on, then? Because I don’t know about you, but I am absolutely panicking.\""
    
    f "\"Okay, okay, okay, okay, uhhhhhhh firstly—don’t do that. No panicking allowed.\""
    
    m "I roll my eyes. \"Great. Top tier advice, ten of ten.\""
    
    f "\"Do you want my help or are you gonna sit here and sass me?\" the fairy asks, crossing her tiny arms."
    
    m "\"Fine. What do I do, then?\""
    
    f "\"Well, firstly, it looks like we’re heading towards the gates of the castle, so… let’s see where this cart takes us.\""
    
    m "\"… Your plan is \"play the tutorial and cross our fingers?\" Great.\""
    
    f "\"……. Well, unless you’ve got anything better, that’s what we’re going with. Oh, wow, check out those turrets!"
    
    m "\"For the record? Not a subtle subject change. At all.\""
    
    m "However, I have to admit that she’s right. There really isn’t another choice at the moment, unless we want to jump off a back of a moving cart, of course, and the cart does seem to be moving in the direction of a massive castle."
    
    m "As we come closer, I realize that there seems to be a huge, fenced-in pasture around the entire castle that encloses a herd of happily grazing sheep. They are the fluffiest, whitest, and largest sheep I’ve ever seen in my life, two to three times bigger than the typical domestic ones on earth farms."
    
    m "Earth farms? Come to think of it, are we even still on earth? Where am I? Do the typical rules of earth physics even apply here, much less societal norms?"
    
    m "I sigh, cursing a blue streak under my breath. It’s probably best to assume that the answer is no."
    
    # TODO
    # Background: town scene, zoom in on castle
    
    "Driver" "\"Okay, this is our stop! Everyone out.\""
    
    m "\"Thank you!\" I wave at the driver and do my best to gracefully jump down from the back of the cart, hoping that he isn’t expecting any money. I suspect earth cash would be useless here, if I was even wearing my own clothes and could attempt to fish a couple coins from my lint-ridden pockets."
    
    m "As my feet hit the ground, my boot heel catches in a particularly slippery spot of mud. I screech, flailing wildly as I try and fail to maintain balance, but just before I land in the dirt, someone grabs my arm and pulls me upright."
    
    u "\"Careful, there!\""
    
    # TODO 
    # Background: Leslie intro CG
    
    # TODO
    # Music: Leslie Theme
    
    m "A tall woman with neatly styled blonde hair and a broad smile stands before me, holding my upper arm in a tight grip for a moment until she is sure that I am steady."
    
    le "\"Good to meet you. I’m Leslie, the castle stewardess,\" she says with a broad smile."
    
    # TODO
    #Background: town scene, zoom in on castle
    
    # TODO
    #Sprite: Leslie zoom

    show leslie sprite at center
    
    le "\"I assume you’re the new librarian we’ve been waiting on? It’s such a relief! The space needs organizing badly.\""
    
    m "I glance at the fairy as subtly as I can, noting that it seems like Leslie is also unable to see her. The tiny woman makes a shooing motion with her hands, mouthing something that is too small for me to lip read."
    
    m "\"I’m… the librarian?\" I say hesitantly. However, I quickly realize it sounded like a question, so I clear my throat and straighten my posture jus a little. \"Th— that is, I am the librarian. Yes. That’s me.\"" 
    
    m "Leslie claps her hands together in excitement."
    
    le "\"Wonderful! Follow me inside and we’ll get you settled. I’m sure you’ve heard that it’s a big job, so we’ll get you started right away.\""
    
    m "She starts walking towards a wooden door, clearly a side entrance, so quickly that I have to scramble to catch up, just hoping that the fairy doesn’t lose track of me as I dodge other members of the castle staff going about their business."
    
    m "At least, I presume they’re staff. They’re dressed in practical clothing and seem to be rushing about as though they know where they’re going, carrying boxes or baskets or lists this way and that. Essentially, they’re doing the opposite of me, and I’m positive I stick out like a sore thumb as I simply try not to run into anyone before I can slip inside the door."
    
    # TODO
    #Background: castle hallway left

    #TODO
    #Music: Fantastical Day
    play music fantastical_day
    
    m "The door leads into a long hallway with several branching paths off either side, but it is significantly less crowded than outside. The stone walls are simple and practical, with high and narrow windows that make the place look like it was built as a fortress rather than a place of luxury and comfort."
    
    m "A few comforts stand out despite the construction style, though. A plush carpet covers the stone floors, muffling the sound of footsteps that otherwise might echo in the corridor. Along the walls, both providing insulation and an additional source of muffling sound, are thick, white tapestries. Each one bears the image of a crest stitched on with brown thread that seems to shimmer gold in the hallway’s low lighting."
    
    m "As we pass, I sneak a closer look, noticing that the crest has a diagonal slash across it and bears two symbols, one on either side of the line. One is clearly a rose in full bloom, while the other appears to be a very simple, but very clear drawing of a massive sheep."
    
    #TODO
    #Sprite: Leslie full body
    
    le "\"Oh, admiring the crests? It’s beautiful work. Our weavers are the best in all the surrounding kingdoms.\""
    
    m "\"The… sheep is unexpected,\" I murmur." 
    
    #TODO
    #Sound: sheep bleat
    play sound sheep_short
    
    m "Leslie giggles."
    
    le "\"You must have traveled from very far away, indeed. The noble sheep is our national animal!\" she says proudly. \"We specialize in raising and caring for them, crafting with their wool, and living harmoniously with them as a species.\""
    
    m "\"So… everyone here is a shepherd?\" I ask, eyebrows raised."
    
    le "\"Oh, of course not!\" She presses a hand to her chest, eyes wide. \"Only the most skilled become shepherds. The profession is handed down from parent to child among those in the noble class. The job is difficult, but highly coveted and respected.\""
    
    m "I blink slowly. \"The nobles are shepherds here? How… cool.\""
    
    m "No, honestly. I really think it’s cool. There’s a part of me that is both fascinated by and loves the fact that shepherds are their noble class, that the people who are working the hardest to keep the economy running are the ones who are societally revered."
    
    m "As someone who grew up in farming country, I think I could get behind a setup like this."
    
    le "Leslie turns to me, brow furrowed. \"I assure you that we are currently in the warmer season, but if you require heavier clothing, I can find some for you.\""
    
    m "\"Oh! Uh… No, thank you. I’m fine. It’s a… local expression, I suppose.\" Note to self: watch out for modern slang…"
    
    m "I pause, suddenly wondering how these people are speaking modern English at all. Wouldn’t a fantasy world have its own completely different language as well as a different culture? How are they even speaking an approximation of the kind of English that I know?"
    
    f "\"It’s the game translating for you based on your language settings,\" the fairy says. \"Sorry, I can kind of hear your thoughts if you think too loud. Some things go by fantasy world rules, because I guess we ARE in a different world… but it’s still a game. If you can have dialogue boxes, you can have translation settings."
    
    m "I… guess that makes sense? If I think about it too hard, it might start to not make sense, though, so I put a pin in it for later."
    
    m "I also wonder how it’s even possible to think loudly, but decide not to question it, especially in front of Leslie, who is still casually spouting facts about the kingdom’s economy, which does appear to be entirely based on… sheep and sheep products." 
    
    le "\"Of course, the subject of mutton and mutton-related products is always a tricky thing, but the procedures for ethical treatment of sheep have been very much improved in the last two decades…\""
    
    m "I catch onto snippets of Leslie’s explanation as we walking, trying to drink in as much of the castle as possible. Though we seem to be traveling through a complex system of corridors, I do my best to make note of our path. It would be a good idea to know the lay of the land so I can move around easily, especially considering I am still not quite certain what the goal of this story actually is." 
    
    m "I am so absorbed in trying to make a mental map of the space that I round the next corner without paying proper attention, running face-first into a solid wall of dark-toned metal."
    
    #TODO
    #Sound effect: crash
    play sound crash
    
    m "There is an awful clanging sound as I bounce off the object like a cartoon character with a muffled cry, covering my poor nose where it smashed against the hard surface. As I rub the bridge of my nose, I look up to see that it was not an object at all. It was a person."
    
    #TODO
    #CG: Tarran introduction
    
    #TODO
    #Music: Tarran Theme
    play music tarran_theme
    
    m "A tall man in gunmetal-toned armor with gold accents stands in front of me. His blonde hair drapes slightly over his right eye, shining almost white in the sunbeam coming through one of the high windows. He smiles, well, sheepishly as he looks down at me."
    
    u "\"Sorry about that. Leslie says I need to be more aware of my surroundings.\" He extends  his hand for a welcoming shake."
    
    

    t "\"I’m Tarran, Knight of the Crystal Fleece.\""
    
    m "\"Nice to meet you. I’m the… new librarian. [player_name],\" I say, trying not to sound too hesitant."
    
    t "\"Oh, that’s wonderful! I know Leslie has been looking forward to your arrival. We don’t have anyone trained for that in the castle, so we’ve had to go looking. I know I certainly couldn’t help,\" he says with a chuckle."
    
    # TODO
    #Background: back to normal

    # TODO
    #Sprite: Tarran, Leslie
    
    show tarran sprite at right
    show leslie sprite at center


    # TODO
    #Music: fantastical day
    play music fantastical_day

    
    m "Leslie rolls her eyes and gently bats at Tarran’s arm."
    
    le "\"Don’t let him fool you. He’s one of our absolute finest around here, top of his class and almost at the top of our knightly ranks.\""
    
    m "Tarran’s cheeks turn red as he shrugs. It’s almost cute, in a way, "
    
    t "\"I am proud of what I do, but I am not blind to the fact that I have weaknesses as well. One person can never do everything.\""
    
    le "\"He’s too modest.\" She smiles softly and turns back to me. \"I’m sure you’ll see each other around here and there. It’s good that we all met on the way to the library.\""
    
    t "\"Best of luck!\" he says genially, giving a wave. \"I should get back to my post, but it was very nice to meet you. I hope we’ll see each other again soon. Don’t stay hidden in that dusty old archive for too long.\""
    
    m "\"Archive?\" I murmur as Tarran walks away."
    
    # TODO
    #Exit: Tarran sprite
    hide tarran sprite
    
    le "\"Oh, yes. It’s in a terrible state. The main library is decently organized, but I’m afraid the archive room is a true disaster,\" she says with a long sigh. \"It’s been used as a storage space for objects that simply have no other home for far too long, and now we… Wel, we simply can’t find a thing.\""
    
    m "\"Am I going to run into magical brooms if I open the door too quickly?\" I joke half-heartedly as I follow Leslie down the hall, images of Mickey Mouse flitting through my brain."
    
    le "\"Brooms, no, though I’m afraid you might need them. There are plenty of items in the archive of a more magical nature, though, so I suggest you take care… but then again, you’re the expert on these things! I’m sure you already know anything I might be able to tell you.\""
    
    m "Just as I am mentally calculating how to explain that I certainly do NOT know everything that Leslie thinks that I do without making myself sound delusional or useless, Leslie comes to a dead stop in front of a pair of large double doors. I only barely avoid running into her, stumbling back a step or two as she turns towards me."
    
    le "\"Here we are!\"" 
    
    m "Leslie gestures to the double doors with a wide smile and reaches into her pocket with her free hand, pulling out a clanking ring of ancient-looking keys. She picks a particularly rusty one and inserts it into the lock on the door, turning it with a sickening clank."
    
    m "It seems like the doors themselves are protesting against being opened, and I can’t help but empathize."
    
    m "When the squeaking hinges finally give way, there are no dancing brooms on the other side. In fact, it mostly looks like a normal library."
    
    # TODO
    #Background: library 1
    scene bgp
    
    m "It’s a room full of books. It’s dark and dusty, of course, the only light filtering in through the large stained glass window with a decorative image of a fluffy sheep surrounded by roses. Other than the dust, though, it really doesn’t look too bad, and I say as much to Leslie."
    
    le "\"Oh, this is just the main library area. It’s a bit disused, but other than that it’s alright. The real problem is…\""
    
    m "She trails off, making her way to the far side of the room, where a wooden door in the wall is almost entirely obscured by shadows. A part of me thrums with anticipation, wondering if all the fantasy stories I read as a child are true, if there’s a secret passage or a hidden stairway."
    
    m "Leslie throws opens the door and shrieks, diving out of the way. I am not fast enough."
    
    # TODO
    #CG: comical moment, if time, just the hand sticking up from the boxes
    
    m "A pile of boxes made of something that feels suspiciously like Fantasy Cardboard comes crashing down on me and I stumble, landing on my rear on the hard wooden floor. The boxes simply keep falling, covering me in an avalanche of papers and clanking, random objects. They aren’t terribly heavy, but there are many of them, and the shock is enough to keep me pinned to the floor until the sound of falling objects finally ceases."
    
    le "\"Are you alright?!\""
    
    m "Leslie carefully begins to dig through the pile, removing boxes until she’s able to grab my hand and pull me upright."
    
    # TODO
    #Background: library 2
    scene bgp
    
    le "\"I know it’s been quite a while since I’ve walked into the archive, but I didn’t think it had gotten that bad!\" She shudders slightly, looking between me, the pile, and the open door in abject horror."
    
    m "\"It’s okay, I’m not hurt.\" Only my pride, that is. I brush some dust off with a shrug and surreptitiously rub my rear."
    
    m "My pride… and maybe my tailbone."
    
    le "\"I’ll go get you some cleaning supplies,\" Leslie says a little awkwardly. \"Why don’t you… ah…\""
    
    m "Leslie trails off helplessly and I shrug, bending down to pick up a random box."
    
    m "\"I’ll get started.\" I place the box on one of the empty library tables and take off the top, finding a stack of papers inside written in a language I can’t identify."
    
    le "\"You’re sure you’re not injured?\"" 
    
    m "I look up before I have time to process the documents. \"Oh, I’m okay! No worries.\""
    
    le "\"As long as you’re certain. I’ll be back in a moment.\""
    
    m "Leslie shuffles out the door and I turn back to the documents in the box. I squint at the lines, frowning. I can read cursive just fine, but whatever language this is, it’s not English."
    
    m "\"Hey, Fairy?\" I whisper. \"Why aren’t my translation settings working on these?\""
    
    # TODO
    #Sprite: Fairy full body
    show fairy sprite at right
    
    f "\"Hmm?\" She pops up in a shower of sparkles, seemingly out of nowhere. \"What do you mean they’re not working?\""
    
    m "I simply gesture at the pages in response. The fairy flies closer, as if trying to make sense of the situation, herself."
    
    u "\"An interesting question, isn’t it?\""
    
    m "I bite back a scream at the unexpected masculine voice that echoes around the room, whirling towards the library door. Then I bite back another scream at the figure who stands near the door, simply watching."
    
    # TODO
    #Add character sprite: bird man/Lorenzo
    show lorenzo sprite at center
    
    # TODO
    #Music: Lorenzo’s Theme
    play music lorenzo_theme
    

    u "\"Would you like some assistance with that?\" He tilts his head towards the stack of papers, the beak of his bird mask bobbing, ignoring how I am most certainly staring at him in abject confusion and horror."
    
    m "I am half waiting for a system dialogue to pop up, but after a few seconds, nothing does. Instead, I nod very slowly, almost imperceptibly, every muscle in my body tense as the man in what appears to be a plague doctor costume comes closer."
    
    m "The bird man pulls a short stick from his pocket and taps the edge of the box with it twice. As if in response, the ink on the pages begins to shift and shimmer, reforming itself into entirely new lines of text… that I can now read."
    
    m "\"How did you do that?\" I ask, snatching up the topmost page, marveling that I can suddenly make out records of castle comings and going from what before meant nothing at all to me."
    
    u "\"All games have glitches now and then. Consider me something of a… patch. Mm. Yes, I like that. I’m the Patcher.\""
    
    m "I raise my eyebrow, gaze suddenly locked on the dark glass in the eye holes of the bird mask. \"Games?\""
    
    u "He laughs softly. \"No need to play more games with me. We both already know you’re in a very high-stakes one right now.\""
    
    f "\"I don’t like this…\""
    
    "Patcher" "\"Why? Because I happen to know more than you? Because you’re a part of a glitchy system code? Pride is a terrible weakness, my dear. Easily exploited.\""
    
    m "The fairy practically quivers with rage, and I don’t blame her. I’m shaking, too, but I can’t put my finger on which emotion the adrenaline comes from – rage, fear, curiosity, or some combination of all three. Then I realize something—"
    
    m "\"You can see her?!\" I thought the NPCs couldn’t see her because she was a part of the game system."

    "Patcher" "\"I see more than you realize. For example, I saw when you dropped into this world from your library.\""
    
    m "\"If you know so much, then tell me how I’m supposed to get out of here.\""
    
    m "The fairy tugs at the fabric of my sleeve, shaking her head frantically, but I ignore her for now. She wasn’t even completely sure how to leave the game. It wouldn’t hurt to hear some more information from whoever might be able to help."
    
    "Patcher" "\"Easy enough,\" he says with a shrug. \"Organize the archive.\""
    
    m "I blink slowly."
    
    m "\"That’s… that’s seriously it?\""
    
    "Patcher" "\"That’s it.\""
    
    "Patcher" "\"There may, of course, be attempts to distract you along your way. A game has to have some challenge, after all. If you succeed in your task, the game will reset, kicking you out in the process and returning you home.\""
    
    m "I squint, hackles still raised. I don’t entirely trust him, but it’s not like I have any other leads at the moment."
    
    m "\"Do I have a time limit?\""
    
    "Patcher" "\"I’m afraid that depends entirely on you. I can’t say more than that.\""
    
    m "I huff and sit down on a nearby stood, resting my head in my hands. \"Thanks. I think.\""
    
    "Patcher" "\"You are quite welcome.\" He turns, footsteps retreating towards the library doors."
    
    "Patcher" "\"I will say, though: if I were you, I wouldn’t delay.\""
    
    m "As the last folds of his dark cloak swish out the door, I rise from my stool and chase after him, calling out as I scramble out the doorway."
    
    m "\"Wait— !\""
    
    m "But when I step outside the library, the long hallway is completely empty."
    
    # TODO
    #SCENE SHIFT, fade to black and ticking clock noise
    
    # TODO
    #Background: archive room
    
    # TODO
    #Music: main character waltz
    play music mc_theme
    
    # TODO
    #Sprite: fairy full body
    show fairy sprite at right
    
    f "\"Well, at least we have all the boxes cleared now.\""
    
    m "\"We? I think you mean me,\" I huff, sitting the last of the fallen boxes in an organized stack to the side of the room."
    
    m "It’s been hours just trying to put the boxes of papers into stacks of vaguely related files. I haven’t even started on the boxes of random objects yet, but I think it would be best to simply get into the room now and see what else is there beyond just a mountain of unorganized papers."
    
    m "Leslie eventually came back with a mop, a broom, a pile of rags, and a bucket for cleaning, but the room was just now in a state where I could really start sweeping. I picked up the broom and shook my head."
    
    m "\"Too bad the only cleaning tools are human-sized,\" I grumble."
    
    f "\"Hey, I can’t help I’m just a system help guide. I’m made for information, not strength!\""
    
    m "\"Well, can you get some information on how to light those lamps? It’s getting dark.\" I gesture to the oil lamps lining the walls. There were also one or two on the tables around the room. Unfortunately, there weren’t any wicks in them when I checked earlier."
    
    f "\"Oh, that part’s easy,\" she says with a laugh. \"Just push the button!\""
    
    m "I blink very slowly at her before I turn to one of the lamps."
    
    m "\"The… button?\""
    
    m "Sure enough, upon closer inspection there is a button on the base of one of the table lamps. It’s white, inlaid with something that looks like mother-of-pearl, and there’s a vague clicking noise when I press it."
    
    m "A shower of sparkling lights comes from seemingly nowhere, glowing and floating inside the lamp like a small swarm of fireflies, and it casts a much brighter light than I would have expected."
    
    m "\"They have electricity here? Advanced,\" I mutter, blinking in the bright light."
    
    f "\"Not exactly. They’re magic lights.\""
    
    m "I open my mouth to speak, but immediately close it again. I’m stuck in a video game. There are clearly weirder things happening than magic light sources, and I have other things to worry about."
    
    m "For example: getting home before time runs out. Whatever time that might be…"
    
    m "I walk over to the archive door, which is actually a room about the size of a large broom closet… or my graduate office that I share with three other people. Running my hand across the wall in the darkness, I find another sconce with a button switch and turn on the lamp."
    
    m "I wish I could say the room looks better in the light, but it does not. It’s simply a clearer version of a big mess. One medium-sized table sits against the far wall, but at least I can’t say it’s dusty— there are papers, boxes, and strange objects littering the surface for any of the dust to reach the tabletop."
    
    m "\"Is this an archive or a lost and found room?\" I ask, wrinkling my nose."
    
    f "\"Looks like both to me.\"" 
    
    m "\"Motherclucker,\" I mutter, and then stop, eyes wide. \"… Cluck? Cluck. Cluck!\""
    
    f "\"That’s the censoring. This is a PG game.\""
    
    m "\"Don’t PG rated things get like ONE cluck??\""
    
    f "\"We err on the side of caution,\" she says. \"Anyways, are you concerned about the library or your sailor mouth? We have things to do.\""
    
    # TODO
    # 
    #While the player and Fairy look at objects in the archives, different music plays to indicate the backstory of each object. Fairy makes note of this, telling the player they can learn things from the music associated with each item because it changes when you pick them up, and they might be able to return some of them to their owners and clean up the archive if they pay attention. The player asks why they can hear the music if the others can’t, and Fairy explains it’s because they aren’t from this world. They have some advantages because they’re working in the game system. The first object they come across is an old pocket watch.
    
    # TODO
    #Overlay: pocket watch close up image
    
    # TODO
    #Choice: HAVE YOU HEARD THIS MUSIC BEFORE? 
    #[Yes, from Leslie;
    # Yes, from Tarran;
    # No, I haven’t heard it before]

    label music_choice:    
        menu:
            "Yes, from Leslie":
                jump yes_leslie
            "Yes, from Tarran":
                jump yes_tarran
            "No, I haven't heard it before":
                jump no

    label no:    

        f "\"I don’t know, sounds kinda familiar to me. I’m almost positive we’ve heard it before.\""

        jump music_choice
    
    label yes_leslie:
    
        f "\"Mmmmm, I don’t think that’s quite right. Is there anyone else we’ve met?\""

        jump music_choice
    
    label yes_tarran:
        f  "This sounds like Tarran’s theme! Let’s go bring this to him and see what he says."


    m "We find Tarran outside, looking out over a wide meadow inhabited by overlarge, fluffy clouds."
    
    m "Nope. Wait. Those are sheep."
    
    # TODO
    #Background: pasture
    scene bgp

    #Sprite: Tarran full
    show tarran sprite at center
    

    #Music: Tarran’s Lullaby
    play music tarran_theme
    
    # TODO
    #Sound: occasional sheep bleats, repeated
    play sound sheep_long loop
    
    m "I stumble slightly as I notice the sounds around me. It’s not just the sheep, it’s something I had tuned out altogether before simply because I wasn’t paying proper attention."
    
    m "It almost sounds like… a lullaby."
    
    t "\"Well met, good librarian!\" Tarran says as I come closer, clearly oblivious to the tiny fairy hovering by my shoulder."
    
    m "\"Well met,\" I repeat a little awkwardly. I fish around in my borrowed satchel for a moment before pulling out the box with the silver pocket watch inside."
    
    m "Tarran’s go wide as he immediately brightens, reaching out for the box."
    
    # TODO
    #Music: castle day/neutral positive encounter music
    
    t "\"Where on earth did you manage to find this? I’ve been looking for it for ages!\""
    
    m "He laughs excitedly as he opens the box, tracing his fingers over the elegant swirling designs on the watch cover with incredible care."
    
    m "\"I’m glad I was able to return it,\" I say genuinely. Seeing the look on his face is heartwarming, despite my personal situation. ]At least now I can g]et back to the library, though. This was a nice pick-me-up, but I do have a job to do."
    
    t "\"This watch brings back many memories,\" he mutters, eyes sparkling."
    
    m "It’s almost like he doesn’t see me at all in that moment. Something about the nostalgia written all over his body language is intriguing, but I don’t know how much time I have to linger here."
    
    # TODO
    #CHOICE OPTION: 
    #Quietly leave him and go back to the library [MINUS 2 AFFECTION], 
    #Make your excuses and head back to your task [NO CHANGE], 
    #Ask about the watch [PLUS 2 AFFECTION]
    
    # affection[0]
    menu:
        "Quietly leave him and go back to the library":
            $ affection[0] = -2
            jump leave_quiet
        "Make your excuses and head back to your task":
            $ affection[0] = 0
            jump make_excuses
        "Ask about the watch":
            $ affection[0] = 2
            jump watch

    # TODO
    label leave_quiet:
    
        m "While Tarran is lost in thought, I carefully back away from him to sneak back to the library. He doesn’t seem to notice my moments, completely caught up in his memories."
    
        jump encounter_skip
    # TODO
    #[REDIRECT TO TARRAN ENCOUNTER SKIP POINT]
    
    # TODO
    label make_excuses:
    
        m "\"It’s very good to see you, but I should be heading back.\""
        
        m "Tarran jumps, as if surprised to find someone else standing here."
        
        t "\"Oh. Ah… of course. Thank you for returning this. It is very important to me.\""
        
        m "\"You’re very welcome.\""

        jump encounter_skip
    
    # TODO
    #[REDIRECT TO TARRAN ENCOUNTER SKIP POINT]
    
    label watch:
    
        m "\"That watch must be very special to you,\" I say carefully, stepping just a little closer."
        
        m "Tarran finally looks up from the box, blinking as though coming out of a daze."
        
        t "\"Forgive me, I was… somewhere else,\" he mutters. \"Yes, it is very important to me. It belonged to my father.\""
        
        m "\"Family heirloom. I should have guessed,\" I say with a smile. \"It’s a beautiful piece.\""
        
        t "\"It is, but the appearance isn’t what makes it important. Truthfully, the mechanism is broken. It doesn’t even run properly anymore.\""
        
        m "\"Then why…\" I trail off, unsure how to ask, but Tarran only smiles and carefully closes the box."
        
        t "\"When I had nightmares as a child, my father would sing me back to sleep. It was dark in our home, but I remember seeing the moonlight glinting off his watch. He said the watch didn’t run, but the ticking went perfectly with the tempo of the lullaby.\""
        
        t "\"When I grew older and moved away from home, he gave me the piece as a memento. It’s a symbol of both comfort and bravery for me.\""
        
        m "\"I think that’s a beautiful story.\""
        
        m "I mean it, too. We all have pieces of memories tucked away in corners around us."
        
        m "However, just at that moment, something occurs to me."
        
        m "\"Tarran… do you remember that lullaby?\""
        
        t "\"I do, but I’m afraid I’m not much of a singer,\" he says with a soft laugh."
        
        m "\"Could you try? Please?\""
        
        play music tarran_theme
        
        m "Tarran’s eyes narrow for a moment, betraying his curiosity over the odd request, but he nods and begins to hum the tune. It’s short and simple, the perfect little piece for a children’s song, but what chills me to the core is that I know I have heard this music before."
        
        m "It is the piece that played when I opened the watch box in the first place. It is the piece playing now, the one that Tarran can’t hear, the one that represents him."
        
        m "At that moment I realize how truly precious the memory is to him and how much that old, broken watch represents a part of his core memories and ideals. It is so essential to his personality that it has become the music that identifies him as a character."
        
        m "It is… humanizing, really. Logically, I know he’s not real. I know that he’s an NPC and this is a video game I’m trying to escape, but something is haunting about the symbolism of that music. Even if he isn’t a real human person with a real life and real dreams, he seems like it, just for a second."
        
        m "\"Those must be very precious memories.\""
        
        m "Tarran’s expression suddenly turns dark, and he nods solemnly."
        
        t "\"I can’t recall much of my childhood. It’s mostly vague impressions, like a smile or a touch. A lullaby.\""
        
        m "\"Did… something happen to your memories?\""
        
        t "\"I…\" he pauses, squinting into the distance for a moment, and then a look that can only be described as pained crosses his face."
        
        t "\"I think it must have been an accident. You know, knights and horses and sheep going off cliffs. It… must have been,\" he says, shaking his head. \"It doesn’t matter, though. This is who I am now.\""
        
        m "\"The ballad of Sir Tarran…\" I mutter contemplatively, gazing off into the distance."
        
        t "\"Just Tarran, please.\""
        
        m "\"Not a fan of the title you worked so hard for?\""
        
        t "\"Not particularly,\" he says with a laugh. \"I find it gives others the notion that a knight is all that I am, and I am not fond of the idea that a person can live life as one specific thing.\""
        
        t "\"Like you, for example. Surely a librarian is not all that you are.\""
        
        m "\"I mean that… is my only job, if that’s what you’re asking?\""
        
        t "\"Not your job, no. I’m asking what you are. You, as a person, not the task you are paid to do.\""
        
        m "I blink at him in bewilderment, scrambling to latch onto something."
        
        m "\"I… like to… crochet, I guess?\" It’s a shot in the dark, but he smiles."
        
        t "\"That is a very good something else to be,\" he says, nodding approvingly. \"Even if you sound uncertain.\""
        
        m "\"I guess I… I’ve had this idea in my head of what I’m supposed to be for so long that I kind of never stopped to consider what I liked doing. And now I… don’t know that I know any more.\""
        
        m "There is a long silence between us as an uncomfortable feeling of uncertainty settles in my chest."
        
        m "\"Will you sing that lullaby for me again?\" I ask softly. \"I’d like to hear it.\""
        
        m "He smiles and nods shyly, opening his mouth again to sing, but then something in the distance catches his eye."
        
        t "\"Oh. That isn’t good,\" he mutters."
        
        m "I follow his gaze to the far side of the field, where the fence is nearly obscured by a tangle of leaves that looks suspiciously like Fantasy Kudzu."
        
        m "Looking past the fantasy version of arguably the most annoying plant in existence, I finally see what he’s pointing out. Part of the fence has collapsed, but it’s nearly impossible to see because of the vines. The sheep haven’t gone through the gap yet, but it’s likely only a matter of time before it causes trouble."
        
        t "\"I suppose that means break time is over,\" he says with a sigh, rising to his feet. \"We have work to do. I won’t ask you to stay and repair the fence with me, though.\""
    
    # TODO
    # FLAG
    #CHOICE OPTION 

    #I’m afraid I’ve been gone too long already (-1 affection)
    #I can stay if you like… (no change)
    #I’d like to help (+1 affection)]
    
    # affection[1]
    menu:
        "I’m afraid I’ve been gone too long already":
            $ affection[1] = -1
            jump choice2_bad
            # -1 affection
        "I can stay if you like… ":
            $ affection[1] = 0
            # no change
            jump choice2_neutral
        "I’d like to help":
            # +1 affection
            $ affection[1] = 1
            jump choice2_good


    # I’m afraid I’ve been gone too long already
    label choice2_bad:

        #Music: protagonist’s waltz
        play musci mc_theme
        
        m "\"Sorry, I’m afraid I’ve been gone too long already. I should really get back to the library.\""
        
        t "\"Well, in any case, thank you for bringing me this,\" he says, holding up the watch. \"I’m glad to have it back.\""
        
        m "I smile, but I’m not sure it reaches my eyes. The worry over getting back to my job and winning this game is starting to get back to me."
        
        m "\"I’ll see you around, then?\""
        
        t "\"Indeed,\" he says with a polite nod."
    
        jump encounter_skip
    

    # I can stay if you like
    label choice2_neutral:

        play music mc_theme

        m "\"I can stay if you want…\" I say hesitantly, but I think he can probably hear the worry in my voice."
        
        m "The anxiety of being away from the library, from the thing I’m supposed to be doing to get home, for too long is already starting to eat at me, and I’ve barely been out of the room."
        
        t "\"That’s alright. I can handle this.\" He briefly places a reassuring hand on my shoulder. \"You go on.\""
        
        m "\"Thank you,\" I say with a smile, my relief palpable."
    


        jump encounter_skip

    #I’d like to help
    label choice2_good:
    
    
        #Music: protagonist’s waltz
        play music mc_theme
        
        m "\"I’ll help,\" I say, and Tarran’s eyebrows raise."
        
        t "\"You certainly don’t have to.\""
        
        m "\"I know, but I can use a hammer and it seems like it would be easier with an extra pair of hands. Let me help. I’m enjoying being outside.\""
        
        m "Truthfully, I’ve spent far too much of the last few years indoors. I’m either in a library, an archive, or staring at a computer screen reading articles, creating lessons, doing who knows what else… and I’m kind of done with it."
        
        m "Not entirely, of course. I do like some parts of it, but being here with Tarran is making me wonder what I was missing outside in the sunlight all that time. I remember going camping with my parents as a kid, hanging out in a hammock under trees, and even going on long hikes through creeks and near waterfalls as a teenager."
        
        m "Why don’t I do that anymore, I wonder?"
        
        # TODO
        #Music: pasture theme
        
        m "It really doesn’t take long to fix the fence. Maybe 20 minutes at most, though I can tell it’s easier with a second pair of hands. Some rope, a new board, and a few long nails have everything back in place, and the sheep just bleat on like nothing is happening during the entire process."
        
        m "Unfortunately, after the fence is fixed, I can’t make any excuses to stay outside. I shouldn’t keep Tarran from his job, and I have my own work to do… Which, now that I think of it, is really starting to make me anxious."

        jump encounter_skip        
    
    label encounter_skip:
    
        m "As I turn to leave, I notice that someone new is walking towards us."
        
        # TODO
        #CG: Noah introduction
        
        # TODO
        #Music: Noah theme
        #play music noah_theme
        
        m "His long brown hair is so dark that it’s almost black. There is a naturally golden-blonde streak on one side, the light color peeking and out of a braid thrown over his shoulder. His green eyes are soft and kind, but the simple circlet and heavily embroidered doublet he wears puts me on edge."
        
        t "\"Good afternoon, Your Majesty.\""
        
        u "\"To you as well,\" he says politely, nodding his head towards us before he turns to me. \"I don’t believe we’ve met.\""
        
        m "\"We… um… have not. Your Majesty?\" I stumble and stutter over my words as I look up at the newcomer. Is he a prince? A king? Some other noble rank I haven’t heard of? I don’t know what the etiquette is for greeting a noble in this world."
        
        m "… Not that I would know the etiquette for that in my own world, but that’s beside the point."
        
        t "\"This is [player_name], the new castle librarian. [player_name]¸meet Prince Noah.\""
        
        # TODO
        #Background: pasture
        scene bgp

        #Sprites: Tarran and Noah 

        show noah sprite at right
        show tarran sprite at center
        
        m "\"It’s nice to meet you, Your Majesty,\" I say as calmly as I can, forcing a nervous smile that probably looks as awkward as it feels. The prince waves his hand in protest."
        
        n "\"Please, just call me Noah. At least… while no one else is around, it is certainly fine with me if you do.\" He smiles softly, as if trying to soothe any stray nerves."
        
        n "\"I just came to speak to Tarran, but I’m glad I caught you. I was in a meeting when you arrived this morning and couldn’t greet you myself. Welcome to Phenai.\""
        
        m "\"Thank you. I’ll… um… see you both around?\""
        
        m "They both nod, and that’s enough of a cue for me to bid them an awkward goodbye and take my leave. I need to get back to the library." 
        
        #Background: fade to black

        jump chapter3