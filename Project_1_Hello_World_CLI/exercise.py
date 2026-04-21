prompts = {
    'en': { 'name': 'What is your name?', 'color': "What's your favorite color?", 'job': "What's your Job?", 'dream': "What's your Dream?"},
    'fr': { 'name': 'Quel est votre nom?', 'color': "Quelle est votre couleur préférée ?", 'job': "Quel est votre métier?", 'dream': "Quel est votre rêve ?" },
    'rw': { 'name': 'Izina ryacu ni irihe?', 'color': "Ni irihe bara ukunda?", 'job': "Akazi kawe ni akahe?", 'dream': "Inzozi zawe ni izihe?" }
}
lang = input("Choose a language:(en, fr, rw) \n").lower()
if lang not in prompts:
    print("Invalid Input")
else:
    name = input(prompts[lang]['name']) 
    color = input(prompts[lang]['color']) 
    job = input(prompts[lang]['job']) 
    dream = input(prompts[lang]['dream']) 
    print("------ Summary ------")#prints the content in the ""
    print(f"Name: {name}\nColor: {color}\nJob: {job}\nDream: {dream}")#does the same thing as line 2, except \n is a line breaker