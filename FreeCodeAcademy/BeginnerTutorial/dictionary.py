monthConversions ={
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "Augest",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8:"Augest",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

#print(monthConversions["Nov"])
#print(monthConversions.get("Nov"))
print(monthConversions.get(1, "Not a valid key"))