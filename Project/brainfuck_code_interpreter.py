import subprocess
class BrainFuck:
    def __init__(self):
        self.ptr = 0  # Data pointer
        self.length = 65535  # Max memory limit
        self.memory = [0] * self.length  # Memory array
        
    def run_shell_command(self, command):
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()

    # Interpreter function which accepts the code as a string parameter
    def interpret(self, s):
        output = ""
        # Parsing through each character of the code
        i = 0
        while i < len(s):
            # BrainFuck is a tiny language with only eight instructions.
            # In this loop, we check and execute all those eight instructions.

            # > moves the pointer to the right
            if s[i] == '>':
                if self.ptr == self.length - 1:  # If memory is full, pointer is returned to zero
                    self.ptr = 0
                else:
                    self.ptr += 1

            # < moves the pointer to the left
            elif s[i] == '<':
                if self.ptr == 0:  # If the pointer reaches zero, pointer is returned to rightmost memory position
                    self.ptr = self.length - 1
                else:
                    self.ptr -= 1

            # + increments the value of the memory cell under the pointer
            elif s[i] == '+':
                self.memory[self.ptr] += 1

            # - decrements the value of the memory cell under the pointer
            elif s[i] == '-':
                self.memory[self.ptr] -= 1

            # . outputs the character signified by the cell at the pointer
            elif s[i] == '.':
                output += chr(self.memory[self.ptr])

            # , inputs a character and store it in the cell at the pointer
            elif s[i] == ',':
                self.memory[self.ptr] = ord(input()[0])

            # [ jumps past the matching ] if the cell under the pointer is 0
            elif s[i] == '[':
                if self.memory[self.ptr] == 0:
                    c = 1
                    while c > 0 or s[i] != ']':
                        i += 1
                        if s[i] == '[':
                            c += 1
                        elif s[i] == ']':
                            c -= 1

            # ] jumps back to the matching [ if the cell under the pointer is nonzero
            elif s[i] == ']':
                if self.memory[self.ptr] != 0:
                    c = 1
                    while c > 0 or s[i] != '[':
                        i -= 1
                        if s[i] == ']':
                            c += 1
                        elif s[i] == '[':
                            c -= 1

            i += 1

        return output

# Helper function to read the content of a file and return it as a string
def read_file_content(filename):
    with open(filename, 'r') as file:
        return file.read()

# Driver code
if __name__ == "__main__":
    filename = "Brainfuck_code"
    bf = BrainFuck()
    code = read_file_content(filename)

    print("Brainfuck code:")
    print(code)

    print("\nOutput:")
    output = bf.interpret(code)
    print(output)

