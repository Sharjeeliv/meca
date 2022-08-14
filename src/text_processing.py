import nltk
import nltk.corpus

# nltk.download('averaged_perceptron_tagger')
TERM, TAG = 0, 1


def is_noun(tag: str) -> bool:
    return tag in {'NNP', 'NNPS'}


def end_in_period_or_colon(term: str) -> bool:
    return term[-1] in {'.', ':'}


# WIP NLP - For deconstruction and formatting of title
def format_title_to_apa(title: str) -> str:
    # This function formats the title into APA format: Described as
    # Proper nouns capitalized, first word, and first word after a colon or period.

    tokens = nltk.pos_tag(title.lower().strip().split(" "))
    out = []

    capitalize_next = False
    for token in tokens:
        term = token[TERM].capitalize() if is_noun(token[TAG]) or capitalize_next else token[TERM]
        capitalize_next = end_in_period_or_colon(term)
        out.append(term)

    out[0] = out[0].capitalize()
    return ' '.join(out)


if __name__ == '__main__':
    print(format_title_to_apa('Team Meeting Attitudes: Conceptualization and Investigation of a New Construct'))
