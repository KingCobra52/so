import threading
from collections import Counter
import time

# Constants
N = 10  # Top N most common words
T = 4   # Number of threads

# Function to count words in a text segment
def count_words_segment(segment, local_counter):
    words = segment.split()
    local_counter.update(words)

def split_text(text, parts):
    size = len(text)
    segment_len = size // parts
    return [text[i*segment_len:(i+1)*segment_len] for i in range(parts - 1)] + [text[(parts-1)*segment_len:]]

def main():
    start = time.time()

    # Reading the file
    with open("texto.txt", "r", encoding="utf-8") as f:
        text = f.read().lower()

    segments = split_text(text, T)

    threads = []
    accountants = [Counter() for _ in range(T)]

    # Create and start the threads
    for i in range(T):
        thread = threading.Thread(target=count_words_segment, args=(segments[i], accountants[i]))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish.
    for thread in threads:
        thread.join()

    # Combine the results
    total_counter = Counter()
    for c in accountants:
        total_counter.update(c)

    # Print the N most common words
    print(f"\nTop {N} most frequent words:")
    for word, freq in total_counter.most_common(N):
        print(f"{word}: {freq}")

    end = time.time()
    Duracao = end - start
    print(f"\nProgram duration: {Duracao:.2f} seconds")

if __name__ == "__main__":
    main()
