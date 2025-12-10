from pathlib import Path

def read_file(filename):
    # Construct the file path relative to this script
    file_path = Path(__file__).parent / filename
    
    try:
        with open(file_path,"r") as f:
            content = f.read()
        
        print("\n🌟FILE ANALYZER🌟\n")
    
        lines = content.splitlines()
        total_lines = len(lines)
        non_empty_lines = len([line for line in lines if line.strip()])
        
        print(f"\nTotal lines: {total_lines}")
        print(f"Non-empty lines: {non_empty_lines}")
        
        # Count words by splitting the content to make it a list of words
        words = content.split()
        print(f"Total words: {len(words)}")
        
        # Count word frequencies by creating a dictionary
        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
                   
        if frequency:
            max_count = max(frequency.values())
            most_frequent = {word for word, count in frequency.items() if count == max_count}
            print(f"Most frequent word(s): {most_frequent} with {max_count} occurrence(s)")
        
    except FileNotFoundError:
        print(f"Error: '{filename}' not found")

read_file('words.txt')
