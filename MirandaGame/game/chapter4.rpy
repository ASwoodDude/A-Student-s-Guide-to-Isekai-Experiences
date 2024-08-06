

label chapter4:

    # TODO
    #Background: chapter title
    scene title cp4 with fade 

    $ renpy.pause()

    # TODO
    # ASK
    #fade to library 1 background
    scene bg castlelib
    
    play music fantastical_day
    
    m "I didn’t really get why bread and cheese would be super appetizing to adventurers in fantasy books till I knew what some of the other options are for meals."
    
    m "I know I come from an area where squirrel stew is a thing, but I have to say I’ve never seen sheep’s brains on a breakfast menu before, and I hope to never see them again."
    
    m "Since all the chairs have various piles of things in them, I plop down on the library floor and nibble at my cheese and fresh hunk of bread while I sit on the rug, thinking over what’s left to do today."
    
    m "I woke up as soon as the sun rose and got started organizing, moving files and shuffling boxes and reorganizing bookshelves for a couple of hours before I made my way to the kitchen for breakfast."

    m "I swept out the floor, wiped down the furniture, and created a dump pile for anything that definitely needs to be thrown out."
    
    m "Now that the light is really coming in through the windows, I can take a good look around. As much as it still looks like a whole load of chaos, it does indeed look a little better in here."
    
    u "\"Hello? Anyone in— ah, I didn’t see you!\""
    
    show noah sprite at center

    play music noah_theme
    
    m "I wave from my position on the floor, mouth full of cheese, as I motion Noah over."
    
    n "\"Sorry to disturb your breakfast,\" he says with a smile."
    
    m "I wave him off and swallow my mouthful as I struggle to my feet. \"No problem. What’s up?\""
    
    n "\"Straight to the point, then— you haven’t come across a medical treatise by Erandon of Silver Falls, have you? It’s called Invisible Wounds.\""
    
    m "\"I…\" I trail off. Blink. However, I really and truly can’t remember anything like that. I’ve probably reorganized two hundred volumes just this morning, and if it was among them, I don’t remember it."
    
    m "\"Unfortunately, no,\" I say with a sigh. \"You’re welcome to look around, if you want? I’m in the middle of reorganizing the shelves anyways, so if we find it, it’s all yours.\""
    
    n "\"Thank you. I would appreciate that,\" he says with a nod."
    
    m "I direct him to the slightly less dusty shelves that I’ve already organized and get back to my work. At least I can keep at my task this way."
    
    m "Contrary to my expectations, Noah is actually good company. He’s quiet, doesn’t feel the need to speak too much except to ask organizational questions, and I get a good chunk of work done over the course of the time he spends looking for the tome."
    
    m "It isn’t until I hear a dull thump and a heavy sigh that I look over, finding him sitting on the floor with his back against the shelves, shaking his head."
    
    n "\"This is utter insanity. How on earth is any of this meant to be organized?\""
    
    m "I snort out a laugh and plop down beside him. \"It isn’t. Well, not till I’m done with it, anyways.\""
    
    m "Noah grumbles something unintelligible and crosses his arms over his chest."
    
    m "\"What are you doing looking for a medical treatise, anyways?\""
    
    n "\"It’s an important historical text that many newer authors reference, but I’ve never read it myself, so I thought it would be a good idea to read it myself.\""
    
    m "\"Okay,\" I say slowly, \"the philosophy of that is sound, but I guess what I really mean to ask is… Why is a political figure looking to read a medical treatise?\""
    
    n "\"Oh!\" His eyes widen for a moment and his cheeks flush slightly. \"I forgot that you haven’t been here long. It’s something of an open secret that I am… more interested in medical studies than I am in politics, much to the shame of my father.\""
    
    n "\"I would much rather be a healer than a politician, but I have a responsibility to the people here. The most I can do is study medicine in my free time… however little of that there is.\""
    
    m "\"Boy, do I feel that.\" I sigh, wondering what it’s like to have free time. Some days I’m not sure what it feels like to sit down and just stop doing things for a little while."
    
    n "\"Is it very busy being a librarian?\""
    

    play music mc_theme
    
    m "\"Oh. Uh…\" I almost forgot I was in a fantasy world for a minute. \"I was… A scholar before this. And a teacher. I’m still working on tying some of that up, and it… doesn’t leave a lot of time.\""
    
    m "I bite my lip, trying to think about how best to describe it. \"It’s like… I’m always working. At every hour of the day or night, I have to be ready to work."

    m "\"I’m answering e-mai— uh, correspondences— at 11PM, and if I stop to read a book for enjoyment or eat a good meal, that’s too much time and there are other things I could have done in that moment that would benefit my career more. Does that make any sense?\""
    
    m "Noah slowly nods back at me, eyes wide."
    
    n "\"That is… exactly how I feel, in many ways,\" he says, letting out a long breath. \"I can’t rest. If I do, I’m inevitably failing someone in that moment.\""
    
    m "\"You are the most relatable prince I’ve ever met,\" I say with a wry laugh. \"You’re also the only prince I’ve ever met, but the point stands.\""
    

    menu:
        "I am sure you can be a wonderful healer and a king":

            # +2 affection
            $ affection[4] = 2
            jump healer_and_king

        "It’s good to have hobbies":

            # no change
            jump hobbies

        "I think you should focus on ruling":

            # -2 affection
            $ affection[4] = -2
            jump ruling

    
    label healer_and_king:
        m "\"I’m sure you can find a way to embrace all the parts of yourself,\" I say with a tiny, hesitant smile."
        
        n "\"Thank you,\" he says softly, returning that small smile."
        
        m "It’s like Leslie said— you have to find a way to do things that make you happy, to do things that make you feel like yourself. I just hope that Noah can find that, too."
        
        m "Part of me wonders is it’s because I recognize the resigned slump of his shoulders or the tired look in his eyes. Part of me wonders if it’s just because I like him. Maybe it’s both."
        
        m "Either way, I want him to find his happiness."
        
        m "A little voice in the back of my head protests, says that he’s an NPC. He’s a line of computer code. But… in this moment he feels as real as any other human, and just for a second, I want to believe that."
    
        jump choice4_1_end


    label hobbies:
    
        m "I’m trying to be both supportive and as neutral as I can, but I don’t think it’s really working. Noah seems nonplussed, though, giving a shrug as he stares off into the middle distance."
        
        n "\"If it has to remain a hobby, then it has to remain a hobby,\" he says sadly. \"I wouldn’t mind that as much as giving it up entirely.\""
        
        m "There’s a tiny niggling something at the back of my brain that agrees with him."
        
        m "\"I… I get it, I do,\" I say softly, thinking of my conversation with Leslie. \"But maybe that’s good, too? To have something to just do for you?\""
        
        n "\"Ordinarily I would agree with you, but I don’t want it to be just for me. I want to be able to help people with this, to devote time to research and medical practice, but… Well, perhaps it isn’t feasible in the long run.\""
        
        m "He sounds so sad, and it breaks my heart, but I don’t know what to tell him. I know very well how a career path can sweep in from the side and take over your life, and sometimes… Well, sometimes we love it."

        m "Other times, it becomes our life in a way we really don’t enjoy at all."
        
        m "I just hope that Noah is able to find a path that works for him, that makes him happy, however he has to do it."

        jump choice4_1_end

    
    label ruling: 
        m "Noah sighs, some of the light going out of his eyes as he tosses a lock of hair out of his face."
        
        n "\"That’s what my father would say, too, I’m afraid. And my sister, to an extent, though they have different reasons.\""
        
        n "\"Kylie wants me to be the best that I can be. My father wants me to be… him,\" he says distastefully, but he doesn’t elaborate."
        
        m "I wish I knew what to say, but I don’t have any advice for him. I’ve always been one to grit my teeth, fake a smile, and just do what I needed to do, and it’s changed my outlook on these things."
        
        m "Logically, I know I shouldn’t expect everyone to do that. Logically, I even know it’s not good to do that. It’s hard to shake a lifetime’s worth of habits, though."
    
    label choice4_1_end:
    
        m "I can’t stop thinking about our conversation, even as we continue to look through rows and rows of dusty tomes, still completely failing to find Invisible Wounds."
        
        m "In the end, I’m not sure how long I sit there turning over ideas in my head, half paying attention to the books in my hands, but it’s Noah’s voice that brings me out of my thoughts."
        
        n "\"It’s safe to say it isn’t here,\" he says with a sigh, rubbing his temples. \"I’m sorry to have taken up your time, I just can’t seem to find it anywhere in my rooms, so I thought it might have been found and brought back here.\""
        
        m "Something flits through my mind about lost library book fines, but considering he’s a prince and the library is in the castle that he’s set to inherit, I don’t think that really applies here."
        
        n "\"I should search the castle— retrace my steps.\" He pauses, then turns to me. \"You’re welcome to come with me if you like. I could show you around a little more?\""
        

        menu: 
            "I’d love to look around":

                $ affection[5] = 1
                jump love_to_look

            "Um… sure?":

                jump um_sure

            "I really have work I need to do":

                $ affection[5] = -1
                jump work_to_do
            


        label work_to_do:
        
            m "\"I’m sorry, but I really need to keep working here.\""
            
            n "\"Oh, it’s no problem,\" he says, but he seems a little disappointed. \"I’ll find you later, then?\""
            
            m "\"Sure.\""

            hide noah sprite
            
            m "And I go back to my books."
            
            m "As I work, the sun crosses the sky and the light coming through the windows fades to a rich tone of red-orange. By the time I realize that the light has well and truly started to fade, my stomach is growling and my feet are tired and I have still not finished."
            
            m "I know that, logically, big tasks like this take time."
            
            m "… But I want to go home."

            jump chapter4_redirect

    
        label um_sure:

            m "My response is hesitant, but Noah smiles."
            
            n "\"It’ll be fun, I promise.\" He smiles and motions for me to follow him out the door."

            jump explore
        
    

        label love_to_look:
        
            m "I haven’t seen much of the castle so far, and let’s be honest, how many times in your life can you really look around a castle? Especially a fully-functioning one with knights and royalty."
            
            n "\"Excellent!\" He claps his hands together and motions for me to follow him out the door."

        
        label explore:

            
            play music noah_theme

            scene bg castle hallway

            show noah sprite at center
            
            n "\"I do go out to the pasture to read sometimes, so it might be a good idea to check out there. I don’t think I’d have left it outside, but better to check.\""
            
            m "\"They do always say that things are in the last place you look,\" I say with a shrug. Noah frowns, though."
            
            n "\"Who is ‘they?’\" he asks. \"And why wouldn’t the things be in the last place you look? There’s no need to keep looking after that.\""
            
            m "I open my mouth to respond, but then close it just as quickly. That feels like a circular conversation waiting to happen."
            
            m "\"Um… Never mind.\""
            
            m "It doesn’t take too long to get to the pasture, and I find that I recognize a few things here and there from when I went to return the pocketwatch to Tarran."

            m "That’s a small miracle in itself as far as I’m concerned, as I’m absolutely terrible with directions and the fact that every single hallway in the castle looks identical does not help my confusion."
            
            m "The fleeting thought crosses my mind that if this is a video game, the artist could have put a little more effort into making the hallways look different, but maybe that’s overthinking it too much."
            
