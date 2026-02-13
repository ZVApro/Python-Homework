class StringUtils:


    def capitalize(self, string: str) -> str:
        if isinstance(string, str):
            return string.capitalize()
        raise TypeError("Input must be a string.")


    def trim(self, string: str) -> str:
        if isinstance(string, str):
            return string.strip()
        raise TypeError("Input must be a string.")

    def contains(self, string: str, symbol: str) -> bool:
        if isinstance(string, str) and isinstance(symbol,str):
            return symbol in string
        raise TypeError ("Both inputs must be strings.")


    def delete_symbol(self, string: str, symbol: str) -> str:
        if isinstance(string, str) and isinstance(symbol,str):
             return string.replace(symbol, "")
        raise TypeError ("Both inputs must be strings.")


