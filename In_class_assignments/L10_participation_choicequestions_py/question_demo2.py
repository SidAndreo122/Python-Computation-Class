##
#  a simple quiz with two choice questions.
#

#from questions import ChoiceQuestion
from questions import *

def main() :
   first = Question()
   first.setText("Who was the inventor of Python? ")
   first.setAnswer("Guido van Rossum")
   

   second = ChoiceQuestion()
   second.setText("In which country was the inventor of Python born?")
   second.addChoice("Australia", False)
   second.addChoice("Canada", False)
   second.addChoice("Netherlands", True)
   second.addChoice("United States", False)

   presentQuestion(first)
   presentQuestion(second)

## Presents a question to the user and checks the response.
#  @param q the question
#
def presentQuestion(q) :
   print(q)
   response = input("Your answer: ")
   print(q.checkAnswer(response))

# Start the program.
main()
