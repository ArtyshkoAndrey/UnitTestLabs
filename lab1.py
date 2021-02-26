from datetime import datetime

class lab1():
  """docstring for lab1"""
  def lab (self, day, month, day1, month1, year1):
    try:
      upperYear = 0
      format = "%Y-%m-%d"

      base = datetime.strptime(str(year1) + '-' + str(month) + '-' + str(day) , format)

      diff = datetime.strptime(str(year1) + '-' + str(month1) + '-' + str(day1), format) - base

      answer = int(diff.days)

      answer = answer * (-1)


      # return answer
      if answer < 0:
        base = datetime.strptime(str(year1 + 1) + '-' + str(month) + '-' + str(day) , format)
        diff = base - datetime.strptime(str(year1) + '-' + str(month1) + '-' + str(day1), format)
        answer = int(diff.days)

      return answer

    except ValueError as e:
      return None
    


# if __name__ == '__main__':
#   day, month = map(int, input().split())
#   day1, month1, year1 = map(int, input().split())

#   print(lab(day, month, day1, month1, year1))
