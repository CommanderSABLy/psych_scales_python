from os import system, name

nine_scale = "1 if you very strongly disagree with the statement\n2 if you strongly disagree with the statement\n3 if you moderately disagree with the statement\n4 if you slightly disagree with the statement\n5 if you feel exactly neutral about the statement\n6 if you slightly agree with the statement\n7 if you moderately agree with the statement\n8 if you strongly agree with the statement\n9 if you very strongly agree with the statement\n"

four_scale = "1 if you strongly agree\n2 if you somewhat agree\n3 if you somewhat disagree\n4 if you strongly disagree\n"
all_most_some_not_scale = "1 for all of it\n2 for most\n3 for some\n4 for not much at all\n"
push_speed_scale = "1 for trying to push very much too fast\n2 for going too slowly\n3 for moving at about the right speed\n"

test_options = "Select a test to add to your queue. Tests will only be executed once.\n1) Right-Wing Authoratarianism\n2) Modern Racism Scale\n3) Symbolic Racism Scale\nd) Done adding\n"


def clear():
  # for windows
  if name == 'nt':
    _ = system('cls')
  # for mac and linux(the os.name is 'posix')
  else:
    _ = system('clear')


def question(inquiry: str, scale: str, min: int, max: int) -> int:
  invalid = True
  print("\n\n")
  print(inquiry)
  while invalid:
    temp = input(scale)
    if (temp.isdigit()):
      val = int(temp)
      if val >= min and val <= max:
        invalid = False
      else:
        print("Invalid input. Please try again.")
        print(inquiry)
    else:
      print("Invalid input. Please try again.")
      print(inquiry)
  clear()
  return (val)


def ask(inquiry: str, scale: str, min: int, max: int, weight: int) -> int:
  return weight * question(inquiry, scale, min, max)


def RWA() -> int:
  question_table = [
    "Life imprisonment is justified for certain crimes.",
    "Women should have to promise to obey their husbands when they get married.",
    "The established authorities in our country are usually smarter, better informed, and more competent than others are, and the people can rely on them.",
    "It is important to protect fully the rights of radicals and deviants.",
    "Our country desperately needs a mighty leader who will do what has to be done to destroy the radical new ways and sinfulness that are ruining us.",
    "Gays and lesbians are just as healthy and moral as anybody else.",
    "Our country will be great if we honor the ways of our forefathers, do what the authorities tell us to do, and get rid of the rotten apples who are ruining everything.",
    "Atheists and others who have rebelled against established religion are no doubt every bit as good and virtuous as those who attend church regularly.",
    "The real keys to the good life are obedience, discipline, and sticking to the straight and narrow.",
    "A lot of our rules regarding modesty and sexual behavior are just customs which are not necessarily any better or holier than those which other people follow.",
    "There are many radical, immoral people in our country today who are trying to ruin it for their own godless purposes, whom the authorities should put out of action.",
    "It is always better to trust the judgment of the proper authorities in government and religion than to listen to the noisy rabble-rousers in our society who are trying to create doubt in people's minds.",
    "There is absolutely nothing wrong with nudist camps.",
    "There is no one right way to live your life. Everybody has to create their own way.",
    "Our country will be destroyed someday if we do not smash the perversions eating away at our moral fiber and traditional beliefs.",
    "It's a mistake to stick strictly to the straight and narrow in life, for you'll miss a lot of interesting people from quite different backgrounds who can change you, and some of the best experiences you can have.",
    "The situation in our country is getting so serious, the strongest methods would be justified if they eliminated the troublemakers and got us back to our true path.",
    "It would be best for everyone if the proper authorities censored magazines so that people could not get their hands on trashy and disgusting material.",
    "Everyone should have their own lifestyle, religious beliefs, and sexual preferences, even if it makes them different from everyone else.",
    "A woman's place should be wherever she wants to be. The days when women are submissive to their husbands and social conventions belong strictly in the past.",
    "What our country really needs is a strong, determined leader who will crush evil and take us back to our true path.",
    "People should pay less attention to the Bible and the other old traditional forms of religious guidance and instead develop their own personal standards of what is moral and immoral.",
    "Enough is enough! If the loafers, deviants, and troublemakers won't shape up, then they should be severely disciplined and taught a lesson they'll never forget.",
    "Our country needs freethinkers who will have the courage to defy traditional ways, even if this upsets many people.",
    "There is nothing wrong with premarital sexual intercourse.",
    "It may be considered old-fashioned by some, but having a normal, proper appearance is still the mark of a gentleman and, especially, a lady.",
    "It is wonderful that young people today have greater freedom to protest against things they don't like and to make their own rules to govern their behavior.",
    "What our country really needs, instead of more civil rights, is a good stiff dose of law and order.",
    "Government, judges, and the police should never be allowed to censor books.",
    "Obedience and respect for authority are the most important virtues children should learn.",
    "We should treat protesters and radicals with open arms and open minds, since new ideas are the lifeblood of progressive change.",
    "Once our government leaders and the authorities condemn the dangerous elements in our society, it will be the duty of every patriotic citizen to help stomp out the rot that is poisoning our country from within.",
    "Rules about being well-behaved and respectable should be changed in favor of greater freedom and new ways of living.",
    "The facts on crime, sexual immorality, and recent public disorders all show we have to crack down harder on deviant groups and troublemakers if we are going to save our moral standards and preserve law and order."
  ]
  total = 0
  for i in range(len(question_table)):
    if i < 4:
      total = total + ask(question_table[i], nine_scale, 1, 9, 0)
    elif (i == 5 or i == 7 or i == 9 or i == 12 or i == 13 or i == 15
          or i == 18 or i == 19 or i == 21 or i == 23 or i == 24 or i == 26
          or i == 28 or i == 30 or i == 32):
      total = total + 10 - ask(question_table[i], nine_scale, 1, 9, 1)
    else:
      total = total + ask(question_table[i], nine_scale, 1, 9, 1)

  return (total)


