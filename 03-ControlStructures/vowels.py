###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0

# Count vowels in the text
text_indx = 0
while text_indx<len(text):
    if text[text_indx] in vowels:
        vowel_count += 1
    text_indx+=1
print(f"The number of vowels in the text is: {vowel_count}")