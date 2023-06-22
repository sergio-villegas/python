"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
- s = "12:01:00PM"
Return '12:01:00'.
- s = "12:01:00AM"
Return '00:01:00'.

Sample
Sample Input: 07:05:45PM
Sample Output: 19:05:45
"""

def timeConversion(s):
    hora = int(s[0] + s[1])

    if s[-2] == "A":
        if hora == 12:
            cadena = str(hora - 12) + "0" + s[slice(2, 8)]
        else:
            cadena = "0" + str(hora) + s[slice(2, 8)]
    elif s[-2] == "P":
        if hora >= 12 or hora < 1:
            cadena = str(hora) + s[slice(2, 8)]
        else:
            cadena = str(hora + 12) + s[slice(2, 8)]
    print(cadena)


if __name__ == "__main__":
    s = str(input())
    timeConversion(s)
