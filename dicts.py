month_con = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    0: "Zero"
}

print(month_con)
print(month_con['Jan'])
print(month_con.get('Feb'))
print(month_con.get('Luv'))
print(month_con.get('Luv', "Not a valid key"))
print(month_con.get('Luv', month_con['Jan']))
print(month_con[0])
