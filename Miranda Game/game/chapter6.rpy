

label chapter6:
    m "I can’t tell if the fantasy profanity censors are working over the din of the rumbling, shaking, and falling stone, but I’m sure I sound exactly like a screaming chicken if they are."
    
    m "I land painfully on my knees beside the unconscious Lorenzo, and Kylie goes down with me. Only a moment later the shaking stops, but it’s not enough to stop the sheer panic screaming in my gut."
    
    m "This isn’t like before. This isn’t like the worry I wouldn’t finish my task with the library. Something is wrong. I feel it in my bones."
    
    m "\"What. Was. That.\" I speak through gritted teeth and struggle to my feet, leaning on the wall for support, my knees still stinging from the impact against the stone floor."
    
    k "\"This piece of festering human waste created this place,\" Kylie explains, her voice dripping with vitriol. \" Since he created it, I’m guessing he has a certain amount of connection to it.\"" 
    
    k "\"Lorenzo is dying, so the magic that holds this place together is collapsing. And, frankly, I’m not too keen on the idea of saving him. He’ll just keep this purgatory cycle going to the end of time.\"" 
    
    m "\"Do you have an alternative suggestion, then?\" I try and fail to keep the squeak out of my voice. Kylie sighs, shaking her head as she nervously runs a hand through her hair."
    
    k "\"I wish I had a solution, but I… I only know storybook magic rules. Not real magic rules.\" She takes a deep breath to steady herself. \" The best guess I have is that… maybe you stand a chance of using what magic is left to find your way out of here before the whole place collapses in on itself.\"" 
    
    m "\"What happens to all of you if I leave, though?\"" 
    
    k "\"Like I said, I only know storybook magic rules. I’m just guessing, but… I think we probably go down with the ship, if you get my drift.\" There’s a hollow, resigned look in her eyes as she swallows hard."
    
    m "\"I’m not just leaving you here!\" I screech."
    
    m "I can’t leave them here. There’s no way, not now that I know they were all helpless victims, the same as me. They all have real lives to return to."
    
    k "\"All our memories are gone now. We don’t know what’s going to happen to us even if we did go back.\"" 
    
    m "My heart sinks like a stone."
    
    m "I open my mouth to respond, but a scream from down the hallway cuts me off. Kylie’s eyes go wide as she turns towards the sound."
    
    k "\"You should go.\"" 
    
    m "\"But—\"" 
    
    k "\"GO, NOW!\"" 
    
    

      

    python:

        total = 0

        for x in affection:
            total = total + x

        if total >= 7:
            renpy.jump('good_ending')

        elif total >= 4:
            renpy.jump('normal_ending')

        else:
            renpy.jump('bad_ending')

    
    #[[STUCK ENDING (BAD END 3) – low affection

    label bad_ending:
        m "I hear a coughing sound behind me before I can take off, though when I turn back I’m surprised to see that Kylie has disappeared. I don’t know where she went, but it’s just me and a dying Lorenzo now."
        
        lo "\"Wait,\" the magician croaks out."
        
        lo "\"You have the power to save them.\"" 
        
        #play music bad_end
        
        m "I freeze. It sounds too good to be true, especially coming from him."
        
        m "\"… How do I do that?\" I narrow my eyes, suspicious."
        
        lo "\"Simple. As I said, the memories of your world, of your childhood and life before this, are much more potent than memories made here, and you are the only person with access to them. Besides myself, of course,\" he amends quickly."
        
        m "\"Then you sacrifice memories this time,\" I snap."
        
        lo "\"If I sacrifice mine, I will forego knowledge of how to keep this place intact for the rest of us,\" he says matter-of-factly. \" It must be you.\"" 
        
        lo "\"If you sacrifice your memories to fuel the magic here, then we will all live on. I can use that power to heal the world, to heal myself, and keep a steady hold on the life we all have here.\"" 
        
        m "My stomach roils, but I can’t tell if it’s from my emotions or the quaking castle around me."
        
        m "The most terrifying thing about this entire experience so far is that Lorenzo, for all his twisted logic, does actually make sense in this moment. It might be the only option that we have."
        
        lo "\"It’s not so bad, after all,\" he says, his voice taking on an almost soothing tone. \" I can make your story whatever you want. You could be a princess, a sorceress, a famed scholar—anything your heart wants and your mind can imagine, I can do for you.\"" 
        
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
        
    # TODO
    #Background: fade to black
        
        lo "\"There now, I promise it won’t be so hard. Perfectly painless.\"" 
        
        m "And it is. Mostly."
        
        m "The first thing I notice is that it’s cold. It’s like everything around me is freezing and dark and the darkness is closing in… "
        
        m "And then the pressure releases with a pop, almost like ears adjusting to high altitudes, and I feel… better."
        
    # TODO
    #Background: castle hallway left
        scene bgp
        
    # TODO
    #Sprite: Lorenzo
        show lorenzo sprite at center
        
        m "The only problem is that I don’t remember how I got here. Where am I?"
        
        m "Who am I?"
        
        m "I know my name, but I can’t seem to place anything else about myself, or about the stone-walled hallway I’m currently standing in, or about the admittedly frightening masked man standing in front of me."
        
        m "\"What’s happening?\" I manage to squeak out. My throat is raw and I realize my cheeks are wet, like maybe I’d been crying, but I don’t know why I would have been."
        
        lo "\"Why, you’re the castle librarian,\" he says. \" Come with me. I’ll show you your new home.\"" 
        
        # TODO
      #Background: fade to "THE END"

        jump the_end
        
    # TODO
    #NORMAL ENDING – med affection

    label normal_ending:
        
        m "Spurred on by Kylie’s shout and sheer adrenaline, I scramble down the collapsing hallway and back towards the library."
        
        f "\"Shouldn’t we be getting OUT of the castle?\"" 
        
        m "\"We can’t! If books are the catalyst for the magic in this place, it stands to reason that the library is our best chance of getting out of here!\"" 
        
        f "\"Okay, fair point! EEK!\" She screams as she dodges a piece of falling debris."
        
        m "I skid to a stop in front of the library doors, making my way past the messiness of the main stacks and towards the archive. Everything helpful that I’ve found so far has come from there. Maybe there’s a way out there, too."
        
        m "The only problem is that I don’t know what I’m looking for. At all. There are too many books and documents and not enough time. I squeeze my eyes shut in frustration—"
        
        m "And that’s when I hear it."
        
        # TODO
      #Music: protagonist’s waltz
        play music mc_theme
        
        m "It takes me a moment to identify it."
        
        m "It’s a dance-like theme, a little unbalanced and a little unsteady, but endearing all the same. I could waltz to this if I wanted to. I almost do, my feet stepping and turning all on their own as I follow the music to the back corner of the room."
        
        m "The tune is… a little unusual, if I’m honest. It’s chromatic and winding, wandering, with large leaps and sudden short runs interspersing a long, melodic line, but… I like it."
        
        m "It isn’t until my eyes catch on a flash of gold that I realize where it’s coming from."
        
        m "It’s a book. It’s brown and leather, and besides the peeling gold text embossed on the spine, it looks pretty unassuming, but I pull it off the shelf anyways and put it on the wide table in the middle of the room."
        
        m "When I open it, I finally realize why I like the tune so much."
        
        m "It’s me."
        
        m "The inside of the book shows a chapter index— \"Our Journey Begins\", \"In the Land of Sheep\", and on through \"The Way the Castle Crumbles\" which I can only assume is what is happening this very minute. I even see an illustration of myself in the cart on the first page."
        
        m "This is MY story. It’s my tune, my music playing in my ears, it’s the sound that encompasses my personality and my confusion and the resolution to my troubles all in one."
        
        m "My initial instinct is that if my whole story is written here, maybe it’ll tell me how to get out. Maybe all I have to do is follow the clues and I’ll get back home. Maybe the directions were here the entire time, like sparkling silver slippers ready to take me home."
        
        m "However, when I flip through the last chapter, my heart sinks."
        
        m "The back of the book is blank."
        
        m "I want to scream. I want to cry. I want to rail against the universe for dangling the solution in front of me and then not providing the way out."
        
        m "But then, just as I’m ready to entirely give up, the castle shakes again and something drops to the ground beside me."
        
        m "It’s a pen."
        
        m "It’s not a quill, it’s an actual ink pen, though it’s a fountain pen in an older style. I pick it up almost dazedly, reflexively, and that’s when something dawns on me."
        
        # TODO
      #Sprite: fairy

        show fairy sprite at center
        
        f "\"Maybe it’s not about winning, maybe it’s about getting to the ending.\"" 
        
        # TODO
      #Fade away fairy sprite
        hide fairy sprite
        
        m "That’s it. That’s the solution I’ve been looking for this whole time. The Fairy knew what I was supposed to be doing after all."
        
        m "I uncap the pen and begin to write. My scrawl is quick and messy, the ink smudging slightly as my hand drags across the paper in my desperate attempt to put words on the page, but it does the job."
        
        "The librarian finished her task."
        
        "The story completed, she was released and returned home."
        
        "THE END."
        
        # TODO
      #Background: whiteout

        scene bgp
        
        m "As I place the final period, the world goes white."
        
        m "I am entirely blinded for a moment, but then the world seems to spin, and spin, and spin even in the blinding white nothingness, and suddenly—"
        
        # TODO
      #Background: library computer
        scene bgp
        
        # TODO
      #Music: ordinary day theme

    label chapter_1_ending:

        play music ordinary_day
        
        m "I wake with my face in a small puddle of drool on the particle board library desks, slumped over in a way that makes my back cry out in protest when I straighten my spine."
        
        m "Did I fall asleep?"
        
        m "I wipe the drool from my face, looking around to see if anyone saw me, but no one else is on this floor. Typical. The sun is setting, though, and that’s strange to me."
        
        m "I’ve never fallen asleep at a library desk before. Even more than that, my heart is hammering in my chest like I’ve just run a marathon, but I have no idea what I was dreaming about, or even if I was dreaming at all."
        
        m "Eh, probably just stress nightmares again. No big deal."
        
        m "Still strange that I slept the… whole day on this desk? I look at the computer screen, strangely not in sleep mode despite the fact that I clearly haven’t touched it for hours. There’s a weird program icon on the desktop, something that looks like a pixelated storybook."
        
        m "Some strange sense in the back of my mind tingles, and I almost click it from sheer curiosity, but the ding of the elevator brings me back to my senses."
        
        m "I should get some food. I’ve wasted enough time today."
        
        # TODO
      #Background: fade to THE END

        jump the_end
        
    label good_ending:
      #GOOD ENDING – high affection
        
        m "Before Kylie has a chance to run down the hallway, I grab her arm."
        
        m "\"Meet me in the library!\" I shout above the din."
        
        m "\"Gather everyone you can—everyone you know with missing memories—and meet me back in the library as fast as possible!\"" 
        
        m "Kylie stares back at me for one long heartbeat. Then two."
        
        m "Then she nods quickly and shakes free of my grip."
        
        k "\"We don’t have much time. I’ll be back as soon as I can.\"" 
        
        m "I scramble down the hallway, skidding around corners as fast as possible as I sprint towards the library. I only have a very, very vague thought in my head, and I’m not sure it’s going to work, but I think it’s worth a shot."
        
        m "It might be the only shot we have."
        
        m "As the castle shakes, the fairy flies up beside me."
        
        f "\"What are you DOING? We have to get OUT of this building—\"" 
        
        m "\"I’m not leaving! Everything so far has been about that library. There are things in there that connect to everyone in this castle. There’s got to be something that gets us out there, too!\"" 
        
        f "\"That’s one heck of a hunch…\"" 
        
        m "\"It’s the only one I’ve got at the moment. Let’s go!\"" 
        
        m "Lungs burning, I finally slide through the doors to the library and pick my way around cluttered boxes, fallen and scattered in the earthquake, to get to the archive room."
        
        m "The only problem is that I don’t know what I’m looking for. At all. There are too many books and documents and not enough time. I squeeze my eyes shut in frustration—"
        
        m "And that’s when I hear it."
        
        # TODO
      #Music: protagonist’s waltz
        play music mc_theme
        
        m "It takes me a moment to identify it."
        
        m "It’s a dance-like theme, a little unbalanced and a little unsteady, but endearing all the same. I could waltz to this if I wanted to. I almost do, my feet stepping and turning all on their own as I follow the music to the back corner of the room."
        
        m "The tune is… a little unusual, if I’m honest. It’s chromatic and winding, wandering, with large leaps and sudden short runs interspersing a long, melodic line, but… I like it."
        
        m "It isn’t until my eyes catch on a flash of gold that I realize where it’s coming from."
        
        m "It’s a book. It’s brown and leather, and besides the peeling gold text embossed on the spine, it looks pretty unassuming, but I pull it off the shelf anyways and put it on the wide table in the middle of the room."
        
        m "When I open it, I finally realize why I like the tune so much."
        
        m "It’s me."
        
        m "The inside of the book shows a chapter index— \"Our Journey Begins\", \"In the Land of Sheep\", and on through \"The Way the Castle Crumbles\" which I can only assume is what is happening right this very minute. I even see an illustration of myself in the cart on the first page."
        
        m "This is MY story. It’s my tune, my music playing in my ears, it’s the sound that encompasses my personality and my confusion and the resolution to my troubles all in one."
        
        m "I don’t have time to flip any further before I hear voices at the door."
        
        # TODO
      #Music: castle day

        play music castle_day
        
        k "\"HELLO? ARE YOU DEAD?\"" 
        
        m "I bark out a laugh despite myself."
        
        n "\"That’s the greeting you go with?\"" 
        
        m "\"I’m in the back!\"" 
        
        m "Four familiar faces come tumbling through the door to the archive shortly after my shout. Kylie, Noah, Tarran, and Leslie all stare at me with wide eyes, their gaze going from me to the book open on the table in front of me and back again."
        
        # TODO
      #Sprites: tarran, Leslie, noah, kylie

      # GOTTA FIGURE THIS ONE OUT
        
        t "\"We caught Lorenzo trying to crawl out of the grave on the way here,\" he says darkly."
        
        t "\"He won’t be causing trouble any longer.\"" 
        
        m "\"So he’s…?\" I trail off. Did they kill him? I know our lives are at stake, but that still seems a little shocking."
        
        l "\"Hog tied in the hallway. Tarran’s being dramatic.\" She rolls her eyes."
        
        l "\"As much as we want him to get what’s coming to him, Kylie thinks killing him will only make the whole place collapse even faster.\"" 
        
        k "\"Considering he’s probably somehow tied to the magic keeping us all here, I think it’s better to run than anything.\" She pauses, taking a look at the book on the table. \" What’s that?\"" 
        
        m "\"I think… I’m not sure, but I thought there might be a way to get us out of here. If you want.\"" 
        
        m "The four of them look between each other knowingly." 
        
        m "Their lives had been stolen from them. I didn’t know how much Kylie had told them or how much they remembered now that the magic was crumbling, but it was clearly enough to make them understand the gravity of the situation."
        
        k "\"… Do it,\" she whispered, barely audible over the most recent round of shaking and rumbling."
        
        t "\"I agree. Get us out of here.\"" 
        
        l "\"It’s time.\"" 
        
        m "I look between them slowly. \"You’re… sure? I’m not even certain this is going to work.\"" 
        
        n "\"It’s now or never. We’re all with you: we don’t want to live in a fantasy where our entire lives are written for us.\"" 
        
        n "\"You’ve come closer than any of us when we were in your shoes. We might as well try.\"" 
        
        m "\"Okay,\" I say, nodding slowly."
        
        # TODO
      #Fade away all sprites

      # 
        
        m "My initial instinct is that if my whole story is written here, maybe it’ll tell me how to get out. Maybe all I have to do is follow the clues and I’ll get back home. Maybe the directions were here the entire time, like sparkling silver slippers ready to take me home."
        
        m "However, when I flip through the last chapter, my heart sinks."
        
        m "The back of the book is blank."
        
        m "I want to scream. I want to cry. I want to rail against the universe for dangling the solution in front of me and then not providing the way out."
        
        m "But then, just as I’m ready to entirely give up, the castle shakes again and something drops to the ground beside me."
        
        m "It’s a pen."
        
        m "It’s not a quill, it’s an actual ink pen, though it’s a fountain pen in an older style. I pick it up almost dazedly, reflexively, and that’s when something dawns on me."
        
        # TODO
      #Sprite: fairy

        show fairy sprite at center
        
        f "\"Maybe it’s not about winning, maybe it’s about getting to the ending.\"" 
        
        # TODO
      #Fade away fairy sprite

        hide fairy sprite
        
        m "That’s it. That’s the solution I’ve been looking for this whole time. The Fairy knew what I needed to do after all."
        
        m "I stare at the blank page as fear runs down my spine, seeping through my veins like a paralytic. I grip the pen with white knuckles, my hand hovering over the paper but not moving to touch the page."
        
        m "What if I can’t do this?"
        
        m "In the midst of my panic, I feel a warm hand on mine, supporting the hand holding the pen."
        
        # TODO
      #Sprite: leslie

        show leslie sprite at center
        
        l "\"You told me you’re a writer. You love stories.\"" 
        
        m "\"I— I do,\" I stutter, a tear falling down my cheek and onto the blank page."
        
        # TODO
      #Sprite: noah

        show noah sprite at right
        
        n "\"Write our story, then. Give us the ending you want.\"" 
        
        m "I turn to look up at him. He is surprisingly calm, his green eyes clear and focused."
        
        m "\"Do you really think it’s that simple?\"" 
        
        n "\"I think it’s worth a try,\" he says softly, putting his hand on my shoulder. \" You showed us love while you’ve been here. You showed us care. You looked at us as people, not characters or a means to an end, and it brought us to this point.\"" 
        
        m "\"Destruction…\"" 
        
        n "\"Hope. You brought us hope.\"" 
        
        m "Noah puts his arm fully around my shoulders for a moment, providing some support for my shaking legs."
        
        n "\"Take all of that love, care, and hope,\" he says softly, \" and use it to write us a better ending.\"" 
        
        m "Tears stream freely down my face, an overflow of complex emotions that I don’t have the time to puzzle through at the moment. As they fall, the drops make spots on the blank pages."
        
        m "Though my hand shakes, I put my pen to paper."
        
        "As Lorenzo dies, the world begins to collapse, the magic fading away with his life."
        
        "However, a few brave heroes found the source of the magic hidden away in the library. All the books, all the memories, all the love and passion of generations past preserved in one room to pass on over and over again— all of it combined into a little pocket of true magic, untouched by Lorenzo, preserved by the story world itself."
        
        "There is magic in that kind of space. There is magic in memory, in recording stories, in using things we learn to shape our world for the better, and that magic persists in stories of all kinds. It is in books. It is in games. It is in songs."
        
        "As the castle shook, the books began to disappear. One by one, they vanish in a shower of sparks, and as each book vanishes, one person at a time returns to their world. They return to their lives and their loved ones, their memories restored from the very volumes that sent them home."
        
        "And, in the end, when all but this very book have disappeared, the librarian herself puts down her pen. The book in front of her disappears, and she goes back to the library to resume her own life."
        
        "THE END."
        
        m "I don’t quite understand what happens after I put the pen down."
        
        m "Everything seems to go blurry, then completely black, and for a moment I feel as if I am floating on an endless ocean of nothingness."
        
        m "And then someone pokes my shoulder."
        
        u "\"Ma’am? Are you okay?\"" 
        
        m "I groggily open my eyes, realizing there’s a hard surface under me."
        
        m "I am sitting in front of a computer at the university library. A string of random letters followed by a long stream of constant T’s cover the page of my open word processing document, and I touch my face only to realize that there is most certainly an imprint of square keys on my cheek."
        
        u "\"Ma’am??\"" 
        
        m "\"Oh! I’m, um. I’m good. Sorry.\" I sheepishly wave off the librarian, too shocked to blush and too disoriented to say much more."
        
        m "I’m only half aware as I pack my things, letting muscle memory take over while my mind is somewhere else entirely."
        
        m "I would say it was a dream, but the memories are vivid and detailed, fully present images rather than vague notions of memories and pieces that don’t quite fit together."
        
        m "What happened to everyone else? I can’t let the thought go as I pack my belongings, feeling numb and floaty and utterly disconnected from the world around me. I wonder if they were able to get out, to return to where they were. Or… maybe not. Maybe they were trapped."
        
        m "I sling my backpack over my shoulder and bite my lip. It’s also very possible that I am simply crazy, or I just fell asleep on an early morning and had a nightmare that shook me too the core. I decide to grab some tea at the library café on the way home, reorient myself, and hopefully feel less like I’ve lost my mind by the time I reach my apartment."
        
        m "I’m too lost in my thoughts to really pay attention to where I’m going, and as I turn down one of the rows of bookshelves, I collide head on with another figure."
        
        m "I backpedal in time to keep from falling, but my books spill out of my arms along with theirs, echoing with a deafening series of thunks in the otherwise silent library."
        
        m "\"I am so, so, sorr—\"" 
        
        m "I cut off as I look up at the face of the person I just barreled into."
        
        # TODO
      #Background: reunion CG
        
        # TODO
      #Music: noah theme
        play music noah_theme
        
        m "His long brown hair is so dark that it’s almost black. There is a naturally golden-blonde streak on one side, the light color peeking and out of a braid thrown over his shoulder. He wears half-moon glasses this time instead of a circlet and a normal vest instead of a brocade doublet, but the green eyes are the same."
        
        m "\"… Noah?\"" 
        
        n "\"… [player_name]?\"" 
        
        # TODO
      #Background: library
        scene bgp
        
        # TODO
      #sprite: modern noah
        show noah modern
        
        m "I can’t help it. I rush forward and hug him, probably too tightly to be socially acceptable."
        
        m "To be fair, he hugs me back just as tightly."
        
        n "\"Would you… would you like to have coff— tea! Would you like to have tea with me?\"" 
        
        m "\"Yeah. Yeah, I would,\" I manage to choke out, finally releasing him from the hug."
        
        m "We make our way down to the library’s café on the first floor and order drinks like nothing is out of the ordinary. I’m still in a daze, if I’m honest, but I don’t know how to shake myself out of it."
        
        m "It seems like Noah is just as affected as I am. We find a table and sip our teas in silence until it becomes clear that someone needs to say something."
        
        m "In the end, I am the first one to speak."
        
        m "\"How long has it been for you?\"" 
        
        n "\"About a year. You?\"" 
        
        m "\"Roughly…\" I pause and check the time on my phone. \" Twenty minutes. Max.\"" 
        
        n "\"Dear god,\" he says softly, taking off his glasses to rub his temples." 
        
        m "\"Weird question: how… old are you?\" I ask, squinting. \" Are you, like, a professor who got stuck on the haunted floor?\"" 
        
        m "Well, to be fair… I guess it’s no longer haunted now. That’s a weird realization. The missing people probably all just got sucked into the same program that I did."
        
        n "\"I’m thirty-two, and I’m a biologist, by the way,\" he says with a grin. \" Some things even fantasy can’t take away entirely.\"" 
        
        n "\"Not a professor, either. I haven’t quite finished my terminal degree.\" At this, the grin fades a little. \" And… if I’m honest, this whole experience hasn’t exactly helped with that. I was trapped for a year, so coming back feels like… stretching out a phantom limb.\"" 
        
        m "I nod slowly. It feels weird for me, too, and I was only gone for a few days. I can’t imagine how he feels, and it makes my heart break even more for Kylie. I wish I knew where she was so I could check on her, but… Lorenzo said she was one of the ‘early ones’ back in the castle hallway. I highly doubt she’d been sent back to modern times like Noah and I."
        
        n "\"Do you have any idea how insane I felt?\" he says softly, but then shakes his head. \" Of course you do. You’re living it.\"" 
        
        m "\"Well… yeah. That’s fair. I’m not going to tell you I feel completely sane in this moment, and not just because I’ve been in school for this long.\"" 
        
        m "That wrings a soft laugh out of Noah and he shakes his head, taking a long sip of his drink before he speaks again."
        
        n "\"Someone once told me that your identity has to amount to more than someone who does something, though. That just a part of you can’t define the whole. It’s helped with the adjustment a lot, just as I work back up to the way I was before all that.\"" 
        
        m "I smile, feeling my cheeks turn red, but I’m not sure how to respond."
        
        n "\"Do you ever wonder how many more there might have been in there? Just… trapped?\"" 
        
        m "The thought sends chills down my spine in the worst possible way. I don’t even want to imagine how many people Lorenzo took captive over the centuries he was hiding. It can’t have been just the ones I met, not if he was feeding on memories to stay alive for so long."
        
        m "\"Do you think they all… went back? Like we did?\"" 
        
        n "\"We can only hope. I’m no astrophysicist, but based on our experiences alone, it does seem like we were all returned to the time and place we were taken from.\"" 
        
        n "\"That… and I managed to find this.\" He passes his phone over to me, the image of a painting on the screen. \" It’s from the late nineteenth century, but I think we’re well aware of who it was that painted it.\"" 
        
        # TODO
        #Background: painted portrait on phone CG

        scene bgp
        
        m "I gasp as I look at the portrait of five people."
        
        m "The silhouettes are familiar, even without zooming into the image on the small phone screen. I don’t need to look closer. I already know who they are."
        
        m "\"It’s us.\"" 
        
        n "\"It’s us,\" he confirms. \" Leslie painted it. Took me a while to track down, but once I found it, there was no question at all. Her father was a major patron of the university library. All his books went here after his death.\"" 
        
        m "Which explains how the book… that became the game… that became my almost doom… ended up here in the first place."
        
        m "Something inside me settles just a little at that, at having some kind of answer to all this madness, even if it’s a small one among the scope of things."
        
        m "\"So we really did all go back to where we came from?\" I ask, shock coloring my tone as I stare at the picture."
        
        n "\"It appears so, yes. I haven’t been able to track down Tarran or Kylie yet, but I’m looking.\"" 
        
        m "\"I’ll help you,\" I say without hesitation."
        
        # TODO
      #Background: coffee shop
        scene bgp
        
        # TODO
      #sprite: modern noah
        show noah modern
        
        n "\"I would very much appreciate that,\" he says softly. \" It’s been… a long road to get here.\"" 
        
        m "I can understand that. It’s horrible enough coming out of a game you’ve been trapped in, but he was there for so much longer than I was, and then he had to go through a whole year wondering if he was making the whole thing up."
        
        m "\"You’re not alone any more. We’ll track them down,\" I say firmly, and I mean it. We’ll find them if it’s possible the find them, even if it takes years. Noah cracks a small smile and nods."
        
        m "\"So… what now?\" I ask, leaning back in my chair. Everything feels so surreal."
        
        n "\"That’s what I’ve been asking myself for the last year or so. I still haven’t figured it out.\"" 
        
        m "I huff and shake my head. Looks like I’m not alone in feeling the ennui seeping into my bones. But…"
        
        m "I think back to my time in the game. Sure, it was only a few days, but I remember the vibrancy of it all with a strange kind of fondness."
        
        m "Being outside with Tarran, running around on adventures with Noah and Kylie, hearing Leslie talk about painting with all her heart and soul… it was enough to make me feel alive in ways I haven’t really felt in years."
        
        m "Maybe that’s what I really need to be doing. Trying to feel alive."
        
        m "\"Did you ever talk to that fairy character?\" I ask. \" Before you lost your memories, I mean.\"" 
        
        n "\"The system interface avatar, yes. I remember she helped me when I first arrived, too.\"" 
        
        m "\"She was… kinda weird,\" I say fondly."
        
        n "\"That she was,\" he says with a chuckle."
        
        m "\"I think she made some good points about things, though.\"" 
        
        m "\"I was so focused on winning the game that I almost didn’t make it out, and it was her that made me really stop and think about what I was doing and why I was doing it.\"" 
        
        m "\"She said that it wasn’t about winning. If it had been about winning, then there should have been a reward or punishment every time I did something right.\"" 
        
        m "Noah nods patiently as I speak, looking on thoughtfully."
        
        m "\"The ending is its own reward. That’s what she was talking about the whole time… and not just the ending or knowing that you did things right, but the joy of playing along the way.\"" 
        
        m "\"We got to build a story together, Noah,\" I say with a smile. \" I think that’s its own reward.\"" 
        
        n "\"That we did… and with some wonderful friends, too.\"" 
        
        m "He stays silent for a long moment before he finally grins."
        
        n "\"On the chance you’d like to start another story, I can think of a great local place to have dinner on Saturday?\"" 
        
        m "I smile, a slight blush creeping into my cheeks."
        
        m "\"Are you… asking me out?\"" 
        
        m "He just shrugs, a small smile playing across his face."
        
        n "\"We’re building a story. We can see how it goes.\"" 
        
        m "Somehow, I think that’s exactly the answer I would have wanted."
        

        label the_end:
            "THE END."