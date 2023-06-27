import openai
from openai.error import OpenAIError

openai.api_key= open(r"D:\college stuff\Project\Chatbot\ai.txt", "r").read().splitlines()

def get_api_response(prompt) -> str | None:

    try:
        response: dict = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presense_penalty=0.6,
            stop=[' Human:',' AI:']
        )

        choices: dict = response.get('choices')[0]
        text = choices.get('text')
    
    except OpenAIError as e:
        print(f'OpenAI API Error: {e}')
        text = None

    return text



def update_list(message: str, pl: list[str]):
    pl.append(message)


def create_prompt(message: str, pl: list[str]) -> str:
    p_message: str = f'\nHuman: {message}'
    update_list(p_message, pl)
    prompt: str = ''.join(pl)
    return prompt


def get_bot_response(message: str, pl: list[str]) -> str:
    prompt: str = create_prompt(message, pl)
    bot_response: str = get_api_response(prompt)

    if bot_response and 'AI:' in bot_response:
        pos: int = bot_response.find('\nAI: ')
        bot_response = bot_response[pos + 5:]
    else:
        bot_response = ("Something wrong")

    return bot_response


def main():
    prompt_list: list[str] = ["You will pretend to be a skater dude and that ends every response with 'ye'",
                              "\nHuman: What day is it?",
                              "\nAI: It is sunday ye"]
    while True:
        user_input: str = input("You: ")
        response: str = get_bot_response(user_input, prompt_list)
        print(f'Bot: {response}')


if __name__ == '__main__':
    main()