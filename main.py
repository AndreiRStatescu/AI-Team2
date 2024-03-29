from dotenv import load_dotenv, find_dotenv

from alao_ai_utils import answer_with_ai_1
from andrei_ai_utils import answer_with_ai_2, validate_with_ai_1

load_dotenv(find_dotenv(), override=True)


def print_array(array):
    print("\n\n" + ("=" * 20))
    for elem in array:
        print(elem + "\n" + ("=" * 10))

if __name__ == "__main__":
    print("Starting CV analysis...\n\n" + ("=" * 20) + "\n\n")

    input_resume = "files/Andrei_Statescu_Senior_Software_Engineer_Feb_2024.pdf"

    # questions = [
    #     "Based on the provided document, illustrate the leadership experience of the candidate"
    # ]

    questions = [
        "Based on the provided document, showcase Andrei's hobbies?",
        "Based on the provided document, showcase Andrei's experience with Web3JS?",
        "Based on the provided document, showcase the candidate' best 5 skills?",
    ]

    # answers = answer_with_ai_1(input_resume, questions)
    answers = answer_with_ai_2(input_resume, questions)
    print_array(answers)

    # answers = [
    #     "swimming, volleyball",
    #     "During his time at Google, between 2018 and 2021, Andrei has been a principal engineer, leading a team of 5",
    #     "Leadership, Web3JS, NodeJS, ReactJS, Management",
    # ]

    validation_results = validate_with_ai_1(input_resume, questions, answers)
    print_array(validation_results)


    print("\n\n" + ("=" * 20) + "\n\nCompleted CV analysis!")
