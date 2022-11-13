# from transformers import pipeline
# generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
# prompt = """"""
# res = generator(prompt, max_length=2000, do_sample=True, temperature=0.9)
# print(res[0]['generated_text'])

# import os
# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

# with open('Python Projects/CSE 110/08_prove_assignment_wordlist.txt') as f:
#     words = f.readlines()
#     for word in words:
#         if len(word) == 7:
#             print(f"\"{word.strip()}\", ", end="")
