def no_c(my_str):
        m = ["c","C"]
        erase = my_str
        erase ="".join(j for j in erase if j not in m)
        return (erase)

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

