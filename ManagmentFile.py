class ManagementFiles:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Get the resource'.center(50, '-'))
        self.name = open(self.name, 'r', encoding='utf-8')
        return self.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Close the resource'.center(50, '-'))
        if self.name:
            self.name.close()
