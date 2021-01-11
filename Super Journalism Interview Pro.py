import random, time

def introduction():
    print('SUPER JOURNALISM INTERVIEW PRO')
    print()
    print()
    print ('''Congratulations. You have earned your spot as a mobile news anchor for P3TV.
Use your expert journalist skills to interview people live on tv and get to the truth!

Press any key to continue.''')
    input()
    print()
    time.sleep(1)
    print ('''Remember the facts that the news-station provides you with and be ready to confront
interviewees when their story strays from the truth. You have 5 seconds to read each paragraph
the interviewee gives you and decide whether to confront them.

Press any key to continue.''')
    input()
    time.sleep(1)
    print ('''When you think your interviewee is fibbing type "liar" or "bullshit" and hit enter
to send them packing! But don't get too hasty, call bullshit too often and its game over!

Press any key to begin and start your high-flying journalism career!''')
    input()
           

def mission_briefing (mission_title, mission_blurb):
    
    print (mission_title)
    time.sleep(2)
    print ()
    print (mission_blurb)


cat_title = ('''9 Lives and Counting''')
cat_blurb = (''' Time - 9:37am. 56 Everclear Avenue.
Okay.. first call of the day. Looks like some lady's cat got stuck in a tree. A passing neighbour
let her know after calling 911 for her and the local fire-department rescured it. EMT's were there as a matter of protocal but
actually ended up helping hold the ladder for the fire-fighters. Her flower patch was trampled by some blundering police offcer
but he offered to pay for a landscaper to fix it... Heart-warming stuff... Let's go folks...''')

cat_lie1 = ['My neighbour deliberatly threw my cat into the tree, that is when I heard the yelling' , 'The postman has a habit of scaring cats and chasing them up trees,', 'The police called me to say my cat was stuck up a tree, so I went to check.', 'The postman told me that my cat was stuck up a tree.'] 
cat_lie2 = ['I had to run back inside and call 911 because no one had a phone on them.', 'I immiediatly called 911 with my mobile phone.', 'We were lucky that a fire-truck was passing by and I could flag it down.', 'I was lucky that my husband was a cop and had a CB radio to call the others']
cat_lie3 = ['The paramedics refused to help with my cat.', 'The police stole my prize lillies and spat at me, which was confusing.', 'The firemen threw rocks at my poor cat to get him down, the monsters!', 'The paramedics trampled my prize lillies, the oafs!']

cat_fluff_start = ['I had just woken up when I saw all this', 'I had barely finished my coffee', 'I mean I could not believe it', 'It was just chaos'] 
cat_fluff_end = [' and had no idea what to do.', '. That is when I dialled 911.', '. What could I do?', ' but I already knew I had to get help.']


cat_truth1 = ['I heard meowing and thought I better go check on Mr Mittens.', 'Mr Mittens was calling for help, the poor soul.', 'Mr Mittens is so clumsy, he just cannot help himself!', 'I saw from my window that Mr Mittens was calling for help'] 
cat_truth2 = ['I tried to tempt him down from the tree with treats but he refused to come down.', 'He looked so scared up in the tree and I was too short to reach him', 'My husband was so shocked he had to sit down on account of his heart when he saw Mittens so stuck!', 'My little bundle of joy was so frightened, he never normally climbs that high!']
cat_truth3 = ['Thank God the firefighters got here so swiftly and rescued my precious kitty.', 'I am glad 911 got to us so quickly and helped rescue Mittens with their ladder.', 'In the end it took both the paramedics and the firefighters to rescue Mr Mittens.', 'Mr Mittens was rescued by a burly fire-fighter who had to climb all the way up to get him down!']
cat_truth_list = [cat_truth1, cat_truth2, cat_truth3]




def truth_deployer (truth_list):
    print (truth_list[random.randint(0,3)])



#Generates fluff for the Cat Story
#fluff_generator (cat_fluff_start[random.randint (0,3)], cat_fluff_end[random.randint(0,3)])
  

