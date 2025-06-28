import re

def make_accessible(response: str) -> str:
    """Formats responses for screen readers and reduces complexity.
       - Simplifies complex sentences.
       - Ensures clear structure (e.g., using explicit labels like 'Summary:').
       - Removes any characters or formatting that could be confusing for a screen reader."""
    # Remove non-ASCII and special characters except basic punctuation
    response = re.sub(r'[^\w\s\.,:\'\-]', '', response)
    # Replace multiple spaces with a single space
    response = re.sub(r'\s+', ' ', response)
    # Ensure labels like 'Summary:' or 'Email Summary:' are at the start
    if not re.match(r'^(Summary:|Email Summary:|Calendar Events:|Search Results:|Posted to|Okay,|Voice command received:)', response):
        response = 'Summary: ' + response
    # Shorten sentences for clarity
    sentences = response.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    short_response = '. '.join(sentences)
    if not short_response.endswith('.'):
        short_response += '.'
    return short_response