label inprogress:
            
            scene bg pasture

            show noah sprite at center
            
            play music pasture

            play sound sheep_long 
            
            n "\"The last time I was out here, I was under that tree. That’s probably the first place to look.\""
            
            m "He takes off across the grass, weaving through sheep and stopping to pat their soft noses here and there."
            
            m "Not for the first time, I’m struck by how picturesque it is out here. The sun is warm on my skin and a light breeze carries away most of the sheep smell."
            
            hide noah sprite

            stop sound fadeout 1.0

            
            m "As Noah moves towards the tree, I realize that the sounds around me have changed."
            
            m "Maybe it’s being in the library and locating items by sound, but I’ve started to notice a little more of the music and sound around me, and as soon as we arrived here, the tune changed to something pastoral and soothing."
            
            m "It strikes me that, if this were a normal video game, someone would need to code all of this into place, and I stop to listen."
            
            m "It’s a soft tune, the melody carried by a recorder in a minor key, like many European folk songs."

            m "Something pulls at a memory in the back of my mind, information about shepherds and pan pipes and an eighteenth-century French fascination with \"simple\" living and pastoral scenes."
            
            m "Someone had to pick this music."

            m "Right now, considering that I’m the only one who hears it, I can’t say if it’s associations from my own mind, something from the game, whoever created this game, or something else entirely, but someone had to pick it, and they picked it intentionally."
            
            m "Sound creates meaning. That much was evident from library adventures and lost objects alone, but it’s even more potent out here."
            
            m "Who decided that this is pastoral? What culture is the influence coming from? What makes me feel like this sounds like a personification of open fields?"
            
            m "And, also, who was responsible for programming the sheep bleating? Because someone had to do that, too."

            play sound sheep_short
            
            m "I heard a sheep bleat on the computer before I was even sucked into this nonsense. Someone put that there because it meant something, because it was important, because they were trying to build a layered sense of meaning."
            
            m "In the real world, there is no programming, but there are certainly layers of sound all around us. Sound is vibration, vibration is movement, and movement is everywhere."

            m "Even though I may not take particular notice of the sound of my own footsteps, they follow me wherever I go, overlaying with construction, singing birds, and snippets of conversation as I pass people, and those layers differ when I am in different places."
            
            m "Yet again, it strikes me that the music and sounds work together to create a sense of place here. Noah may not be able to hear it all, but I can, and it adds a sense of meaning that I would not otherwise be able to understand."
            
            m "I wonder if this is another way that the system is aiding me. I haven’t seen the Fairy today, but I would ask her if I could. When I first arrived, she told me that there were some things only I could hear because I am the player."
            
            m "The weird part about it is that… it puts me in the story, but also outside the story to hear things like this. Am I a player or a character? Am I both? I certainly feel like both, the longer that I spend in this world."
            
            m "Just as I’m turning this idea around in my head, Noah calls from over by the tree."
            
            show noah sprite at center

            n "\"Not here! Do you see anything?\""
            
            m "\"I don’t, I’m sorry!\""
            
            m "Besides the wide swath of grass and the occasional sheep dung, there’s nothing out here. Noah simply shrugs, undeterred."
            
            n "\"Well, on to the next site! At least this way you’ll be able to see a good chunk of the castle.\""
            
            m "I find that I’m smiling without even thinking about it, wondering how the next location will look and sound."


            scene black

            $ renpy.pause()
            
            scene bg castlewall
            
            play music castle_theme volume .8

            show noah sprite at centerleft
            
            m "The next place he takes me to is the castle entryway. I’m not exactly sure why someone would spend a large amount of time in the entryway, but Noah manages to answer my question before I even ask it."
            
            n "\"I know it wouldn’t make sense to read here, but I’m often called away from my reading to come greet guests.\""
            
            m "\"Makes sense,\" I mutter, nodding, but I’m distracted by the grand scale of the room. The last time I was here, I was too overwhelmed and terrified to take in how beautiful the room really is."

            m "Brightly-colored banners hang between five stained glass windows, each with a different scene."
            
            m "At that time, I was also too overwhelmed to notice the music."
            
            m "It’s a grand theme befitting a grand room, with brass fanfares and a march rhythm. The contrast is so stark compared to the music from the meadow that it makes my head spin."
            
            m "I start to think about the military implications of a march theme before I remember that I know very little about this kingdom’s history, fictional or otherwise."

            m "Then again, perhaps it doesn’t matter. Perhaps since this music is made for me, the player, to hear… then it’s just based on my perception."
            
            m "That would make the most sense, I decide. If I’m supposed to gather meaning from the music that only I can hear, then it isn’t music made for the people of this kingdom, and thus my perceptions of musical symbolism should still apply, at least to a degree."
            
            m "This music tells me that the castle entryway, as a location, holds some sort of importance for the kingdom. An expression of pride, of heralding visitors into the castle with fanfare, of showcasing what Phenai has to offer in one room… It certainly supports the surroundings."
            
            n "\"The stained glass is beautiful, isn’t it? The scenes illustrate folklore and symbols of Phenai.\""
            

            hide noah sprite 
            
            # ASK
            # Which one is this?
            # Castle Entryway

            # TODO
            #Background: zoom on windows
            # ???
            
            m "At Noah’s comment, I look closer at the windows."
            
            m "The first one, unsurprisingly, shows a sheep."
            
            m "Another shows a tangle of rose vines, like the roses on the Phenai banner."
            
            m "Yet another window shows textile trades, specifically spinning wool into thread and weaving it into cloth. It would make sense that Phenai specializes in textiles, what with the importance of sheep."
            
            m "Another window shows a glass representation of the townscape, castle in the distance included, a representation of what I saw from the cart when I first arrived."
            
            m "The center window is the one that captures my attention, though."

            m "It’s a more complex scene than the other windows, showing something that appears to be a long-bearded man holding a storybook in one hand and a staff in the other."

            m "I step a little closer to examine the image."

            camera:
                ease 1 zpos -300

            play music lorenzo_theme

            $ renpy.pause()
            
            m "I blink, stepping back from the window."

            camera:
                ease 1 zpos 0
                      
            play music castle_theme volume .8

            $ renpy.pause()
            
            m "… Weird."
            
            m "I step closer to the window again."
            
            camera:
                ease 1 zpos -300

            play music lorenzo_theme

            $ renpy.pause()
            
            m "Yep, the music definitely changed here. So… What makes this scene different than the others?"
            
            m "Most obviously, it’s the only one with a person, but none of the other windows triggered a change in the game music like this one did. Does that have something to do with the person pictured, I wonder?"
            
            m "Digging through my memory, I struggle to place both image and music. It tickles some kind of recognition in the back of my mind, but I can’t quite place it."
            
            m "On the table is a cup and a sword. I know that in fairy tales, the legend of the cup and sword relates to the fisher king— one to catch the blood and one to spill it. In some tales, it’s the choice between vengeance and mercy, between aggression and healing."
            
            m "That’s when the icon at the top of the scene catches my eye, though."
            
            m "It’s a five-pointed star inside a circle. Something in my brain recognizes it: pentacle."
            
            m "That’s when it clicks and I recognize the illustration. Save for the storybook, it’s an image that is almost an exact representation of the Magician card in a tarot deck."
            
            m "\"Who is this?\" I ask Noah, still squinting at the image."

            show noah sprite at centerright:
                zpos +300
            
            n "\"No one is entirely sure. Some people say he’s the first historian in Phenai, keeping records of the kingdom and making sure it’s all passed down, but if you actually look at the early records…\" he winces."
            
            m "\"What about them?\""
            
            n "\"They’re terrible, frankly. Badly organized, only vaguely kept at all. Hardly a reason to immortalize someone.\""
            
            m "As I stare at the image, wondering if I’m just imagining the connection with the tarot card, I suddenly realize that something looks familiar."
            
            m "\"That sash…\" I mutter, squinting at the cloth around the figure’s waist."
            
            m "Granted, it’s a chunky representation in stained glass, but I know I’ve seen it before. I just can’t quite remember where."
            
            n "\"What’s this…?\""
            
            #Background: zoom back out from windows
            
            # TODO
            #Music: Phenai kingdom theme
            play music castle_theme volume .8
            
            m "When I glance over, he’s reaching towards where a battered book is lying at the corner of the windowsill. I didn’t notice it before, too preoccupied with the window itself, but it appears to have been sitting there for a while."

            m "Noah brushes dust off the cover and coughs, flipping through the pages."
            
            n "\"Well, that’s certainly not what I’m looking for. I can’t even read it,\" he says, shaking his head."
            
            m "\"What language is it?\""
            
            n "\"I don’t know. I’ve never seen it before.\" He shrugs and offers the book to me. \"If you’d like to take a look at it, you’re welcome to do so.\""
            
            m "I’m not really sure what I can do with it if he doesn’t know the language, but I decide that it can’t hurt to take a peek. After all, the game translation circuits might kick in."
            
            m "However, as I open the book, it’s clear that the game translation circuits are not going to kick in."
            
            m "I can see a jumble of characters in the Roman alphabet, separated by spaces, but I can’t make out the seemingly random jumble of letters."

            m "They look more like keyboard smashes than an actual language, despite the spacing, and even the author name and book title on the first page look like random text."
            
            m "I squint at the page. My language skills aren’t fantastic, but at least if it was Latin or German or French, or even Spanish, I might stand a chance. This looks like… absolutely nothing."
            
            # TODO
            #Sprite: Lorenzo MEGA CLOSE UP
            hide noah sprite

            show lorenzo sprite:
                xalign .5
                yalign -.05
                zoom 5

            u "\"Are you enjoying the castle tour?\""
            
            play music lorenzo_theme

            m "I bite my lip to keep from screaming and almost drop the book as I look up at the huge, black bird beak in front of me. Instead, I clutch it close to my chest and take a step back, heaving a sigh of relief."

            hide lorenzo sprite
            
            show lorenzo sprite at centerright
            show noah sprite at centerleft
            
            m "\"Do you scare the snot out of everyone when you say hello, or is it just me?\" I grumble."
            
            m "(I did not use the word ‘snot.’ Stupid censoring.)"
            
            "Patcher" "\"My apologies. I simply wanted to check on your progress. And good morning to you, too, Your Majesty.\" He inclines his bird beak towards Noah."
            
            n "\"Good morning, ah…?\""
            
            m "Noah clearly sounds like he’s waiting for a name, but the Patcher acts as though he hasn’t heard at all. He turns his bird beak back to me, tilting down towards the book I’m holding."
            
            "Patcher" "\"I certainly hope you’re planning to put that where it belongs,\" he says pointedly. \"If you like, I’m certain I can help you file it.\""
            
            m "Something about his tone ruffles my feathers. I feel a bit like a cat hissing at a threat, ready to scratch at any moment, but I’m not sure why. Perhaps it’s that he’s trying to tell me what to do, and I’ve never taken well to that."
            
            m "… Or perhaps it’s because he’s reaching for the book that I’m holding very firmly."
            
            m "\"No, thank you,\" I say, snatching the book away just as his fingers brush the fabric cover. \"I can handle it myself.\""
            
            m "His shoulders stiffen as he steps back from me, and though I can’t read his expression under the mask, his body language tells me he isn’t happy with my response, though I can’t tell if he’s offended, angry, saddened, or anything else in between."
            
            "Patcher" "\"Remember: I am here to assist you. I want you to achieve your goal as much as you do,\" he says carefully, his tone lightening."
            
            m "\"I’m making progress,\" I say firmly, though I’m not really sure if I am any more."
            
            "Patcher" "\"I should hope so.\""
            
            hide lorenzo sprite 
            
            play music noah_theme
            
            # ASK
            #Background: normal entryway
            scene bg castlecurtains
            show noah sprite at centerright
            
            m "At that, the Patcher turns on his heel and walks away, leaving Noah and I alone in the entryway. I turn to the prince to find him watching the beaked figure walking out of the room."
            
            n "\"Do you know him?\" he asks absently. \"I’m certain I’ve seen him before, but not… I’m not sure where.\""
            
            m "\"I’ve seen him here and there. He pops up at the least convenient times.\""
            
            n "\"He seems… very invested in you,\" Noah says carefully."
            
            m "I can’t say I get it, but I think he’s trying to be encouraging.\""
            
            n "\"It’s interesting,\" Noah begins, turning back towards the windows. \"Don’t you think his sash—\""
            
            m "But then Noah crumples, knees buckling and doubling over, stopped mid-sentence. On instinct, I reach out to him, putting a hand on his shoulder as he winces in pain."
            
            m "\"Noah? Noah, talk to me! Are you okay?\" I’m frantic, panicking. I can see him wincing in pain, his breathing too fast, his eyes squeezed shut and fists clenched so tightly his knuckles are white."
            
            n "\"I’m… I can’t…\" he struggles to say, but cannot manage any more, sinking to his knees."
            
            m "I kneel to the ground beside him, ready to call for help, but suddenly… his breathing slows."
            
            m "Like flipping a switch, his body calms. Noah’s breathing slows and his eyes open. The tension fades from his shoulders as he sits upright, looking around the room in a daze. His eyes are unfocused and cloudy, and a wrinkle of confusion crosses his forehead."
            
            n "\"Sorry. What were we talking about?\" he asks, blinking. \"Why… am I on the floor?\""
            
            m "A strange tightness settles into my chest, but I keep my expression carefully blank as I speak, still holding the book tightly as I help Noah to his feet."
            
            m "\"Nothing. Let’s… go find that book?\" I carefully watch his expression as I speak, but he still looks like he’s walking around in a fog, like trying to find something without knowing what he’s searching for."
            
            n "\"Yes… We should do that.\""
            
            scene bg kitchen
           
            m "I still feel uneasy as we leave the entryway and wander through the castle towards the kitchens, like there’s an itch I can’t scratch, but there’s not much I can do about it now. I should spend some time investigating that book from the entryway later, I decide, clutching it close to my chest."
            
            show noah sprite at centerleft

            n "\"I don’t intend to stop here for long, but we should both get a little food while we’re passing through,\" he says, turning into the kitchens."
            
            m "My stomach growls in agreement. It’s been a long while since breakfast and a while since lunch, too, but we both lost track of time."
            
            m "Entering the kitchens, I notice the music has changed yet again."
            
            m "I notice that the music now seems stable, practical, and consistent. That makes sense for a work space, and the simple melody is catchy and easy to hum. Work songs have a long and rich history, and this tune wouldn’t be out of place with them."
            
            m "As I look around, my mind on the sounds of the crackling fire and the kettle hissing steam as it hangs on the crane over the flames, I finally set eyes on the figure in the corner, quietly munching a snack and waiting for us to see them."
            
            n "\"Kylie?!\""
            
            play music kylie_theme

            show kylie sprite at centerright
            
            m "I whirl around to see the princess sitting on a stool in the corner, munching on a loaf of fresh bread by the fire."
            
            k "\"Hi,\" she says, speech muffled through a mouthful of bread."
            
            n "\"Do you ever stop snacking?\" he mutters, rolling his eyes."
            
            k "\"No.\" She swallows thickly and brushes a few crumbs off her skirt. \"Besides, aren’t you here for food, too?\""
            
            n "\"Missed lunch. We were sidetracked trying to find a book. You haven’t seen Invisible Wounds around here anywhere, have you?\""
            
            m "Kylie’s eyes light up in recognition."
            
            k "\"Oh! That one. It’s in my room.\""
            
            n "\"WHAT?\" His jaw hangs open, shoulders slack as he stares."
            
            k "\"I borrowed it from your desk because I thought it looked interesting and magical, but it was actually really boring. I can go get it!\""
            
            n "\"Please do,\" he says with a heavy sigh, rubbing a hand over his eyes."
            

            play music kitchen
            
            hide kylie sprite 
            
            m "As Kylie leaves, loaf of bread in hand, Noah turns to me, the tips of his ears turning red."
            
            n "\"I am so sorry,\" he says earnestly."
            
            m "\"It’s okay. I did get to see the castle, and we did find the book, so… goals accomplished?\" I shrug. I feel like I should be more anxious than this, more particular about getting the library organized, but in reality… I had fun."
            
            m "I can’t remember the last time I had a day just for fun. It’s hard to find time for yourself, and somewhere along the way I simply stopped taking any time at all. This was a really nice break, and I feel lighter and refreshed because of it."
            
            m "As I’m thinking over this, Noah pulls an iron kettle off the fire."
            
            n "\"Coffee?\" He asks, eyebrow raised."
            
            m "\"Ah, no thank you, I’m a tea drinker.\""
            
            n "\"I am, too. I’ll brew us a pot,\" he says with a tired smile."
            
            m "Noah busies himself putting the tea together while I hunt down sandwich materials. I manage to find some bread and hard-boiled eggs from this morning, and put them together with some spices and pickled cabbage from a pottery crock on the shelf."
            
            m "All in all, not a bad lunch! Though I can’t say I’ve ever made a sandwich for a prince before, he seems to like it, and we eat in a peaceful, settled silence for a while."
            
            m "After I swallow the last bite of my sandwich, Kylie still isn’t back, and I find that I’m watching the door and waiting for her return. I don’t know how far her rooms are from the kitchens, though."
            
            n "\"I bet she got distracted,\" he mumbles. \"Typical Kylie.\""
            
            m "Though I haven’t seen them interact much, I already find Noah and Kylie’s sibling relationship endearing, and it brings a smile to my face even as I turn back to his grumpy frown."
            
            m "\"I never asked: What is Invisible Wounds even about?\""
            
            m "My instinct says it’s something about arthritis, tumors, brain damage, or anything else not inherently visible that could cause medical issues, but I’m interested to know what kind of science is in this place, even if it’s pretty far off from modern medicine."

            m "Noah’s entire demeanor shifts as he begins to speak, cheering him immediately."
            
            n "\"Oh, it’s about emotional scars,\" he says calmly, as though that’s a common topic, but I suddenly freeze in place."
            

            play music mc_theme
            
            m "\"Like… mental health treatment?\" I ask, frozen with my teacup only inches from my lips. It’s a pretty modern topic for a fantasy game."
            
            n "\"If you’d like to call it that, yes.\""
            
            n "\"In truth, I thought it might be of some personal help,\" he admits, his voice growing a little softer. \"I am not taking the emotional split of duty and passion particularly well.\""
            
            m "\"Yeah, I get that. And then when you figure out you don’t love something any more that you used to love, and now you’re kinda stuck with it.\""
            
            m "Noah turns to me, raising an eyebrow."
            
            n "\"Seems like a personal anecdote.\""
            
            m "\"Unfortunately,\" I grumble, sipping my tea. \"I was talking to Leslie about it a little.\""
            
            n "\"So what… do we do?\""
            
            m "\"Tarran told me something the other day: Your entire life isn’t defined by your title.\""
            
            m "\"We were talking about his role as a knight, and even though he has a lot of pride in it, it isn’t everything that makes him who he is.\""
            
            m "\"Something I’ve been kind of… forced to deal with in the last few years is that you can’t build an entire identity around one part of yourself. I haven’t really figured out how to reconcile it yet. Still a work in progress, you know? But you just… you can’t. It’ll destroy you.\""
            
            n "\"How so?\" he asks softly."
            
            m "\"It’s…\" I pause, licking my dry lips as I try to think of how to phrase it."

            m "\"When you place so much value on one part of yourself and build your entire personality around it, then what happens when that collapses or changes? Because it will change, at the least, in one way or another.\""
            
            m "\"I wonder if that’s why people are so resistant to changing the way they do things sometimes, especially in their careers."

            m "It’s changing part of this central identity they’ve build for themselves, in a way, and it’s natural to be resistant to that, because in your mind it’s subconsciously connected to changing a very personal and important part of yourself.\""
            
            m "\"You have to be more than a career and more than a hobby and more than a someone who does something."

            m "Or maybe you have to be someone who does a lot of somethings. I don’t really know, but I know that you can’t define your whole self by just a part of who you are.\""
            
            m "\"Trust me when I say that it will crush you,\" I mutter."
            
            n "\"What did you do before you got here, [player_name]?\" He tilts his head inquisitively as he looks at me over the rim of his teacup."
            
            m "I open my mouth to respond, feeling myself settle into place to give the description I’ve given a hundred times before, almost like muscle memory taking over…"
            
            m "… but nothing comes out."
            
            m "My mouth hangs open in horror as I realize that I can’t seem to remember what I was doing or where I was before I came here."
            
            m "I remember my childhood. I remember school, I think, and I remember vague impressions of classrooms and blurry silhouettes of people, but I don’t remember what I was studying."

            m "I remember being in the library before I entered this world, but I don’t remember what I was doing or why I was there."
            
            m "All the words that just spilled out of my mouth are true, I know that, but I don’t remember why. I don’t know what made me come to believe these things. I don’t know what experiences are fueling the emotions building in my chest."
            
            n "\"[player_name]?\""
            
            m "With a jolt, I come back to my senses and realize that I’m hyperventilating, breath coming far too fast and eyes wide."
            
            m "\"I… I have to go, I’m sorry,\" I squeak out, jumping to my feet and walking out of the kitchen with as much restraint as I can manage."
            
            m "I need to find the Patcher. I need to find the Fairy. I need to talk to someone. I need to sit. I need to run. I need to finish organizing the library."
            
            m "I need to go home."
            
            m "My steps get faster and faster, and suddenly I’m running all the way back to the library."
            
            label chapter4_redirect:
            
                # TODO
                #Background: library 1
                scene bg castlelib
                
                # TODO
                # ASK
                #Music: fantasy ambient
                #play music nighttime
                
                m "I sigh as I flop down on a chair in the library. The Fairy, who has been absent all day, is waiting for me there, perched on a table and reading a page in an open book that is far too big for her."
                
                m "\"At this rate, I’m really not going to be able to get anything else done today.\" A quick glance out the window reveals that the sun is already low in the sky."

                m "There’s precious little time until we lose the light, and besides searching with Noah and placing a few boxes, I’ve gotten nothing done today. We spent more time looking for that book than I’d intended."
                
                m "A knot of anxiety forms in my chest and settles there, constricting my throat and making my stomach roil."
                
                show fairy sprite at fairycenter
                f "\"What’s wrong?\" She lands on my shoulder and perches there, her voice gentle rather than her usual demanding tone."
                
                m "\"What if I can’t do this in time?\" I whisper. \"What if I’m stuck here forever?\""
                
                f "\"I don’t know,\" she says sadly. \"I wish I did.\""
                
                m "I place my head in my hands, rubbing my temples. Should I stay awake longer? Should I try to power through this at any cost? Is this like a last-minute workload that has to be done no matter what, or is there something I’m missing entirely?"
                
                m "Is there even any chance of me getting home at all?"
                
                m "Tears leak out of the corners of my eyes, and even though I wipe them away, they don’t seem to stop coming."
                
                m "\"Why can’t anyone tell me what to do? Why is the only person who knows anything the stupid guy in the bird mask?\" I choke out through my sobs. \"I mean, you’re part of the game system and not when you’re sure what I’m supposed to do!\""
                
                f "\"… I’ve been thinking about that,\" she admits."
                
                m "I perk up a little at the strange tone in her voice."
                
                m "\"Thinking about what? How to win the game and get me home?\""
                
                f "\"Sort of. It’s just… this game is a story, yeah?\""
                
                m "\"Yes…?\" I blink away more tears, confused."
                
                f "\"I don’t really know if you can win at a story. Maybe it’s not about that. Maybe it’s about… getting to the end.\""
                
                m "\"So why didn’t the Patcher tell us that? If he’s supposed to fix things, then… shouldn’t he know? If he’s a patch to the system?\""
                
                f "\"I was thinking about that, too,\" she says slowly."
                
                f "\"Could be I’m reading into this, but if he’s a patch, that means he wasn’t here to begin with, right? It implies he was added later for something."

                m "I know I’m the system interface. I don’t have information, but I can help you as the player interact with the game functions. We don’t really know what Bird Man was added for, though, and I don’t remember when he got here.\""
                
                m "\"Does that… bother you?\""
                
                f "\"A little, yeah. It bothers me that I can’t read his data and it bothers me that he doesn’t show up on my system map. There’s something… weird.\""
                
                m "\"Maybe he was added later to help make the game easier?\" I suggest, shrugging helplessly."
                
                f "\"Is he making it easier for you, though?\" the fairy asks, narrowing her eyes. \"Is he really?\""
                

                menu:
                    "he is":
                        $ affection [6] = -1
                        jump he_is
                    "he isn't":
                        $ affection [6] = 1
                        jump he_isnt
                    "I don't know":
                        jump i_dont_know1


                label he_is:
                
                    m "\"He is.\""
                    
                    f "The fairy squints."
                    
                    m "\"Oh, come on, he’s the only one who’s given me any real information about this place so far.\""
                    
                    f "\"HEY!\" she shouts, crossing her arms over her chest."
                    
                    m "\"You’re very helpful, I promise,\" I say gently, forcing a small smile. \"But even you admit that you don’t know how I’m supposed to get home. We’re just making our best guess here.\""
                    
                    f "\"Okay… You’re the player and I’m the interface,\" she says with a sigh, \"So I’ll follow your lead. If you want to trust him, trust him.\""
                
                    jump chapter4_redirect_2
                

                label i_dont_know1:
                    
                    m "\"I… I’m not sure.\" My head is pounding and a thousand thoughts are running through it. I can barely think at all at the moment, much less think critically."
                    
                    m "The fairy frowns at me."
                    
                    f "\"I think you might want to figure that out. Quick.\""
                
                    jump chapter4_redirect_2


                
                label he_isnt:
                    m "I think over my past encounters with the masked man. What all has he really done for me?"
                    
                    m "\"I… you know, now that you mention it… I don’t think he’s making it easier after all.\""
                    
                    m "Looking back, he’s given me precious little information at the cost of spiking my anxiety over the whole situation to skyscraper heights."

                    m "He’s told me that organizing the library is the way home, but… none of the other characters seems to be encouraging me to do that in the same way he is."
                    
                    m "\"Don’t most key NPCs in video games do their best to keep the player on the main quest?\" I ask absentmindedly."
                    
                    f "\"What do you mean?\""
                    
                    m "\"It’s just… he’s the only one that’s encouraging me to really get on the move with organizing the library. Like. The only one.\""
                    
                    m "\"The other characters I’ve talked to have tried to, like… actually talk to me about other things. The patcher hasn’t, and I can’t figure out if that’s a good thing or a bad thing. But it freaks me out a little that he’s the only one talking that way.\""
                    
                    f "\"You do have a point there…\""

                #REDIRECT POINT FOR ALL CHOICES>>>>
                label chapter4_redirect_2:

                    m "\"Maybe it’s time I go to bed. We can talk about this more tomorrow.\""
                    
                    f "\"Agreed. I know you have a lot on your plate, but you won’t be able to get any of it done without sleep.\""
                    
                    m "She’s right. I know she is. However, as I make my way back to my room, I can’t stop turning over our conversation in my mind."
                
                    scene black with fade

                    stop music
                    stop sound 
                    jump chapter5