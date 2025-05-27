class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = Code(root_name)

    def add_field(self, type, name):
        self.__root.elements.append([type, name])
        return self

    def __str__(self):
        return str(self.__root)

class Code:
    indent_size = 2

    def __init__(self, name):
        self.name = name
        self.elements = []

    def _str(self, indent):
        indent1 = ' ' * self.indent_size * (indent + 1)
        indent2 = ' ' * self.indent_size * (indent + 2)

        lines = [f"class {self.name}:"]
        
        if not self.elements:
            lines.append(f"{indent1}pass")
        else:
            lines.append(f"{indent1}def __init__(self):")
            for type_, name in self.elements:
                lines.append(f"{indent2}self.{type_} = {name}")
        
        return "\n".join(lines)

    def __str__(self):
        return self._str(0)


cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
print(cb)
