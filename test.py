@call_only_once  
def func():
    print ('Calling func only this time'  )


def call_only_once(func):
    def new_func(*args, **kwargs):  
        if not new_func._called:  
            try:  
                return func(*args, **kwargs)  
            finally:  
                new_func._called = True  
    new_func._called = False  
    return new_func  