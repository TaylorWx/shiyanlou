import re
f=open('ch11.txt','w')
def repl(match_obj):
    print(len(match_obj.group()),match_obj.groups()[0],end='*',file=f)
    return '%s%s' % (len(match_obj.group()), match_obj.groups()[0])

if __name__ == '__main__':
    a = '1'
    reg = re.compile(r'(\d)\1*')
    for i in range(10):
        a = reg.sub(repl, a)
        print('---------',file=f)
    print('a[30] = %s\n' % a,file=f)
    print('len(a[30]) = %d' % len(a),file=f)
f.close()

