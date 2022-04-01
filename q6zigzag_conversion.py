def convert(s, numRows):
    if numRows == 1:
        return s
    else:
        ptr = 0
        n = len(s)
        space = numRows * 2 - 2
        res = ""
        n_row = numRows
        while (n_row > 0):
            res_inner = ""
            while (ptr % (numRows - 1) == 0) & (ptr <= n - 1):
                res_inner += s[ptr]
                ptr += space
            while (ptr % (numRows - 1) != 0) & (ptr <= n - 1):
                res_inner += s[ptr]
                new_space = space - 2 * (numRows - n_row)
                ptr += new_space
                if ptr <= n - 1:
                    res_inner += s[ptr]
                ptr += 2 * (numRows - n_row)

            n_row -= 1
            ptr = numRows - n_row
            res += res_inner
        return res


if __name__ == "__main__":
    print("testing result...")
    s = input("Enter a string:")
    numRows = int(input("Enter an int:"))
    print(numRows, len(s))
    res = convert(s, numRows)
    print("Finished")
    print("s:{}\nnumRows:{}\nresult:{}".format(s,
                                               numRows,
                                               res))
