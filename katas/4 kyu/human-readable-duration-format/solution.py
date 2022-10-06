# human-readable-duration-format
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def format_duration(seconds):
  words = ["year", "day", "hour", "minute", "second"]

  if not seconds:
    return "now"
  else:
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)

    time = [y, d, h, m, s]

    duration = []

    for x, i in enumerate(time):
      if i == 1:
        duration.append(f"{i} {words[x]}")
      elif i > 1:
        duration.append(f"{i} {words[x]}s")

    if len(duration) == 1:
      return duration[0]
    elif len(duration) == 2:
      return f"{duration[0]} and {duration[1]}"
    else:
      return ", ".join(duration[:-1]) + " and " + duration[-1]
# ------------------------------ CLEVER SOLUTION ----------------------------- #
times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(format_duration(1), "1 second")
test.assert_equals(format_duration(62), "1 minute and 2 seconds")
test.assert_equals(format_duration(120), "2 minutes")
test.assert_equals(format_duration(3600), "1 hour")
test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")