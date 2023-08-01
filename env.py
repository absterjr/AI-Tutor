print("Hey, lets run this")
apiKey = input("Type your OpenAI API_KEY (You can get it from your account settings): ")
with open("apikey.txt", "w") as file:
    file.write(apiKey)
