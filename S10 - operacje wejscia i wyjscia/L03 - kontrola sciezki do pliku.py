import os
import datetime

data_input = r"D:\Projekty\Kursy Python\Python - Beginner\S10 - operacje wejscia i wyjscia\FOLDER\data_input"
data_output = r"D:\Projekty\Kursy Python\Python - Beginner\S10 - operacje wejscia i wyjscia\FOLDER\data_output"

today = datetime.date.strftime(datetime.date.today(), "%Y-%m-%d")

is_input_ok = os.path.isdir(data_input)
is_output_ok = os.path.isdir(data_output)

is_output_today_ok = not os.path.isdir(
    os.path.join(data_output, today)
) and not os.path.isfile(os.path.join(data_output, today + ".csv"))


if is_input_ok and is_output_ok and is_output_today_ok:
    print("OK")
elif not is_input_ok:
    print("INPUT NOK")
elif not is_output_ok:
    print("OUTPUT NOK")
else:
    print("OUTPUT TODAY NOK")
