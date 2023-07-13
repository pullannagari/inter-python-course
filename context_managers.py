# great tool for resource management

with open('notes.txt', 'w') as file:
    file.write('some todo....')

# the context manager will close the file even in case of exception
# its a recommended way of opening a file or access any other resources
# other examples are db connections, lock (for lock.acquire and lock.release), etc

# context managers for custom classes
class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    # need to implement enter and exit methods for custom context managers
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exec_type, exec_value, exec_traceback):
        if self.file:
            self.file.close()
        print('exec: ', exec_type, exec_value)
        print('exit')

with ManagedFile('notes.txt') as file:
    print('do some stuff...')
    file.write('some todo...')

print('continuing...')

# context managers as function
from contextlib import contextmanager

@contextmanager
def open_managed_file(file_name):
    f = open(file_name, 'w')
    try:
        yield f # temporarily suspends its own execution, and once the with exists this will be resumed
    finally:
        f.close() # acts as a block for handling exceptions

with open_managed_file('notes.txt') as f:
    f.write('some todo at the end')