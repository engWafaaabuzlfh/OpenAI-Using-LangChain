from prompt import SYSTEM_INSTRUCTIONS
from initialize import prompt_template, llm_chain




def main():
    user_input = input("What do you want to generate a prompt for? ")
    prompt = prompt_template(SYSTEM_INSTRUCTIONS)
    chain = llm_chain(prompt=prompt)
    response = chain.run(user_input)
    print(response)


if __name__ == "__main__":
    main()