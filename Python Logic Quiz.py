#setup
print("Welcome to the python Logic Quiz!")
quizNum = int(input("Please enter the number of questions to be answered: "))
curQuestion = 0
run = 'y'
ans = 0
correctQ = 0
import random

#setup the lists of Questions
terms = ["abstraction", "comprehension", "Concept", "Deductive Inference", "Essence", "extension", "judgment", "logic", "formal logic", 
"material logic", "note", "porphyrian tree", "proposition", "sense perception", "signification", "simple apprehension", "soundness", 
"substance", "supposition", "syllogism", "term", "validity"]

defs = ["The process of deriving a simple apprehension from a sense perception and mental image",
"What an object is according to its notes (substance, material, living, sentience, and rationality); one of the properties of simple apprehension",
"An abstract idea or mental picture",
"When the mind makes a connection between the terms and the syllogism, showing the conclusions to derive from the premises",
"The permanent nature of something that makes it what it is",
"What a concept refers to; One of the properties of simple apprehension",
"Second mental act of logic; Occurs when you affirm or deny something",
"The science of right thinking",
"Focus is on the structure of argumentation (argument is constructed the right way)",
"Focus is on the content of the argumentation (whether or not the argument is true)",
"a simple concept used to define a more complex concept (e.g., sentience)",
"a diagram designed to help you classify and divide all of reality ,in order to show similarities and differences among physical objects",
"The verbal expression of judgment; Also called a statement (e.g., all cups are red). _______s are very important because they are the only verbal expressions that are either true or false.",
"The ability to see, hear, or become aware of something through the senses", 
"The sense of a term and what meaning it conveys (univocal, equivocal, analogous)",
"the first mental act of logic (an act) and the concept itself",
"when a syllogism is valid and it has all true premises",
"a  ______  is something rather than nothing, if anything exists it is a  ______",
"The kind of existence a term refers to (verbal, mental, or real)",
"an argument in which a conclusion is drawn from two premises, which both share a common term that does not occur in the conclusion. _______s are either valid or invalid",
"The verbal expression of simple apprehension (e.g., ‘man’ or ‘plant’). _____s Are either clear or unclear in their meaning(s)",
"when the premises of an argument actually support the conclusion, and are all arranged in the correct way. One or more of the premises may be false. _______ Is all about structure"]

#main loop
while run == 'y':
    while curQuestion < quizNum:
        randomQuestionNum = random.randint(0,len(defs) - 1)
        print('"' + defs[randomQuestionNum] + '"' + " is the defintion for what? - Case doesn't matter -")
        ans = input('')
        ans = ans.upper()
        termAns = terms[randomQuestionNum]
        termAns = termAns.upper()
        if ans == "WORD BANK":
            print(terms)
            print("-")
            print('"' + defs[randomQuestionNum] + '"' + " is the defintion for what? - Case doesn't matter -")
            ans = input('')
        if ans == termAns:
            correctQ +=1
            curQuestion +=1
            print("-")
            print("-")
            print("Correct! Your Correct Percentage is Now " + str((float(correctQ)/float(curQuestion) * 100.0)//1) + "%!" )
            print("-")
            print("-")
            
        else:
            curQuestion +=1
            print("-")
            print("-")
            print("I was looking for " + str(termAns))
            print("-")
            print("-")

    run = "n"

print("Thanks for playing!!")
        