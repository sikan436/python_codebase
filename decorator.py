

def greet(fx):
    def mfx(*args,**kwargs):
        print ('inside decorator')
        fx(*args,**kwargs)
        print ('outside decorator')
    return mfx

@greet
def gudnit():
    print('gud nyth')

@greet
def add(a,b):
    print (a+b)

gudnit()
add(3,4)
    