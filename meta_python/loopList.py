sentences = [
    "The sun rises in the east.",
    "Cats love to nap in the sun.",
    "Pizza is my favorite food.",
    "Birds sing in the morning.",
    "Rainbows are beautiful after rain.",
    "Books open new worlds.",
    "Coffee wakes me up.",
    "Stars twinkle in the night sky.",
    "Flowers bloom in spring.",
    "Time flies when you're having fun.",
    "Laughter is contagious.",
    "Music soothes the soul.",
    "Dogs wag their tails when happy.",
    "Smiles can brighten someone's day.",
    "The moon glows at night.",
    "Dreams inspire creativity.",
    "Ice cream melts quickly in the sun.",
    "Hugs convey warmth and comfort.",
    "Kindness costs nothing.",
    "The ocean waves are calming.",
    "Sunsets are magical moments.",
    "Learning is a lifelong journey.",
    "Balloons float in the air.",
    "Butterflies symbolize transformation.",
    "Snowflakes are unique.",
    "Clouds form interesting shapes.",
    "Exercise energizes the body.",
    "The wind whispers through the trees.",
    "Friends make life richer.",
    "Every day is a new opportunity."
]

################

a="The sun rises in the east."
b="Cats love to nap in the sun."
c="Pizza is my favorite food."
d="Birds sing in the morning."
e="Rainbows are beautiful after rain."
f="Books open new worlds."
g="Coffee wakes me up."
h="Stars twinkle in the night sky."
i="Flowers bloom in spring."
j="Time flies when you're having fun."
k="Laughter is contagious."
l="Music soothes the soul."
m="Dogs wag their tails when happy."
n="Smiles can brighten someone's day."
o="The moon glows at night."
p="Dreams inspire creativity."
q="Ice cream melts quickly in the sun."
r="Hugs convey warmth and comfort."
s="Kindness costs nothing."
t="The ocean waves are calming."
u="Sunsets are magical moments."
v="Learning is a lifelong journey."
w="Balloons float in the air."
x="Butterflies symbolize transformation."
y="Snowflakes are unique."
z="#######################"

sents = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

for al in range(len(sents)): print(sents[al])

# Print each sentence
for sentence in sentences:
    print(sentence)

######################
# Short cut way for looping the list 

[print(sent) for sent in sentences]
