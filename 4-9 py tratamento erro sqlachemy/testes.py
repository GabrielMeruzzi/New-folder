def find_vs_index(s, char):
    try:
        pos = s.index(char)
        print(f"Character '{char}' found at position {pos}")
    except ValueError:
        print(f"Character '{char}' not found using index()")
    
    pos_find = s.find(char)
    if pos_find == -1:
        print(f"Character '{char}' not found using find()")
    else:
        print(f"Character '{char}' found at position {pos_find}")

find_vs_index("hello", ":")