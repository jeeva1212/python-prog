class monkey:
    def patch(self):
        print("patch() is being called")

def monk_p(self):
    print("monk_p() is being called")
# Replacing address of "patch" with "monk_p"
monkey.patch = monk_p

obj = monkey()
obj. patch()
# monk_p() is being called
