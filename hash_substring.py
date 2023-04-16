# python3

def read_input():
  
    choice = input()
    
    if "I" in choice:
        pattern = input().strip()
        txt = input().strip()
        return pattern, txt
        
    elif "F" in choice:
        filename = "06"
        if "a" in filename:
            print("File names with letter a are not allowed")
            return
        try:
            with open('tests/' + filename, 'r') as file:
                pattern = f.readline().strip()
                txt = f.readline().strip()
                
        except FileNotFoundError:
            print("Error")
            return


def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, txt):
    occurrences = []
    find_len = len(pattern)
    txt_len = len(txt)
    find_hesh = hash(pattern)
    txt_hesh = hash(txt[:find_len])
    
    for i in range(len(txt) - len(pattern) + 1):
        if pattern_hash == txt_hash:
            if pattern == txt[i:i+len(pattern)]:
                occurrences.append(i)
        if i < len(txt) - len(pattern):
            txt_hash = txt_hash - ord(txt[i]) + ord(txt[i+len(pattern)])
            txt_hash %= 101
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
