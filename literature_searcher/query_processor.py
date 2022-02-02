database = {"shakespeare":
            "William Shakespeare (26 April 1564 - 23 April 1616) was an\n"
            "English poet, playwright, and actor, widely regarded as the\n"
            "greatest writer in the English language and the world's\n"
            "pre-eminent dramatist.",
            "asimov":
            "Isaac Asimov (2 January 1920 - 6 April 1992) was an\n"
            "American writer and professor of Biochemistry, famous for\n"
            "his works of hard science fiction and popular science.",
            "darwin":
            "Charles Darwin (12 February 1809 - 19 April 1882) was an\n"
            "English naturalist, geologist and biologist.",
            "dickens":
            "Charles Dickens (7 February 1812 - 9 June 1870) was an\n"
            "English writer and social critic."
            }

def process(query):
    return [val for key, val in database.items() if key in query.lower()]