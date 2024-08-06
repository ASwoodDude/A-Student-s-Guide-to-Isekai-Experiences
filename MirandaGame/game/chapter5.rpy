
# TODO
    #

# Characters



label chapter5:

    scene title cp5 with fade

    $ renpy.pause()

    # TODO
    # ASK
    #Background: library
    scene bg castlelib

    play music library_ambient
    
    m "I try to focus on the library the next day, I do, but something about the book that Noah found calls to me, and I find myself constantly glancing over at the table where it rests, longing to crack it open."
    
    m "After an hour of work, once the sun is high enough into the sky to be able to easily read, I can’t stand to wait any longer and open the book."
    
    m "The Fairy, who has been flitting around to help me organize a little, flies over to sit on my shoulder, staring down at the page."


    show fairy sprite at fairycenter
    
    f "\"Where did you find that?\" she asks, tiny head tilting to the side."
    
    m "\"Down by the stained-glass windows in the entryway. It bugs me that I can’t translate it, though.\""
    
    f "\"The game translation circuits aren’t working?\" she asks incredulously."
    
    m "\"Nope. It just looks like a jumble of letters.\""
    
    f "\"That’s impossible!\" she cries, flying in an agitated circle over the text. \"The translation circuits know every human language. There’s no way this wouldn’t work unless it was a whole new language, or in code, or just gibberish, or really, really bad penmanship—\""
    
    m "I blink, a lightbulb flickering on in my brain."
    
    m "I’m not entirely new to video games. I was a puzzle fiend as a child, and I loved mystery solving point-and-click titles. I should have recognized it sooner."
    
    m "\"It’s in code,\" I whisper, excitement taking over. If I could translate it into an actual language, maybe the game circuits would take over for me! I’m about to take off and run with that idea when another thought hits me."
    
    m "\"Cluck.\""
    
    m "I rest my head in my hands. This isn’t a point-and-click game with a guaranteed hint somewhere. There’s not going to be a book on decoding messages on the shelf. I’m not even sure I was supposed to find this book, especially if it confuses the Fairy."
    
    m "Weirdly, that makes me even more determined to figure out what’s inside. Why go to all the trouble of putting a text like this in code if it isn’t important?"
    
    m "I stare at the page, scanning over it for any hint of what the code formula might be."
    
    f "\"What are you thinking?\" she asks, raising an eyebrow."
    
    m "\"It’s got to be solveable. I can do this,\" I say, setting my jaw."
    
    m "\"It’s… Okay, it’s looking like a jumble of letters, but they’re all from the Roman alphabet. There’s spaces between them like words, but they’re not words…\""
    
    m "That’s when it hits me."
    
    m "\"It’s a Caesar shift cypher!\" I snap my fingers and grab an old ledger sheet, turning it over onto the blank back, where I write out the whole alphabet in a messy scrawl."
    
    f "\"A what?\" she blinks."
    
    m "\"They shifted the letters up or down the alphabet by a certain number. It’s still written out in the same patterns, you just have to move everything down…\" I trail off, biting my lip. \"The problem is that I don’t know by what number.\""
    
    u "\"Try seven.\""
    
    # TODO
    #Music: kylie theme

    hide fairy sprite

    play music kylie_theme
    

    show kylie sprite at center
    
    m "I spin around in my chair to see Kylie standing in the doorway."
    
    m "\"Is everyone in this place determined to give me a minor heart attack?\" I grumble, sighing as Kylie enters the library."
    
    k "\"Seven. Number of perfection in magic and alchemy. Try that.\""
    
    m "I want to question her, but the desire to see if she’s right supersedes everything at the moment. I turn back to my letter list, counting down one letter at a time and scribbling as I go."
    
    m "\"Aut inven…\" I mutter, slowly translating, but just as I think we’re out of luck and will have to try every numerical combination, I recognize a word."
    
    m "\"Inveniam,\" I mutter. \"It’s cyphered Latin.\""
    
    m "I finish translating the title of the book, and sure enough, there it is in front of me: Aut inveniam viam aut faciam."

    m "If I cannot find a way, I will make one. It’s a common maxim that we translated in one of my classes, ringing a faraway bell in my mind."
    
    m "As I finish the sentence, the game’s translation circuits seem to kick in for me, the Latin text turning to English as I watch. Beside my brief translation, the pages of the book appear to ripple."
    
    m "\"How is it doing that?\" I ask, staring as the coded Latin fades to modern English before my eyes. Instead of a jumble of code, the words appear as they should, easily legible and translated."
    
    f "\"You… wrote new code,\" she says incredulously. \"You just taught the game system new code. It learned how to do that from you, and now that it knows the decoding program, it can finish it for you.\""
    
    m "The urge to immediately start scanning pages is strong, but instead I turn back to Kylie."
    
    m "\"How did you know that would work?\" Thinking back, it makes sense, as I know Renaissance magicians and alchemists like John Dee did consider the number seven to be perfect and divine."

    m "We found this book in the Magician’s window, but… I wouldn’t have pulled it off the top of my head as quickly as Kylie."
    
    k "\"I’m a wizard,\" she says, pulling up a chair \"I know a thing or two about magic.\""
    
    m "\"I remember,\" I say, recalling our conversation with Leslie. \"How long have you been studying magic?\""
    
    k "\"I… can’t remember,\" she says bitterly. \"That’s why I started studying it in the first place. There are too many of us here who just… can’t remember a lot of our lives.\""
    
    k "\"We remember big events, mostly. But… sometimes it’s hard to separate one day from another. I know, in my head, how old I am. I don’t feel like that, though. I feel so much older. Leslie is the same way.\""
    
    k "\"It scares me,\" she admits."
    
    play music bad_end
    
    m "\"I’m missing memories, too,\" I say softly."
    
    k "\"But— but you just got here!\" Kylie’s eyes are wide with fear. \"Did that start happening before you arrived in Phenai?\""
    
    m "\"No, not until I arrived.\""
    
    m "I admit that I’m scatterbrained and I tend to lose my keys, but I’ve never lost whole sections of my life before like I am now, and they’re getting fuzzier by the hour."
    
    m "Somewhere in the back of my mind, pieces are trying to click together, but there’s some crucial missing information that should make them all link. I can’t put my finger on it, I don’t know what’s happening, but I feel like I have all the pieces…"
    
    m "Very slowly, I turn back to the book in front of me."
    
    m "The windows showing the story of the kingdom…"

    m "The mysterious bird man with the sash…"

    m "A book in code…" 

    m "Everything seems just out of the way enough that it might be something to chase, but there is always the risk that it will push me off schedule just enough to ruin my way home forever."
    
    m "Now, though, looking Kylie, I think it’s worth it to investigate."
    
    m "I open the book."
    
    
    
    play music lorenzo_theme
    
    m "Originally, I’d assumed it was some kind of handwritten historical text, but in reality, it appears to be more of a diary."

    m "The author is only listed as The Magician, no actual name provided anywhere at all, and the portion of the text loosely describes the need to ‘travel away’ to escape something that isn’t specified."
    
    m "There are a few interspersed jottings on various alchemical experiments, and I recognize brief scribblings and symbols that represent elements, planets, metals, and plants."

    m "The first entry is dated as August of 1472, but the date system quickly shifts into something much simpler."
    
    m "\"Day one?\" I mutter, narrowing my eyes at an entry a few pages in."
    
    k "\"What does it say?\" She leans in, but after only the briefest glance, she looks up again."
    
    m "Assuming the translation function doesn’t work for her in the same way it does for me, what with player special privileges, I begin to read out loud."
    
    m "\"It is fortunate that I recently began a new book, though I will need to be very diligent about writing only in code, so as to keep these experiments secret from the denizens of this new world.\""
    
    m "\"New… world?\" I splutter. \"Other worlds don’t exist.\""
    
    k "\"Well, that’s rather small-minded of you, especially considering how you found yourself here in the first place. At least, if my guess is correct.\""
    
    m "I openly gape at her, unsure of how to respond to that statement. How on earth would Kylie have any idea of how I got here? What does she know? And why hasn’t she mentioned it before?"
    
    k "\"I know you’re not from here. I don’t know where you are from, but I know it’s not this place.\""
    
    m "\"………\""
    
    k "\"I can smell it on you, sort of. Sense it. It’s like a weird kind of skin tingle or itchy nose right before you sneeze. You’re different.\" She sighs deeply. \"Noah was like that, too, at first.\""
    
    m "\"Noah?\" My brow furrows. \"I thought he was older than you.\""
    
    k "\"He… is. I think. He… looks older, so he must be…\" she trails off. \"Regardless, I can remember when he first arrived.\""

    m "\"They said he came from a trip, arrived from far off, but… I’m sorry, it’s getting really fuzzy in my head.\" She squeezes her eyes shut, rubbing at her temples with her fingertips."
    
    k "\"I just… I know he wasn’t here forever. I don’t know how I know, but I do, and I remember he felt like you do. And then he… stopped feeling like that.\""
    
    m "I feel like the wheels in my head are turning, but I’m spinning in place. Noah and Kylie are all NPCs. They’re game characters."

    m "The system doesn’t work for them like it does for me, they can’t see Fairy… so how could they possibly be affected by memory loss in the same way I am?"
    
    m "\"Question— what do you remember?\""
    
    k "\"Not much,\" she says with a snort."
    
    k "\"I’m Noah’s half-sister. My mom died a long time ago, not too long after giving birth to me."

    k "I know a few things about magic, but I keep feeling like I’m spinning in circles. I get déjà vu every time I try to read more about alchemy, the library somehow feels too small and endless all at the same time…\" She sighs, shoulders slumping."
    
    k "\"I don’t think you want to hear my life story, though.\""
    
    
    menu:
        "Go on":
            # +1 affection
            $ affection[7] = 1
            jump chapter5_encounter
        "Anything might help":
            # no change
            # continues to same as 'go on'
            jump chapter5_encounter
        "Go back to reading":
            # -1 affection
            $ affection[7] = -1
            jump go_back_to_reading

    
    label go_back_to_reading:
    
        m "Unsure of what to say, I go back to the book text."
    
        jump chapter5_skip1
    
    
    label chapter5_encounter:
    
        m "Kylie looks hesitant for a moment, but then nods."
        
        k "\"I wish I could remember more, but every time I try, it’s like I’m just reciting a monologue from memory. It… clearly was supposed to have happened, but I don’t know that it actually did, if that makes any sense.\""
        
        m "\"False memories…\" I mutter, nodding slowly."
        
        k "\"I know I’m a princess and I know my father won’t let me study politics, but I don’t remember how or why I started looking into magic.\""
        
        k "\"I love it. It’s interesting. But every time I come across something new, it’s like it’s one step forward and two steps back, and I constantly feel like I’m… looking for something important. I can never find it, though.\""
        
        m "\"You can’t remember what it is?\""
        
        k "\"No.\" She shakes her head sadly. \"It’s like chasing an itch you can’t scratch.\""
        
        k "\"I’m scrambling around in the dark, and I know I’m looking for something, but I don’t know what it is or how I’ll know it when I find it.\""
        
        k "\"And this is going to sound crazy, but there’s this… this guy? It’s like he disappears from people’s minds,\" she pauses, shaking her head. \"I can remember he wears a mask and all black, but I… I… don’t know anything else. It doesn’t matter how hard I try.\""
        
        m "I am positive I know exactly who she is talking about. The same thing happened to Noah in the castle entryway."

        m "For whatever reason, I am the only one who seems to remember the man in the bird mask without issue, and I am also the only one he appears to regularly seek out."
        
        m "I wonder why that is? Maybe I should have been asking questions like this before now…"
        
        
        label chapter5_skip1:

            u "\"Well, I must say, this place is an utter mess—\""

            show kylie sprite at centerleft

            show lorenzo sprite at centerright

            m "I spin around in my chair to see the Patcher in all his bird masked glory, standing stock still at the door to the library. Kylie stares back at him, her face slowly contorting into an expression that can only be described as pure rage."
            
            k "\"You.\""
            
            k "\"I should have known you would show your pointy face if I kept looking long enough.\""
            
            m "And then the man in the bird mask does something I would have never expected."
            
            m "He turns tail and runs."

            scene bg castle hallway

            hide lorenzo sprite 
            hide kylie 
            
            m "Kylie is off like a shot before I even have time to react, chasing after him right on his heels, screeching something unintelligible as she takes off down the hallway."
            
            m "It takes a moment for me to recover, but when I do, I scramble to my feet so quickly that the chair falls over behind me and chase after them, the Fairy right behind me."
            

            show fairy sprite at fairycenter
            
            f "\"What is she doing?\""
            
            m "\"How should I know?!\" All I know is that I want to see it. If Kylie has been hunting this guy down, now might be the opportunity we need."
            
            hide fairy sprite

            show lorenzo sprite at centerright
            show kylie sprite at center
            
            m "Kylie stands at a dead end in the hallway, having backed the man in the mask into a literal corner. She cautiously steps forward, reaching out towards him as I finally catch up to them, moving to stand beside her."
            
            k "\"Let’s see who you really are under there.\""
            
            m "But the Patcher isn’t about to let her grab at him. He pulls a knife from a hidden pocket somewhere in his robes, brandishing it in his closed fist."
            
            "Patcher" "\" You have been a thorn in my side for far too long,\" he growls, lunging forward to slash out with the knife."
            
            menu:

                "push kylie out of the way":
                    $ affection [8] = 2
                    jump push_kylie
                    # +2 affection
                "dodge":
                    jump dodge
                    # no change
                "watch what happens":
                    jump bad_end_1
                    # bad end 1

            label bad_end_1:
            
                play music bad_end

                scene bg castle hallway with blood
                
                m "I stand there frozen in shock, wondering what I should do for just a second too long, thinking he’s aiming for Kylie and wondering if it’s worth the risk to save her."
                
                m "Unfortunately, my calculations are very wrong."
                
                m "He wasn’t aiming for Kylie. He wasn’t even speaking to Kylie."
                
                m "He was aiming for me, as evidenced by the screaming gash in my gut, as evidenced by the knife stained with my blood clattering against the hallway floor."
                
                m "My knees buckle in shock as Kylie stares, kneeling down beside me when I collapse onto the floor. She tries to put her hands over the wound to staunch the blood flow, but it’s useless. Even I can tell it’s useless."
                
                m "Bright red blood stains my hands and hers as a beaked face looms over us."
                
                show lorenzo sprite at center
                
                "Patcher" "\" I was going to let you live, but you just had to meddle, didn’t you?\""
                
                "Patcher" "\" No matter. Life force isn’t as potent as memories, and yours is rapidly draining, but it should be more than enough to sustain us until someone else comes by.\""
                
                m "Us? I wonder why he’s saying us, but my thoughts are foggy. The pain is all I can feel, all I can think about, but some morbid little corner of my mind tells me it should be over soon. Permanently over."
                
                "Patcher" "\" Goodbye, little nuisance.\""
                
                m "He puts a black gloved hand over the wound in my stomach, coating it in blood, and I see him raise his hand… snap his fingers…"
                
                m "And that is the last thing I ever see."

                jump the_end


            label push_kylie:
            
                m "I don’t have time to think as I lunge towards Kylie, knocking us both to the floor but out of the way of the blade swinging towards our necks."

                jump chapter5_encounter2

            label dodge:
            
                m "I flail and careen to the side, losing my balance but diving out of the way of the knife."
            
            label chapter5_encounter2:
            
                m "My hands and knees sting as I roll across the hallway, narrowly missing knocking my head into the wall. I can only assume that Kylie wasn’t hit, either, as she recovers even faster than I can."
                
                k "\"Grab him!\" she shouts."
                
                m "I don’t think, I just listen to instructions. Still on the floor, I grab for one of the Patcher’s ankles and swipe him off balance by pulling out one of his legs from under him."

                m "Both his mask and wide-brimmed hat fly off his head as his body thuds to the floor like a sack."

                scene cg unmasked 
                
                m "Somewhere in the back of my mind, I register a strange, sickening, wet noise, but I’m too focused on surviving to investigate at the moment."
                
                m "I kick the bird man in the shin and he screeches, giving me enough time to clamber to my knees, ready to pin him down, when I suddenly notice—"
                
                m "\"Oh god,\" I whisper."
                
                m "The knife that the Patcher just attempted to stab us with is now hilt-deep in his stomach."
                
                m "He must have fallen on it when he lost his balance. Unlikely in practice, but in a fairy tale like we are now… I suppose if not making sense, it’s at least more plausible."
                
                k "\"I knew it. You’re the one that created this whole… situation,\" she says distastefully as she struggles to her feet. She looks a little green and gasps at the sight of the knife."
                
                "Patcher" "\" Please, this is an art form of magic that your pathetic little hands couldn’t dream of making,\" he spits, clearly more offended by the implication that he created a mess than anything \"It’s nothing like your silly little child alchemy.\""
                
                m "To my surprise, he makes a strained noise and pulls himself up, leaning against the wall, knife still in his stomach."
                
                "Patcher" "\" Unfortunate…\" he mutters, shaking his head as though he’s been papercut instead of stabbed. \"I’m getting sloppy.\""
                
                m "He barely grunts as he pulls the knife from his body, tossing it aside on the floor like it’s a used toothpick. Kylie picks it up, probably in part to keep it away from him and partly to have a weapon herself. Just in case."
                
                m "A part of me wants to laugh. It’s maniacal, and definitely born of a near death experience, but it’s laughter all the same."
                
                m "\"Kinda stupid to put characters in here that can foil your plans, if you ask me,\" I mutter. \"Kylie’s been onto you for a long time.\""
                
                "Patcher" "\" Characters? I created the storybook, stupid girl, not the people. You think I had time for all that? I had to populate it of my own volition.\""
                
                m "A cold streak of horror slices through my chest as sudden realization seizes me."
                
                m "\"Oh, god,\" I whisper. \"They’re not NPCs.\""
                
                m "I turn to Kylie with unveiled abject horror splashed across my face."

                scene bg castle hallway
                show kylie sprite at centerleft

                show lorenzo sprite at centerright
                
                m "\"Kylie…\" I whisper. \"Your memories.\""
                
                m "Beside me, Kylie begins to shake. Her eyes are wide as she slowly nods."
                
                "Patcher" "\" Yes, you were one of the early ones. Always been a thorn in my side, too. Had to constantly drain memories off to keep you off my trail.\""
                
                k "\"How…\" She pales."
                
                k "\"How long have I been here?\""
                
                m "It’s a barely audible whisper, but it’s enough to make my heart break."
                
                "Patcher" "\" One does lose track of the years over time, but by my count, it’s been four… perhaps five…\""
                
                m "Kylie’s shoulders slump a little in relief."
                
                "Patcher" "\" … centuries.\""
                
                m "The sheer look of horror on Kylie’s face is something that I hope to never see again in my life."
                
                m "Sheer rage flares to life somewhere deep in my gut. I start to shake as well, but it isn’t with fear."

                m " As though I can shield Kylie from the masked man, I step in front of her and stalk closer to where he leans against the wall."
                
                m "\"You’re going to tell me who you are, and you’re going to tell me NOW,\" I say through gritted teeth."
                
                m "\"I’m done playing games.\""
                
                "Patcher" "\" Ironic turn of phrase,\" he scoffs. \"You’re not done till I say you’re done.\""
                
                m "\"Wrong.\""
                
                m "In one movement, I grab the dagger from Kylie’s loose grip and surge forward, holding the blade to the now unmasked bird man's throat."
                
                m "\"I think you’re done when I say you’re done.\""
                
                m "The reins on my nerves have officially snapped. As far as I’m concerned, we’re now in a life-or-death situation."

                m "This man knows something, it’s key to our survival, and now I’m even more determined to get that information out of him."
                
                "Patcher" "\" What exactly do you plan to do?\" He tries to laugh, but it turns into a cough. \"In case you haven’t noticed, I’m bleeding out already.\""
                
                m "Crap. He’s right."
                
                m "That, and I legitimately do not think I have the stomach to drag this blade across his neck if it comes down to it."
                
                m "Time to bluff until we can bluff no more."
                
                m "\"Well, let’s see,\" I muse, letting my voice take on a disconnected tone. \"I could make you bleed out faster if I wanted. Cut your life even shorter.\""
                
                "Patcher" "\" That wouldn’t end particularly well for you,\" he snorts."
                
                m "\"Then why don’t you start talking and convince me why I shouldn’t move this dagger.\""
                
                m "At first, I think it’s not going to work. Maybe he’ll just keep denying me and die and we’ll never get out of here, but as I press the dagger in closer to his neck, I feel a shudder run through him."

                m "A realization hits me."
                
                m "He’s afraid."
                
                m "Out of all the things he clearly is not afraid of, he is genuinely afraid of dying in this moment— even though this is a fictional world, is a storybook, is a game... It’s not a game to him, and that might be the one single thing we have over him in this moment."
                
                m "What power does he have that he felt fine, even calm, while bleeding out, but the prospect of my killing him instantly truly puts fear into his heart?"
                
                "Patcher" "\" Give me something to staunch the bleeding. Then I’ll talk.\""
                
                m "Kylie moves to grab a piece of fabric, but I catch her eye and shake my head."
                
                m "\"Talk first. Then staunch,\" I snap. \"The faster you talk, the less you bleed.\""
                
                m "He looks like he wants to argue, but eventually he huffs, reaching up to rip off his bird mask with one hand."
                
                play music lorenzo_theme
                
                m "The face under the mask isn’t… Well, I’d say it isn’t what I expected, but I don’t really know what I expected at all."
                
                m "He’s a middle-aged man with a long beard, not that I know how that mask was hiding it. His skin is wrinkled and rough, and his eyes are tired."
                
                lo "\"My name is Lorenzo,\" he says slowly, heaving a long sigh."
                
                lo "\"I was a magician in Italy, around 1470. Not one of those party tricks, either. I was a real alchemist.\""
                
                m "\"So how did you wind up in a video game in the 2020s?\" I ask, patience growing thin."
                
                lo "\"Straight to the point, are we? Alright, then. It’s quite simple: I wanted to live.\""
                
                m "\"Thank you for that incredibly thorough and detailed explanation,\" I deadpan. Kylie stifles a slightly manic laugh from beside me."
                
                lo "\"You’re a historian, yes?\""
                
                m "\"Me?\" I pause, my memories still fuzzy. \"Uh… I think… I think so, yeah.\""
                
                lo "\"Surely you’re well aware of the various bouts of diseases that ravaged the land in my time.\""
                
                m "He speaks with a certain pompous air that really grates on my nerves, but despite the urge to smack him, I do know what he’s talking about. There were certainly plenty of diseases in Renaissance Europe, especially with recurring bouts of—"
                
                m "Wait."
                
                m "\"Were you running from the Black Plague?\" I ask incredulously. I feel incredibly silly for not having realized that before. He’s wearing a plague doctor mask, after all!"
                
                lo "\"Not running. Surviving.\""
                
                scene bg flipped hallway

                show lorenzo sprite at center
                
                lo "\"I was already infected at the time, you see, and with few options for treatment, I turned to what I knew best: the alchemical arts.\""
                
                lo "\"However, instead of trying to cure myself, I looked for an escape. I thought that, surely, if I could escape to a world where the plague did not exist, then surely I would be cured.\""
                
                m "I want to tell him that the logic of that is shaky at best and that it would be much more likely for him to bring the Plague into the new world and subsequently infect all its inhabitants rather than being magically cured upon arrival…"
                
                m "Unfortunately, though, I’m standing in evidence that his plan, at least to some unknown degree, actually worked. Instead of protesting, I simply wave a hand for him to continue on."
                
                lo "\"It did not cure me, much to my displeasure, but the journey here did halt the progression of the disease. So long as I remained in this world, I was kept in a state of pause. Preserved.\""
                
                lo "\"Unfortunately, the universe does demand some amount of give and take. Since I left the world, something else had to come into being in my place, and since I was not aging, something else had to provide the life force for me to sustain myself rather than my own body.\""
                
                m "That… very weirdly, makes sense."
                
                m "\"Okay, so the first law of thermodynamics and Newton’s third law of motion all meet magic. I follow.\""
                
                m "Lorenzo just stares. If it weren’t for the mask, I would say he was gawking at me."
                
                lo "\"You may speak in tongues to confuse me, but I care not, so long as you understand that I was successful in my task.\""
                
                m "\"Okay, I get that you wanted to leave your world because you didn’t want to die, but how does it tie into a video game? Those didn’t even exist in the fifteenth century.\""
                
                lo "\"A story is a story. This world exists in whatever format it needs to so that I may acquire the energy I need to sustain it.\""
                
                m "\"The… energy?\""
                
                lo "\"Memories are their own sort of potent magic.\""
                
                m "Oh, god."
                
                m "A chill runs through me as I suddenly realize why Tarran has memory troubles… as I realize why Noah couldn’t place who Lorenzo was or why he was in the castle."
                
                m "\"You stole all their memories…\" I whisper."
                
                lo "\"I used them as fuel to keep this world alive,\" he snaps, shaking his head. \"A memory has a much, much longer lifespan than any human could ever imagine. Memory predates us, it outlives us, it keeps going long after we are gone.\""
                
                lo "\"I suppose I could have simply drained the life force from anyone who came in contact with my storybook, but that wouldn’t have lasted anywhere near as long as their memories.\""
                
                m "\"So you just… kept them? Like… like prisoners?\""
                
                lo "\"More like pets.\""
                
                m "Right. Because that’s so much better."
                
                lo "\"I drain their old memories and then they make new ones in this world. Though the memories of this world are not near as potent a power source as ones from the world we came from, they will do in emergencies.\""
                
                m "\"So… let me get this straight,\" I say, and even I can hear the incredulity in my voice."
                
                m "\"You trap these people here and slowly drain their memories. And then if you need MORE than what you’ve already taken from the, you drain memories they’ve made here and leave them just floating through their daily lives in this fictional world?\""
                
                lo "\"Yes.\""
                
                m "He says it like there’s no problem at all, but I am reeling."
                
                lo "\"Only when they fail, though,\" he says with a watery cough. \"Then they happily agree to my bargain."
                
                m "\"Fail?\" I ask, incredulous. \"If you wanted me to fail, why were you helping me?\""
                
                lo "\"Was I, though?\""
                
                m "I think back for a moment."
                
                m "The entire time I’ve been here, Lorenzo has appeared to help me. He was the one who told me about organizing the library. He was the only one who knew where I was from…"
                
                m "Because he put me here, I remind myself. Lorenzo wasn’t ever helping me, in the end."

                m "The Fairy was helping me, stationed as the system interface. But if Lorenzo was trying to get me to organize the library and the game put me here was a librarian, then the question remains…"
                
                m "What was I actually supposed to be doing all this time?"
                
                lo "\"It’s too late, you’re already doomed. You’ve made your choices like all the rest.\""
                

                # affection[8]
                menu:
                    "I'm not giving up!":
                        # +2 affection
                        $ affection[9] = 2
                        jump not_giving_up
                    "I don’t really know":
                        # no change
                        jump i_dont_know
                    "Maybe it’s hopeless after all":
                        $ affection[9] = -2
                        # -2 affection
                        jump hopeless

                # TODO
                # FADE?                
                label not_giving_up:
                    show fairy sprite:
                        xalign  1
                        yalign  .6
                    show kylie sprite at centerleft
                    show lorenzo sprite at centerright

                    play music mc_theme
                    
                    k "\"I like your spirit!\""
                    
                    f "\"You’ve come too far to quit now!\""
                    
                    m "\"You’re right. I’m not stopping now.\""
                    
                    m "We are so close to the end that I can taste it. I can feel it in my bones. I know it’s within my grasp if I just keep trying to look for a solution."
                
                    jump chapter5_encounter3_end
                

                label i_dont_know:
                    hide lorenzo sprite

                    show fairy sprite at fairyright
                    show kylie sprite at center
                
                    play music mc_theme
                
                    m "I feel stuck in more than one way. What if I have already made my choices? What if everything I’ve done so far has already set my fate in a direction I don’t want it to go?"
                    
                    k "\"[player_name]?\""
                    
                    f "\"You can’t stop now. Please,\" she says softly."
                    
                    m "Unfortunately, I know they’re right."

                    jump chapter5_encounter3_end


                label hopeless:                
                    hide lorenzo sprite

                    show fairy sprite at fairycenterright
                    show kylie sprite at centerleft
                
                    play music mc_theme
                
                    m "I open my mouth to speak, but no words come out. A tear rolls down my cheek as I hang my head."
                    
                    m "I think it really might be too late."
                    
                    m "I’m unsure of so many of the choices I’ve made. I don’t like how things have gone since I’ve started here. I’m confused and sad, and I want to go home… but my memories of that home are rapidly fading."
                    
                    k "\"You really think there’s nothing more to do?\""
                    
                    m "\"I… I wish there was.\""
                

                #REDIRECT POINT >>>
                
                label chapter5_encounter3_end:
                    m "At that point, I start to hear rumbling in the distance."
                    
                    m "It starts off quietly, slowly, far off in the distance, growing and growing until the stones under my feet are vibrating, threatening to send me tumbling to the ground."
                    
                    m "\"What’s happening?!\""
                    
                    k "\"I—I don’t know! We’ve never had an earthquake here before—\""
                    
                    lo "\"It has been far too long since the magic has been fed,\" Lorenzo says. \"I will die and this world along with it if it is not taken care of soon.\""
                    
                    m "Strangely, he doesn’t seem panicked just yet, shrugging as though this is simply a passing thunderstorm."
                    
                    lo "\"It’s unfortunate, but we’ve bounced back from here before.\""
                    
                    m "\"What? How?!\" I ask as the rumbling settles."
                    
                    lo "\"I need more magic. From there, I can use the magic to heal myself and heal this world, and then we all go on to live our lives in peace.\""
                    
                    m "\"In peace? Trapped in here without our memories?\""
                    
                    lo "\"The sacrifice of memories to live forever in comfort and safety is more than a fair trade, wouldn’t you say?\""
                    
                    m "Honestly, I don’t know any more."
                    
                    m "Maybe the worst part about it all is that living here in comfort and safety, with a sense of routine set before me, away from the things I’m afraid of in the real world… It doesn’t actually sound like a terrible plan."
                    
                    m "On the other hand, the real world is real. Do I want to spend the rest of my life in a fantasy, away from family and friends, in exchange for… what?"
                    
                    lo "\"Come, now, would it really be so bad to stay here?\" he asks. \"All I ask is that you consider my bargain.\""
                    

                    
                    menu:
                        "I can't stay.":
                            jump i_cant_stay
                        "Maybe it wouldn't be so bad.":
                            jump bad_end_2
                            

                    label bad_end_2:


                        play music bad_end
                        
                        m "\"What’s your bargain?\" I ask after a long pause."
                        
                        k "\"[player_name], no, you don’t want this—\""
                        
                        m "But I’m no longer listening to her."
                        
                        hide fairy sprite
                        hide kylie sprite
                        
                        lo "\"Simple. As I said, the memories of your world, of your childhood and life before this, are much more potent than memories made here, and you are the only person with access to them. Besides myself, of course,\" he amends quickly."
                        
                        m "\"Then you sacrifice memories this time,\" I snap."
                        
                        lo "\"If I sacrifice mine, I will forego knowledge of how to keep this place intact for the rest of us,\" he says matter-of-factly. \"It must be you.\""
                        
                        lo "\"If you sacrifice your memories to fuel the magic here, then we will all live on. I can use that power to heal the world, to heal myself, and keep a steady hold on the life we all have here.\""
                        
                        m "My stomach roils, but I can’t tell if it’s from my emotions or the quaking castle around me."
                        
                        m "The most terrifying thing about this entire experience so far is that Lorenzo, for all his twisted logic, does actually make sense in this moment. It might be the only option that we have."
                        
                        lo "\"It’s not so bad, after all,\" he says, his voice taking on an almost soothing tone. \"I can make your story whatever you want. You could be a princess, a sorceress, a famed scholar—anything your heart wants and your mind can imagine, I can do for you.\""
                        
                        m "I can’t deny that to some part of me, that offer is tempting."
                        
                        m "I am tired. I’m burnt out on everything. It seems much easier to let things go, to have the chance of a new start here, than to fight for something I’m not even sure I want any more."
                        
                        m "Still, I hesitate."
                        
                        m "\"Did the others all make the same choice?\""
                        
                        lo "\"They had their reasons. Besides, it is infinitely less painful to have no memories in a world that you will never escape.\""
                        
                        m "I hate that he’s right. I hate that I know that if I have to be stuck here forever, that it might be better not to remember. For the faintest moment, I think back to what Tarran said, about how he doesn’t remember much from his childhood, about how his memories are generally fuzzy…"
                        
                        m "I realize that, in all likelihood, I am not the first to make this choice. I will probably not be the last, either."
                        
                        lo "\"It’s your memories or the death of us all.\""
                        
                        m "That’s it, then. The choice has already been made for me."
                        
                        m "I may be burnt out, but I’m not ready to die with this world, and I am the only one left besides Lorenzo with any memories to burn to save it… and to save myself in the process."
                        
                        m "I don’t have another option. All I can do is hope that maybe one day another solution will present itself, even if this cycle continues far beyond me."
                        
                        m "\"… Okay.\""
                        
                        m "I take a deep breath in as tears begin to run down my cheeks, squeezing my eyes shut."
                        

                        scene black with fade
                        
                        lo "\"There now, I promise it won’t be so hard. Perfectly painless.\""
                        
                        m "And it is. Mostly."
                        
                        m "The first thing I notice is that it’s cold. It’s like everything around me is freezing and dark and the darkness is closing in… "
                        
                        m "And then the pressure releases with a pop, almost like ears adjusting to high altitudes, and I feel… better."
                        


                        scene bg flipped hallway

                        show lorenzo sprite at center
                        
                        m "The only problem is that I don’t remember how I got here. Where am I?"
                        
                        m "Who am I?"
                        
                        m "I know my name, but I can’t seem to place anything else about myself, or about the stone-walled hallway I’m currently standing in, or about the admittedly frightening masked man standing in front of me."
                        
                        m "\"What’s happening?\" I manage to squeak out. My throat is raw and I realize my cheeks are wet, like maybe I’d been crying, but I don’t know why I would have been."
                        
                        lo "\"Why, you’re the castle librarian,\" he says. \"Come with me. I’ll show you your new home.\""

                        jump the_end

                    label i_cant_stay:
                    
                        m "No matter what, I know in my heart that it isn’t worth it to back down. I want to go home, and I’m going to fight for that. Not just for me, but for everyone else that clearly has been trapped here, too."
                        
                        m "I hit Lorenzo over the head with his own staff in response."

                        hide lorenzo sprite
                         
                        m "\"Yeah, cluck you,\" I spit at his unconscious form. \"I’ll take my chances on door number three.\""
                        
                        m "Kylie gives a low whistle as she looks over Lorenzo’s unconscious body, eyebrows raised."
                        
                        k "\"You’ve got a whole lot of suppressed rage hiding out in there, huh?\""
                        
                        m "\"Is now really the time for this?\" I ask with a sigh."
                        
                        k "\"… Fair.\""
                        
                        m "Unfortunately, that is when the entire castle really starts to shake."
                        

                        scene black with fade


                        stop sound
                        stop music

                        jump chapter6