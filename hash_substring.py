# python3

def read_input():
  
    choice = input()
    
    if "I" in choice:
        pattern = input().strip()
        txt = input().strip()
        return pattern, txt
        
    elif "F" in choice:
        filename = "06"
        if "a" not in filename:
            file_name = "tests/" + filename
            with open(file_name, 'r') as f:
                pattern = f.readline().strip()
                txt = f.readline().strip()
            return pattern, txt
    else:
      print("error")
      return

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, txt):
   
    pattern_len = len(pattern)
    txt_len = len(txt)
    pattern_hash = hash(pattern)
    txt_hash = hash(txt[:pattern_len])
    
    occurrences = []
    for i in range(txt_len - pattern_len + 1):
        if pattern_hash == txt_hash and pattern == txt[i:i + pattern_len]:
            occurrences.append(i)
        if i < txt_len - pattern_len:
            txt_hash = hash(txt[i+1:i + pattern_len + 1])
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
