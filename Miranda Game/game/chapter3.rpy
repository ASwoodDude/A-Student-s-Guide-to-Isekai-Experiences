



label chapter3:


    # TODO
    #Background: chapter title
    
    # TODO
    #fade to library background
    
    # TODO
        #music: main character theme

    play music mc_theme
    
    m "I would say I’m done for the day. After all, I did spend this morning acclimating to an entirely different world, among plenty of other chores this afternoon…"
    
    m "Unfortunately, there is too much at stake for me to stop now."
    
    m "Even more unfortunately, when we make it back to the library, the lighting is absolutely terrible."
    
    m "The entire room is a swath of lumpy shadows and vague objects, the soft glow of the lamps doing very little to truly help me distinguish anything among the papers and boxes, and even my fairy friend sighs in distaste as we enter."
    
    # TODO
    #Sprite: fairy

    show fairy sprite at center
    
    f "\"You should really turn in for the night, you know? There’s only so much you can do in one day.\""
    
    m "\"What if one day is all I have, though?\" I whisper, turning to her with wide eyes."
    
    f "\"I know I’m just a system interface, but I think it would be okay if you wanted to sleep. I don’t know how much else you’ll get done like this.\""
    
    m "\"I’ve pushed through before when things needed to be done.\""
    
    m "And I have. I’ve always been good and finding time to make sure things get done, at squirreling away a few minutes here and an hour there to stay on track and juggle everything."
    
    m "What I’m not very good at is realizing when I need to rest, and it seems like the Fairy knows it too."
    
    f "\"Go get some sleep. We can keep going in the morning.\""
    
    m "\"But the sun JUST set, and—\" I pause suddenly, looking around the room. \"Do you hear that?\""
    
    # TODO
    # Music: Leslie theme
    # play music leslie_theme
    
    m "Ignoring the Fairy’s tiny squawks of protest, I carefully pick my way around the shadowy piles of boxes towards the source of the sound. It’s a little difficult to locate it in the growing darkness, but eventually my hand brushes a roll of canvas with something hard tucked inside."
    
    m "I grab the roll and bring it closer, the music that guides me growing a little louder as I bring it closer to my face, squinting through the shadows at the object. There is a leather cord tied around the roll, and I carefully undo it to see what is inside."
    
    # TODO
    #Image overlay: paintbrushes
    # ???
    
    m "It’s a tool roll, and it’s completely filled with paint tubes and paintbrushes. Looks like it belonged to some sort of artist, but I haven’t met anyone who has identified themselves as an artist since I arrived here."
    
    # TODO
    #CHOICE PROMPT: HAVE I HEARD THIS MUSIC BEFORE?

        # yes, from Leslie;
        # yes, from Noah;
        # no, I don’t recognize it

    label loopback:
        menu:
            "yes, from Leslie":
                jump choice3_leslie
            "yes, from Noah":
                jump choice3_noah
            "no, I don’t recognize it":
                jump choice3_no
    
    
    # TODO
    #yes, from Noah
    
        label choice3_noah:
            m "I think back to my earlier encounter with Prince Noah out in the field."
            
            # TODO
            #Background: pasture
            scene bgp
            
            # TODO
            #Music: Noah theme
            #play music noah_theme
            
            # TODO
            #Sprite: Noah
            show noah sprite at center
            
            m "As much as I think I’ve heard this tune somewhere before, I don’t think it was from him. His music sounds like something else, something softer and more fluid. I think it’s in a different meter, too, like a dance of some sort."
            
            # TODO
            #>> LOOP BACK TO CHOICE PROMPT & RESET VISUALS
            jump loopback
    
    # TODO
    #no, I don’t recognize it
        label choice3_no:
            m "Try as I might, I truly cannot place the tune, so I turn to the Fairy."
            
            f "\"Need some help?\""
            
            m "\"I can hear music from this, but I don’t think we’ve heard it before. Or… I’m not sure,\" I say uncertainly."
            
            f "\"This one might require you to think a little farther back,\" she says slowly. \"I know you know the answer.\""
    
            jump loopback

    # TODO
    #yes, from Leslie
    
        label choice3_leslie:
            m "Now that I think about it, this music really seems to feel like Leslie, not just play when I’m near her. It seems to indicate Leslie’s headstrong and practical personality, but I can’t quite put my finger on why."
            
            m "What confuses me more at the moment, truthfully, is why Leslie would own a set of paintbrushes."
            
            f "\"Well, come on! We can return these to Leslie on the way to your room to sleep. Works out perfectly.\""
            
            m "\"As long as you know where you’re going, because I will definitely get lost and have to sleep in the corner of the hallway if I have to figure out directions.\""
            
            m "The little fairy shakes her head in a way that makes me think she’s rolling her eyes."
            
            f "\"Just follow me. I can tell where anyone in the castle is at any time.\""
            
            m "I blink in astonishment."
            
            m "\"Seriously?\""
            
            f "\"Mmm-hmm! It’s to help you find people if you need to talk to them. Benefits of being a sentient interface and all.\""
            
            m "The gears in my mind start to turn, the ghost of a plan forming as we walk out of the library."
    
    # TODO
    #Background: castle hallway right
    # scene castle hallway
    
    # TODO
    #sprite: fairy
    show fairy sprite at right
    
    # TODO
    #music: peaceful exploration
    #play music peaceful_exploration
    
    m "\"So… if you can tell where anyone is at any time, can you find the bird mask man for me?\" He might have answers that I desperately need, and he’s the only one so far who seems to understand my situation… even if he was pretty cryptic about it."
    
    m "I’m so caught up in my thoughts that I almost don’t notice the Fairy has stopped flying in front of me and nearly crash into her."
    
    m "\"Whoa, what’s the holdup?\" I ask, skidding to a stop."
    
    f "\"I… can’t find him,\" she admits, eyes wide."
    
    m "\"You literally just told me that you could locate anybody.\""
    
    f "\"I should be able to,\" she grumbles. \"I should! I just can’t. It’s like he’s disappeared!\""
    
    m "My brow furrows as I sigh. That makes absolutely no sense at all, but I suppose it also doesn’t make any sense to be trapped in a video game in the first place."
    
    m "If nothing else, it definitely emphasizes the fact that the bird mask man is someone I need to find. Sooner or later, I’ll have to locate him."
    
    m "For now, though, I just follow the fairy down the hallway as we walk towards Leslie. At least I can knock one more item off my list today."
    
    m "It doesn’t take too long to find her. She’s sitting at a desk in a small office on the second floor, going over what looks like ledger sheets. I knock hesitantly on the open door frame and she looks up."
    
    # TODO
    #Background: hallway left
    # scene hallway left
    
    # TODO
    #sprite: Leslie
    show leslie sprite at center
    
    le "\"Oh! Come in.\""
    
    m "\"I’m just dropping this off on my way to turn in for the evening. It, um… felt like yours,\" I say carefully, trying to figure out the most logical way to explain it to someone who can’t at all hear the same music that I can."
    
    m "Leslie’s eyes go wide as she reaches for the brush roll."
    
    le "\"Oh, my! Did you find this in the archives? It’s been missing for so long!\""
    
    m "\"What… is it?\" I ask slowly. \"I did find it in the library, and I… thought you would be the person to ask about it since you know everyone.\""
    
    m "The lie comes easily enough. I don’t need to wind up sleeping in the dungeons tonight for spouting insanities, and it kind of makes sense. I suppose? If you squint."
    
    m "In any case, Leslie doesn’t question it, too preoccupied with running her fingers over the brushes and paints inside the cloth case. She holds it like it’s a precious treasure."
    
    # TODO
    #CHOICE OPTION: [ask about the case PLUS 2 AFFECTION; don’t ask MINUS 2 AFFECTION]

    # affection[2]
    menu:
        "ask about the case":
            # +2 Affection
            jump ask
        "don’t ask":
            # -2 Affection
            jump dont_ask
    
    # TODO
    #don’t ask:
    label dont_ask:
    
        m "It feels like I should say something at this moment, but I am utterly drained and my thoughts are in fragmented bits. I can’t seem to latch onto one."
        
        m "Besides, it’s probably not my business to ask."
        
        m "Instead, I wait patiently while Leslie has her moment with the brush roll. Only a few seconds later she tucks the canvas into her apron pocket, clears her throat, and looks up at me."
        
    
        jump leslie_skip
    
    label ask:
    
        m "\"That must be very special to you. You didn’t tell me you were an artist,\" I say lightly."
        
        # TODO
        #Music: Leslie’s theme
        #play music leslie_theme
        
        m "Leslie looks surprised, but she tucks the case into her apron pocket with a smile and a shrug."
        
        le "\"I suppose it’s common knowledge around here by now. Sometimes I forget that not everyone has seen me splattered in paint when I have a little time to myself.\""
        
        m "\"I’m surprised you have time,\" I say with a sigh. \"This seems like a busy place.\" I speak without thinking and for a moment wonder if I’ve offended her, but Leslie just nods along with my statement."
        
        le "\"It certainly is. However, if there’s anything that I’ve learned over time, it’s that sometimes you have to make time for things that help keep you healthy.\""
        
        le "\"… And sometimes the things that really hold us together are not food and sleep, but things we do that make us feel most like ourselves.\""
        
        m "I feel my muscles stiffen as she speaks, awkwardly shuffling my weight from foot to foot."
        
        m "\"So painting makes you feel… like… yourself?\" I ask slowly. Leslie smiles, placing a gentle hand on my shoulder."
        
        le "\"Painting is one of many things that make me feel like myself,\" she says dreamily. \"I spend so much of my time with my feet on the ground that picking up a brush feels like the key to balancing it.\""
        
        le "\"I don’t like having to be practical and pragmatic all the time,\" she admits. \"It’s my nature, in a way, but we can’t confine ourselves to one single nature and still be dimensional human beings, you know? We need variation. We need stability, yes, but we need… more than that.\""
        
        le "\"Stability alone is often not quite enough to make us truly happy.\""
        
        m "As she speaks, I realize that I can hear these things about her. I can hear it in the music that plays when she’s near. It’s like a reflection of what she’s saying, but in the form of sounds."
        
        m "Leslie’s theme is in 4/4 meter, strong and stable. It’s flowing and melodic, though, rather than structured and percussive. Despite her practical personality, she is a gentle person, knowing when to push for her way and when to compromise."
        
        m "The strings lend some sense of softness, too. Rather than the proud brass ensemble I keep hearing around the palace, this has some give and take to it."
        
        m "In Western music, strings are usually associated with classical European music or general art music, conservatory school traditions, and an air of refinement. Noble birth or a noble personality type would both be appropriate associations for string instruments."
        
        le "\"Hello, there?\""
        
        m "I jolt out of my mental analysis, embarrassed."
        
        m "\"Sorry.\""
        
        le "\"It’s okay. Wherever you went, it looked like you were thinking of something you enjoyed. Something that… set your wheels turning, you know? Like an itch you have to scratch.\""
        
        m "\"I… suppose,\" I say awkwardly. It’s been a long time since I enjoyed academia, but I admit it did feel good to put those skills to use and think through something that is, at the moment, of particular importance to me."
        
        le "\"That’s almost how I feel when I paint,\" she says softly, her hand going to the pouch of brushes in her pocket."
        
        le "\"Have you ever lost yourself in something and found later that you’re left with a sense of lightness? It’s almost a euphoric feeling, like everything you were carrying went into that activity and you’re able to be yourself once more, you’re able to see clearly again?\""
        
        m "\"I…\""
        
        m "\"I don’t know.\""

            
        # TODO
        #CHOICE OPTION: 

        # try and think of an experience PLUS 1 AFFECTION
        # say you can’t remember NO CHANGE
        # say you’ve never felt that MINUS 1 AFFECTION

        # affection[3]
        menu:
            "try and think of an experience":
                # +1 affection
                jump think_of_experience
            "say you can’t remember":
                # no affection change
                jump leslie_skip
            "say you’ve never felt that":
                # -1 Affection
                jump leslie_skip

        # TODO
        label think_of_experience: 
        
            m "\"Writing,\" I finally say, breaking the long silence. \"I feel like myself when I’m writing.\" I feel almost ashamed admitting it, but the corners of Leslie’s mouth turn upwards in a gentle smile."
            
            le "\"A very academic answer of you.\""
            
            m "\"Not really,\" I scoff, a shaking my head. \"I mean, I do write academically, but that’s… that’s just business. There’s an art to it, but it’s not… It doesn’t feel…\""
            
            le "\"It’s not the thing that speaks to you,\" she supplies, nodding."
            
            m "\"It’s not,\" I whisper, biting my lip."
            
            le "\"What is it you write that makes you feel alive, then?\""
            
            m "I hesitate for a moment. I don’t tell many people about this, not right away. I’m well aware that it seems like a silly pipe dream and not something that will advance my academic career in any way, but… it makes me feel like me."
            
            m "\"Fiction,\" I say, letting out a breath. \"I like writing novels, mostly. Sometimes short stories. I like thinking through the different aspects of building an entire world in my head, and I like working with characters and situations that I’d never be in myself.\""
            
            m "\"It’s a beautiful stretch for the imagination, and it’s a coping mechanism and a healing mechanism. It’s an art form, to me, to craft a good story and to put together something that not only means something to you, but communicates an idea or heals a wound in the way no other medium can.\""
            
            le "\"I think that’s wonderful.\" There’s a slight sheen to her eyes as she pats my shoulder."
            
            le "\"I admit, I’m surprised that you didn’t say music, though. I saw on your resume that you have a large amount of musical training.\""
            
            m "I blink in shock. I don’t really know what kinds of information these entirely fictional people have about me or how they got it, but she’s right. I do have music training. I’m a Musicology student. Perhaps that’s why I latched onto the sounds and musical pieces in this game so easily."
            
            m "\"If… I’m really, really honest,\" I say slowly, \"Music school systematically sucked the joy out of playing in a way that I’m not sure I’m ever really going to be able to recover from.\""
            
            m "Leslie pauses, seeming to think over her words for a long moment."
            
            le "\"I think that when you love something like that, it seeps into your bones.\""
            
            m "I blink at her."
            
            m "\"What… does that mean?\""
            
            le "\"It means that it’s still there with you in some form. Whenever you feel you can do it for yourself again, whenever you’re wondering if there’s any love left for it at all, it’ll find you again. Somehow.\""
            
            m "\"How can you be sure?\""
            
            m "I want her to be right. I really, really do. I would give anything to be able to enjoy music for the love of it again, to not associate it with stress and grades and some kind of intrinsic, inescapable tie to my entire sense of self-worth… but I’m not sure that’s possible."
            
            le "\"I used to work as a painter as a career. I had a shop in town.\""
            
            m "My jaw drops. \"You what now?!\""
            
            le "\"I gave it up for the same reasons you described. I realized that tying in something I loved so much with my primary source of income was actually quite bad for me mentally and emotionally. It works for some people, of course, but it did not work for me at all.\""
            
            le "\"It was a slow slide, but one day I realized that I simply didn’t enjoy painting any more. There was something that it used to have that was long, long gone, and I didn’t think I’d be able to get it back again, either.\""
            
            m "\"And you did,\" I whispered, eyes going to the brush roll sticking out of her apron pocket."
            
            le "\"It took a long time,\" she admits. \"I won’t say it was easy to undo those years of conditioning, but creating boundaries where you can helps. Taking time to paint— or to make music— just for yourself helps.\""
            
            m "I nod very slowly as some hidden knot in my chest that I didn’t know I had begins to ease."
            
            m "\"Maybe I’ll give that a try, then.\""
            
            le "\"I think you should. Maybe it would make you feel a little more like you again.\""
    
        label leslie_skip:

            play music fantastical_day
            
            le "\"It’s getting late. Are you going to the staff apartments? We can cut through the kitchens and get there faster. Follow me.\""
            
            m "I trail behind Leslie as she wanders through the castle’s maze of hallways and staircases. I’m already incredibly lost by the third turn we make, but her footsteps are confident, and very soon we find ourselves at the downstairs kitchens."
            
            # TODO
            #Background: kitchens
            scene bgp
            
            m "It’s a cozier space than I thought it would be, if I’m honest. I’ve never been in a kitchen that wasn’t completely modern before, and this is something entirely unfamiliar to me. The ghost of one or two embers glow in the bank of ashes in the hearth, heat still radiating even though the fire has long been put out. Magic-powered lamps cast a soft glow around the rest of the room, just enough to see by."
            
            m "Cloth covered baskets sit on the table, and the smell of sweets is in the air, possibly a treat for tomorrow’s breakfast. I’m so busy looking at the neatly stored cast iron cooking implements that I almost don’t notice the shadow move in the corner of the room."
            
            m "Instinct takes over and I flinch in surprise, turning towards the source of the movement. Leslie, however, barely reacts at all."
            
            le "\"Hey. Come out of there. I see you, princess.\""
            
            # TODO
            #CG: Kylie intro
            
            # TODO
            #Music: kylie theme
            #play music kylie_theme
            
            m "A face appears around the corner, a jam stain at the corner of her mouth and a half-eaten tart in her hands."
            
            u "\"Hi…\" she mutters, mouth half full of pastry."
            
            le "\"That is no way for a princess to introduce herself.\""
            
            m "The girl sighs, her shoulders heaving exaggeratedly, and takes a large swallow, wiping the jam stain from her mouth with the back of her sleeve. Her mouth turns down in a pinched, displeased expression as she picks up the side of her skirt with sticky fingers and curtseys to me."
            
            k "\"How do you do,\" she deadpans. \"I am princess Kylie.\""
            
            m "\"Pleasure to meet you,\" I say hesitantly, bobbing a wobbly curtsey. Leslie sighs, but Kylie laughs loudly, the cheerful sound echoing around the dim kitchen."
            
            # TODO
            #Background: kitchens
            
            # TODO
            #Sprite: Kylie, Leslie

            show kylie sprite at center
            show leslie sprite at right
            
            k "You look about as comfortable with that as I feel,\" she says with a broad smile. \"Are you new?\""
            
            m "\"First day,\" I admit. \"I’m the librarian.\"" 
            
            k "\"Oof, good luck with that monstrosity of a room,\" she says, her nose wrinkling as she steps a little closer to me."
            
            m "Now that I get a good look at her, I realize Kylie doesn’t exactly look like the picture of a princess that I might expect. Of course, the jam stain on her sleeve doesn’t help that image, but besides that, I notice that her dress is wrinkled and has a muddy hem, her hair is clipped short and not pinned back in the slightest, she wears no crown, and there appear to be packets and bottles and random objects hanging off a belt around her waist."
            
            m "I know people love dressing like that at Renaissance Faires, but I am nearly one hundred percent certain that a huge, clunky belt is not historical in any way, shape or form. Especially with… what on earth is on that belt, anyhow?"
            
            k "\"Oh, checking out my potion bottles? I was out looking for ingredients before the sun set, but I couldn’t find them all. I’ll have to try again later.\""
            
            m "\"I’m sorry, you said potion bottles?\""
            
            m "It probably shouldn’t be all that surprising to me, considering that the lamps operate on magic and I made it to this world entirely via magic, but it still catches me off guard that a princess is carrying around magic potions."
            
            k "\"I’m studying to become a wizard,\" she says in a proud stage whisper that is not even the slightest bit quiet."
            
            le "\"Yes, against her father’s wishes.\""
            
            m "Kylie does not seem bothered by that in the least. She simply shrugs."
            
            k "\"Consider this my rebellious phase. He won’t let me contest my brother for the crown—not that Noah even wants the crown—so this is plan B. If he really wanted to stop it, he could start letting me study politics.\""
            
            le "\"That… is a fair point,\" she concedes with a shrug. \"If the king asks, I didn’t agree with you, though.\""
            
            k "\"Don’t worry, it’ll be our little secret,\" she says with a smile."
            
            k "\"Aaaaaaand speaking of secrets, I’d better go before anyone figures out I’m not in my room. Buh-bye!\""
            
            m "She’s off before I even have the chance to raise a hand and wave to her."
            
            le "\"In and out like an absolute whirlwind,\" she says with a soft laugh. \"Kylie’s a good girl, though. She brings out the life in you.\""
            
            m "\"I can tell,\" I say, unable to keep the laughter out of my voice."
            
            le "\"Come on. Let’s get to bed. I have a feeling it’s been a long day for the both of us.\""
            
            # TODO
            #Background: fade to black
            
            # TODO
            #Background: basic bedroom
            
            m "Sleep takes a long time to come. Even tucked under warm blankets in a relatively comfortable bed, I’m still sleeping in an entirely unfamiliar room, and my thoughts are plagued by worries."
            
            m "Now that I have time to sit and breathe, the idea of going to sleep in this place just makes the whole situation feel even more real, and I find myself wondering if maybe, if I’m very lucky, I’ll wake up tomorrow morning back in my own bed."
            
            m "Maybe this is really all just a dream."
            
            m "I fall asleep with that thought in the back of my mind, hoping and praying that unconsciousness will bring some relief from the knot of panic that’s slowly growing in my chest."
            
            m "It does not. Instead, I’m plagued by nightmares and sleep fitfully. When I wake, it’s still dark."
            
            m "… And as I squint into the darkness, I can see a tall, humanoid shadow in my room."
            
            # TODO
            #CHOICE OPTION: get ready to run; get ready to fight
            
            menu: 
                "get ready to run":
                    jump run_fight
                "get ready to fight":
                    jump run_fight

            label run_fight:

            "Patcher" "\"Calm down, girl, I’m not here to hurt you!\""
            
            m "It takes a moment for me to recognize the voice, but as my heart rate calms and my eyes adjust, I can make out the outline of a beaked mask."
            
            show lorenzo sprite at center
            
            m "\"Bird man!\" I cry out in relief, shoulders slumping as I sit up in bed."
            
            m "I can’t make out everything he’s saying in response, but there’s definitely grumbling coming from under the mask."
            
            "Patcher" "\"My name is not bird man… but it’s fine, I suppose. How is progress?\""
            
            m "\"That library is an organizational nightmare. Do you realize what we had to do just to get into the archive room at all?\""
            
            "Patcher" "\"Yes, from what I understand, it is a bit of a mess.\""
            
            m "\"Understatement,\" I snap."
            
            "Patcher" "\"Would you like to return home or not?\" He says with a shrug. \"I don’t make the rules, I only recite them. It’s your job to take care of the tasks.\""
            
            m "\"I’m doing my best over here, okay? Would you like to deal with being dropped in another world and having to figure it all out yourself?\""
            
            m "There is a suspiciously long silence then, as though he is considering my words."
            
            "Patcher" "\"… No. I cannot say I would enjoy that.\""
            
            "Patcher" "\"However, that does not change what must be done, nor does it change the fact that it must be done quickly.\""
            
            m "I glare at him silently. There’s nothing more I can do unless I forego eating and sleeping, and past experiences in the library have taught me that foregoing those two things does not usually lead to anything good."
            
            m "Then again, we’re in a video game. Maybe normal rules don’t apply here."
            
            "Patcher" "\"Fix it. Soon,\" he snaps. Then he opens the door and exits my room, vanishing into the night."
            

            jump chapter4