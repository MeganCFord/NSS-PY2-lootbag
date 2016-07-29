
class Lootbag:
    def __init__(self):
        print("hello world!")

    def list_children(self):
        '''
        list all children in lootbag that have toys attached to them/are undelivered.
        '''
        pass

    def list_toys(self):
        '''
        list all toys in lootbag that are assigned to a certain child's name.
        '''
        pass

    def deliver_to_child(self):
        '''
        set 'delivered' on child to true. will likely empty the 'to give toys' and put them in the 'given' toys list.
        '''
        pass

    def add_toy(self):
        '''
        add a new toy to a child's 'to give toys' list.
        '''
        pass

    def remove_toy(self):
        '''
        remove a toy from a child's 'to give toys' list.
        '''

    def remove_all_toys(self):
        '''
        remove all toys from a child's 'to give toys' list.
        '''


if __name__ == '__main__':
    app = Lootbag()
