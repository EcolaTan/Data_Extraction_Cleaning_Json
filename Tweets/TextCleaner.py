import json

tweets_file = 'Tweets./Text.json'
output_path = 'Tweets./wordcount.csv'

words_dict = {}
remove_chars = "&$@[].,\'#()-\\\"!?’_"

with open(tweets_file, "r") as json_file:
    tweets = json.loads(json_file.read())

tweet_texts = [i["full_text"] for i in tweets]
#print(len(tweet_texts))
#print(tweet_texts)

tweet_texts = set(tweet_texts)
#print(tweet_texts)

for i in tweet_texts:
    i = i.split()
    for x in i:
        for y in remove_chars: x = x.replace(y,"")
        x = x.upper()
        if x:
            if words_dict.get(x,0) == 0: words_dict[x] = 1
            else: words_dict[x] += 1
#print(tweet_texts)

words_lists = [(k, v) for k, v in words_dict.items()] 
#print(words_lists)

words_lists = sorted(words_lists, key=lambda x: x[1],reverse=True)
#print(words_lists)

for i in range(5):
    print(i+1 , end = " ")
    print(words_lists[i])

with open(output_path, 'w',encoding="utf-8") as f:
    f.write("word,count\n")
    for i in range(len(words_lists)):
        f.write(str(words_lists[i][0]) +","+ str(words_lists[i][1]))
        f.write("\n")
