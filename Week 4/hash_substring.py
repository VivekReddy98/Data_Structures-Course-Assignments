# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    return print(' '.join(map(str, output)))

def get_occurrences(list_pattern, list_text):
    m = len(list_pattern)
    list_occurences = []
    hash_pattern = hashvalue(list_pattern,prev=0,left=0,right=0,m=m)
    hash_text = hashvalue(list_text[0:len(list_pattern)],prev=0,left=0,right=0,m=m)
    if hash_pattern == hash_text:
        list_occurences.append(0)
    for i in range(1,len(list_text)-len(list_pattern)+1):
        hash_text = hashvalue(data=0,prev=hash_text,left=list_text[i-1],right=list_text[i+m-1],m=m)
        if hash_text==hash_pattern:
           list_occurences.append(i)
    return list_occurences

def hashvalue(data,prev,left,right,m):
    #print(left,right)
    q = 1000000007
    r = 23
    if data!=0:
        dummy = 0
        for i in range(m):
            dummy = (dummy%q+ord(data[i])*pow(r,m-i-1,q))%q
            dummy = dummy%q
        #print(dummy)
        return dummy
    else:
        neg = ((ord(left)%q)*pow(r,m-1,q))%q
        prev = (prev%q - neg + q)%q
        prev = (prev*r)%q
        prev = (prev%q+ord(right))%q
        #print(prev)
        return prev


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

