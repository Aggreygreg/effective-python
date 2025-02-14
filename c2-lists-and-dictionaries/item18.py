# Item 18: Know How to Construct Key-Dependent Default Values with __missing__

class Pictures(dict):
    def __missing__(self, key):
        value = self.open_picture(key)
        self[key] = value
        return value

    @staticmethod
    def open_picture(profile_path):
        try:
            return open(profile_path, 'a+b')
        except OSError:
            print(f'Failed to open path {profile_path}')
            raise

# Usage example
path = 'profile_1234.png'
pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
