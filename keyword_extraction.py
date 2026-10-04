from rake_nltk import Rake

print("=" * 60)
print("             KEYWORD EXTRACTION SYSTEM")
print("=" * 60)

text = input("\nEnter a paragraph:\n")

rake = Rake()
rake.extract_keywords_from_text(text)

keywords = rake.get_ranked_phrases()

print("\n--- IMPORTANT KEYWORDS ---")

if keywords:
    for i, keyword in enumerate(keywords[:10], start=1):
        print(f"{i}. {keyword}")
else:
    print("No keywords found.")