def MRS() -> int:
  question_table = [
    "It is easy to understand the anger of black people in America",
    "Blacks have more influence upon school desegregation plans that they ought to have.",
    "Blacks are getting too demanding in their push for equal rights.",
    "over the past few years blacks have gotten more economically than they deserve.",
    "Over the past few years the government and news media have shown more respect to blacks than they deserve.",
    "Blacks should not push themselves where they're not wanted",
    "Discrimination against blacks is no longer a problem in the United States"
  ]
  total = 0
  for i in range(len(question_table)):
    if i > 0:
      total = total + ask(question_table[i], nine_scale, 1, 9, 1)
    else:
      total = total + 10 + ask(question_table[i], nine_scale, 1, 9, -1)
  return total


def SRS() -> float:
  question_table = [
    "It's really a matter of some people not trying hard enough; if blacks would only try harder they could be just as well off as whites.",
    "Irish, Italian, Jewish and many other minorities overcame prejudice and worked their way. Blacks should do the same.",
    "Some say that black leaders have been trying to push too fast. Others feel that they haven't pushed fast enough. What do you think?",
    "How much of the racial tension that exists in the United States today do you think blacks are responsible for creating?",
    "How much discrimination against blacks do you feel there is in the United States today, limiting their chances to get ahead?",
    "Generations of slavery and discrimination have created conditions that make it difficult for blacks to work their way out of the lower class.",
    "Over the past few years, blacks have gotten less than they deserve.",
    "Over the past few years, blacks have gotten more economically than they deserve."
  ]
  total = 0
  for i in range(len(question_table)):
    if i == 2:
      temp = ask(question_table[i], push_speed_scale, 1, 3, 1)
      if temp == 1:
        total = total + 1
      elif temp == 2:
        total = total + 0
      elif temp == 3:
        total = total + 0.5
      else:
        print("Critical Error in SRS")
    elif i == 0 or i == 1 or i == 3 or i == 7:
      if i != 3:
        total = total + ((4 - ask(question_table[i], four_scale, 1, 4, 1)) / 3)
      else:
        total = total + (
          (4 - ask(question_table[i], all_most_some_not_scale, 1, 4, 1)) / 3)
    elif i == 4:
      total = total + (
        (ask(question_table[i], all_most_some_not_scale, 1, 4, 1) - 1) / 3)
    else:
      total = total + ((ask(question_table[i], four_scale, 1, 4, 1) - 1) / 3)
  return total


def menu():
  test_selections = {"RWA": False, "MRS": False, "SRS": False}
  output_string = ""
  select = ''

  while select != 'd':
    select = input(test_options)
    if select.isdigit():
      if select == '1':
        #add RWA
        test_selections["RWA"] = True
        clear()
      elif select == '2':
        #add MRS
        test_selections["MRS"] = True
        clear()
      elif select == '3':
        test_selections["SRS"] = True
        clear()
      else:
        clear()
        print("Error: invalid input")
    elif select != 'd':
      clear()
      print("Error: invalid input")
    else:
      clear()
  if test_selections["RWA"]:
    score = RWA()
    pscore = 100 * ((score - 30) / 240)
    output_string = output_string + "Your Right-Wing Authoritarianism Score is:\n" + str(
      pscore) + "%\n(Raw: " + str(score) + ")\n"
  if test_selections["MRS"]:
    score = MRS()
    pscore = 100 * ((score - 7) / 56)
    output_string = output_string + "Your Modern Racism Scale Score is:\n" + str(
      pscore) + "%\n(Raw: " + str(score) + ")\n"
  if test_selections["SRS"]:
    score = SRS()
    pscore = 100 * ((score) / 8)
    output_string = output_string + "Your Symbolic Racism Scale Score is:\n" + str(
      pscore) + "%\n(Raw: " + str(score) + ")\n"
  print(output_string)


menu()
