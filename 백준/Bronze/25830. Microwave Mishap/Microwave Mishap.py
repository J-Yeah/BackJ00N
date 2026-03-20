m, s = map(int, input().split(":"))
i_time = m * 60 + s
r_time = m * 3600 + s * 60

ans = r_time - i_time

hour = ans // 3600
min = (ans % 3600) // 60
sec = ans % 60
hour_str = str(hour).rjust(2, '0')
min_str = str(min).rjust(2, '0')
sec_str = str(sec).rjust(2, '0')

print(hour_str+":"+min_str+":"+sec_str)