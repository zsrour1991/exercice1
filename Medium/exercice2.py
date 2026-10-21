def count_words(text):
    split_text = text.split()
    result={x:split_text.count(x) for x in split_text}
    return result

input_text=input("Enter a text: ") 
counts = count_words(input_text)
print(counts)