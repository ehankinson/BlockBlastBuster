class BitBoard:
    


    def __init__ (self, value: int):
        self.value = value



    def set (self, pos: int):
        self.value = self.value | (1 << pos)
    


    def clear (self, pos: int):
        self.value = self.value & ~(1 << pos)



    def toggle (self, pos: int):
        self.value = self.value ^ (1 << pos)

    

    def is_bit_set (self, pos: int) -> bool:
        return self.value & (1 << pos) != 0 
    


    def place_piece(self, other_board) -> bool:
        return self.value & other_board.value != 0


    def __repr__ (self) -> str:
        string_board = format(self.value, '064b')
        boarder = "+---+---+---+---+---+---+---+---+\n"
        rows = [boarder]

        for row in range(8):
            row_str = ''.join(f"| {string_board[row * 8 + col]} " for col in range(8))
            rows.append(f"{row_str}| {8 - row}\n")
            rows.append(boarder)
        board_rep = ''.join(rows)

        return f"{board_rep}\n{self.value}"
    


if __name__ == "__main__": 
    b = 2**32 - 1

    bitboard = BitBoard(18446744078004518911)
    
    print(bitboard)